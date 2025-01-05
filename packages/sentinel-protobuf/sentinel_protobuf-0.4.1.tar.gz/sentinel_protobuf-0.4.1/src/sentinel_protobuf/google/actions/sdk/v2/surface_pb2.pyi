from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SurfaceRequirements(_message.Message):
    __slots__ = ('minimum_requirements',)
    MINIMUM_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    minimum_requirements: _containers.RepeatedCompositeFieldContainer[CapabilityRequirement]

    def __init__(self, minimum_requirements: _Optional[_Iterable[_Union[CapabilityRequirement, _Mapping]]]=...) -> None:
        ...

class CapabilityRequirement(_message.Message):
    __slots__ = ('capability',)

    class SurfaceCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SURFACE_CAPABILITY_UNSPECIFIED: _ClassVar[CapabilityRequirement.SurfaceCapability]
        AUDIO_OUTPUT: _ClassVar[CapabilityRequirement.SurfaceCapability]
        SCREEN_OUTPUT: _ClassVar[CapabilityRequirement.SurfaceCapability]
        MEDIA_RESPONSE_AUDIO: _ClassVar[CapabilityRequirement.SurfaceCapability]
        WEB_BROWSER: _ClassVar[CapabilityRequirement.SurfaceCapability]
        ACCOUNT_LINKING: _ClassVar[CapabilityRequirement.SurfaceCapability]
        INTERACTIVE_CANVAS: _ClassVar[CapabilityRequirement.SurfaceCapability]
        HOME_STORAGE: _ClassVar[CapabilityRequirement.SurfaceCapability]
    SURFACE_CAPABILITY_UNSPECIFIED: CapabilityRequirement.SurfaceCapability
    AUDIO_OUTPUT: CapabilityRequirement.SurfaceCapability
    SCREEN_OUTPUT: CapabilityRequirement.SurfaceCapability
    MEDIA_RESPONSE_AUDIO: CapabilityRequirement.SurfaceCapability
    WEB_BROWSER: CapabilityRequirement.SurfaceCapability
    ACCOUNT_LINKING: CapabilityRequirement.SurfaceCapability
    INTERACTIVE_CANVAS: CapabilityRequirement.SurfaceCapability
    HOME_STORAGE: CapabilityRequirement.SurfaceCapability
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    capability: CapabilityRequirement.SurfaceCapability

    def __init__(self, capability: _Optional[_Union[CapabilityRequirement.SurfaceCapability, str]]=...) -> None:
        ...