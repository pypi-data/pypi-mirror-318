from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class BigQueryExportSettings(_message.Message):
    __slots__ = ('enabled', 'bigquery_table')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    bigquery_table: str

    def __init__(self, enabled: bool=..., bigquery_table: _Optional[str]=...) -> None:
        ...