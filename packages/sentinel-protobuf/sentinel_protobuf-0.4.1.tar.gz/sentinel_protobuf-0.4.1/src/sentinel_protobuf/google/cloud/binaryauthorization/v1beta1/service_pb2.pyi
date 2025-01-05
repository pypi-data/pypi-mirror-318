from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.binaryauthorization.v1beta1 import resources_pb2 as _resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ('policy',)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _resources_pb2.Policy

    def __init__(self, policy: _Optional[_Union[_resources_pb2.Policy, _Mapping]]=...) -> None:
        ...

class CreateAttestorRequest(_message.Message):
    __slots__ = ('parent', 'attestor_id', 'attestor')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ATTESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ATTESTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    attestor_id: str
    attestor: _resources_pb2.Attestor

    def __init__(self, parent: _Optional[str]=..., attestor_id: _Optional[str]=..., attestor: _Optional[_Union[_resources_pb2.Attestor, _Mapping]]=...) -> None:
        ...

class GetAttestorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAttestorRequest(_message.Message):
    __slots__ = ('attestor',)
    ATTESTOR_FIELD_NUMBER: _ClassVar[int]
    attestor: _resources_pb2.Attestor

    def __init__(self, attestor: _Optional[_Union[_resources_pb2.Attestor, _Mapping]]=...) -> None:
        ...

class ListAttestorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAttestorsResponse(_message.Message):
    __slots__ = ('attestors', 'next_page_token')
    ATTESTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attestors: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Attestor]
    next_page_token: str

    def __init__(self, attestors: _Optional[_Iterable[_Union[_resources_pb2.Attestor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteAttestorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetSystemPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...