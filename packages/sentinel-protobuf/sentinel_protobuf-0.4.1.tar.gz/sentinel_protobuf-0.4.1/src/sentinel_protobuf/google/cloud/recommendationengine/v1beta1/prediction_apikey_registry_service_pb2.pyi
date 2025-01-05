from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.api import client_pb2 as _client_pb2
from google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as _recommendationengine_resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictionApiKeyRegistration(_message.Message):
    __slots__ = ('api_key',)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str

    def __init__(self, api_key: _Optional[str]=...) -> None:
        ...

class CreatePredictionApiKeyRegistrationRequest(_message.Message):
    __slots__ = ('parent', 'prediction_api_key_registration')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_API_KEY_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    prediction_api_key_registration: PredictionApiKeyRegistration

    def __init__(self, parent: _Optional[str]=..., prediction_api_key_registration: _Optional[_Union[PredictionApiKeyRegistration, _Mapping]]=...) -> None:
        ...

class ListPredictionApiKeyRegistrationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPredictionApiKeyRegistrationsResponse(_message.Message):
    __slots__ = ('prediction_api_key_registrations', 'next_page_token')
    PREDICTION_API_KEY_REGISTRATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    prediction_api_key_registrations: _containers.RepeatedCompositeFieldContainer[PredictionApiKeyRegistration]
    next_page_token: str

    def __init__(self, prediction_api_key_registrations: _Optional[_Iterable[_Union[PredictionApiKeyRegistration, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeletePredictionApiKeyRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...