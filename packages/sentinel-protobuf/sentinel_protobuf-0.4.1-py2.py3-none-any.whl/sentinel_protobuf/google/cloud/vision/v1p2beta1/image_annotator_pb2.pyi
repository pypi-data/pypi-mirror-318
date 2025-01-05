from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.vision.v1p2beta1 import geometry_pb2 as _geometry_pb2
from google.cloud.vision.v1p2beta1 import text_annotation_pb2 as _text_annotation_pb2
from google.cloud.vision.v1p2beta1 import web_detection_pb2 as _web_detection_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import color_pb2 as _color_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Likelihood(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[Likelihood]
    VERY_UNLIKELY: _ClassVar[Likelihood]
    UNLIKELY: _ClassVar[Likelihood]
    POSSIBLE: _ClassVar[Likelihood]
    LIKELY: _ClassVar[Likelihood]
    VERY_LIKELY: _ClassVar[Likelihood]
UNKNOWN: Likelihood
VERY_UNLIKELY: Likelihood
UNLIKELY: Likelihood
POSSIBLE: Likelihood
LIKELY: Likelihood
VERY_LIKELY: Likelihood

class Feature(_message.Message):
    __slots__ = ('type', 'max_results', 'model')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Feature.Type]
        FACE_DETECTION: _ClassVar[Feature.Type]
        LANDMARK_DETECTION: _ClassVar[Feature.Type]
        LOGO_DETECTION: _ClassVar[Feature.Type]
        LABEL_DETECTION: _ClassVar[Feature.Type]
        TEXT_DETECTION: _ClassVar[Feature.Type]
        DOCUMENT_TEXT_DETECTION: _ClassVar[Feature.Type]
        SAFE_SEARCH_DETECTION: _ClassVar[Feature.Type]
        IMAGE_PROPERTIES: _ClassVar[Feature.Type]
        CROP_HINTS: _ClassVar[Feature.Type]
        WEB_DETECTION: _ClassVar[Feature.Type]
    TYPE_UNSPECIFIED: Feature.Type
    FACE_DETECTION: Feature.Type
    LANDMARK_DETECTION: Feature.Type
    LOGO_DETECTION: Feature.Type
    LABEL_DETECTION: Feature.Type
    TEXT_DETECTION: Feature.Type
    DOCUMENT_TEXT_DETECTION: Feature.Type
    SAFE_SEARCH_DETECTION: Feature.Type
    IMAGE_PROPERTIES: Feature.Type
    CROP_HINTS: Feature.Type
    WEB_DETECTION: Feature.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    type: Feature.Type
    max_results: int
    model: str

    def __init__(self, type: _Optional[_Union[Feature.Type, str]]=..., max_results: _Optional[int]=..., model: _Optional[str]=...) -> None:
        ...

class ImageSource(_message.Message):
    __slots__ = ('gcs_image_uri', 'image_uri')
    GCS_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_image_uri: str
    image_uri: str

    def __init__(self, gcs_image_uri: _Optional[str]=..., image_uri: _Optional[str]=...) -> None:
        ...

class Image(_message.Message):
    __slots__ = ('content', 'source')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    source: ImageSource

    def __init__(self, content: _Optional[bytes]=..., source: _Optional[_Union[ImageSource, _Mapping]]=...) -> None:
        ...

