from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4beta1 import common_pb2 as _common_pb2
from google.cloud.talent.v4beta1 import filters_pb2 as _filters_pb2
from google.cloud.talent.v4beta1 import histogram_pb2 as _histogram_pb2
from google.cloud.talent.v4beta1 import job_pb2 as _job_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_VIEW_UNSPECIFIED: _ClassVar[JobView]
    JOB_VIEW_ID_ONLY: _ClassVar[JobView]
    JOB_VIEW_MINIMAL: _ClassVar[JobView]
    JOB_VIEW_SMALL: _ClassVar[JobView]
    JOB_VIEW_FULL: _ClassVar[JobView]
JOB_VIEW_UNSPECIFIED: JobView
JOB_VIEW_ID_ONLY: JobView
JOB_VIEW_MINIMAL: JobView
JOB_VIEW_SMALL: JobView
JOB_VIEW_FULL: JobView

class CreateJobRequest(_message.Message):
    __slots__ = ('parent', 'job')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job: _job_pb2.Job

    def __init__(self, parent: _Optional[str]=..., job: _Optional[_Union[_job_pb2.Job, _Mapping]]=...) -> None:
        ...

class GetJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateJobRequest(_message.Message):
    __slots__ = ('job', 'update_mask')
    JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    job: _job_pb2.Job
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, job: _Optional[_Union[_job_pb2.Job, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchDeleteJobsRequest(_message.Message):
    __slots__ = ('parent', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListJobsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_token', 'page_size', 'job_view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    JOB_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_token: str
    page_size: int
    job_view: JobView

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., job_view: _Optional[_Union[JobView, str]]=...) -> None:
        ...

class ListJobsResponse(_message.Message):
    __slots__ = ('jobs', 'next_page_token', 'metadata')
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_job_pb2.Job]
    next_page_token: str
    metadata: _common_pb2.ResponseMetadata

    def __init__(self, jobs: _Optional[_Iterable[_Union[_job_pb2.Job, _Mapping]]]=..., next_page_token: _Optional[str]=..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]]=...) -> None:
        ...

