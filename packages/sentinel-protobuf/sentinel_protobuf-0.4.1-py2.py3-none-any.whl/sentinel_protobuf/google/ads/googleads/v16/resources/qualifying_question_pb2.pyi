from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class QualifyingQuestion(_message.Message):
    __slots__ = ('resource_name', 'qualifying_question_id', 'locale', 'text')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUALIFYING_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    qualifying_question_id: int
    locale: str
    text: str

    def __init__(self, resource_name: _Optional[str]=..., qualifying_question_id: _Optional[int]=..., locale: _Optional[str]=..., text: _Optional[str]=...) -> None:
        ...