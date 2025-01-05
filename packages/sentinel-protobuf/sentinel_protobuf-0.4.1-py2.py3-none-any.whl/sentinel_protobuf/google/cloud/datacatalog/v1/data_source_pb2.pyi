from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataSource(_message.Message):
    __slots__ = ('service', 'resource', 'source_entry', 'storage_properties')

    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_UNSPECIFIED: _ClassVar[DataSource.Service]
        CLOUD_STORAGE: _ClassVar[DataSource.Service]
        BIGQUERY: _ClassVar[DataSource.Service]
    SERVICE_UNSPECIFIED: DataSource.Service
    CLOUD_STORAGE: DataSource.Service
    BIGQUERY: DataSource.Service
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    service: DataSource.Service
    resource: str
    source_entry: str
    storage_properties: StorageProperties

    def __init__(self, service: _Optional[_Union[DataSource.Service, str]]=..., resource: _Optional[str]=..., source_entry: _Optional[str]=..., storage_properties: _Optional[_Union[StorageProperties, _Mapping]]=...) -> None:
        ...

class StorageProperties(_message.Message):
    __slots__ = ('file_pattern', 'file_type')
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    file_pattern: _containers.RepeatedScalarFieldContainer[str]
    file_type: str

    def __init__(self, file_pattern: _Optional[_Iterable[str]]=..., file_type: _Optional[str]=...) -> None:
        ...