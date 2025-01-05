from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CommonOperationMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CommonOperationMetadata.State]
        RUNNING: _ClassVar[CommonOperationMetadata.State]
        CANCELLING: _ClassVar[CommonOperationMetadata.State]
        SUCCEEDED: _ClassVar[CommonOperationMetadata.State]
        FAILED: _ClassVar[CommonOperationMetadata.State]
        CANCELLED: _ClassVar[CommonOperationMetadata.State]
        PENDING: _ClassVar[CommonOperationMetadata.State]
    STATE_UNSPECIFIED: CommonOperationMetadata.State
    RUNNING: CommonOperationMetadata.State
    CANCELLING: CommonOperationMetadata.State
    SUCCEEDED: CommonOperationMetadata.State
    FAILED: CommonOperationMetadata.State
    CANCELLED: CommonOperationMetadata.State
    PENDING: CommonOperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    state: CommonOperationMetadata.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[CommonOperationMetadata.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...