class FaceAnnotation(_message.Message):
    __slots__ = ('bounding_poly', 'fd_bounding_poly', 'landmarks', 'roll_angle', 'pan_angle', 'tilt_angle', 'detection_confidence', 'landmarking_confidence', 'joy_likelihood', 'sorrow_likelihood', 'anger_likelihood', 'surprise_likelihood', 'under_exposed_likelihood', 'blurred_likelihood', 'headwear_likelihood')

    class Landmark(_message.Message):
        __slots__ = ('type', 'position')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_LANDMARK: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_OF_LEFT_EYEBROW: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_OF_LEFT_EYEBROW: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_OF_RIGHT_EYEBROW: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_OF_RIGHT_EYEBROW: _ClassVar[FaceAnnotation.Landmark.Type]
            MIDPOINT_BETWEEN_EYES: _ClassVar[FaceAnnotation.Landmark.Type]
            NOSE_TIP: _ClassVar[FaceAnnotation.Landmark.Type]
            UPPER_LIP: _ClassVar[FaceAnnotation.Landmark.Type]
            LOWER_LIP: _ClassVar[FaceAnnotation.Landmark.Type]
            MOUTH_LEFT: _ClassVar[FaceAnnotation.Landmark.Type]
            MOUTH_RIGHT: _ClassVar[FaceAnnotation.Landmark.Type]
            MOUTH_CENTER: _ClassVar[FaceAnnotation.Landmark.Type]
            NOSE_BOTTOM_RIGHT: _ClassVar[FaceAnnotation.Landmark.Type]
            NOSE_BOTTOM_LEFT: _ClassVar[FaceAnnotation.Landmark.Type]
            NOSE_BOTTOM_CENTER: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE_TOP_BOUNDARY: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE_RIGHT_CORNER: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE_BOTTOM_BOUNDARY: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE_LEFT_CORNER: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE_TOP_BOUNDARY: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE_RIGHT_CORNER: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE_BOTTOM_BOUNDARY: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE_LEFT_CORNER: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYEBROW_UPPER_MIDPOINT: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYEBROW_UPPER_MIDPOINT: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EAR_TRAGION: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EAR_TRAGION: _ClassVar[FaceAnnotation.Landmark.Type]
            LEFT_EYE_PUPIL: _ClassVar[FaceAnnotation.Landmark.Type]
            RIGHT_EYE_PUPIL: _ClassVar[FaceAnnotation.Landmark.Type]
            FOREHEAD_GLABELLA: _ClassVar[FaceAnnotation.Landmark.Type]
            CHIN_GNATHION: _ClassVar[FaceAnnotation.Landmark.Type]
            CHIN_LEFT_GONION: _ClassVar[FaceAnnotation.Landmark.Type]
            CHIN_RIGHT_GONION: _ClassVar[FaceAnnotation.Landmark.Type]
        UNKNOWN_LANDMARK: FaceAnnotation.Landmark.Type
        LEFT_EYE: FaceAnnotation.Landmark.Type
        RIGHT_EYE: FaceAnnotation.Landmark.Type
        LEFT_OF_LEFT_EYEBROW: FaceAnnotation.Landmark.Type
        RIGHT_OF_LEFT_EYEBROW: FaceAnnotation.Landmark.Type
        LEFT_OF_RIGHT_EYEBROW: FaceAnnotation.Landmark.Type
        RIGHT_OF_RIGHT_EYEBROW: FaceAnnotation.Landmark.Type
        MIDPOINT_BETWEEN_EYES: FaceAnnotation.Landmark.Type
        NOSE_TIP: FaceAnnotation.Landmark.Type
        UPPER_LIP: FaceAnnotation.Landmark.Type
        LOWER_LIP: FaceAnnotation.Landmark.Type
        MOUTH_LEFT: FaceAnnotation.Landmark.Type
        MOUTH_RIGHT: FaceAnnotation.Landmark.Type
        MOUTH_CENTER: FaceAnnotation.Landmark.Type
        NOSE_BOTTOM_RIGHT: FaceAnnotation.Landmark.Type
        NOSE_BOTTOM_LEFT: FaceAnnotation.Landmark.Type
        NOSE_BOTTOM_CENTER: FaceAnnotation.Landmark.Type
        LEFT_EYE_TOP_BOUNDARY: FaceAnnotation.Landmark.Type
        LEFT_EYE_RIGHT_CORNER: FaceAnnotation.Landmark.Type
        LEFT_EYE_BOTTOM_BOUNDARY: FaceAnnotation.Landmark.Type
        LEFT_EYE_LEFT_CORNER: FaceAnnotation.Landmark.Type
        RIGHT_EYE_TOP_BOUNDARY: FaceAnnotation.Landmark.Type
        RIGHT_EYE_RIGHT_CORNER: FaceAnnotation.Landmark.Type
        RIGHT_EYE_BOTTOM_BOUNDARY: FaceAnnotation.Landmark.Type
        RIGHT_EYE_LEFT_CORNER: FaceAnnotation.Landmark.Type
        LEFT_EYEBROW_UPPER_MIDPOINT: FaceAnnotation.Landmark.Type
        RIGHT_EYEBROW_UPPER_MIDPOINT: FaceAnnotation.Landmark.Type
        LEFT_EAR_TRAGION: FaceAnnotation.Landmark.Type
        RIGHT_EAR_TRAGION: FaceAnnotation.Landmark.Type
        LEFT_EYE_PUPIL: FaceAnnotation.Landmark.Type
        RIGHT_EYE_PUPIL: FaceAnnotation.Landmark.Type
        FOREHEAD_GLABELLA: FaceAnnotation.Landmark.Type
        CHIN_GNATHION: FaceAnnotation.Landmark.Type
        CHIN_LEFT_GONION: FaceAnnotation.Landmark.Type
        CHIN_RIGHT_GONION: FaceAnnotation.Landmark.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        type: FaceAnnotation.Landmark.Type
        position: _geometry_pb2.Position

        def __init__(self, type: _Optional[_Union[FaceAnnotation.Landmark.Type, str]]=..., position: _Optional[_Union[_geometry_pb2.Position, _Mapping]]=...) -> None:
            ...
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    FD_BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    LANDMARKS_FIELD_NUMBER: _ClassVar[int]
    ROLL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    PAN_ANGLE_FIELD_NUMBER: _ClassVar[int]
    TILT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LANDMARKING_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    JOY_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    SORROW_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    ANGER_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    SURPRISE_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    UNDER_EXPOSED_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    BLURRED_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    HEADWEAR_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    bounding_poly: _geometry_pb2.BoundingPoly
    fd_bounding_poly: _geometry_pb2.BoundingPoly
    landmarks: _containers.RepeatedCompositeFieldContainer[FaceAnnotation.Landmark]
    roll_angle: float
    pan_angle: float
    tilt_angle: float
    detection_confidence: float
    landmarking_confidence: float
    joy_likelihood: Likelihood
    sorrow_likelihood: Likelihood
    anger_likelihood: Likelihood
    surprise_likelihood: Likelihood
    under_exposed_likelihood: Likelihood
    blurred_likelihood: Likelihood
    headwear_likelihood: Likelihood

    def __init__(self, bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., fd_bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., landmarks: _Optional[_Iterable[_Union[FaceAnnotation.Landmark, _Mapping]]]=..., roll_angle: _Optional[float]=..., pan_angle: _Optional[float]=..., tilt_angle: _Optional[float]=..., detection_confidence: _Optional[float]=..., landmarking_confidence: _Optional[float]=..., joy_likelihood: _Optional[_Union[Likelihood, str]]=..., sorrow_likelihood: _Optional[_Union[Likelihood, str]]=..., anger_likelihood: _Optional[_Union[Likelihood, str]]=..., surprise_likelihood: _Optional[_Union[Likelihood, str]]=..., under_exposed_likelihood: _Optional[_Union[Likelihood, str]]=..., blurred_likelihood: _Optional[_Union[Likelihood, str]]=..., headwear_likelihood: _Optional[_Union[Likelihood, str]]=...) -> None:
        ...

