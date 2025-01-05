from google.ads.admanager.v1 import applied_label_pb2 as _applied_label_pb2
from google.ads.admanager.v1 import custom_field_value_pb2 as _custom_field_value_pb2
from google.ads.admanager.v1 import order_enums_pb2 as _order_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ("name", "order_id", "display_name", "programmatic", "trafficker", "advertiser_contacts", "advertiser", "agency_contacts", "agency", "applied_teams", "effective_teams", "creator", "currency_code", "start_time", "end_time", "unlimited_end_time", "external_order_id", "archived", "last_modified_by_app", "update_time", "notes", "po_number", "status", "salesperson", "secondary_salespeople", "secondary_traffickers", "applied_labels", "effective_applied_labels", "custom_field_values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMATIC_FIELD_NUMBER: _ClassVar[int]
    TRAFFICKER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_FIELD_NUMBER: _ClassVar[int]
    AGENCY_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    APPLIED_TEAMS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TEAMS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UNLIMITED_END_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_APP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PO_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_SALESPEOPLE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_TRAFFICKERS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    order_id: int
    display_name: str
    programmatic: bool
    trafficker: str
    advertiser_contacts: _containers.RepeatedScalarFieldContainer[str]
    advertiser: str
    agency_contacts: _containers.RepeatedScalarFieldContainer[str]
    agency: str
    applied_teams: _containers.RepeatedScalarFieldContainer[str]
    effective_teams: _containers.RepeatedScalarFieldContainer[str]
    creator: str
    currency_code: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    unlimited_end_time: bool
    external_order_id: int
    archived: bool
    last_modified_by_app: str
    update_time: _timestamp_pb2.Timestamp
    notes: str
    po_number: str
    status: _order_enums_pb2.OrderStatusEnum.OrderStatus
    salesperson: str
    secondary_salespeople: _containers.RepeatedScalarFieldContainer[str]
    secondary_traffickers: _containers.RepeatedScalarFieldContainer[str]
    applied_labels: _containers.RepeatedCompositeFieldContainer[_applied_label_pb2.AppliedLabel]
    effective_applied_labels: _containers.RepeatedCompositeFieldContainer[_applied_label_pb2.AppliedLabel]
    custom_field_values: _containers.RepeatedCompositeFieldContainer[_custom_field_value_pb2.CustomFieldValue]
    def __init__(self, name: _Optional[str] = ..., order_id: _Optional[int] = ..., display_name: _Optional[str] = ..., programmatic: bool = ..., trafficker: _Optional[str] = ..., advertiser_contacts: _Optional[_Iterable[str]] = ..., advertiser: _Optional[str] = ..., agency_contacts: _Optional[_Iterable[str]] = ..., agency: _Optional[str] = ..., applied_teams: _Optional[_Iterable[str]] = ..., effective_teams: _Optional[_Iterable[str]] = ..., creator: _Optional[str] = ..., currency_code: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., unlimited_end_time: bool = ..., external_order_id: _Optional[int] = ..., archived: bool = ..., last_modified_by_app: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., po_number: _Optional[str] = ..., status: _Optional[_Union[_order_enums_pb2.OrderStatusEnum.OrderStatus, str]] = ..., salesperson: _Optional[str] = ..., secondary_salespeople: _Optional[_Iterable[str]] = ..., secondary_traffickers: _Optional[_Iterable[str]] = ..., applied_labels: _Optional[_Iterable[_Union[_applied_label_pb2.AppliedLabel, _Mapping]]] = ..., effective_applied_labels: _Optional[_Iterable[_Union[_applied_label_pb2.AppliedLabel, _Mapping]]] = ..., custom_field_values: _Optional[_Iterable[_Union[_custom_field_value_pb2.CustomFieldValue, _Mapping]]] = ...) -> None: ...
