from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserFeedback(_message.Message):
    __slots__ = ('name', 'free_form_feedback', 'rating')

    class UserFeedbackRating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_FEEDBACK_RATING_UNSPECIFIED: _ClassVar[UserFeedback.UserFeedbackRating]
        POSITIVE: _ClassVar[UserFeedback.UserFeedbackRating]
        NEGATIVE: _ClassVar[UserFeedback.UserFeedbackRating]
    USER_FEEDBACK_RATING_UNSPECIFIED: UserFeedback.UserFeedbackRating
    POSITIVE: UserFeedback.UserFeedbackRating
    NEGATIVE: UserFeedback.UserFeedbackRating
    NAME_FIELD_NUMBER: _ClassVar[int]
    FREE_FORM_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    name: str
    free_form_feedback: str
    rating: UserFeedback.UserFeedbackRating

    def __init__(self, name: _Optional[str]=..., free_form_feedback: _Optional[str]=..., rating: _Optional[_Union[UserFeedback.UserFeedbackRating, str]]=...) -> None:
        ...