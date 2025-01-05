from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RuntimeEvent(_message.Message):
    __slots__ = ('type', 'details')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[RuntimeEvent.EventType]
        RUNTIME_STATE_CHANGE_EVENT: _ClassVar[RuntimeEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: RuntimeEvent.EventType
    RUNTIME_STATE_CHANGE_EVENT: RuntimeEvent.EventType

    class DetailsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    type: RuntimeEvent.EventType
    details: _containers.ScalarMap[str, str]

    def __init__(self, type: _Optional[_Union[RuntimeEvent.EventType, str]]=..., details: _Optional[_Mapping[str, str]]=...) -> None:
        ...