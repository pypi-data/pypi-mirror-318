from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.gkehub.v1beta import feature_pb2 as _feature_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFeaturesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListFeaturesResponse(_message.Message):
    __slots__ = ("resources", "next_page_token")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    next_page_token: str
    def __init__(self, resources: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetFeatureRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFeatureRequest(_message.Message):
    __slots__ = ("parent", "feature_id", "resource", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_id: str
    resource: _feature_pb2.Feature
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., feature_id: _Optional[str] = ..., resource: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteFeatureRequest(_message.Message):
    __slots__ = ("name", "force", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    request_id: str
    def __init__(self, name: _Optional[str] = ..., force: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateFeatureRequest(_message.Message):
    __slots__ = ("name", "update_mask", "resource", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    resource: _feature_pb2.Feature
    request_id: str
    def __init__(self, name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., resource: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_detail", "cancel_requested", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_detail: _Optional[str] = ..., cancel_requested: bool = ..., api_version: _Optional[str] = ...) -> None: ...
