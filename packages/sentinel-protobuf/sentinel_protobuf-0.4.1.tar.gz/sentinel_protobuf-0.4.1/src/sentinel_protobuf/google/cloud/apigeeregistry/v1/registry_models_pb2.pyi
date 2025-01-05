from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Api(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'availability', 'recommended_version', 'recommended_deployment', 'labels', 'annotations')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_VERSION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    availability: str
    recommended_version: str
    recommended_deployment: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., availability: _Optional[str]=..., recommended_version: _Optional[str]=..., recommended_deployment: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ApiVersion(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'state', 'labels', 'annotations')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ApiSpec(_message.Message):
    __slots__ = ('name', 'filename', 'description', 'revision_id', 'create_time', 'revision_create_time', 'revision_update_time', 'mime_type', 'size_bytes', 'hash', 'source_uri', 'contents', 'labels', 'annotations')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename: str
    description: str
    revision_id: str
    create_time: _timestamp_pb2.Timestamp
    revision_create_time: _timestamp_pb2.Timestamp
    revision_update_time: _timestamp_pb2.Timestamp
    mime_type: str
    size_bytes: int
    hash: str
    source_uri: str
    contents: bytes
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., filename: _Optional[str]=..., description: _Optional[str]=..., revision_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=..., hash: _Optional[str]=..., source_uri: _Optional[str]=..., contents: _Optional[bytes]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ApiDeployment(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'revision_id', 'create_time', 'revision_create_time', 'revision_update_time', 'api_spec_revision', 'endpoint_uri', 'external_channel_uri', 'intended_audience', 'access_guidance', 'labels', 'annotations')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    API_SPEC_REVISION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_URI_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CHANNEL_URI_FIELD_NUMBER: _ClassVar[int]
    INTENDED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    revision_id: str
    create_time: _timestamp_pb2.Timestamp
    revision_create_time: _timestamp_pb2.Timestamp
    revision_update_time: _timestamp_pb2.Timestamp
    api_spec_revision: str
    endpoint_uri: str
    external_channel_uri: str
    intended_audience: str
    access_guidance: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., revision_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., api_spec_revision: _Optional[str]=..., endpoint_uri: _Optional[str]=..., external_channel_uri: _Optional[str]=..., intended_audience: _Optional[str]=..., access_guidance: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Artifact(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'mime_type', 'size_bytes', 'hash', 'contents')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    mime_type: str
    size_bytes: int
    hash: str
    contents: bytes

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=..., hash: _Optional[str]=..., contents: _Optional[bytes]=...) -> None:
        ...