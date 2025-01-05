from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[EncodingType]
    UTF8: _ClassVar[EncodingType]
    UTF16: _ClassVar[EncodingType]
    UTF32: _ClassVar[EncodingType]
NONE: EncodingType
UTF8: EncodingType
UTF16: EncodingType
UTF32: EncodingType

class Document(_message.Message):
    __slots__ = ('type', 'content', 'gcs_content_uri', 'language_code')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Document.Type]
        PLAIN_TEXT: _ClassVar[Document.Type]
        HTML: _ClassVar[Document.Type]
    TYPE_UNSPECIFIED: Document.Type
    PLAIN_TEXT: Document.Type
    HTML: Document.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    GCS_CONTENT_URI_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    type: Document.Type
    content: str
    gcs_content_uri: str
    language_code: str

    def __init__(self, type: _Optional[_Union[Document.Type, str]]=..., content: _Optional[str]=..., gcs_content_uri: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class Sentence(_message.Message):
    __slots__ = ('text', 'sentiment')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    text: TextSpan
    sentiment: Sentiment

    def __init__(self, text: _Optional[_Union[TextSpan, _Mapping]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class Entity(_message.Message):
    __slots__ = ('name', 'type', 'metadata', 'mentions', 'sentiment')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Entity.Type]
        PERSON: _ClassVar[Entity.Type]
        LOCATION: _ClassVar[Entity.Type]
        ORGANIZATION: _ClassVar[Entity.Type]
        EVENT: _ClassVar[Entity.Type]
        WORK_OF_ART: _ClassVar[Entity.Type]
        CONSUMER_GOOD: _ClassVar[Entity.Type]
        OTHER: _ClassVar[Entity.Type]
        PHONE_NUMBER: _ClassVar[Entity.Type]
        ADDRESS: _ClassVar[Entity.Type]
        DATE: _ClassVar[Entity.Type]
        NUMBER: _ClassVar[Entity.Type]
        PRICE: _ClassVar[Entity.Type]
    UNKNOWN: Entity.Type
    PERSON: Entity.Type
    LOCATION: Entity.Type
    ORGANIZATION: Entity.Type
    EVENT: Entity.Type
    WORK_OF_ART: Entity.Type
    CONSUMER_GOOD: Entity.Type
    OTHER: Entity.Type
    PHONE_NUMBER: Entity.Type
    ADDRESS: Entity.Type
    DATE: Entity.Type
    NUMBER: Entity.Type
    PRICE: Entity.Type

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Entity.Type
    metadata: _containers.ScalarMap[str, str]
    mentions: _containers.RepeatedCompositeFieldContainer[EntityMention]
    sentiment: Sentiment

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Entity.Type, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., mentions: _Optional[_Iterable[_Union[EntityMention, _Mapping]]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class Sentiment(_message.Message):
    __slots__ = ('magnitude', 'score')
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    magnitude: float
    score: float

    def __init__(self, magnitude: _Optional[float]=..., score: _Optional[float]=...) -> None:
        ...

class EntityMention(_message.Message):
    __slots__ = ('text', 'type', 'sentiment', 'probability')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[EntityMention.Type]
        PROPER: _ClassVar[EntityMention.Type]
        COMMON: _ClassVar[EntityMention.Type]
    TYPE_UNKNOWN: EntityMention.Type
    PROPER: EntityMention.Type
    COMMON: EntityMention.Type
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    text: TextSpan
    type: EntityMention.Type
    sentiment: Sentiment
    probability: float

    def __init__(self, text: _Optional[_Union[TextSpan, _Mapping]]=..., type: _Optional[_Union[EntityMention.Type, str]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=..., probability: _Optional[float]=...) -> None:
        ...

class TextSpan(_message.Message):
    __slots__ = ('content', 'begin_offset')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_OFFSET_FIELD_NUMBER: _ClassVar[int]
    content: str
    begin_offset: int

    def __init__(self, content: _Optional[str]=..., begin_offset: _Optional[int]=...) -> None:
        ...

class ClassificationCategory(_message.Message):
    __slots__ = ('name', 'confidence', 'severity')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    confidence: float
    severity: float

    def __init__(self, name: _Optional[str]=..., confidence: _Optional[float]=..., severity: _Optional[float]=...) -> None:
        ...

class AnalyzeSentimentRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeSentimentResponse(_message.Message):
    __slots__ = ('document_sentiment', 'language_code', 'sentences', 'language_supported')
    DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    document_sentiment: Sentiment
    language_code: str
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]
    language_supported: bool

    def __init__(self, document_sentiment: _Optional[_Union[Sentiment, _Mapping]]=..., language_code: _Optional[str]=..., sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]]=..., language_supported: bool=...) -> None:
        ...

class AnalyzeEntitiesRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeEntitiesResponse(_message.Message):
    __slots__ = ('entities', 'language_code', 'language_supported')
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    language_code: str
    language_supported: bool

    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., language_code: _Optional[str]=..., language_supported: bool=...) -> None:
        ...

