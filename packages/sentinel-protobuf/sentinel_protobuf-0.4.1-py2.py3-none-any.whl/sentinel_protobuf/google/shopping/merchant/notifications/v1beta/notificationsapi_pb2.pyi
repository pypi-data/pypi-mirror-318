from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_UNSPECIFIED: _ClassVar[Resource]
    PRODUCT: _ClassVar[Resource]

class Attribute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ATTRIBUTE_UNSPECIFIED: _ClassVar[Attribute]
    STATUS: _ClassVar[Attribute]
RESOURCE_UNSPECIFIED: Resource
PRODUCT: Resource
ATTRIBUTE_UNSPECIFIED: Attribute
STATUS: Attribute

class GetNotificationSubscriptionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateNotificationSubscriptionRequest(_message.Message):
    __slots__ = ("parent", "notification_subscription")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notification_subscription: NotificationSubscription
    def __init__(self, parent: _Optional[str] = ..., notification_subscription: _Optional[_Union[NotificationSubscription, _Mapping]] = ...) -> None: ...

class UpdateNotificationSubscriptionRequest(_message.Message):
    __slots__ = ("notification_subscription", "update_mask")
    NOTIFICATION_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    notification_subscription: NotificationSubscription
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, notification_subscription: _Optional[_Union[NotificationSubscription, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteNotificationSubscriptionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListNotificationSubscriptionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListNotificationSubscriptionsResponse(_message.Message):
    __slots__ = ("notification_subscriptions", "next_page_token")
    NOTIFICATION_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notification_subscriptions: _containers.RepeatedCompositeFieldContainer[NotificationSubscription]
    next_page_token: str
    def __init__(self, notification_subscriptions: _Optional[_Iterable[_Union[NotificationSubscription, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class NotificationSubscription(_message.Message):
    __slots__ = ("all_managed_accounts", "target_account", "name", "registered_event", "call_back_uri")
    class NotificationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFICATION_EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationSubscription.NotificationEventType]
        PRODUCT_STATUS_CHANGE: _ClassVar[NotificationSubscription.NotificationEventType]
    NOTIFICATION_EVENT_TYPE_UNSPECIFIED: NotificationSubscription.NotificationEventType
    PRODUCT_STATUS_CHANGE: NotificationSubscription.NotificationEventType
    ALL_MANAGED_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_EVENT_FIELD_NUMBER: _ClassVar[int]
    CALL_BACK_URI_FIELD_NUMBER: _ClassVar[int]
    all_managed_accounts: bool
    target_account: str
    name: str
    registered_event: NotificationSubscription.NotificationEventType
    call_back_uri: str
    def __init__(self, all_managed_accounts: bool = ..., target_account: _Optional[str] = ..., name: _Optional[str] = ..., registered_event: _Optional[_Union[NotificationSubscription.NotificationEventType, str]] = ..., call_back_uri: _Optional[str] = ...) -> None: ...

class ProductChange(_message.Message):
    __slots__ = ("old_value", "new_value", "region_code", "reporting_context")
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    old_value: str
    new_value: str
    region_code: str
    reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
    def __init__(self, old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., region_code: _Optional[str] = ..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ...) -> None: ...

class ProductStatusChangeMessage(_message.Message):
    __slots__ = ("account", "managing_account", "resource_type", "attribute", "changes", "resource_id", "resource")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MANAGING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    account: str
    managing_account: str
    resource_type: Resource
    attribute: Attribute
    changes: _containers.RepeatedCompositeFieldContainer[ProductChange]
    resource_id: str
    resource: str
    def __init__(self, account: _Optional[str] = ..., managing_account: _Optional[str] = ..., resource_type: _Optional[_Union[Resource, str]] = ..., attribute: _Optional[_Union[Attribute, str]] = ..., changes: _Optional[_Iterable[_Union[ProductChange, _Mapping]]] = ..., resource_id: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...
