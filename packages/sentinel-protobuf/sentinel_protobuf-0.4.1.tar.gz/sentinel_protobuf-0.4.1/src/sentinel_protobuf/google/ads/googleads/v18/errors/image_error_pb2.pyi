from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ImageErrorEnum(_message.Message):
    __slots__ = ()

    class ImageError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ImageErrorEnum.ImageError]
        UNKNOWN: _ClassVar[ImageErrorEnum.ImageError]
        INVALID_IMAGE: _ClassVar[ImageErrorEnum.ImageError]
        STORAGE_ERROR: _ClassVar[ImageErrorEnum.ImageError]
        BAD_REQUEST: _ClassVar[ImageErrorEnum.ImageError]
        UNEXPECTED_SIZE: _ClassVar[ImageErrorEnum.ImageError]
        ANIMATED_NOT_ALLOWED: _ClassVar[ImageErrorEnum.ImageError]
        ANIMATION_TOO_LONG: _ClassVar[ImageErrorEnum.ImageError]
        SERVER_ERROR: _ClassVar[ImageErrorEnum.ImageError]
        CMYK_JPEG_NOT_ALLOWED: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_NOT_ALLOWED: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_WITHOUT_CLICKTAG: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_ERROR_AFTER_FIXING_CLICK_TAG: _ClassVar[ImageErrorEnum.ImageError]
        ANIMATED_VISUAL_EFFECT: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_ERROR: _ClassVar[ImageErrorEnum.ImageError]
        LAYOUT_PROBLEM: _ClassVar[ImageErrorEnum.ImageError]
        PROBLEM_READING_IMAGE_FILE: _ClassVar[ImageErrorEnum.ImageError]
        ERROR_STORING_IMAGE: _ClassVar[ImageErrorEnum.ImageError]
        ASPECT_RATIO_NOT_ALLOWED: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_HAS_NETWORK_OBJECTS: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_HAS_NETWORK_METHODS: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_HAS_URL: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_HAS_MOUSE_TRACKING: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_HAS_RANDOM_NUM: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_SELF_TARGETS: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_BAD_GETURL_TARGET: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_VERSION_NOT_SUPPORTED: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_WITHOUT_HARD_CODED_CLICK_URL: _ClassVar[ImageErrorEnum.ImageError]
        INVALID_FLASH_FILE: _ClassVar[ImageErrorEnum.ImageError]
        FAILED_TO_FIX_CLICK_TAG_IN_FLASH: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_ACCESSES_NETWORK_RESOURCES: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_EXTERNAL_JS_CALL: _ClassVar[ImageErrorEnum.ImageError]
        FLASH_EXTERNAL_FS_CALL: _ClassVar[ImageErrorEnum.ImageError]
        FILE_TOO_LARGE: _ClassVar[ImageErrorEnum.ImageError]
        IMAGE_DATA_TOO_LARGE: _ClassVar[ImageErrorEnum.ImageError]
        IMAGE_PROCESSING_ERROR: _ClassVar[ImageErrorEnum.ImageError]
        IMAGE_TOO_SMALL: _ClassVar[ImageErrorEnum.ImageError]
        INVALID_INPUT: _ClassVar[ImageErrorEnum.ImageError]
        PROBLEM_READING_FILE: _ClassVar[ImageErrorEnum.ImageError]
        IMAGE_CONSTRAINTS_VIOLATED: _ClassVar[ImageErrorEnum.ImageError]
        FORMAT_NOT_ALLOWED: _ClassVar[ImageErrorEnum.ImageError]
    UNSPECIFIED: ImageErrorEnum.ImageError
    UNKNOWN: ImageErrorEnum.ImageError
    INVALID_IMAGE: ImageErrorEnum.ImageError
    STORAGE_ERROR: ImageErrorEnum.ImageError
    BAD_REQUEST: ImageErrorEnum.ImageError
    UNEXPECTED_SIZE: ImageErrorEnum.ImageError
    ANIMATED_NOT_ALLOWED: ImageErrorEnum.ImageError
    ANIMATION_TOO_LONG: ImageErrorEnum.ImageError
    SERVER_ERROR: ImageErrorEnum.ImageError
    CMYK_JPEG_NOT_ALLOWED: ImageErrorEnum.ImageError
    FLASH_NOT_ALLOWED: ImageErrorEnum.ImageError
    FLASH_WITHOUT_CLICKTAG: ImageErrorEnum.ImageError
    FLASH_ERROR_AFTER_FIXING_CLICK_TAG: ImageErrorEnum.ImageError
    ANIMATED_VISUAL_EFFECT: ImageErrorEnum.ImageError
    FLASH_ERROR: ImageErrorEnum.ImageError
    LAYOUT_PROBLEM: ImageErrorEnum.ImageError
    PROBLEM_READING_IMAGE_FILE: ImageErrorEnum.ImageError
    ERROR_STORING_IMAGE: ImageErrorEnum.ImageError
    ASPECT_RATIO_NOT_ALLOWED: ImageErrorEnum.ImageError
    FLASH_HAS_NETWORK_OBJECTS: ImageErrorEnum.ImageError
    FLASH_HAS_NETWORK_METHODS: ImageErrorEnum.ImageError
    FLASH_HAS_URL: ImageErrorEnum.ImageError
    FLASH_HAS_MOUSE_TRACKING: ImageErrorEnum.ImageError
    FLASH_HAS_RANDOM_NUM: ImageErrorEnum.ImageError
    FLASH_SELF_TARGETS: ImageErrorEnum.ImageError
    FLASH_BAD_GETURL_TARGET: ImageErrorEnum.ImageError
    FLASH_VERSION_NOT_SUPPORTED: ImageErrorEnum.ImageError
    FLASH_WITHOUT_HARD_CODED_CLICK_URL: ImageErrorEnum.ImageError
    INVALID_FLASH_FILE: ImageErrorEnum.ImageError
    FAILED_TO_FIX_CLICK_TAG_IN_FLASH: ImageErrorEnum.ImageError
    FLASH_ACCESSES_NETWORK_RESOURCES: ImageErrorEnum.ImageError
    FLASH_EXTERNAL_JS_CALL: ImageErrorEnum.ImageError
    FLASH_EXTERNAL_FS_CALL: ImageErrorEnum.ImageError
    FILE_TOO_LARGE: ImageErrorEnum.ImageError
    IMAGE_DATA_TOO_LARGE: ImageErrorEnum.ImageError
    IMAGE_PROCESSING_ERROR: ImageErrorEnum.ImageError
    IMAGE_TOO_SMALL: ImageErrorEnum.ImageError
    INVALID_INPUT: ImageErrorEnum.ImageError
    PROBLEM_READING_FILE: ImageErrorEnum.ImageError
    IMAGE_CONSTRAINTS_VIOLATED: ImageErrorEnum.ImageError
    FORMAT_NOT_ALLOWED: ImageErrorEnum.ImageError

    def __init__(self) -> None:
        ...