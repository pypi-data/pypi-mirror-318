from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MimeTypeEnum(_message.Message):
    __slots__ = ()

    class MimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MimeTypeEnum.MimeType]
        UNKNOWN: _ClassVar[MimeTypeEnum.MimeType]
        IMAGE_JPEG: _ClassVar[MimeTypeEnum.MimeType]
        IMAGE_GIF: _ClassVar[MimeTypeEnum.MimeType]
        IMAGE_PNG: _ClassVar[MimeTypeEnum.MimeType]
        FLASH: _ClassVar[MimeTypeEnum.MimeType]
        TEXT_HTML: _ClassVar[MimeTypeEnum.MimeType]
        PDF: _ClassVar[MimeTypeEnum.MimeType]
        MSWORD: _ClassVar[MimeTypeEnum.MimeType]
        MSEXCEL: _ClassVar[MimeTypeEnum.MimeType]
        RTF: _ClassVar[MimeTypeEnum.MimeType]
        AUDIO_WAV: _ClassVar[MimeTypeEnum.MimeType]
        AUDIO_MP3: _ClassVar[MimeTypeEnum.MimeType]
        HTML5_AD_ZIP: _ClassVar[MimeTypeEnum.MimeType]
    UNSPECIFIED: MimeTypeEnum.MimeType
    UNKNOWN: MimeTypeEnum.MimeType
    IMAGE_JPEG: MimeTypeEnum.MimeType
    IMAGE_GIF: MimeTypeEnum.MimeType
    IMAGE_PNG: MimeTypeEnum.MimeType
    FLASH: MimeTypeEnum.MimeType
    TEXT_HTML: MimeTypeEnum.MimeType
    PDF: MimeTypeEnum.MimeType
    MSWORD: MimeTypeEnum.MimeType
    MSEXCEL: MimeTypeEnum.MimeType
    RTF: MimeTypeEnum.MimeType
    AUDIO_WAV: MimeTypeEnum.MimeType
    AUDIO_MP3: MimeTypeEnum.MimeType
    HTML5_AD_ZIP: MimeTypeEnum.MimeType

    def __init__(self) -> None:
        ...