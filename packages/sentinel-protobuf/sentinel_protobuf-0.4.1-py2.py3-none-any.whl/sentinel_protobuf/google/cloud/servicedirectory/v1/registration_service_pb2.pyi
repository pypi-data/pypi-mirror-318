from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.servicedirectory.v1 import endpoint_pb2 as _endpoint_pb2
from google.cloud.servicedirectory.v1 import namespace_pb2 as _namespace_pb2
from google.cloud.servicedirectory.v1 import service_pb2 as _service_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateNamespaceRequest(_message.Message):
    __slots__ = ('parent', 'namespace_id', 'namespace')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    namespace_id: str
    namespace: _namespace_pb2.Namespace

    def __init__(self, parent: _Optional[str]=..., namespace_id: _Optional[str]=..., namespace: _Optional[_Union[_namespace_pb2.Namespace, _Mapping]]=...) -> None:
        ...

class ListNamespacesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListNamespacesResponse(_message.Message):
    __slots__ = ('namespaces', 'next_page_token')
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    namespaces: _containers.RepeatedCompositeFieldContainer[_namespace_pb2.Namespace]
    next_page_token: str

    def __init__(self, namespaces: _Optional[_Iterable[_Union[_namespace_pb2.Namespace, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetNamespaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateNamespaceRequest(_message.Message):
    __slots__ = ('namespace', 'update_mask')
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    namespace: _namespace_pb2.Namespace
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, namespace: _Optional[_Union[_namespace_pb2.Namespace, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteNamespaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceRequest(_message.Message):
    __slots__ = ('parent', 'service_id', 'service')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_id: str
    service: _service_pb2.Service

    def __init__(self, parent: _Optional[str]=..., service_id: _Optional[str]=..., service: _Optional[_Union[_service_pb2.Service, _Mapping]]=...) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    next_page_token: str

    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ('service', 'update_mask')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service: _service_pb2.Service
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEndpointRequest(_message.Message):
    __slots__ = ('parent', 'endpoint_id', 'endpoint')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    endpoint_id: str
    endpoint: _endpoint_pb2.Endpoint

    def __init__(self, parent: _Optional[str]=..., endpoint_id: _Optional[str]=..., endpoint: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]]=...) -> None:
        ...

class ListEndpointsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListEndpointsResponse(_message.Message):
    __slots__ = ('endpoints', 'next_page_token')
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.Endpoint]
    next_page_token: str

    def __init__(self, endpoints: _Optional[_Iterable[_Union[_endpoint_pb2.Endpoint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEndpointRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateEndpointRequest(_message.Message):
    __slots__ = ('endpoint', 'update_mask')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    endpoint: _endpoint_pb2.Endpoint
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, endpoint: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...