from google.actions.sdk.v2.conversation import intent_pb2 as _intent_pb2
from google.actions.sdk.v2.conversation.prompt import prompt_pb2 as _prompt_pb2
from google.actions.sdk.v2.conversation import scene_pb2 as _scene_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionEvent(_message.Message):
    __slots__ = ('event_time', 'execution_state', 'status', 'user_input', 'intent_match', 'conditions_evaluated', 'on_scene_enter', 'webhook_request', 'webhook_response', 'webhook_initiated_transition', 'slot_match', 'slot_requested', 'slot_validated', 'form_filled', 'waiting_user_input', 'end_conversation', 'warning_messages')
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    INTENT_MATCH_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_EVALUATED_FIELD_NUMBER: _ClassVar[int]
    ON_SCENE_ENTER_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_INITIATED_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    SLOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    SLOT_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SLOT_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    FORM_FILLED_FIELD_NUMBER: _ClassVar[int]
    WAITING_USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    END_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp
    execution_state: ExecutionState
    status: _status_pb2.Status
    user_input: UserConversationInput
    intent_match: IntentMatch
    conditions_evaluated: ConditionsEvaluated
    on_scene_enter: OnSceneEnter
    webhook_request: WebhookRequest
    webhook_response: WebhookResponse
    webhook_initiated_transition: WebhookInitiatedTransition
    slot_match: SlotMatch
    slot_requested: SlotRequested
    slot_validated: SlotValidated
    form_filled: FormFilled
    waiting_user_input: WaitingForUserInput
    end_conversation: EndConversation
    warning_messages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., execution_state: _Optional[_Union[ExecutionState, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., user_input: _Optional[_Union[UserConversationInput, _Mapping]]=..., intent_match: _Optional[_Union[IntentMatch, _Mapping]]=..., conditions_evaluated: _Optional[_Union[ConditionsEvaluated, _Mapping]]=..., on_scene_enter: _Optional[_Union[OnSceneEnter, _Mapping]]=..., webhook_request: _Optional[_Union[WebhookRequest, _Mapping]]=..., webhook_response: _Optional[_Union[WebhookResponse, _Mapping]]=..., webhook_initiated_transition: _Optional[_Union[WebhookInitiatedTransition, _Mapping]]=..., slot_match: _Optional[_Union[SlotMatch, _Mapping]]=..., slot_requested: _Optional[_Union[SlotRequested, _Mapping]]=..., slot_validated: _Optional[_Union[SlotValidated, _Mapping]]=..., form_filled: _Optional[_Union[FormFilled, _Mapping]]=..., waiting_user_input: _Optional[_Union[WaitingForUserInput, _Mapping]]=..., end_conversation: _Optional[_Union[EndConversation, _Mapping]]=..., warning_messages: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExecutionState(_message.Message):
    __slots__ = ('current_scene_id', 'session_storage', 'slots', 'prompt_queue', 'user_storage', 'household_storage')
    CURRENT_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_STORAGE_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_QUEUE_FIELD_NUMBER: _ClassVar[int]
    USER_STORAGE_FIELD_NUMBER: _ClassVar[int]
    HOUSEHOLD_STORAGE_FIELD_NUMBER: _ClassVar[int]
    current_scene_id: str
    session_storage: _struct_pb2.Struct
    slots: Slots
    prompt_queue: _containers.RepeatedCompositeFieldContainer[_prompt_pb2.Prompt]
    user_storage: _struct_pb2.Struct
    household_storage: _struct_pb2.Struct

    def __init__(self, current_scene_id: _Optional[str]=..., session_storage: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., slots: _Optional[_Union[Slots, _Mapping]]=..., prompt_queue: _Optional[_Iterable[_Union[_prompt_pb2.Prompt, _Mapping]]]=..., user_storage: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., household_storage: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Slots(_message.Message):
    __slots__ = ('status', 'slots')

    class SlotsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _scene_pb2.Slot

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_scene_pb2.Slot, _Mapping]]=...) -> None:
            ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    status: _scene_pb2.SlotFillingStatus
    slots: _containers.MessageMap[str, _scene_pb2.Slot]

    def __init__(self, status: _Optional[_Union[_scene_pb2.SlotFillingStatus, str]]=..., slots: _Optional[_Mapping[str, _scene_pb2.Slot]]=...) -> None:
        ...

