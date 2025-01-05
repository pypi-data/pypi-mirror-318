from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import flow_pb2 as _flow_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateVersionOperationMetadata(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str

    def __init__(self, version: _Optional[str]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'nlu_settings', 'create_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Version.State]
        RUNNING: _ClassVar[Version.State]
        SUCCEEDED: _ClassVar[Version.State]
        FAILED: _ClassVar[Version.State]
    STATE_UNSPECIFIED: Version.State
    RUNNING: Version.State
    SUCCEEDED: Version.State
    FAILED: Version.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NLU_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    nlu_settings: _flow_pb2.NluSettings
    create_time: _timestamp_pb2.Timestamp
    state: Version.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., nlu_settings: _Optional[_Union[_flow_pb2.NluSettings, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Version.State, str]]=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    version: Version

    def __init__(self, parent: _Optional[str]=..., version: _Optional[_Union[Version, _Mapping]]=...) -> None:
        ...

class UpdateVersionRequest(_message.Message):
    __slots__ = ('version', 'update_mask')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    version: Version
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, version: _Optional[_Union[Version, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LoadVersionRequest(_message.Message):
    __slots__ = ('name', 'allow_override_agent_resources')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_OVERRIDE_AGENT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_override_agent_resources: bool

    def __init__(self, name: _Optional[str]=..., allow_override_agent_resources: bool=...) -> None:
        ...

class CompareVersionsRequest(_message.Message):
    __slots__ = ('base_version', 'target_version', 'language_code')
    BASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    base_version: str
    target_version: str
    language_code: str

    def __init__(self, base_version: _Optional[str]=..., target_version: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class CompareVersionsResponse(_message.Message):
    __slots__ = ('base_version_content_json', 'target_version_content_json', 'compare_time')
    BASE_VERSION_CONTENT_JSON_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_CONTENT_JSON_FIELD_NUMBER: _ClassVar[int]
    COMPARE_TIME_FIELD_NUMBER: _ClassVar[int]
    base_version_content_json: str
    target_version_content_json: str
    compare_time: _timestamp_pb2.Timestamp

    def __init__(self, base_version_content_json: _Optional[str]=..., target_version_content_json: _Optional[str]=..., compare_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...