from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerEvent(_message.Message):
    __slots__ = ('customer', 'event_type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[CustomerEvent.Type]
        PRIMARY_DOMAIN_CHANGED: _ClassVar[CustomerEvent.Type]
        PRIMARY_DOMAIN_VERIFIED: _ClassVar[CustomerEvent.Type]
    TYPE_UNSPECIFIED: CustomerEvent.Type
    PRIMARY_DOMAIN_CHANGED: CustomerEvent.Type
    PRIMARY_DOMAIN_VERIFIED: CustomerEvent.Type
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer: str
    event_type: CustomerEvent.Type

    def __init__(self, customer: _Optional[str]=..., event_type: _Optional[_Union[CustomerEvent.Type, str]]=...) -> None:
        ...

class EntitlementEvent(_message.Message):
    __slots__ = ('entitlement', 'event_type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[EntitlementEvent.Type]
        CREATED: _ClassVar[EntitlementEvent.Type]
        PRICE_PLAN_SWITCHED: _ClassVar[EntitlementEvent.Type]
        COMMITMENT_CHANGED: _ClassVar[EntitlementEvent.Type]
        RENEWED: _ClassVar[EntitlementEvent.Type]
        SUSPENDED: _ClassVar[EntitlementEvent.Type]
        ACTIVATED: _ClassVar[EntitlementEvent.Type]
        CANCELLED: _ClassVar[EntitlementEvent.Type]
        SKU_CHANGED: _ClassVar[EntitlementEvent.Type]
        RENEWAL_SETTING_CHANGED: _ClassVar[EntitlementEvent.Type]
        PAID_SERVICE_STARTED: _ClassVar[EntitlementEvent.Type]
        LICENSE_ASSIGNMENT_CHANGED: _ClassVar[EntitlementEvent.Type]
        LICENSE_CAP_CHANGED: _ClassVar[EntitlementEvent.Type]
    TYPE_UNSPECIFIED: EntitlementEvent.Type
    CREATED: EntitlementEvent.Type
    PRICE_PLAN_SWITCHED: EntitlementEvent.Type
    COMMITMENT_CHANGED: EntitlementEvent.Type
    RENEWED: EntitlementEvent.Type
    SUSPENDED: EntitlementEvent.Type
    ACTIVATED: EntitlementEvent.Type
    CANCELLED: EntitlementEvent.Type
    SKU_CHANGED: EntitlementEvent.Type
    RENEWAL_SETTING_CHANGED: EntitlementEvent.Type
    PAID_SERVICE_STARTED: EntitlementEvent.Type
    LICENSE_ASSIGNMENT_CHANGED: EntitlementEvent.Type
    LICENSE_CAP_CHANGED: EntitlementEvent.Type
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    entitlement: str
    event_type: EntitlementEvent.Type

    def __init__(self, entitlement: _Optional[str]=..., event_type: _Optional[_Union[EntitlementEvent.Type, str]]=...) -> None:
        ...

class SubscriberEvent(_message.Message):
    __slots__ = ('customer_event', 'entitlement_event')
    CUSTOMER_EVENT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    customer_event: CustomerEvent
    entitlement_event: EntitlementEvent

    def __init__(self, customer_event: _Optional[_Union[CustomerEvent, _Mapping]]=..., entitlement_event: _Optional[_Union[EntitlementEvent, _Mapping]]=...) -> None:
        ...