from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as _flow_pb2
from google.cloud.dialogflow.cx.v3beta1 import intent_pb2 as _intent_pb2
from google.cloud.dialogflow.cx.v3beta1 import page_pb2 as _page_pb2
from google.cloud.dialogflow.cx.v3beta1 import response_message_pb2 as _response_message_pb2
from google.cloud.dialogflow.cx.v3beta1 import session_pb2 as _session_pb2
from google.cloud.dialogflow.cx.v3beta1 import transition_route_group_pb2 as _transition_route_group_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TestResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_RESULT_UNSPECIFIED: _ClassVar[TestResult]
    PASSED: _ClassVar[TestResult]
    FAILED: _ClassVar[TestResult]
TEST_RESULT_UNSPECIFIED: TestResult
PASSED: TestResult
FAILED: TestResult

class TestCase(_message.Message):
    __slots__ = ('name', 'tags', 'display_name', 'notes', 'test_config', 'test_case_conversation_turns', 'creation_time', 'last_test_result')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    TEST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEST_CASE_CONVERSATION_TURNS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    notes: str
    test_config: TestConfig
    test_case_conversation_turns: _containers.RepeatedCompositeFieldContainer[ConversationTurn]
    creation_time: _timestamp_pb2.Timestamp
    last_test_result: TestCaseResult

    def __init__(self, name: _Optional[str]=..., tags: _Optional[_Iterable[str]]=..., display_name: _Optional[str]=..., notes: _Optional[str]=..., test_config: _Optional[_Union[TestConfig, _Mapping]]=..., test_case_conversation_turns: _Optional[_Iterable[_Union[ConversationTurn, _Mapping]]]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_test_result: _Optional[_Union[TestCaseResult, _Mapping]]=...) -> None:
        ...

