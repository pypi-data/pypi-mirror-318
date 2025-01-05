from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MetadataStore(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'encryption_spec', 'description', 'state', 'dataplex_config')

    class MetadataStoreState(_message.Message):
        __slots__ = ('disk_utilization_bytes',)
        DISK_UTILIZATION_BYTES_FIELD_NUMBER: _ClassVar[int]
        disk_utilization_bytes: int

        def __init__(self, disk_utilization_bytes: _Optional[int]=...) -> None:
            ...

    class DataplexConfig(_message.Message):
        __slots__ = ('enabled_pipelines_lineage',)
        ENABLED_PIPELINES_LINEAGE_FIELD_NUMBER: _ClassVar[int]
        enabled_pipelines_lineage: bool

        def __init__(self, enabled_pipelines_lineage: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    description: str
    state: MetadataStore.MetadataStoreState
    dataplex_config: MetadataStore.DataplexConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., description: _Optional[str]=..., state: _Optional[_Union[MetadataStore.MetadataStoreState, _Mapping]]=..., dataplex_config: _Optional[_Union[MetadataStore.DataplexConfig, _Mapping]]=...) -> None:
        ...