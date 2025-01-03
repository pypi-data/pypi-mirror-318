import csv
import io

from trio.abc import ReceiveStream, SendStream

from kabomu.abstractions import DefaultQuasiHttpResponse,\
    DefaultQuasiHttpRequest
from kabomu.quasi_http_utils import _get_optional_attr
from kabomu.tlv import tlv_utils
from kabomu import misc_utils_internal, io_utils_internal, quasi_http_utils
from kabomu.errors import IllegalArgumentError, ExpectationViolationError,\
    MissingDependencyError,\
    QuasiHttpError,\
    QUASI_HTTP_ERROR_REASON_GENERAL,\
    QUASI_HTTP_ERROR_REASON_TIMEOUT,\
    QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,\
    QUASI_HTTP_ERROR_REASON_MESSAGE_LENGTH_LIMIT_EXCEEDED

async def run_timeout_scheduler(
        connection, for_client, proc):
    if not hasattr(connection, "schedule_timeout"):
        return
    result = await connection.schedule_timeout(proc)
    if result is None:
        return
    error = _get_optional_attr(result, "error")
    if error:
        raise error
    if _get_optional_attr(result, "timeout"):
        timeout_msg = "send timeout" if for_client else "receive timeout"
        raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_TIMEOUT,
            timeout_msg)

    if for_client:
        response = _get_optional_attr(result, "response")
        if response is None:
            raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_GENERAL,
                "no response from timeout scheduler")
        return response
    else:
        return True

def validate_http_header_section(is_response, csv_data):
    if not csv_data:
        raise ExpectationViolationError(
            "expected csv to contain at least the special header")
    special_header = csv_data[0]
    if len(special_header) != 4:
        raise ExpectationViolationError(
            "expected special header to have 4 values " +
            f"instead of {len(special_header)}")
    error_tag = "status" if is_response else "request"
    for i in range(len(special_header)):
        item = special_header[i]
        if not contains_only_printable_ascii_chars(
                item, is_response and i == 2):
            raise QuasiHttpError(
                QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                    f"quasi http {error_tag} line " +
                    "field contains spaces, newlines or " +
                    "non-printable ASCII characters: " +
                    item)
    for row in csv_data[1:]:
        if len(row) < 2:
            raise ExpectationViolationError(
                "expected row to have at least 2 values " +
                f"instead of {len(row)}")
        header_name = row[0]
        if not contains_only_header_name_chars(header_name):
            raise QuasiHttpError(
                QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                    "quasi http header name contains characters " +
                    "other than hyphen and English alphabets: " +
                    header_name)
        for header_value in row[1:]:
            if not contains_only_printable_ascii_chars(header_value, True):
                raise QuasiHttpError(
                    QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                        "quasi http header value contains newlines or " +
                        "non-printable ASCII characters: " +
                        header_value)

def contains_only_header_name_chars(v):
    for c in v:
        c = ord(c)
        if c >= 48 and c < 58:
            # digits.
            pass
        elif c >= 65 and c < 91:
            # upper case
            pass
        elif c >= 97 and c < 123:
            # lower case
            pass
        elif c == 45:
            # hyphen
            pass
        else:
            return False
    return True

def contains_only_printable_ascii_chars(v, allow_space):
    for c in v:
        c = ord(c)
        if c < 32 or c > 126:
            return False
        if not allow_space and c == 32:
            return False
    return True

def encode_quasi_http_headers(is_response, req_or_status_line,
                              remaining_headers):
    if not req_or_status_line:
        raise IllegalArgumentError("req_or_status_line argument is null")
    csv_data = []
    special_header = []
    for v in req_or_status_line:
        special_header.append('' if v is None else str(v))
    csv_data.append(special_header)
    if remaining_headers:
        for header_name, header_value in remaining_headers.items():
            header_name = '' if header_name is None else str(header_name)
            if not header_name:
                raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                    "quasi http header name cannot be empty")
            # allow string values not inside an array.
            if type(header_value) == str:
                header_value = [header_value]
            if header_value is None or not len(header_value):
                continue
            header_row = [header_name]
            for v in header_value:
                v = "" if v is None else str(v)
                if not v:
                    raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                        "quasi http header value cannot be empty")
                header_row.append(v)
            csv_data.append(header_row)

    validate_http_header_section(is_response, csv_data)

    with io.StringIO(newline='') as serialized:
        for row in csv_data:
            add_comma = False
            for col in row:
                if add_comma:
                    serialized.write(',')
                serialized.write('"' + col.replace('"', '""') + '"')
                add_comma = True
            serialized.write('\n')
        return misc_utils_internal.string_to_bytes(
            serialized.getvalue())
    
