from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MediaBundleErrorEnum(_message.Message):
    __slots__ = ()

    class MediaBundleError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        UNKNOWN: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        BAD_REQUEST: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        DOUBLECLICK_BUNDLE_NOT_ALLOWED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        EXTERNAL_URL_NOT_ALLOWED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        FILE_TOO_LARGE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_INPUT: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_MEDIA_BUNDLE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_MEDIA_BUNDLE_ENTRY: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_MIME_TYPE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_PATH: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        INVALID_URL_REFERENCE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        MEDIA_DATA_TOO_LARGE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        SERVER_ERROR: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        STORAGE_ERROR: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        SWIFFY_BUNDLE_NOT_ALLOWED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        TOO_MANY_FILES: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        UNEXPECTED_SIZE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        UNSUPPORTED_HTML5_FEATURE: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
        CUSTOM_EXIT_NOT_ALLOWED: _ClassVar[MediaBundleErrorEnum.MediaBundleError]
    UNSPECIFIED: MediaBundleErrorEnum.MediaBundleError
    UNKNOWN: MediaBundleErrorEnum.MediaBundleError
    BAD_REQUEST: MediaBundleErrorEnum.MediaBundleError
    DOUBLECLICK_BUNDLE_NOT_ALLOWED: MediaBundleErrorEnum.MediaBundleError
    EXTERNAL_URL_NOT_ALLOWED: MediaBundleErrorEnum.MediaBundleError
    FILE_TOO_LARGE: MediaBundleErrorEnum.MediaBundleError
    GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: MediaBundleErrorEnum.MediaBundleError
    INVALID_INPUT: MediaBundleErrorEnum.MediaBundleError
    INVALID_MEDIA_BUNDLE: MediaBundleErrorEnum.MediaBundleError
    INVALID_MEDIA_BUNDLE_ENTRY: MediaBundleErrorEnum.MediaBundleError
    INVALID_MIME_TYPE: MediaBundleErrorEnum.MediaBundleError
    INVALID_PATH: MediaBundleErrorEnum.MediaBundleError
    INVALID_URL_REFERENCE: MediaBundleErrorEnum.MediaBundleError
    MEDIA_DATA_TOO_LARGE: MediaBundleErrorEnum.MediaBundleError
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: MediaBundleErrorEnum.MediaBundleError
    SERVER_ERROR: MediaBundleErrorEnum.MediaBundleError
    STORAGE_ERROR: MediaBundleErrorEnum.MediaBundleError
    SWIFFY_BUNDLE_NOT_ALLOWED: MediaBundleErrorEnum.MediaBundleError
    TOO_MANY_FILES: MediaBundleErrorEnum.MediaBundleError
    UNEXPECTED_SIZE: MediaBundleErrorEnum.MediaBundleError
    UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: MediaBundleErrorEnum.MediaBundleError
    UNSUPPORTED_HTML5_FEATURE: MediaBundleErrorEnum.MediaBundleError
    URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: MediaBundleErrorEnum.MediaBundleError
    CUSTOM_EXIT_NOT_ALLOWED: MediaBundleErrorEnum.MediaBundleError

    def __init__(self) -> None:
        ...