class UserConversationInput(_message.Message):
    __slots__ = ('type', 'original_query')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_QUERY_FIELD_NUMBER: _ClassVar[int]
    type: str
    original_query: str

    def __init__(self, type: _Optional[str]=..., original_query: _Optional[str]=...) -> None:
        ...

class IntentMatch(_message.Message):
    __slots__ = ('intent_id', 'intent_parameters', 'handler', 'next_scene_id')

    class IntentParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _intent_pb2.IntentParameterValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_intent_pb2.IntentParameterValue, _Mapping]]=...) -> None:
            ...
    INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    HANDLER_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    intent_id: str
    intent_parameters: _containers.MessageMap[str, _intent_pb2.IntentParameterValue]
    handler: str
    next_scene_id: str

    def __init__(self, intent_id: _Optional[str]=..., intent_parameters: _Optional[_Mapping[str, _intent_pb2.IntentParameterValue]]=..., handler: _Optional[str]=..., next_scene_id: _Optional[str]=...) -> None:
        ...

class ConditionsEvaluated(_message.Message):
    __slots__ = ('failed_conditions', 'success_condition')
    FAILED_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_CONDITION_FIELD_NUMBER: _ClassVar[int]
    failed_conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    success_condition: Condition

    def __init__(self, failed_conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]]=..., success_condition: _Optional[_Union[Condition, _Mapping]]=...) -> None:
        ...

class Condition(_message.Message):
    __slots__ = ('expression', 'handler', 'next_scene_id')
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    HANDLER_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    expression: str
    handler: str
    next_scene_id: str

    def __init__(self, expression: _Optional[str]=..., handler: _Optional[str]=..., next_scene_id: _Optional[str]=...) -> None:
        ...

class OnSceneEnter(_message.Message):
    __slots__ = ('handler',)
    HANDLER_FIELD_NUMBER: _ClassVar[int]
    handler: str

    def __init__(self, handler: _Optional[str]=...) -> None:
        ...

class WebhookInitiatedTransition(_message.Message):
    __slots__ = ('next_scene_id',)
    NEXT_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    next_scene_id: str

    def __init__(self, next_scene_id: _Optional[str]=...) -> None:
        ...

class WebhookRequest(_message.Message):
    __slots__ = ('request_json',)
    REQUEST_JSON_FIELD_NUMBER: _ClassVar[int]
    request_json: str

    def __init__(self, request_json: _Optional[str]=...) -> None:
        ...

class WebhookResponse(_message.Message):
    __slots__ = ('response_json',)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str

    def __init__(self, response_json: _Optional[str]=...) -> None:
        ...

class SlotMatch(_message.Message):
    __slots__ = ('nlu_parameters',)

    class NluParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _intent_pb2.IntentParameterValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_intent_pb2.IntentParameterValue, _Mapping]]=...) -> None:
            ...
    NLU_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    nlu_parameters: _containers.MessageMap[str, _intent_pb2.IntentParameterValue]

    def __init__(self, nlu_parameters: _Optional[_Mapping[str, _intent_pb2.IntentParameterValue]]=...) -> None:
        ...

class SlotRequested(_message.Message):
    __slots__ = ('slot', 'prompt')
    SLOT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    slot: str
    prompt: _prompt_pb2.Prompt

    def __init__(self, slot: _Optional[str]=..., prompt: _Optional[_Union[_prompt_pb2.Prompt, _Mapping]]=...) -> None:
        ...

class SlotValidated(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FormFilled(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WaitingForUserInput(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EndConversation(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...