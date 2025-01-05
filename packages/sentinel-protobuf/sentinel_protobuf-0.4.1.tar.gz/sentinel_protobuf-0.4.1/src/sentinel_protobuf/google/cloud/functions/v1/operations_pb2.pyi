from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_UNSPECIFIED: _ClassVar[OperationType]
    CREATE_FUNCTION: _ClassVar[OperationType]
    UPDATE_FUNCTION: _ClassVar[OperationType]
    DELETE_FUNCTION: _ClassVar[OperationType]
OPERATION_UNSPECIFIED: OperationType
CREATE_FUNCTION: OperationType
UPDATE_FUNCTION: OperationType
DELETE_FUNCTION: OperationType

class OperationMetadataV1(_message.Message):
    __slots__ = ('target', 'type', 'request', 'version_id', 'update_time', 'build_id', 'source_token', 'build_name')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BUILD_NAME_FIELD_NUMBER: _ClassVar[int]
    target: str
    type: OperationType
    request: _any_pb2.Any
    version_id: int
    update_time: _timestamp_pb2.Timestamp
    build_id: str
    source_token: str
    build_name: str

    def __init__(self, target: _Optional[str]=..., type: _Optional[_Union[OperationType, str]]=..., request: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., version_id: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., build_id: _Optional[str]=..., source_token: _Optional[str]=..., build_name: _Optional[str]=...) -> None:
        ...