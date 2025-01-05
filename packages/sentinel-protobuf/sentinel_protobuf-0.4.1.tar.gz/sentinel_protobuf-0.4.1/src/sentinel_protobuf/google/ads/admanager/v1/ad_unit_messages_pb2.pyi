from google.ads.admanager.v1 import ad_unit_enums_pb2 as _ad_unit_enums_pb2
from google.ads.admanager.v1 import applied_label_pb2 as _applied_label_pb2
from google.ads.admanager.v1 import environment_type_enum_pb2 as _environment_type_enum_pb2
from google.ads.admanager.v1 import frequency_cap_pb2 as _frequency_cap_pb2
from google.ads.admanager.v1 import size_pb2 as _size_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdUnit(_message.Message):
    __slots__ = ("name", "ad_unit_id", "parent_ad_unit", "parent_path", "display_name", "ad_unit_code", "status", "applied_target_window", "effective_target_window", "applied_teams", "teams", "description", "explicitly_targeted", "has_children", "update_time", "ad_unit_sizes", "external_set_top_box_channel_id", "refresh_delay", "applied_labels", "effective_applied_labels", "applied_label_frequency_caps", "effective_label_frequency_caps", "smart_size_mode", "applied_adsense_enabled", "effective_adsense_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_AD_UNIT_FIELD_NUMBER: _ClassVar[int]
    PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_UNIT_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_TARGET_WINDOW_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TARGET_WINDOW_FIELD_NUMBER: _ClassVar[int]
    APPLIED_TEAMS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPLICITLY_TARGETED_FIELD_NUMBER: _ClassVar[int]
    HAS_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AD_UNIT_SIZES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SET_TOP_BOX_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_DELAY_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABEL_FREQUENCY_CAPS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LABEL_FREQUENCY_CAPS_FIELD_NUMBER: _ClassVar[int]
    SMART_SIZE_MODE_FIELD_NUMBER: _ClassVar[int]
    APPLIED_ADSENSE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ADSENSE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_unit_id: int
    parent_ad_unit: str
    parent_path: _containers.RepeatedCompositeFieldContainer[AdUnitParent]
    display_name: str
    ad_unit_code: str
    status: _ad_unit_enums_pb2.AdUnitStatusEnum.AdUnitStatus
    applied_target_window: _ad_unit_enums_pb2.TargetWindowEnum.TargetWindow
    effective_target_window: _ad_unit_enums_pb2.TargetWindowEnum.TargetWindow
    applied_teams: _containers.RepeatedScalarFieldContainer[str]
    teams: _containers.RepeatedScalarFieldContainer[str]
    description: str
    explicitly_targeted: bool
    has_children: bool
    update_time: _timestamp_pb2.Timestamp
    ad_unit_sizes: _containers.RepeatedCompositeFieldContainer[AdUnitSize]
    external_set_top_box_channel_id: str
    refresh_delay: _duration_pb2.Duration
    applied_labels: _containers.RepeatedCompositeFieldContainer[_applied_label_pb2.AppliedLabel]
    effective_applied_labels: _containers.RepeatedCompositeFieldContainer[_applied_label_pb2.AppliedLabel]
    applied_label_frequency_caps: _containers.RepeatedCompositeFieldContainer[LabelFrequencyCap]
    effective_label_frequency_caps: _containers.RepeatedCompositeFieldContainer[LabelFrequencyCap]
    smart_size_mode: _ad_unit_enums_pb2.SmartSizeModeEnum.SmartSizeMode
    applied_adsense_enabled: bool
    effective_adsense_enabled: bool
    def __init__(self, name: _Optional[str] = ..., ad_unit_id: _Optional[int] = ..., parent_ad_unit: _Optional[str] = ..., parent_path: _Optional[_Iterable[_Union[AdUnitParent, _Mapping]]] = ..., display_name: _Optional[str] = ..., ad_unit_code: _Optional[str] = ..., status: _Optional[_Union[_ad_unit_enums_pb2.AdUnitStatusEnum.AdUnitStatus, str]] = ..., applied_target_window: _Optional[_Union[_ad_unit_enums_pb2.TargetWindowEnum.TargetWindow, str]] = ..., effective_target_window: _Optional[_Union[_ad_unit_enums_pb2.TargetWindowEnum.TargetWindow, str]] = ..., applied_teams: _Optional[_Iterable[str]] = ..., teams: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., explicitly_targeted: bool = ..., has_children: bool = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ad_unit_sizes: _Optional[_Iterable[_Union[AdUnitSize, _Mapping]]] = ..., external_set_top_box_channel_id: _Optional[str] = ..., refresh_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., applied_labels: _Optional[_Iterable[_Union[_applied_label_pb2.AppliedLabel, _Mapping]]] = ..., effective_applied_labels: _Optional[_Iterable[_Union[_applied_label_pb2.AppliedLabel, _Mapping]]] = ..., applied_label_frequency_caps: _Optional[_Iterable[_Union[LabelFrequencyCap, _Mapping]]] = ..., effective_label_frequency_caps: _Optional[_Iterable[_Union[LabelFrequencyCap, _Mapping]]] = ..., smart_size_mode: _Optional[_Union[_ad_unit_enums_pb2.SmartSizeModeEnum.SmartSizeMode, str]] = ..., applied_adsense_enabled: bool = ..., effective_adsense_enabled: bool = ...) -> None: ...

class AdUnitSize(_message.Message):
    __slots__ = ("size", "environment_type", "companions")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPANIONS_FIELD_NUMBER: _ClassVar[int]
    size: _size_pb2.Size
    environment_type: _environment_type_enum_pb2.EnvironmentTypeEnum.EnvironmentType
    companions: _containers.RepeatedCompositeFieldContainer[_size_pb2.Size]
    def __init__(self, size: _Optional[_Union[_size_pb2.Size, _Mapping]] = ..., environment_type: _Optional[_Union[_environment_type_enum_pb2.EnvironmentTypeEnum.EnvironmentType, str]] = ..., companions: _Optional[_Iterable[_Union[_size_pb2.Size, _Mapping]]] = ...) -> None: ...

class AdUnitParent(_message.Message):
    __slots__ = ("parent_ad_unit", "display_name", "ad_unit_code")
    PARENT_AD_UNIT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_UNIT_CODE_FIELD_NUMBER: _ClassVar[int]
    parent_ad_unit: str
    display_name: str
    ad_unit_code: str
    def __init__(self, parent_ad_unit: _Optional[str] = ..., display_name: _Optional[str] = ..., ad_unit_code: _Optional[str] = ...) -> None: ...

class LabelFrequencyCap(_message.Message):
    __slots__ = ("label", "frequency_cap")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_CAP_FIELD_NUMBER: _ClassVar[int]
    label: str
    frequency_cap: _frequency_cap_pb2.FrequencyCap
    def __init__(self, label: _Optional[str] = ..., frequency_cap: _Optional[_Union[_frequency_cap_pb2.FrequencyCap, _Mapping]] = ...) -> None: ...