class SearchJobsRequest(_message.Message):
    __slots__ = ('parent', 'search_mode', 'request_metadata', 'job_query', 'enable_broadening', 'require_precise_result_size', 'histogram_queries', 'job_view', 'offset', 'page_size', 'page_token', 'order_by', 'diversification_level', 'custom_ranking_info', 'disable_keyword_match', 'keyword_match_mode', 'relevance_threshold')

    class SearchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEARCH_MODE_UNSPECIFIED: _ClassVar[SearchJobsRequest.SearchMode]
        JOB_SEARCH: _ClassVar[SearchJobsRequest.SearchMode]
        FEATURED_JOB_SEARCH: _ClassVar[SearchJobsRequest.SearchMode]
    SEARCH_MODE_UNSPECIFIED: SearchJobsRequest.SearchMode
    JOB_SEARCH: SearchJobsRequest.SearchMode
    FEATURED_JOB_SEARCH: SearchJobsRequest.SearchMode

    class DiversificationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIVERSIFICATION_LEVEL_UNSPECIFIED: _ClassVar[SearchJobsRequest.DiversificationLevel]
        DISABLED: _ClassVar[SearchJobsRequest.DiversificationLevel]
        SIMPLE: _ClassVar[SearchJobsRequest.DiversificationLevel]
    DIVERSIFICATION_LEVEL_UNSPECIFIED: SearchJobsRequest.DiversificationLevel
    DISABLED: SearchJobsRequest.DiversificationLevel
    SIMPLE: SearchJobsRequest.DiversificationLevel

    class KeywordMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEYWORD_MATCH_MODE_UNSPECIFIED: _ClassVar[SearchJobsRequest.KeywordMatchMode]
        KEYWORD_MATCH_DISABLED: _ClassVar[SearchJobsRequest.KeywordMatchMode]
        KEYWORD_MATCH_ALL: _ClassVar[SearchJobsRequest.KeywordMatchMode]
        KEYWORD_MATCH_TITLE_ONLY: _ClassVar[SearchJobsRequest.KeywordMatchMode]
    KEYWORD_MATCH_MODE_UNSPECIFIED: SearchJobsRequest.KeywordMatchMode
    KEYWORD_MATCH_DISABLED: SearchJobsRequest.KeywordMatchMode
    KEYWORD_MATCH_ALL: SearchJobsRequest.KeywordMatchMode
    KEYWORD_MATCH_TITLE_ONLY: SearchJobsRequest.KeywordMatchMode

    class RelevanceThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEVANCE_THRESHOLD_UNSPECIFIED: _ClassVar[SearchJobsRequest.RelevanceThreshold]
        LOWEST: _ClassVar[SearchJobsRequest.RelevanceThreshold]
        LOW: _ClassVar[SearchJobsRequest.RelevanceThreshold]
        MEDIUM: _ClassVar[SearchJobsRequest.RelevanceThreshold]
        HIGH: _ClassVar[SearchJobsRequest.RelevanceThreshold]
    RELEVANCE_THRESHOLD_UNSPECIFIED: SearchJobsRequest.RelevanceThreshold
    LOWEST: SearchJobsRequest.RelevanceThreshold
    LOW: SearchJobsRequest.RelevanceThreshold
    MEDIUM: SearchJobsRequest.RelevanceThreshold
    HIGH: SearchJobsRequest.RelevanceThreshold

    class CustomRankingInfo(_message.Message):
        __slots__ = ('importance_level', 'ranking_expression')

        class ImportanceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IMPORTANCE_LEVEL_UNSPECIFIED: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            NONE: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            LOW: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            MILD: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            MEDIUM: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            HIGH: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
            EXTREME: _ClassVar[SearchJobsRequest.CustomRankingInfo.ImportanceLevel]
        IMPORTANCE_LEVEL_UNSPECIFIED: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        NONE: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        LOW: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        MILD: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        MEDIUM: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        HIGH: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        EXTREME: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        IMPORTANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        RANKING_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        importance_level: SearchJobsRequest.CustomRankingInfo.ImportanceLevel
        ranking_expression: str

        def __init__(self, importance_level: _Optional[_Union[SearchJobsRequest.CustomRankingInfo.ImportanceLevel, str]]=..., ranking_expression: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_MODE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    JOB_QUERY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BROADENING_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PRECISE_RESULT_SIZE_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_QUERIES_FIELD_NUMBER: _ClassVar[int]
    JOB_VIEW_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    DIVERSIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RANKING_INFO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_KEYWORD_MATCH_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    search_mode: SearchJobsRequest.SearchMode
    request_metadata: _common_pb2.RequestMetadata
    job_query: _filters_pb2.JobQuery
    enable_broadening: bool
    require_precise_result_size: bool
    histogram_queries: _containers.RepeatedCompositeFieldContainer[_histogram_pb2.HistogramQuery]
    job_view: JobView
    offset: int
    page_size: int
    page_token: str
    order_by: str
    diversification_level: SearchJobsRequest.DiversificationLevel
    custom_ranking_info: SearchJobsRequest.CustomRankingInfo
    disable_keyword_match: bool
    keyword_match_mode: SearchJobsRequest.KeywordMatchMode
    relevance_threshold: SearchJobsRequest.RelevanceThreshold

    def __init__(self, parent: _Optional[str]=..., search_mode: _Optional[_Union[SearchJobsRequest.SearchMode, str]]=..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]]=..., job_query: _Optional[_Union[_filters_pb2.JobQuery, _Mapping]]=..., enable_broadening: bool=..., require_precise_result_size: bool=..., histogram_queries: _Optional[_Iterable[_Union[_histogram_pb2.HistogramQuery, _Mapping]]]=..., job_view: _Optional[_Union[JobView, str]]=..., offset: _Optional[int]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., diversification_level: _Optional[_Union[SearchJobsRequest.DiversificationLevel, str]]=..., custom_ranking_info: _Optional[_Union[SearchJobsRequest.CustomRankingInfo, _Mapping]]=..., disable_keyword_match: bool=..., keyword_match_mode: _Optional[_Union[SearchJobsRequest.KeywordMatchMode, str]]=..., relevance_threshold: _Optional[_Union[SearchJobsRequest.RelevanceThreshold, str]]=...) -> None:
        ...

