from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ExportEvaluatedDataItemsConfig(_message.Message):
    __slots__ = ('destination_bigquery_uri', 'override_existing_table')
    DESTINATION_BIGQUERY_URI_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_EXISTING_TABLE_FIELD_NUMBER: _ClassVar[int]
    destination_bigquery_uri: str
    override_existing_table: bool

    def __init__(self, destination_bigquery_uri: _Optional[str]=..., override_existing_table: bool=...) -> None:
        ...