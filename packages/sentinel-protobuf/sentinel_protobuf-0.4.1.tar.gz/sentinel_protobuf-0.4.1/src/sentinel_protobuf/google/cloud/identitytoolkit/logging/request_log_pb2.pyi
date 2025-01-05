from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RequestLog(_message.Message):
    __slots__ = ('method_name', 'status', 'request_metadata', 'request', 'response', 'num_response_items', 'metadata')
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NUM_RESPONSE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    method_name: str
    status: _status_pb2.Status
    request_metadata: RequestMetadata
    request: _struct_pb2.Struct
    response: _struct_pb2.Struct
    num_response_items: int
    metadata: _struct_pb2.Struct

    def __init__(self, method_name: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., request_metadata: _Optional[_Union[RequestMetadata, _Mapping]]=..., request: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., response: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., num_response_items: _Optional[int]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class RequestMetadata(_message.Message):
    __slots__ = ('caller_ip', 'caller_supplied_user_agent')
    CALLER_IP_FIELD_NUMBER: _ClassVar[int]
    CALLER_SUPPLIED_USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    caller_ip: str
    caller_supplied_user_agent: str

    def __init__(self, caller_ip: _Optional[str]=..., caller_supplied_user_agent: _Optional[str]=...) -> None:
        ...