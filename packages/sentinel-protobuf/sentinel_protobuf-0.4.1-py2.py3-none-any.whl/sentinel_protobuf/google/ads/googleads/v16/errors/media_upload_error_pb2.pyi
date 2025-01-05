from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MediaUploadErrorEnum(_message.Message):
    __slots__ = ()

    class MediaUploadError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        UNKNOWN: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        FILE_TOO_BIG: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        UNPARSEABLE_IMAGE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        ANIMATED_IMAGE_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        FORMAT_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        EXTERNAL_URL_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        INVALID_URL_REFERENCE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        ANIMATED_VISUAL_EFFECT: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        ANIMATION_TOO_LONG: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        ASPECT_RATIO_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        AUDIO_NOT_ALLOWED_IN_MEDIA_BUNDLE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        CMYK_JPEG_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        FLASH_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        FRAME_RATE_TOO_HIGH: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        IMAGE_CONSTRAINTS_VIOLATED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        INVALID_MEDIA_BUNDLE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        INVALID_MEDIA_BUNDLE_ENTRY: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        INVALID_MIME_TYPE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        INVALID_PATH: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        LAYOUT_PROBLEM: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        MALFORMED_URL: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        MEDIA_BUNDLE_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        MEDIA_BUNDLE_NOT_COMPATIBLE_TO_PRODUCT_TYPE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        MEDIA_BUNDLE_REJECTED_BY_MULTIPLE_ASSET_SPECS: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        TOO_MANY_FILES_IN_MEDIA_BUNDLE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        UNSUPPORTED_HTML5_FEATURE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        VIDEO_FILE_NAME_TOO_LONG: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        VIDEO_MULTIPLE_FILES_WITH_SAME_NAME: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        VIDEO_NOT_ALLOWED_IN_MEDIA_BUNDLE: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        CANNOT_UPLOAD_MEDIA_TYPE_THROUGH_API: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
        DIMENSIONS_NOT_ALLOWED: _ClassVar[MediaUploadErrorEnum.MediaUploadError]
    UNSPECIFIED: MediaUploadErrorEnum.MediaUploadError
    UNKNOWN: MediaUploadErrorEnum.MediaUploadError
    FILE_TOO_BIG: MediaUploadErrorEnum.MediaUploadError
    UNPARSEABLE_IMAGE: MediaUploadErrorEnum.MediaUploadError
    ANIMATED_IMAGE_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    FORMAT_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    EXTERNAL_URL_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    INVALID_URL_REFERENCE: MediaUploadErrorEnum.MediaUploadError
    MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY: MediaUploadErrorEnum.MediaUploadError
    ANIMATED_VISUAL_EFFECT: MediaUploadErrorEnum.MediaUploadError
    ANIMATION_TOO_LONG: MediaUploadErrorEnum.MediaUploadError
    ASPECT_RATIO_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    AUDIO_NOT_ALLOWED_IN_MEDIA_BUNDLE: MediaUploadErrorEnum.MediaUploadError
    CMYK_JPEG_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    FLASH_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    FRAME_RATE_TOO_HIGH: MediaUploadErrorEnum.MediaUploadError
    GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED: MediaUploadErrorEnum.MediaUploadError
    IMAGE_CONSTRAINTS_VIOLATED: MediaUploadErrorEnum.MediaUploadError
    INVALID_MEDIA_BUNDLE: MediaUploadErrorEnum.MediaUploadError
    INVALID_MEDIA_BUNDLE_ENTRY: MediaUploadErrorEnum.MediaUploadError
    INVALID_MIME_TYPE: MediaUploadErrorEnum.MediaUploadError
    INVALID_PATH: MediaUploadErrorEnum.MediaUploadError
    LAYOUT_PROBLEM: MediaUploadErrorEnum.MediaUploadError
    MALFORMED_URL: MediaUploadErrorEnum.MediaUploadError
    MEDIA_BUNDLE_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError
    MEDIA_BUNDLE_NOT_COMPATIBLE_TO_PRODUCT_TYPE: MediaUploadErrorEnum.MediaUploadError
    MEDIA_BUNDLE_REJECTED_BY_MULTIPLE_ASSET_SPECS: MediaUploadErrorEnum.MediaUploadError
    TOO_MANY_FILES_IN_MEDIA_BUNDLE: MediaUploadErrorEnum.MediaUploadError
    UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT: MediaUploadErrorEnum.MediaUploadError
    UNSUPPORTED_HTML5_FEATURE: MediaUploadErrorEnum.MediaUploadError
    URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT: MediaUploadErrorEnum.MediaUploadError
    VIDEO_FILE_NAME_TOO_LONG: MediaUploadErrorEnum.MediaUploadError
    VIDEO_MULTIPLE_FILES_WITH_SAME_NAME: MediaUploadErrorEnum.MediaUploadError
    VIDEO_NOT_ALLOWED_IN_MEDIA_BUNDLE: MediaUploadErrorEnum.MediaUploadError
    CANNOT_UPLOAD_MEDIA_TYPE_THROUGH_API: MediaUploadErrorEnum.MediaUploadError
    DIMENSIONS_NOT_ALLOWED: MediaUploadErrorEnum.MediaUploadError

    def __init__(self) -> None:
        ...