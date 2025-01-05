from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import branch_pb2 as _branch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListBranchesRequest(_message.Message):
    __slots__ = ("parent", "view")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: _branch_pb2.BranchView
    def __init__(self, parent: _Optional[str] = ..., view: _Optional[_Union[_branch_pb2.BranchView, str]] = ...) -> None: ...

class ListBranchesResponse(_message.Message):
    __slots__ = ("branches",)
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedCompositeFieldContainer[_branch_pb2.Branch]
    def __init__(self, branches: _Optional[_Iterable[_Union[_branch_pb2.Branch, _Mapping]]] = ...) -> None: ...

class GetBranchRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _branch_pb2.BranchView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[_branch_pb2.BranchView, str]] = ...) -> None: ...
