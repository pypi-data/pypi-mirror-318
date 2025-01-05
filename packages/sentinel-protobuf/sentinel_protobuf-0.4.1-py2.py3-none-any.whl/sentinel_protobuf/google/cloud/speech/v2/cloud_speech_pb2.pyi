from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateRecognizerRequest(_message.Message):
    __slots__ = ('recognizer', 'validate_only', 'recognizer_id', 'parent')
    RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RECOGNIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    recognizer: Recognizer
    validate_only: bool
    recognizer_id: str
    parent: str

    def __init__(self, recognizer: _Optional[_Union[Recognizer, _Mapping]]=..., validate_only: bool=..., recognizer_id: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time', 'resource', 'method', 'kms_key_name', 'kms_key_version_name', 'batch_recognize_request', 'create_recognizer_request', 'update_recognizer_request', 'delete_recognizer_request', 'undelete_recognizer_request', 'create_custom_class_request', 'update_custom_class_request', 'delete_custom_class_request', 'undelete_custom_class_request', 'create_phrase_set_request', 'update_phrase_set_request', 'delete_phrase_set_request', 'undelete_phrase_set_request', 'update_config_request', 'progress_percent', 'batch_recognize_metadata')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    BATCH_RECOGNIZE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_RECOGNIZER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_RECOGNIZER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_RECOGNIZER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNDELETE_RECOGNIZER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_CUSTOM_CLASS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CUSTOM_CLASS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_CUSTOM_CLASS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNDELETE_CUSTOM_CLASS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_PHRASE_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PHRASE_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_PHRASE_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UNDELETE_PHRASE_SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONFIG_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_RECOGNIZE_METADATA_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    resource: str
    method: str
    kms_key_name: str
    kms_key_version_name: str
    batch_recognize_request: BatchRecognizeRequest
    create_recognizer_request: CreateRecognizerRequest
    update_recognizer_request: UpdateRecognizerRequest
    delete_recognizer_request: DeleteRecognizerRequest
    undelete_recognizer_request: UndeleteRecognizerRequest
    create_custom_class_request: CreateCustomClassRequest
    update_custom_class_request: UpdateCustomClassRequest
    delete_custom_class_request: DeleteCustomClassRequest
    undelete_custom_class_request: UndeleteCustomClassRequest
    create_phrase_set_request: CreatePhraseSetRequest
    update_phrase_set_request: UpdatePhraseSetRequest
    delete_phrase_set_request: DeletePhraseSetRequest
    undelete_phrase_set_request: UndeletePhraseSetRequest
    update_config_request: UpdateConfigRequest
    progress_percent: int
    batch_recognize_metadata: BatchRecognizeMetadata

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resource: _Optional[str]=..., method: _Optional[str]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=..., batch_recognize_request: _Optional[_Union[BatchRecognizeRequest, _Mapping]]=..., create_recognizer_request: _Optional[_Union[CreateRecognizerRequest, _Mapping]]=..., update_recognizer_request: _Optional[_Union[UpdateRecognizerRequest, _Mapping]]=..., delete_recognizer_request: _Optional[_Union[DeleteRecognizerRequest, _Mapping]]=..., undelete_recognizer_request: _Optional[_Union[UndeleteRecognizerRequest, _Mapping]]=..., create_custom_class_request: _Optional[_Union[CreateCustomClassRequest, _Mapping]]=..., update_custom_class_request: _Optional[_Union[UpdateCustomClassRequest, _Mapping]]=..., delete_custom_class_request: _Optional[_Union[DeleteCustomClassRequest, _Mapping]]=..., undelete_custom_class_request: _Optional[_Union[UndeleteCustomClassRequest, _Mapping]]=..., create_phrase_set_request: _Optional[_Union[CreatePhraseSetRequest, _Mapping]]=..., update_phrase_set_request: _Optional[_Union[UpdatePhraseSetRequest, _Mapping]]=..., delete_phrase_set_request: _Optional[_Union[DeletePhraseSetRequest, _Mapping]]=..., undelete_phrase_set_request: _Optional[_Union[UndeletePhraseSetRequest, _Mapping]]=..., update_config_request: _Optional[_Union[UpdateConfigRequest, _Mapping]]=..., progress_percent: _Optional[int]=..., batch_recognize_metadata: _Optional[_Union[BatchRecognizeMetadata, _Mapping]]=...) -> None:
        ...

class ListRecognizersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListRecognizersResponse(_message.Message):
    __slots__ = ('recognizers', 'next_page_token')
    RECOGNIZERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    recognizers: _containers.RepeatedCompositeFieldContainer[Recognizer]
    next_page_token: str

    def __init__(self, recognizers: _Optional[_Iterable[_Union[Recognizer, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRecognizerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateRecognizerRequest(_message.Message):
    __slots__ = ('recognizer', 'update_mask', 'validate_only')
    RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    recognizer: Recognizer
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, recognizer: _Optional[_Union[Recognizer, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteRecognizerRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'allow_missing', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=..., etag: _Optional[str]=...) -> None:
        ...

class UndeleteRecognizerRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class Recognizer(_message.Message):
    __slots__ = ('name', 'uid', 'display_name', 'model', 'language_codes', 'default_recognition_config', 'annotations', 'state', 'create_time', 'update_time', 'delete_time', 'expire_time', 'etag', 'reconciling', 'kms_key_name', 'kms_key_version_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Recognizer.State]
        ACTIVE: _ClassVar[Recognizer.State]
        DELETED: _ClassVar[Recognizer.State]
    STATE_UNSPECIFIED: Recognizer.State
    ACTIVE: Recognizer.State
    DELETED: Recognizer.State

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RECOGNITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    display_name: str
    model: str
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    default_recognition_config: RecognitionConfig
    annotations: _containers.ScalarMap[str, str]
    state: Recognizer.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    etag: str
    reconciling: bool
    kms_key_name: str
    kms_key_version_name: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., model: _Optional[str]=..., language_codes: _Optional[_Iterable[str]]=..., default_recognition_config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Recognizer.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., reconciling: bool=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=...) -> None:
        ...

class AutoDetectDecodingConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExplicitDecodingConfig(_message.Message):
    __slots__ = ('encoding', 'sample_rate_hertz', 'audio_channel_count')

    class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_ENCODING_UNSPECIFIED: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        LINEAR16: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        MULAW: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        ALAW: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        AMR: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        AMR_WB: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        FLAC: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        MP3: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        OGG_OPUS: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        WEBM_OPUS: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        MP4_AAC: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        M4A_AAC: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
        MOV_AAC: _ClassVar[ExplicitDecodingConfig.AudioEncoding]
    AUDIO_ENCODING_UNSPECIFIED: ExplicitDecodingConfig.AudioEncoding
    LINEAR16: ExplicitDecodingConfig.AudioEncoding
    MULAW: ExplicitDecodingConfig.AudioEncoding
    ALAW: ExplicitDecodingConfig.AudioEncoding
    AMR: ExplicitDecodingConfig.AudioEncoding
    AMR_WB: ExplicitDecodingConfig.AudioEncoding
    FLAC: ExplicitDecodingConfig.AudioEncoding
    MP3: ExplicitDecodingConfig.AudioEncoding
    OGG_OPUS: ExplicitDecodingConfig.AudioEncoding
    WEBM_OPUS: ExplicitDecodingConfig.AudioEncoding
    MP4_AAC: ExplicitDecodingConfig.AudioEncoding
    M4A_AAC: ExplicitDecodingConfig.AudioEncoding
    MOV_AAC: ExplicitDecodingConfig.AudioEncoding
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    encoding: ExplicitDecodingConfig.AudioEncoding
    sample_rate_hertz: int
    audio_channel_count: int

    def __init__(self, encoding: _Optional[_Union[ExplicitDecodingConfig.AudioEncoding, str]]=..., sample_rate_hertz: _Optional[int]=..., audio_channel_count: _Optional[int]=...) -> None:
        ...

class SpeakerDiarizationConfig(_message.Message):
    __slots__ = ('min_speaker_count', 'max_speaker_count')
    MIN_SPEAKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEAKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_speaker_count: int
    max_speaker_count: int

    def __init__(self, min_speaker_count: _Optional[int]=..., max_speaker_count: _Optional[int]=...) -> None:
        ...

class RecognitionFeatures(_message.Message):
    __slots__ = ('profanity_filter', 'enable_word_time_offsets', 'enable_word_confidence', 'enable_automatic_punctuation', 'enable_spoken_punctuation', 'enable_spoken_emojis', 'multi_channel_mode', 'diarization_config', 'max_alternatives')

    class MultiChannelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MULTI_CHANNEL_MODE_UNSPECIFIED: _ClassVar[RecognitionFeatures.MultiChannelMode]
        SEPARATE_RECOGNITION_PER_CHANNEL: _ClassVar[RecognitionFeatures.MultiChannelMode]
    MULTI_CHANNEL_MODE_UNSPECIFIED: RecognitionFeatures.MultiChannelMode
    SEPARATE_RECOGNITION_PER_CHANNEL: RecognitionFeatures.MultiChannelMode
    PROFANITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_TIME_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPOKEN_PUNCTUATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPOKEN_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    MULTI_CHANNEL_MODE_FIELD_NUMBER: _ClassVar[int]
    DIARIZATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    profanity_filter: bool
    enable_word_time_offsets: bool
    enable_word_confidence: bool
    enable_automatic_punctuation: bool
    enable_spoken_punctuation: bool
    enable_spoken_emojis: bool
    multi_channel_mode: RecognitionFeatures.MultiChannelMode
    diarization_config: SpeakerDiarizationConfig
    max_alternatives: int

    def __init__(self, profanity_filter: bool=..., enable_word_time_offsets: bool=..., enable_word_confidence: bool=..., enable_automatic_punctuation: bool=..., enable_spoken_punctuation: bool=..., enable_spoken_emojis: bool=..., multi_channel_mode: _Optional[_Union[RecognitionFeatures.MultiChannelMode, str]]=..., diarization_config: _Optional[_Union[SpeakerDiarizationConfig, _Mapping]]=..., max_alternatives: _Optional[int]=...) -> None:
        ...

class TranscriptNormalization(_message.Message):
    __slots__ = ('entries',)

    class Entry(_message.Message):
        __slots__ = ('search', 'replace', 'case_sensitive')
        SEARCH_FIELD_NUMBER: _ClassVar[int]
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        search: str
        replace: str
        case_sensitive: bool

        def __init__(self, search: _Optional[str]=..., replace: _Optional[str]=..., case_sensitive: bool=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[TranscriptNormalization.Entry]

    def __init__(self, entries: _Optional[_Iterable[_Union[TranscriptNormalization.Entry, _Mapping]]]=...) -> None:
        ...

class TranslationConfig(_message.Message):
    __slots__ = ('target_language',)
    TARGET_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    target_language: str

    def __init__(self, target_language: _Optional[str]=...) -> None:
        ...

class SpeechAdaptation(_message.Message):
    __slots__ = ('phrase_sets', 'custom_classes')

    class AdaptationPhraseSet(_message.Message):
        __slots__ = ('phrase_set', 'inline_phrase_set')
        PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
        INLINE_PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
        phrase_set: str
        inline_phrase_set: PhraseSet

        def __init__(self, phrase_set: _Optional[str]=..., inline_phrase_set: _Optional[_Union[PhraseSet, _Mapping]]=...) -> None:
            ...
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    phrase_sets: _containers.RepeatedCompositeFieldContainer[SpeechAdaptation.AdaptationPhraseSet]
    custom_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]

    def __init__(self, phrase_sets: _Optional[_Iterable[_Union[SpeechAdaptation.AdaptationPhraseSet, _Mapping]]]=..., custom_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]]=...) -> None:
        ...

class RecognitionConfig(_message.Message):
    __slots__ = ('auto_decoding_config', 'explicit_decoding_config', 'model', 'language_codes', 'features', 'adaptation', 'transcript_normalization', 'translation_config')
    AUTO_DECODING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_DECODING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_NORMALIZATION_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    auto_decoding_config: AutoDetectDecodingConfig
    explicit_decoding_config: ExplicitDecodingConfig
    model: str
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    features: RecognitionFeatures
    adaptation: SpeechAdaptation
    transcript_normalization: TranscriptNormalization
    translation_config: TranslationConfig

    def __init__(self, auto_decoding_config: _Optional[_Union[AutoDetectDecodingConfig, _Mapping]]=..., explicit_decoding_config: _Optional[_Union[ExplicitDecodingConfig, _Mapping]]=..., model: _Optional[str]=..., language_codes: _Optional[_Iterable[str]]=..., features: _Optional[_Union[RecognitionFeatures, _Mapping]]=..., adaptation: _Optional[_Union[SpeechAdaptation, _Mapping]]=..., transcript_normalization: _Optional[_Union[TranscriptNormalization, _Mapping]]=..., translation_config: _Optional[_Union[TranslationConfig, _Mapping]]=...) -> None:
        ...

class RecognizeRequest(_message.Message):
    __slots__ = ('recognizer', 'config', 'config_mask', 'content', 'uri')
    RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    recognizer: str
    config: RecognitionConfig
    config_mask: _field_mask_pb2.FieldMask
    content: bytes
    uri: str

    def __init__(self, recognizer: _Optional[str]=..., config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., content: _Optional[bytes]=..., uri: _Optional[str]=...) -> None:
        ...

class RecognitionResponseMetadata(_message.Message):
    __slots__ = ('request_id', 'total_billed_duration')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_DURATION_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    total_billed_duration: _duration_pb2.Duration

    def __init__(self, request_id: _Optional[str]=..., total_billed_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class SpeechRecognitionAlternative(_message.Message):
    __slots__ = ('transcript', 'confidence', 'words')
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    transcript: str
    confidence: float
    words: _containers.RepeatedCompositeFieldContainer[WordInfo]

    def __init__(self, transcript: _Optional[str]=..., confidence: _Optional[float]=..., words: _Optional[_Iterable[_Union[WordInfo, _Mapping]]]=...) -> None:
        ...

class WordInfo(_message.Message):
    __slots__ = ('start_offset', 'end_offset', 'word', 'confidence', 'speaker_label')
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_LABEL_FIELD_NUMBER: _ClassVar[int]
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    word: str
    confidence: float
    speaker_label: str

    def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., word: _Optional[str]=..., confidence: _Optional[float]=..., speaker_label: _Optional[str]=...) -> None:
        ...

class SpeechRecognitionResult(_message.Message):
    __slots__ = ('alternatives', 'channel_tag', 'result_end_offset', 'language_code')
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]
    channel_tag: int
    result_end_offset: _duration_pb2.Duration
    language_code: str

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=..., channel_tag: _Optional[int]=..., result_end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class RecognizeResponse(_message.Message):
    __slots__ = ('results', 'metadata')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionResult]
    metadata: RecognitionResponseMetadata

    def __init__(self, results: _Optional[_Iterable[_Union[SpeechRecognitionResult, _Mapping]]]=..., metadata: _Optional[_Union[RecognitionResponseMetadata, _Mapping]]=...) -> None:
        ...

class StreamingRecognitionFeatures(_message.Message):
    __slots__ = ('enable_voice_activity_events', 'interim_results', 'voice_activity_timeout')

    class VoiceActivityTimeout(_message.Message):
        __slots__ = ('speech_start_timeout', 'speech_end_timeout')
        SPEECH_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        SPEECH_END_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        speech_start_timeout: _duration_pb2.Duration
        speech_end_timeout: _duration_pb2.Duration

        def __init__(self, speech_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., speech_end_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    ENABLE_VOICE_ACTIVITY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    INTERIM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    VOICE_ACTIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    enable_voice_activity_events: bool
    interim_results: bool
    voice_activity_timeout: StreamingRecognitionFeatures.VoiceActivityTimeout

    def __init__(self, enable_voice_activity_events: bool=..., interim_results: bool=..., voice_activity_timeout: _Optional[_Union[StreamingRecognitionFeatures.VoiceActivityTimeout, _Mapping]]=...) -> None:
        ...

class StreamingRecognitionConfig(_message.Message):
    __slots__ = ('config', 'config_mask', 'streaming_features')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    STREAMING_FEATURES_FIELD_NUMBER: _ClassVar[int]
    config: RecognitionConfig
    config_mask: _field_mask_pb2.FieldMask
    streaming_features: StreamingRecognitionFeatures

    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., streaming_features: _Optional[_Union[StreamingRecognitionFeatures, _Mapping]]=...) -> None:
        ...

class StreamingRecognizeRequest(_message.Message):
    __slots__ = ('recognizer', 'streaming_config', 'audio')
    RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    STREAMING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    recognizer: str
    streaming_config: StreamingRecognitionConfig
    audio: bytes

    def __init__(self, recognizer: _Optional[str]=..., streaming_config: _Optional[_Union[StreamingRecognitionConfig, _Mapping]]=..., audio: _Optional[bytes]=...) -> None:
        ...

class BatchRecognizeRequest(_message.Message):
    __slots__ = ('recognizer', 'config', 'config_mask', 'files', 'recognition_output_config', 'processing_strategy')

    class ProcessingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSING_STRATEGY_UNSPECIFIED: _ClassVar[BatchRecognizeRequest.ProcessingStrategy]
        DYNAMIC_BATCHING: _ClassVar[BatchRecognizeRequest.ProcessingStrategy]
    PROCESSING_STRATEGY_UNSPECIFIED: BatchRecognizeRequest.ProcessingStrategy
    DYNAMIC_BATCHING: BatchRecognizeRequest.ProcessingStrategy
    RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    RECOGNITION_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    recognizer: str
    config: RecognitionConfig
    config_mask: _field_mask_pb2.FieldMask
    files: _containers.RepeatedCompositeFieldContainer[BatchRecognizeFileMetadata]
    recognition_output_config: RecognitionOutputConfig
    processing_strategy: BatchRecognizeRequest.ProcessingStrategy

    def __init__(self, recognizer: _Optional[str]=..., config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., files: _Optional[_Iterable[_Union[BatchRecognizeFileMetadata, _Mapping]]]=..., recognition_output_config: _Optional[_Union[RecognitionOutputConfig, _Mapping]]=..., processing_strategy: _Optional[_Union[BatchRecognizeRequest.ProcessingStrategy, str]]=...) -> None:
        ...

class GcsOutputConfig(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class InlineOutputConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NativeOutputFileFormatConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class VttOutputFileFormatConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SrtOutputFileFormatConfig(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OutputFormatConfig(_message.Message):
    __slots__ = ('native', 'vtt', 'srt')
    NATIVE_FIELD_NUMBER: _ClassVar[int]
    VTT_FIELD_NUMBER: _ClassVar[int]
    SRT_FIELD_NUMBER: _ClassVar[int]
    native: NativeOutputFileFormatConfig
    vtt: VttOutputFileFormatConfig
    srt: SrtOutputFileFormatConfig

    def __init__(self, native: _Optional[_Union[NativeOutputFileFormatConfig, _Mapping]]=..., vtt: _Optional[_Union[VttOutputFileFormatConfig, _Mapping]]=..., srt: _Optional[_Union[SrtOutputFileFormatConfig, _Mapping]]=...) -> None:
        ...

class RecognitionOutputConfig(_message.Message):
    __slots__ = ('gcs_output_config', 'inline_response_config', 'output_format_config')
    GCS_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INLINE_RESPONSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gcs_output_config: GcsOutputConfig
    inline_response_config: InlineOutputConfig
    output_format_config: OutputFormatConfig

    def __init__(self, gcs_output_config: _Optional[_Union[GcsOutputConfig, _Mapping]]=..., inline_response_config: _Optional[_Union[InlineOutputConfig, _Mapping]]=..., output_format_config: _Optional[_Union[OutputFormatConfig, _Mapping]]=...) -> None:
        ...

class BatchRecognizeResponse(_message.Message):
    __slots__ = ('results', 'total_billed_duration')

    class ResultsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BatchRecognizeFileResult

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[BatchRecognizeFileResult, _Mapping]]=...) -> None:
            ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_DURATION_FIELD_NUMBER: _ClassVar[int]
    results: _containers.MessageMap[str, BatchRecognizeFileResult]
    total_billed_duration: _duration_pb2.Duration

    def __init__(self, results: _Optional[_Mapping[str, BatchRecognizeFileResult]]=..., total_billed_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class BatchRecognizeResults(_message.Message):
    __slots__ = ('results', 'metadata')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionResult]
    metadata: RecognitionResponseMetadata

    def __init__(self, results: _Optional[_Iterable[_Union[SpeechRecognitionResult, _Mapping]]]=..., metadata: _Optional[_Union[RecognitionResponseMetadata, _Mapping]]=...) -> None:
        ...

class CloudStorageResult(_message.Message):
    __slots__ = ('uri', 'vtt_format_uri', 'srt_format_uri')
    URI_FIELD_NUMBER: _ClassVar[int]
    VTT_FORMAT_URI_FIELD_NUMBER: _ClassVar[int]
    SRT_FORMAT_URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    vtt_format_uri: str
    srt_format_uri: str

    def __init__(self, uri: _Optional[str]=..., vtt_format_uri: _Optional[str]=..., srt_format_uri: _Optional[str]=...) -> None:
        ...

class InlineResult(_message.Message):
    __slots__ = ('transcript', 'vtt_captions', 'srt_captions')
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    VTT_CAPTIONS_FIELD_NUMBER: _ClassVar[int]
    SRT_CAPTIONS_FIELD_NUMBER: _ClassVar[int]
    transcript: BatchRecognizeResults
    vtt_captions: str
    srt_captions: str

    def __init__(self, transcript: _Optional[_Union[BatchRecognizeResults, _Mapping]]=..., vtt_captions: _Optional[str]=..., srt_captions: _Optional[str]=...) -> None:
        ...

class BatchRecognizeFileResult(_message.Message):
    __slots__ = ('error', 'metadata', 'cloud_storage_result', 'inline_result', 'uri', 'transcript')
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STORAGE_RESULT_FIELD_NUMBER: _ClassVar[int]
    INLINE_RESULT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    metadata: RecognitionResponseMetadata
    cloud_storage_result: CloudStorageResult
    inline_result: InlineResult
    uri: str
    transcript: BatchRecognizeResults

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., metadata: _Optional[_Union[RecognitionResponseMetadata, _Mapping]]=..., cloud_storage_result: _Optional[_Union[CloudStorageResult, _Mapping]]=..., inline_result: _Optional[_Union[InlineResult, _Mapping]]=..., uri: _Optional[str]=..., transcript: _Optional[_Union[BatchRecognizeResults, _Mapping]]=...) -> None:
        ...

