from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Billing(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_UNSPECIFIED: _ClassVar[Billing]
    PAY_AS_YOU_GO: _ClassVar[Billing]
    ANTHOS_LICENSE: _ClassVar[Billing]
BILLING_UNSPECIFIED: Billing
PAY_AS_YOU_GO: Billing
ANTHOS_LICENSE: Billing

class FeatureSpec(_message.Message):
    __slots__ = ('config_membership', 'billing')
    CONFIG_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    BILLING_FIELD_NUMBER: _ClassVar[int]
    config_membership: str
    billing: Billing

    def __init__(self, config_membership: _Optional[str]=..., billing: _Optional[_Union[Billing, str]]=...) -> None:
        ...