class LocationInfo(_message.Message):
    __slots__ = ('lat_lng',)
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    lat_lng: _latlng_pb2.LatLng

    def __init__(self, lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=...) -> None:
        ...

class Property(_message.Message):
    __slots__ = ('name', 'value', 'uint64_value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    uint64_value: int

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=..., uint64_value: _Optional[int]=...) -> None:
        ...

class EntityAnnotation(_message.Message):
    __slots__ = ('mid', 'locale', 'description', 'score', 'confidence', 'topicality', 'bounding_poly', 'locations', 'properties')
    MID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TOPICALITY_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    mid: str
    locale: str
    description: str
    score: float
    confidence: float
    topicality: float
    bounding_poly: _geometry_pb2.BoundingPoly
    locations: _containers.RepeatedCompositeFieldContainer[LocationInfo]
    properties: _containers.RepeatedCompositeFieldContainer[Property]

    def __init__(self, mid: _Optional[str]=..., locale: _Optional[str]=..., description: _Optional[str]=..., score: _Optional[float]=..., confidence: _Optional[float]=..., topicality: _Optional[float]=..., bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., locations: _Optional[_Iterable[_Union[LocationInfo, _Mapping]]]=..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]]=...) -> None:
        ...

class SafeSearchAnnotation(_message.Message):
    __slots__ = ('adult', 'spoof', 'medical', 'violence', 'racy')
    ADULT_FIELD_NUMBER: _ClassVar[int]
    SPOOF_FIELD_NUMBER: _ClassVar[int]
    MEDICAL_FIELD_NUMBER: _ClassVar[int]
    VIOLENCE_FIELD_NUMBER: _ClassVar[int]
    RACY_FIELD_NUMBER: _ClassVar[int]
    adult: Likelihood
    spoof: Likelihood
    medical: Likelihood
    violence: Likelihood
    racy: Likelihood

    def __init__(self, adult: _Optional[_Union[Likelihood, str]]=..., spoof: _Optional[_Union[Likelihood, str]]=..., medical: _Optional[_Union[Likelihood, str]]=..., violence: _Optional[_Union[Likelihood, str]]=..., racy: _Optional[_Union[Likelihood, str]]=...) -> None:
        ...

