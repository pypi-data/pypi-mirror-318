from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupPrimaryStatusReasonEnum(_message.Message):
    __slots__ = ()

    class AssetGroupPrimaryStatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        UNKNOWN: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        ASSET_GROUP_PAUSED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        ASSET_GROUP_REMOVED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        CAMPAIGN_REMOVED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        CAMPAIGN_PAUSED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        CAMPAIGN_PENDING: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        CAMPAIGN_ENDED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        ASSET_GROUP_LIMITED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        ASSET_GROUP_DISAPPROVED: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
        ASSET_GROUP_UNDER_REVIEW: _ClassVar[AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
    UNSPECIFIED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    UNKNOWN: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ASSET_GROUP_PAUSED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ASSET_GROUP_REMOVED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    CAMPAIGN_REMOVED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    CAMPAIGN_PAUSED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    CAMPAIGN_PENDING: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    CAMPAIGN_ENDED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ASSET_GROUP_LIMITED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ASSET_GROUP_DISAPPROVED: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ASSET_GROUP_UNDER_REVIEW: AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason

    def __init__(self) -> None:
        ...