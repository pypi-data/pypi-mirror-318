from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import action_pb2 as _action_pb2
from google.devtools.resultstore.v2 import configuration_pb2 as _configuration_pb2
from google.devtools.resultstore.v2 import configured_target_pb2 as _configured_target_pb2
from google.devtools.resultstore.v2 import download_metadata_pb2 as _download_metadata_pb2
from google.devtools.resultstore.v2 import file_set_pb2 as _file_set_pb2
from google.devtools.resultstore.v2 import invocation_pb2 as _invocation_pb2
from google.devtools.resultstore.v2 import target_pb2 as _target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchInvocationsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'offset', 'query', 'project_id', 'exact_match')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    offset: int
    query: str
    project_id: str
    exact_match: bool

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., query: _Optional[str]=..., project_id: _Optional[str]=..., exact_match: bool=...) -> None:
        ...

class SearchInvocationsResponse(_message.Message):
    __slots__ = ('invocations', 'next_page_token')
    INVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invocations: _containers.RepeatedCompositeFieldContainer[_invocation_pb2.Invocation]
    next_page_token: str

    def __init__(self, invocations: _Optional[_Iterable[_Union[_invocation_pb2.Invocation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ExportInvocationRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'offset', 'targets_filter', 'configured_targets_filter', 'actions_filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FILTER_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGETS_FILTER_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    offset: int
    targets_filter: str
    configured_targets_filter: str
    actions_filter: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., targets_filter: _Optional[str]=..., configured_targets_filter: _Optional[str]=..., actions_filter: _Optional[str]=...) -> None:
        ...

class ExportInvocationResponse(_message.Message):
    __slots__ = ('invocation', 'download_metadata', 'targets', 'configurations', 'configured_targets', 'actions', 'file_sets', 'next_page_token')
    INVOCATION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_METADATA_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGETS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invocation: _invocation_pb2.Invocation
    download_metadata: _download_metadata_pb2.DownloadMetadata
    targets: _containers.RepeatedCompositeFieldContainer[_target_pb2.Target]
    configurations: _containers.RepeatedCompositeFieldContainer[_configuration_pb2.Configuration]
    configured_targets: _containers.RepeatedCompositeFieldContainer[_configured_target_pb2.ConfiguredTarget]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    file_sets: _containers.RepeatedCompositeFieldContainer[_file_set_pb2.FileSet]
    next_page_token: str

    def __init__(self, invocation: _Optional[_Union[_invocation_pb2.Invocation, _Mapping]]=..., download_metadata: _Optional[_Union[_download_metadata_pb2.DownloadMetadata, _Mapping]]=..., targets: _Optional[_Iterable[_Union[_target_pb2.Target, _Mapping]]]=..., configurations: _Optional[_Iterable[_Union[_configuration_pb2.Configuration, _Mapping]]]=..., configured_targets: _Optional[_Iterable[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]]=..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]]=..., file_sets: _Optional[_Iterable[_Union[_file_set_pb2.FileSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetInvocationDownloadMetadataRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetConfigurationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConfigurationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ListConfigurationsResponse(_message.Message):
    __slots__ = ('configurations', 'next_page_token')
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    configurations: _containers.RepeatedCompositeFieldContainer[_configuration_pb2.Configuration]
    next_page_token: str

    def __init__(self, configurations: _Optional[_Iterable[_Union[_configuration_pb2.Configuration, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTargetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTargetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ListTargetsResponse(_message.Message):
    __slots__ = ('targets', 'next_page_token')
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[_target_pb2.Target]
    next_page_token: str

    def __init__(self, targets: _Optional[_Iterable[_Union[_target_pb2.Target, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetConfiguredTargetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConfiguredTargetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ListConfiguredTargetsResponse(_message.Message):
    __slots__ = ('configured_targets', 'next_page_token')
    CONFIGURED_TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    configured_targets: _containers.RepeatedCompositeFieldContainer[_configured_target_pb2.ConfiguredTarget]
    next_page_token: str

    def __init__(self, configured_targets: _Optional[_Iterable[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchConfiguredTargetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'query', 'project_id', 'exact_match')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    query: str
    project_id: str
    exact_match: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., query: _Optional[str]=..., project_id: _Optional[str]=..., exact_match: bool=...) -> None:
        ...

class SearchConfiguredTargetsResponse(_message.Message):
    __slots__ = ('configured_targets', 'next_page_token')
    CONFIGURED_TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    configured_targets: _containers.RepeatedCompositeFieldContainer[_configured_target_pb2.ConfiguredTarget]
    next_page_token: str

    def __init__(self, configured_targets: _Optional[_Iterable[_Union[_configured_target_pb2.ConfiguredTarget, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetActionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListActionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ListActionsResponse(_message.Message):
    __slots__ = ('actions', 'next_page_token')
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    next_page_token: str

    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchListActionsRequest(_message.Message):
    __slots__ = ('parent', 'configured_targets', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGETS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    configured_targets: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., configured_targets: _Optional[_Iterable[str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class BatchListActionsResponse(_message.Message):
    __slots__ = ('actions', 'next_page_token', 'not_found')
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    next_page_token: str
    not_found: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]]=..., next_page_token: _Optional[str]=..., not_found: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetFileSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFileSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'offset', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    offset: int
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ListFileSetsResponse(_message.Message):
    __slots__ = ('file_sets', 'next_page_token')
    FILE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    file_sets: _containers.RepeatedCompositeFieldContainer[_file_set_pb2.FileSet]
    next_page_token: str

    def __init__(self, file_sets: _Optional[_Iterable[_Union[_file_set_pb2.FileSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class TraverseFileSetsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'offset')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    offset: int

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., offset: _Optional[int]=...) -> None:
        ...

class TraverseFileSetsResponse(_message.Message):
    __slots__ = ('file_sets', 'next_page_token')
    FILE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    file_sets: _containers.RepeatedCompositeFieldContainer[_file_set_pb2.FileSet]
    next_page_token: str

    def __init__(self, file_sets: _Optional[_Iterable[_Union[_file_set_pb2.FileSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...