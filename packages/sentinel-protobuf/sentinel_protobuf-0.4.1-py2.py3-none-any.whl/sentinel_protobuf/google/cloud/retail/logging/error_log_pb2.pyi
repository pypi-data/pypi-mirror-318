from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceContext(_message.Message):
    __slots__ = ('service',)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str

    def __init__(self, service: _Optional[str]=...) -> None:
        ...

class HttpRequestContext(_message.Message):
    __slots__ = ('response_status_code',)
    RESPONSE_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    response_status_code: int

    def __init__(self, response_status_code: _Optional[int]=...) -> None:
        ...

class SourceLocation(_message.Message):
    __slots__ = ('function_name',)
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    function_name: str

    def __init__(self, function_name: _Optional[str]=...) -> None:
        ...

class ErrorContext(_message.Message):
    __slots__ = ('http_request', 'report_location')
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    http_request: HttpRequestContext
    report_location: SourceLocation

    def __init__(self, http_request: _Optional[_Union[HttpRequestContext, _Mapping]]=..., report_location: _Optional[_Union[SourceLocation, _Mapping]]=...) -> None:
        ...

class ImportErrorContext(_message.Message):
    __slots__ = ('operation_name', 'gcs_path', 'line_number', 'catalog_item', 'product', 'user_event')
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ITEM_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    operation_name: str
    gcs_path: str
    line_number: str
    catalog_item: str
    product: str
    user_event: str

    def __init__(self, operation_name: _Optional[str]=..., gcs_path: _Optional[str]=..., line_number: _Optional[str]=..., catalog_item: _Optional[str]=..., product: _Optional[str]=..., user_event: _Optional[str]=...) -> None:
        ...

class ErrorLog(_message.Message):
    __slots__ = ('service_context', 'context', 'message', 'status', 'request_payload', 'response_payload', 'import_payload')
    SERVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    service_context: ServiceContext
    context: ErrorContext
    message: str
    status: _status_pb2.Status
    request_payload: _struct_pb2.Struct
    response_payload: _struct_pb2.Struct
    import_payload: ImportErrorContext

    def __init__(self, service_context: _Optional[_Union[ServiceContext, _Mapping]]=..., context: _Optional[_Union[ErrorContext, _Mapping]]=..., message: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., request_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., response_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., import_payload: _Optional[_Union[ImportErrorContext, _Mapping]]=...) -> None:
        ...