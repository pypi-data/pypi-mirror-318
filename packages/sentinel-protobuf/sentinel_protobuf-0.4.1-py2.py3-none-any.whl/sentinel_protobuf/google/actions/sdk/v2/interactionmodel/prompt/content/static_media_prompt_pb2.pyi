from google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as _static_image_prompt_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticMediaPrompt(_message.Message):
    __slots__ = ('media_type', 'start_offset', 'optional_media_controls', 'media_objects', 'repeat_mode')

    class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIA_TYPE_UNSPECIFIED: _ClassVar[StaticMediaPrompt.MediaType]
        AUDIO: _ClassVar[StaticMediaPrompt.MediaType]
        MEDIA_STATUS_ACK: _ClassVar[StaticMediaPrompt.MediaType]
    MEDIA_TYPE_UNSPECIFIED: StaticMediaPrompt.MediaType
    AUDIO: StaticMediaPrompt.MediaType
    MEDIA_STATUS_ACK: StaticMediaPrompt.MediaType

    class OptionalMediaControls(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED: _ClassVar[StaticMediaPrompt.OptionalMediaControls]
        PAUSED: _ClassVar[StaticMediaPrompt.OptionalMediaControls]
        STOPPED: _ClassVar[StaticMediaPrompt.OptionalMediaControls]
    OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED: StaticMediaPrompt.OptionalMediaControls
    PAUSED: StaticMediaPrompt.OptionalMediaControls
    STOPPED: StaticMediaPrompt.OptionalMediaControls

    class RepeatMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPEAT_MODE_UNSPECIFIED: _ClassVar[StaticMediaPrompt.RepeatMode]
        OFF: _ClassVar[StaticMediaPrompt.RepeatMode]
        ALL: _ClassVar[StaticMediaPrompt.RepeatMode]
    REPEAT_MODE_UNSPECIFIED: StaticMediaPrompt.RepeatMode
    OFF: StaticMediaPrompt.RepeatMode
    ALL: StaticMediaPrompt.RepeatMode
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MEDIA_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    REPEAT_MODE_FIELD_NUMBER: _ClassVar[int]
    media_type: StaticMediaPrompt.MediaType
    start_offset: _duration_pb2.Duration
    optional_media_controls: _containers.RepeatedScalarFieldContainer[StaticMediaPrompt.OptionalMediaControls]
    media_objects: _containers.RepeatedCompositeFieldContainer[MediaObject]
    repeat_mode: StaticMediaPrompt.RepeatMode

    def __init__(self, media_type: _Optional[_Union[StaticMediaPrompt.MediaType, str]]=..., start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., optional_media_controls: _Optional[_Iterable[_Union[StaticMediaPrompt.OptionalMediaControls, str]]]=..., media_objects: _Optional[_Iterable[_Union[MediaObject, _Mapping]]]=..., repeat_mode: _Optional[_Union[StaticMediaPrompt.RepeatMode, str]]=...) -> None:
        ...

class MediaObject(_message.Message):
    __slots__ = ('name', 'description', 'url', 'image')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    url: str
    image: MediaImage

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., url: _Optional[str]=..., image: _Optional[_Union[MediaImage, _Mapping]]=...) -> None:
        ...

class MediaImage(_message.Message):
    __slots__ = ('large', 'icon')
    LARGE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    large: _static_image_prompt_pb2.StaticImagePrompt
    icon: _static_image_prompt_pb2.StaticImagePrompt

    def __init__(self, large: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=..., icon: _Optional[_Union[_static_image_prompt_pb2.StaticImagePrompt, _Mapping]]=...) -> None:
        ...