from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.vision.v1p3beta1 import geometry_pb2 as _geometry_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'product_category', 'product_labels')

    class KeyValue(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    product_category: str
    product_labels: _containers.RepeatedCompositeFieldContainer[Product.KeyValue]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., product_category: _Optional[str]=..., product_labels: _Optional[_Iterable[_Union[Product.KeyValue, _Mapping]]]=...) -> None:
        ...

class ProductSet(_message.Message):
    __slots__ = ('name', 'display_name', 'index_time', 'index_error')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    index_time: _timestamp_pb2.Timestamp
    index_error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., index_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., index_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ReferenceImage(_message.Message):
    __slots__ = ('name', 'uri', 'bounding_polys')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_POLYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    bounding_polys: _containers.RepeatedCompositeFieldContainer[_geometry_pb2.BoundingPoly]

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., bounding_polys: _Optional[_Iterable[_Union[_geometry_pb2.BoundingPoly, _Mapping]]]=...) -> None:
        ...

class CreateProductRequest(_message.Message):
    __slots__ = ('parent', 'product', 'product_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    product: Product
    product_id: str

    def __init__(self, parent: _Optional[str]=..., product: _Optional[_Union[Product, _Mapping]]=..., product_id: _Optional[str]=...) -> None:
        ...

class ListProductsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProductsResponse(_message.Message):
    __slots__ = ('products', 'next_page_token')
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    next_page_token: str

    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetProductRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateProductRequest(_message.Message):
    __slots__ = ('product', 'update_mask')
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    product: Product
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, product: _Optional[_Union[Product, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteProductRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateProductSetRequest(_message.Message):
    __slots__ = ('parent', 'product_set', 'product_set_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SET_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    product_set: ProductSet
    product_set_id: str

    def __init__(self, parent: _Optional[str]=..., product_set: _Optional[_Union[ProductSet, _Mapping]]=..., product_set_id: _Optional[str]=...) -> None:
        ...

class ListProductSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProductSetsResponse(_message.Message):
    __slots__ = ('product_sets', 'next_page_token')
    PRODUCT_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    product_sets: _containers.RepeatedCompositeFieldContainer[ProductSet]
    next_page_token: str

    def __init__(self, product_sets: _Optional[_Iterable[_Union[ProductSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetProductSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateProductSetRequest(_message.Message):
    __slots__ = ('product_set', 'update_mask')
    PRODUCT_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    product_set: ProductSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, product_set: _Optional[_Union[ProductSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteProductSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReferenceImageRequest(_message.Message):
    __slots__ = ('parent', 'reference_image', 'reference_image_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reference_image: ReferenceImage
    reference_image_id: str

    def __init__(self, parent: _Optional[str]=..., reference_image: _Optional[_Union[ReferenceImage, _Mapping]]=..., reference_image_id: _Optional[str]=...) -> None:
        ...

class ListReferenceImagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReferenceImagesResponse(_message.Message):
    __slots__ = ('reference_images', 'page_size', 'next_page_token')
    REFERENCE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reference_images: _containers.RepeatedCompositeFieldContainer[ReferenceImage]
    page_size: int
    next_page_token: str

    def __init__(self, reference_images: _Optional[_Iterable[_Union[ReferenceImage, _Mapping]]]=..., page_size: _Optional[int]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetReferenceImageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteReferenceImageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AddProductToProductSetRequest(_message.Message):
    __slots__ = ('name', 'product')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    name: str
    product: str

    def __init__(self, name: _Optional[str]=..., product: _Optional[str]=...) -> None:
        ...

class RemoveProductFromProductSetRequest(_message.Message):
    __slots__ = ('name', 'product')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    name: str
    product: str

    def __init__(self, name: _Optional[str]=..., product: _Optional[str]=...) -> None:
        ...

class ListProductsInProductSetRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProductsInProductSetResponse(_message.Message):
    __slots__ = ('products', 'next_page_token')
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    next_page_token: str

    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ImportProductSetsGcsSource(_message.Message):
    __slots__ = ('csv_file_uri',)
    CSV_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    csv_file_uri: str

    def __init__(self, csv_file_uri: _Optional[str]=...) -> None:
        ...

class ImportProductSetsInputConfig(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: ImportProductSetsGcsSource

    def __init__(self, gcs_source: _Optional[_Union[ImportProductSetsGcsSource, _Mapping]]=...) -> None:
        ...

class ImportProductSetsRequest(_message.Message):
    __slots__ = ('parent', 'input_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    input_config: ImportProductSetsInputConfig

    def __init__(self, parent: _Optional[str]=..., input_config: _Optional[_Union[ImportProductSetsInputConfig, _Mapping]]=...) -> None:
        ...

class ImportProductSetsResponse(_message.Message):
    __slots__ = ('reference_images', 'statuses')
    REFERENCE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    reference_images: _containers.RepeatedCompositeFieldContainer[ReferenceImage]
    statuses: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, reference_images: _Optional[_Iterable[_Union[ReferenceImage, _Mapping]]]=..., statuses: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class BatchOperationMetadata(_message.Message):
    __slots__ = ('state', 'submit_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchOperationMetadata.State]
        PROCESSING: _ClassVar[BatchOperationMetadata.State]
        SUCCESSFUL: _ClassVar[BatchOperationMetadata.State]
        FAILED: _ClassVar[BatchOperationMetadata.State]
        CANCELLED: _ClassVar[BatchOperationMetadata.State]
    STATE_UNSPECIFIED: BatchOperationMetadata.State
    PROCESSING: BatchOperationMetadata.State
    SUCCESSFUL: BatchOperationMetadata.State
    FAILED: BatchOperationMetadata.State
    CANCELLED: BatchOperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    state: BatchOperationMetadata.State
    submit_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[BatchOperationMetadata.State, str]]=..., submit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...