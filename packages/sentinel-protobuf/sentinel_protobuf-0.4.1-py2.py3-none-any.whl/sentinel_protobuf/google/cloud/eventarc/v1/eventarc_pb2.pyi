from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.eventarc.v1 import channel_pb2 as _channel_pb2
from google.cloud.eventarc.v1 import channel_connection_pb2 as _channel_connection_pb2
from google.cloud.eventarc.v1 import discovery_pb2 as _discovery_pb2
from google.cloud.eventarc.v1 import enrollment_pb2 as _enrollment_pb2
from google.cloud.eventarc.v1 import google_api_source_pb2 as _google_api_source_pb2
from google.cloud.eventarc.v1 import google_channel_config_pb2 as _google_channel_config_pb2
from google.cloud.eventarc.v1 import message_bus_pb2 as _message_bus_pb2
from google.cloud.eventarc.v1 import pipeline_pb2 as _pipeline_pb2
from google.cloud.eventarc.v1 import trigger_pb2 as _trigger_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetTriggerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTriggersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListTriggersResponse(_message.Message):
    __slots__ = ('triggers', 'next_page_token', 'unreachable')
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    triggers: _containers.RepeatedCompositeFieldContainer[_trigger_pb2.Trigger]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, triggers: _Optional[_Iterable[_Union[_trigger_pb2.Trigger, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateTriggerRequest(_message.Message):
    __slots__ = ('parent', 'trigger', 'trigger_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    trigger: _trigger_pb2.Trigger
    trigger_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., trigger: _Optional[_Union[_trigger_pb2.Trigger, _Mapping]]=..., trigger_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateTriggerRequest(_message.Message):
    __slots__ = ('trigger', 'update_mask', 'allow_missing', 'validate_only')
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    trigger: _trigger_pb2.Trigger
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    validate_only: bool

    def __init__(self, trigger: _Optional[_Union[_trigger_pb2.Trigger, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteTriggerRequest(_message.Message):
    __slots__ = ('name', 'etag', 'allow_missing', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class GetChannelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListChannelsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListChannelsResponse(_message.Message):
    __slots__ = ('channels', 'next_page_token', 'unreachable')
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateChannelRequest(_message.Message):
    __slots__ = ('parent', 'channel', 'channel_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    channel: _channel_pb2.Channel
    channel_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]]=..., channel_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateChannelRequest(_message.Message):
    __slots__ = ('channel', 'update_mask', 'validate_only')
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    channel: _channel_pb2.Channel
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteChannelRequest(_message.Message):
    __slots__ = ('name', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class GetProviderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListProvidersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListProvidersResponse(_message.Message):
    __slots__ = ('providers', 'next_page_token', 'unreachable')
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[_discovery_pb2.Provider]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, providers: _Optional[_Iterable[_Union[_discovery_pb2.Provider, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetChannelConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListChannelConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListChannelConnectionsResponse(_message.Message):
    __slots__ = ('channel_connections', 'next_page_token', 'unreachable')
    CHANNEL_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    channel_connections: _containers.RepeatedCompositeFieldContainer[_channel_connection_pb2.ChannelConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, channel_connections: _Optional[_Iterable[_Union[_channel_connection_pb2.ChannelConnection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateChannelConnectionRequest(_message.Message):
    __slots__ = ('parent', 'channel_connection', 'channel_connection_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    channel_connection: _channel_connection_pb2.ChannelConnection
    channel_connection_id: str

    def __init__(self, parent: _Optional[str]=..., channel_connection: _Optional[_Union[_channel_connection_pb2.ChannelConnection, _Mapping]]=..., channel_connection_id: _Optional[str]=...) -> None:
        ...

class DeleteChannelConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateGoogleChannelConfigRequest(_message.Message):
    __slots__ = ('google_channel_config', 'update_mask')
    GOOGLE_CHANNEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    google_channel_config: _google_channel_config_pb2.GoogleChannelConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, google_channel_config: _Optional[_Union[_google_channel_config_pb2.GoogleChannelConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetGoogleChannelConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetMessageBusRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMessageBusesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListMessageBusesResponse(_message.Message):
    __slots__ = ('message_buses', 'next_page_token', 'unreachable')
    MESSAGE_BUSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    message_buses: _containers.RepeatedCompositeFieldContainer[_message_bus_pb2.MessageBus]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, message_buses: _Optional[_Iterable[_Union[_message_bus_pb2.MessageBus, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListMessageBusEnrollmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMessageBusEnrollmentsResponse(_message.Message):
    __slots__ = ('enrollments', 'next_page_token', 'unreachable')
    ENROLLMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    enrollments: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, enrollments: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateMessageBusRequest(_message.Message):
    __slots__ = ('parent', 'message_bus', 'message_bus_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BUS_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    message_bus: _message_bus_pb2.MessageBus
    message_bus_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., message_bus: _Optional[_Union[_message_bus_pb2.MessageBus, _Mapping]]=..., message_bus_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateMessageBusRequest(_message.Message):
    __slots__ = ('message_bus', 'update_mask', 'allow_missing', 'validate_only')
    MESSAGE_BUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    message_bus: _message_bus_pb2.MessageBus
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    validate_only: bool

    def __init__(self, message_bus: _Optional[_Union[_message_bus_pb2.MessageBus, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteMessageBusRequest(_message.Message):
    __slots__ = ('name', 'etag', 'allow_missing', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class GetEnrollmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEnrollmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListEnrollmentsResponse(_message.Message):
    __slots__ = ('enrollments', 'next_page_token', 'unreachable')
    ENROLLMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    enrollments: _containers.RepeatedCompositeFieldContainer[_enrollment_pb2.Enrollment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, enrollments: _Optional[_Iterable[_Union[_enrollment_pb2.Enrollment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateEnrollmentRequest(_message.Message):
    __slots__ = ('parent', 'enrollment', 'enrollment_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    enrollment: _enrollment_pb2.Enrollment
    enrollment_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., enrollment: _Optional[_Union[_enrollment_pb2.Enrollment, _Mapping]]=..., enrollment_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateEnrollmentRequest(_message.Message):
    __slots__ = ('enrollment', 'update_mask', 'allow_missing', 'validate_only')
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    enrollment: _enrollment_pb2.Enrollment
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    validate_only: bool

    def __init__(self, enrollment: _Optional[_Union[_enrollment_pb2.Enrollment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteEnrollmentRequest(_message.Message):
    __slots__ = ('name', 'etag', 'allow_missing', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class GetPipelineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPipelinesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPipelinesResponse(_message.Message):
    __slots__ = ('pipelines', 'next_page_token', 'unreachable')
    PIPELINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    pipelines: _containers.RepeatedCompositeFieldContainer[_pipeline_pb2.Pipeline]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, pipelines: _Optional[_Iterable[_Union[_pipeline_pb2.Pipeline, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreatePipelineRequest(_message.Message):
    __slots__ = ('parent', 'pipeline', 'pipeline_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pipeline: _pipeline_pb2.Pipeline
    pipeline_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., pipeline: _Optional[_Union[_pipeline_pb2.Pipeline, _Mapping]]=..., pipeline_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdatePipelineRequest(_message.Message):
    __slots__ = ('pipeline', 'update_mask', 'allow_missing', 'validate_only')
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    pipeline: _pipeline_pb2.Pipeline
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    validate_only: bool

    def __init__(self, pipeline: _Optional[_Union[_pipeline_pb2.Pipeline, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeletePipelineRequest(_message.Message):
    __slots__ = ('name', 'etag', 'allow_missing', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class GetGoogleApiSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGoogleApiSourcesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListGoogleApiSourcesResponse(_message.Message):
    __slots__ = ('google_api_sources', 'next_page_token', 'unreachable')
    GOOGLE_API_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    google_api_sources: _containers.RepeatedCompositeFieldContainer[_google_api_source_pb2.GoogleApiSource]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, google_api_sources: _Optional[_Iterable[_Union[_google_api_source_pb2.GoogleApiSource, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateGoogleApiSourceRequest(_message.Message):
    __slots__ = ('parent', 'google_api_source', 'google_api_source_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_API_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_API_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    google_api_source: _google_api_source_pb2.GoogleApiSource
    google_api_source_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., google_api_source: _Optional[_Union[_google_api_source_pb2.GoogleApiSource, _Mapping]]=..., google_api_source_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateGoogleApiSourceRequest(_message.Message):
    __slots__ = ('google_api_source', 'update_mask', 'allow_missing', 'validate_only')
    GOOGLE_API_SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    google_api_source: _google_api_source_pb2.GoogleApiSource
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    validate_only: bool

    def __init__(self, google_api_source: _Optional[_Union[_google_api_source_pb2.GoogleApiSource, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteGoogleApiSourceRequest(_message.Message):
    __slots__ = ('name', 'etag', 'allow_missing', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...