from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetProtectedResourcesSummaryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ProtectedResourcesSummary(_message.Message):
    __slots__ = ('name', 'resource_count', 'project_count', 'resource_types', 'cloud_products', 'locations')

    class ResourceTypesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...

    class CloudProductsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...

    class LocationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_count: int
    project_count: int
    resource_types: _containers.ScalarMap[str, int]
    cloud_products: _containers.ScalarMap[str, int]
    locations: _containers.ScalarMap[str, int]

    def __init__(self, name: _Optional[str]=..., resource_count: _Optional[int]=..., project_count: _Optional[int]=..., resource_types: _Optional[_Mapping[str, int]]=..., cloud_products: _Optional[_Mapping[str, int]]=..., locations: _Optional[_Mapping[str, int]]=...) -> None:
        ...

class SearchProtectedResourcesRequest(_message.Message):
    __slots__ = ('scope', 'crypto_key', 'page_size', 'page_token', 'resource_types')
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    scope: str
    crypto_key: str
    page_size: int
    page_token: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, scope: _Optional[str]=..., crypto_key: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., resource_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class SearchProtectedResourcesResponse(_message.Message):
    __slots__ = ('protected_resources', 'next_page_token')
    PROTECTED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    protected_resources: _containers.RepeatedCompositeFieldContainer[ProtectedResource]
    next_page_token: str

    def __init__(self, protected_resources: _Optional[_Iterable[_Union[ProtectedResource, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ProtectedResource(_message.Message):
    __slots__ = ('name', 'project', 'project_id', 'cloud_product', 'resource_type', 'location', 'labels', 'crypto_key_version', 'crypto_key_versions', 'create_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    project_id: str
    cloud_product: str
    resource_type: str
    location: str
    labels: _containers.ScalarMap[str, str]
    crypto_key_version: str
    crypto_key_versions: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., project: _Optional[str]=..., project_id: _Optional[str]=..., cloud_product: _Optional[str]=..., resource_type: _Optional[str]=..., location: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., crypto_key_version: _Optional[str]=..., crypto_key_versions: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...