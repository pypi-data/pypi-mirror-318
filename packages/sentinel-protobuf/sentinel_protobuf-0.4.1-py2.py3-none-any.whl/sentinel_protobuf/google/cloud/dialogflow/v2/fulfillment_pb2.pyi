from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Fulfillment(_message.Message):
    __slots__ = ('name', 'display_name', 'generic_web_service', 'enabled', 'features')

    class GenericWebService(_message.Message):
        __slots__ = ('uri', 'username', 'password', 'request_headers', 'is_cloud_function')

        class RequestHeadersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        URI_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
        IS_CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        uri: str
        username: str
        password: str
        request_headers: _containers.ScalarMap[str, str]
        is_cloud_function: bool

        def __init__(self, uri: _Optional[str]=..., username: _Optional[str]=..., password: _Optional[str]=..., request_headers: _Optional[_Mapping[str, str]]=..., is_cloud_function: bool=...) -> None:
            ...

    class Feature(_message.Message):
        __slots__ = ('type',)

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Fulfillment.Feature.Type]
            SMALLTALK: _ClassVar[Fulfillment.Feature.Type]
        TYPE_UNSPECIFIED: Fulfillment.Feature.Type
        SMALLTALK: Fulfillment.Feature.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: Fulfillment.Feature.Type

        def __init__(self, type: _Optional[_Union[Fulfillment.Feature.Type, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERIC_WEB_SERVICE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    generic_web_service: Fulfillment.GenericWebService
    enabled: bool
    features: _containers.RepeatedCompositeFieldContainer[Fulfillment.Feature]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., generic_web_service: _Optional[_Union[Fulfillment.GenericWebService, _Mapping]]=..., enabled: bool=..., features: _Optional[_Iterable[_Union[Fulfillment.Feature, _Mapping]]]=...) -> None:
        ...

class GetFulfillmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateFulfillmentRequest(_message.Message):
    __slots__ = ('fulfillment', 'update_mask')
    FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    fulfillment: Fulfillment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, fulfillment: _Optional[_Union[Fulfillment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...