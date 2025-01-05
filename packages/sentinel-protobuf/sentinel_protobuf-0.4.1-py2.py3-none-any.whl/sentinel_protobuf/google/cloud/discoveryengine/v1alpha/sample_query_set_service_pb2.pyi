from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import sample_query_set_pb2 as _sample_query_set_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetSampleQuerySetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSampleQuerySetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSampleQuerySetsResponse(_message.Message):
    __slots__ = ('sample_query_sets', 'next_page_token')
    SAMPLE_QUERY_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sample_query_sets: _containers.RepeatedCompositeFieldContainer[_sample_query_set_pb2.SampleQuerySet]
    next_page_token: str

    def __init__(self, sample_query_sets: _Optional[_Iterable[_Union[_sample_query_set_pb2.SampleQuerySet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateSampleQuerySetRequest(_message.Message):
    __slots__ = ('parent', 'sample_query_set', 'sample_query_set_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_QUERY_SET_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_QUERY_SET_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    sample_query_set: _sample_query_set_pb2.SampleQuerySet
    sample_query_set_id: str

    def __init__(self, parent: _Optional[str]=..., sample_query_set: _Optional[_Union[_sample_query_set_pb2.SampleQuerySet, _Mapping]]=..., sample_query_set_id: _Optional[str]=...) -> None:
        ...

class UpdateSampleQuerySetRequest(_message.Message):
    __slots__ = ('sample_query_set', 'update_mask')
    SAMPLE_QUERY_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sample_query_set: _sample_query_set_pb2.SampleQuerySet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, sample_query_set: _Optional[_Union[_sample_query_set_pb2.SampleQuerySet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSampleQuerySetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...