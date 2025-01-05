from google.ads.googleads.v18.common import asset_policy_pb2 as _asset_policy_pb2
from google.ads.googleads.v18.common import policy_summary_pb2 as _policy_summary_pb2
from google.ads.googleads.v18.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v18.enums import asset_link_primary_status_pb2 as _asset_link_primary_status_pb2
from google.ads.googleads.v18.enums import asset_link_primary_status_reason_pb2 as _asset_link_primary_status_reason_pb2
from google.ads.googleads.v18.enums import asset_link_status_pb2 as _asset_link_status_pb2
from google.ads.googleads.v18.enums import asset_performance_label_pb2 as _asset_performance_label_pb2
from google.ads.googleads.v18.enums import asset_source_pb2 as _asset_source_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupAsset(_message.Message):
    __slots__ = ("resource_name", "asset_group", "asset", "field_type", "status", "primary_status", "primary_status_reasons", "primary_status_details", "performance_label", "policy_summary", "source")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_REASONS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_LABEL_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    asset: str
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    status: _asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus
    primary_status: _asset_link_primary_status_pb2.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    primary_status_reasons: _containers.RepeatedScalarFieldContainer[_asset_link_primary_status_reason_pb2.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
    primary_status_details: _containers.RepeatedCompositeFieldContainer[_asset_policy_pb2.AssetLinkPrimaryStatusDetails]
    performance_label: _asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary: _policy_summary_pb2.PolicySummary
    source: _asset_source_pb2.AssetSourceEnum.AssetSource
    def __init__(self, resource_name: _Optional[str] = ..., asset_group: _Optional[str] = ..., asset: _Optional[str] = ..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]] = ..., status: _Optional[_Union[_asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus, str]] = ..., primary_status: _Optional[_Union[_asset_link_primary_status_pb2.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus, str]] = ..., primary_status_reasons: _Optional[_Iterable[_Union[_asset_link_primary_status_reason_pb2.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason, str]]] = ..., primary_status_details: _Optional[_Iterable[_Union[_asset_policy_pb2.AssetLinkPrimaryStatusDetails, _Mapping]]] = ..., performance_label: _Optional[_Union[_asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel, str]] = ..., policy_summary: _Optional[_Union[_policy_summary_pb2.PolicySummary, _Mapping]] = ..., source: _Optional[_Union[_asset_source_pb2.AssetSourceEnum.AssetSource, str]] = ...) -> None: ...
