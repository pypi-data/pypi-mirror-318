from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import user_event_pb2 as _user_event_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ("placement", "user_event", "page_size", "page_token", "filter", "validate_only", "params", "labels")
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    placement: str
    user_event: _user_event_pb2.UserEvent
    page_size: int
    page_token: str
    filter: str
    validate_only: bool
    params: _containers.MessageMap[str, _struct_pb2.Value]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, placement: _Optional[str] = ..., user_event: _Optional[_Union[_user_event_pb2.UserEvent, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., validate_only: bool = ..., params: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ("results", "attribution_token", "missing_ids", "validate_only")
    class PredictionResult(_message.Message):
        __slots__ = ("id", "metadata")
        class MetadataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _struct_pb2.Value
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        id: str
        metadata: _containers.MessageMap[str, _struct_pb2.Value]
        def __init__(self, id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MISSING_IDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PredictResponse.PredictionResult]
    attribution_token: str
    missing_ids: _containers.RepeatedScalarFieldContainer[str]
    validate_only: bool
    def __init__(self, results: _Optional[_Iterable[_Union[PredictResponse.PredictionResult, _Mapping]]] = ..., attribution_token: _Optional[str] = ..., missing_ids: _Optional[_Iterable[str]] = ..., validate_only: bool = ...) -> None: ...
