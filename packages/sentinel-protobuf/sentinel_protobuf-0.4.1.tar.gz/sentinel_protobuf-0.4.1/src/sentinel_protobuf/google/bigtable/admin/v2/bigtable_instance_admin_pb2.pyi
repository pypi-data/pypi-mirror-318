from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.bigtable.admin.v2 import instance_pb2 as _instance_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateInstanceRequest(_message.Message):
    __slots__ = ("parent", "instance_id", "instance", "clusters")
    class ClustersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _instance_pb2.Cluster
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_instance_pb2.Cluster, _Mapping]] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: _instance_pb2.Instance
    clusters: _containers.MessageMap[str, _instance_pb2.Cluster]
    def __init__(self, parent: _Optional[str] = ..., instance_id: _Optional[str] = ..., instance: _Optional[_Union[_instance_pb2.Instance, _Mapping]] = ..., clusters: _Optional[_Mapping[str, _instance_pb2.Cluster]] = ...) -> None: ...

class GetInstanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListInstancesRequest(_message.Message):
    __slots__ = ("parent", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListInstancesResponse(_message.Message):
    __slots__ = ("instances", "failed_locations", "next_page_token")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_instance_pb2.Instance]
    failed_locations: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, instances: _Optional[_Iterable[_Union[_instance_pb2.Instance, _Mapping]]] = ..., failed_locations: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PartialUpdateInstanceRequest(_message.Message):
    __slots__ = ("instance", "update_mask")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    instance: _instance_pb2.Instance
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, instance: _Optional[_Union[_instance_pb2.Instance, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _instance_pb2.Cluster
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_instance_pb2.Cluster, _Mapping]] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("parent", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "failed_locations", "next_page_token")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_instance_pb2.Cluster]
    failed_locations: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, clusters: _Optional[_Iterable[_Union[_instance_pb2.Cluster, _Mapping]]] = ..., failed_locations: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateInstanceMetadata(_message.Message):
    __slots__ = ("original_request", "request_time", "finish_time")
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: CreateInstanceRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    def __init__(self, original_request: _Optional[_Union[CreateInstanceRequest, _Mapping]] = ..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateInstanceMetadata(_message.Message):
    __slots__ = ("original_request", "request_time", "finish_time")
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: PartialUpdateInstanceRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    def __init__(self, original_request: _Optional[_Union[PartialUpdateInstanceRequest, _Mapping]] = ..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateClusterMetadata(_message.Message):
    __slots__ = ("original_request", "request_time", "finish_time", "tables")
    class TableProgress(_message.Message):
        __slots__ = ("estimated_size_bytes", "estimated_copied_bytes", "state")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[CreateClusterMetadata.TableProgress.State]
            PENDING: _ClassVar[CreateClusterMetadata.TableProgress.State]
            COPYING: _ClassVar[CreateClusterMetadata.TableProgress.State]
            COMPLETED: _ClassVar[CreateClusterMetadata.TableProgress.State]
            CANCELLED: _ClassVar[CreateClusterMetadata.TableProgress.State]
        STATE_UNSPECIFIED: CreateClusterMetadata.TableProgress.State
        PENDING: CreateClusterMetadata.TableProgress.State
        COPYING: CreateClusterMetadata.TableProgress.State
        COMPLETED: CreateClusterMetadata.TableProgress.State
        CANCELLED: CreateClusterMetadata.TableProgress.State
        ESTIMATED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_COPIED_BYTES_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        estimated_size_bytes: int
        estimated_copied_bytes: int
        state: CreateClusterMetadata.TableProgress.State
        def __init__(self, estimated_size_bytes: _Optional[int] = ..., estimated_copied_bytes: _Optional[int] = ..., state: _Optional[_Union[CreateClusterMetadata.TableProgress.State, str]] = ...) -> None: ...
    class TablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CreateClusterMetadata.TableProgress
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CreateClusterMetadata.TableProgress, _Mapping]] = ...) -> None: ...
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    original_request: CreateClusterRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    tables: _containers.MessageMap[str, CreateClusterMetadata.TableProgress]
    def __init__(self, original_request: _Optional[_Union[CreateClusterRequest, _Mapping]] = ..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tables: _Optional[_Mapping[str, CreateClusterMetadata.TableProgress]] = ...) -> None: ...

class UpdateClusterMetadata(_message.Message):
    __slots__ = ("original_request", "request_time", "finish_time")
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: _instance_pb2.Cluster
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    def __init__(self, original_request: _Optional[_Union[_instance_pb2.Cluster, _Mapping]] = ..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PartialUpdateClusterMetadata(_message.Message):
    __slots__ = ("request_time", "finish_time", "original_request")
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    original_request: PartialUpdateClusterRequest
    def __init__(self, request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., original_request: _Optional[_Union[PartialUpdateClusterRequest, _Mapping]] = ...) -> None: ...

class PartialUpdateClusterRequest(_message.Message):
    __slots__ = ("cluster", "update_mask")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    cluster: _instance_pb2.Cluster
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, cluster: _Optional[_Union[_instance_pb2.Cluster, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateAppProfileRequest(_message.Message):
    __slots__ = ("parent", "app_profile_id", "app_profile", "ignore_warnings")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    app_profile_id: str
    app_profile: _instance_pb2.AppProfile
    ignore_warnings: bool
    def __init__(self, parent: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., app_profile: _Optional[_Union[_instance_pb2.AppProfile, _Mapping]] = ..., ignore_warnings: bool = ...) -> None: ...

class GetAppProfileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAppProfilesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAppProfilesResponse(_message.Message):
    __slots__ = ("app_profiles", "next_page_token", "failed_locations")
    APP_PROFILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    app_profiles: _containers.RepeatedCompositeFieldContainer[_instance_pb2.AppProfile]
    next_page_token: str
    failed_locations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, app_profiles: _Optional[_Iterable[_Union[_instance_pb2.AppProfile, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., failed_locations: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateAppProfileRequest(_message.Message):
    __slots__ = ("app_profile", "update_mask", "ignore_warnings")
    APP_PROFILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    IGNORE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    app_profile: _instance_pb2.AppProfile
    update_mask: _field_mask_pb2.FieldMask
    ignore_warnings: bool
    def __init__(self, app_profile: _Optional[_Union[_instance_pb2.AppProfile, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., ignore_warnings: bool = ...) -> None: ...

class DeleteAppProfileRequest(_message.Message):
    __slots__ = ("name", "ignore_warnings")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IGNORE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ignore_warnings: bool
    def __init__(self, name: _Optional[str] = ..., ignore_warnings: bool = ...) -> None: ...

class UpdateAppProfileMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHotTabletsRequest(_message.Message):
    __slots__ = ("parent", "start_time", "end_time", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListHotTabletsResponse(_message.Message):
    __slots__ = ("hot_tablets", "next_page_token")
    HOT_TABLETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hot_tablets: _containers.RepeatedCompositeFieldContainer[_instance_pb2.HotTablet]
    next_page_token: str
    def __init__(self, hot_tablets: _Optional[_Iterable[_Union[_instance_pb2.HotTablet, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
