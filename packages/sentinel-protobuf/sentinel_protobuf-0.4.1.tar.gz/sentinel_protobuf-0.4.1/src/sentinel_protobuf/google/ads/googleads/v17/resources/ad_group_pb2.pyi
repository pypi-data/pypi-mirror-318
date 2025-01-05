from google.ads.googleads.v17.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v17.common import targeting_setting_pb2 as _targeting_setting_pb2
from google.ads.googleads.v17.enums import ad_group_ad_rotation_mode_pb2 as _ad_group_ad_rotation_mode_pb2
from google.ads.googleads.v17.enums import ad_group_primary_status_pb2 as _ad_group_primary_status_pb2
from google.ads.googleads.v17.enums import ad_group_primary_status_reason_pb2 as _ad_group_primary_status_reason_pb2
from google.ads.googleads.v17.enums import ad_group_status_pb2 as _ad_group_status_pb2
from google.ads.googleads.v17.enums import ad_group_type_pb2 as _ad_group_type_pb2
from google.ads.googleads.v17.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v17.enums import asset_set_type_pb2 as _asset_set_type_pb2
from google.ads.googleads.v17.enums import bidding_source_pb2 as _bidding_source_pb2
from google.ads.googleads.v17.enums import targeting_dimension_pb2 as _targeting_dimension_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroup(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "type", "ad_rotation_mode", "base_ad_group", "tracking_url_template", "url_custom_parameters", "campaign", "cpc_bid_micros", "effective_cpc_bid_micros", "cpm_bid_micros", "target_cpa_micros", "cpv_bid_micros", "target_cpm_micros", "target_roas", "percent_cpc_bid_micros", "fixed_cpm_micros", "target_cpv_micros", "optimized_targeting_enabled", "display_custom_bid_dimension", "final_url_suffix", "targeting_setting", "audience_setting", "effective_target_cpa_micros", "effective_target_cpa_source", "effective_target_roas", "effective_target_roas_source", "labels", "excluded_parent_asset_field_types", "excluded_parent_asset_set_types", "primary_status", "primary_status_reasons")
    class AudienceSetting(_message.Message):
        __slots__ = ("use_audience_grouped",)
        USE_AUDIENCE_GROUPED_FIELD_NUMBER: _ClassVar[int]
        use_audience_grouped: bool
        def __init__(self, use_audience_grouped: bool = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_ROTATION_MODE_FIELD_NUMBER: _ClassVar[int]
    BASE_AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPM_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    CPV_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPM_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    FIXED_CPM_MICROS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPV_MICROS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZED_TARGETING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CUSTOM_BID_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TARGETING_SETTING_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_SETTING_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TARGET_CPA_MICROS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TARGET_CPA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TARGET_ROAS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TARGET_ROAS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PARENT_ASSET_FIELD_TYPES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PARENT_ASSET_SET_TYPES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_REASONS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus
    type: _ad_group_type_pb2.AdGroupTypeEnum.AdGroupType
    ad_rotation_mode: _ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    base_ad_group: str
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    campaign: str
    cpc_bid_micros: int
    effective_cpc_bid_micros: int
    cpm_bid_micros: int
    target_cpa_micros: int
    cpv_bid_micros: int
    target_cpm_micros: int
    target_roas: float
    percent_cpc_bid_micros: int
    fixed_cpm_micros: int
    target_cpv_micros: int
    optimized_targeting_enabled: bool
    display_custom_bid_dimension: _targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension
    final_url_suffix: str
    targeting_setting: _targeting_setting_pb2.TargetingSetting
    audience_setting: AdGroup.AudienceSetting
    effective_target_cpa_micros: int
    effective_target_cpa_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    effective_target_roas: float
    effective_target_roas_source: _bidding_source_pb2.BiddingSourceEnum.BiddingSource
    labels: _containers.RepeatedScalarFieldContainer[str]
    excluded_parent_asset_field_types: _containers.RepeatedScalarFieldContainer[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType]
    excluded_parent_asset_set_types: _containers.RepeatedScalarFieldContainer[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType]
    primary_status: _ad_group_primary_status_pb2.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    primary_status_reasons: _containers.RepeatedScalarFieldContainer[_ad_group_primary_status_reason_pb2.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus, str]] = ..., type: _Optional[_Union[_ad_group_type_pb2.AdGroupTypeEnum.AdGroupType, str]] = ..., ad_rotation_mode: _Optional[_Union[_ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode, str]] = ..., base_ad_group: _Optional[str] = ..., tracking_url_template: _Optional[str] = ..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]] = ..., campaign: _Optional[str] = ..., cpc_bid_micros: _Optional[int] = ..., effective_cpc_bid_micros: _Optional[int] = ..., cpm_bid_micros: _Optional[int] = ..., target_cpa_micros: _Optional[int] = ..., cpv_bid_micros: _Optional[int] = ..., target_cpm_micros: _Optional[int] = ..., target_roas: _Optional[float] = ..., percent_cpc_bid_micros: _Optional[int] = ..., fixed_cpm_micros: _Optional[int] = ..., target_cpv_micros: _Optional[int] = ..., optimized_targeting_enabled: bool = ..., display_custom_bid_dimension: _Optional[_Union[_targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension, str]] = ..., final_url_suffix: _Optional[str] = ..., targeting_setting: _Optional[_Union[_targeting_setting_pb2.TargetingSetting, _Mapping]] = ..., audience_setting: _Optional[_Union[AdGroup.AudienceSetting, _Mapping]] = ..., effective_target_cpa_micros: _Optional[int] = ..., effective_target_cpa_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., effective_target_roas: _Optional[float] = ..., effective_target_roas_source: _Optional[_Union[_bidding_source_pb2.BiddingSourceEnum.BiddingSource, str]] = ..., labels: _Optional[_Iterable[str]] = ..., excluded_parent_asset_field_types: _Optional[_Iterable[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]] = ..., excluded_parent_asset_set_types: _Optional[_Iterable[_Union[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType, str]]] = ..., primary_status: _Optional[_Union[_ad_group_primary_status_pb2.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus, str]] = ..., primary_status_reasons: _Optional[_Iterable[_Union[_ad_group_primary_status_reason_pb2.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason, str]]] = ...) -> None: ...
