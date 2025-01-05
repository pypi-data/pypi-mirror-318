from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.visionai.v1 import common_pb2 as _common_pb2
from google.cloud.visionai.v1 import lva_resources_pb2 as _lva_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Registry(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGISTRY_UNSPECIFIED: _ClassVar[Registry]
    PUBLIC: _ClassVar[Registry]
    PRIVATE: _ClassVar[Registry]
REGISTRY_UNSPECIFIED: Registry
PUBLIC: Registry
PRIVATE: Registry

class ListOperatorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListOperatorsResponse(_message.Message):
    __slots__ = ('operators', 'next_page_token', 'unreachable')
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    operators: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Operator]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, operators: _Optional[_Iterable[_Union[_lva_resources_pb2.Operator, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOperatorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOperatorRequest(_message.Message):
    __slots__ = ('parent', 'operator_id', 'operator', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    operator_id: str
    operator: _lva_resources_pb2.Operator
    request_id: str

    def __init__(self, parent: _Optional[str]=..., operator_id: _Optional[str]=..., operator: _Optional[_Union[_lva_resources_pb2.Operator, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateOperatorRequest(_message.Message):
    __slots__ = ('update_mask', 'operator', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    operator: _lva_resources_pb2.Operator
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., operator: _Optional[_Union[_lva_resources_pb2.Operator, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteOperatorRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListAnalysesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListAnalysesResponse(_message.Message):
    __slots__ = ('analyses', 'next_page_token', 'unreachable')
    ANALYSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    analyses: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Analysis]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, analyses: _Optional[_Iterable[_Union[_lva_resources_pb2.Analysis, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAnalysisRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAnalysisRequest(_message.Message):
    __slots__ = ('parent', 'analysis_id', 'analysis', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_ID_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    analysis_id: str
    analysis: _lva_resources_pb2.Analysis
    request_id: str

    def __init__(self, parent: _Optional[str]=..., analysis_id: _Optional[str]=..., analysis: _Optional[_Union[_lva_resources_pb2.Analysis, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateAnalysisRequest(_message.Message):
    __slots__ = ('update_mask', 'analysis', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    analysis: _lva_resources_pb2.Analysis
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., analysis: _Optional[_Union[_lva_resources_pb2.Analysis, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteAnalysisRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListProcessesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListProcessesResponse(_message.Message):
    __slots__ = ('processes', 'next_page_token', 'unreachable')
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    processes: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Process]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, processes: _Optional[_Iterable[_Union[_lva_resources_pb2.Process, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetProcessRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateProcessRequest(_message.Message):
    __slots__ = ('parent', 'process_id', 'process', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    process_id: str
    process: _lva_resources_pb2.Process
    request_id: str

    def __init__(self, parent: _Optional[str]=..., process_id: _Optional[str]=..., process: _Optional[_Union[_lva_resources_pb2.Process, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateProcessRequest(_message.Message):
    __slots__ = ('update_mask', 'process', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    process: _lva_resources_pb2.Process
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., process: _Optional[_Union[_lva_resources_pb2.Process, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteProcessRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class BatchRunProcessRequest(_message.Message):
    __slots__ = ('parent', 'requests', 'options', 'batch_id')

    class BatchRunProcessOptions(_message.Message):
        __slots__ = ('retry_count', 'batch_size')
        RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
        retry_count: int
        batch_size: int

        def __init__(self, retry_count: _Optional[int]=..., batch_size: _Optional[int]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateProcessRequest]
    options: BatchRunProcessRequest.BatchRunProcessOptions
    batch_id: str

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateProcessRequest, _Mapping]]]=..., options: _Optional[_Union[BatchRunProcessRequest.BatchRunProcessOptions, _Mapping]]=..., batch_id: _Optional[str]=...) -> None:
        ...

class BatchRunProcessResponse(_message.Message):
    __slots__ = ('batch_id', 'processes')
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    processes: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Process]

    def __init__(self, batch_id: _Optional[str]=..., processes: _Optional[_Iterable[_Union[_lva_resources_pb2.Process, _Mapping]]]=...) -> None:
        ...

class ResolveOperatorInfoRequest(_message.Message):
    __slots__ = ('parent', 'queries')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    queries: _containers.RepeatedCompositeFieldContainer[OperatorQuery]

    def __init__(self, parent: _Optional[str]=..., queries: _Optional[_Iterable[_Union[OperatorQuery, _Mapping]]]=...) -> None:
        ...

class OperatorQuery(_message.Message):
    __slots__ = ('operator', 'tag', 'registry')
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    operator: str
    tag: str
    registry: Registry

    def __init__(self, operator: _Optional[str]=..., tag: _Optional[str]=..., registry: _Optional[_Union[Registry, str]]=...) -> None:
        ...

class ResolveOperatorInfoResponse(_message.Message):
    __slots__ = ('operators',)
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    operators: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Operator]

    def __init__(self, operators: _Optional[_Iterable[_Union[_lva_resources_pb2.Operator, _Mapping]]]=...) -> None:
        ...

class ListPublicOperatorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListPublicOperatorsResponse(_message.Message):
    __slots__ = ('operators', 'next_page_token')
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operators: _containers.RepeatedCompositeFieldContainer[_lva_resources_pb2.Operator]
    next_page_token: str

    def __init__(self, operators: _Optional[_Iterable[_Union[_lva_resources_pb2.Operator, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...