class ClassifyTextRequest(_message.Message):
    __slots__ = ('document',)
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: Document

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=...) -> None:
        ...

class ClassifyTextResponse(_message.Message):
    __slots__ = ('categories', 'language_code', 'language_supported')
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]
    language_code: str
    language_supported: bool

    def __init__(self, categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=..., language_code: _Optional[str]=..., language_supported: bool=...) -> None:
        ...

class ModerateTextRequest(_message.Message):
    __slots__ = ('document', 'model_version')

    class ModelVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_VERSION_UNSPECIFIED: _ClassVar[ModerateTextRequest.ModelVersion]
        MODEL_VERSION_1: _ClassVar[ModerateTextRequest.ModelVersion]
        MODEL_VERSION_2: _ClassVar[ModerateTextRequest.ModelVersion]
    MODEL_VERSION_UNSPECIFIED: ModerateTextRequest.ModelVersion
    MODEL_VERSION_1: ModerateTextRequest.ModelVersion
    MODEL_VERSION_2: ModerateTextRequest.ModelVersion
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    document: Document
    model_version: ModerateTextRequest.ModelVersion

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., model_version: _Optional[_Union[ModerateTextRequest.ModelVersion, str]]=...) -> None:
        ...

class ModerateTextResponse(_message.Message):
    __slots__ = ('moderation_categories', 'language_code', 'language_supported')
    MODERATION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    moderation_categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]
    language_code: str
    language_supported: bool

    def __init__(self, moderation_categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=..., language_code: _Optional[str]=..., language_supported: bool=...) -> None:
        ...

class AnnotateTextRequest(_message.Message):
    __slots__ = ('document', 'features', 'encoding_type')

    class Features(_message.Message):
        __slots__ = ('extract_entities', 'extract_document_sentiment', 'classify_text', 'moderate_text')
        EXTRACT_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        EXTRACT_DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        CLASSIFY_TEXT_FIELD_NUMBER: _ClassVar[int]
        MODERATE_TEXT_FIELD_NUMBER: _ClassVar[int]
        extract_entities: bool
        extract_document_sentiment: bool
        classify_text: bool
        moderate_text: bool

        def __init__(self, extract_entities: bool=..., extract_document_sentiment: bool=..., classify_text: bool=..., moderate_text: bool=...) -> None:
            ...
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    features: AnnotateTextRequest.Features
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., features: _Optional[_Union[AnnotateTextRequest.Features, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnnotateTextResponse(_message.Message):
    __slots__ = ('sentences', 'entities', 'document_sentiment', 'language_code', 'categories', 'moderation_categories', 'language_supported')
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    MODERATION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    document_sentiment: Sentiment
    language_code: str
    categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]
    moderation_categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]
    language_supported: bool

    def __init__(self, sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]]=..., entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., document_sentiment: _Optional[_Union[Sentiment, _Mapping]]=..., language_code: _Optional[str]=..., categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=..., moderation_categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=..., language_supported: bool=...) -> None:
        ...