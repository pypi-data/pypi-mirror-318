from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import model_pb2 as _model_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateModelRequest(_message.Message):
    __slots__ = ("parent", "model", "dry_run")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model: _model_pb2.Model
    dry_run: bool
    def __init__(self, parent: _Optional[str] = ..., model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ..., dry_run: bool = ...) -> None: ...

class UpdateModelRequest(_message.Message):
    __slots__ = ("model", "update_mask")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    model: _model_pb2.Model
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PauseModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class DeleteModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models", "next_page_token")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[_model_pb2.Model]
    next_page_token: str
    def __init__(self, models: _Optional[_Iterable[_Union[_model_pb2.Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class TuneModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateModelMetadata(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str
    def __init__(self, model: _Optional[str] = ...) -> None: ...

class TuneModelMetadata(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: str
    def __init__(self, model: _Optional[str] = ...) -> None: ...

class TuneModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
