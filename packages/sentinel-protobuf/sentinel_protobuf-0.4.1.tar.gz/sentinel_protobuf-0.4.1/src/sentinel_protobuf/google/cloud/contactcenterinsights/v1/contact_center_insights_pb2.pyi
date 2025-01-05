from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contactcenterinsights.v1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_VIEW_UNSPECIFIED: _ClassVar[ConversationView]
    FULL: _ClassVar[ConversationView]
    BASIC: _ClassVar[ConversationView]
CONVERSATION_VIEW_UNSPECIFIED: ConversationView
FULL: ConversationView
BASIC: ConversationView

class CalculateStatsRequest(_message.Message):
    __slots__ = ("location", "filter")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    location: str
    filter: str
    def __init__(self, location: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class CalculateStatsResponse(_message.Message):
    __slots__ = ("average_duration", "average_turn_count", "conversation_count", "smart_highlighter_matches", "custom_highlighter_matches", "issue_matches", "issue_matches_stats", "conversation_count_time_series")
    class TimeSeries(_message.Message):
        __slots__ = ("interval_duration", "points")
        class Interval(_message.Message):
            __slots__ = ("start_time", "conversation_count")
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            CONVERSATION_COUNT_FIELD_NUMBER: _ClassVar[int]
            start_time: _timestamp_pb2.Timestamp
            conversation_count: int
            def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., conversation_count: _Optional[int] = ...) -> None: ...
        INTERVAL_DURATION_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        interval_duration: _duration_pb2.Duration
        points: _containers.RepeatedCompositeFieldContainer[CalculateStatsResponse.TimeSeries.Interval]
        def __init__(self, interval_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., points: _Optional[_Iterable[_Union[CalculateStatsResponse.TimeSeries.Interval, _Mapping]]] = ...) -> None: ...
    class SmartHighlighterMatchesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class CustomHighlighterMatchesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class IssueMatchesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class IssueMatchesStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _resources_pb2.IssueModelLabelStats.IssueStats
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_resources_pb2.IssueModelLabelStats.IssueStats, _Mapping]] = ...) -> None: ...
    AVERAGE_DURATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TURN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    SMART_HIGHLIGHTER_MATCHES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_HIGHLIGHTER_MATCHES_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MATCHES_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MATCHES_STATS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COUNT_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    average_duration: _duration_pb2.Duration
    average_turn_count: int
    conversation_count: int
    smart_highlighter_matches: _containers.ScalarMap[str, int]
    custom_highlighter_matches: _containers.ScalarMap[str, int]
    issue_matches: _containers.ScalarMap[str, int]
    issue_matches_stats: _containers.MessageMap[str, _resources_pb2.IssueModelLabelStats.IssueStats]
    conversation_count_time_series: CalculateStatsResponse.TimeSeries
    def __init__(self, average_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., average_turn_count: _Optional[int] = ..., conversation_count: _Optional[int] = ..., smart_highlighter_matches: _Optional[_Mapping[str, int]] = ..., custom_highlighter_matches: _Optional[_Mapping[str, int]] = ..., issue_matches: _Optional[_Mapping[str, int]] = ..., issue_matches_stats: _Optional[_Mapping[str, _resources_pb2.IssueModelLabelStats.IssueStats]] = ..., conversation_count_time_series: _Optional[_Union[CalculateStatsResponse.TimeSeries, _Mapping]] = ...) -> None: ...

class CreateAnalysisOperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "conversation", "annotator_selector")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATOR_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    conversation: str
    annotator_selector: _resources_pb2.AnnotatorSelector
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., conversation: _Optional[str] = ..., annotator_selector: _Optional[_Union[_resources_pb2.AnnotatorSelector, _Mapping]] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ("parent", "conversation", "conversation_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation: _resources_pb2.Conversation
    conversation_id: str
    def __init__(self, parent: _Optional[str] = ..., conversation: _Optional[_Union[_resources_pb2.Conversation, _Mapping]] = ..., conversation_id: _Optional[str] = ...) -> None: ...

class UploadConversationRequest(_message.Message):
    __slots__ = ("parent", "conversation", "conversation_id", "redaction_config", "speech_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation: _resources_pb2.Conversation
    conversation_id: str
    redaction_config: _resources_pb2.RedactionConfig
    speech_config: _resources_pb2.SpeechConfig
    def __init__(self, parent: _Optional[str] = ..., conversation: _Optional[_Union[_resources_pb2.Conversation, _Mapping]] = ..., conversation_id: _Optional[str] = ..., redaction_config: _Optional[_Union[_resources_pb2.RedactionConfig, _Mapping]] = ..., speech_config: _Optional[_Union[_resources_pb2.SpeechConfig, _Mapping]] = ...) -> None: ...

class UploadConversationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "analysis_operation", "applied_redaction_config")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_OPERATION_FIELD_NUMBER: _ClassVar[int]
    APPLIED_REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: UploadConversationRequest
    analysis_operation: str
    applied_redaction_config: _resources_pb2.RedactionConfig
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[UploadConversationRequest, _Mapping]] = ..., analysis_operation: _Optional[str] = ..., applied_redaction_config: _Optional[_Union[_resources_pb2.RedactionConfig, _Mapping]] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: ConversationView
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., view: _Optional[_Union[ConversationView, str]] = ...) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations", "next_page_token")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Conversation]
    next_page_token: str
    def __init__(self, conversations: _Optional[_Iterable[_Union[_resources_pb2.Conversation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ConversationView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[ConversationView, str]] = ...) -> None: ...

class UpdateConversationRequest(_message.Message):
    __slots__ = ("conversation", "update_mask")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    conversation: _resources_pb2.Conversation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, conversation: _Optional[_Union[_resources_pb2.Conversation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class IngestConversationsRequest(_message.Message):
    __slots__ = ("gcs_source", "transcript_object_config", "parent", "conversation_config", "redaction_config", "speech_config", "sample_size")
    class GcsSource(_message.Message):
        __slots__ = ("bucket_uri", "bucket_object_type", "metadata_bucket_uri", "custom_metadata_keys")
        class BucketObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BUCKET_OBJECT_TYPE_UNSPECIFIED: _ClassVar[IngestConversationsRequest.GcsSource.BucketObjectType]
            TRANSCRIPT: _ClassVar[IngestConversationsRequest.GcsSource.BucketObjectType]
            AUDIO: _ClassVar[IngestConversationsRequest.GcsSource.BucketObjectType]
        BUCKET_OBJECT_TYPE_UNSPECIFIED: IngestConversationsRequest.GcsSource.BucketObjectType
        TRANSCRIPT: IngestConversationsRequest.GcsSource.BucketObjectType
        AUDIO: IngestConversationsRequest.GcsSource.BucketObjectType
        BUCKET_URI_FIELD_NUMBER: _ClassVar[int]
        BUCKET_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        METADATA_BUCKET_URI_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_METADATA_KEYS_FIELD_NUMBER: _ClassVar[int]
        bucket_uri: str
        bucket_object_type: IngestConversationsRequest.GcsSource.BucketObjectType
        metadata_bucket_uri: str
        custom_metadata_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, bucket_uri: _Optional[str] = ..., bucket_object_type: _Optional[_Union[IngestConversationsRequest.GcsSource.BucketObjectType, str]] = ..., metadata_bucket_uri: _Optional[str] = ..., custom_metadata_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class TranscriptObjectConfig(_message.Message):
        __slots__ = ("medium",)
        MEDIUM_FIELD_NUMBER: _ClassVar[int]
        medium: _resources_pb2.Conversation.Medium
        def __init__(self, medium: _Optional[_Union[_resources_pb2.Conversation.Medium, str]] = ...) -> None: ...
    class ConversationConfig(_message.Message):
        __slots__ = ("agent_id", "agent_channel", "customer_channel")
        AGENT_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        agent_id: str
        agent_channel: int
        customer_channel: int
        def __init__(self, agent_id: _Optional[str] = ..., agent_channel: _Optional[int] = ..., customer_channel: _Optional[int] = ...) -> None: ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_OBJECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: IngestConversationsRequest.GcsSource
    transcript_object_config: IngestConversationsRequest.TranscriptObjectConfig
    parent: str
    conversation_config: IngestConversationsRequest.ConversationConfig
    redaction_config: _resources_pb2.RedactionConfig
    speech_config: _resources_pb2.SpeechConfig
    sample_size: int
    def __init__(self, gcs_source: _Optional[_Union[IngestConversationsRequest.GcsSource, _Mapping]] = ..., transcript_object_config: _Optional[_Union[IngestConversationsRequest.TranscriptObjectConfig, _Mapping]] = ..., parent: _Optional[str] = ..., conversation_config: _Optional[_Union[IngestConversationsRequest.ConversationConfig, _Mapping]] = ..., redaction_config: _Optional[_Union[_resources_pb2.RedactionConfig, _Mapping]] = ..., speech_config: _Optional[_Union[_resources_pb2.SpeechConfig, _Mapping]] = ..., sample_size: _Optional[int] = ...) -> None: ...

class IngestConversationsMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors", "ingest_conversations_stats")
    class IngestConversationsStats(_message.Message):
        __slots__ = ("processed_object_count", "duplicates_skipped_count", "successful_ingest_count", "failed_ingest_count")
        PROCESSED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        DUPLICATES_SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUCCESSFUL_INGEST_COUNT_FIELD_NUMBER: _ClassVar[int]
        FAILED_INGEST_COUNT_FIELD_NUMBER: _ClassVar[int]
        processed_object_count: int
        duplicates_skipped_count: int
        successful_ingest_count: int
        failed_ingest_count: int
        def __init__(self, processed_object_count: _Optional[int] = ..., duplicates_skipped_count: _Optional[int] = ..., successful_ingest_count: _Optional[int] = ..., failed_ingest_count: _Optional[int] = ...) -> None: ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    INGEST_CONVERSATIONS_STATS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: IngestConversationsRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    ingest_conversations_stats: IngestConversationsMetadata.IngestConversationsStats
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[IngestConversationsRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., ingest_conversations_stats: _Optional[_Union[IngestConversationsMetadata.IngestConversationsStats, _Mapping]] = ...) -> None: ...

class IngestConversationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateAnalysisRequest(_message.Message):
    __slots__ = ("parent", "analysis")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    analysis: _resources_pb2.Analysis
    def __init__(self, parent: _Optional[str] = ..., analysis: _Optional[_Union[_resources_pb2.Analysis, _Mapping]] = ...) -> None: ...

class ListAnalysesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAnalysesResponse(_message.Message):
    __slots__ = ("analyses", "next_page_token")
    ANALYSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    analyses: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Analysis]
    next_page_token: str
    def __init__(self, analyses: _Optional[_Iterable[_Union[_resources_pb2.Analysis, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAnalysisRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteAnalysisRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BulkAnalyzeConversationsRequest(_message.Message):
    __slots__ = ("parent", "filter", "analysis_percentage", "annotator_selector")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATOR_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    analysis_percentage: float
    annotator_selector: _resources_pb2.AnnotatorSelector
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., analysis_percentage: _Optional[float] = ..., annotator_selector: _Optional[_Union[_resources_pb2.AnnotatorSelector, _Mapping]] = ...) -> None: ...

class BulkAnalyzeConversationsMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "completed_analyses_count", "failed_analyses_count", "total_requested_analyses_count", "partial_errors")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_ANALYSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ANALYSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REQUESTED_ANALYSES_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: BulkAnalyzeConversationsRequest
    completed_analyses_count: int
    failed_analyses_count: int
    total_requested_analyses_count: int
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[BulkAnalyzeConversationsRequest, _Mapping]] = ..., completed_analyses_count: _Optional[int] = ..., failed_analyses_count: _Optional[int] = ..., total_requested_analyses_count: _Optional[int] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class BulkAnalyzeConversationsResponse(_message.Message):
    __slots__ = ("successful_analysis_count", "failed_analysis_count")
    SUCCESSFUL_ANALYSIS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ANALYSIS_COUNT_FIELD_NUMBER: _ClassVar[int]
    successful_analysis_count: int
    failed_analysis_count: int
    def __init__(self, successful_analysis_count: _Optional[int] = ..., failed_analysis_count: _Optional[int] = ...) -> None: ...

class BulkDeleteConversationsRequest(_message.Message):
    __slots__ = ("parent", "filter", "max_delete_count", "force")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_DELETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    max_delete_count: int
    force: bool
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., max_delete_count: _Optional[int] = ..., force: bool = ...) -> None: ...

class BulkDeleteConversationsMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: BulkDeleteConversationsRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[BulkDeleteConversationsRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class BulkDeleteConversationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportInsightsDataRequest(_message.Message):
    __slots__ = ("big_query_destination", "parent", "filter", "kms_key", "write_disposition")
    class WriteDisposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WRITE_DISPOSITION_UNSPECIFIED: _ClassVar[ExportInsightsDataRequest.WriteDisposition]
        WRITE_TRUNCATE: _ClassVar[ExportInsightsDataRequest.WriteDisposition]
        WRITE_APPEND: _ClassVar[ExportInsightsDataRequest.WriteDisposition]
    WRITE_DISPOSITION_UNSPECIFIED: ExportInsightsDataRequest.WriteDisposition
    WRITE_TRUNCATE: ExportInsightsDataRequest.WriteDisposition
    WRITE_APPEND: ExportInsightsDataRequest.WriteDisposition
    class BigQueryDestination(_message.Message):
        __slots__ = ("project_id", "dataset", "table")
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        DATASET_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        dataset: str
        table: str
        def __init__(self, project_id: _Optional[str] = ..., dataset: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    BIG_QUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    big_query_destination: ExportInsightsDataRequest.BigQueryDestination
    parent: str
    filter: str
    kms_key: str
    write_disposition: ExportInsightsDataRequest.WriteDisposition
    def __init__(self, big_query_destination: _Optional[_Union[ExportInsightsDataRequest.BigQueryDestination, _Mapping]] = ..., parent: _Optional[str] = ..., filter: _Optional[str] = ..., kms_key: _Optional[str] = ..., write_disposition: _Optional[_Union[ExportInsightsDataRequest.WriteDisposition, str]] = ...) -> None: ...

class ExportInsightsDataMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: ExportInsightsDataRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[ExportInsightsDataRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class ExportInsightsDataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateIssueModelRequest(_message.Message):
    __slots__ = ("parent", "issue_model")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    issue_model: _resources_pb2.IssueModel
    def __init__(self, parent: _Optional[str] = ..., issue_model: _Optional[_Union[_resources_pb2.IssueModel, _Mapping]] = ...) -> None: ...

class CreateIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: CreateIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[CreateIssueModelRequest, _Mapping]] = ...) -> None: ...

class UpdateIssueModelRequest(_message.Message):
    __slots__ = ("issue_model", "update_mask")
    ISSUE_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    issue_model: _resources_pb2.IssueModel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, issue_model: _Optional[_Union[_resources_pb2.IssueModel, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListIssueModelsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListIssueModelsResponse(_message.Message):
    __slots__ = ("issue_models",)
    ISSUE_MODELS_FIELD_NUMBER: _ClassVar[int]
    issue_models: _containers.RepeatedCompositeFieldContainer[_resources_pb2.IssueModel]
    def __init__(self, issue_models: _Optional[_Iterable[_Union[_resources_pb2.IssueModel, _Mapping]]] = ...) -> None: ...

class GetIssueModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteIssueModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: DeleteIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[DeleteIssueModelRequest, _Mapping]] = ...) -> None: ...

class DeployIssueModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeployIssueModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeployIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: DeployIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[DeployIssueModelRequest, _Mapping]] = ...) -> None: ...

class UndeployIssueModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UndeployIssueModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UndeployIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: UndeployIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[UndeployIssueModelRequest, _Mapping]] = ...) -> None: ...

