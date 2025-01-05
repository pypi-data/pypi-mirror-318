from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslateTextGlossaryConfig(_message.Message):
    __slots__ = ('glossary', 'ignore_case')
    GLOSSARY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
    glossary: str
    ignore_case: bool

    def __init__(self, glossary: _Optional[str]=..., ignore_case: bool=...) -> None:
        ...

class TranslateTextRequest(_message.Message):
    __slots__ = ('contents', 'mime_type', 'source_language_code', 'target_language_code', 'parent', 'model', 'glossary_config', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedScalarFieldContainer[str]
    mime_type: str
    source_language_code: str
    target_language_code: str
    parent: str
    model: str
    glossary_config: TranslateTextGlossaryConfig
    labels: _containers.ScalarMap[str, str]

    def __init__(self, contents: _Optional[_Iterable[str]]=..., mime_type: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=..., parent: _Optional[str]=..., model: _Optional[str]=..., glossary_config: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TranslateTextResponse(_message.Message):
    __slots__ = ('translations', 'glossary_translations')
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    translations: _containers.RepeatedCompositeFieldContainer[Translation]
    glossary_translations: _containers.RepeatedCompositeFieldContainer[Translation]

    def __init__(self, translations: _Optional[_Iterable[_Union[Translation, _Mapping]]]=..., glossary_translations: _Optional[_Iterable[_Union[Translation, _Mapping]]]=...) -> None:
        ...

class Translation(_message.Message):
    __slots__ = ('translated_text', 'model', 'detected_language_code', 'glossary_config')
    TRANSLATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DETECTED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    translated_text: str
    model: str
    detected_language_code: str
    glossary_config: TranslateTextGlossaryConfig

    def __init__(self, translated_text: _Optional[str]=..., model: _Optional[str]=..., detected_language_code: _Optional[str]=..., glossary_config: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=...) -> None:
        ...

class DetectLanguageRequest(_message.Message):
    __slots__ = ('parent', 'model', 'content', 'mime_type', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model: str
    content: str
    mime_type: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, parent: _Optional[str]=..., model: _Optional[str]=..., content: _Optional[str]=..., mime_type: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class DetectedLanguage(_message.Message):
    __slots__ = ('language_code', 'confidence')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    confidence: float

    def __init__(self, language_code: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class DetectLanguageResponse(_message.Message):
    __slots__ = ('languages',)
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[DetectedLanguage]

    def __init__(self, languages: _Optional[_Iterable[_Union[DetectedLanguage, _Mapping]]]=...) -> None:
        ...

class GetSupportedLanguagesRequest(_message.Message):
    __slots__ = ('parent', 'display_language_code', 'model')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_language_code: str
    model: str

    def __init__(self, parent: _Optional[str]=..., display_language_code: _Optional[str]=..., model: _Optional[str]=...) -> None:
        ...

class SupportedLanguages(_message.Message):
    __slots__ = ('languages',)
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[SupportedLanguage]

    def __init__(self, languages: _Optional[_Iterable[_Union[SupportedLanguage, _Mapping]]]=...) -> None:
        ...

class SupportedLanguage(_message.Message):
    __slots__ = ('language_code', 'display_name', 'support_source', 'support_target')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_TARGET_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    display_name: str
    support_source: bool
    support_target: bool

    def __init__(self, language_code: _Optional[str]=..., display_name: _Optional[str]=..., support_source: bool=..., support_target: bool=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('input_uri',)
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    input_uri: str

    def __init__(self, input_uri: _Optional[str]=...) -> None:
        ...

class InputConfig(_message.Message):
    __slots__ = ('mime_type', 'gcs_source')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    gcs_source: GcsSource

    def __init__(self, mime_type: _Optional[str]=..., gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('output_uri_prefix',)
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    output_uri_prefix: str

    def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=...) -> None:
        ...

class DocumentInputConfig(_message.Message):
    __slots__ = ('content', 'gcs_source', 'mime_type')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    gcs_source: GcsSource
    mime_type: str

    def __init__(self, content: _Optional[bytes]=..., gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., mime_type: _Optional[str]=...) -> None:
        ...

class DocumentOutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'mime_type')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    mime_type: str

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., mime_type: _Optional[str]=...) -> None:
        ...

class TranslateDocumentRequest(_message.Message):
    __slots__ = ('parent', 'source_language_code', 'target_language_code', 'document_input_config', 'document_output_config', 'model', 'glossary_config', 'labels', 'customized_attribution', 'is_translate_native_pdf_only', 'enable_shadow_removal_native_pdf', 'enable_rotation_correction')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSLATE_NATIVE_PDF_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SHADOW_REMOVAL_NATIVE_PDF_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ROTATION_CORRECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_language_code: str
    target_language_code: str
    document_input_config: DocumentInputConfig
    document_output_config: DocumentOutputConfig
    model: str
    glossary_config: TranslateTextGlossaryConfig
    labels: _containers.ScalarMap[str, str]
    customized_attribution: str
    is_translate_native_pdf_only: bool
    enable_shadow_removal_native_pdf: bool
    enable_rotation_correction: bool

    def __init__(self, parent: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=..., document_input_config: _Optional[_Union[DocumentInputConfig, _Mapping]]=..., document_output_config: _Optional[_Union[DocumentOutputConfig, _Mapping]]=..., model: _Optional[str]=..., glossary_config: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., customized_attribution: _Optional[str]=..., is_translate_native_pdf_only: bool=..., enable_shadow_removal_native_pdf: bool=..., enable_rotation_correction: bool=...) -> None:
        ...

class DocumentTranslation(_message.Message):
    __slots__ = ('byte_stream_outputs', 'mime_type', 'detected_language_code')
    BYTE_STREAM_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETECTED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    byte_stream_outputs: _containers.RepeatedScalarFieldContainer[bytes]
    mime_type: str
    detected_language_code: str

    def __init__(self, byte_stream_outputs: _Optional[_Iterable[bytes]]=..., mime_type: _Optional[str]=..., detected_language_code: _Optional[str]=...) -> None:
        ...

class TranslateDocumentResponse(_message.Message):
    __slots__ = ('document_translation', 'glossary_document_translation', 'model', 'glossary_config')
    DOCUMENT_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_DOCUMENT_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    document_translation: DocumentTranslation
    glossary_document_translation: DocumentTranslation
    model: str
    glossary_config: TranslateTextGlossaryConfig

    def __init__(self, document_translation: _Optional[_Union[DocumentTranslation, _Mapping]]=..., glossary_document_translation: _Optional[_Union[DocumentTranslation, _Mapping]]=..., model: _Optional[str]=..., glossary_config: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=...) -> None:
        ...

class BatchTranslateTextRequest(_message.Message):
    __slots__ = ('parent', 'source_language_code', 'target_language_codes', 'models', 'input_configs', 'output_config', 'glossaries', 'labels')

    class ModelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class GlossariesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TranslateTextGlossaryConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOSSARIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_language_code: str
    target_language_codes: _containers.RepeatedScalarFieldContainer[str]
    models: _containers.ScalarMap[str, str]
    input_configs: _containers.RepeatedCompositeFieldContainer[InputConfig]
    output_config: OutputConfig
    glossaries: _containers.MessageMap[str, TranslateTextGlossaryConfig]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, parent: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_codes: _Optional[_Iterable[str]]=..., models: _Optional[_Mapping[str, str]]=..., input_configs: _Optional[_Iterable[_Union[InputConfig, _Mapping]]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., glossaries: _Optional[_Mapping[str, TranslateTextGlossaryConfig]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BatchTranslateMetadata(_message.Message):
    __slots__ = ('state', 'translated_characters', 'failed_characters', 'total_characters', 'submit_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchTranslateMetadata.State]
        RUNNING: _ClassVar[BatchTranslateMetadata.State]
        SUCCEEDED: _ClassVar[BatchTranslateMetadata.State]
        FAILED: _ClassVar[BatchTranslateMetadata.State]
        CANCELLING: _ClassVar[BatchTranslateMetadata.State]
        CANCELLED: _ClassVar[BatchTranslateMetadata.State]
    STATE_UNSPECIFIED: BatchTranslateMetadata.State
    RUNNING: BatchTranslateMetadata.State
    SUCCEEDED: BatchTranslateMetadata.State
    FAILED: BatchTranslateMetadata.State
    CANCELLING: BatchTranslateMetadata.State
    CANCELLED: BatchTranslateMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    state: BatchTranslateMetadata.State
    translated_characters: int
    failed_characters: int
    total_characters: int
    submit_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[BatchTranslateMetadata.State, str]]=..., translated_characters: _Optional[int]=..., failed_characters: _Optional[int]=..., total_characters: _Optional[int]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchTranslateResponse(_message.Message):
    __slots__ = ('total_characters', 'translated_characters', 'failed_characters', 'submit_time', 'end_time')
    TOTAL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    total_characters: int
    translated_characters: int
    failed_characters: int
    submit_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, total_characters: _Optional[int]=..., translated_characters: _Optional[int]=..., failed_characters: _Optional[int]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GlossaryInputConfig(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class Glossary(_message.Message):
    __slots__ = ('name', 'language_pair', 'language_codes_set', 'input_config', 'entry_count', 'submit_time', 'end_time')

    class LanguageCodePair(_message.Message):
        __slots__ = ('source_language_code', 'target_language_code')
        SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        source_language_code: str
        target_language_code: str

        def __init__(self, source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=...) -> None:
            ...

    class LanguageCodesSet(_message.Message):
        __slots__ = ('language_codes',)
        LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
        language_codes: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, language_codes: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_PAIR_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_SET_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_pair: Glossary.LanguageCodePair
    language_codes_set: Glossary.LanguageCodesSet
    input_config: GlossaryInputConfig
    entry_count: int
    submit_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., language_pair: _Optional[_Union[Glossary.LanguageCodePair, _Mapping]]=..., language_codes_set: _Optional[_Union[Glossary.LanguageCodesSet, _Mapping]]=..., input_config: _Optional[_Union[GlossaryInputConfig, _Mapping]]=..., entry_count: _Optional[int]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateGlossaryRequest(_message.Message):
    __slots__ = ('parent', 'glossary')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    glossary: Glossary

    def __init__(self, parent: _Optional[str]=..., glossary: _Optional[_Union[Glossary, _Mapping]]=...) -> None:
        ...

class GetGlossaryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteGlossaryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGlossariesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListGlossariesResponse(_message.Message):
    __slots__ = ('glossaries', 'next_page_token')
    GLOSSARIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    glossaries: _containers.RepeatedCompositeFieldContainer[Glossary]
    next_page_token: str

    def __init__(self, glossaries: _Optional[_Iterable[_Union[Glossary, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateGlossaryMetadata(_message.Message):
    __slots__ = ('name', 'state', 'submit_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CreateGlossaryMetadata.State]
        RUNNING: _ClassVar[CreateGlossaryMetadata.State]
        SUCCEEDED: _ClassVar[CreateGlossaryMetadata.State]
        FAILED: _ClassVar[CreateGlossaryMetadata.State]
        CANCELLING: _ClassVar[CreateGlossaryMetadata.State]
        CANCELLED: _ClassVar[CreateGlossaryMetadata.State]
    STATE_UNSPECIFIED: CreateGlossaryMetadata.State
    RUNNING: CreateGlossaryMetadata.State
    SUCCEEDED: CreateGlossaryMetadata.State
    FAILED: CreateGlossaryMetadata.State
    CANCELLING: CreateGlossaryMetadata.State
    CANCELLED: CreateGlossaryMetadata.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: CreateGlossaryMetadata.State
    submit_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[CreateGlossaryMetadata.State, str]]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteGlossaryMetadata(_message.Message):
    __slots__ = ('name', 'state', 'submit_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DeleteGlossaryMetadata.State]
        RUNNING: _ClassVar[DeleteGlossaryMetadata.State]
        SUCCEEDED: _ClassVar[DeleteGlossaryMetadata.State]
        FAILED: _ClassVar[DeleteGlossaryMetadata.State]
        CANCELLING: _ClassVar[DeleteGlossaryMetadata.State]
        CANCELLED: _ClassVar[DeleteGlossaryMetadata.State]
    STATE_UNSPECIFIED: DeleteGlossaryMetadata.State
    RUNNING: DeleteGlossaryMetadata.State
    SUCCEEDED: DeleteGlossaryMetadata.State
    FAILED: DeleteGlossaryMetadata.State
    CANCELLING: DeleteGlossaryMetadata.State
    CANCELLED: DeleteGlossaryMetadata.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: DeleteGlossaryMetadata.State
    submit_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[DeleteGlossaryMetadata.State, str]]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteGlossaryResponse(_message.Message):
    __slots__ = ('name', 'submit_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    submit_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchTranslateDocumentRequest(_message.Message):
    __slots__ = ('parent', 'source_language_code', 'target_language_codes', 'input_configs', 'output_config', 'models', 'glossaries', 'format_conversions', 'customized_attribution', 'enable_shadow_removal_native_pdf', 'enable_rotation_correction')

    class ModelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class GlossariesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TranslateTextGlossaryConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TranslateTextGlossaryConfig, _Mapping]]=...) -> None:
            ...

    class FormatConversionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    GLOSSARIES_FIELD_NUMBER: _ClassVar[int]
    FORMAT_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SHADOW_REMOVAL_NATIVE_PDF_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ROTATION_CORRECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_language_code: str
    target_language_codes: _containers.RepeatedScalarFieldContainer[str]
    input_configs: _containers.RepeatedCompositeFieldContainer[BatchDocumentInputConfig]
    output_config: BatchDocumentOutputConfig
    models: _containers.ScalarMap[str, str]
    glossaries: _containers.MessageMap[str, TranslateTextGlossaryConfig]
    format_conversions: _containers.ScalarMap[str, str]
    customized_attribution: str
    enable_shadow_removal_native_pdf: bool
    enable_rotation_correction: bool

    def __init__(self, parent: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_codes: _Optional[_Iterable[str]]=..., input_configs: _Optional[_Iterable[_Union[BatchDocumentInputConfig, _Mapping]]]=..., output_config: _Optional[_Union[BatchDocumentOutputConfig, _Mapping]]=..., models: _Optional[_Mapping[str, str]]=..., glossaries: _Optional[_Mapping[str, TranslateTextGlossaryConfig]]=..., format_conversions: _Optional[_Mapping[str, str]]=..., customized_attribution: _Optional[str]=..., enable_shadow_removal_native_pdf: bool=..., enable_rotation_correction: bool=...) -> None:
        ...

class BatchDocumentInputConfig(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class BatchDocumentOutputConfig(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=...) -> None:
        ...

class BatchTranslateDocumentResponse(_message.Message):
    __slots__ = ('total_pages', 'translated_pages', 'failed_pages', 'total_billable_pages', 'total_characters', 'translated_characters', 'failed_characters', 'total_billable_characters', 'submit_time', 'end_time')
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_PAGES_FIELD_NUMBER: _ClassVar[int]
    FAILED_PAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_PAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    total_pages: int
    translated_pages: int
    failed_pages: int
    total_billable_pages: int
    total_characters: int
    translated_characters: int
    failed_characters: int
    total_billable_characters: int
    submit_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, total_pages: _Optional[int]=..., translated_pages: _Optional[int]=..., failed_pages: _Optional[int]=..., total_billable_pages: _Optional[int]=..., total_characters: _Optional[int]=..., translated_characters: _Optional[int]=..., failed_characters: _Optional[int]=..., total_billable_characters: _Optional[int]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchTranslateDocumentMetadata(_message.Message):
    __slots__ = ('state', 'total_pages', 'translated_pages', 'failed_pages', 'total_billable_pages', 'total_characters', 'translated_characters', 'failed_characters', 'total_billable_characters', 'submit_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchTranslateDocumentMetadata.State]
        RUNNING: _ClassVar[BatchTranslateDocumentMetadata.State]
        SUCCEEDED: _ClassVar[BatchTranslateDocumentMetadata.State]
        FAILED: _ClassVar[BatchTranslateDocumentMetadata.State]
        CANCELLING: _ClassVar[BatchTranslateDocumentMetadata.State]
        CANCELLED: _ClassVar[BatchTranslateDocumentMetadata.State]
    STATE_UNSPECIFIED: BatchTranslateDocumentMetadata.State
    RUNNING: BatchTranslateDocumentMetadata.State
    SUCCEEDED: BatchTranslateDocumentMetadata.State
    FAILED: BatchTranslateDocumentMetadata.State
    CANCELLING: BatchTranslateDocumentMetadata.State
    CANCELLED: BatchTranslateDocumentMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_PAGES_FIELD_NUMBER: _ClassVar[int]
    FAILED_PAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_PAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    state: BatchTranslateDocumentMetadata.State
    total_pages: int
    translated_pages: int
    failed_pages: int
    total_billable_pages: int
    total_characters: int
    translated_characters: int
    failed_characters: int
    total_billable_characters: int
    submit_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[BatchTranslateDocumentMetadata.State, str]]=..., total_pages: _Optional[int]=..., translated_pages: _Optional[int]=..., failed_pages: _Optional[int]=..., total_billable_pages: _Optional[int]=..., total_characters: _Optional[int]=..., translated_characters: _Optional[int]=..., failed_characters: _Optional[int]=..., total_billable_characters: _Optional[int]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...