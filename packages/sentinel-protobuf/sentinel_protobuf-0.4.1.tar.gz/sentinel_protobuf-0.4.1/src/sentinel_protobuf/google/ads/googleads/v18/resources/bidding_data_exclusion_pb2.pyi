from google.ads.googleads.v18.enums import advertising_channel_type_pb2 as _advertising_channel_type_pb2
from google.ads.googleads.v18.enums import device_pb2 as _device_pb2
from google.ads.googleads.v18.enums import seasonality_event_scope_pb2 as _seasonality_event_scope_pb2
from google.ads.googleads.v18.enums import seasonality_event_status_pb2 as _seasonality_event_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingDataExclusion(_message.Message):
    __slots__ = ('resource_name', 'data_exclusion_id', 'scope', 'status', 'start_date_time', 'end_date_time', 'name', 'description', 'devices', 'campaigns', 'advertising_channel_types')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCLUSION_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_CHANNEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    data_exclusion_id: int
    scope: _seasonality_event_scope_pb2.SeasonalityEventScopeEnum.SeasonalityEventScope
    status: _seasonality_event_status_pb2.SeasonalityEventStatusEnum.SeasonalityEventStatus
    start_date_time: str
    end_date_time: str
    name: str
    description: str
    devices: _containers.RepeatedScalarFieldContainer[_device_pb2.DeviceEnum.Device]
    campaigns: _containers.RepeatedScalarFieldContainer[str]
    advertising_channel_types: _containers.RepeatedScalarFieldContainer[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType]

    def __init__(self, resource_name: _Optional[str]=..., data_exclusion_id: _Optional[int]=..., scope: _Optional[_Union[_seasonality_event_scope_pb2.SeasonalityEventScopeEnum.SeasonalityEventScope, str]]=..., status: _Optional[_Union[_seasonality_event_status_pb2.SeasonalityEventStatusEnum.SeasonalityEventStatus, str]]=..., start_date_time: _Optional[str]=..., end_date_time: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., devices: _Optional[_Iterable[_Union[_device_pb2.DeviceEnum.Device, str]]]=..., campaigns: _Optional[_Iterable[str]]=..., advertising_channel_types: _Optional[_Iterable[_Union[_advertising_channel_type_pb2.AdvertisingChannelTypeEnum.AdvertisingChannelType, str]]]=...) -> None:
        ...