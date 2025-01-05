from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccountLinking(_message.Message):
    __slots__ = ('enable_account_creation', 'linking_type', 'auth_grant_type', 'app_client_id', 'authorization_url', 'token_url', 'scopes', 'learn_more_url', 'use_basic_auth_header')

    class LinkingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LINKING_TYPE_UNSPECIFIED: _ClassVar[AccountLinking.LinkingType]
        GOOGLE_SIGN_IN: _ClassVar[AccountLinking.LinkingType]
        OAUTH_AND_GOOGLE_SIGN_IN: _ClassVar[AccountLinking.LinkingType]
        OAUTH: _ClassVar[AccountLinking.LinkingType]
    LINKING_TYPE_UNSPECIFIED: AccountLinking.LinkingType
    GOOGLE_SIGN_IN: AccountLinking.LinkingType
    OAUTH_AND_GOOGLE_SIGN_IN: AccountLinking.LinkingType
    OAUTH: AccountLinking.LinkingType

    class AuthGrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTH_GRANT_TYPE_UNSPECIFIED: _ClassVar[AccountLinking.AuthGrantType]
        AUTH_CODE: _ClassVar[AccountLinking.AuthGrantType]
        IMPLICIT: _ClassVar[AccountLinking.AuthGrantType]
    AUTH_GRANT_TYPE_UNSPECIFIED: AccountLinking.AuthGrantType
    AUTH_CODE: AccountLinking.AuthGrantType
    IMPLICIT: AccountLinking.AuthGrantType
    ENABLE_ACCOUNT_CREATION_FIELD_NUMBER: _ClassVar[int]
    LINKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    LEARN_MORE_URL_FIELD_NUMBER: _ClassVar[int]
    USE_BASIC_AUTH_HEADER_FIELD_NUMBER: _ClassVar[int]
    enable_account_creation: bool
    linking_type: AccountLinking.LinkingType
    auth_grant_type: AccountLinking.AuthGrantType
    app_client_id: str
    authorization_url: str
    token_url: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    learn_more_url: str
    use_basic_auth_header: bool

    def __init__(self, enable_account_creation: bool=..., linking_type: _Optional[_Union[AccountLinking.LinkingType, str]]=..., auth_grant_type: _Optional[_Union[AccountLinking.AuthGrantType, str]]=..., app_client_id: _Optional[str]=..., authorization_url: _Optional[str]=..., token_url: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., learn_more_url: _Optional[str]=..., use_basic_auth_header: bool=...) -> None:
        ...