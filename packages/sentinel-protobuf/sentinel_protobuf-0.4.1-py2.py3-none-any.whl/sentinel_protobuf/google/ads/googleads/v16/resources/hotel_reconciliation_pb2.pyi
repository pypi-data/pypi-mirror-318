from google.ads.googleads.v16.enums import hotel_reconciliation_status_pb2 as _hotel_reconciliation_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HotelReconciliation(_message.Message):
    __slots__ = ('resource_name', 'commission_id', 'order_id', 'campaign', 'hotel_center_id', 'hotel_id', 'check_in_date', 'check_out_date', 'reconciled_value_micros', 'billed', 'status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    RECONCILED_VALUE_MICROS_FIELD_NUMBER: _ClassVar[int]
    BILLED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    commission_id: str
    order_id: str
    campaign: str
    hotel_center_id: int
    hotel_id: str
    check_in_date: str
    check_out_date: str
    reconciled_value_micros: int
    billed: bool
    status: _hotel_reconciliation_status_pb2.HotelReconciliationStatusEnum.HotelReconciliationStatus

    def __init__(self, resource_name: _Optional[str]=..., commission_id: _Optional[str]=..., order_id: _Optional[str]=..., campaign: _Optional[str]=..., hotel_center_id: _Optional[int]=..., hotel_id: _Optional[str]=..., check_in_date: _Optional[str]=..., check_out_date: _Optional[str]=..., reconciled_value_micros: _Optional[int]=..., billed: bool=..., status: _Optional[_Union[_hotel_reconciliation_status_pb2.HotelReconciliationStatusEnum.HotelReconciliationStatus, str]]=...) -> None:
        ...