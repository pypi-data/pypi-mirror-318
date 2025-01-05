from google.ads.searchads360.v0.common import targeting_setting_pb2 as _targeting_setting_pb2
from google.ads.searchads360.v0.enums import ad_group_ad_rotation_mode_pb2 as _ad_group_ad_rotation_mode_pb2
from google.ads.searchads360.v0.enums import ad_group_engine_status_pb2 as _ad_group_engine_status_pb2
from google.ads.searchads360.v0.enums import ad_group_status_pb2 as _ad_group_status_pb2
from google.ads.searchads360.v0.enums import ad_group_type_pb2 as _ad_group_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroup(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "type", "ad_rotation_mode", "cpc_bid_micros", "creation_time", "engine_status", "targeting_setting", "labels", "effective_labels", "engine_id", "start_date", "end_date", "language_code", "last_modified_time")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_ROTATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CPC_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGETING_SETTING_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus
    type: _ad_group_type_pb2.AdGroupTypeEnum.AdGroupType
    ad_rotation_mode: _ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    cpc_bid_micros: int
    creation_time: str
    engine_status: _ad_group_engine_status_pb2.AdGroupEngineStatusEnum.AdGroupEngineStatus
    targeting_setting: _targeting_setting_pb2.TargetingSetting
    labels: _containers.RepeatedScalarFieldContainer[str]
    effective_labels: _containers.RepeatedScalarFieldContainer[str]
    engine_id: str
    start_date: str
    end_date: str
    language_code: str
    last_modified_time: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_ad_group_status_pb2.AdGroupStatusEnum.AdGroupStatus, str]] = ..., type: _Optional[_Union[_ad_group_type_pb2.AdGroupTypeEnum.AdGroupType, str]] = ..., ad_rotation_mode: _Optional[_Union[_ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum.AdGroupAdRotationMode, str]] = ..., cpc_bid_micros: _Optional[int] = ..., creation_time: _Optional[str] = ..., engine_status: _Optional[_Union[_ad_group_engine_status_pb2.AdGroupEngineStatusEnum.AdGroupEngineStatus, str]] = ..., targeting_setting: _Optional[_Union[_targeting_setting_pb2.TargetingSetting, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., effective_labels: _Optional[_Iterable[str]] = ..., engine_id: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., language_code: _Optional[str] = ..., last_modified_time: _Optional[str] = ...) -> None: ...