class LatLongRect(_message.Message):
    __slots__ = ('min_lat_lng', 'max_lat_lng')
    MIN_LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    MAX_LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    min_lat_lng: _latlng_pb2.LatLng
    max_lat_lng: _latlng_pb2.LatLng

    def __init__(self, min_lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., max_lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=...) -> None:
        ...

class ColorInfo(_message.Message):
    __slots__ = ('color', 'score', 'pixel_fraction')
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PIXEL_FRACTION_FIELD_NUMBER: _ClassVar[int]
    color: _color_pb2.Color
    score: float
    pixel_fraction: float

    def __init__(self, color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., score: _Optional[float]=..., pixel_fraction: _Optional[float]=...) -> None:
        ...

class DominantColorsAnnotation(_message.Message):
    __slots__ = ('colors',)
    COLORS_FIELD_NUMBER: _ClassVar[int]
    colors: _containers.RepeatedCompositeFieldContainer[ColorInfo]

    def __init__(self, colors: _Optional[_Iterable[_Union[ColorInfo, _Mapping]]]=...) -> None:
        ...

class ImageProperties(_message.Message):
    __slots__ = ('dominant_colors',)
    DOMINANT_COLORS_FIELD_NUMBER: _ClassVar[int]
    dominant_colors: DominantColorsAnnotation

    def __init__(self, dominant_colors: _Optional[_Union[DominantColorsAnnotation, _Mapping]]=...) -> None:
        ...

class CropHint(_message.Message):
    __slots__ = ('bounding_poly', 'confidence', 'importance_fraction')
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    bounding_poly: _geometry_pb2.BoundingPoly
    confidence: float
    importance_fraction: float

    def __init__(self, bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., confidence: _Optional[float]=..., importance_fraction: _Optional[float]=...) -> None:
        ...

class CropHintsAnnotation(_message.Message):
    __slots__ = ('crop_hints',)
    CROP_HINTS_FIELD_NUMBER: _ClassVar[int]
    crop_hints: _containers.RepeatedCompositeFieldContainer[CropHint]

    def __init__(self, crop_hints: _Optional[_Iterable[_Union[CropHint, _Mapping]]]=...) -> None:
        ...

class CropHintsParams(_message.Message):
    __slots__ = ('aspect_ratios',)
    ASPECT_RATIOS_FIELD_NUMBER: _ClassVar[int]
    aspect_ratios: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, aspect_ratios: _Optional[_Iterable[float]]=...) -> None:
        ...

