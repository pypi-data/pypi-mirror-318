from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MediaFileErrorEnum(_message.Message):
    __slots__ = ()

    class MediaFileError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MediaFileErrorEnum.MediaFileError]
        UNKNOWN: _ClassVar[MediaFileErrorEnum.MediaFileError]
        CANNOT_CREATE_STANDARD_ICON: _ClassVar[MediaFileErrorEnum.MediaFileError]
        CANNOT_SELECT_STANDARD_ICON_WITH_OTHER_TYPES: _ClassVar[MediaFileErrorEnum.MediaFileError]
        CANNOT_SPECIFY_MEDIA_FILE_ID_AND_DATA: _ClassVar[MediaFileErrorEnum.MediaFileError]
        DUPLICATE_MEDIA: _ClassVar[MediaFileErrorEnum.MediaFileError]
        EMPTY_FIELD: _ClassVar[MediaFileErrorEnum.MediaFileError]
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS: _ClassVar[MediaFileErrorEnum.MediaFileError]
        FIELD_NOT_SUPPORTED_FOR_MEDIA_SUB_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_MEDIA_FILE_ID: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_MEDIA_SUB_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_MEDIA_FILE_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_MIME_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_REFERENCE_ID: _ClassVar[MediaFileErrorEnum.MediaFileError]
        INVALID_YOU_TUBE_ID: _ClassVar[MediaFileErrorEnum.MediaFileError]
        MEDIA_FILE_FAILED_TRANSCODING: _ClassVar[MediaFileErrorEnum.MediaFileError]
        MEDIA_NOT_TRANSCODED: _ClassVar[MediaFileErrorEnum.MediaFileError]
        MEDIA_TYPE_DOES_NOT_MATCH_MEDIA_FILE_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        NO_FIELDS_SPECIFIED: _ClassVar[MediaFileErrorEnum.MediaFileError]
        NULL_REFERENCE_ID_AND_MEDIA_ID: _ClassVar[MediaFileErrorEnum.MediaFileError]
        TOO_LONG: _ClassVar[MediaFileErrorEnum.MediaFileError]
        UNSUPPORTED_TYPE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        YOU_TUBE_SERVICE_UNAVAILABLE: _ClassVar[MediaFileErrorEnum.MediaFileError]
        YOU_TUBE_VIDEO_HAS_NON_POSITIVE_DURATION: _ClassVar[MediaFileErrorEnum.MediaFileError]
        YOU_TUBE_VIDEO_NOT_FOUND: _ClassVar[MediaFileErrorEnum.MediaFileError]
    UNSPECIFIED: MediaFileErrorEnum.MediaFileError
    UNKNOWN: MediaFileErrorEnum.MediaFileError
    CANNOT_CREATE_STANDARD_ICON: MediaFileErrorEnum.MediaFileError
    CANNOT_SELECT_STANDARD_ICON_WITH_OTHER_TYPES: MediaFileErrorEnum.MediaFileError
    CANNOT_SPECIFY_MEDIA_FILE_ID_AND_DATA: MediaFileErrorEnum.MediaFileError
    DUPLICATE_MEDIA: MediaFileErrorEnum.MediaFileError
    EMPTY_FIELD: MediaFileErrorEnum.MediaFileError
    RESOURCE_REFERENCED_IN_MULTIPLE_OPS: MediaFileErrorEnum.MediaFileError
    FIELD_NOT_SUPPORTED_FOR_MEDIA_SUB_TYPE: MediaFileErrorEnum.MediaFileError
    INVALID_MEDIA_FILE_ID: MediaFileErrorEnum.MediaFileError
    INVALID_MEDIA_SUB_TYPE: MediaFileErrorEnum.MediaFileError
    INVALID_MEDIA_FILE_TYPE: MediaFileErrorEnum.MediaFileError
    INVALID_MIME_TYPE: MediaFileErrorEnum.MediaFileError
    INVALID_REFERENCE_ID: MediaFileErrorEnum.MediaFileError
    INVALID_YOU_TUBE_ID: MediaFileErrorEnum.MediaFileError
    MEDIA_FILE_FAILED_TRANSCODING: MediaFileErrorEnum.MediaFileError
    MEDIA_NOT_TRANSCODED: MediaFileErrorEnum.MediaFileError
    MEDIA_TYPE_DOES_NOT_MATCH_MEDIA_FILE_TYPE: MediaFileErrorEnum.MediaFileError
    NO_FIELDS_SPECIFIED: MediaFileErrorEnum.MediaFileError
    NULL_REFERENCE_ID_AND_MEDIA_ID: MediaFileErrorEnum.MediaFileError
    TOO_LONG: MediaFileErrorEnum.MediaFileError
    UNSUPPORTED_TYPE: MediaFileErrorEnum.MediaFileError
    YOU_TUBE_SERVICE_UNAVAILABLE: MediaFileErrorEnum.MediaFileError
    YOU_TUBE_VIDEO_HAS_NON_POSITIVE_DURATION: MediaFileErrorEnum.MediaFileError
    YOU_TUBE_VIDEO_NOT_FOUND: MediaFileErrorEnum.MediaFileError

    def __init__(self) -> None:
        ...