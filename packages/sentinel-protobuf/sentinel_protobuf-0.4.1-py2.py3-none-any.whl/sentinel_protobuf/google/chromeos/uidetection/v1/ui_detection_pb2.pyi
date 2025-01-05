from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UiDetectionRequest(_message.Message):
    __slots__ = ("image_png", "request", "resize_image", "test_id", "test_metadata", "force_image_resizing", "return_transformed_image")
    IMAGE_PNG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESIZE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_IMAGE_RESIZING_FIELD_NUMBER: _ClassVar[int]
    RETURN_TRANSFORMED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    image_png: bytes
    request: DetectionRequest
    resize_image: bool
    test_id: str
    test_metadata: TestMetadata
    force_image_resizing: bool
    return_transformed_image: bool
    def __init__(self, image_png: _Optional[bytes] = ..., request: _Optional[_Union[DetectionRequest, _Mapping]] = ..., resize_image: bool = ..., test_id: _Optional[str] = ..., test_metadata: _Optional[_Union[TestMetadata, _Mapping]] = ..., force_image_resizing: bool = ..., return_transformed_image: bool = ...) -> None: ...

class DetectionRequest(_message.Message):
    __slots__ = ("word_detection_request", "text_block_detection_request", "custom_icon_detection_request")
    WORD_DETECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TEXT_BLOCK_DETECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ICON_DETECTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    word_detection_request: WordDetectionRequest
    text_block_detection_request: TextBlockDetectionRequest
    custom_icon_detection_request: CustomIconDetectionRequest
    def __init__(self, word_detection_request: _Optional[_Union[WordDetectionRequest, _Mapping]] = ..., text_block_detection_request: _Optional[_Union[TextBlockDetectionRequest, _Mapping]] = ..., custom_icon_detection_request: _Optional[_Union[CustomIconDetectionRequest, _Mapping]] = ...) -> None: ...

class TestMetadata(_message.Message):
    __slots__ = ("test_id", "board", "model", "cros_build")
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CROS_BUILD_FIELD_NUMBER: _ClassVar[int]
    test_id: str
    board: str
    model: str
    cros_build: str
    def __init__(self, test_id: _Optional[str] = ..., board: _Optional[str] = ..., model: _Optional[str] = ..., cros_build: _Optional[str] = ...) -> None: ...

class WordDetectionRequest(_message.Message):
    __slots__ = ("word", "regex_mode", "disable_approx_match", "max_edit_distance")
    WORD_FIELD_NUMBER: _ClassVar[int]
    REGEX_MODE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_APPROX_MATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_EDIT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    word: str
    regex_mode: bool
    disable_approx_match: bool
    max_edit_distance: int
    def __init__(self, word: _Optional[str] = ..., regex_mode: bool = ..., disable_approx_match: bool = ..., max_edit_distance: _Optional[int] = ...) -> None: ...

class TextBlockDetectionRequest(_message.Message):
    __slots__ = ("words", "regex_mode", "disable_approx_match", "max_edit_distance", "specified_words_only")
    WORDS_FIELD_NUMBER: _ClassVar[int]
    REGEX_MODE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_APPROX_MATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_EDIT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SPECIFIED_WORDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    words: _containers.RepeatedScalarFieldContainer[str]
    regex_mode: bool
    disable_approx_match: bool
    max_edit_distance: int
    specified_words_only: bool
    def __init__(self, words: _Optional[_Iterable[str]] = ..., regex_mode: bool = ..., disable_approx_match: bool = ..., max_edit_distance: _Optional[int] = ..., specified_words_only: bool = ...) -> None: ...

class CustomIconDetectionRequest(_message.Message):
    __slots__ = ("icon_png", "match_count", "min_confidence_threshold")
    ICON_PNG_FIELD_NUMBER: _ClassVar[int]
    MATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    icon_png: bytes
    match_count: int
    min_confidence_threshold: float
    def __init__(self, icon_png: _Optional[bytes] = ..., match_count: _Optional[int] = ..., min_confidence_threshold: _Optional[float] = ...) -> None: ...

class UiDetectionResponse(_message.Message):
    __slots__ = ("bounding_boxes", "transformed_image_png", "resizing_scale_factor")
    BOUNDING_BOXES_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMED_IMAGE_PNG_FIELD_NUMBER: _ClassVar[int]
    RESIZING_SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    bounding_boxes: _containers.RepeatedCompositeFieldContainer[BoundingBox]
    transformed_image_png: bytes
    resizing_scale_factor: float
    def __init__(self, bounding_boxes: _Optional[_Iterable[_Union[BoundingBox, _Mapping]]] = ..., transformed_image_png: _Optional[bytes] = ..., resizing_scale_factor: _Optional[float] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ("text", "top", "left", "bottom", "right")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    text: str
    top: int
    left: int
    bottom: int
    right: int
    def __init__(self, text: _Optional[str] = ..., top: _Optional[int] = ..., left: _Optional[int] = ..., bottom: _Optional[int] = ..., right: _Optional[int] = ...) -> None: ...