class WebDetectionParams(_message.Message):
    __slots__ = ('include_geo_results',)
    INCLUDE_GEO_RESULTS_FIELD_NUMBER: _ClassVar[int]
    include_geo_results: bool

    def __init__(self, include_geo_results: bool=...) -> None:
        ...

class TextDetectionParams(_message.Message):
    __slots__ = ('enable_text_detection_confidence_score', 'advanced_ocr_options')
    ENABLE_TEXT_DETECTION_CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_OCR_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    enable_text_detection_confidence_score: bool
    advanced_ocr_options: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, enable_text_detection_confidence_score: bool=..., advanced_ocr_options: _Optional[_Iterable[str]]=...) -> None:
        ...

class ImageContext(_message.Message):
    __slots__ = ('lat_long_rect', 'language_hints', 'crop_hints_params', 'web_detection_params', 'text_detection_params')
    LAT_LONG_RECT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_HINTS_FIELD_NUMBER: _ClassVar[int]
    CROP_HINTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    WEB_DETECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEXT_DETECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    lat_long_rect: LatLongRect
    language_hints: _containers.RepeatedScalarFieldContainer[str]
    crop_hints_params: CropHintsParams
    web_detection_params: WebDetectionParams
    text_detection_params: TextDetectionParams

    def __init__(self, lat_long_rect: _Optional[_Union[LatLongRect, _Mapping]]=..., language_hints: _Optional[_Iterable[str]]=..., crop_hints_params: _Optional[_Union[CropHintsParams, _Mapping]]=..., web_detection_params: _Optional[_Union[WebDetectionParams, _Mapping]]=..., text_detection_params: _Optional[_Union[TextDetectionParams, _Mapping]]=...) -> None:
        ...

class AnnotateImageRequest(_message.Message):
    __slots__ = ('image', 'features', 'image_context')
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    image: Image
    features: _containers.RepeatedCompositeFieldContainer[Feature]
    image_context: ImageContext

    def __init__(self, image: _Optional[_Union[Image, _Mapping]]=..., features: _Optional[_Iterable[_Union[Feature, _Mapping]]]=..., image_context: _Optional[_Union[ImageContext, _Mapping]]=...) -> None:
        ...

class ImageAnnotationContext(_message.Message):
    __slots__ = ('uri', 'page_number')
    URI_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    uri: str
    page_number: int

    def __init__(self, uri: _Optional[str]=..., page_number: _Optional[int]=...) -> None:
        ...

