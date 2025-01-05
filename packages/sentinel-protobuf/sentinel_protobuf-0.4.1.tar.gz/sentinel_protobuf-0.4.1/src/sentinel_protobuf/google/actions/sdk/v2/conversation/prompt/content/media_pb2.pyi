from google.actions.sdk.v2.conversation.prompt.content import image_pb2 as _image_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Media(_message.Message):
    __slots__ = ('media_type', 'start_offset', 'optional_media_controls', 'media_objects')

    class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIA_TYPE_UNSPECIFIED: _ClassVar[Media.MediaType]
        AUDIO: _ClassVar[Media.MediaType]
        MEDIA_STATUS_ACK: _ClassVar[Media.MediaType]
    MEDIA_TYPE_UNSPECIFIED: Media.MediaType
    AUDIO: Media.MediaType
    MEDIA_STATUS_ACK: Media.MediaType

    class OptionalMediaControls(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED: _ClassVar[Media.OptionalMediaControls]
        PAUSED: _ClassVar[Media.OptionalMediaControls]
        STOPPED: _ClassVar[Media.OptionalMediaControls]
    OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED: Media.OptionalMediaControls
    PAUSED: Media.OptionalMediaControls
    STOPPED: Media.OptionalMediaControls
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MEDIA_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    media_type: Media.MediaType
    start_offset: _duration_pb2.Duration
    optional_media_controls: _containers.RepeatedScalarFieldContainer[Media.OptionalMediaControls]
    media_objects: _containers.RepeatedCompositeFieldContainer[MediaObject]

    def __init__(self, media_type: _Optional[_Union[Media.MediaType, str]]=..., start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., optional_media_controls: _Optional[_Iterable[_Union[Media.OptionalMediaControls, str]]]=..., media_objects: _Optional[_Iterable[_Union[MediaObject, _Mapping]]]=...) -> None:
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
    large: _image_pb2.Image
    icon: _image_pb2.Image

    def __init__(self, large: _Optional[_Union[_image_pb2.Image, _Mapping]]=..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]]=...) -> None:
        ...