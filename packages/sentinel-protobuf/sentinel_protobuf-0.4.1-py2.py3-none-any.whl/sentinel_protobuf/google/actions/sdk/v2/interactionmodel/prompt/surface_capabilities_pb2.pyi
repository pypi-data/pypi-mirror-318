from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SurfaceCapabilities(_message.Message):
    __slots__ = ('capabilities',)

    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SurfaceCapabilities.Capability]
        SPEECH: _ClassVar[SurfaceCapabilities.Capability]
        RICH_RESPONSE: _ClassVar[SurfaceCapabilities.Capability]
        LONG_FORM_AUDIO: _ClassVar[SurfaceCapabilities.Capability]
        INTERACTIVE_CANVAS: _ClassVar[SurfaceCapabilities.Capability]
        WEB_LINK: _ClassVar[SurfaceCapabilities.Capability]
        HOME_STORAGE: _ClassVar[SurfaceCapabilities.Capability]
    UNSPECIFIED: SurfaceCapabilities.Capability
    SPEECH: SurfaceCapabilities.Capability
    RICH_RESPONSE: SurfaceCapabilities.Capability
    LONG_FORM_AUDIO: SurfaceCapabilities.Capability
    INTERACTIVE_CANVAS: SurfaceCapabilities.Capability
    WEB_LINK: SurfaceCapabilities.Capability
    HOME_STORAGE: SurfaceCapabilities.Capability
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedScalarFieldContainer[SurfaceCapabilities.Capability]

    def __init__(self, capabilities: _Optional[_Iterable[_Union[SurfaceCapabilities.Capability, str]]]=...) -> None:
        ...