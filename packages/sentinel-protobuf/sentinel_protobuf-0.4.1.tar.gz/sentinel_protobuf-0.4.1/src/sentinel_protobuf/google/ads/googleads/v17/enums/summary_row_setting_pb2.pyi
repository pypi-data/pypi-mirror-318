from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SummaryRowSettingEnum(_message.Message):
    __slots__ = ()

    class SummaryRowSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SummaryRowSettingEnum.SummaryRowSetting]
        UNKNOWN: _ClassVar[SummaryRowSettingEnum.SummaryRowSetting]
        NO_SUMMARY_ROW: _ClassVar[SummaryRowSettingEnum.SummaryRowSetting]
        SUMMARY_ROW_WITH_RESULTS: _ClassVar[SummaryRowSettingEnum.SummaryRowSetting]
        SUMMARY_ROW_ONLY: _ClassVar[SummaryRowSettingEnum.SummaryRowSetting]
    UNSPECIFIED: SummaryRowSettingEnum.SummaryRowSetting
    UNKNOWN: SummaryRowSettingEnum.SummaryRowSetting
    NO_SUMMARY_ROW: SummaryRowSettingEnum.SummaryRowSetting
    SUMMARY_ROW_WITH_RESULTS: SummaryRowSettingEnum.SummaryRowSetting
    SUMMARY_ROW_ONLY: SummaryRowSettingEnum.SummaryRowSetting

    def __init__(self) -> None:
        ...