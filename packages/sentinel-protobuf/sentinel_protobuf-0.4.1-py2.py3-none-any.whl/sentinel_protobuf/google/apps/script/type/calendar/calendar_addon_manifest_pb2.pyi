from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.apps.script.type import extension_point_pb2 as _extension_point_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CalendarAddOnManifest(_message.Message):
    __slots__ = ('homepage_trigger', 'conference_solution', 'create_settings_url_function', 'event_open_trigger', 'event_update_trigger', 'current_event_access')

    class EventAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CalendarAddOnManifest.EventAccess]
        METADATA: _ClassVar[CalendarAddOnManifest.EventAccess]
        READ: _ClassVar[CalendarAddOnManifest.EventAccess]
        WRITE: _ClassVar[CalendarAddOnManifest.EventAccess]
        READ_WRITE: _ClassVar[CalendarAddOnManifest.EventAccess]
    UNSPECIFIED: CalendarAddOnManifest.EventAccess
    METADATA: CalendarAddOnManifest.EventAccess
    READ: CalendarAddOnManifest.EventAccess
    WRITE: CalendarAddOnManifest.EventAccess
    READ_WRITE: CalendarAddOnManifest.EventAccess
    HOMEPAGE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CONFERENCE_SOLUTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_SETTINGS_URL_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_OPEN_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    EVENT_UPDATE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_EVENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    homepage_trigger: _extension_point_pb2.HomepageExtensionPoint
    conference_solution: _containers.RepeatedCompositeFieldContainer[ConferenceSolution]
    create_settings_url_function: str
    event_open_trigger: CalendarExtensionPoint
    event_update_trigger: CalendarExtensionPoint
    current_event_access: CalendarAddOnManifest.EventAccess

    def __init__(self, homepage_trigger: _Optional[_Union[_extension_point_pb2.HomepageExtensionPoint, _Mapping]]=..., conference_solution: _Optional[_Iterable[_Union[ConferenceSolution, _Mapping]]]=..., create_settings_url_function: _Optional[str]=..., event_open_trigger: _Optional[_Union[CalendarExtensionPoint, _Mapping]]=..., event_update_trigger: _Optional[_Union[CalendarExtensionPoint, _Mapping]]=..., current_event_access: _Optional[_Union[CalendarAddOnManifest.EventAccess, str]]=...) -> None:
        ...

class ConferenceSolution(_message.Message):
    __slots__ = ('on_create_function', 'id', 'name', 'logo_url')
    ON_CREATE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    on_create_function: str
    id: str
    name: str
    logo_url: str

    def __init__(self, on_create_function: _Optional[str]=..., id: _Optional[str]=..., name: _Optional[str]=..., logo_url: _Optional[str]=...) -> None:
        ...

class CalendarExtensionPoint(_message.Message):
    __slots__ = ('run_function',)
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    run_function: str

    def __init__(self, run_function: _Optional[str]=...) -> None:
        ...