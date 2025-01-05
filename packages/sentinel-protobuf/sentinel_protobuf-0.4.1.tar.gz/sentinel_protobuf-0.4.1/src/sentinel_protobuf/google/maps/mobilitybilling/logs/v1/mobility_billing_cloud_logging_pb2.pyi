from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ReportBillableEventLog(_message.Message):
    __slots__ = ('billable_event_id', 'region_code', 'related_ids')
    BILLABLE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    RELATED_IDS_FIELD_NUMBER: _ClassVar[int]
    billable_event_id: str
    region_code: str
    related_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, billable_event_id: _Optional[str]=..., region_code: _Optional[str]=..., related_ids: _Optional[_Iterable[str]]=...) -> None:
        ...