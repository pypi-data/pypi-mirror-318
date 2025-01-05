from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchEngineResultsPageTypeEnum(_message.Message):
    __slots__ = ()

    class SearchEngineResultsPageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType]
        UNKNOWN: _ClassVar[SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType]
        ADS_ONLY: _ClassVar[SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType]
        ORGANIC_ONLY: _ClassVar[SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType]
        ADS_AND_ORGANIC: _ClassVar[SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType]
    UNSPECIFIED: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    UNKNOWN: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ADS_ONLY: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ORGANIC_ONLY: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ADS_AND_ORGANIC: SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType

    def __init__(self) -> None:
        ...