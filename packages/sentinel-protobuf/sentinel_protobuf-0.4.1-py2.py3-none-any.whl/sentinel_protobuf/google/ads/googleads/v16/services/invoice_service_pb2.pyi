from google.ads.googleads.v16.enums import month_of_year_pb2 as _month_of_year_pb2
from google.ads.googleads.v16.resources import invoice_pb2 as _invoice_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListInvoicesRequest(_message.Message):
    __slots__ = ("customer_id", "billing_setup", "issue_year", "issue_month")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_SETUP_FIELD_NUMBER: _ClassVar[int]
    ISSUE_YEAR_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MONTH_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    billing_setup: str
    issue_year: str
    issue_month: _month_of_year_pb2.MonthOfYearEnum.MonthOfYear
    def __init__(self, customer_id: _Optional[str] = ..., billing_setup: _Optional[str] = ..., issue_year: _Optional[str] = ..., issue_month: _Optional[_Union[_month_of_year_pb2.MonthOfYearEnum.MonthOfYear, str]] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ("invoices",)
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_invoice_pb2.Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[_invoice_pb2.Invoice, _Mapping]]] = ...) -> None: ...