class SearchJobsResponse(_message.Message):
    __slots__ = ('matching_jobs', 'histogram_query_results', 'next_page_token', 'location_filters', 'estimated_total_size', 'total_size', 'metadata', 'broadened_query_jobs_count', 'spell_correction')

    class MatchingJob(_message.Message):
        __slots__ = ('job', 'job_summary', 'job_title_snippet', 'search_text_snippet', 'commute_info')
        JOB_FIELD_NUMBER: _ClassVar[int]
        JOB_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        JOB_TITLE_SNIPPET_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TEXT_SNIPPET_FIELD_NUMBER: _ClassVar[int]
        COMMUTE_INFO_FIELD_NUMBER: _ClassVar[int]
        job: _job_pb2.Job
        job_summary: str
        job_title_snippet: str
        search_text_snippet: str
        commute_info: SearchJobsResponse.CommuteInfo

        def __init__(self, job: _Optional[_Union[_job_pb2.Job, _Mapping]]=..., job_summary: _Optional[str]=..., job_title_snippet: _Optional[str]=..., search_text_snippet: _Optional[str]=..., commute_info: _Optional[_Union[SearchJobsResponse.CommuteInfo, _Mapping]]=...) -> None:
            ...

    class CommuteInfo(_message.Message):
        __slots__ = ('job_location', 'travel_duration')
        JOB_LOCATION_FIELD_NUMBER: _ClassVar[int]
        TRAVEL_DURATION_FIELD_NUMBER: _ClassVar[int]
        job_location: _common_pb2.Location
        travel_duration: _duration_pb2.Duration

        def __init__(self, job_location: _Optional[_Union[_common_pb2.Location, _Mapping]]=..., travel_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    MATCHING_JOBS_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    BROADENED_QUERY_JOBS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SPELL_CORRECTION_FIELD_NUMBER: _ClassVar[int]
    matching_jobs: _containers.RepeatedCompositeFieldContainer[SearchJobsResponse.MatchingJob]
    histogram_query_results: _containers.RepeatedCompositeFieldContainer[_histogram_pb2.HistogramQueryResult]
    next_page_token: str
    location_filters: _containers.RepeatedCompositeFieldContainer[_common_pb2.Location]
    estimated_total_size: int
    total_size: int
    metadata: _common_pb2.ResponseMetadata
    broadened_query_jobs_count: int
    spell_correction: _common_pb2.SpellingCorrection

    def __init__(self, matching_jobs: _Optional[_Iterable[_Union[SearchJobsResponse.MatchingJob, _Mapping]]]=..., histogram_query_results: _Optional[_Iterable[_Union[_histogram_pb2.HistogramQueryResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., location_filters: _Optional[_Iterable[_Union[_common_pb2.Location, _Mapping]]]=..., estimated_total_size: _Optional[int]=..., total_size: _Optional[int]=..., metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]]=..., broadened_query_jobs_count: _Optional[int]=..., spell_correction: _Optional[_Union[_common_pb2.SpellingCorrection, _Mapping]]=...) -> None:
        ...

class BatchCreateJobsRequest(_message.Message):
    __slots__ = ('parent', 'jobs')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    jobs: _containers.RepeatedCompositeFieldContainer[_job_pb2.Job]

    def __init__(self, parent: _Optional[str]=..., jobs: _Optional[_Iterable[_Union[_job_pb2.Job, _Mapping]]]=...) -> None:
        ...

class BatchUpdateJobsRequest(_message.Message):
    __slots__ = ('parent', 'jobs', 'update_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    jobs: _containers.RepeatedCompositeFieldContainer[_job_pb2.Job]
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., jobs: _Optional[_Iterable[_Union[_job_pb2.Job, _Mapping]]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class JobOperationResult(_message.Message):
    __slots__ = ('job_results',)

    class JobResult(_message.Message):
        __slots__ = ('job', 'status')
        JOB_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        job: _job_pb2.Job
        status: _status_pb2.Status

        def __init__(self, job: _Optional[_Union[_job_pb2.Job, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    JOB_RESULTS_FIELD_NUMBER: _ClassVar[int]
    job_results: _containers.RepeatedCompositeFieldContainer[JobOperationResult.JobResult]

    def __init__(self, job_results: _Optional[_Iterable[_Union[JobOperationResult.JobResult, _Mapping]]]=...) -> None:
        ...