from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListChildAccountsRequest(_message.Message):
    __slots__ = ("parent", "label_id", "full_name", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    label_id: int
    full_name: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., label_id: _Optional[int] = ..., full_name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListChildAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    next_page_token: str
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("name", "parent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    def __init__(self, name: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class UpdateAccountLabelsRequest(_message.Message):
    __slots__ = ("name", "label_ids", "parent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    label_ids: _containers.RepeatedScalarFieldContainer[int]
    parent: str
    def __init__(self, name: _Optional[str] = ..., label_ids: _Optional[_Iterable[int]] = ..., parent: _Optional[str] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("name", "full_name", "display_name", "homepage_uri", "parent", "label_ids", "automatic_label_ids", "account_type")
    class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_TYPE_UNSPECIFIED: _ClassVar[Account.AccountType]
        CSS_GROUP: _ClassVar[Account.AccountType]
        CSS_DOMAIN: _ClassVar[Account.AccountType]
        MC_PRIMARY_CSS_MCA: _ClassVar[Account.AccountType]
        MC_CSS_MCA: _ClassVar[Account.AccountType]
        MC_MARKETPLACE_MCA: _ClassVar[Account.AccountType]
        MC_OTHER_MCA: _ClassVar[Account.AccountType]
        MC_STANDALONE: _ClassVar[Account.AccountType]
        MC_MCA_SUBACCOUNT: _ClassVar[Account.AccountType]
    ACCOUNT_TYPE_UNSPECIFIED: Account.AccountType
    CSS_GROUP: Account.AccountType
    CSS_DOMAIN: Account.AccountType
    MC_PRIMARY_CSS_MCA: Account.AccountType
    MC_CSS_MCA: Account.AccountType
    MC_MARKETPLACE_MCA: Account.AccountType
    MC_OTHER_MCA: Account.AccountType
    MC_STANDALONE: Account.AccountType
    MC_MCA_SUBACCOUNT: Account.AccountType
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HOMEPAGE_URI_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    display_name: str
    homepage_uri: str
    parent: str
    label_ids: _containers.RepeatedScalarFieldContainer[int]
    automatic_label_ids: _containers.RepeatedScalarFieldContainer[int]
    account_type: Account.AccountType
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ..., display_name: _Optional[str] = ..., homepage_uri: _Optional[str] = ..., parent: _Optional[str] = ..., label_ids: _Optional[_Iterable[int]] = ..., automatic_label_ids: _Optional[_Iterable[int]] = ..., account_type: _Optional[_Union[Account.AccountType, str]] = ...) -> None: ...