class ExportIssueModelRequest(_message.Message):
    __slots__ = ("gcs_destination", "name")
    class GcsDestination(_message.Message):
        __slots__ = ("object_uri",)
        OBJECT_URI_FIELD_NUMBER: _ClassVar[int]
        object_uri: str
        def __init__(self, object_uri: _Optional[str] = ...) -> None: ...
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: ExportIssueModelRequest.GcsDestination
    name: str
    def __init__(self, gcs_destination: _Optional[_Union[ExportIssueModelRequest.GcsDestination, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ExportIssueModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: ExportIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[ExportIssueModelRequest, _Mapping]] = ...) -> None: ...

class ImportIssueModelRequest(_message.Message):
    __slots__ = ("gcs_source", "parent", "create_new_model")
    class GcsSource(_message.Message):
        __slots__ = ("object_uri",)
        OBJECT_URI_FIELD_NUMBER: _ClassVar[int]
        object_uri: str
        def __init__(self, object_uri: _Optional[str] = ...) -> None: ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_MODEL_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportIssueModelRequest.GcsSource
    parent: str
    create_new_model: bool
    def __init__(self, gcs_source: _Optional[_Union[ImportIssueModelRequest.GcsSource, _Mapping]] = ..., parent: _Optional[str] = ..., create_new_model: bool = ...) -> None: ...

class ImportIssueModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImportIssueModelMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: ImportIssueModelRequest
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[ImportIssueModelRequest, _Mapping]] = ...) -> None: ...

class GetIssueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIssuesRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListIssuesResponse(_message.Message):
    __slots__ = ("issues",)
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Issue]
    def __init__(self, issues: _Optional[_Iterable[_Union[_resources_pb2.Issue, _Mapping]]] = ...) -> None: ...

