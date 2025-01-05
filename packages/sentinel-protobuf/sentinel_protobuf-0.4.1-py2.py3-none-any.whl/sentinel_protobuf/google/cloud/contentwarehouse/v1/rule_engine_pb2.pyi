from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RuleSet(_message.Message):
    __slots__ = ('name', 'description', 'source', 'rules')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source: str
    rules: _containers.RepeatedCompositeFieldContainer[Rule]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., source: _Optional[str]=..., rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=...) -> None:
        ...

class Rule(_message.Message):
    __slots__ = ('description', 'rule_id', 'trigger_type', 'condition', 'actions')

    class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Rule.TriggerType]
        ON_CREATE: _ClassVar[Rule.TriggerType]
        ON_UPDATE: _ClassVar[Rule.TriggerType]
        ON_CREATE_LINK: _ClassVar[Rule.TriggerType]
        ON_DELETE_LINK: _ClassVar[Rule.TriggerType]
    UNKNOWN: Rule.TriggerType
    ON_CREATE: Rule.TriggerType
    ON_UPDATE: Rule.TriggerType
    ON_CREATE_LINK: Rule.TriggerType
    ON_DELETE_LINK: Rule.TriggerType
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    description: str
    rule_id: str
    trigger_type: Rule.TriggerType
    condition: str
    actions: _containers.RepeatedCompositeFieldContainer[Action]

    def __init__(self, description: _Optional[str]=..., rule_id: _Optional[str]=..., trigger_type: _Optional[_Union[Rule.TriggerType, str]]=..., condition: _Optional[str]=..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]]=...) -> None:
        ...

class Action(_message.Message):
    __slots__ = ('action_id', 'access_control', 'data_validation', 'data_update', 'add_to_folder', 'publish_to_pub_sub', 'remove_from_folder_action', 'delete_document_action')
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    DATA_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    DATA_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ADD_TO_FOLDER_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TO_PUB_SUB_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FROM_FOLDER_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_DOCUMENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    access_control: AccessControlAction
    data_validation: DataValidationAction
    data_update: DataUpdateAction
    add_to_folder: AddToFolderAction
    publish_to_pub_sub: PublishAction
    remove_from_folder_action: RemoveFromFolderAction
    delete_document_action: DeleteDocumentAction

    def __init__(self, action_id: _Optional[str]=..., access_control: _Optional[_Union[AccessControlAction, _Mapping]]=..., data_validation: _Optional[_Union[DataValidationAction, _Mapping]]=..., data_update: _Optional[_Union[DataUpdateAction, _Mapping]]=..., add_to_folder: _Optional[_Union[AddToFolderAction, _Mapping]]=..., publish_to_pub_sub: _Optional[_Union[PublishAction, _Mapping]]=..., remove_from_folder_action: _Optional[_Union[RemoveFromFolderAction, _Mapping]]=..., delete_document_action: _Optional[_Union[DeleteDocumentAction, _Mapping]]=...) -> None:
        ...

class AccessControlAction(_message.Message):
    __slots__ = ('operation_type', 'policy')

    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[AccessControlAction.OperationType]
        ADD_POLICY_BINDING: _ClassVar[AccessControlAction.OperationType]
        REMOVE_POLICY_BINDING: _ClassVar[AccessControlAction.OperationType]
        REPLACE_POLICY_BINDING: _ClassVar[AccessControlAction.OperationType]
    UNKNOWN: AccessControlAction.OperationType
    ADD_POLICY_BINDING: AccessControlAction.OperationType
    REMOVE_POLICY_BINDING: AccessControlAction.OperationType
    REPLACE_POLICY_BINDING: AccessControlAction.OperationType
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    operation_type: AccessControlAction.OperationType
    policy: _policy_pb2.Policy

    def __init__(self, operation_type: _Optional[_Union[AccessControlAction.OperationType, str]]=..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=...) -> None:
        ...

