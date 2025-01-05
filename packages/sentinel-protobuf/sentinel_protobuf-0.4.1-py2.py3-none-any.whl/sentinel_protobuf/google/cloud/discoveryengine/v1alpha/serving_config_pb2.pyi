from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1alpha import search_service_pb2 as _search_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServingConfig(_message.Message):
    __slots__ = ("media_config", "generic_config", "name", "display_name", "solution_type", "model_id", "diversity_level", "embedding_config", "ranking_expression", "guided_search_spec", "custom_fine_tuning_spec", "create_time", "update_time", "filter_control_ids", "boost_control_ids", "redirect_control_ids", "synonyms_control_ids", "oneway_synonyms_control_ids", "dissociate_control_ids", "replacement_control_ids", "ignore_control_ids")
    class MediaConfig(_message.Message):
        __slots__ = ("content_watched_percentage_threshold", "content_watched_seconds_threshold", "demotion_event_type", "content_freshness_cutoff_days")
        CONTENT_WATCHED_PERCENTAGE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        CONTENT_WATCHED_SECONDS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        DEMOTION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FRESHNESS_CUTOFF_DAYS_FIELD_NUMBER: _ClassVar[int]
        content_watched_percentage_threshold: float
        content_watched_seconds_threshold: float
        demotion_event_type: str
        content_freshness_cutoff_days: int
        def __init__(self, content_watched_percentage_threshold: _Optional[float] = ..., content_watched_seconds_threshold: _Optional[float] = ..., demotion_event_type: _Optional[str] = ..., content_freshness_cutoff_days: _Optional[int] = ...) -> None: ...
    class GenericConfig(_message.Message):
        __slots__ = ("content_search_spec",)
        CONTENT_SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
        content_search_spec: _search_service_pb2.SearchRequest.ContentSearchSpec
        def __init__(self, content_search_spec: _Optional[_Union[_search_service_pb2.SearchRequest.ContentSearchSpec, _Mapping]] = ...) -> None: ...
    MEDIA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GENERIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DIVERSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RANKING_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    GUIDED_SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FINE_TUNING_SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    BOOST_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    ONEWAY_SYNONYMS_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    DISSOCIATE_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    media_config: ServingConfig.MediaConfig
    generic_config: ServingConfig.GenericConfig
    name: str
    display_name: str
    solution_type: _common_pb2.SolutionType
    model_id: str
    diversity_level: str
    embedding_config: _common_pb2.EmbeddingConfig
    ranking_expression: str
    guided_search_spec: _common_pb2.GuidedSearchSpec
    custom_fine_tuning_spec: _common_pb2.CustomFineTuningSpec
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    filter_control_ids: _containers.RepeatedScalarFieldContainer[str]
    boost_control_ids: _containers.RepeatedScalarFieldContainer[str]
    redirect_control_ids: _containers.RepeatedScalarFieldContainer[str]
    synonyms_control_ids: _containers.RepeatedScalarFieldContainer[str]
    oneway_synonyms_control_ids: _containers.RepeatedScalarFieldContainer[str]
    dissociate_control_ids: _containers.RepeatedScalarFieldContainer[str]
    replacement_control_ids: _containers.RepeatedScalarFieldContainer[str]
    ignore_control_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, media_config: _Optional[_Union[ServingConfig.MediaConfig, _Mapping]] = ..., generic_config: _Optional[_Union[ServingConfig.GenericConfig, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., solution_type: _Optional[_Union[_common_pb2.SolutionType, str]] = ..., model_id: _Optional[str] = ..., diversity_level: _Optional[str] = ..., embedding_config: _Optional[_Union[_common_pb2.EmbeddingConfig, _Mapping]] = ..., ranking_expression: _Optional[str] = ..., guided_search_spec: _Optional[_Union[_common_pb2.GuidedSearchSpec, _Mapping]] = ..., custom_fine_tuning_spec: _Optional[_Union[_common_pb2.CustomFineTuningSpec, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter_control_ids: _Optional[_Iterable[str]] = ..., boost_control_ids: _Optional[_Iterable[str]] = ..., redirect_control_ids: _Optional[_Iterable[str]] = ..., synonyms_control_ids: _Optional[_Iterable[str]] = ..., oneway_synonyms_control_ids: _Optional[_Iterable[str]] = ..., dissociate_control_ids: _Optional[_Iterable[str]] = ..., replacement_control_ids: _Optional[_Iterable[str]] = ..., ignore_control_ids: _Optional[_Iterable[str]] = ...) -> None: ...
