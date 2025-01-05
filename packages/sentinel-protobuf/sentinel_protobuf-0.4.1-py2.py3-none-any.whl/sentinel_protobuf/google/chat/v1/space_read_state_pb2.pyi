from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SpaceReadState(_message.Message):
    __slots__ = ('name', 'last_read_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    last_read_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., last_read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetSpaceReadStateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSpaceReadStateRequest(_message.Message):
    __slots__ = ('space_read_state', 'update_mask')
    SPACE_READ_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    space_read_state: SpaceReadState
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, space_read_state: _Optional[_Union[SpaceReadState, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...