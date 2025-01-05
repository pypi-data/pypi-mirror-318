from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.playablelocations.v3 import resources_pb2 as _resources_pb2
from google.maps.playablelocations.v3.sample import resources_pb2 as _resources_pb2_1
from google.maps.unity import clientinfo_pb2 as _clientinfo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SamplePlayableLocationsRequest(_message.Message):
    __slots__ = ('area_filter', 'criteria')
    AREA_FILTER_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    area_filter: _resources_pb2_1.AreaFilter
    criteria: _containers.RepeatedCompositeFieldContainer[_resources_pb2_1.Criterion]

    def __init__(self, area_filter: _Optional[_Union[_resources_pb2_1.AreaFilter, _Mapping]]=..., criteria: _Optional[_Iterable[_Union[_resources_pb2_1.Criterion, _Mapping]]]=...) -> None:
        ...

class SamplePlayableLocationsResponse(_message.Message):
    __slots__ = ('locations_per_game_object_type', 'ttl')

    class LocationsPerGameObjectTypeEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _resources_pb2_1.PlayableLocationList

        def __init__(self, key: _Optional[int]=..., value: _Optional[_Union[_resources_pb2_1.PlayableLocationList, _Mapping]]=...) -> None:
            ...
    LOCATIONS_PER_GAME_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    locations_per_game_object_type: _containers.MessageMap[int, _resources_pb2_1.PlayableLocationList]
    ttl: _duration_pb2.Duration

    def __init__(self, locations_per_game_object_type: _Optional[_Mapping[int, _resources_pb2_1.PlayableLocationList]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LogPlayerReportsRequest(_message.Message):
    __slots__ = ('player_reports', 'request_id', 'client_info')
    PLAYER_REPORTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    player_reports: _containers.RepeatedCompositeFieldContainer[_resources_pb2.PlayerReport]
    request_id: str
    client_info: _clientinfo_pb2.ClientInfo

    def __init__(self, player_reports: _Optional[_Iterable[_Union[_resources_pb2.PlayerReport, _Mapping]]]=..., request_id: _Optional[str]=..., client_info: _Optional[_Union[_clientinfo_pb2.ClientInfo, _Mapping]]=...) -> None:
        ...

class LogPlayerReportsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LogImpressionsRequest(_message.Message):
    __slots__ = ('impressions', 'request_id', 'client_info')
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    impressions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Impression]
    request_id: str
    client_info: _clientinfo_pb2.ClientInfo

    def __init__(self, impressions: _Optional[_Iterable[_Union[_resources_pb2.Impression, _Mapping]]]=..., request_id: _Optional[str]=..., client_info: _Optional[_Union[_clientinfo_pb2.ClientInfo, _Mapping]]=...) -> None:
        ...

class LogImpressionsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...