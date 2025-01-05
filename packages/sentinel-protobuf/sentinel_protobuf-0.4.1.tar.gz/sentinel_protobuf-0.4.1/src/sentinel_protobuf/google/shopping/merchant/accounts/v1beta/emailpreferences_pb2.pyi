from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EmailPreferences(_message.Message):
    __slots__ = ('name', 'news_and_tips')

    class OptInState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPT_IN_STATE_UNSPECIFIED: _ClassVar[EmailPreferences.OptInState]
        OPTED_OUT: _ClassVar[EmailPreferences.OptInState]
        OPTED_IN: _ClassVar[EmailPreferences.OptInState]
        UNCONFIRMED: _ClassVar[EmailPreferences.OptInState]
    OPT_IN_STATE_UNSPECIFIED: EmailPreferences.OptInState
    OPTED_OUT: EmailPreferences.OptInState
    OPTED_IN: EmailPreferences.OptInState
    UNCONFIRMED: EmailPreferences.OptInState
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEWS_AND_TIPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    news_and_tips: EmailPreferences.OptInState

    def __init__(self, name: _Optional[str]=..., news_and_tips: _Optional[_Union[EmailPreferences.OptInState, str]]=...) -> None:
        ...

class GetEmailPreferencesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateEmailPreferencesRequest(_message.Message):
    __slots__ = ('email_preferences', 'update_mask')
    EMAIL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    email_preferences: EmailPreferences
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, email_preferences: _Optional[_Union[EmailPreferences, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...