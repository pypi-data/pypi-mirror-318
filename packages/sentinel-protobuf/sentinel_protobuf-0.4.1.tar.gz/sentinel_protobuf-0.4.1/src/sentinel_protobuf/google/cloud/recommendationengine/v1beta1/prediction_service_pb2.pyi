from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommendationengine.v1beta1 import user_event_pb2 as _user_event_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ('name', 'user_event', 'page_size', 'page_token', 'filter', 'dry_run', 'params', 'labels')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_event: _user_event_pb2.UserEvent
    page_size: int
    page_token: str
    filter: str
    dry_run: bool
    params: _containers.MessageMap[str, _struct_pb2.Value]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., user_event: _Optional[_Union[_user_event_pb2.UserEvent, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., dry_run: bool=..., params: _Optional[_Mapping[str, _struct_pb2.Value]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class PredictResponse(_message.Message):
    __slots__ = ('results', 'recommendation_token', 'items_missing_in_catalog', 'dry_run', 'metadata', 'next_page_token')

    class PredictionResult(_message.Message):
        __slots__ = ('id', 'item_metadata')

        class ItemMetadataEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...
        ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_METADATA_FIELD_NUMBER: _ClassVar[int]
        id: str
        item_metadata: _containers.MessageMap[str, _struct_pb2.Value]

        def __init__(self, id: _Optional[str]=..., item_metadata: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ITEMS_MISSING_IN_CATALOG_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PredictResponse.PredictionResult]
    recommendation_token: str
    items_missing_in_catalog: _containers.RepeatedScalarFieldContainer[str]
    dry_run: bool
    metadata: _containers.MessageMap[str, _struct_pb2.Value]
    next_page_token: str

    def __init__(self, results: _Optional[_Iterable[_Union[PredictResponse.PredictionResult, _Mapping]]]=..., recommendation_token: _Optional[str]=..., items_missing_in_catalog: _Optional[_Iterable[str]]=..., dry_run: bool=..., metadata: _Optional[_Mapping[str, _struct_pb2.Value]]=..., next_page_token: _Optional[str]=...) -> None:
        ...