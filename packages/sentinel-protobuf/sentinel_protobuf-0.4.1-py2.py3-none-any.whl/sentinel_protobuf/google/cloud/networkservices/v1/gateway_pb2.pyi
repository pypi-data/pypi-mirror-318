from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Gateway(_message.Message):
    __slots__ = ('name', 'self_link', 'create_time', 'update_time', 'labels', 'description', 'type', 'ports', 'scope', 'server_tls_policy')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Gateway.Type]
        OPEN_MESH: _ClassVar[Gateway.Type]
        SECURE_WEB_GATEWAY: _ClassVar[Gateway.Type]
    TYPE_UNSPECIFIED: Gateway.Type
    OPEN_MESH: Gateway.Type
    SECURE_WEB_GATEWAY: Gateway.Type

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TLS_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    self_link: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    type: Gateway.Type
    ports: _containers.RepeatedScalarFieldContainer[int]
    scope: str
    server_tls_policy: str

    def __init__(self, name: _Optional[str]=..., self_link: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., type: _Optional[_Union[Gateway.Type, str]]=..., ports: _Optional[_Iterable[int]]=..., scope: _Optional[str]=..., server_tls_policy: _Optional[str]=...) -> None:
        ...

class ListGatewaysRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListGatewaysResponse(_message.Message):
    __slots__ = ('gateways', 'next_page_token')
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gateways: _containers.RepeatedCompositeFieldContainer[Gateway]
    next_page_token: str

    def __init__(self, gateways: _Optional[_Iterable[_Union[Gateway, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ('parent', 'gateway_id', 'gateway')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gateway_id: str
    gateway: Gateway

    def __init__(self, parent: _Optional[str]=..., gateway_id: _Optional[str]=..., gateway: _Optional[_Union[Gateway, _Mapping]]=...) -> None:
        ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ('update_mask', 'gateway')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    gateway: Gateway

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., gateway: _Optional[_Union[Gateway, _Mapping]]=...) -> None:
        ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...