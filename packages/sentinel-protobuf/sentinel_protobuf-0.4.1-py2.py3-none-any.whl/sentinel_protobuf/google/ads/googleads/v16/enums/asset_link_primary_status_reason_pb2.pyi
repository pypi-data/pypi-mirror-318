from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetLinkPrimaryStatusReasonEnum(_message.Message):
    __slots__ = ()

    class AssetLinkPrimaryStatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        UNKNOWN: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        ASSET_LINK_PAUSED: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        ASSET_LINK_REMOVED: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        ASSET_DISAPPROVED: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        ASSET_UNDER_REVIEW: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
        ASSET_APPROVED_LABELED: _ClassVar[AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
    UNSPECIFIED: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    UNKNOWN: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ASSET_LINK_PAUSED: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ASSET_LINK_REMOVED: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ASSET_DISAPPROVED: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ASSET_UNDER_REVIEW: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ASSET_APPROVED_LABELED: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason

    def __init__(self) -> None:
        ...