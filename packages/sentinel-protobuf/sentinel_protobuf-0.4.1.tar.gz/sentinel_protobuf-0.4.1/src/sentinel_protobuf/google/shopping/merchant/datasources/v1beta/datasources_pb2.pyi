from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.merchant.datasources.v1beta import datasourcetypes_pb2 as _datasourcetypes_pb2
from google.shopping.merchant.datasources.v1beta import fileinputs_pb2 as _fileinputs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataSource(_message.Message):
    __slots__ = ("primary_product_data_source", "supplemental_product_data_source", "local_inventory_data_source", "regional_inventory_data_source", "promotion_data_source", "name", "data_source_id", "display_name", "input", "file_input")
    class Input(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INPUT_UNSPECIFIED: _ClassVar[DataSource.Input]
        API: _ClassVar[DataSource.Input]
        FILE: _ClassVar[DataSource.Input]
        UI: _ClassVar[DataSource.Input]
        AUTOFEED: _ClassVar[DataSource.Input]
    INPUT_UNSPECIFIED: DataSource.Input
    API: DataSource.Input
    FILE: DataSource.Input
    UI: DataSource.Input
    AUTOFEED: DataSource.Input
    PRIMARY_PRODUCT_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_PRODUCT_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORY_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_INVENTORY_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    FILE_INPUT_FIELD_NUMBER: _ClassVar[int]
    primary_product_data_source: _datasourcetypes_pb2.PrimaryProductDataSource
    supplemental_product_data_source: _datasourcetypes_pb2.SupplementalProductDataSource
    local_inventory_data_source: _datasourcetypes_pb2.LocalInventoryDataSource
    regional_inventory_data_source: _datasourcetypes_pb2.RegionalInventoryDataSource
    promotion_data_source: _datasourcetypes_pb2.PromotionDataSource
    name: str
    data_source_id: int
    display_name: str
    input: DataSource.Input
    file_input: _fileinputs_pb2.FileInput
    def __init__(self, primary_product_data_source: _Optional[_Union[_datasourcetypes_pb2.PrimaryProductDataSource, _Mapping]] = ..., supplemental_product_data_source: _Optional[_Union[_datasourcetypes_pb2.SupplementalProductDataSource, _Mapping]] = ..., local_inventory_data_source: _Optional[_Union[_datasourcetypes_pb2.LocalInventoryDataSource, _Mapping]] = ..., regional_inventory_data_source: _Optional[_Union[_datasourcetypes_pb2.RegionalInventoryDataSource, _Mapping]] = ..., promotion_data_source: _Optional[_Union[_datasourcetypes_pb2.PromotionDataSource, _Mapping]] = ..., name: _Optional[str] = ..., data_source_id: _Optional[int] = ..., display_name: _Optional[str] = ..., input: _Optional[_Union[DataSource.Input, str]] = ..., file_input: _Optional[_Union[_fileinputs_pb2.FileInput, _Mapping]] = ...) -> None: ...

class GetDataSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataSourcesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDataSourcesResponse(_message.Message):
    __slots__ = ("data_sources", "next_page_token")
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    next_page_token: str
    def __init__(self, data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateDataSourceRequest(_message.Message):
    __slots__ = ("parent", "data_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_source: DataSource
    def __init__(self, parent: _Optional[str] = ..., data_source: _Optional[_Union[DataSource, _Mapping]] = ...) -> None: ...

class UpdateDataSourceRequest(_message.Message):
    __slots__ = ("data_source", "update_mask")
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_source: DataSource
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_source: _Optional[_Union[DataSource, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class FetchDataSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteDataSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
