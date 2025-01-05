from google.ads.googleads.v18.resources import account_link_pb2 as _account_link_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccountLinkRequest(_message.Message):
    __slots__ = ("customer_id", "account_link")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LINK_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    account_link: _account_link_pb2.AccountLink
    def __init__(self, customer_id: _Optional[str] = ..., account_link: _Optional[_Union[_account_link_pb2.AccountLink, _Mapping]] = ...) -> None: ...

class CreateAccountLinkResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class MutateAccountLinkRequest(_message.Message):
    __slots__ = ("customer_id", "operation", "partial_failure", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: AccountLinkOperation
    partial_failure: bool
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[AccountLinkOperation, _Mapping]] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...

class AccountLinkOperation(_message.Message):
    __slots__ = ("update_mask", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    update: _account_link_pb2.AccountLink
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., update: _Optional[_Union[_account_link_pb2.AccountLink, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateAccountLinkResponse(_message.Message):
    __slots__ = ("result", "partial_failure_error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    result: MutateAccountLinkResult
    partial_failure_error: _status_pb2.Status
    def __init__(self, result: _Optional[_Union[MutateAccountLinkResult, _Mapping]] = ..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class MutateAccountLinkResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
