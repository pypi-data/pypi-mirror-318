from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROFILE_TYPE_UNSPECIFIED: _ClassVar[ProfileType]
    CPU: _ClassVar[ProfileType]
    WALL: _ClassVar[ProfileType]
    HEAP: _ClassVar[ProfileType]
    THREADS: _ClassVar[ProfileType]
    CONTENTION: _ClassVar[ProfileType]
    PEAK_HEAP: _ClassVar[ProfileType]
    HEAP_ALLOC: _ClassVar[ProfileType]
PROFILE_TYPE_UNSPECIFIED: ProfileType
CPU: ProfileType
WALL: ProfileType
HEAP: ProfileType
THREADS: ProfileType
CONTENTION: ProfileType
PEAK_HEAP: ProfileType
HEAP_ALLOC: ProfileType

class CreateProfileRequest(_message.Message):
    __slots__ = ('parent', 'deployment', 'profile_type')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment: Deployment
    profile_type: _containers.RepeatedScalarFieldContainer[ProfileType]

    def __init__(self, parent: _Optional[str]=..., deployment: _Optional[_Union[Deployment, _Mapping]]=..., profile_type: _Optional[_Iterable[_Union[ProfileType, str]]]=...) -> None:
        ...

class CreateOfflineProfileRequest(_message.Message):
    __slots__ = ('parent', 'profile')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    profile: Profile

    def __init__(self, parent: _Optional[str]=..., profile: _Optional[_Union[Profile, _Mapping]]=...) -> None:
        ...

class UpdateProfileRequest(_message.Message):
    __slots__ = ('profile', 'update_mask')
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    profile: Profile
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, profile: _Optional[_Union[Profile, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Profile(_message.Message):
    __slots__ = ('name', 'profile_type', 'deployment', 'duration', 'profile_bytes', 'labels', 'start_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    profile_type: ProfileType
    deployment: Deployment
    duration: _duration_pb2.Duration
    profile_bytes: bytes
    labels: _containers.ScalarMap[str, str]
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., profile_type: _Optional[_Union[ProfileType, str]]=..., deployment: _Optional[_Union[Deployment, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., profile_bytes: _Optional[bytes]=..., labels: _Optional[_Mapping[str, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ('project_id', 'target', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    target: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, project_id: _Optional[str]=..., target: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListProfilesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProfilesResponse(_message.Message):
    __slots__ = ('profiles', 'next_page_token', 'skipped_profiles')
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_PROFILES_FIELD_NUMBER: _ClassVar[int]
    profiles: _containers.RepeatedCompositeFieldContainer[Profile]
    next_page_token: str
    skipped_profiles: int

    def __init__(self, profiles: _Optional[_Iterable[_Union[Profile, _Mapping]]]=..., next_page_token: _Optional[str]=..., skipped_profiles: _Optional[int]=...) -> None:
        ...