from google.ads.googleads.v18.resources import payments_account_pb2 as _payments_account_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPaymentsAccountsRequest(_message.Message):
    __slots__ = ("customer_id",)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class ListPaymentsAccountsResponse(_message.Message):
    __slots__ = ("payments_accounts",)
    PAYMENTS_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    payments_accounts: _containers.RepeatedCompositeFieldContainer[_payments_account_pb2.PaymentsAccount]
    def __init__(self, payments_accounts: _Optional[_Iterable[_Union[_payments_account_pb2.PaymentsAccount, _Mapping]]] = ...) -> None: ...
