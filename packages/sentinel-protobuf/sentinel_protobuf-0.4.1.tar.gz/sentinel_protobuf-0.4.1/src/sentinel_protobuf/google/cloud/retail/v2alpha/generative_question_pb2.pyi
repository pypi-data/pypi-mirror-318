from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GenerativeQuestionsFeatureConfig(_message.Message):
    __slots__ = ('catalog', 'feature_enabled', 'minimum_products')
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    feature_enabled: bool
    minimum_products: int

    def __init__(self, catalog: _Optional[str]=..., feature_enabled: bool=..., minimum_products: _Optional[int]=...) -> None:
        ...

class GenerativeQuestionConfig(_message.Message):
    __slots__ = ('catalog', 'facet', 'generated_question', 'final_question', 'example_values', 'frequency', 'allowed_in_conversation')
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    FACET_FIELD_NUMBER: _ClassVar[int]
    GENERATED_QUESTION_FIELD_NUMBER: _ClassVar[int]
    FINAL_QUESTION_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IN_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    facet: str
    generated_question: str
    final_question: str
    example_values: _containers.RepeatedScalarFieldContainer[str]
    frequency: float
    allowed_in_conversation: bool

    def __init__(self, catalog: _Optional[str]=..., facet: _Optional[str]=..., generated_question: _Optional[str]=..., final_question: _Optional[str]=..., example_values: _Optional[_Iterable[str]]=..., frequency: _Optional[float]=..., allowed_in_conversation: bool=...) -> None:
        ...