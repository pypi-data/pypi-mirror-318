from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetAutomationTypeEnum(_message.Message):
    __slots__ = ()

    class AssetAutomationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetAutomationTypeEnum.AssetAutomationType]
        UNKNOWN: _ClassVar[AssetAutomationTypeEnum.AssetAutomationType]
        TEXT_ASSET_AUTOMATION: _ClassVar[AssetAutomationTypeEnum.AssetAutomationType]
        GENERATE_VERTICAL_YOUTUBE_VIDEOS: _ClassVar[AssetAutomationTypeEnum.AssetAutomationType]
        GENERATE_SHORTER_YOUTUBE_VIDEOS: _ClassVar[AssetAutomationTypeEnum.AssetAutomationType]
    UNSPECIFIED: AssetAutomationTypeEnum.AssetAutomationType
    UNKNOWN: AssetAutomationTypeEnum.AssetAutomationType
    TEXT_ASSET_AUTOMATION: AssetAutomationTypeEnum.AssetAutomationType
    GENERATE_VERTICAL_YOUTUBE_VIDEOS: AssetAutomationTypeEnum.AssetAutomationType
    GENERATE_SHORTER_YOUTUBE_VIDEOS: AssetAutomationTypeEnum.AssetAutomationType

    def __init__(self) -> None:
        ...