class TestCaseResult(_message.Message):
    __slots__ = ('name', 'environment', 'conversation_turns', 'test_result', 'test_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_TURNS_FIELD_NUMBER: _ClassVar[int]
    TEST_RESULT_FIELD_NUMBER: _ClassVar[int]
    TEST_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    environment: str
    conversation_turns: _containers.RepeatedCompositeFieldContainer[ConversationTurn]
    test_result: TestResult
    test_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., environment: _Optional[str]=..., conversation_turns: _Optional[_Iterable[_Union[ConversationTurn, _Mapping]]]=..., test_result: _Optional[_Union[TestResult, str]]=..., test_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TestConfig(_message.Message):
    __slots__ = ('tracking_parameters', 'flow', 'page')
    TRACKING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    tracking_parameters: _containers.RepeatedScalarFieldContainer[str]
    flow: str
    page: str

    def __init__(self, tracking_parameters: _Optional[_Iterable[str]]=..., flow: _Optional[str]=..., page: _Optional[str]=...) -> None:
        ...

class ConversationTurn(_message.Message):
    __slots__ = ('user_input', 'virtual_agent_output')

    class UserInput(_message.Message):
        __slots__ = ('input', 'injected_parameters', 'is_webhook_enabled', 'enable_sentiment_analysis')
        INPUT_FIELD_NUMBER: _ClassVar[int]
        INJECTED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        IS_WEBHOOK_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SENTIMENT_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
        input: _session_pb2.QueryInput
        injected_parameters: _struct_pb2.Struct
        is_webhook_enabled: bool
        enable_sentiment_analysis: bool

        def __init__(self, input: _Optional[_Union[_session_pb2.QueryInput, _Mapping]]=..., injected_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., is_webhook_enabled: bool=..., enable_sentiment_analysis: bool=...) -> None:
            ...

    class VirtualAgentOutput(_message.Message):
        __slots__ = ('session_parameters', 'differences', 'diagnostic_info', 'triggered_intent', 'current_page', 'text_responses', 'status')
        SESSION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        DIFFERENCES_FIELD_NUMBER: _ClassVar[int]
        DIAGNOSTIC_INFO_FIELD_NUMBER: _ClassVar[int]
        TRIGGERED_INTENT_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_RESPONSES_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        session_parameters: _struct_pb2.Struct
        differences: _containers.RepeatedCompositeFieldContainer[TestRunDifference]
        diagnostic_info: _struct_pb2.Struct
        triggered_intent: _intent_pb2.Intent
        current_page: _page_pb2.Page
        text_responses: _containers.RepeatedCompositeFieldContainer[_response_message_pb2.ResponseMessage.Text]
        status: _status_pb2.Status

        def __init__(self, session_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., differences: _Optional[_Iterable[_Union[TestRunDifference, _Mapping]]]=..., diagnostic_info: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., triggered_intent: _Optional[_Union[_intent_pb2.Intent, _Mapping]]=..., current_page: _Optional[_Union[_page_pb2.Page, _Mapping]]=..., text_responses: _Optional[_Iterable[_Union[_response_message_pb2.ResponseMessage.Text, _Mapping]]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_AGENT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    user_input: ConversationTurn.UserInput
    virtual_agent_output: ConversationTurn.VirtualAgentOutput

    def __init__(self, user_input: _Optional[_Union[ConversationTurn.UserInput, _Mapping]]=..., virtual_agent_output: _Optional[_Union[ConversationTurn.VirtualAgentOutput, _Mapping]]=...) -> None:
        ...

class TestRunDifference(_message.Message):
    __slots__ = ('type', 'description')

    class DiffType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIFF_TYPE_UNSPECIFIED: _ClassVar[TestRunDifference.DiffType]
        INTENT: _ClassVar[TestRunDifference.DiffType]
        PAGE: _ClassVar[TestRunDifference.DiffType]
        PARAMETERS: _ClassVar[TestRunDifference.DiffType]
        UTTERANCE: _ClassVar[TestRunDifference.DiffType]
        FLOW: _ClassVar[TestRunDifference.DiffType]
    DIFF_TYPE_UNSPECIFIED: TestRunDifference.DiffType
    INTENT: TestRunDifference.DiffType
    PAGE: TestRunDifference.DiffType
    PARAMETERS: TestRunDifference.DiffType
    UTTERANCE: TestRunDifference.DiffType
    FLOW: TestRunDifference.DiffType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    type: TestRunDifference.DiffType
    description: str

    def __init__(self, type: _Optional[_Union[TestRunDifference.DiffType, str]]=..., description: _Optional[str]=...) -> None:
        ...

class TransitionCoverage(_message.Message):
    __slots__ = ('transitions', 'coverage_score')

    class TransitionNode(_message.Message):
        __slots__ = ('page', 'flow')
        PAGE_FIELD_NUMBER: _ClassVar[int]
        FLOW_FIELD_NUMBER: _ClassVar[int]
        page: _page_pb2.Page
        flow: _flow_pb2.Flow

        def __init__(self, page: _Optional[_Union[_page_pb2.Page, _Mapping]]=..., flow: _Optional[_Union[_flow_pb2.Flow, _Mapping]]=...) -> None:
            ...

    class Transition(_message.Message):
        __slots__ = ('source', 'index', 'target', 'covered', 'transition_route', 'event_handler')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        COVERED_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_ROUTE_FIELD_NUMBER: _ClassVar[int]
        EVENT_HANDLER_FIELD_NUMBER: _ClassVar[int]
        source: TransitionCoverage.TransitionNode
        index: int
        target: TransitionCoverage.TransitionNode
        covered: bool
        transition_route: _page_pb2.TransitionRoute
        event_handler: _page_pb2.EventHandler

        def __init__(self, source: _Optional[_Union[TransitionCoverage.TransitionNode, _Mapping]]=..., index: _Optional[int]=..., target: _Optional[_Union[TransitionCoverage.TransitionNode, _Mapping]]=..., covered: bool=..., transition_route: _Optional[_Union[_page_pb2.TransitionRoute, _Mapping]]=..., event_handler: _Optional[_Union[_page_pb2.EventHandler, _Mapping]]=...) -> None:
            ...
    TRANSITIONS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_SCORE_FIELD_NUMBER: _ClassVar[int]
    transitions: _containers.RepeatedCompositeFieldContainer[TransitionCoverage.Transition]
    coverage_score: float

    def __init__(self, transitions: _Optional[_Iterable[_Union[TransitionCoverage.Transition, _Mapping]]]=..., coverage_score: _Optional[float]=...) -> None:
        ...

class TransitionRouteGroupCoverage(_message.Message):
    __slots__ = ('coverages', 'coverage_score')

    class Coverage(_message.Message):
        __slots__ = ('route_group', 'transitions', 'coverage_score')

        class Transition(_message.Message):
            __slots__ = ('transition_route', 'covered')
            TRANSITION_ROUTE_FIELD_NUMBER: _ClassVar[int]
            COVERED_FIELD_NUMBER: _ClassVar[int]
            transition_route: _page_pb2.TransitionRoute
            covered: bool

            def __init__(self, transition_route: _Optional[_Union[_page_pb2.TransitionRoute, _Mapping]]=..., covered: bool=...) -> None:
                ...
        ROUTE_GROUP_FIELD_NUMBER: _ClassVar[int]
        TRANSITIONS_FIELD_NUMBER: _ClassVar[int]
        COVERAGE_SCORE_FIELD_NUMBER: _ClassVar[int]
        route_group: _transition_route_group_pb2.TransitionRouteGroup
        transitions: _containers.RepeatedCompositeFieldContainer[TransitionRouteGroupCoverage.Coverage.Transition]
        coverage_score: float

        def __init__(self, route_group: _Optional[_Union[_transition_route_group_pb2.TransitionRouteGroup, _Mapping]]=..., transitions: _Optional[_Iterable[_Union[TransitionRouteGroupCoverage.Coverage.Transition, _Mapping]]]=..., coverage_score: _Optional[float]=...) -> None:
            ...
    COVERAGES_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_SCORE_FIELD_NUMBER: _ClassVar[int]
    coverages: _containers.RepeatedCompositeFieldContainer[TransitionRouteGroupCoverage.Coverage]
    coverage_score: float

    def __init__(self, coverages: _Optional[_Iterable[_Union[TransitionRouteGroupCoverage.Coverage, _Mapping]]]=..., coverage_score: _Optional[float]=...) -> None:
        ...

class IntentCoverage(_message.Message):
    __slots__ = ('intents', 'coverage_score')

    class Intent(_message.Message):
        __slots__ = ('intent', 'covered')
        INTENT_FIELD_NUMBER: _ClassVar[int]
        COVERED_FIELD_NUMBER: _ClassVar[int]
        intent: str
        covered: bool

        def __init__(self, intent: _Optional[str]=..., covered: bool=...) -> None:
            ...
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_SCORE_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[IntentCoverage.Intent]
    coverage_score: float

    def __init__(self, intents: _Optional[_Iterable[_Union[IntentCoverage.Intent, _Mapping]]]=..., coverage_score: _Optional[float]=...) -> None:
        ...

class CalculateCoverageRequest(_message.Message):
    __slots__ = ('agent', 'type')

    class CoverageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COVERAGE_TYPE_UNSPECIFIED: _ClassVar[CalculateCoverageRequest.CoverageType]
        INTENT: _ClassVar[CalculateCoverageRequest.CoverageType]
        PAGE_TRANSITION: _ClassVar[CalculateCoverageRequest.CoverageType]
        TRANSITION_ROUTE_GROUP: _ClassVar[CalculateCoverageRequest.CoverageType]
    COVERAGE_TYPE_UNSPECIFIED: CalculateCoverageRequest.CoverageType
    INTENT: CalculateCoverageRequest.CoverageType
    PAGE_TRANSITION: CalculateCoverageRequest.CoverageType
    TRANSITION_ROUTE_GROUP: CalculateCoverageRequest.CoverageType
    AGENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    agent: str
    type: CalculateCoverageRequest.CoverageType

    def __init__(self, agent: _Optional[str]=..., type: _Optional[_Union[CalculateCoverageRequest.CoverageType, str]]=...) -> None:
        ...

class CalculateCoverageResponse(_message.Message):
    __slots__ = ('agent', 'intent_coverage', 'transition_coverage', 'route_group_coverage')
    AGENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_GROUP_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    agent: str
    intent_coverage: IntentCoverage
    transition_coverage: TransitionCoverage
    route_group_coverage: TransitionRouteGroupCoverage

    def __init__(self, agent: _Optional[str]=..., intent_coverage: _Optional[_Union[IntentCoverage, _Mapping]]=..., transition_coverage: _Optional[_Union[TransitionCoverage, _Mapping]]=..., route_group_coverage: _Optional[_Union[TransitionRouteGroupCoverage, _Mapping]]=...) -> None:
        ...

class ListTestCasesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')

    class TestCaseView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEST_CASE_VIEW_UNSPECIFIED: _ClassVar[ListTestCasesRequest.TestCaseView]
        BASIC: _ClassVar[ListTestCasesRequest.TestCaseView]
        FULL: _ClassVar[ListTestCasesRequest.TestCaseView]
    TEST_CASE_VIEW_UNSPECIFIED: ListTestCasesRequest.TestCaseView
    BASIC: ListTestCasesRequest.TestCaseView
    FULL: ListTestCasesRequest.TestCaseView
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ListTestCasesRequest.TestCaseView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ListTestCasesRequest.TestCaseView, str]]=...) -> None:
        ...