class DataValidationAction(_message.Message):
    __slots__ = ('conditions',)

    class ConditionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.ScalarMap[str, str]

    def __init__(self, conditions: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class DataUpdateAction(_message.Message):
    __slots__ = ('entries',)

    class EntriesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.ScalarMap[str, str]

    def __init__(self, entries: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class AddToFolderAction(_message.Message):
    __slots__ = ('folders',)
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, folders: _Optional[_Iterable[str]]=...) -> None:
        ...

class RemoveFromFolderAction(_message.Message):
    __slots__ = ('condition', 'folder')
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    condition: str
    folder: str

    def __init__(self, condition: _Optional[str]=..., folder: _Optional[str]=...) -> None:
        ...

class PublishAction(_message.Message):
    __slots__ = ('topic_id', 'messages')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    messages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, topic_id: _Optional[str]=..., messages: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteDocumentAction(_message.Message):
    __slots__ = ('enable_hard_delete',)
    ENABLE_HARD_DELETE_FIELD_NUMBER: _ClassVar[int]
    enable_hard_delete: bool

    def __init__(self, enable_hard_delete: bool=...) -> None:
        ...

class RuleEngineOutput(_message.Message):
    __slots__ = ('document_name', 'rule_evaluator_output', 'action_executor_output')
    DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_EVALUATOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTOR_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    document_name: str
    rule_evaluator_output: RuleEvaluatorOutput
    action_executor_output: ActionExecutorOutput

    def __init__(self, document_name: _Optional[str]=..., rule_evaluator_output: _Optional[_Union[RuleEvaluatorOutput, _Mapping]]=..., action_executor_output: _Optional[_Union[ActionExecutorOutput, _Mapping]]=...) -> None:
        ...

class RuleEvaluatorOutput(_message.Message):
    __slots__ = ('triggered_rules', 'matched_rules', 'invalid_rules')
    TRIGGERED_RULES_FIELD_NUMBER: _ClassVar[int]
    MATCHED_RULES_FIELD_NUMBER: _ClassVar[int]
    INVALID_RULES_FIELD_NUMBER: _ClassVar[int]
    triggered_rules: _containers.RepeatedCompositeFieldContainer[Rule]
    matched_rules: _containers.RepeatedCompositeFieldContainer[Rule]
    invalid_rules: _containers.RepeatedCompositeFieldContainer[InvalidRule]

    def __init__(self, triggered_rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., matched_rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., invalid_rules: _Optional[_Iterable[_Union[InvalidRule, _Mapping]]]=...) -> None:
        ...

class InvalidRule(_message.Message):
    __slots__ = ('rule', 'error')
    RULE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    error: str

    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]]=..., error: _Optional[str]=...) -> None:
        ...

class ActionExecutorOutput(_message.Message):
    __slots__ = ('rule_actions_pairs',)
    RULE_ACTIONS_PAIRS_FIELD_NUMBER: _ClassVar[int]
    rule_actions_pairs: _containers.RepeatedCompositeFieldContainer[RuleActionsPair]

    def __init__(self, rule_actions_pairs: _Optional[_Iterable[_Union[RuleActionsPair, _Mapping]]]=...) -> None:
        ...

class RuleActionsPair(_message.Message):
    __slots__ = ('rule', 'action_outputs')
    RULE_FIELD_NUMBER: _ClassVar[int]
    ACTION_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    action_outputs: _containers.RepeatedCompositeFieldContainer[ActionOutput]

    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]]=..., action_outputs: _Optional[_Iterable[_Union[ActionOutput, _Mapping]]]=...) -> None:
        ...

class ActionOutput(_message.Message):
    __slots__ = ('action_id', 'action_state', 'output_message')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ActionOutput.State]
        ACTION_SUCCEEDED: _ClassVar[ActionOutput.State]
        ACTION_FAILED: _ClassVar[ActionOutput.State]
        ACTION_TIMED_OUT: _ClassVar[ActionOutput.State]
        ACTION_PENDING: _ClassVar[ActionOutput.State]
    UNKNOWN: ActionOutput.State
    ACTION_SUCCEEDED: ActionOutput.State
    ACTION_FAILED: ActionOutput.State
    ACTION_TIMED_OUT: ActionOutput.State
    ACTION_PENDING: ActionOutput.State
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_STATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    action_state: ActionOutput.State
    output_message: str

    def __init__(self, action_id: _Optional[str]=..., action_state: _Optional[_Union[ActionOutput.State, str]]=..., output_message: _Optional[str]=...) -> None:
        ...