from google.ads.admanager.v1 import entity_signals_mapping_messages_pb2 as _entity_signals_mapping_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetEntitySignalsMappingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEntitySignalsMappingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'skip')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., skip: _Optional[int]=...) -> None:
        ...

class CreateEntitySignalsMappingRequest(_message.Message):
    __slots__ = ('parent', 'entity_signals_mapping')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SIGNALS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_signals_mapping: _entity_signals_mapping_messages_pb2.EntitySignalsMapping

    def __init__(self, parent: _Optional[str]=..., entity_signals_mapping: _Optional[_Union[_entity_signals_mapping_messages_pb2.EntitySignalsMapping, _Mapping]]=...) -> None:
        ...

class UpdateEntitySignalsMappingRequest(_message.Message):
    __slots__ = ('entity_signals_mapping', 'update_mask')
    ENTITY_SIGNALS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entity_signals_mapping: _entity_signals_mapping_messages_pb2.EntitySignalsMapping
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entity_signals_mapping: _Optional[_Union[_entity_signals_mapping_messages_pb2.EntitySignalsMapping, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListEntitySignalsMappingsResponse(_message.Message):
    __slots__ = ('entity_signals_mappings', 'next_page_token', 'total_size')
    ENTITY_SIGNALS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    entity_signals_mappings: _containers.RepeatedCompositeFieldContainer[_entity_signals_mapping_messages_pb2.EntitySignalsMapping]
    next_page_token: str
    total_size: int

    def __init__(self, entity_signals_mappings: _Optional[_Iterable[_Union[_entity_signals_mapping_messages_pb2.EntitySignalsMapping, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class BatchCreateEntitySignalsMappingsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateEntitySignalsMappingRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateEntitySignalsMappingRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateEntitySignalsMappingsResponse(_message.Message):
    __slots__ = ('entity_signals_mappings',)
    ENTITY_SIGNALS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    entity_signals_mappings: _containers.RepeatedCompositeFieldContainer[_entity_signals_mapping_messages_pb2.EntitySignalsMapping]

    def __init__(self, entity_signals_mappings: _Optional[_Iterable[_Union[_entity_signals_mapping_messages_pb2.EntitySignalsMapping, _Mapping]]]=...) -> None:
        ...

class BatchUpdateEntitySignalsMappingsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateEntitySignalsMappingRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateEntitySignalsMappingRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateEntitySignalsMappingsResponse(_message.Message):
    __slots__ = ('entity_signals_mappings',)
    ENTITY_SIGNALS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    entity_signals_mappings: _containers.RepeatedCompositeFieldContainer[_entity_signals_mapping_messages_pb2.EntitySignalsMapping]

    def __init__(self, entity_signals_mappings: _Optional[_Iterable[_Union[_entity_signals_mapping_messages_pb2.EntitySignalsMapping, _Mapping]]]=...) -> None:
        ...