from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.commerce.consumer.procurement.v1 import order_pb2 as _order_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoRenewalBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED: _ClassVar[AutoRenewalBehavior]
    AUTO_RENEWAL_BEHAVIOR_ENABLE: _ClassVar[AutoRenewalBehavior]
    AUTO_RENEWAL_BEHAVIOR_DISABLE: _ClassVar[AutoRenewalBehavior]
AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED: AutoRenewalBehavior
AUTO_RENEWAL_BEHAVIOR_ENABLE: AutoRenewalBehavior
AUTO_RENEWAL_BEHAVIOR_DISABLE: AutoRenewalBehavior

class PlaceOrderRequest(_message.Message):
    __slots__ = ('parent', 'display_name', 'line_item_info', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_name: str
    line_item_info: _containers.RepeatedCompositeFieldContainer[_order_pb2.LineItemInfo]
    request_id: str

    def __init__(self, parent: _Optional[str]=..., display_name: _Optional[str]=..., line_item_info: _Optional[_Iterable[_Union[_order_pb2.LineItemInfo, _Mapping]]]=..., request_id: _Optional[str]=...) -> None:
        ...

class PlaceOrderMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOrderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOrdersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListOrdersResponse(_message.Message):
    __slots__ = ('orders', 'next_page_token')
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[_order_pb2.Order]
    next_page_token: str

    def __init__(self, orders: _Optional[_Iterable[_Union[_order_pb2.Order, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ModifyOrderRequest(_message.Message):
    __slots__ = ('name', 'modifications', 'display_name', 'etag')

    class Modification(_message.Message):
        __slots__ = ('line_item_id', 'change_type', 'new_line_item_info', 'auto_renewal_behavior')
        LINE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        NEW_LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
        AUTO_RENEWAL_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        line_item_id: str
        change_type: _order_pb2.LineItemChangeType
        new_line_item_info: _order_pb2.LineItemInfo
        auto_renewal_behavior: AutoRenewalBehavior

        def __init__(self, line_item_id: _Optional[str]=..., change_type: _Optional[_Union[_order_pb2.LineItemChangeType, str]]=..., new_line_item_info: _Optional[_Union[_order_pb2.LineItemInfo, _Mapping]]=..., auto_renewal_behavior: _Optional[_Union[AutoRenewalBehavior, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    modifications: _containers.RepeatedCompositeFieldContainer[ModifyOrderRequest.Modification]
    display_name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., modifications: _Optional[_Iterable[_Union[ModifyOrderRequest.Modification, _Mapping]]]=..., display_name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ModifyOrderMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CancelOrderRequest(_message.Message):
    __slots__ = ('name', 'etag', 'cancellation_policy')

    class CancellationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CANCELLATION_POLICY_UNSPECIFIED: _ClassVar[CancelOrderRequest.CancellationPolicy]
        CANCELLATION_POLICY_CANCEL_IMMEDIATELY: _ClassVar[CancelOrderRequest.CancellationPolicy]
        CANCELLATION_POLICY_CANCEL_AT_TERM_END: _ClassVar[CancelOrderRequest.CancellationPolicy]
    CANCELLATION_POLICY_UNSPECIFIED: CancelOrderRequest.CancellationPolicy
    CANCELLATION_POLICY_CANCEL_IMMEDIATELY: CancelOrderRequest.CancellationPolicy
    CANCELLATION_POLICY_CANCEL_AT_TERM_END: CancelOrderRequest.CancellationPolicy
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    cancellation_policy: CancelOrderRequest.CancellationPolicy

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., cancellation_policy: _Optional[_Union[CancelOrderRequest.CancellationPolicy, str]]=...) -> None:
        ...

class CancelOrderMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...