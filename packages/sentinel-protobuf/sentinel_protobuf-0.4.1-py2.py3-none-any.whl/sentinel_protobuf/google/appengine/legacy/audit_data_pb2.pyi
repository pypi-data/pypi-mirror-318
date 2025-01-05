from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AuditData(_message.Message):
    __slots__ = ('event_message', 'event_data')

    class EventDataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    event_message: str
    event_data: _containers.ScalarMap[str, str]

    def __init__(self, event_message: _Optional[str]=..., event_data: _Optional[_Mapping[str, str]]=...) -> None:
        ...