from google.cloud.datacatalog.v1 import common_pb2 as _common_pb2
from google.cloud.datacatalog.v1 import physical_schema_pb2 as _physical_schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataplexSpec(_message.Message):
    __slots__ = ('asset', 'data_format', 'compression_format', 'project_id')
    ASSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    asset: str
    data_format: _physical_schema_pb2.PhysicalSchema
    compression_format: str
    project_id: str

    def __init__(self, asset: _Optional[str]=..., data_format: _Optional[_Union[_physical_schema_pb2.PhysicalSchema, _Mapping]]=..., compression_format: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class DataplexFilesetSpec(_message.Message):
    __slots__ = ('dataplex_spec',)
    DATAPLEX_SPEC_FIELD_NUMBER: _ClassVar[int]
    dataplex_spec: DataplexSpec

    def __init__(self, dataplex_spec: _Optional[_Union[DataplexSpec, _Mapping]]=...) -> None:
        ...

class DataplexTableSpec(_message.Message):
    __slots__ = ('external_tables', 'dataplex_spec', 'user_managed')
    EXTERNAL_TABLES_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_MANAGED_FIELD_NUMBER: _ClassVar[int]
    external_tables: _containers.RepeatedCompositeFieldContainer[DataplexExternalTable]
    dataplex_spec: DataplexSpec
    user_managed: bool

    def __init__(self, external_tables: _Optional[_Iterable[_Union[DataplexExternalTable, _Mapping]]]=..., dataplex_spec: _Optional[_Union[DataplexSpec, _Mapping]]=..., user_managed: bool=...) -> None:
        ...

class DataplexExternalTable(_message.Message):
    __slots__ = ('system', 'fully_qualified_name', 'google_cloud_resource', 'data_catalog_entry')
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CLOUD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_CATALOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
    system: _common_pb2.IntegratedSystem
    fully_qualified_name: str
    google_cloud_resource: str
    data_catalog_entry: str

    def __init__(self, system: _Optional[_Union[_common_pb2.IntegratedSystem, str]]=..., fully_qualified_name: _Optional[str]=..., google_cloud_resource: _Optional[str]=..., data_catalog_entry: _Optional[str]=...) -> None:
        ...