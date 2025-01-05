from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslationDetails(_message.Message):
    __slots__ = ('source_target_mapping', 'target_base_uri', 'source_environment', 'target_return_literals', 'target_types')
    SOURCE_TARGET_MAPPING_FIELD_NUMBER: _ClassVar[int]
    TARGET_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_RETURN_LITERALS_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    source_target_mapping: _containers.RepeatedCompositeFieldContainer[SourceTargetMapping]
    target_base_uri: str
    source_environment: SourceEnvironment
    target_return_literals: _containers.RepeatedScalarFieldContainer[str]
    target_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, source_target_mapping: _Optional[_Iterable[_Union[SourceTargetMapping, _Mapping]]]=..., target_base_uri: _Optional[str]=..., source_environment: _Optional[_Union[SourceEnvironment, _Mapping]]=..., target_return_literals: _Optional[_Iterable[str]]=..., target_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class SourceTargetMapping(_message.Message):
    __slots__ = ('source_spec', 'target_spec')
    SOURCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_SPEC_FIELD_NUMBER: _ClassVar[int]
    source_spec: SourceSpec
    target_spec: TargetSpec

    def __init__(self, source_spec: _Optional[_Union[SourceSpec, _Mapping]]=..., target_spec: _Optional[_Union[TargetSpec, _Mapping]]=...) -> None:
        ...

class SourceSpec(_message.Message):
    __slots__ = ('base_uri', 'literal', 'encoding')
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    LITERAL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    literal: Literal
    encoding: str

    def __init__(self, base_uri: _Optional[str]=..., literal: _Optional[_Union[Literal, _Mapping]]=..., encoding: _Optional[str]=...) -> None:
        ...

class TargetSpec(_message.Message):
    __slots__ = ('relative_path',)
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    relative_path: str

    def __init__(self, relative_path: _Optional[str]=...) -> None:
        ...

class Literal(_message.Message):
    __slots__ = ('literal_string', 'literal_bytes', 'relative_path')
    LITERAL_STRING_FIELD_NUMBER: _ClassVar[int]
    LITERAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    literal_string: str
    literal_bytes: bytes
    relative_path: str

    def __init__(self, literal_string: _Optional[str]=..., literal_bytes: _Optional[bytes]=..., relative_path: _Optional[str]=...) -> None:
        ...

class SourceEnvironment(_message.Message):
    __slots__ = ('default_database', 'schema_search_path', 'metadata_store_dataset')
    DEFAULT_DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_SEARCH_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_STORE_DATASET_FIELD_NUMBER: _ClassVar[int]
    default_database: str
    schema_search_path: _containers.RepeatedScalarFieldContainer[str]
    metadata_store_dataset: str

    def __init__(self, default_database: _Optional[str]=..., schema_search_path: _Optional[_Iterable[str]]=..., metadata_store_dataset: _Optional[str]=...) -> None:
        ...