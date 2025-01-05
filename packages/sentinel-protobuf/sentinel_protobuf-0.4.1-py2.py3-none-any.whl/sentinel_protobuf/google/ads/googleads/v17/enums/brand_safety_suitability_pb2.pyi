from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BrandSafetySuitabilityEnum(_message.Message):
    __slots__ = ()

    class BrandSafetySuitability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BrandSafetySuitabilityEnum.BrandSafetySuitability]
        UNKNOWN: _ClassVar[BrandSafetySuitabilityEnum.BrandSafetySuitability]
        EXPANDED_INVENTORY: _ClassVar[BrandSafetySuitabilityEnum.BrandSafetySuitability]
        STANDARD_INVENTORY: _ClassVar[BrandSafetySuitabilityEnum.BrandSafetySuitability]
        LIMITED_INVENTORY: _ClassVar[BrandSafetySuitabilityEnum.BrandSafetySuitability]
    UNSPECIFIED: BrandSafetySuitabilityEnum.BrandSafetySuitability
    UNKNOWN: BrandSafetySuitabilityEnum.BrandSafetySuitability
    EXPANDED_INVENTORY: BrandSafetySuitabilityEnum.BrandSafetySuitability
    STANDARD_INVENTORY: BrandSafetySuitabilityEnum.BrandSafetySuitability
    LIMITED_INVENTORY: BrandSafetySuitabilityEnum.BrandSafetySuitability

    def __init__(self) -> None:
        ...