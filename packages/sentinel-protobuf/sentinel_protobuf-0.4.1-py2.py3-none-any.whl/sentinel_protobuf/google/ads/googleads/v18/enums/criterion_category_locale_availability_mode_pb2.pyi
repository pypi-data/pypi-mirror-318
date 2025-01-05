from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CriterionCategoryLocaleAvailabilityModeEnum(_message.Message):
    __slots__ = ()

    class CriterionCategoryLocaleAvailabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
        UNKNOWN: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
        ALL_LOCALES: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
        COUNTRY_AND_ALL_LANGUAGES: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
        LANGUAGE_AND_ALL_COUNTRIES: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
        COUNTRY_AND_LANGUAGE: _ClassVar[CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode]
    UNSPECIFIED: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    UNKNOWN: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    ALL_LOCALES: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    COUNTRY_AND_ALL_LANGUAGES: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    LANGUAGE_AND_ALL_COUNTRIES: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    COUNTRY_AND_LANGUAGE: CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode

    def __init__(self) -> None:
        ...