def decode_quasi_http_headers(is_response, buffer,
                              headers_receiver):
    csv_data = []
    try:
        with io.StringIO(misc_utils_internal.bytes_to_string(
                buffer)) as s:
            deserializer = csv.reader(s,strict=True)
            for row in deserializer:
                csv_data.append(row)
    except Exception as ex:
        quasiHttpEx = QuasiHttpError(
            QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
            "invalid quasi http headers")
        quasiHttpEx.__cause__ = ex
        raise quasiHttpEx
    if not csv_data:
        raise QuasiHttpError(
            QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
            "invalid quasi http headers")
    
    error_tag = "status" if is_response else "request"
    special_header = csv_data[0]
    if len(special_header) < 4:
        raise QuasiHttpError(
            QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
            f"invalid quasi http {error_tag} line")
    for header_row in csv_data[1:]:
        if len(header_row) < 2:
            continue
        # merge headers with the same normalized name in different rows.
        header_name = header_row[0].lower()
        if header_name not in headers_receiver:
            headers_receiver[header_name] = []
        header_value = header_row[1:]
        headers_receiver[header_name].extend(header_value)
    return special_header

async def write_quasi_http_headers(
        is_response, dest: SendStream, req_or_status_line,
        remaining_headers, max_headers_size):
    encoded_headers = encode_quasi_http_headers(
        is_response, req_or_status_line, remaining_headers)
    if not max_headers_size or max_headers_size < 0:
        max_headers_size = quasi_http_utils.DEFAULT_MAX_HEADERS_SIZE

    # finally check that byte count of csv doesn't exceed limit.
    if len(encoded_headers) > max_headers_size:
        msg_suffix = f"{len(encoded_headers)} > {max_headers_size}"
        raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_MESSAGE_LENGTH_LIMIT_EXCEEDED,
            f"quasi http headers exceed max size ({msg_suffix})")

    tag_and_len = tlv_utils.encode_tag_and_length(
        tlv_utils.TAG_FOR_QUASI_HTTP_HEADERS,
        len(encoded_headers))
    await dest.send_all(tag_and_len)
    await dest.send_all(encoded_headers)

async def read_quasi_http_headers(
        is_response, src: ReceiveStream,
        headers_receiver, max_headers_size):
    encoded_tag = await io_utils_internal.read_bytes_fully(src, 4)
    tag = tlv_utils.decode_tag(encoded_tag, 0)
    if tag != tlv_utils.TAG_FOR_QUASI_HTTP_HEADERS:
        raise QuasiHttpError(
            QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
            f"unexpected quasi http headers tag: ${tag}")

    if not max_headers_size or max_headers_size < 0:
        max_headers_size = quasi_http_utils.DEFAULT_MAX_HEADERS_SIZE
    encoded_len = await io_utils_internal.read_bytes_fully(src, 4)
    headers_size = tlv_utils.decode_length(encoded_len, 0)
    if headers_size > max_headers_size:
        msg_suffix = f"{headers_size} > {max_headers_size}"
        raise QuasiHttpError(QUASI_HTTP_ERROR_REASON_MESSAGE_LENGTH_LIMIT_EXCEEDED,
            f"quasi http headers exceed max size ({msg_suffix})")
    encoded_headers = await io_utils_internal.read_bytes_fully(
        src, headers_size)
    return decode_quasi_http_headers(is_response, encoded_headers,
        headers_receiver)

