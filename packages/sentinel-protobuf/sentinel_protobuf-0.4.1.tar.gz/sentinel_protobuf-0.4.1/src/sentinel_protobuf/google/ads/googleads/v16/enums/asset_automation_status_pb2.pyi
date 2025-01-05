from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetAutomationStatusEnum(_message.Message):
    __slots__ = ()

    class AssetAutomationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetAutomationStatusEnum.AssetAutomationStatus]
        UNKNOWN: _ClassVar[AssetAutomationStatusEnum.AssetAutomationStatus]
        OPTED_IN: _ClassVar[AssetAutomationStatusEnum.AssetAutomationStatus]
        OPTED_OUT: _ClassVar[AssetAutomationStatusEnum.AssetAutomationStatus]
    UNSPECIFIED: AssetAutomationStatusEnum.AssetAutomationStatus
    UNKNOWN: AssetAutomationStatusEnum.AssetAutomationStatus
    OPTED_IN: AssetAutomationStatusEnum.AssetAutomationStatus
    OPTED_OUT: AssetAutomationStatusEnum.AssetAutomationStatus

    def __init__(self) -> None:
        ...