class UpdateIssueRequest(_message.Message):
    __slots__ = ("issue", "update_mask")
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    issue: _resources_pb2.Issue
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, issue: _Optional[_Union[_resources_pb2.Issue, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteIssueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CalculateIssueModelStatsRequest(_message.Message):
    __slots__ = ("issue_model",)
    ISSUE_MODEL_FIELD_NUMBER: _ClassVar[int]
    issue_model: str
    def __init__(self, issue_model: _Optional[str] = ...) -> None: ...

class CalculateIssueModelStatsResponse(_message.Message):
    __slots__ = ("current_stats",)
    CURRENT_STATS_FIELD_NUMBER: _ClassVar[int]
    current_stats: _resources_pb2.IssueModelLabelStats
    def __init__(self, current_stats: _Optional[_Union[_resources_pb2.IssueModelLabelStats, _Mapping]] = ...) -> None: ...

class CreatePhraseMatcherRequest(_message.Message):
    __slots__ = ("parent", "phrase_matcher")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    phrase_matcher: _resources_pb2.PhraseMatcher
    def __init__(self, parent: _Optional[str] = ..., phrase_matcher: _Optional[_Union[_resources_pb2.PhraseMatcher, _Mapping]] = ...) -> None: ...

class ListPhraseMatchersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListPhraseMatchersResponse(_message.Message):
    __slots__ = ("phrase_matchers", "next_page_token")
    PHRASE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phrase_matchers: _containers.RepeatedCompositeFieldContainer[_resources_pb2.PhraseMatcher]
    next_page_token: str
    def __init__(self, phrase_matchers: _Optional[_Iterable[_Union[_resources_pb2.PhraseMatcher, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetPhraseMatcherRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeletePhraseMatcherRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdatePhraseMatcherRequest(_message.Message):
    __slots__ = ("phrase_matcher", "update_mask")
    PHRASE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    phrase_matcher: _resources_pb2.PhraseMatcher
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, phrase_matcher: _Optional[_Union[_resources_pb2.PhraseMatcher, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ("settings", "update_mask")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    settings: _resources_pb2.Settings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, settings: _Optional[_Union[_resources_pb2.Settings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateAnalysisRuleRequest(_message.Message):
    __slots__ = ("parent", "analysis_rule")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    analysis_rule: _resources_pb2.AnalysisRule
    def __init__(self, parent: _Optional[str] = ..., analysis_rule: _Optional[_Union[_resources_pb2.AnalysisRule, _Mapping]] = ...) -> None: ...

class GetAnalysisRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAnalysisRuleRequest(_message.Message):
    __slots__ = ("analysis_rule", "update_mask")
    ANALYSIS_RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    analysis_rule: _resources_pb2.AnalysisRule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, analysis_rule: _Optional[_Union[_resources_pb2.AnalysisRule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAnalysisRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAnalysisRulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAnalysisRulesResponse(_message.Message):
    __slots__ = ("analysis_rules", "next_page_token")
    ANALYSIS_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    analysis_rules: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AnalysisRule]
    next_page_token: str
    def __init__(self, analysis_rules: _Optional[_Iterable[_Union[_resources_pb2.AnalysisRule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetEncryptionSpecRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InitializeEncryptionSpecRequest(_message.Message):
    __slots__ = ("encryption_spec",)
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    encryption_spec: _resources_pb2.EncryptionSpec
    def __init__(self, encryption_spec: _Optional[_Union[_resources_pb2.EncryptionSpec, _Mapping]] = ...) -> None: ...

class InitializeEncryptionSpecResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitializeEncryptionSpecMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: InitializeEncryptionSpecRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[InitializeEncryptionSpecRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class CreateViewRequest(_message.Message):
    __slots__ = ("parent", "view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: _resources_pb2.View
    def __init__(self, parent: _Optional[str] = ..., view: _Optional[_Union[_resources_pb2.View, _Mapping]] = ...) -> None: ...

class GetViewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListViewsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListViewsResponse(_message.Message):
    __slots__ = ("views", "next_page_token")
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    views: _containers.RepeatedCompositeFieldContainer[_resources_pb2.View]
    next_page_token: str
    def __init__(self, views: _Optional[_Iterable[_Union[_resources_pb2.View, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateViewRequest(_message.Message):
    __slots__ = ("view", "update_mask")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    view: _resources_pb2.View
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, view: _Optional[_Union[_resources_pb2.View, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteViewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Dimension(_message.Message):
    __slots__ = ("issue_dimension_metadata", "agent_dimension_metadata", "qa_question_dimension_metadata", "qa_question_answer_dimension_metadata", "dimension_key")
    class DimensionKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIMENSION_KEY_UNSPECIFIED: _ClassVar[Dimension.DimensionKey]
        ISSUE: _ClassVar[Dimension.DimensionKey]
        AGENT: _ClassVar[Dimension.DimensionKey]
        AGENT_TEAM: _ClassVar[Dimension.DimensionKey]
        QA_QUESTION_ID: _ClassVar[Dimension.DimensionKey]
        QA_QUESTION_ANSWER_VALUE: _ClassVar[Dimension.DimensionKey]
        CONVERSATION_PROFILE_ID: _ClassVar[Dimension.DimensionKey]
    DIMENSION_KEY_UNSPECIFIED: Dimension.DimensionKey
    ISSUE: Dimension.DimensionKey
    AGENT: Dimension.DimensionKey
    AGENT_TEAM: Dimension.DimensionKey
    QA_QUESTION_ID: Dimension.DimensionKey
    QA_QUESTION_ANSWER_VALUE: Dimension.DimensionKey
    CONVERSATION_PROFILE_ID: Dimension.DimensionKey
    class IssueDimensionMetadata(_message.Message):
        __slots__ = ("issue_id", "issue_display_name", "issue_model_id")
        ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
        ISSUE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ISSUE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        issue_id: str
        issue_display_name: str
        issue_model_id: str
        def __init__(self, issue_id: _Optional[str] = ..., issue_display_name: _Optional[str] = ..., issue_model_id: _Optional[str] = ...) -> None: ...
    class AgentDimensionMetadata(_message.Message):
        __slots__ = ("agent_id", "agent_display_name", "agent_team")
        AGENT_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        AGENT_TEAM_FIELD_NUMBER: _ClassVar[int]
        agent_id: str
        agent_display_name: str
        agent_team: str
        def __init__(self, agent_id: _Optional[str] = ..., agent_display_name: _Optional[str] = ..., agent_team: _Optional[str] = ...) -> None: ...
    class QaQuestionDimensionMetadata(_message.Message):
        __slots__ = ("qa_scorecard_id", "qa_question_id", "question_body")
        QA_SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
        QA_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        QUESTION_BODY_FIELD_NUMBER: _ClassVar[int]
        qa_scorecard_id: str
        qa_question_id: str
        question_body: str
        def __init__(self, qa_scorecard_id: _Optional[str] = ..., qa_question_id: _Optional[str] = ..., question_body: _Optional[str] = ...) -> None: ...
    class QaQuestionAnswerDimensionMetadata(_message.Message):
        __slots__ = ("qa_scorecard_id", "qa_question_id", "question_body", "answer_value")
        QA_SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
        QA_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        QUESTION_BODY_FIELD_NUMBER: _ClassVar[int]
        ANSWER_VALUE_FIELD_NUMBER: _ClassVar[int]
        qa_scorecard_id: str
        qa_question_id: str
        question_body: str
        answer_value: str
        def __init__(self, qa_scorecard_id: _Optional[str] = ..., qa_question_id: _Optional[str] = ..., question_body: _Optional[str] = ..., answer_value: _Optional[str] = ...) -> None: ...
    ISSUE_DIMENSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    AGENT_DIMENSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_DIMENSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_ANSWER_DIMENSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_KEY_FIELD_NUMBER: _ClassVar[int]
    issue_dimension_metadata: Dimension.IssueDimensionMetadata
    agent_dimension_metadata: Dimension.AgentDimensionMetadata
    qa_question_dimension_metadata: Dimension.QaQuestionDimensionMetadata
    qa_question_answer_dimension_metadata: Dimension.QaQuestionAnswerDimensionMetadata
    dimension_key: Dimension.DimensionKey
    def __init__(self, issue_dimension_metadata: _Optional[_Union[Dimension.IssueDimensionMetadata, _Mapping]] = ..., agent_dimension_metadata: _Optional[_Union[Dimension.AgentDimensionMetadata, _Mapping]] = ..., qa_question_dimension_metadata: _Optional[_Union[Dimension.QaQuestionDimensionMetadata, _Mapping]] = ..., qa_question_answer_dimension_metadata: _Optional[_Union[Dimension.QaQuestionAnswerDimensionMetadata, _Mapping]] = ..., dimension_key: _Optional[_Union[Dimension.DimensionKey, str]] = ...) -> None: ...

class QueryMetricsRequest(_message.Message):
    __slots__ = ("location", "filter", "time_granularity", "dimensions", "measure_mask")
    class TimeGranularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_GRANULARITY_UNSPECIFIED: _ClassVar[QueryMetricsRequest.TimeGranularity]
        NONE: _ClassVar[QueryMetricsRequest.TimeGranularity]
        DAILY: _ClassVar[QueryMetricsRequest.TimeGranularity]
        HOURLY: _ClassVar[QueryMetricsRequest.TimeGranularity]
        PER_MINUTE: _ClassVar[QueryMetricsRequest.TimeGranularity]
        PER_5_MINUTES: _ClassVar[QueryMetricsRequest.TimeGranularity]
        MONTHLY: _ClassVar[QueryMetricsRequest.TimeGranularity]
    TIME_GRANULARITY_UNSPECIFIED: QueryMetricsRequest.TimeGranularity
    NONE: QueryMetricsRequest.TimeGranularity
    DAILY: QueryMetricsRequest.TimeGranularity
    HOURLY: QueryMetricsRequest.TimeGranularity
    PER_MINUTE: QueryMetricsRequest.TimeGranularity
    PER_5_MINUTES: QueryMetricsRequest.TimeGranularity
    MONTHLY: QueryMetricsRequest.TimeGranularity
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    MEASURE_MASK_FIELD_NUMBER: _ClassVar[int]
    location: str
    filter: str
    time_granularity: QueryMetricsRequest.TimeGranularity
    dimensions: _containers.RepeatedCompositeFieldContainer[Dimension]
    measure_mask: _field_mask_pb2.FieldMask
    def __init__(self, location: _Optional[str] = ..., filter: _Optional[str] = ..., time_granularity: _Optional[_Union[QueryMetricsRequest.TimeGranularity, str]] = ..., dimensions: _Optional[_Iterable[_Union[Dimension, _Mapping]]] = ..., measure_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class QueryMetricsResponse(_message.Message):
    __slots__ = ("location", "update_time", "slices", "macro_average_slice")
    class Slice(_message.Message):
        __slots__ = ("dimensions", "total", "time_series")
        class DataPoint(_message.Message):
            __slots__ = ("conversation_measure", "interval")
            class ConversationMeasure(_message.Message):
                __slots__ = ("conversation_count", "average_silence_percentage", "average_duration", "average_turn_count", "average_agent_sentiment_score", "average_client_sentiment_score", "average_customer_satisfaction_rating", "average_qa_normalized_score", "qa_tag_scores", "average_qa_question_normalized_score")
                class QaTagScore(_message.Message):
                    __slots__ = ("tag", "average_tag_normalized_score")
                    TAG_FIELD_NUMBER: _ClassVar[int]
                    AVERAGE_TAG_NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
                    tag: str
                    average_tag_normalized_score: float
                    def __init__(self, tag: _Optional[str] = ..., average_tag_normalized_score: _Optional[float] = ...) -> None: ...
                CONVERSATION_COUNT_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_SILENCE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_DURATION_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_TURN_COUNT_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_AGENT_SENTIMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_CLIENT_SENTIMENT_SCORE_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_CUSTOMER_SATISFACTION_RATING_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_QA_NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
                QA_TAG_SCORES_FIELD_NUMBER: _ClassVar[int]
                AVERAGE_QA_QUESTION_NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
                conversation_count: int
                average_silence_percentage: float
                average_duration: _duration_pb2.Duration
                average_turn_count: float
                average_agent_sentiment_score: float
                average_client_sentiment_score: float
                average_customer_satisfaction_rating: float
                average_qa_normalized_score: float
                qa_tag_scores: _containers.RepeatedCompositeFieldContainer[QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore]
                average_qa_question_normalized_score: float
                def __init__(self, conversation_count: _Optional[int] = ..., average_silence_percentage: _Optional[float] = ..., average_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., average_turn_count: _Optional[float] = ..., average_agent_sentiment_score: _Optional[float] = ..., average_client_sentiment_score: _Optional[float] = ..., average_customer_satisfaction_rating: _Optional[float] = ..., average_qa_normalized_score: _Optional[float] = ..., qa_tag_scores: _Optional[_Iterable[_Union[QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore, _Mapping]]] = ..., average_qa_question_normalized_score: _Optional[float] = ...) -> None: ...
            CONVERSATION_MEASURE_FIELD_NUMBER: _ClassVar[int]
            INTERVAL_FIELD_NUMBER: _ClassVar[int]
            conversation_measure: QueryMetricsResponse.Slice.DataPoint.ConversationMeasure
            interval: _interval_pb2.Interval
            def __init__(self, conversation_measure: _Optional[_Union[QueryMetricsResponse.Slice.DataPoint.ConversationMeasure, _Mapping]] = ..., interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ...) -> None: ...
        class TimeSeries(_message.Message):
            __slots__ = ("data_points",)
            DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
            data_points: _containers.RepeatedCompositeFieldContainer[QueryMetricsResponse.Slice.DataPoint]
            def __init__(self, data_points: _Optional[_Iterable[_Union[QueryMetricsResponse.Slice.DataPoint, _Mapping]]] = ...) -> None: ...
        DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
        dimensions: _containers.RepeatedCompositeFieldContainer[Dimension]
        total: QueryMetricsResponse.Slice.DataPoint
        time_series: QueryMetricsResponse.Slice.TimeSeries
        def __init__(self, dimensions: _Optional[_Iterable[_Union[Dimension, _Mapping]]] = ..., total: _Optional[_Union[QueryMetricsResponse.Slice.DataPoint, _Mapping]] = ..., time_series: _Optional[_Union[QueryMetricsResponse.Slice.TimeSeries, _Mapping]] = ...) -> None: ...
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    MACRO_AVERAGE_SLICE_FIELD_NUMBER: _ClassVar[int]
    location: str
    update_time: _timestamp_pb2.Timestamp
    slices: _containers.RepeatedCompositeFieldContainer[QueryMetricsResponse.Slice]
    macro_average_slice: QueryMetricsResponse.Slice
    def __init__(self, location: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., slices: _Optional[_Iterable[_Union[QueryMetricsResponse.Slice, _Mapping]]] = ..., macro_average_slice: _Optional[_Union[QueryMetricsResponse.Slice, _Mapping]] = ...) -> None: ...

class QueryMetricsMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateQaQuestionRequest(_message.Message):
    __slots__ = ("parent", "qa_question", "qa_question_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    qa_question: _resources_pb2.QaQuestion
    qa_question_id: str
    def __init__(self, parent: _Optional[str] = ..., qa_question: _Optional[_Union[_resources_pb2.QaQuestion, _Mapping]] = ..., qa_question_id: _Optional[str] = ...) -> None: ...

class GetQaQuestionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListQaQuestionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListQaQuestionsResponse(_message.Message):
    __slots__ = ("qa_questions", "next_page_token")
    QA_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    qa_questions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.QaQuestion]
    next_page_token: str
    def __init__(self, qa_questions: _Optional[_Iterable[_Union[_resources_pb2.QaQuestion, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateQaQuestionRequest(_message.Message):
    __slots__ = ("qa_question", "update_mask")
    QA_QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    qa_question: _resources_pb2.QaQuestion
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, qa_question: _Optional[_Union[_resources_pb2.QaQuestion, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteQaQuestionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateQaScorecardRequest(_message.Message):
    __slots__ = ("parent", "qa_scorecard", "qa_scorecard_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QA_SCORECARD_FIELD_NUMBER: _ClassVar[int]
    QA_SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    qa_scorecard: _resources_pb2.QaScorecard
    qa_scorecard_id: str
    def __init__(self, parent: _Optional[str] = ..., qa_scorecard: _Optional[_Union[_resources_pb2.QaScorecard, _Mapping]] = ..., qa_scorecard_id: _Optional[str] = ...) -> None: ...

class GetQaScorecardRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateQaScorecardRequest(_message.Message):
    __slots__ = ("qa_scorecard", "update_mask")
    QA_SCORECARD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    qa_scorecard: _resources_pb2.QaScorecard
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, qa_scorecard: _Optional[_Union[_resources_pb2.QaScorecard, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteQaScorecardRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class CreateQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("parent", "qa_scorecard_revision", "qa_scorecard_revision_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QA_SCORECARD_REVISION_FIELD_NUMBER: _ClassVar[int]
    QA_SCORECARD_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    qa_scorecard_revision: _resources_pb2.QaScorecardRevision
    qa_scorecard_revision_id: str
    def __init__(self, parent: _Optional[str] = ..., qa_scorecard_revision: _Optional[_Union[_resources_pb2.QaScorecardRevision, _Mapping]] = ..., qa_scorecard_revision_id: _Optional[str] = ...) -> None: ...

class GetQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TuneQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("parent", "filter", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class TuneQaScorecardRevisionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TuneQaScorecardRevisionMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "qa_question_dataset_validation_results", "qa_question_dataset_tuning_metrics", "tuning_completion_ratio")
    class QaQuestionDatasetValidationResult(_message.Message):
        __slots__ = ("question", "dataset_validation_warnings", "valid_feedback_labels_count")
        QUESTION_FIELD_NUMBER: _ClassVar[int]
        DATASET_VALIDATION_WARNINGS_FIELD_NUMBER: _ClassVar[int]
        VALID_FEEDBACK_LABELS_COUNT_FIELD_NUMBER: _ClassVar[int]
        question: str
        dataset_validation_warnings: _containers.RepeatedScalarFieldContainer[_resources_pb2.DatasetValidationWarning]
        valid_feedback_labels_count: int
        def __init__(self, question: _Optional[str] = ..., dataset_validation_warnings: _Optional[_Iterable[_Union[_resources_pb2.DatasetValidationWarning, str]]] = ..., valid_feedback_labels_count: _Optional[int] = ...) -> None: ...
    class QaQuestionDatasetTuningMetrics(_message.Message):
        __slots__ = ("question", "metrics")
        class Metrics(_message.Message):
            __slots__ = ("accuracy",)
            ACCURACY_FIELD_NUMBER: _ClassVar[int]
            accuracy: float
            def __init__(self, accuracy: _Optional[float] = ...) -> None: ...
        QUESTION_FIELD_NUMBER: _ClassVar[int]
        METRICS_FIELD_NUMBER: _ClassVar[int]
        question: str
        metrics: TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics
        def __init__(self, question: _Optional[str] = ..., metrics: _Optional[_Union[TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics, _Mapping]] = ...) -> None: ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_DATASET_VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    QA_QUESTION_DATASET_TUNING_METRICS_FIELD_NUMBER: _ClassVar[int]
    TUNING_COMPLETION_RATIO_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: TuneQaScorecardRevisionRequest
    qa_question_dataset_validation_results: _containers.RepeatedCompositeFieldContainer[TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult]
    qa_question_dataset_tuning_metrics: _containers.RepeatedCompositeFieldContainer[TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics]
    tuning_completion_ratio: float
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[TuneQaScorecardRevisionRequest, _Mapping]] = ..., qa_question_dataset_validation_results: _Optional[_Iterable[_Union[TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult, _Mapping]]] = ..., qa_question_dataset_tuning_metrics: _Optional[_Iterable[_Union[TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics, _Mapping]]] = ..., tuning_completion_ratio: _Optional[float] = ...) -> None: ...

class DeployQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UndeployQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteQaScorecardRevisionRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListQaScorecardsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListQaScorecardsResponse(_message.Message):
    __slots__ = ("qa_scorecards", "next_page_token")
    QA_SCORECARDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    qa_scorecards: _containers.RepeatedCompositeFieldContainer[_resources_pb2.QaScorecard]
    next_page_token: str
    def __init__(self, qa_scorecards: _Optional[_Iterable[_Union[_resources_pb2.QaScorecard, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListQaScorecardRevisionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListQaScorecardRevisionsResponse(_message.Message):
    __slots__ = ("qa_scorecard_revisions", "next_page_token")
    QA_SCORECARD_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    qa_scorecard_revisions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.QaScorecardRevision]
    next_page_token: str
    def __init__(self, qa_scorecard_revisions: _Optional[_Iterable[_Union[_resources_pb2.QaScorecardRevision, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateFeedbackLabelRequest(_message.Message):
    __slots__ = ("parent", "feedback_label_id", "feedback_label")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_LABEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feedback_label_id: str
    feedback_label: _resources_pb2.FeedbackLabel
    def __init__(self, parent: _Optional[str] = ..., feedback_label_id: _Optional[str] = ..., feedback_label: _Optional[_Union[_resources_pb2.FeedbackLabel, _Mapping]] = ...) -> None: ...

class ListFeedbackLabelsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListFeedbackLabelsResponse(_message.Message):
    __slots__ = ("feedback_labels", "next_page_token")
    FEEDBACK_LABELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feedback_labels: _containers.RepeatedCompositeFieldContainer[_resources_pb2.FeedbackLabel]
    next_page_token: str
    def __init__(self, feedback_labels: _Optional[_Iterable[_Union[_resources_pb2.FeedbackLabel, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetFeedbackLabelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateFeedbackLabelRequest(_message.Message):
    __slots__ = ("feedback_label", "update_mask")
    FEEDBACK_LABEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feedback_label: _resources_pb2.FeedbackLabel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, feedback_label: _Optional[_Union[_resources_pb2.FeedbackLabel, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFeedbackLabelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAllFeedbackLabelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAllFeedbackLabelsResponse(_message.Message):
    __slots__ = ("feedback_labels", "next_page_token")
    FEEDBACK_LABELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feedback_labels: _containers.RepeatedCompositeFieldContainer[_resources_pb2.FeedbackLabel]
    next_page_token: str
    def __init__(self, feedback_labels: _Optional[_Iterable[_Union[_resources_pb2.FeedbackLabel, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class BulkUploadFeedbackLabelsRequest(_message.Message):
    __slots__ = ("gcs_source", "parent", "validate_only")
    class GcsSource(_message.Message):
        __slots__ = ("format", "object_uri")
        class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FORMAT_UNSPECIFIED: _ClassVar[BulkUploadFeedbackLabelsRequest.GcsSource.Format]
            CSV: _ClassVar[BulkUploadFeedbackLabelsRequest.GcsSource.Format]
            JSON: _ClassVar[BulkUploadFeedbackLabelsRequest.GcsSource.Format]
        FORMAT_UNSPECIFIED: BulkUploadFeedbackLabelsRequest.GcsSource.Format
        CSV: BulkUploadFeedbackLabelsRequest.GcsSource.Format
        JSON: BulkUploadFeedbackLabelsRequest.GcsSource.Format
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        OBJECT_URI_FIELD_NUMBER: _ClassVar[int]
        format: BulkUploadFeedbackLabelsRequest.GcsSource.Format
        object_uri: str
        def __init__(self, format: _Optional[_Union[BulkUploadFeedbackLabelsRequest.GcsSource.Format, str]] = ..., object_uri: _Optional[str] = ...) -> None: ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    gcs_source: BulkUploadFeedbackLabelsRequest.GcsSource
    parent: str
    validate_only: bool
    def __init__(self, gcs_source: _Optional[_Union[BulkUploadFeedbackLabelsRequest.GcsSource, _Mapping]] = ..., parent: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class BulkUploadFeedbackLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkUploadFeedbackLabelsMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors", "upload_stats")
    class UploadStats(_message.Message):
        __slots__ = ("processed_object_count", "failed_validation_count", "successful_upload_count")
        PROCESSED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        FAILED_VALIDATION_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUCCESSFUL_UPLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
        processed_object_count: int
        failed_validation_count: int
        successful_upload_count: int
        def __init__(self, processed_object_count: _Optional[int] = ..., failed_validation_count: _Optional[int] = ..., successful_upload_count: _Optional[int] = ...) -> None: ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_STATS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: BulkUploadFeedbackLabelsRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    upload_stats: BulkUploadFeedbackLabelsMetadata.UploadStats
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[BulkUploadFeedbackLabelsRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., upload_stats: _Optional[_Union[BulkUploadFeedbackLabelsMetadata.UploadStats, _Mapping]] = ...) -> None: ...

class BulkDownloadFeedbackLabelsRequest(_message.Message):
    __slots__ = ("gcs_destination", "parent", "filter", "max_download_count", "feedback_label_type", "conversation_filter", "template_qa_scorecard_id")
    class FeedbackLabelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEEDBACK_LABEL_TYPE_UNSPECIFIED: _ClassVar[BulkDownloadFeedbackLabelsRequest.FeedbackLabelType]
        QUALITY_AI: _ClassVar[BulkDownloadFeedbackLabelsRequest.FeedbackLabelType]
        TOPIC_MODELING: _ClassVar[BulkDownloadFeedbackLabelsRequest.FeedbackLabelType]
    FEEDBACK_LABEL_TYPE_UNSPECIFIED: BulkDownloadFeedbackLabelsRequest.FeedbackLabelType
    QUALITY_AI: BulkDownloadFeedbackLabelsRequest.FeedbackLabelType
    TOPIC_MODELING: BulkDownloadFeedbackLabelsRequest.FeedbackLabelType
    class GcsDestination(_message.Message):
        __slots__ = ("format", "object_uri", "add_whitespace", "always_print_empty_fields", "records_per_file_count")
        class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FORMAT_UNSPECIFIED: _ClassVar[BulkDownloadFeedbackLabelsRequest.GcsDestination.Format]
            CSV: _ClassVar[BulkDownloadFeedbackLabelsRequest.GcsDestination.Format]
            JSON: _ClassVar[BulkDownloadFeedbackLabelsRequest.GcsDestination.Format]
        FORMAT_UNSPECIFIED: BulkDownloadFeedbackLabelsRequest.GcsDestination.Format
        CSV: BulkDownloadFeedbackLabelsRequest.GcsDestination.Format
        JSON: BulkDownloadFeedbackLabelsRequest.GcsDestination.Format
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        OBJECT_URI_FIELD_NUMBER: _ClassVar[int]
        ADD_WHITESPACE_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_PRINT_EMPTY_FIELDS_FIELD_NUMBER: _ClassVar[int]
        RECORDS_PER_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        format: BulkDownloadFeedbackLabelsRequest.GcsDestination.Format
        object_uri: str
        add_whitespace: bool
        always_print_empty_fields: bool
        records_per_file_count: int
        def __init__(self, format: _Optional[_Union[BulkDownloadFeedbackLabelsRequest.GcsDestination.Format, str]] = ..., object_uri: _Optional[str] = ..., add_whitespace: bool = ..., always_print_empty_fields: bool = ..., records_per_file_count: _Optional[int] = ...) -> None: ...
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_LABEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_QA_SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: BulkDownloadFeedbackLabelsRequest.GcsDestination
    parent: str
    filter: str
    max_download_count: int
    feedback_label_type: BulkDownloadFeedbackLabelsRequest.FeedbackLabelType
    conversation_filter: str
    template_qa_scorecard_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gcs_destination: _Optional[_Union[BulkDownloadFeedbackLabelsRequest.GcsDestination, _Mapping]] = ..., parent: _Optional[str] = ..., filter: _Optional[str] = ..., max_download_count: _Optional[int] = ..., feedback_label_type: _Optional[_Union[BulkDownloadFeedbackLabelsRequest.FeedbackLabelType, str]] = ..., conversation_filter: _Optional[str] = ..., template_qa_scorecard_id: _Optional[_Iterable[str]] = ...) -> None: ...

class BulkDownloadFeedbackLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkDownloadFeedbackLabelsMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "request", "partial_errors", "download_stats")
    class DownloadStats(_message.Message):
        __slots__ = ("processed_object_count", "successful_download_count", "total_files_written", "file_names")
        PROCESSED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUCCESSFUL_DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FILES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
        FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
        processed_object_count: int
        successful_download_count: int
        total_files_written: int
        file_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, processed_object_count: _Optional[int] = ..., successful_download_count: _Optional[int] = ..., total_files_written: _Optional[int] = ..., file_names: _Optional[_Iterable[str]] = ...) -> None: ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STATS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    request: BulkDownloadFeedbackLabelsRequest
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    download_stats: BulkDownloadFeedbackLabelsMetadata.DownloadStats
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., request: _Optional[_Union[BulkDownloadFeedbackLabelsRequest, _Mapping]] = ..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., download_stats: _Optional[_Union[BulkDownloadFeedbackLabelsMetadata.DownloadStats, _Mapping]] = ...) -> None: ...
