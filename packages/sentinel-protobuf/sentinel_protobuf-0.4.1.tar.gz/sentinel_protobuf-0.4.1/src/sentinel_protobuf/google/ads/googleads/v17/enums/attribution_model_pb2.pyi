from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AttributionModelEnum(_message.Message):
    __slots__ = ()

    class AttributionModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AttributionModelEnum.AttributionModel]
        UNKNOWN: _ClassVar[AttributionModelEnum.AttributionModel]
        EXTERNAL: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_ADS_LAST_CLICK: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_SEARCH_ATTRIBUTION_LINEAR: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED: _ClassVar[AttributionModelEnum.AttributionModel]
        GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN: _ClassVar[AttributionModelEnum.AttributionModel]
    UNSPECIFIED: AttributionModelEnum.AttributionModel
    UNKNOWN: AttributionModelEnum.AttributionModel
    EXTERNAL: AttributionModelEnum.AttributionModel
    GOOGLE_ADS_LAST_CLICK: AttributionModelEnum.AttributionModel
    GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK: AttributionModelEnum.AttributionModel
    GOOGLE_SEARCH_ATTRIBUTION_LINEAR: AttributionModelEnum.AttributionModel
    GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY: AttributionModelEnum.AttributionModel
    GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED: AttributionModelEnum.AttributionModel
    GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN: AttributionModelEnum.AttributionModel

    def __init__(self) -> None:
        ...