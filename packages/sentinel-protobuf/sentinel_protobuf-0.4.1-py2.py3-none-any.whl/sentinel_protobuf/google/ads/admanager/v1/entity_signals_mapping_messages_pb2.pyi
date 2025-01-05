from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EntitySignalsMapping(_message.Message):
    __slots__ = ('audience_segment_id', 'content_bundle_id', 'custom_targeting_value_id', 'name', 'entity_signals_mapping_id', 'taxonomy_category_ids')
    AUDIENCE_SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGETING_VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SIGNALS_MAPPING_ID_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    audience_segment_id: int
    content_bundle_id: int
    custom_targeting_value_id: int
    name: str
    entity_signals_mapping_id: int
    taxonomy_category_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, audience_segment_id: _Optional[int]=..., content_bundle_id: _Optional[int]=..., custom_targeting_value_id: _Optional[int]=..., name: _Optional[str]=..., entity_signals_mapping_id: _Optional[int]=..., taxonomy_category_ids: _Optional[_Iterable[int]]=...) -> None:
        ...