from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetRuntimeConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RuntimeConfig(_message.Message):
    __slots__ = ('location_id', 'connd_topic', 'connd_subscription', 'control_plane_topic', 'control_plane_subscription', 'runtime_endpoint', 'state', 'schema_gcs_bucket', 'service_directory', 'name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RuntimeConfig.State]
        INACTIVE: _ClassVar[RuntimeConfig.State]
        ACTIVATING: _ClassVar[RuntimeConfig.State]
        ACTIVE: _ClassVar[RuntimeConfig.State]
        CREATING: _ClassVar[RuntimeConfig.State]
        DELETING: _ClassVar[RuntimeConfig.State]
        UPDATING: _ClassVar[RuntimeConfig.State]
    STATE_UNSPECIFIED: RuntimeConfig.State
    INACTIVE: RuntimeConfig.State
    ACTIVATING: RuntimeConfig.State
    ACTIVE: RuntimeConfig.State
    CREATING: RuntimeConfig.State
    DELETING: RuntimeConfig.State
    UPDATING: RuntimeConfig.State
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONND_TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONND_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    location_id: str
    connd_topic: str
    connd_subscription: str
    control_plane_topic: str
    control_plane_subscription: str
    runtime_endpoint: str
    state: RuntimeConfig.State
    schema_gcs_bucket: str
    service_directory: str
    name: str

    def __init__(self, location_id: _Optional[str]=..., connd_topic: _Optional[str]=..., connd_subscription: _Optional[str]=..., control_plane_topic: _Optional[str]=..., control_plane_subscription: _Optional[str]=..., runtime_endpoint: _Optional[str]=..., state: _Optional[_Union[RuntimeConfig.State, str]]=..., schema_gcs_bucket: _Optional[str]=..., service_directory: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...