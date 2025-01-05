from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Deployment(_message.Message):
    __slots__ = ('name', 'flow_version', 'state', 'result', 'start_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Deployment.State]
        RUNNING: _ClassVar[Deployment.State]
        SUCCEEDED: _ClassVar[Deployment.State]
        FAILED: _ClassVar[Deployment.State]
    STATE_UNSPECIFIED: Deployment.State
    RUNNING: Deployment.State
    SUCCEEDED: Deployment.State
    FAILED: Deployment.State

    class Result(_message.Message):
        __slots__ = ('deployment_test_results', 'experiment')
        DEPLOYMENT_TEST_RESULTS_FIELD_NUMBER: _ClassVar[int]
        EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
        deployment_test_results: _containers.RepeatedScalarFieldContainer[str]
        experiment: str

        def __init__(self, deployment_test_results: _Optional[_Iterable[str]]=..., experiment: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLOW_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    flow_version: str
    state: Deployment.State
    result: Deployment.Result
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., flow_version: _Optional[str]=..., state: _Optional[_Union[Deployment.State, str]]=..., result: _Optional[_Union[Deployment.Result, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...