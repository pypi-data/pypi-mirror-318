from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValidationMessage(_message.Message):
    __slots__ = ('resource_type', 'resources', 'resource_names', 'severity', 'detail')

    class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESOURCE_TYPE_UNSPECIFIED: _ClassVar[ValidationMessage.ResourceType]
        AGENT: _ClassVar[ValidationMessage.ResourceType]
        INTENT: _ClassVar[ValidationMessage.ResourceType]
        INTENT_TRAINING_PHRASE: _ClassVar[ValidationMessage.ResourceType]
        INTENT_PARAMETER: _ClassVar[ValidationMessage.ResourceType]
        INTENTS: _ClassVar[ValidationMessage.ResourceType]
        INTENT_TRAINING_PHRASES: _ClassVar[ValidationMessage.ResourceType]
        ENTITY_TYPE: _ClassVar[ValidationMessage.ResourceType]
        ENTITY_TYPES: _ClassVar[ValidationMessage.ResourceType]
        WEBHOOK: _ClassVar[ValidationMessage.ResourceType]
        FLOW: _ClassVar[ValidationMessage.ResourceType]
        PAGE: _ClassVar[ValidationMessage.ResourceType]
        PAGES: _ClassVar[ValidationMessage.ResourceType]
        TRANSITION_ROUTE_GROUP: _ClassVar[ValidationMessage.ResourceType]
        AGENT_TRANSITION_ROUTE_GROUP: _ClassVar[ValidationMessage.ResourceType]
    RESOURCE_TYPE_UNSPECIFIED: ValidationMessage.ResourceType
    AGENT: ValidationMessage.ResourceType
    INTENT: ValidationMessage.ResourceType
    INTENT_TRAINING_PHRASE: ValidationMessage.ResourceType
    INTENT_PARAMETER: ValidationMessage.ResourceType
    INTENTS: ValidationMessage.ResourceType
    INTENT_TRAINING_PHRASES: ValidationMessage.ResourceType
    ENTITY_TYPE: ValidationMessage.ResourceType
    ENTITY_TYPES: ValidationMessage.ResourceType
    WEBHOOK: ValidationMessage.ResourceType
    FLOW: ValidationMessage.ResourceType
    PAGE: ValidationMessage.ResourceType
    PAGES: ValidationMessage.ResourceType
    TRANSITION_ROUTE_GROUP: ValidationMessage.ResourceType
    AGENT_TRANSITION_ROUTE_GROUP: ValidationMessage.ResourceType

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[ValidationMessage.Severity]
        INFO: _ClassVar[ValidationMessage.Severity]
        WARNING: _ClassVar[ValidationMessage.Severity]
        ERROR: _ClassVar[ValidationMessage.Severity]
    SEVERITY_UNSPECIFIED: ValidationMessage.Severity
    INFO: ValidationMessage.Severity
    WARNING: ValidationMessage.Severity
    ERROR: ValidationMessage.Severity
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    resource_type: ValidationMessage.ResourceType
    resources: _containers.RepeatedScalarFieldContainer[str]
    resource_names: _containers.RepeatedCompositeFieldContainer[ResourceName]
    severity: ValidationMessage.Severity
    detail: str

    def __init__(self, resource_type: _Optional[_Union[ValidationMessage.ResourceType, str]]=..., resources: _Optional[_Iterable[str]]=..., resource_names: _Optional[_Iterable[_Union[ResourceName, _Mapping]]]=..., severity: _Optional[_Union[ValidationMessage.Severity, str]]=..., detail: _Optional[str]=...) -> None:
        ...

class ResourceName(_message.Message):
    __slots__ = ('name', 'display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...