from google.apps.script.type import addon_widget_set_pb2 as _addon_widget_set_pb2
from google.apps.script.type import extension_point_pb2 as _extension_point_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GmailAddOnManifest(_message.Message):
    __slots__ = ('homepage_trigger', 'contextual_triggers', 'universal_actions', 'compose_trigger', 'authorization_check_function')
    HOMEPAGE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CONTEXTUAL_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPOSE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CHECK_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    homepage_trigger: _extension_point_pb2.HomepageExtensionPoint
    contextual_triggers: _containers.RepeatedCompositeFieldContainer[ContextualTrigger]
    universal_actions: _containers.RepeatedCompositeFieldContainer[UniversalAction]
    compose_trigger: ComposeTrigger
    authorization_check_function: str

    def __init__(self, homepage_trigger: _Optional[_Union[_extension_point_pb2.HomepageExtensionPoint, _Mapping]]=..., contextual_triggers: _Optional[_Iterable[_Union[ContextualTrigger, _Mapping]]]=..., universal_actions: _Optional[_Iterable[_Union[UniversalAction, _Mapping]]]=..., compose_trigger: _Optional[_Union[ComposeTrigger, _Mapping]]=..., authorization_check_function: _Optional[str]=...) -> None:
        ...

class UniversalAction(_message.Message):
    __slots__ = ('text', 'open_link', 'run_function')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OPEN_LINK_FIELD_NUMBER: _ClassVar[int]
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    text: str
    open_link: str
    run_function: str

    def __init__(self, text: _Optional[str]=..., open_link: _Optional[str]=..., run_function: _Optional[str]=...) -> None:
        ...

class ComposeTrigger(_message.Message):
    __slots__ = ('actions', 'draft_access')

    class DraftAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ComposeTrigger.DraftAccess]
        NONE: _ClassVar[ComposeTrigger.DraftAccess]
        METADATA: _ClassVar[ComposeTrigger.DraftAccess]
    UNSPECIFIED: ComposeTrigger.DraftAccess
    NONE: ComposeTrigger.DraftAccess
    METADATA: ComposeTrigger.DraftAccess
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_extension_point_pb2.MenuItemExtensionPoint]
    draft_access: ComposeTrigger.DraftAccess

    def __init__(self, actions: _Optional[_Iterable[_Union[_extension_point_pb2.MenuItemExtensionPoint, _Mapping]]]=..., draft_access: _Optional[_Union[ComposeTrigger.DraftAccess, str]]=...) -> None:
        ...

class ContextualTrigger(_message.Message):
    __slots__ = ('unconditional', 'on_trigger_function')
    UNCONDITIONAL_FIELD_NUMBER: _ClassVar[int]
    ON_TRIGGER_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    unconditional: UnconditionalTrigger
    on_trigger_function: str

    def __init__(self, unconditional: _Optional[_Union[UnconditionalTrigger, _Mapping]]=..., on_trigger_function: _Optional[str]=...) -> None:
        ...

class UnconditionalTrigger(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...