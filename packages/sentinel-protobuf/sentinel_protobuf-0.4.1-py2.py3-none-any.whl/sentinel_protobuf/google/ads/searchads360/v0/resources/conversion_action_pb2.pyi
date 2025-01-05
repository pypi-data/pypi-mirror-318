from google.ads.searchads360.v0.enums import attribution_model_pb2 as _attribution_model_pb2
from google.ads.searchads360.v0.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.searchads360.v0.enums import conversion_action_status_pb2 as _conversion_action_status_pb2
from google.ads.searchads360.v0.enums import conversion_action_type_pb2 as _conversion_action_type_pb2
from google.ads.searchads360.v0.enums import data_driven_model_status_pb2 as _data_driven_model_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversionAction(_message.Message):
    __slots__ = ("resource_name", "id", "name", "creation_time", "status", "type", "primary_for_goal", "category", "owner_customer", "include_in_client_account_conversions_metric", "include_in_conversions_metric", "click_through_lookback_window_days", "value_settings", "attribution_model_settings", "app_id", "floodlight_settings")
    class AttributionModelSettings(_message.Message):
        __slots__ = ("attribution_model", "data_driven_model_status")
        ATTRIBUTION_MODEL_FIELD_NUMBER: _ClassVar[int]
        DATA_DRIVEN_MODEL_STATUS_FIELD_NUMBER: _ClassVar[int]
        attribution_model: _attribution_model_pb2.AttributionModelEnum.AttributionModel
        data_driven_model_status: _data_driven_model_status_pb2.DataDrivenModelStatusEnum.DataDrivenModelStatus
        def __init__(self, attribution_model: _Optional[_Union[_attribution_model_pb2.AttributionModelEnum.AttributionModel, str]] = ..., data_driven_model_status: _Optional[_Union[_data_driven_model_status_pb2.DataDrivenModelStatusEnum.DataDrivenModelStatus, str]] = ...) -> None: ...
    class ValueSettings(_message.Message):
        __slots__ = ("default_value", "default_currency_code", "always_use_default_value")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_USE_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        default_value: float
        default_currency_code: str
        always_use_default_value: bool
        def __init__(self, default_value: _Optional[float] = ..., default_currency_code: _Optional[str] = ..., always_use_default_value: bool = ...) -> None: ...
    class FloodlightSettings(_message.Message):
        __slots__ = ("activity_group_tag", "activity_tag", "activity_id")
        ACTIVITY_GROUP_TAG_FIELD_NUMBER: _ClassVar[int]
        ACTIVITY_TAG_FIELD_NUMBER: _ClassVar[int]
        ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
        activity_group_tag: str
        activity_tag: str
        activity_id: int
        def __init__(self, activity_group_tag: _Optional[str] = ..., activity_tag: _Optional[str] = ..., activity_id: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FOR_GOAL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IN_CLIENT_ACCOUNT_CONVERSIONS_METRIC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IN_CONVERSIONS_METRIC_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_LOOKBACK_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    VALUE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FLOODLIGHT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    creation_time: str
    status: _conversion_action_status_pb2.ConversionActionStatusEnum.ConversionActionStatus
    type: _conversion_action_type_pb2.ConversionActionTypeEnum.ConversionActionType
    primary_for_goal: bool
    category: _conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory
    owner_customer: str
    include_in_client_account_conversions_metric: bool
    include_in_conversions_metric: bool
    click_through_lookback_window_days: int
    value_settings: ConversionAction.ValueSettings
    attribution_model_settings: ConversionAction.AttributionModelSettings
    app_id: str
    floodlight_settings: ConversionAction.FloodlightSettings
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., creation_time: _Optional[str] = ..., status: _Optional[_Union[_conversion_action_status_pb2.ConversionActionStatusEnum.ConversionActionStatus, str]] = ..., type: _Optional[_Union[_conversion_action_type_pb2.ConversionActionTypeEnum.ConversionActionType, str]] = ..., primary_for_goal: bool = ..., category: _Optional[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]] = ..., owner_customer: _Optional[str] = ..., include_in_client_account_conversions_metric: bool = ..., include_in_conversions_metric: bool = ..., click_through_lookback_window_days: _Optional[int] = ..., value_settings: _Optional[_Union[ConversionAction.ValueSettings, _Mapping]] = ..., attribution_model_settings: _Optional[_Union[ConversionAction.AttributionModelSettings, _Mapping]] = ..., app_id: _Optional[str] = ..., floodlight_settings: _Optional[_Union[ConversionAction.FloodlightSettings, _Mapping]] = ...) -> None: ...
