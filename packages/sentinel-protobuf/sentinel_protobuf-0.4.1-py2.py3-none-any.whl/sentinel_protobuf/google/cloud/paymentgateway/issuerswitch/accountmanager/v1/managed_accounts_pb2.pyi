from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ManagedAccount(_message.Message):
    __slots__ = ('name', 'account_reference', 'state', 'balance', 'last_reconciliation_state', 'last_reconciliation_time', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ManagedAccount.State]
        ACTIVE: _ClassVar[ManagedAccount.State]
        DEACTIVATED: _ClassVar[ManagedAccount.State]
    STATE_UNSPECIFIED: ManagedAccount.State
    ACTIVE: ManagedAccount.State
    DEACTIVATED: ManagedAccount.State

    class AccountReconciliationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_RECONCILIATION_STATE_UNSPECIFIED: _ClassVar[ManagedAccount.AccountReconciliationState]
        SUCCEEDED: _ClassVar[ManagedAccount.AccountReconciliationState]
        FAILED: _ClassVar[ManagedAccount.AccountReconciliationState]
    ACCOUNT_RECONCILIATION_STATE_UNSPECIFIED: ManagedAccount.AccountReconciliationState
    SUCCEEDED: ManagedAccount.AccountReconciliationState
    FAILED: ManagedAccount.AccountReconciliationState
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    LAST_RECONCILIATION_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_RECONCILIATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_reference: _common_fields_pb2.AccountReference
    state: ManagedAccount.State
    balance: _money_pb2.Money
    last_reconciliation_state: ManagedAccount.AccountReconciliationState
    last_reconciliation_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., account_reference: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=..., state: _Optional[_Union[ManagedAccount.State, str]]=..., balance: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., last_reconciliation_state: _Optional[_Union[ManagedAccount.AccountReconciliationState, str]]=..., last_reconciliation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ReconcileManagedAccountBalanceRequest(_message.Message):
    __slots__ = ('account', 'expected_balance', 'reference_time')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TIME_FIELD_NUMBER: _ClassVar[int]
    account: ManagedAccount
    expected_balance: _money_pb2.Money
    reference_time: _timestamp_pb2.Timestamp

    def __init__(self, account: _Optional[_Union[ManagedAccount, _Mapping]]=..., expected_balance: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., reference_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchReconcileManagedAccountBalanceRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[ReconcileManagedAccountBalanceRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[ReconcileManagedAccountBalanceRequest, _Mapping]]]=...) -> None:
        ...

class BatchReconcileManagedAccountBalanceResponse(_message.Message):
    __slots__ = ('accounts',)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[ManagedAccount]

    def __init__(self, accounts: _Optional[_Iterable[_Union[ManagedAccount, _Mapping]]]=...) -> None:
        ...

class GetManagedAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...