class BatchRecognizeTranscriptionMetadata(_message.Message):
    __slots__ = ('progress_percent', 'error', 'uri')
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    error: _status_pb2.Status
    uri: str

    def __init__(self, progress_percent: _Optional[int]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., uri: _Optional[str]=...) -> None:
        ...

class BatchRecognizeMetadata(_message.Message):
    __slots__ = ('transcription_metadata',)

    class TranscriptionMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BatchRecognizeTranscriptionMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[BatchRecognizeTranscriptionMetadata, _Mapping]]=...) -> None:
            ...
    TRANSCRIPTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    transcription_metadata: _containers.MessageMap[str, BatchRecognizeTranscriptionMetadata]

    def __init__(self, transcription_metadata: _Optional[_Mapping[str, BatchRecognizeTranscriptionMetadata]]=...) -> None:
        ...

class BatchRecognizeFileMetadata(_message.Message):
    __slots__ = ('uri', 'config', 'config_mask')
    URI_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    uri: str
    config: RecognitionConfig
    config_mask: _field_mask_pb2.FieldMask

    def __init__(self, uri: _Optional[str]=..., config: _Optional[_Union[RecognitionConfig, _Mapping]]=..., config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class StreamingRecognitionResult(_message.Message):
    __slots__ = ('alternatives', 'is_final', 'stability', 'result_end_offset', 'channel_tag', 'language_code')
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    STABILITY_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[SpeechRecognitionAlternative]
    is_final: bool
    stability: float
    result_end_offset: _duration_pb2.Duration
    channel_tag: int
    language_code: str

    def __init__(self, alternatives: _Optional[_Iterable[_Union[SpeechRecognitionAlternative, _Mapping]]]=..., is_final: bool=..., stability: _Optional[float]=..., result_end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., channel_tag: _Optional[int]=..., language_code: _Optional[str]=...) -> None:
        ...

class StreamingRecognizeResponse(_message.Message):
    __slots__ = ('results', 'speech_event_type', 'speech_event_offset', 'metadata')

    class SpeechEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEECH_EVENT_TYPE_UNSPECIFIED: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        END_OF_SINGLE_UTTERANCE: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        SPEECH_ACTIVITY_BEGIN: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
        SPEECH_ACTIVITY_END: _ClassVar[StreamingRecognizeResponse.SpeechEventType]
    SPEECH_EVENT_TYPE_UNSPECIFIED: StreamingRecognizeResponse.SpeechEventType
    END_OF_SINGLE_UTTERANCE: StreamingRecognizeResponse.SpeechEventType
    SPEECH_ACTIVITY_BEGIN: StreamingRecognizeResponse.SpeechEventType
    SPEECH_ACTIVITY_END: StreamingRecognizeResponse.SpeechEventType
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SPEECH_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEECH_EVENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[StreamingRecognitionResult]
    speech_event_type: StreamingRecognizeResponse.SpeechEventType
    speech_event_offset: _duration_pb2.Duration
    metadata: RecognitionResponseMetadata

    def __init__(self, results: _Optional[_Iterable[_Union[StreamingRecognitionResult, _Mapping]]]=..., speech_event_type: _Optional[_Union[StreamingRecognizeResponse.SpeechEventType, str]]=..., speech_event_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., metadata: _Optional[_Union[RecognitionResponseMetadata, _Mapping]]=...) -> None:
        ...

class Config(_message.Message):
    __slots__ = ('name', 'kms_key_name', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key_name: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., kms_key_name: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateConfigRequest(_message.Message):
    __slots__ = ('config', 'update_mask')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    config: Config
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, config: _Optional[_Union[Config, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CustomClass(_message.Message):
    __slots__ = ('name', 'uid', 'display_name', 'items', 'state', 'create_time', 'update_time', 'delete_time', 'expire_time', 'annotations', 'etag', 'reconciling', 'kms_key_name', 'kms_key_version_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CustomClass.State]
        ACTIVE: _ClassVar[CustomClass.State]
        DELETED: _ClassVar[CustomClass.State]
    STATE_UNSPECIFIED: CustomClass.State
    ACTIVE: CustomClass.State
    DELETED: CustomClass.State

    class ClassItem(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    display_name: str
    items: _containers.RepeatedCompositeFieldContainer[CustomClass.ClassItem]
    state: CustomClass.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    reconciling: bool
    kms_key_name: str
    kms_key_version_name: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., items: _Optional[_Iterable[_Union[CustomClass.ClassItem, _Mapping]]]=..., state: _Optional[_Union[CustomClass.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., reconciling: bool=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=...) -> None:
        ...

class PhraseSet(_message.Message):
    __slots__ = ('name', 'uid', 'phrases', 'boost', 'display_name', 'state', 'create_time', 'update_time', 'delete_time', 'expire_time', 'annotations', 'etag', 'reconciling', 'kms_key_name', 'kms_key_version_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PhraseSet.State]
        ACTIVE: _ClassVar[PhraseSet.State]
        DELETED: _ClassVar[PhraseSet.State]
    STATE_UNSPECIFIED: PhraseSet.State
    ACTIVE: PhraseSet.State
    DELETED: PhraseSet.State

    class Phrase(_message.Message):
        __slots__ = ('value', 'boost')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOST_FIELD_NUMBER: _ClassVar[int]
        value: str
        boost: float

        def __init__(self, value: _Optional[str]=..., boost: _Optional[float]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    phrases: _containers.RepeatedCompositeFieldContainer[PhraseSet.Phrase]
    boost: float
    display_name: str
    state: PhraseSet.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    reconciling: bool
    kms_key_name: str
    kms_key_version_name: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., phrases: _Optional[_Iterable[_Union[PhraseSet.Phrase, _Mapping]]]=..., boost: _Optional[float]=..., display_name: _Optional[str]=..., state: _Optional[_Union[PhraseSet.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., reconciling: bool=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=...) -> None:
        ...

class CreateCustomClassRequest(_message.Message):
    __slots__ = ('custom_class', 'validate_only', 'custom_class_id', 'parent')
    CUSTOM_CLASS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    custom_class: CustomClass
    validate_only: bool
    custom_class_id: str
    parent: str

    def __init__(self, custom_class: _Optional[_Union[CustomClass, _Mapping]]=..., validate_only: bool=..., custom_class_id: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class ListCustomClassesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListCustomClassesResponse(_message.Message):
    __slots__ = ('custom_classes', 'next_page_token')
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]
    next_page_token: str

    def __init__(self, custom_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCustomClassRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCustomClassRequest(_message.Message):
    __slots__ = ('custom_class', 'update_mask', 'validate_only')
    CUSTOM_CLASS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    custom_class: CustomClass
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, custom_class: _Optional[_Union[CustomClass, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteCustomClassRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'allow_missing', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=..., etag: _Optional[str]=...) -> None:
        ...

class UndeleteCustomClassRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class CreatePhraseSetRequest(_message.Message):
    __slots__ = ('phrase_set', 'validate_only', 'phrase_set_id', 'parent')
    PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    phrase_set: PhraseSet
    validate_only: bool
    phrase_set_id: str
    parent: str

    def __init__(self, phrase_set: _Optional[_Union[PhraseSet, _Mapping]]=..., validate_only: bool=..., phrase_set_id: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class ListPhraseSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListPhraseSetsResponse(_message.Message):
    __slots__ = ('phrase_sets', 'next_page_token')
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phrase_sets: _containers.RepeatedCompositeFieldContainer[PhraseSet]
    next_page_token: str

    def __init__(self, phrase_sets: _Optional[_Iterable[_Union[PhraseSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPhraseSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePhraseSetRequest(_message.Message):
    __slots__ = ('phrase_set', 'update_mask', 'validate_only')
    PHRASE_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    phrase_set: PhraseSet
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, phrase_set: _Optional[_Union[PhraseSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeletePhraseSetRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'allow_missing', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    allow_missing: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=..., etag: _Optional[str]=...) -> None:
        ...

class UndeletePhraseSetRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...