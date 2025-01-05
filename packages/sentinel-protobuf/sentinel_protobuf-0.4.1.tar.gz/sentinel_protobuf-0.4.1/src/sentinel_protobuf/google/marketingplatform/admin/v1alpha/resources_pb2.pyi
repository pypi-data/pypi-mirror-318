from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LinkVerificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_VERIFICATION_STATE_UNSPECIFIED: _ClassVar[LinkVerificationState]
    LINK_VERIFICATION_STATE_VERIFIED: _ClassVar[LinkVerificationState]
    LINK_VERIFICATION_STATE_NOT_VERIFIED: _ClassVar[LinkVerificationState]
LINK_VERIFICATION_STATE_UNSPECIFIED: LinkVerificationState
LINK_VERIFICATION_STATE_VERIFIED: LinkVerificationState
LINK_VERIFICATION_STATE_NOT_VERIFIED: LinkVerificationState

class Organization(_message.Message):
    __slots__ = ('name', 'display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class AnalyticsAccountLink(_message.Message):
    __slots__ = ('name', 'analytics_account', 'display_name', 'link_verification_state')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    analytics_account: str
    display_name: str
    link_verification_state: LinkVerificationState

    def __init__(self, name: _Optional[str]=..., analytics_account: _Optional[str]=..., display_name: _Optional[str]=..., link_verification_state: _Optional[_Union[LinkVerificationState, str]]=...) -> None:
        ...