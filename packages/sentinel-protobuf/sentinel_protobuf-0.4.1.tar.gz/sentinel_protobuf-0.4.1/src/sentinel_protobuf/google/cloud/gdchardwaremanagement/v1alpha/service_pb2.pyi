from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gdchardwaremanagement.v1alpha import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListOrdersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListOrdersResponse(_message.Message):
    __slots__ = ('orders', 'next_page_token', 'unreachable')
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Order]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, orders: _Optional[_Iterable[_Union[_resources_pb2.Order, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOrderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOrderRequest(_message.Message):
    __slots__ = ('parent', 'order_id', 'order', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    order_id: str
    order: _resources_pb2.Order
    request_id: str

    def __init__(self, parent: _Optional[str]=..., order_id: _Optional[str]=..., order: _Optional[_Union[_resources_pb2.Order, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateOrderRequest(_message.Message):
    __slots__ = ('update_mask', 'order', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    order: _resources_pb2.Order
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order: _Optional[_Union[_resources_pb2.Order, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteOrderRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class SubmitOrderRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SubmitOrderRequest.Type]
        INFO_PENDING: _ClassVar[SubmitOrderRequest.Type]
        INFO_COMPLETE: _ClassVar[SubmitOrderRequest.Type]
    TYPE_UNSPECIFIED: SubmitOrderRequest.Type
    INFO_PENDING: SubmitOrderRequest.Type
    INFO_COMPLETE: SubmitOrderRequest.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    type: SubmitOrderRequest.Type

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., type: _Optional[_Union[SubmitOrderRequest.Type, str]]=...) -> None:
        ...

class ListSitesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSitesResponse(_message.Message):
    __slots__ = ('sites', 'next_page_token', 'unreachable')
    SITES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    sites: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Site]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, sites: _Optional[_Iterable[_Union[_resources_pb2.Site, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSiteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSiteRequest(_message.Message):
    __slots__ = ('parent', 'site_id', 'site', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    site_id: str
    site: _resources_pb2.Site
    request_id: str

    def __init__(self, parent: _Optional[str]=..., site_id: _Optional[str]=..., site: _Optional[_Union[_resources_pb2.Site, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSiteRequest(_message.Message):
    __slots__ = ('update_mask', 'site', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    site: _resources_pb2.Site
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., site: _Optional[_Union[_resources_pb2.Site, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSiteRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListHardwareGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListHardwareGroupsResponse(_message.Message):
    __slots__ = ('hardware_groups', 'next_page_token', 'unreachable')
    HARDWARE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    hardware_groups: _containers.RepeatedCompositeFieldContainer[_resources_pb2.HardwareGroup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, hardware_groups: _Optional[_Iterable[_Union[_resources_pb2.HardwareGroup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetHardwareGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateHardwareGroupRequest(_message.Message):
    __slots__ = ('parent', 'hardware_group_id', 'hardware_group', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hardware_group_id: str
    hardware_group: _resources_pb2.HardwareGroup
    request_id: str

    def __init__(self, parent: _Optional[str]=..., hardware_group_id: _Optional[str]=..., hardware_group: _Optional[_Union[_resources_pb2.HardwareGroup, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateHardwareGroupRequest(_message.Message):
    __slots__ = ('update_mask', 'hardware_group', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    hardware_group: _resources_pb2.HardwareGroup
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., hardware_group: _Optional[_Union[_resources_pb2.HardwareGroup, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteHardwareGroupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListHardwareRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListHardwareResponse(_message.Message):
    __slots__ = ('hardware', 'next_page_token', 'unreachable')
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    hardware: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Hardware]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, hardware: _Optional[_Iterable[_Union[_resources_pb2.Hardware, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetHardwareRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateHardwareRequest(_message.Message):
    __slots__ = ('parent', 'hardware_id', 'hardware')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hardware_id: str
    hardware: _resources_pb2.Hardware

    def __init__(self, parent: _Optional[str]=..., hardware_id: _Optional[str]=..., hardware: _Optional[_Union[_resources_pb2.Hardware, _Mapping]]=...) -> None:
        ...

class UpdateHardwareRequest(_message.Message):
    __slots__ = ('update_mask', 'hardware', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    hardware: _resources_pb2.Hardware
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., hardware: _Optional[_Union[_resources_pb2.Hardware, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteHardwareRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListCommentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCommentsResponse(_message.Message):
    __slots__ = ('comments', 'next_page_token', 'unreachable')
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Comment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, comments: _Optional[_Iterable[_Union[_resources_pb2.Comment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCommentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCommentRequest(_message.Message):
    __slots__ = ('parent', 'comment_id', 'comment', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    comment_id: str
    comment: _resources_pb2.Comment
    request_id: str

    def __init__(self, parent: _Optional[str]=..., comment_id: _Optional[str]=..., comment: _Optional[_Union[_resources_pb2.Comment, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class RecordActionOnCommentRequest(_message.Message):
    __slots__ = ('name', 'action_type')

    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[RecordActionOnCommentRequest.ActionType]
        READ: _ClassVar[RecordActionOnCommentRequest.ActionType]
        UNREAD: _ClassVar[RecordActionOnCommentRequest.ActionType]
    ACTION_TYPE_UNSPECIFIED: RecordActionOnCommentRequest.ActionType
    READ: RecordActionOnCommentRequest.ActionType
    UNREAD: RecordActionOnCommentRequest.ActionType
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    action_type: RecordActionOnCommentRequest.ActionType

    def __init__(self, name: _Optional[str]=..., action_type: _Optional[_Union[RecordActionOnCommentRequest.ActionType, str]]=...) -> None:
        ...

class ListChangeLogEntriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListChangeLogEntriesResponse(_message.Message):
    __slots__ = ('change_log_entries', 'next_page_token', 'unreachable')
    CHANGE_LOG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    change_log_entries: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ChangeLogEntry]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, change_log_entries: _Optional[_Iterable[_Union[_resources_pb2.ChangeLogEntry, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetChangeLogEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSkusRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSkusResponse(_message.Message):
    __slots__ = ('skus', 'next_page_token', 'unreachable')
    SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    skus: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Sku]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, skus: _Optional[_Iterable[_Union[_resources_pb2.Sku, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSkuRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListZonesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListZonesResponse(_message.Message):
    __slots__ = ('zones', 'next_page_token', 'unreachable')
    ZONES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Zone]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, zones: _Optional[_Iterable[_Union[_resources_pb2.Zone, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetZoneRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateZoneRequest(_message.Message):
    __slots__ = ('parent', 'zone_id', 'zone', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    zone_id: str
    zone: _resources_pb2.Zone
    request_id: str

    def __init__(self, parent: _Optional[str]=..., zone_id: _Optional[str]=..., zone: _Optional[_Union[_resources_pb2.Zone, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateZoneRequest(_message.Message):
    __slots__ = ('update_mask', 'zone', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    zone: _resources_pb2.Zone
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., zone: _Optional[_Union[_resources_pb2.Zone, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteZoneRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class SignalZoneStateRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'state_signal', 'provisioning_state_signal')

    class StateSignal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_SIGNAL_UNSPECIFIED: _ClassVar[SignalZoneStateRequest.StateSignal]
        FACTORY_TURNUP_CHECKS_PASSED: _ClassVar[SignalZoneStateRequest.StateSignal]
        READY_FOR_SITE_TURNUP: _ClassVar[SignalZoneStateRequest.StateSignal]
        FACTORY_TURNUP_CHECKS_FAILED: _ClassVar[SignalZoneStateRequest.StateSignal]
    STATE_SIGNAL_UNSPECIFIED: SignalZoneStateRequest.StateSignal
    FACTORY_TURNUP_CHECKS_PASSED: SignalZoneStateRequest.StateSignal
    READY_FOR_SITE_TURNUP: SignalZoneStateRequest.StateSignal
    FACTORY_TURNUP_CHECKS_FAILED: SignalZoneStateRequest.StateSignal

    class ProvisioningStateSignal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_STATE_SIGNAL_UNSPECIFIED: _ClassVar[SignalZoneStateRequest.ProvisioningStateSignal]
        PROVISIONING_IN_PROGRESS: _ClassVar[SignalZoneStateRequest.ProvisioningStateSignal]
        PROVISIONING_COMPLETE: _ClassVar[SignalZoneStateRequest.ProvisioningStateSignal]
    PROVISIONING_STATE_SIGNAL_UNSPECIFIED: SignalZoneStateRequest.ProvisioningStateSignal
    PROVISIONING_IN_PROGRESS: SignalZoneStateRequest.ProvisioningStateSignal
    PROVISIONING_COMPLETE: SignalZoneStateRequest.ProvisioningStateSignal
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_STATE_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    state_signal: SignalZoneStateRequest.StateSignal
    provisioning_state_signal: SignalZoneStateRequest.ProvisioningStateSignal

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., state_signal: _Optional[_Union[SignalZoneStateRequest.StateSignal, str]]=..., provisioning_state_signal: _Optional[_Union[SignalZoneStateRequest.ProvisioningStateSignal, str]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...