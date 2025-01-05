from google.cloud.automl.v1 import classification_pb2 as _classification_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TextClassificationDatasetMetadata(_message.Message):
    __slots__ = ('classification_type',)
    CLASSIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    classification_type: _classification_pb2.ClassificationType

    def __init__(self, classification_type: _Optional[_Union[_classification_pb2.ClassificationType, str]]=...) -> None:
        ...

class TextClassificationModelMetadata(_message.Message):
    __slots__ = ('classification_type',)
    CLASSIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    classification_type: _classification_pb2.ClassificationType

    def __init__(self, classification_type: _Optional[_Union[_classification_pb2.ClassificationType, str]]=...) -> None:
        ...

class TextExtractionDatasetMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TextExtractionModelMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TextSentimentDatasetMetadata(_message.Message):
    __slots__ = ('sentiment_max',)
    SENTIMENT_MAX_FIELD_NUMBER: _ClassVar[int]
    sentiment_max: int

    def __init__(self, sentiment_max: _Optional[int]=...) -> None:
        ...

class TextSentimentModelMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...