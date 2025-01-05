from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RawDocument(_message.Message):
    __slots__ = ('content', 'mime_type', 'display_name')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    mime_type: str
    display_name: str

    def __init__(self, content: _Optional[bytes]=..., mime_type: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class GcsDocument(_message.Message):
    __slots__ = ('gcs_uri', 'mime_type')
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    gcs_uri: str
    mime_type: str

    def __init__(self, gcs_uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
        ...

class GcsDocuments(_message.Message):
    __slots__ = ('documents',)
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[GcsDocument]

    def __init__(self, documents: _Optional[_Iterable[_Union[GcsDocument, _Mapping]]]=...) -> None:
        ...

class GcsPrefix(_message.Message):
    __slots__ = ('gcs_uri_prefix',)
    GCS_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_uri_prefix: str

    def __init__(self, gcs_uri_prefix: _Optional[str]=...) -> None:
        ...

class BatchDocumentsInputConfig(_message.Message):
    __slots__ = ('gcs_prefix', 'gcs_documents')
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GCS_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: GcsPrefix
    gcs_documents: GcsDocuments

    def __init__(self, gcs_prefix: _Optional[_Union[GcsPrefix, _Mapping]]=..., gcs_documents: _Optional[_Union[GcsDocuments, _Mapping]]=...) -> None:
        ...

class DocumentOutputConfig(_message.Message):
    __slots__ = ('gcs_output_config',)

    class GcsOutputConfig(_message.Message):
        __slots__ = ('gcs_uri', 'field_mask', 'sharding_config')

        class ShardingConfig(_message.Message):
            __slots__ = ('pages_per_shard', 'pages_overlap')
            PAGES_PER_SHARD_FIELD_NUMBER: _ClassVar[int]
            PAGES_OVERLAP_FIELD_NUMBER: _ClassVar[int]
            pages_per_shard: int
            pages_overlap: int

            def __init__(self, pages_per_shard: _Optional[int]=..., pages_overlap: _Optional[int]=...) -> None:
                ...
        GCS_URI_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        SHARDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        gcs_uri: str
        field_mask: _field_mask_pb2.FieldMask
        sharding_config: DocumentOutputConfig.GcsOutputConfig.ShardingConfig

        def __init__(self, gcs_uri: _Optional[str]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., sharding_config: _Optional[_Union[DocumentOutputConfig.GcsOutputConfig.ShardingConfig, _Mapping]]=...) -> None:
            ...
    GCS_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gcs_output_config: DocumentOutputConfig.GcsOutputConfig

    def __init__(self, gcs_output_config: _Optional[_Union[DocumentOutputConfig.GcsOutputConfig, _Mapping]]=...) -> None:
        ...

class OcrConfig(_message.Message):
    __slots__ = ('hints', 'enable_native_pdf_parsing', 'enable_image_quality_scores', 'advanced_ocr_options', 'enable_symbol', 'compute_style_info', 'disable_character_boxes_detection', 'premium_features')

    class Hints(_message.Message):
        __slots__ = ('language_hints',)
        LANGUAGE_HINTS_FIELD_NUMBER: _ClassVar[int]
        language_hints: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, language_hints: _Optional[_Iterable[str]]=...) -> None:
            ...

    class PremiumFeatures(_message.Message):
        __slots__ = ('enable_selection_mark_detection', 'compute_style_info', 'enable_math_ocr')
        ENABLE_SELECTION_MARK_DETECTION_FIELD_NUMBER: _ClassVar[int]
        COMPUTE_STYLE_INFO_FIELD_NUMBER: _ClassVar[int]
        ENABLE_MATH_OCR_FIELD_NUMBER: _ClassVar[int]
        enable_selection_mark_detection: bool
        compute_style_info: bool
        enable_math_ocr: bool

        def __init__(self, enable_selection_mark_detection: bool=..., compute_style_info: bool=..., enable_math_ocr: bool=...) -> None:
            ...
    HINTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NATIVE_PDF_PARSING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IMAGE_QUALITY_SCORES_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_OCR_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_STYLE_INFO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CHARACTER_BOXES_DETECTION_FIELD_NUMBER: _ClassVar[int]
    PREMIUM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    hints: OcrConfig.Hints
    enable_native_pdf_parsing: bool
    enable_image_quality_scores: bool
    advanced_ocr_options: _containers.RepeatedScalarFieldContainer[str]
    enable_symbol: bool
    compute_style_info: bool
    disable_character_boxes_detection: bool
    premium_features: OcrConfig.PremiumFeatures

    def __init__(self, hints: _Optional[_Union[OcrConfig.Hints, _Mapping]]=..., enable_native_pdf_parsing: bool=..., enable_image_quality_scores: bool=..., advanced_ocr_options: _Optional[_Iterable[str]]=..., enable_symbol: bool=..., compute_style_info: bool=..., disable_character_boxes_detection: bool=..., premium_features: _Optional[_Union[OcrConfig.PremiumFeatures, _Mapping]]=...) -> None:
        ...