class AnnotateImageResponse(_message.Message):
    __slots__ = ('face_annotations', 'landmark_annotations', 'logo_annotations', 'label_annotations', 'text_annotations', 'full_text_annotation', 'safe_search_annotation', 'image_properties_annotation', 'crop_hints_annotation', 'web_detection', 'error', 'context')
    FACE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LOGO_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FULL_TEXT_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    SAFE_SEARCH_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PROPERTIES_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    CROP_HINTS_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    WEB_DETECTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    face_annotations: _containers.RepeatedCompositeFieldContainer[FaceAnnotation]
    landmark_annotations: _containers.RepeatedCompositeFieldContainer[EntityAnnotation]
    logo_annotations: _containers.RepeatedCompositeFieldContainer[EntityAnnotation]
    label_annotations: _containers.RepeatedCompositeFieldContainer[EntityAnnotation]
    text_annotations: _containers.RepeatedCompositeFieldContainer[EntityAnnotation]
    full_text_annotation: _text_annotation_pb2.TextAnnotation
    safe_search_annotation: SafeSearchAnnotation
    image_properties_annotation: ImageProperties
    crop_hints_annotation: CropHintsAnnotation
    web_detection: _web_detection_pb2.WebDetection
    error: _status_pb2.Status
    context: ImageAnnotationContext

    def __init__(self, face_annotations: _Optional[_Iterable[_Union[FaceAnnotation, _Mapping]]]=..., landmark_annotations: _Optional[_Iterable[_Union[EntityAnnotation, _Mapping]]]=..., logo_annotations: _Optional[_Iterable[_Union[EntityAnnotation, _Mapping]]]=..., label_annotations: _Optional[_Iterable[_Union[EntityAnnotation, _Mapping]]]=..., text_annotations: _Optional[_Iterable[_Union[EntityAnnotation, _Mapping]]]=..., full_text_annotation: _Optional[_Union[_text_annotation_pb2.TextAnnotation, _Mapping]]=..., safe_search_annotation: _Optional[_Union[SafeSearchAnnotation, _Mapping]]=..., image_properties_annotation: _Optional[_Union[ImageProperties, _Mapping]]=..., crop_hints_annotation: _Optional[_Union[CropHintsAnnotation, _Mapping]]=..., web_detection: _Optional[_Union[_web_detection_pb2.WebDetection, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., context: _Optional[_Union[ImageAnnotationContext, _Mapping]]=...) -> None:
        ...

class AnnotateFileResponse(_message.Message):
    __slots__ = ('input_config', 'responses')
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    input_config: InputConfig
    responses: _containers.RepeatedCompositeFieldContainer[AnnotateImageResponse]

    def __init__(self, input_config: _Optional[_Union[InputConfig, _Mapping]]=..., responses: _Optional[_Iterable[_Union[AnnotateImageResponse, _Mapping]]]=...) -> None:
        ...

class BatchAnnotateImagesRequest(_message.Message):
    __slots__ = ('requests',)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[AnnotateImageRequest]

    def __init__(self, requests: _Optional[_Iterable[_Union[AnnotateImageRequest, _Mapping]]]=...) -> None:
        ...

class BatchAnnotateImagesResponse(_message.Message):
    __slots__ = ('responses',)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[AnnotateImageResponse]

    def __init__(self, responses: _Optional[_Iterable[_Union[AnnotateImageResponse, _Mapping]]]=...) -> None:
        ...

class AsyncAnnotateFileRequest(_message.Message):
    __slots__ = ('input_config', 'features', 'image_context', 'output_config')
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    input_config: InputConfig
    features: _containers.RepeatedCompositeFieldContainer[Feature]
    image_context: ImageContext
    output_config: OutputConfig

    def __init__(self, input_config: _Optional[_Union[InputConfig, _Mapping]]=..., features: _Optional[_Iterable[_Union[Feature, _Mapping]]]=..., image_context: _Optional[_Union[ImageContext, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class AsyncAnnotateFileResponse(_message.Message):
    __slots__ = ('output_config',)
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    output_config: OutputConfig

    def __init__(self, output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class AsyncBatchAnnotateFilesRequest(_message.Message):
    __slots__ = ('requests',)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[AsyncAnnotateFileRequest]

    def __init__(self, requests: _Optional[_Iterable[_Union[AsyncAnnotateFileRequest, _Mapping]]]=...) -> None:
        ...

class AsyncBatchAnnotateFilesResponse(_message.Message):
    __slots__ = ('responses',)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[AsyncAnnotateFileResponse]

    def __init__(self, responses: _Optional[_Iterable[_Union[AsyncAnnotateFileResponse, _Mapping]]]=...) -> None:
        ...

class InputConfig(_message.Message):
    __slots__ = ('gcs_source', 'mime_type')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    mime_type: str

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., mime_type: _Optional[str]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'batch_size')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    batch_size: int

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., batch_size: _Optional[int]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OperationMetadata.State]
        CREATED: _ClassVar[OperationMetadata.State]
        RUNNING: _ClassVar[OperationMetadata.State]
        DONE: _ClassVar[OperationMetadata.State]
        CANCELLED: _ClassVar[OperationMetadata.State]
    STATE_UNSPECIFIED: OperationMetadata.State
    CREATED: OperationMetadata.State
    RUNNING: OperationMetadata.State
    DONE: OperationMetadata.State
    CANCELLED: OperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    state: OperationMetadata.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[OperationMetadata.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...