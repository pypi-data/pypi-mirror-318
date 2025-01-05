from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import publisher_model_pb2 as _publisher_model_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublisherModelView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLISHER_MODEL_VIEW_UNSPECIFIED: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VIEW_BASIC: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VIEW_FULL: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VERSION_VIEW_BASIC: _ClassVar[PublisherModelView]
PUBLISHER_MODEL_VIEW_UNSPECIFIED: PublisherModelView
PUBLISHER_MODEL_VIEW_BASIC: PublisherModelView
PUBLISHER_MODEL_VIEW_FULL: PublisherModelView
PUBLISHER_MODEL_VERSION_VIEW_BASIC: PublisherModelView

class GetPublisherModelRequest(_message.Message):
    __slots__ = ("name", "language_code", "view", "is_hugging_face_model", "hugging_face_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_HUGGING_FACE_MODEL_FIELD_NUMBER: _ClassVar[int]
    HUGGING_FACE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    view: PublisherModelView
    is_hugging_face_model: bool
    hugging_face_token: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ..., view: _Optional[_Union[PublisherModelView, str]] = ..., is_hugging_face_model: bool = ..., hugging_face_token: _Optional[str] = ...) -> None: ...
