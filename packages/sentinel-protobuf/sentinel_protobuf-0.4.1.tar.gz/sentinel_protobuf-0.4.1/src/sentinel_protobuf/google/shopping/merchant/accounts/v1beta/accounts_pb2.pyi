from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.merchant.accounts.v1beta import accountservices_pb2 as _accountservices_pb2
from google.shopping.merchant.accounts.v1beta import user_pb2 as _user_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("name", "account_id", "account_name", "adult_content", "test_account", "time_zone", "language_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ADULT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_id: int
    account_name: str
    adult_content: bool
    test_account: bool
    time_zone: _datetime_pb2.TimeZone
    language_code: str
    def __init__(self, name: _Optional[str] = ..., account_id: _Optional[int] = ..., account_name: _Optional[str] = ..., adult_content: bool = ..., test_account: bool = ..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]] = ..., language_code: _Optional[str] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAndConfigureAccountRequest(_message.Message):
    __slots__ = ("account", "users", "accept_terms_of_service", "service")
    class AcceptTermsOfService(_message.Message):
        __slots__ = ("name", "region_code")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        name: str
        region_code: str
        def __init__(self, name: _Optional[str] = ..., region_code: _Optional[str] = ...) -> None: ...
    class AddAccountService(_message.Message):
        __slots__ = ("account_aggregation", "provider")
        ACCOUNT_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        account_aggregation: _accountservices_pb2.AccountAggregation
        provider: str
        def __init__(self, account_aggregation: _Optional[_Union[_accountservices_pb2.AccountAggregation, _Mapping]] = ..., provider: _Optional[str] = ...) -> None: ...
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_TERMS_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    account: Account
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.CreateUserRequest]
    accept_terms_of_service: CreateAndConfigureAccountRequest.AcceptTermsOfService
    service: _containers.RepeatedCompositeFieldContainer[CreateAndConfigureAccountRequest.AddAccountService]
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., users: _Optional[_Iterable[_Union[_user_pb2.CreateUserRequest, _Mapping]]] = ..., accept_terms_of_service: _Optional[_Union[CreateAndConfigureAccountRequest.AcceptTermsOfService, _Mapping]] = ..., service: _Optional[_Iterable[_Union[CreateAndConfigureAccountRequest.AddAccountService, _Mapping]]] = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("account", "update_mask")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    account: Account
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListAccountsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    next_page_token: str
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListSubAccountsRequest(_message.Message):
    __slots__ = ("provider", "page_size", "page_token")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    provider: str
    page_size: int
    page_token: str
    def __init__(self, provider: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSubAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    next_page_token: str
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
