from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RecommenderConfig(_message.Message):
    __slots__ = ('name', 'recommender_generation_config', 'etag', 'update_time', 'revision_id', 'annotations', 'display_name')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDER_GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    recommender_generation_config: RecommenderGenerationConfig
    etag: str
    update_time: _timestamp_pb2.Timestamp
    revision_id: str
    annotations: _containers.ScalarMap[str, str]
    display_name: str

    def __init__(self, name: _Optional[str]=..., recommender_generation_config: _Optional[_Union[RecommenderGenerationConfig, _Mapping]]=..., etag: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_id: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=...) -> None:
        ...

class RecommenderGenerationConfig(_message.Message):
    __slots__ = ('params',)
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _struct_pb2.Struct

    def __init__(self, params: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...