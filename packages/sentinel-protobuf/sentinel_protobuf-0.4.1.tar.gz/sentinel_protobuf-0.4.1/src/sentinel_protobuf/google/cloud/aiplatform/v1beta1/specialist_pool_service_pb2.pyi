from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import specialist_pool_pb2 as _specialist_pool_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpecialistPoolRequest(_message.Message):
    __slots__ = ('parent', 'specialist_pool')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SPECIALIST_POOL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    specialist_pool: _specialist_pool_pb2.SpecialistPool

    def __init__(self, parent: _Optional[str]=..., specialist_pool: _Optional[_Union[_specialist_pool_pb2.SpecialistPool, _Mapping]]=...) -> None:
        ...

class CreateSpecialistPoolOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetSpecialistPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSpecialistPoolsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListSpecialistPoolsResponse(_message.Message):
    __slots__ = ('specialist_pools', 'next_page_token')
    SPECIALIST_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    specialist_pools: _containers.RepeatedCompositeFieldContainer[_specialist_pool_pb2.SpecialistPool]
    next_page_token: str

    def __init__(self, specialist_pools: _Optional[_Iterable[_Union[_specialist_pool_pb2.SpecialistPool, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSpecialistPoolRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateSpecialistPoolRequest(_message.Message):
    __slots__ = ('specialist_pool', 'update_mask')
    SPECIALIST_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    specialist_pool: _specialist_pool_pb2.SpecialistPool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, specialist_pool: _Optional[_Union[_specialist_pool_pb2.SpecialistPool, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateSpecialistPoolOperationMetadata(_message.Message):
    __slots__ = ('specialist_pool', 'generic_metadata')
    SPECIALIST_POOL_FIELD_NUMBER: _ClassVar[int]
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    specialist_pool: str
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, specialist_pool: _Optional[str]=..., generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...