class ListTestCasesResponse(_message.Message):
    __slots__ = ('test_cases', 'next_page_token')
    TEST_CASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    test_cases: _containers.RepeatedCompositeFieldContainer[TestCase]
    next_page_token: str

    def __init__(self, test_cases: _Optional[_Iterable[_Union[TestCase, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchDeleteTestCasesRequest(_message.Message):
    __slots__ = ('parent', 'names')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateTestCaseRequest(_message.Message):
    __slots__ = ('parent', 'test_case')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    test_case: TestCase

    def __init__(self, parent: _Optional[str]=..., test_case: _Optional[_Union[TestCase, _Mapping]]=...) -> None:
        ...

class UpdateTestCaseRequest(_message.Message):
    __slots__ = ('test_case', 'update_mask')
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    test_case: TestCase
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, test_case: _Optional[_Union[TestCase, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetTestCaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunTestCaseRequest(_message.Message):
    __slots__ = ('name', 'environment')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    environment: str

    def __init__(self, name: _Optional[str]=..., environment: _Optional[str]=...) -> None:
        ...

class RunTestCaseResponse(_message.Message):
    __slots__ = ('result',)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: TestCaseResult

    def __init__(self, result: _Optional[_Union[TestCaseResult, _Mapping]]=...) -> None:
        ...

class RunTestCaseMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BatchRunTestCasesRequest(_message.Message):
    __slots__ = ('parent', 'environment', 'test_cases')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TEST_CASES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment: str
    test_cases: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., environment: _Optional[str]=..., test_cases: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchRunTestCasesResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[TestCaseResult]

    def __init__(self, results: _Optional[_Iterable[_Union[TestCaseResult, _Mapping]]]=...) -> None:
        ...

class BatchRunTestCasesMetadata(_message.Message):
    __slots__ = ('errors',)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[TestError]

    def __init__(self, errors: _Optional[_Iterable[_Union[TestError, _Mapping]]]=...) -> None:
        ...

class TestError(_message.Message):
    __slots__ = ('test_case', 'status', 'test_time')
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEST_TIME_FIELD_NUMBER: _ClassVar[int]
    test_case: str
    status: _status_pb2.Status
    test_time: _timestamp_pb2.Timestamp

    def __init__(self, test_case: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., test_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ImportTestCasesRequest(_message.Message):
    __slots__ = ('parent', 'gcs_uri', 'content')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gcs_uri: str
    content: bytes

    def __init__(self, parent: _Optional[str]=..., gcs_uri: _Optional[str]=..., content: _Optional[bytes]=...) -> None:
        ...

class ImportTestCasesResponse(_message.Message):
    __slots__ = ('names',)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, names: _Optional[_Iterable[str]]=...) -> None:
        ...

class ImportTestCasesMetadata(_message.Message):
    __slots__ = ('errors',)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[TestCaseError]

    def __init__(self, errors: _Optional[_Iterable[_Union[TestCaseError, _Mapping]]]=...) -> None:
        ...

class TestCaseError(_message.Message):
    __slots__ = ('test_case', 'status')
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    test_case: TestCase
    status: _status_pb2.Status

    def __init__(self, test_case: _Optional[_Union[TestCase, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ExportTestCasesRequest(_message.Message):
    __slots__ = ('parent', 'gcs_uri', 'data_format', 'filter')

    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExportTestCasesRequest.DataFormat]
        BLOB: _ClassVar[ExportTestCasesRequest.DataFormat]
        JSON: _ClassVar[ExportTestCasesRequest.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExportTestCasesRequest.DataFormat
    BLOB: ExportTestCasesRequest.DataFormat
    JSON: ExportTestCasesRequest.DataFormat
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gcs_uri: str
    data_format: ExportTestCasesRequest.DataFormat
    filter: str

    def __init__(self, parent: _Optional[str]=..., gcs_uri: _Optional[str]=..., data_format: _Optional[_Union[ExportTestCasesRequest.DataFormat, str]]=..., filter: _Optional[str]=...) -> None:
        ...

class ExportTestCasesResponse(_message.Message):
    __slots__ = ('gcs_uri', 'content')
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str
    content: bytes

    def __init__(self, gcs_uri: _Optional[str]=..., content: _Optional[bytes]=...) -> None:
        ...

class ExportTestCasesMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListTestCaseResultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListTestCaseResultsResponse(_message.Message):
    __slots__ = ('test_case_results', 'next_page_token')
    TEST_CASE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    test_case_results: _containers.RepeatedCompositeFieldContainer[TestCaseResult]
    next_page_token: str

    def __init__(self, test_case_results: _Optional[_Iterable[_Union[TestCaseResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTestCaseResultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...