async def write_entity_to_transport(
        is_response, entity, writable_stream: SendStream,
        connection):
    if not writable_stream:
        raise MissingDependencyError("no writable stream found for transport")
    if is_response:
        response = entity
        headers = _get_optional_attr(response, "headers")
        body = _get_optional_attr(response, "body")
        content_length = _get_optional_attr(response, "content_length")
        if not content_length:
            content_length = 0
        status_code = _get_optional_attr(response, "status_code")
        if not status_code:
            status_code = 0
        req_or_status_line = []
        req_or_status_line.append(
            _get_optional_attr(response, "http_version"))
        req_or_status_line.append(status_code)
        req_or_status_line.append(
            _get_optional_attr(response, "http_status_message"))
        req_or_status_line.append(content_length)
    else:
        request = entity
        headers = _get_optional_attr(request, "headers")
        body = _get_optional_attr(request, "body")
        content_length = _get_optional_attr(request, "content_length")
        if not content_length:
            content_length = 0
        req_or_status_line = []
        req_or_status_line.append(
            _get_optional_attr(request, "http_method"))
        req_or_status_line.append(
            _get_optional_attr(request, "target"))
        req_or_status_line.append(
            _get_optional_attr(request, "http_version"))
        req_or_status_line.append(content_length)
    # treat content lengths totally separate from body
    # due to how HEAD method works.
    max_headers_size = _get_optional_attr(
        connection, "processing_options", "max_headers_size")
    await write_quasi_http_headers(is_response,
        writable_stream, req_or_status_line, headers,
        max_headers_size)
    if not body:
        # don't proceed, even if content length is not zero.
        return
    if content_length > 0:
        # don't enforce positive content lengths when writing out
        # quasi http bodies
        await io_utils_internal.copy(body, writable_stream)
    else:
        # proceed, even if content length is 0.
        body_writer = tlv_utils.create_tlv_encoding_writable_stream(
            writable_stream, tlv_utils.TAG_FOR_QUASI_HTTP_BODY_CHUNK)
        await io_utils_internal.copy(body, body_writer)
        await body_writer.send_eof()

async def read_entity_from_transport(
        is_response, readable_stream: ReceiveStream, connection):
    if not readable_stream:
        raise MissingDependencyError("no readable stream found for transport")
    headers_receiver = {}
    processing_options = _get_optional_attr(
        connection, "processing_options")
    max_headers_size = _get_optional_attr(
        processing_options, "max_headers_size")
    req_or_status_line = await read_quasi_http_headers(
        is_response, readable_stream, headers_receiver,
        max_headers_size)
    error_tag = 'response' if is_response else 'request'
    try:
        content_length = misc_utils_internal.parse_int_48(
            req_or_status_line[3])
    except Exception as ex:
        quasi_ex = QuasiHttpError(QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
            f"invalid quasi http {error_tag} content length")
        quasi_ex.__cause__ = ex
        raise quasi_ex
    body = None
    if content_length:
        if content_length > 0:
            body = tlv_utils.create_content_length_enforcing_stream(
                readable_stream, content_length)
        else:
            body = tlv_utils.create_tlv_decoding_readable_stream(
                readable_stream,
                tlv_utils.TAG_FOR_QUASI_HTTP_BODY_CHUNK,
                tlv_utils.TAG_FOR_QUASI_HTTP_BODY_CHUNK_EXT)
    if is_response:
        response = DefaultQuasiHttpResponse()
        response.http_version = req_or_status_line[0]
        try:
            response.status_code = misc_utils_internal.parse_int_32(
                req_or_status_line[1])
        except Exception as ex:
            quasi_ex = QuasiHttpError(QUASI_HTTP_ERROR_REASON_PROTOCOL_VIOLATION,
                "invalid quasi http response status code")
            quasi_ex.__cause__ = ex
            raise quasi_ex
        response.http_status_message = req_or_status_line[2]
        response.content_length = content_length
        response.headers = headers_receiver
        if body:
            body_size_limit = None
            if processing_options:
                body_size_limit = _get_optional_attr(
                    processing_options, "max_response_body_size")
                if not body_size_limit or body_size_limit > 0:
                    body = tlv_utils.create_max_length_enforcing_stream(
                        body, body_size_limit)
        response.body = body
        return response
    else:
        request = DefaultQuasiHttpRequest()
        request.environment = _get_optional_attr(
            connection, "environment")
        request.http_method = req_or_status_line[0]
        request.target = req_or_status_line[1]
        request.http_version = req_or_status_line[2]
        request.content_length = content_length
        request.headers = headers_receiver
        request.body = body
        return request
