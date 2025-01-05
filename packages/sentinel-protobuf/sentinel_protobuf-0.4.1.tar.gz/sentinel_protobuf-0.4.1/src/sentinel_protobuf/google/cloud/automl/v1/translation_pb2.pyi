from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.automl.v1 import data_items_pb2 as _data_items_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslationDatasetMetadata(_message.Message):
    __slots__ = ('source_language_code', 'target_language_code')
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    source_language_code: str
    target_language_code: str

    def __init__(self, source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=...) -> None:
        ...

class TranslationEvaluationMetrics(_message.Message):
    __slots__ = ('bleu_score', 'base_bleu_score')
    BLEU_SCORE_FIELD_NUMBER: _ClassVar[int]
    BASE_BLEU_SCORE_FIELD_NUMBER: _ClassVar[int]
    bleu_score: float
    base_bleu_score: float

    def __init__(self, bleu_score: _Optional[float]=..., base_bleu_score: _Optional[float]=...) -> None:
        ...

class TranslationModelMetadata(_message.Message):
    __slots__ = ('base_model', 'source_language_code', 'target_language_code')
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    source_language_code: str
    target_language_code: str

    def __init__(self, base_model: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=...) -> None:
        ...

class TranslationAnnotation(_message.Message):
    __slots__ = ('translated_content',)
    TRANSLATED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    translated_content: _data_items_pb2.TextSnippet

    def __init__(self, translated_content: _Optional[_Union[_data_items_pb2.TextSnippet, _Mapping]]=...) -> None:
        ...