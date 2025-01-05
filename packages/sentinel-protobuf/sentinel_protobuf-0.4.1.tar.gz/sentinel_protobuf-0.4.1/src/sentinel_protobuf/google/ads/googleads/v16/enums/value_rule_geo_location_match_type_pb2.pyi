from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ValueRuleGeoLocationMatchTypeEnum(_message.Message):
    __slots__ = ()

    class ValueRuleGeoLocationMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType]
        UNKNOWN: _ClassVar[ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType]
        ANY: _ClassVar[ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType]
        LOCATION_OF_PRESENCE: _ClassVar[ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType]
    UNSPECIFIED: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    UNKNOWN: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    ANY: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    LOCATION_OF_PRESENCE: ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType

    def __init__(self) -> None:
        ...