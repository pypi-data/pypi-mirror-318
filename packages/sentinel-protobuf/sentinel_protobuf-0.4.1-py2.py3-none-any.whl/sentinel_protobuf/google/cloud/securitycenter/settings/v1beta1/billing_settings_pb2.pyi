from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BillingTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_TIER_UNSPECIFIED: _ClassVar[BillingTier]
    STANDARD: _ClassVar[BillingTier]
    PREMIUM: _ClassVar[BillingTier]

class BillingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_TYPE_UNSPECIFIED: _ClassVar[BillingType]
    SUBSCRIPTION: _ClassVar[BillingType]
    TRIAL_SUBSCRIPTION: _ClassVar[BillingType]
    ALPHA: _ClassVar[BillingType]
BILLING_TIER_UNSPECIFIED: BillingTier
STANDARD: BillingTier
PREMIUM: BillingTier
BILLING_TYPE_UNSPECIFIED: BillingType
SUBSCRIPTION: BillingType
TRIAL_SUBSCRIPTION: BillingType
ALPHA: BillingType

class BillingSettings(_message.Message):
    __slots__ = ('billing_tier', 'billing_type', 'start_time', 'expire_time')
    BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    BILLING_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    billing_tier: BillingTier
    billing_type: BillingType
    start_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, billing_tier: _Optional[_Union[BillingTier, str]]=..., billing_type: _Optional[_Union[BillingType, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...