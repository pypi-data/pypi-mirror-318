from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.translate.v3 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdaptiveMtDataset(_message.Message):
    __slots__ = ("name", "display_name", "source_language_code", "target_language_code", "example_count", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    source_language_code: str
    target_language_code: str
    example_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., source_language_code: _Optional[str] = ..., target_language_code: _Optional[str] = ..., example_count: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAdaptiveMtDatasetRequest(_message.Message):
    __slots__ = ("parent", "adaptive_mt_dataset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ADAPTIVE_MT_DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    adaptive_mt_dataset: AdaptiveMtDataset
    def __init__(self, parent: _Optional[str] = ..., adaptive_mt_dataset: _Optional[_Union[AdaptiveMtDataset, _Mapping]] = ...) -> None: ...

class DeleteAdaptiveMtDatasetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetAdaptiveMtDatasetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAdaptiveMtDatasetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAdaptiveMtDatasetsResponse(_message.Message):
    __slots__ = ("adaptive_mt_datasets", "next_page_token")
    ADAPTIVE_MT_DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    adaptive_mt_datasets: _containers.RepeatedCompositeFieldContainer[AdaptiveMtDataset]
    next_page_token: str
    def __init__(self, adaptive_mt_datasets: _Optional[_Iterable[_Union[AdaptiveMtDataset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AdaptiveMtTranslateRequest(_message.Message):
    __slots__ = ("parent", "dataset", "content", "reference_sentence_config", "glossary_config")
    class ReferenceSentencePair(_message.Message):
        __slots__ = ("source_sentence", "target_sentence")
        SOURCE_SENTENCE_FIELD_NUMBER: _ClassVar[int]
        TARGET_SENTENCE_FIELD_NUMBER: _ClassVar[int]
        source_sentence: str
        target_sentence: str
        def __init__(self, source_sentence: _Optional[str] = ..., target_sentence: _Optional[str] = ...) -> None: ...
    class ReferenceSentencePairList(_message.Message):
        __slots__ = ("reference_sentence_pairs",)
        REFERENCE_SENTENCE_PAIRS_FIELD_NUMBER: _ClassVar[int]
        reference_sentence_pairs: _containers.RepeatedCompositeFieldContainer[AdaptiveMtTranslateRequest.ReferenceSentencePair]
        def __init__(self, reference_sentence_pairs: _Optional[_Iterable[_Union[AdaptiveMtTranslateRequest.ReferenceSentencePair, _Mapping]]] = ...) -> None: ...
    class ReferenceSentenceConfig(_message.Message):
        __slots__ = ("reference_sentence_pair_lists", "source_language_code", "target_language_code")
        REFERENCE_SENTENCE_PAIR_LISTS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        reference_sentence_pair_lists: _containers.RepeatedCompositeFieldContainer[AdaptiveMtTranslateRequest.ReferenceSentencePairList]
        source_language_code: str
        target_language_code: str
        def __init__(self, reference_sentence_pair_lists: _Optional[_Iterable[_Union[AdaptiveMtTranslateRequest.ReferenceSentencePairList, _Mapping]]] = ..., source_language_code: _Optional[str] = ..., target_language_code: _Optional[str] = ...) -> None: ...
    class GlossaryConfig(_message.Message):
        __slots__ = ("glossary", "ignore_case", "contextual_translation_enabled")
        GLOSSARY_FIELD_NUMBER: _ClassVar[int]
        IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
        CONTEXTUAL_TRANSLATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        glossary: str
        ignore_case: bool
        contextual_translation_enabled: bool
        def __init__(self, glossary: _Optional[str] = ..., ignore_case: bool = ..., contextual_translation_enabled: bool = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SENTENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: str
    content: _containers.RepeatedScalarFieldContainer[str]
    reference_sentence_config: AdaptiveMtTranslateRequest.ReferenceSentenceConfig
    glossary_config: AdaptiveMtTranslateRequest.GlossaryConfig
    def __init__(self, parent: _Optional[str] = ..., dataset: _Optional[str] = ..., content: _Optional[_Iterable[str]] = ..., reference_sentence_config: _Optional[_Union[AdaptiveMtTranslateRequest.ReferenceSentenceConfig, _Mapping]] = ..., glossary_config: _Optional[_Union[AdaptiveMtTranslateRequest.GlossaryConfig, _Mapping]] = ...) -> None: ...

class AdaptiveMtTranslation(_message.Message):
    __slots__ = ("translated_text",)
    TRANSLATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    translated_text: str
    def __init__(self, translated_text: _Optional[str] = ...) -> None: ...

class AdaptiveMtTranslateResponse(_message.Message):
    __slots__ = ("translations", "language_code", "glossary_translations")
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    translations: _containers.RepeatedCompositeFieldContainer[AdaptiveMtTranslation]
    language_code: str
    glossary_translations: _containers.RepeatedCompositeFieldContainer[AdaptiveMtTranslation]
    def __init__(self, translations: _Optional[_Iterable[_Union[AdaptiveMtTranslation, _Mapping]]] = ..., language_code: _Optional[str] = ..., glossary_translations: _Optional[_Iterable[_Union[AdaptiveMtTranslation, _Mapping]]] = ...) -> None: ...

class AdaptiveMtFile(_message.Message):
    __slots__ = ("name", "display_name", "entry_count", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    entry_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., entry_count: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAdaptiveMtFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteAdaptiveMtFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImportAdaptiveMtFileRequest(_message.Message):
    __slots__ = ("parent", "file_input_source", "gcs_input_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILE_INPUT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_INPUT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    file_input_source: _common_pb2.FileInputSource
    gcs_input_source: _common_pb2.GcsInputSource
    def __init__(self, parent: _Optional[str] = ..., file_input_source: _Optional[_Union[_common_pb2.FileInputSource, _Mapping]] = ..., gcs_input_source: _Optional[_Union[_common_pb2.GcsInputSource, _Mapping]] = ...) -> None: ...

class ImportAdaptiveMtFileResponse(_message.Message):
    __slots__ = ("adaptive_mt_file",)
    ADAPTIVE_MT_FILE_FIELD_NUMBER: _ClassVar[int]
    adaptive_mt_file: AdaptiveMtFile
    def __init__(self, adaptive_mt_file: _Optional[_Union[AdaptiveMtFile, _Mapping]] = ...) -> None: ...

class ListAdaptiveMtFilesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAdaptiveMtFilesResponse(_message.Message):
    __slots__ = ("adaptive_mt_files", "next_page_token")
    ADAPTIVE_MT_FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    adaptive_mt_files: _containers.RepeatedCompositeFieldContainer[AdaptiveMtFile]
    next_page_token: str
    def __init__(self, adaptive_mt_files: _Optional[_Iterable[_Union[AdaptiveMtFile, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AdaptiveMtSentence(_message.Message):
    __slots__ = ("name", "source_sentence", "target_sentence", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SENTENCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SENTENCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_sentence: str
    target_sentence: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., source_sentence: _Optional[str] = ..., target_sentence: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAdaptiveMtSentencesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAdaptiveMtSentencesResponse(_message.Message):
    __slots__ = ("adaptive_mt_sentences", "next_page_token")
    ADAPTIVE_MT_SENTENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    adaptive_mt_sentences: _containers.RepeatedCompositeFieldContainer[AdaptiveMtSentence]
    next_page_token: str
    def __init__(self, adaptive_mt_sentences: _Optional[_Iterable[_Union[AdaptiveMtSentence, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
