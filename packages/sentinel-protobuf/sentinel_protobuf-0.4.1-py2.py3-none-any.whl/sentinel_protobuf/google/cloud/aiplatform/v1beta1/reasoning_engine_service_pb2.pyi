from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import reasoning_engine_pb2 as _reasoning_engine_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateReasoningEngineRequest(_message.Message):
    __slots__ = ('parent', 'reasoning_engine')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REASONING_ENGINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reasoning_engine: _reasoning_engine_pb2.ReasoningEngine

    def __init__(self, parent: _Optional[str]=..., reasoning_engine: _Optional[_Union[_reasoning_engine_pb2.ReasoningEngine, _Mapping]]=...) -> None:
        ...

class CreateReasoningEngineOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetReasoningEngineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateReasoningEngineRequest(_message.Message):
    __slots__ = ('reasoning_engine', 'update_mask')
    REASONING_ENGINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    reasoning_engine: _reasoning_engine_pb2.ReasoningEngine
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, reasoning_engine: _Optional[_Union[_reasoning_engine_pb2.ReasoningEngine, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateReasoningEngineOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ListReasoningEnginesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReasoningEnginesResponse(_message.Message):
    __slots__ = ('reasoning_engines', 'next_page_token')
    REASONING_ENGINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reasoning_engines: _containers.RepeatedCompositeFieldContainer[_reasoning_engine_pb2.ReasoningEngine]
    next_page_token: str

    def __init__(self, reasoning_engines: _Optional[_Iterable[_Union[_reasoning_engine_pb2.ReasoningEngine, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteReasoningEngineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...