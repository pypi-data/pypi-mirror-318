from google.ai.generativelanguage.v1beta import model_pb2 as _model_pb2
from google.ai.generativelanguage.v1beta import tuned_model_pb2 as _tuned_model_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models", "next_page_token")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
    next_page_token: str
    def __init__(self, models: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTunedModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTunedModelsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListTunedModelsResponse(_message.Message):
    __slots__ = ("tuned_models", "next_page_token")
    TUNED_MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tuned_models: _containers.RepeatedCompositeFieldContainer[_tuned_model_pb2.TunedModel]
    next_page_token: str
    def __init__(self, tuned_models: _Optional[_Iterable[_Union[_tuned_model_pb2.TunedModel, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateTunedModelRequest(_message.Message):
    __slots__ = ("tuned_model_id", "tuned_model")
    TUNED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    tuned_model_id: str
    tuned_model: _tuned_model_pb2.TunedModel
    def __init__(self, tuned_model_id: _Optional[str] = ..., tuned_model: _Optional[_Union[_tuned_model_pb2.TunedModel, _Mapping]] = ...) -> None: ...

class CreateTunedModelMetadata(_message.Message):
    __slots__ = ("tuned_model", "total_steps", "completed_steps", "completed_percent", "snapshots")
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STEPS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_STEPS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    tuned_model: str
    total_steps: int
    completed_steps: int
    completed_percent: float
    snapshots: _containers.RepeatedCompositeFieldContainer[_tuned_model_pb2.TuningSnapshot]
    def __init__(self, tuned_model: _Optional[str] = ..., total_steps: _Optional[int] = ..., completed_steps: _Optional[int] = ..., completed_percent: _Optional[float] = ..., snapshots: _Optional[_Iterable[_Union[_tuned_model_pb2.TuningSnapshot, _Mapping]]] = ...) -> None: ...

class UpdateTunedModelRequest(_message.Message):
    __slots__ = ("tuned_model", "update_mask")
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tuned_model: _tuned_model_pb2.TunedModel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tuned_model: _Optional[_Union[_tuned_model_pb2.TunedModel, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteTunedModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
