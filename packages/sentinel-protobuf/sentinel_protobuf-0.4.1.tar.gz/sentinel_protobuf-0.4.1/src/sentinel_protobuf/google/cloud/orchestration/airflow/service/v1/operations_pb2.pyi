from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('state', 'operation_type', 'resource', 'resource_uuid', 'create_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OperationMetadata.State]
        PENDING: _ClassVar[OperationMetadata.State]
        RUNNING: _ClassVar[OperationMetadata.State]
        SUCCEEDED: _ClassVar[OperationMetadata.State]
        SUCCESSFUL: _ClassVar[OperationMetadata.State]
        FAILED: _ClassVar[OperationMetadata.State]
    STATE_UNSPECIFIED: OperationMetadata.State
    PENDING: OperationMetadata.State
    RUNNING: OperationMetadata.State
    SUCCEEDED: OperationMetadata.State
    SUCCESSFUL: OperationMetadata.State
    FAILED: OperationMetadata.State

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[OperationMetadata.Type]
        CREATE: _ClassVar[OperationMetadata.Type]
        DELETE: _ClassVar[OperationMetadata.Type]
        UPDATE: _ClassVar[OperationMetadata.Type]
        CHECK: _ClassVar[OperationMetadata.Type]
        SAVE_SNAPSHOT: _ClassVar[OperationMetadata.Type]
        LOAD_SNAPSHOT: _ClassVar[OperationMetadata.Type]
        DATABASE_FAILOVER: _ClassVar[OperationMetadata.Type]
    TYPE_UNSPECIFIED: OperationMetadata.Type
    CREATE: OperationMetadata.Type
    DELETE: OperationMetadata.Type
    UPDATE: OperationMetadata.Type
    CHECK: OperationMetadata.Type
    SAVE_SNAPSHOT: OperationMetadata.Type
    LOAD_SNAPSHOT: OperationMetadata.Type
    DATABASE_FAILOVER: OperationMetadata.Type
    STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    state: OperationMetadata.State
    operation_type: OperationMetadata.Type
    resource: str
    resource_uuid: str
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[OperationMetadata.State, str]]=..., operation_type: _Optional[_Union[OperationMetadata.Type, str]]=..., resource: _Optional[str]=..., resource_uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...