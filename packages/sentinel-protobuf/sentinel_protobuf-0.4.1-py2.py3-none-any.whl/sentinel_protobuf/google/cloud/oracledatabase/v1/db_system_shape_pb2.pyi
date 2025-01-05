from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DbSystemShape(_message.Message):
    __slots__ = ('name', 'shape', 'min_node_count', 'max_node_count', 'min_storage_count', 'max_storage_count', 'available_core_count_per_node', 'available_memory_per_node_gb', 'available_data_storage_tb', 'min_core_count_per_node', 'min_memory_per_node_gb', 'min_db_node_storage_per_node_gb')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_STORAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_STORAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_CORE_COUNT_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MEMORY_PER_NODE_GB_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DATA_STORAGE_TB_FIELD_NUMBER: _ClassVar[int]
    MIN_CORE_COUNT_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    MIN_MEMORY_PER_NODE_GB_FIELD_NUMBER: _ClassVar[int]
    MIN_DB_NODE_STORAGE_PER_NODE_GB_FIELD_NUMBER: _ClassVar[int]
    name: str
    shape: str
    min_node_count: int
    max_node_count: int
    min_storage_count: int
    max_storage_count: int
    available_core_count_per_node: int
    available_memory_per_node_gb: int
    available_data_storage_tb: int
    min_core_count_per_node: int
    min_memory_per_node_gb: int
    min_db_node_storage_per_node_gb: int

    def __init__(self, name: _Optional[str]=..., shape: _Optional[str]=..., min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=..., min_storage_count: _Optional[int]=..., max_storage_count: _Optional[int]=..., available_core_count_per_node: _Optional[int]=..., available_memory_per_node_gb: _Optional[int]=..., available_data_storage_tb: _Optional[int]=..., min_core_count_per_node: _Optional[int]=..., min_memory_per_node_gb: _Optional[int]=..., min_db_node_storage_per_node_gb: _Optional[int]=...) -> None:
        ...