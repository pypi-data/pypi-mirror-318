from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import test_case_pb2 as _test_case_pb2
from google.cloud.dialogflow.cx.v3beta1 import webhook_pb2 as _webhook_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'version_configs', 'update_time', 'test_cases_config', 'webhook_config')

    class VersionConfig(_message.Message):
        __slots__ = ('version',)
        VERSION_FIELD_NUMBER: _ClassVar[int]
        version: str

        def __init__(self, version: _Optional[str]=...) -> None:
            ...

    class TestCasesConfig(_message.Message):
        __slots__ = ('test_cases', 'enable_continuous_run', 'enable_predeployment_run')
        TEST_CASES_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CONTINUOUS_RUN_FIELD_NUMBER: _ClassVar[int]
        ENABLE_PREDEPLOYMENT_RUN_FIELD_NUMBER: _ClassVar[int]
        test_cases: _containers.RepeatedScalarFieldContainer[str]
        enable_continuous_run: bool
        enable_predeployment_run: bool

        def __init__(self, test_cases: _Optional[_Iterable[str]]=..., enable_continuous_run: bool=..., enable_predeployment_run: bool=...) -> None:
            ...

    class WebhookConfig(_message.Message):
        __slots__ = ('webhook_overrides',)
        WEBHOOK_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
        webhook_overrides: _containers.RepeatedCompositeFieldContainer[_webhook_pb2.Webhook]

        def __init__(self, webhook_overrides: _Optional[_Iterable[_Union[_webhook_pb2.Webhook, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TEST_CASES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    version_configs: _containers.RepeatedCompositeFieldContainer[Environment.VersionConfig]
    update_time: _timestamp_pb2.Timestamp
    test_cases_config: Environment.TestCasesConfig
    webhook_config: Environment.WebhookConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., version_configs: _Optional[_Iterable[_Union[Environment.VersionConfig, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., test_cases_config: _Optional[_Union[Environment.TestCasesConfig, _Mapping]]=..., webhook_config: _Optional[_Union[Environment.WebhookConfig, _Mapping]]=...) -> None:
        ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    next_page_token: str

    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ('parent', 'environment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment: Environment

    def __init__(self, parent: _Optional[str]=..., environment: _Optional[_Union[Environment, _Mapping]]=...) -> None:
        ...

class UpdateEnvironmentRequest(_message.Message):
    __slots__ = ('environment', 'update_mask')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    environment: Environment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupEnvironmentHistoryRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupEnvironmentHistoryResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    next_page_token: str

    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ContinuousTestResult(_message.Message):
    __slots__ = ('name', 'result', 'test_case_results', 'run_time')

    class AggregatedTestResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATED_TEST_RESULT_UNSPECIFIED: _ClassVar[ContinuousTestResult.AggregatedTestResult]
        PASSED: _ClassVar[ContinuousTestResult.AggregatedTestResult]
        FAILED: _ClassVar[ContinuousTestResult.AggregatedTestResult]
    AGGREGATED_TEST_RESULT_UNSPECIFIED: ContinuousTestResult.AggregatedTestResult
    PASSED: ContinuousTestResult.AggregatedTestResult
    FAILED: ContinuousTestResult.AggregatedTestResult
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_CASE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    result: ContinuousTestResult.AggregatedTestResult
    test_case_results: _containers.RepeatedScalarFieldContainer[str]
    run_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., result: _Optional[_Union[ContinuousTestResult.AggregatedTestResult, str]]=..., test_case_results: _Optional[_Iterable[str]]=..., run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RunContinuousTestRequest(_message.Message):
    __slots__ = ('environment',)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: str

    def __init__(self, environment: _Optional[str]=...) -> None:
        ...

class RunContinuousTestResponse(_message.Message):
    __slots__ = ('continuous_test_result',)
    CONTINUOUS_TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    continuous_test_result: ContinuousTestResult

    def __init__(self, continuous_test_result: _Optional[_Union[ContinuousTestResult, _Mapping]]=...) -> None:
        ...

class RunContinuousTestMetadata(_message.Message):
    __slots__ = ('errors',)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_test_case_pb2.TestError]

    def __init__(self, errors: _Optional[_Iterable[_Union[_test_case_pb2.TestError, _Mapping]]]=...) -> None:
        ...

class ListContinuousTestResultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListContinuousTestResultsResponse(_message.Message):
    __slots__ = ('continuous_test_results', 'next_page_token')
    CONTINUOUS_TEST_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    continuous_test_results: _containers.RepeatedCompositeFieldContainer[ContinuousTestResult]
    next_page_token: str

    def __init__(self, continuous_test_results: _Optional[_Iterable[_Union[ContinuousTestResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeployFlowRequest(_message.Message):
    __slots__ = ('environment', 'flow_version')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FLOW_VERSION_FIELD_NUMBER: _ClassVar[int]
    environment: str
    flow_version: str

    def __init__(self, environment: _Optional[str]=..., flow_version: _Optional[str]=...) -> None:
        ...

class DeployFlowResponse(_message.Message):
    __slots__ = ('environment', 'deployment')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    environment: Environment
    deployment: str

    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]]=..., deployment: _Optional[str]=...) -> None:
        ...

class DeployFlowMetadata(_message.Message):
    __slots__ = ('test_errors',)
    TEST_ERRORS_FIELD_NUMBER: _ClassVar[int]
    test_errors: _containers.RepeatedCompositeFieldContainer[_test_case_pb2.TestError]

    def __init__(self, test_errors: _Optional[_Iterable[_Union[_test_case_pb2.TestError, _Mapping]]]=...) -> None:
        ...