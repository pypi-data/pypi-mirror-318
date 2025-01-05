from google.ads.searchads360.v0.enums import ad_group_ad_engine_status_pb2 as _ad_group_ad_engine_status_pb2
from google.ads.searchads360.v0.enums import ad_group_ad_status_pb2 as _ad_group_ad_status_pb2
from google.ads.searchads360.v0.resources import ad_pb2 as _ad_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAd(_message.Message):
    __slots__ = ("resource_name", "status", "ad", "creation_time", "labels", "effective_labels", "engine_id", "engine_status", "last_modified_time")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    status: _ad_group_ad_status_pb2.AdGroupAdStatusEnum.AdGroupAdStatus
    ad: _ad_pb2.Ad
    creation_time: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    effective_labels: _containers.RepeatedScalarFieldContainer[str]
    engine_id: str
    engine_status: _ad_group_ad_engine_status_pb2.AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    last_modified_time: str
    def __init__(self, resource_name: _Optional[str] = ..., status: _Optional[_Union[_ad_group_ad_status_pb2.AdGroupAdStatusEnum.AdGroupAdStatus, str]] = ..., ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., creation_time: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., effective_labels: _Optional[_Iterable[str]] = ..., engine_id: _Optional[str] = ..., engine_status: _Optional[_Union[_ad_group_ad_engine_status_pb2.AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus, str]] = ..., last_modified_time: _Optional[str] = ...) -> None: ...
