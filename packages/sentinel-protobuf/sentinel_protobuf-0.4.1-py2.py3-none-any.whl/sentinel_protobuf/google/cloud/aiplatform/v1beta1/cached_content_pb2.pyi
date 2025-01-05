from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CachedContent(_message.Message):
    __slots__ = ("expire_time", "ttl", "name", "display_name", "model", "system_instruction", "contents", "tools", "tool_config", "create_time", "update_time", "usage_metadata")
    class UsageMetadata(_message.Message):
        __slots__ = ("total_token_count", "text_count", "image_count", "video_duration_seconds", "audio_duration_seconds")
        TOTAL_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        TEXT_COUNT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        VIDEO_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
        total_token_count: int
        text_count: int
        image_count: int
        video_duration_seconds: int
        audio_duration_seconds: int
        def __init__(self, total_token_count: _Optional[int] = ..., text_count: _Optional[int] = ..., image_count: _Optional[int] = ..., video_duration_seconds: _Optional[int] = ..., audio_duration_seconds: _Optional[int] = ...) -> None: ...
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    name: str
    display_name: str
    model: str
    system_instruction: _content_pb2.Content
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    tools: _containers.RepeatedCompositeFieldContainer[_tool_pb2.Tool]
    tool_config: _tool_pb2.ToolConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    usage_metadata: CachedContent.UsageMetadata
    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., model: _Optional[str] = ..., system_instruction: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[_tool_pb2.Tool, _Mapping]]] = ..., tool_config: _Optional[_Union[_tool_pb2.ToolConfig, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., usage_metadata: _Optional[_Union[CachedContent.UsageMetadata, _Mapping]] = ...) -> None: ...
