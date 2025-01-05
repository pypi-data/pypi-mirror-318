from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RenewalPricePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RENEWAL_PRICE_POLICY_UNSPECIFIED: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_LESSER: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_LESSER_OR_EQUAL: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_EQUAL: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_NOT_EQUAL: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_GREATER: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_IF_GREATER_OR_EQUAL: _ClassVar[RenewalPricePolicy]
    RENEWAL_PRICE_POLICY_ALWAYS: _ClassVar[RenewalPricePolicy]
RENEWAL_PRICE_POLICY_UNSPECIFIED: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_LESSER: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_LESSER_OR_EQUAL: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_EQUAL: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_NOT_EQUAL: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_GREATER: RenewalPricePolicy
RENEWAL_PRICE_POLICY_IF_GREATER_OR_EQUAL: RenewalPricePolicy
RENEWAL_PRICE_POLICY_ALWAYS: RenewalPricePolicy