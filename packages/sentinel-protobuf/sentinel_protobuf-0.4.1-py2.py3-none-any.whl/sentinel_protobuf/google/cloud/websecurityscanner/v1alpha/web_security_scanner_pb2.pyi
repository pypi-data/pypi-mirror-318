from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.websecurityscanner.v1alpha import crawled_url_pb2 as _crawled_url_pb2
from google.cloud.websecurityscanner.v1alpha import finding_pb2 as _finding_pb2
from google.cloud.websecurityscanner.v1alpha import finding_type_stats_pb2 as _finding_type_stats_pb2
from google.cloud.websecurityscanner.v1alpha import scan_config_pb2 as _scan_config_pb2
from google.cloud.websecurityscanner.v1alpha import scan_run_pb2 as _scan_run_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateScanConfigRequest(_message.Message):
    __slots__ = ('parent', 'scan_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    scan_config: _scan_config_pb2.ScanConfig

    def __init__(self, parent: _Optional[str]=..., scan_config: _Optional[_Union[_scan_config_pb2.ScanConfig, _Mapping]]=...) -> None:
        ...

class DeleteScanConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetScanConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListScanConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class UpdateScanConfigRequest(_message.Message):
    __slots__ = ('scan_config', 'update_mask')
    SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    scan_config: _scan_config_pb2.ScanConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, scan_config: _Optional[_Union[_scan_config_pb2.ScanConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListScanConfigsResponse(_message.Message):
    __slots__ = ('scan_configs', 'next_page_token')
    SCAN_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scan_configs: _containers.RepeatedCompositeFieldContainer[_scan_config_pb2.ScanConfig]
    next_page_token: str

    def __init__(self, scan_configs: _Optional[_Iterable[_Union[_scan_config_pb2.ScanConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class StartScanRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetScanRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListScanRunsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListScanRunsResponse(_message.Message):
    __slots__ = ('scan_runs', 'next_page_token')
    SCAN_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scan_runs: _containers.RepeatedCompositeFieldContainer[_scan_run_pb2.ScanRun]
    next_page_token: str

    def __init__(self, scan_runs: _Optional[_Iterable[_Union[_scan_run_pb2.ScanRun, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class StopScanRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCrawledUrlsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListCrawledUrlsResponse(_message.Message):
    __slots__ = ('crawled_urls', 'next_page_token')
    CRAWLED_URLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    crawled_urls: _containers.RepeatedCompositeFieldContainer[_crawled_url_pb2.CrawledUrl]
    next_page_token: str

    def __init__(self, crawled_urls: _Optional[_Iterable[_Union[_crawled_url_pb2.CrawledUrl, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFindingsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListFindingsResponse(_message.Message):
    __slots__ = ('findings', 'next_page_token')
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[_finding_pb2.Finding]
    next_page_token: str

    def __init__(self, findings: _Optional[_Iterable[_Union[_finding_pb2.Finding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListFindingTypeStatsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListFindingTypeStatsResponse(_message.Message):
    __slots__ = ('finding_type_stats',)
    FINDING_TYPE_STATS_FIELD_NUMBER: _ClassVar[int]
    finding_type_stats: _containers.RepeatedCompositeFieldContainer[_finding_type_stats_pb2.FindingTypeStats]

    def __init__(self, finding_type_stats: _Optional[_Iterable[_Union[_finding_type_stats_pb2.FindingTypeStats, _Mapping]]]=...) -> None:
        ...