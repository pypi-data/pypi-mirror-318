from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceBinding(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'service', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    service: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., service: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListServiceBindingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServiceBindingsResponse(_message.Message):
    __slots__ = ('service_bindings', 'next_page_token')
    SERVICE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_bindings: _containers.RepeatedCompositeFieldContainer[ServiceBinding]
    next_page_token: str

    def __init__(self, service_bindings: _Optional[_Iterable[_Union[ServiceBinding, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetServiceBindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceBindingRequest(_message.Message):
    __slots__ = ('parent', 'service_binding_id', 'service_binding')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_BINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_binding_id: str
    service_binding: ServiceBinding

    def __init__(self, parent: _Optional[str]=..., service_binding_id: _Optional[str]=..., service_binding: _Optional[_Union[ServiceBinding, _Mapping]]=...) -> None:
        ...

class DeleteServiceBindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...