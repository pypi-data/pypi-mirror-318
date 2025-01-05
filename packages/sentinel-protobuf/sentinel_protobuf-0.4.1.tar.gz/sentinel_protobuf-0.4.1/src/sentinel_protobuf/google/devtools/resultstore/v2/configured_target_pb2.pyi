from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConfiguredTarget(_message.Message):
    __slots__ = ('name', 'id', 'status_attributes', 'timing', 'test_attributes', 'properties', 'files')

    class Id(_message.Message):
        __slots__ = ('invocation_id', 'target_id', 'configuration_id')
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str
        target_id: str
        configuration_id: str

        def __init__(self, invocation_id: _Optional[str]=..., target_id: _Optional[str]=..., configuration_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    TEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: ConfiguredTarget.Id
    status_attributes: _common_pb2.StatusAttributes
    timing: _common_pb2.Timing
    test_attributes: ConfiguredTestAttributes
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[ConfiguredTarget.Id, _Mapping]]=..., status_attributes: _Optional[_Union[_common_pb2.StatusAttributes, _Mapping]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., test_attributes: _Optional[_Union[ConfiguredTestAttributes, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=...) -> None:
        ...

class ConfiguredTestAttributes(_message.Message):
    __slots__ = ('total_run_count', 'total_shard_count', 'timeout_duration')
    TOTAL_RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    total_run_count: int
    total_shard_count: int
    timeout_duration: _duration_pb2.Duration

    def __init__(self, total_run_count: _Optional[int]=..., total_shard_count: _Optional[int]=..., timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...