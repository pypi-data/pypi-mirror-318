from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as _advanced_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import response_message_pb2 as _response_message_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Fulfillment(_message.Message):
    __slots__ = ('messages', 'webhook', 'return_partial_responses', 'tag', 'set_parameter_actions', 'conditional_cases', 'advanced_settings', 'enable_generative_fallback')

    class SetParameterAction(_message.Message):
        __slots__ = ('parameter', 'value')
        PARAMETER_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        parameter: str
        value: _struct_pb2.Value

        def __init__(self, parameter: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...

    class ConditionalCases(_message.Message):
        __slots__ = ('cases',)

        class Case(_message.Message):
            __slots__ = ('condition', 'case_content')

            class CaseContent(_message.Message):
                __slots__ = ('message', 'additional_cases')
                MESSAGE_FIELD_NUMBER: _ClassVar[int]
                ADDITIONAL_CASES_FIELD_NUMBER: _ClassVar[int]
                message: _response_message_pb2.ResponseMessage
                additional_cases: Fulfillment.ConditionalCases

                def __init__(self, message: _Optional[_Union[_response_message_pb2.ResponseMessage, _Mapping]]=..., additional_cases: _Optional[_Union[Fulfillment.ConditionalCases, _Mapping]]=...) -> None:
                    ...
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            CASE_CONTENT_FIELD_NUMBER: _ClassVar[int]
            condition: str
            case_content: _containers.RepeatedCompositeFieldContainer[Fulfillment.ConditionalCases.Case.CaseContent]

            def __init__(self, condition: _Optional[str]=..., case_content: _Optional[_Iterable[_Union[Fulfillment.ConditionalCases.Case.CaseContent, _Mapping]]]=...) -> None:
                ...
        CASES_FIELD_NUMBER: _ClassVar[int]
        cases: _containers.RepeatedCompositeFieldContainer[Fulfillment.ConditionalCases.Case]

        def __init__(self, cases: _Optional[_Iterable[_Union[Fulfillment.ConditionalCases.Case, _Mapping]]]=...) -> None:
            ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    RETURN_PARTIAL_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    SET_PARAMETER_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_CASES_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GENERATIVE_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_response_message_pb2.ResponseMessage]
    webhook: str
    return_partial_responses: bool
    tag: str
    set_parameter_actions: _containers.RepeatedCompositeFieldContainer[Fulfillment.SetParameterAction]
    conditional_cases: _containers.RepeatedCompositeFieldContainer[Fulfillment.ConditionalCases]
    advanced_settings: _advanced_settings_pb2.AdvancedSettings
    enable_generative_fallback: bool

    def __init__(self, messages: _Optional[_Iterable[_Union[_response_message_pb2.ResponseMessage, _Mapping]]]=..., webhook: _Optional[str]=..., return_partial_responses: bool=..., tag: _Optional[str]=..., set_parameter_actions: _Optional[_Iterable[_Union[Fulfillment.SetParameterAction, _Mapping]]]=..., conditional_cases: _Optional[_Iterable[_Union[Fulfillment.ConditionalCases, _Mapping]]]=..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]]=..., enable_generative_fallback: bool=...) -> None:
        ...