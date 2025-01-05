from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import import_config_pb2 as _import_config_pb2
from google.cloud.discoveryengine.v1alpha import sample_query_pb2 as _sample_query_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSampleQueryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSampleQueriesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSampleQueriesResponse(_message.Message):
    __slots__ = ("sample_queries", "next_page_token")
    SAMPLE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sample_queries: _containers.RepeatedCompositeFieldContainer[_sample_query_pb2.SampleQuery]
    next_page_token: str
    def __init__(self, sample_queries: _Optional[_Iterable[_Union[_sample_query_pb2.SampleQuery, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateSampleQueryRequest(_message.Message):
    __slots__ = ("parent", "sample_query", "sample_query_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_QUERY_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    sample_query: _sample_query_pb2.SampleQuery
    sample_query_id: str
    def __init__(self, parent: _Optional[str] = ..., sample_query: _Optional[_Union[_sample_query_pb2.SampleQuery, _Mapping]] = ..., sample_query_id: _Optional[str] = ...) -> None: ...

class UpdateSampleQueryRequest(_message.Message):
    __slots__ = ("sample_query", "update_mask")
    SAMPLE_QUERY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sample_query: _sample_query_pb2.SampleQuery
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, sample_query: _Optional[_Union[_sample_query_pb2.SampleQuery, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteSampleQueryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
