from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataqna.v1alpha import question_pb2 as _question_pb2
from google.cloud.dataqna.v1alpha import user_feedback_pb2 as _user_feedback_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetQuestionRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CreateQuestionRequest(_message.Message):
    __slots__ = ('parent', 'question')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    question: _question_pb2.Question

    def __init__(self, parent: _Optional[str]=..., question: _Optional[_Union[_question_pb2.Question, _Mapping]]=...) -> None:
        ...

class ExecuteQuestionRequest(_message.Message):
    __slots__ = ('name', 'interpretation_index')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTERPRETATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    name: str
    interpretation_index: int

    def __init__(self, name: _Optional[str]=..., interpretation_index: _Optional[int]=...) -> None:
        ...

class GetUserFeedbackRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateUserFeedbackRequest(_message.Message):
    __slots__ = ('user_feedback', 'update_mask')
    USER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user_feedback: _user_feedback_pb2.UserFeedback
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, user_feedback: _Optional[_Union[_user_feedback_pb2.UserFeedback, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...