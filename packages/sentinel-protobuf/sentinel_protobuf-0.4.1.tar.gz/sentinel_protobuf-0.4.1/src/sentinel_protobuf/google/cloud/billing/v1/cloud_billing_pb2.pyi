from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BillingAccount(_message.Message):
    __slots__ = ('name', 'open', 'display_name', 'master_billing_account', 'parent', 'currency_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    open: bool
    display_name: str
    master_billing_account: str
    parent: str
    currency_code: str

    def __init__(self, name: _Optional[str]=..., open: bool=..., display_name: _Optional[str]=..., master_billing_account: _Optional[str]=..., parent: _Optional[str]=..., currency_code: _Optional[str]=...) -> None:
        ...

class ProjectBillingInfo(_message.Message):
    __slots__ = ('name', 'project_id', 'billing_account_name', 'billing_enabled')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    BILLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    billing_account_name: str
    billing_enabled: bool

    def __init__(self, name: _Optional[str]=..., project_id: _Optional[str]=..., billing_account_name: _Optional[str]=..., billing_enabled: bool=...) -> None:
        ...

class GetBillingAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBillingAccountsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'filter', 'parent')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    parent: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class ListBillingAccountsResponse(_message.Message):
    __slots__ = ('billing_accounts', 'next_page_token')
    BILLING_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    billing_accounts: _containers.RepeatedCompositeFieldContainer[BillingAccount]
    next_page_token: str

    def __init__(self, billing_accounts: _Optional[_Iterable[_Union[BillingAccount, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateBillingAccountRequest(_message.Message):
    __slots__ = ('billing_account', 'parent')
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    billing_account: BillingAccount
    parent: str

    def __init__(self, billing_account: _Optional[_Union[BillingAccount, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class UpdateBillingAccountRequest(_message.Message):
    __slots__ = ('name', 'account', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: BillingAccount
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., account: _Optional[_Union[BillingAccount, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListProjectBillingInfoRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProjectBillingInfoResponse(_message.Message):
    __slots__ = ('project_billing_info', 'next_page_token')
    PROJECT_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_billing_info: _containers.RepeatedCompositeFieldContainer[ProjectBillingInfo]
    next_page_token: str

    def __init__(self, project_billing_info: _Optional[_Iterable[_Union[ProjectBillingInfo, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetProjectBillingInfoRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateProjectBillingInfoRequest(_message.Message):
    __slots__ = ('name', 'project_billing_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_billing_info: ProjectBillingInfo

    def __init__(self, name: _Optional[str]=..., project_billing_info: _Optional[_Union[ProjectBillingInfo, _Mapping]]=...) -> None:
        ...

class MoveBillingAccountRequest(_message.Message):
    __slots__ = ('name', 'destination_parent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_parent: str

    def __init__(self, name: _Optional[str]=..., destination_parent: _Optional[str]=...) -> None:
        ...