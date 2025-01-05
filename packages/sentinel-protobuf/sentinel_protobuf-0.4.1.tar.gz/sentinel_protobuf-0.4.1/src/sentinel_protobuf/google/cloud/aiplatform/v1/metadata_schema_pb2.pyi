from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MetadataSchema(_message.Message):
    __slots__ = ('name', 'schema_version', 'schema', 'schema_type', 'create_time', 'description')

    class MetadataSchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METADATA_SCHEMA_TYPE_UNSPECIFIED: _ClassVar[MetadataSchema.MetadataSchemaType]
        ARTIFACT_TYPE: _ClassVar[MetadataSchema.MetadataSchemaType]
        EXECUTION_TYPE: _ClassVar[MetadataSchema.MetadataSchemaType]
        CONTEXT_TYPE: _ClassVar[MetadataSchema.MetadataSchemaType]
    METADATA_SCHEMA_TYPE_UNSPECIFIED: MetadataSchema.MetadataSchemaType
    ARTIFACT_TYPE: MetadataSchema.MetadataSchemaType
    EXECUTION_TYPE: MetadataSchema.MetadataSchemaType
    CONTEXT_TYPE: MetadataSchema.MetadataSchemaType
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema_version: str
    schema: str
    schema_type: MetadataSchema.MetadataSchemaType
    create_time: _timestamp_pb2.Timestamp
    description: str

    def __init__(self, name: _Optional[str]=..., schema_version: _Optional[str]=..., schema: _Optional[str]=..., schema_type: _Optional[_Union[MetadataSchema.MetadataSchemaType, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...