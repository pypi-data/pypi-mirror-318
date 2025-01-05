from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import generative_question_pb2 as _generative_question_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateGenerativeQuestionsFeatureConfigRequest(_message.Message):
    __slots__ = ('generative_questions_feature_config', 'update_mask')
    GENERATIVE_QUESTIONS_FEATURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    generative_questions_feature_config: _generative_question_pb2.GenerativeQuestionsFeatureConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, generative_questions_feature_config: _Optional[_Union[_generative_question_pb2.GenerativeQuestionsFeatureConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetGenerativeQuestionsFeatureConfigRequest(_message.Message):
    __slots__ = ('catalog',)
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    catalog: str

    def __init__(self, catalog: _Optional[str]=...) -> None:
        ...

class ListGenerativeQuestionConfigsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListGenerativeQuestionConfigsResponse(_message.Message):
    __slots__ = ('generative_question_configs',)
    GENERATIVE_QUESTION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    generative_question_configs: _containers.RepeatedCompositeFieldContainer[_generative_question_pb2.GenerativeQuestionConfig]

    def __init__(self, generative_question_configs: _Optional[_Iterable[_Union[_generative_question_pb2.GenerativeQuestionConfig, _Mapping]]]=...) -> None:
        ...

class UpdateGenerativeQuestionConfigRequest(_message.Message):
    __slots__ = ('generative_question_config', 'update_mask')
    GENERATIVE_QUESTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    generative_question_config: _generative_question_pb2.GenerativeQuestionConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, generative_question_config: _Optional[_Union[_generative_question_pb2.GenerativeQuestionConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchUpdateGenerativeQuestionConfigsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateGenerativeQuestionConfigRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateGenerativeQuestionConfigRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateGenerativeQuestionConfigsResponse(_message.Message):
    __slots__ = ('generative_question_configs',)
    GENERATIVE_QUESTION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    generative_question_configs: _containers.RepeatedCompositeFieldContainer[_generative_question_pb2.GenerativeQuestionConfig]

    def __init__(self, generative_question_configs: _Optional[_Iterable[_Union[_generative_question_pb2.GenerativeQuestionConfig, _Mapping]]]=...) -> None:
        ...