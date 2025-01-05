from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationExtensionTargetingCriterionFieldEnum(_message.Message):
    __slots__ = ()

    class LocationExtensionTargetingCriterionField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        UNKNOWN: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        ADDRESS_LINE_1: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        ADDRESS_LINE_2: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        CITY: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        PROVINCE: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        POSTAL_CODE: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
        COUNTRY_CODE: _ClassVar[LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField]
    UNSPECIFIED: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    UNKNOWN: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    ADDRESS_LINE_1: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    ADDRESS_LINE_2: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    CITY: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    PROVINCE: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    POSTAL_CODE: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    COUNTRY_CODE: LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField

    def __init__(self) -> None:
        ...