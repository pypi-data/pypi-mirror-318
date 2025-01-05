from google.api import annotations_pb2 as _annotations_pb2
from google.cloud.runtimeconfig.v1beta1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConfigsResponse(_message.Message):
    __slots__ = ('configs', 'next_page_token')
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[_resources_pb2.RuntimeConfig]
    next_page_token: str

    def __init__(self, configs: _Optional[_Iterable[_Union[_resources_pb2.RuntimeConfig, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateConfigRequest(_message.Message):
    __slots__ = ('parent', 'config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    config: _resources_pb2.RuntimeConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., config: _Optional[_Union[_resources_pb2.RuntimeConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateConfigRequest(_message.Message):
    __slots__ = ('name', 'config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _resources_pb2.RuntimeConfig

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[_resources_pb2.RuntimeConfig, _Mapping]]=...) -> None:
        ...

class DeleteConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVariablesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'return_values')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RETURN_VALUES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    return_values: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., return_values: bool=...) -> None:
        ...

class ListVariablesResponse(_message.Message):
    __slots__ = ('variables', 'next_page_token')
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    variables: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Variable]
    next_page_token: str

    def __init__(self, variables: _Optional[_Iterable[_Union[_resources_pb2.Variable, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class WatchVariableRequest(_message.Message):
    __slots__ = ('name', 'newer_than')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEWER_THAN_FIELD_NUMBER: _ClassVar[int]
    name: str
    newer_than: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., newer_than: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetVariableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVariableRequest(_message.Message):
    __slots__ = ('parent', 'variable', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    variable: _resources_pb2.Variable
    request_id: str

    def __init__(self, parent: _Optional[str]=..., variable: _Optional[_Union[_resources_pb2.Variable, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateVariableRequest(_message.Message):
    __slots__ = ('name', 'variable')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    variable: _resources_pb2.Variable

    def __init__(self, name: _Optional[str]=..., variable: _Optional[_Union[_resources_pb2.Variable, _Mapping]]=...) -> None:
        ...

class DeleteVariableRequest(_message.Message):
    __slots__ = ('name', 'recursive')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    recursive: bool

    def __init__(self, name: _Optional[str]=..., recursive: bool=...) -> None:
        ...

class ListWaitersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWaitersResponse(_message.Message):
    __slots__ = ('waiters', 'next_page_token')
    WAITERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    waiters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Waiter]
    next_page_token: str

    def __init__(self, waiters: _Optional[_Iterable[_Union[_resources_pb2.Waiter, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetWaiterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWaiterRequest(_message.Message):
    __slots__ = ('parent', 'waiter', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WAITER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    waiter: _resources_pb2.Waiter
    request_id: str

    def __init__(self, parent: _Optional[str]=..., waiter: _Optional[_Union[_resources_pb2.Waiter, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteWaiterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...