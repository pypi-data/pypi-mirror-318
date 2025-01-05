from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BigLakeConfiguration(_message.Message):
    __slots__ = ('connection_id', 'storage_uri', 'file_format', 'table_format')

    class FileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_FORMAT_UNSPECIFIED: _ClassVar[BigLakeConfiguration.FileFormat]
        PARQUET: _ClassVar[BigLakeConfiguration.FileFormat]
    FILE_FORMAT_UNSPECIFIED: BigLakeConfiguration.FileFormat
    PARQUET: BigLakeConfiguration.FileFormat

    class TableFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TABLE_FORMAT_UNSPECIFIED: _ClassVar[BigLakeConfiguration.TableFormat]
        ICEBERG: _ClassVar[BigLakeConfiguration.TableFormat]
    TABLE_FORMAT_UNSPECIFIED: BigLakeConfiguration.TableFormat
    ICEBERG: BigLakeConfiguration.TableFormat
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TABLE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    storage_uri: str
    file_format: BigLakeConfiguration.FileFormat
    table_format: BigLakeConfiguration.TableFormat

    def __init__(self, connection_id: _Optional[str]=..., storage_uri: _Optional[str]=..., file_format: _Optional[_Union[BigLakeConfiguration.FileFormat, str]]=..., table_format: _Optional[_Union[BigLakeConfiguration.TableFormat, str]]=...) -> None:
        ...