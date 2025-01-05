from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import security_pb2 as _security_pb2
from google.cloud.dataplex.v1 import service_pb2 as _service_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataTaxonomy(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'attribute_count', 'etag', 'class_count')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CLASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    attribute_count: int
    etag: str
    class_count: int

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., attribute_count: _Optional[int]=..., etag: _Optional[str]=..., class_count: _Optional[int]=...) -> None:
        ...

class DataAttribute(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'parent_id', 'attribute_count', 'etag', 'resource_access_spec', 'data_access_spec')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ACCESS_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_ACCESS_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    parent_id: str
    attribute_count: int
    etag: str
    resource_access_spec: _security_pb2.ResourceAccessSpec
    data_access_spec: _security_pb2.DataAccessSpec

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., parent_id: _Optional[str]=..., attribute_count: _Optional[int]=..., etag: _Optional[str]=..., resource_access_spec: _Optional[_Union[_security_pb2.ResourceAccessSpec, _Mapping]]=..., data_access_spec: _Optional[_Union[_security_pb2.DataAccessSpec, _Mapping]]=...) -> None:
        ...

class DataAttributeBinding(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'etag', 'resource', 'attributes', 'paths')

    class Path(_message.Message):
        __slots__ = ('name', 'attributes')
        NAME_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        name: str
        attributes: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, name: _Optional[str]=..., attributes: _Optional[_Iterable[str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    etag: str
    resource: str
    attributes: _containers.RepeatedScalarFieldContainer[str]
    paths: _containers.RepeatedCompositeFieldContainer[DataAttributeBinding.Path]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., resource: _Optional[str]=..., attributes: _Optional[_Iterable[str]]=..., paths: _Optional[_Iterable[_Union[DataAttributeBinding.Path, _Mapping]]]=...) -> None:
        ...

class CreateDataTaxonomyRequest(_message.Message):
    __slots__ = ('parent', 'data_taxonomy_id', 'data_taxonomy', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_TAXONOMY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_taxonomy_id: str
    data_taxonomy: DataTaxonomy
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., data_taxonomy_id: _Optional[str]=..., data_taxonomy: _Optional[_Union[DataTaxonomy, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateDataTaxonomyRequest(_message.Message):
    __slots__ = ('update_mask', 'data_taxonomy', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_taxonomy: DataTaxonomy
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_taxonomy: _Optional[_Union[DataTaxonomy, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetDataTaxonomyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataTaxonomiesRequest(_message.Message):
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

class ListDataTaxonomiesResponse(_message.Message):
    __slots__ = ('data_taxonomies', 'next_page_token', 'unreachable_locations')
    DATA_TAXONOMIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    data_taxonomies: _containers.RepeatedCompositeFieldContainer[DataTaxonomy]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, data_taxonomies: _Optional[_Iterable[_Union[DataTaxonomy, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteDataTaxonomyRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateDataAttributeRequest(_message.Message):
    __slots__ = ('parent', 'data_attribute_id', 'data_attribute', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_attribute_id: str
    data_attribute: DataAttribute
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., data_attribute_id: _Optional[str]=..., data_attribute: _Optional[_Union[DataAttribute, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateDataAttributeRequest(_message.Message):
    __slots__ = ('update_mask', 'data_attribute', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_attribute: DataAttribute
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_attribute: _Optional[_Union[DataAttribute, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetDataAttributeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataAttributesRequest(_message.Message):
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

class ListDataAttributesResponse(_message.Message):
    __slots__ = ('data_attributes', 'next_page_token', 'unreachable_locations')
    DATA_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    data_attributes: _containers.RepeatedCompositeFieldContainer[DataAttribute]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, data_attributes: _Optional[_Iterable[_Union[DataAttribute, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteDataAttributeRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CreateDataAttributeBindingRequest(_message.Message):
    __slots__ = ('parent', 'data_attribute_binding_id', 'data_attribute_binding', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_BINDING_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_BINDING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_attribute_binding_id: str
    data_attribute_binding: DataAttributeBinding
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., data_attribute_binding_id: _Optional[str]=..., data_attribute_binding: _Optional[_Union[DataAttributeBinding, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateDataAttributeBindingRequest(_message.Message):
    __slots__ = ('update_mask', 'data_attribute_binding', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_ATTRIBUTE_BINDING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_attribute_binding: DataAttributeBinding
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_attribute_binding: _Optional[_Union[DataAttributeBinding, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class GetDataAttributeBindingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataAttributeBindingsRequest(_message.Message):
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

class ListDataAttributeBindingsResponse(_message.Message):
    __slots__ = ('data_attribute_bindings', 'next_page_token', 'unreachable_locations')
    DATA_ATTRIBUTE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    data_attribute_bindings: _containers.RepeatedCompositeFieldContainer[DataAttributeBinding]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, data_attribute_bindings: _Optional[_Iterable[_Union[DataAttributeBinding, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteDataAttributeBindingRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...