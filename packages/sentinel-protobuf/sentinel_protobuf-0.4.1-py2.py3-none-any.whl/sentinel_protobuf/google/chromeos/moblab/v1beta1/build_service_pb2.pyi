from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.chromeos.moblab.v1beta1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FindMostStableBuildRequest(_message.Message):
    __slots__ = ('build_target',)
    BUILD_TARGET_FIELD_NUMBER: _ClassVar[int]
    build_target: str

    def __init__(self, build_target: _Optional[str]=...) -> None:
        ...

class FindMostStableBuildResponse(_message.Message):
    __slots__ = ('build',)
    BUILD_FIELD_NUMBER: _ClassVar[int]
    build: _resources_pb2.Build

    def __init__(self, build: _Optional[_Union[_resources_pb2.Build, _Mapping]]=...) -> None:
        ...

class ListBuildTargetsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBuildTargetsResponse(_message.Message):
    __slots__ = ('build_targets', 'next_page_token', 'total_size')
    BUILD_TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    build_targets: _containers.RepeatedCompositeFieldContainer[_resources_pb2.BuildTarget]
    next_page_token: str
    total_size: int

    def __init__(self, build_targets: _Optional[_Iterable[_Union[_resources_pb2.BuildTarget, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListModelsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListModelsResponse(_message.Message):
    __slots__ = ('models', 'next_page_token', 'total_size')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Model]
    next_page_token: str
    total_size: int

    def __init__(self, models: _Optional[_Iterable[_Union[_resources_pb2.Model, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListBuildsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'read_mask', 'group_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    read_mask: _field_mask_pb2.FieldMask
    group_by: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., group_by: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListBuildsResponse(_message.Message):
    __slots__ = ('builds', 'next_page_token', 'total_size')
    BUILDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    builds: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Build]
    next_page_token: str
    total_size: int

    def __init__(self, builds: _Optional[_Iterable[_Union[_resources_pb2.Build, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class CheckBuildStageStatusRequest(_message.Message):
    __slots__ = ('name', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class CheckBuildStageStatusResponse(_message.Message):
    __slots__ = ('is_build_staged', 'staged_build_artifact', 'source_build_artifact')
    IS_BUILD_STAGED_FIELD_NUMBER: _ClassVar[int]
    STAGED_BUILD_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUILD_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    is_build_staged: bool
    staged_build_artifact: _resources_pb2.BuildArtifact
    source_build_artifact: _resources_pb2.BuildArtifact

    def __init__(self, is_build_staged: bool=..., staged_build_artifact: _Optional[_Union[_resources_pb2.BuildArtifact, _Mapping]]=..., source_build_artifact: _Optional[_Union[_resources_pb2.BuildArtifact, _Mapping]]=...) -> None:
        ...

class StageBuildRequest(_message.Message):
    __slots__ = ('name', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class StageBuildResponse(_message.Message):
    __slots__ = ('staged_build_artifact',)
    STAGED_BUILD_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    staged_build_artifact: _resources_pb2.BuildArtifact

    def __init__(self, staged_build_artifact: _Optional[_Union[_resources_pb2.BuildArtifact, _Mapping]]=...) -> None:
        ...

class StageBuildMetadata(_message.Message):
    __slots__ = ('progress_percent', 'start_time', 'end_time')
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    progress_percent: float
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, progress_percent: _Optional[float]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...