from google.ads.googleads.v18.resources import account_budget_proposal_pb2 as _account_budget_proposal_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateAccountBudgetProposalRequest(_message.Message):
    __slots__ = ("customer_id", "operation", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: AccountBudgetProposalOperation
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[AccountBudgetProposalOperation, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class AccountBudgetProposalOperation(_message.Message):
    __slots__ = ("update_mask", "create", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _account_budget_proposal_pb2.AccountBudgetProposal
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_account_budget_proposal_pb2.AccountBudgetProposal, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateAccountBudgetProposalResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateAccountBudgetProposalResult
    def __init__(self, result: _Optional[_Union[MutateAccountBudgetProposalResult, _Mapping]] = ...) -> None: ...

class MutateAccountBudgetProposalResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
