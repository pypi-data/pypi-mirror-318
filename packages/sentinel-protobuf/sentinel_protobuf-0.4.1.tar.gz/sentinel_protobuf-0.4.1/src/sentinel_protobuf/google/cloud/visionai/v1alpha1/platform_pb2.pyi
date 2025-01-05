from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.visionai.v1alpha1 import annotations_pb2 as _annotations_pb2_1
from google.cloud.visionai.v1alpha1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_TYPE_UNSPECIFIED: _ClassVar[ModelType]
    IMAGE_CLASSIFICATION: _ClassVar[ModelType]
    OBJECT_DETECTION: _ClassVar[ModelType]
    VIDEO_CLASSIFICATION: _ClassVar[ModelType]
    VIDEO_OBJECT_TRACKING: _ClassVar[ModelType]
    VIDEO_ACTION_RECOGNITION: _ClassVar[ModelType]
    OCCUPANCY_COUNTING: _ClassVar[ModelType]
    PERSON_BLUR: _ClassVar[ModelType]
    VERTEX_CUSTOM: _ClassVar[ModelType]

class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_K80: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_P100: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_V100: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_P4: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_T4: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_A100: _ClassVar[AcceleratorType]
    TPU_V2: _ClassVar[AcceleratorType]
    TPU_V3: _ClassVar[AcceleratorType]
MODEL_TYPE_UNSPECIFIED: ModelType
IMAGE_CLASSIFICATION: ModelType
OBJECT_DETECTION: ModelType
VIDEO_CLASSIFICATION: ModelType
VIDEO_OBJECT_TRACKING: ModelType
VIDEO_ACTION_RECOGNITION: ModelType
OCCUPANCY_COUNTING: ModelType
PERSON_BLUR: ModelType
VERTEX_CUSTOM: ModelType
ACCELERATOR_TYPE_UNSPECIFIED: AcceleratorType
NVIDIA_TESLA_K80: AcceleratorType
NVIDIA_TESLA_P100: AcceleratorType
NVIDIA_TESLA_V100: AcceleratorType
NVIDIA_TESLA_P4: AcceleratorType
NVIDIA_TESLA_T4: AcceleratorType
NVIDIA_TESLA_A100: AcceleratorType
TPU_V2: AcceleratorType
TPU_V3: AcceleratorType

class DeleteApplicationInstancesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateApplicationInstancesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateApplicationInstancesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateApplicationInstancesRequest(_message.Message):
    __slots__ = ("name", "application_instances", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    application_instances: _containers.RepeatedCompositeFieldContainer[ApplicationInstance]
    request_id: str
    def __init__(self, name: _Optional[str] = ..., application_instances: _Optional[_Iterable[_Union[ApplicationInstance, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteApplicationInstancesRequest(_message.Message):
    __slots__ = ("name", "instance_ids", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_ids: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    def __init__(self, name: _Optional[str] = ..., instance_ids: _Optional[_Iterable[str]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeployApplicationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UndeployApplicationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveApplicationStreamInputResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddApplicationStreamInputResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateApplicationStreamInputResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ("applications", "next_page_token", "unreachable")
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[Application]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, applications: _Optional[_Iterable[_Union[Application, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ("parent", "application_id", "application", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    application_id: str
    application: Application
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., application_id: _Optional[str] = ..., application: _Optional[_Union[Application, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ("update_mask", "application", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    application: Application
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., application: _Optional[_Union[Application, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class DeployApplicationRequest(_message.Message):
    __slots__ = ("name", "validate_only", "request_id", "enable_monitoring")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MONITORING_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    request_id: str
    enable_monitoring: bool
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., request_id: _Optional[str] = ..., enable_monitoring: bool = ...) -> None: ...

class UndeployApplicationRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ApplicationStreamInput(_message.Message):
    __slots__ = ("stream_with_annotation",)
    STREAM_WITH_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    stream_with_annotation: StreamWithAnnotation
    def __init__(self, stream_with_annotation: _Optional[_Union[StreamWithAnnotation, _Mapping]] = ...) -> None: ...

class AddApplicationStreamInputRequest(_message.Message):
    __slots__ = ("name", "application_stream_inputs", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_STREAM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    application_stream_inputs: _containers.RepeatedCompositeFieldContainer[ApplicationStreamInput]
    request_id: str
    def __init__(self, name: _Optional[str] = ..., application_stream_inputs: _Optional[_Iterable[_Union[ApplicationStreamInput, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateApplicationStreamInputRequest(_message.Message):
    __slots__ = ("name", "application_stream_inputs", "request_id", "allow_missing")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_STREAM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    application_stream_inputs: _containers.RepeatedCompositeFieldContainer[ApplicationStreamInput]
    request_id: str
    allow_missing: bool
    def __init__(self, name: _Optional[str] = ..., application_stream_inputs: _Optional[_Iterable[_Union[ApplicationStreamInput, _Mapping]]] = ..., request_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class RemoveApplicationStreamInputRequest(_message.Message):
    __slots__ = ("name", "target_stream_inputs", "request_id")
    class TargetStreamInput(_message.Message):
        __slots__ = ("stream",)
        STREAM_FIELD_NUMBER: _ClassVar[int]
        stream: str
        def __init__(self, stream: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_STREAM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_stream_inputs: _containers.RepeatedCompositeFieldContainer[RemoveApplicationStreamInputRequest.TargetStreamInput]
    request_id: str
    def __init__(self, name: _Optional[str] = ..., target_stream_inputs: _Optional[_Iterable[_Union[RemoveApplicationStreamInputRequest.TargetStreamInput, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListInstancesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListInstancesResponse(_message.Message):
    __slots__ = ("instances", "next_page_token", "unreachable")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetInstanceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDraftsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListDraftsResponse(_message.Message):
    __slots__ = ("drafts", "next_page_token", "unreachable")
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    drafts: _containers.RepeatedCompositeFieldContainer[Draft]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, drafts: _Optional[_Iterable[_Union[Draft, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDraftRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateDraftRequest(_message.Message):
    __slots__ = ("parent", "draft_id", "draft", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    draft_id: str
    draft: Draft
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., draft_id: _Optional[str] = ..., draft: _Optional[_Union[Draft, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateDraftRequest(_message.Message):
    __slots__ = ("update_mask", "draft", "request_id", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    draft: Draft
    request_id: str
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., draft: _Optional[_Union[Draft, _Mapping]] = ..., request_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class UpdateApplicationInstancesRequest(_message.Message):
    __slots__ = ("name", "application_instances", "request_id", "allow_missing")
    class UpdateApplicationInstance(_message.Message):
        __slots__ = ("update_mask", "instance", "instance_id")
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        instance: Instance
        instance_id: str
        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ..., instance_id: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    application_instances: _containers.RepeatedCompositeFieldContainer[UpdateApplicationInstancesRequest.UpdateApplicationInstance]
    request_id: str
    allow_missing: bool
    def __init__(self, name: _Optional[str] = ..., application_instances: _Optional[_Iterable[_Union[UpdateApplicationInstancesRequest.UpdateApplicationInstance, _Mapping]]] = ..., request_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class DeleteDraftRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListProcessorsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListProcessorsResponse(_message.Message):
    __slots__ = ("processors", "next_page_token", "unreachable")
    PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    processors: _containers.RepeatedCompositeFieldContainer[Processor]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, processors: _Optional[_Iterable[_Union[Processor, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class ListPrebuiltProcessorsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListPrebuiltProcessorsResponse(_message.Message):
    __slots__ = ("processors",)
    PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    processors: _containers.RepeatedCompositeFieldContainer[Processor]
    def __init__(self, processors: _Optional[_Iterable[_Union[Processor, _Mapping]]] = ...) -> None: ...

class GetProcessorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateProcessorRequest(_message.Message):
    __slots__ = ("parent", "processor_id", "processor", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    processor_id: str
    processor: Processor
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., processor_id: _Optional[str] = ..., processor: _Optional[_Union[Processor, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateProcessorRequest(_message.Message):
    __slots__ = ("update_mask", "processor", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    processor: Processor
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., processor: _Optional[_Union[Processor, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteProcessorRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class Application(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "description", "application_configs", "runtime_info", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Application.State]
        CREATED: _ClassVar[Application.State]
        DEPLOYING: _ClassVar[Application.State]
        DEPLOYED: _ClassVar[Application.State]
        UNDEPLOYING: _ClassVar[Application.State]
        DELETED: _ClassVar[Application.State]
        ERROR: _ClassVar[Application.State]
        CREATING: _ClassVar[Application.State]
        UPDATING: _ClassVar[Application.State]
        DELETING: _ClassVar[Application.State]
        FIXING: _ClassVar[Application.State]
    STATE_UNSPECIFIED: Application.State
    CREATED: Application.State
    DEPLOYING: Application.State
    DEPLOYED: Application.State
    UNDEPLOYING: Application.State
    DELETED: Application.State
    ERROR: Application.State
    CREATING: Application.State
    UPDATING: Application.State
    DELETING: Application.State
    FIXING: Application.State
    class ApplicationRuntimeInfo(_message.Message):
        __slots__ = ("deploy_time", "global_output_resources", "monitoring_config")
        class GlobalOutputResource(_message.Message):
            __slots__ = ("output_resource", "producer_node", "key")
            OUTPUT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
            PRODUCER_NODE_FIELD_NUMBER: _ClassVar[int]
            KEY_FIELD_NUMBER: _ClassVar[int]
            output_resource: str
            producer_node: str
            key: str
            def __init__(self, output_resource: _Optional[str] = ..., producer_node: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
        class MonitoringConfig(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...
        DEPLOY_TIME_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_OUTPUT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        deploy_time: _timestamp_pb2.Timestamp
        global_output_resources: _containers.RepeatedCompositeFieldContainer[Application.ApplicationRuntimeInfo.GlobalOutputResource]
        monitoring_config: Application.ApplicationRuntimeInfo.MonitoringConfig
        def __init__(self, deploy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., global_output_resources: _Optional[_Iterable[_Union[Application.ApplicationRuntimeInfo.GlobalOutputResource, _Mapping]]] = ..., monitoring_config: _Optional[_Union[Application.ApplicationRuntimeInfo.MonitoringConfig, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str
    application_configs: ApplicationConfigs
    runtime_info: Application.ApplicationRuntimeInfo
    state: Application.State
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., application_configs: _Optional[_Union[ApplicationConfigs, _Mapping]] = ..., runtime_info: _Optional[_Union[Application.ApplicationRuntimeInfo, _Mapping]] = ..., state: _Optional[_Union[Application.State, str]] = ...) -> None: ...

class ApplicationConfigs(_message.Message):
    __slots__ = ("nodes", "event_delivery_config")
    class EventDeliveryConfig(_message.Message):
        __slots__ = ("channel", "minimal_delivery_interval")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        MINIMAL_DELIVERY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        channel: str
        minimal_delivery_interval: _duration_pb2.Duration
        def __init__(self, channel: _Optional[str] = ..., minimal_delivery_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    NODES_FIELD_NUMBER: _ClassVar[int]
    EVENT_DELIVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    event_delivery_config: ApplicationConfigs.EventDeliveryConfig
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., event_delivery_config: _Optional[_Union[ApplicationConfigs.EventDeliveryConfig, _Mapping]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("output_all_output_channels_to_stream", "name", "display_name", "node_config", "processor", "parents")
    class InputEdge(_message.Message):
        __slots__ = ("parent_node", "parent_output_channel", "connected_input_channel")
        PARENT_NODE_FIELD_NUMBER: _ClassVar[int]
        PARENT_OUTPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_INPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        parent_node: str
        parent_output_channel: str
        connected_input_channel: str
        def __init__(self, parent_node: _Optional[str] = ..., parent_output_channel: _Optional[str] = ..., connected_input_channel: _Optional[str] = ...) -> None: ...
    OUTPUT_ALL_OUTPUT_CHANNELS_TO_STREAM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    output_all_output_channels_to_stream: bool
    name: str
    display_name: str
    node_config: ProcessorConfig
    processor: str
    parents: _containers.RepeatedCompositeFieldContainer[Node.InputEdge]
    def __init__(self, output_all_output_channels_to_stream: bool = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., node_config: _Optional[_Union[ProcessorConfig, _Mapping]] = ..., processor: _Optional[str] = ..., parents: _Optional[_Iterable[_Union[Node.InputEdge, _Mapping]]] = ...) -> None: ...

class Draft(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "description", "draft_application_configs")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DRAFT_APPLICATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str
    draft_application_configs: ApplicationConfigs
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., draft_application_configs: _Optional[_Union[ApplicationConfigs, _Mapping]] = ...) -> None: ...

class Instance(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "description", "input_resources", "output_resources", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        CREATED: _ClassVar[Instance.State]
        DEPLOYING: _ClassVar[Instance.State]
        DEPLOYED: _ClassVar[Instance.State]
        UNDEPLOYING: _ClassVar[Instance.State]
        DELETED: _ClassVar[Instance.State]
        ERROR: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        FIXING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    CREATED: Instance.State
    DEPLOYING: Instance.State
    DEPLOYED: Instance.State
    UNDEPLOYING: Instance.State
    DELETED: Instance.State
    ERROR: Instance.State
    UPDATING: Instance.State
    DELETING: Instance.State
    FIXING: Instance.State
    class InputResource(_message.Message):
        __slots__ = ("input_resource", "annotated_stream", "consumer_node", "input_resource_binding", "annotations")
        INPUT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        ANNOTATED_STREAM_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_NODE_FIELD_NUMBER: _ClassVar[int]
        INPUT_RESOURCE_BINDING_FIELD_NUMBER: _ClassVar[int]
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        input_resource: str
        annotated_stream: StreamWithAnnotation
        consumer_node: str
        input_resource_binding: str
        annotations: ResourceAnnotations
        def __init__(self, input_resource: _Optional[str] = ..., annotated_stream: _Optional[_Union[StreamWithAnnotation, _Mapping]] = ..., consumer_node: _Optional[str] = ..., input_resource_binding: _Optional[str] = ..., annotations: _Optional[_Union[ResourceAnnotations, _Mapping]] = ...) -> None: ...
    class OutputResource(_message.Message):
        __slots__ = ("output_resource", "producer_node", "output_resource_binding", "is_temporary", "autogen")
        OUTPUT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_NODE_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_RESOURCE_BINDING_FIELD_NUMBER: _ClassVar[int]
        IS_TEMPORARY_FIELD_NUMBER: _ClassVar[int]
        AUTOGEN_FIELD_NUMBER: _ClassVar[int]
        output_resource: str
        producer_node: str
        output_resource_binding: str
        is_temporary: bool
        autogen: bool
        def __init__(self, output_resource: _Optional[str] = ..., producer_node: _Optional[str] = ..., output_resource_binding: _Optional[str] = ..., is_temporary: bool = ..., autogen: bool = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str
    input_resources: _containers.RepeatedCompositeFieldContainer[Instance.InputResource]
    output_resources: _containers.RepeatedCompositeFieldContainer[Instance.OutputResource]
    state: Instance.State
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., input_resources: _Optional[_Iterable[_Union[Instance.InputResource, _Mapping]]] = ..., output_resources: _Optional[_Iterable[_Union[Instance.OutputResource, _Mapping]]] = ..., state: _Optional[_Union[Instance.State, str]] = ...) -> None: ...

class ApplicationInstance(_message.Message):
    __slots__ = ("instance_id", "instance")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    instance: Instance
    def __init__(self, instance_id: _Optional[str] = ..., instance: _Optional[_Union[Instance, _Mapping]] = ...) -> None: ...

class Processor(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "labels", "display_name", "description", "processor_type", "model_type", "custom_processor_source_info", "state", "processor_io_spec", "configuration_typeurl", "supported_annotation_types", "supports_post_processing")
    class ProcessorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSOR_TYPE_UNSPECIFIED: _ClassVar[Processor.ProcessorType]
        PRETRAINED: _ClassVar[Processor.ProcessorType]
        CUSTOM: _ClassVar[Processor.ProcessorType]
        CONNECTOR: _ClassVar[Processor.ProcessorType]
    PROCESSOR_TYPE_UNSPECIFIED: Processor.ProcessorType
    PRETRAINED: Processor.ProcessorType
    CUSTOM: Processor.ProcessorType
    CONNECTOR: Processor.ProcessorType
    class ProcessorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSOR_STATE_UNSPECIFIED: _ClassVar[Processor.ProcessorState]
        CREATING: _ClassVar[Processor.ProcessorState]
        ACTIVE: _ClassVar[Processor.ProcessorState]
        DELETING: _ClassVar[Processor.ProcessorState]
        FAILED: _ClassVar[Processor.ProcessorState]
    PROCESSOR_STATE_UNSPECIFIED: Processor.ProcessorState
    CREATING: Processor.ProcessorState
    ACTIVE: Processor.ProcessorState
    DELETING: Processor.ProcessorState
    FAILED: Processor.ProcessorState
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROCESSOR_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_IO_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_TYPEURL_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ANNOTATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_POST_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str
    processor_type: Processor.ProcessorType
    model_type: ModelType
    custom_processor_source_info: CustomProcessorSourceInfo
    state: Processor.ProcessorState
    processor_io_spec: ProcessorIOSpec
    configuration_typeurl: str
    supported_annotation_types: _containers.RepeatedScalarFieldContainer[_annotations_pb2_1.StreamAnnotationType]
    supports_post_processing: bool
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., processor_type: _Optional[_Union[Processor.ProcessorType, str]] = ..., model_type: _Optional[_Union[ModelType, str]] = ..., custom_processor_source_info: _Optional[_Union[CustomProcessorSourceInfo, _Mapping]] = ..., state: _Optional[_Union[Processor.ProcessorState, str]] = ..., processor_io_spec: _Optional[_Union[ProcessorIOSpec, _Mapping]] = ..., configuration_typeurl: _Optional[str] = ..., supported_annotation_types: _Optional[_Iterable[_Union[_annotations_pb2_1.StreamAnnotationType, str]]] = ..., supports_post_processing: bool = ...) -> None: ...

class ProcessorIOSpec(_message.Message):
    __slots__ = ("graph_input_channel_specs", "graph_output_channel_specs", "instance_resource_input_binding_specs", "instance_resource_output_binding_specs")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[ProcessorIOSpec.DataType]
        VIDEO: _ClassVar[ProcessorIOSpec.DataType]
        PROTO: _ClassVar[ProcessorIOSpec.DataType]
    DATA_TYPE_UNSPECIFIED: ProcessorIOSpec.DataType
    VIDEO: ProcessorIOSpec.DataType
    PROTO: ProcessorIOSpec.DataType
    class GraphInputChannelSpec(_message.Message):
        __slots__ = ("name", "data_type", "accepted_data_type_uris", "required", "max_connection_allowed")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        ACCEPTED_DATA_TYPE_URIS_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        MAX_CONNECTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        name: str
        data_type: ProcessorIOSpec.DataType
        accepted_data_type_uris: _containers.RepeatedScalarFieldContainer[str]
        required: bool
        max_connection_allowed: int
        def __init__(self, name: _Optional[str] = ..., data_type: _Optional[_Union[ProcessorIOSpec.DataType, str]] = ..., accepted_data_type_uris: _Optional[_Iterable[str]] = ..., required: bool = ..., max_connection_allowed: _Optional[int] = ...) -> None: ...
    class GraphOutputChannelSpec(_message.Message):
        __slots__ = ("name", "data_type", "data_type_uri")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        name: str
        data_type: ProcessorIOSpec.DataType
        data_type_uri: str
        def __init__(self, name: _Optional[str] = ..., data_type: _Optional[_Union[ProcessorIOSpec.DataType, str]] = ..., data_type_uri: _Optional[str] = ...) -> None: ...
    class InstanceResourceInputBindingSpec(_message.Message):
        __slots__ = ("config_type_uri", "resource_type_uri", "name")
        CONFIG_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        config_type_uri: str
        resource_type_uri: str
        name: str
        def __init__(self, config_type_uri: _Optional[str] = ..., resource_type_uri: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class InstanceResourceOutputBindingSpec(_message.Message):
        __slots__ = ("name", "resource_type_uri", "explicit")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        EXPLICIT_FIELD_NUMBER: _ClassVar[int]
        name: str
        resource_type_uri: str
        explicit: bool
        def __init__(self, name: _Optional[str] = ..., resource_type_uri: _Optional[str] = ..., explicit: bool = ...) -> None: ...
    GRAPH_INPUT_CHANNEL_SPECS_FIELD_NUMBER: _ClassVar[int]
    GRAPH_OUTPUT_CHANNEL_SPECS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_RESOURCE_INPUT_BINDING_SPECS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_RESOURCE_OUTPUT_BINDING_SPECS_FIELD_NUMBER: _ClassVar[int]
    graph_input_channel_specs: _containers.RepeatedCompositeFieldContainer[ProcessorIOSpec.GraphInputChannelSpec]
    graph_output_channel_specs: _containers.RepeatedCompositeFieldContainer[ProcessorIOSpec.GraphOutputChannelSpec]
    instance_resource_input_binding_specs: _containers.RepeatedCompositeFieldContainer[ProcessorIOSpec.InstanceResourceInputBindingSpec]
    instance_resource_output_binding_specs: _containers.RepeatedCompositeFieldContainer[ProcessorIOSpec.InstanceResourceOutputBindingSpec]
    def __init__(self, graph_input_channel_specs: _Optional[_Iterable[_Union[ProcessorIOSpec.GraphInputChannelSpec, _Mapping]]] = ..., graph_output_channel_specs: _Optional[_Iterable[_Union[ProcessorIOSpec.GraphOutputChannelSpec, _Mapping]]] = ..., instance_resource_input_binding_specs: _Optional[_Iterable[_Union[ProcessorIOSpec.InstanceResourceInputBindingSpec, _Mapping]]] = ..., instance_resource_output_binding_specs: _Optional[_Iterable[_Union[ProcessorIOSpec.InstanceResourceOutputBindingSpec, _Mapping]]] = ...) -> None: ...

class CustomProcessorSourceInfo(_message.Message):
    __slots__ = ("vertex_model", "source_type", "additional_info", "model_schema")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNSPECIFIED: _ClassVar[CustomProcessorSourceInfo.SourceType]
        VERTEX_AUTOML: _ClassVar[CustomProcessorSourceInfo.SourceType]
        VERTEX_CUSTOM: _ClassVar[CustomProcessorSourceInfo.SourceType]
    SOURCE_TYPE_UNSPECIFIED: CustomProcessorSourceInfo.SourceType
    VERTEX_AUTOML: CustomProcessorSourceInfo.SourceType
    VERTEX_CUSTOM: CustomProcessorSourceInfo.SourceType
    class ModelSchema(_message.Message):
        __slots__ = ("instances_schema", "parameters_schema", "predictions_schema")
        INSTANCES_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        PREDICTIONS_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        instances_schema: _common_pb2.GcsSource
        parameters_schema: _common_pb2.GcsSource
        predictions_schema: _common_pb2.GcsSource
        def __init__(self, instances_schema: _Optional[_Union[_common_pb2.GcsSource, _Mapping]] = ..., parameters_schema: _Optional[_Union[_common_pb2.GcsSource, _Mapping]] = ..., predictions_schema: _Optional[_Union[_common_pb2.GcsSource, _Mapping]] = ...) -> None: ...
    class AdditionalInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VERTEX_MODEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    MODEL_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    vertex_model: str
    source_type: CustomProcessorSourceInfo.SourceType
    additional_info: _containers.ScalarMap[str, str]
    model_schema: CustomProcessorSourceInfo.ModelSchema
    def __init__(self, vertex_model: _Optional[str] = ..., source_type: _Optional[_Union[CustomProcessorSourceInfo.SourceType, str]] = ..., additional_info: _Optional[_Mapping[str, str]] = ..., model_schema: _Optional[_Union[CustomProcessorSourceInfo.ModelSchema, _Mapping]] = ...) -> None: ...

class ProcessorConfig(_message.Message):
    __slots__ = ("video_stream_input_config", "ai_enabled_devices_input_config", "media_warehouse_config", "person_blur_config", "occupancy_count_config", "person_vehicle_detection_config", "vertex_automl_vision_config", "vertex_automl_video_config", "vertex_custom_config", "general_object_detection_config", "big_query_config", "personal_protective_equipment_detection_config")
    VIDEO_STREAM_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AI_ENABLED_DEVICES_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MEDIA_WAREHOUSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSON_BLUR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OCCUPANCY_COUNT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSON_VEHICLE_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AUTOML_VISION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AUTOML_VIDEO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_CUSTOM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GENERAL_OBJECT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_PROTECTIVE_EQUIPMENT_DETECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    video_stream_input_config: VideoStreamInputConfig
    ai_enabled_devices_input_config: AIEnabledDevicesInputConfig
    media_warehouse_config: MediaWarehouseConfig
    person_blur_config: PersonBlurConfig
    occupancy_count_config: OccupancyCountConfig
    person_vehicle_detection_config: PersonVehicleDetectionConfig
    vertex_automl_vision_config: VertexAutoMLVisionConfig
    vertex_automl_video_config: VertexAutoMLVideoConfig
    vertex_custom_config: VertexCustomConfig
    general_object_detection_config: GeneralObjectDetectionConfig
    big_query_config: BigQueryConfig
    personal_protective_equipment_detection_config: PersonalProtectiveEquipmentDetectionConfig
    def __init__(self, video_stream_input_config: _Optional[_Union[VideoStreamInputConfig, _Mapping]] = ..., ai_enabled_devices_input_config: _Optional[_Union[AIEnabledDevicesInputConfig, _Mapping]] = ..., media_warehouse_config: _Optional[_Union[MediaWarehouseConfig, _Mapping]] = ..., person_blur_config: _Optional[_Union[PersonBlurConfig, _Mapping]] = ..., occupancy_count_config: _Optional[_Union[OccupancyCountConfig, _Mapping]] = ..., person_vehicle_detection_config: _Optional[_Union[PersonVehicleDetectionConfig, _Mapping]] = ..., vertex_automl_vision_config: _Optional[_Union[VertexAutoMLVisionConfig, _Mapping]] = ..., vertex_automl_video_config: _Optional[_Union[VertexAutoMLVideoConfig, _Mapping]] = ..., vertex_custom_config: _Optional[_Union[VertexCustomConfig, _Mapping]] = ..., general_object_detection_config: _Optional[_Union[GeneralObjectDetectionConfig, _Mapping]] = ..., big_query_config: _Optional[_Union[BigQueryConfig, _Mapping]] = ..., personal_protective_equipment_detection_config: _Optional[_Union[PersonalProtectiveEquipmentDetectionConfig, _Mapping]] = ...) -> None: ...

class StreamWithAnnotation(_message.Message):
    __slots__ = ("stream", "application_annotations", "node_annotations")
    class NodeAnnotation(_message.Message):
        __slots__ = ("node", "annotations")
        NODE_FIELD_NUMBER: _ClassVar[int]
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        node: str
        annotations: _containers.RepeatedCompositeFieldContainer[_annotations_pb2_1.StreamAnnotation]
        def __init__(self, node: _Optional[str] = ..., annotations: _Optional[_Iterable[_Union[_annotations_pb2_1.StreamAnnotation, _Mapping]]] = ...) -> None: ...
    STREAM_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NODE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    stream: str
    application_annotations: _containers.RepeatedCompositeFieldContainer[_annotations_pb2_1.StreamAnnotation]
    node_annotations: _containers.RepeatedCompositeFieldContainer[StreamWithAnnotation.NodeAnnotation]
    def __init__(self, stream: _Optional[str] = ..., application_annotations: _Optional[_Iterable[_Union[_annotations_pb2_1.StreamAnnotation, _Mapping]]] = ..., node_annotations: _Optional[_Iterable[_Union[StreamWithAnnotation.NodeAnnotation, _Mapping]]] = ...) -> None: ...

class ApplicationNodeAnnotation(_message.Message):
    __slots__ = ("node", "annotations")
    NODE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    node: str
    annotations: _containers.RepeatedCompositeFieldContainer[_annotations_pb2_1.StreamAnnotation]
    def __init__(self, node: _Optional[str] = ..., annotations: _Optional[_Iterable[_Union[_annotations_pb2_1.StreamAnnotation, _Mapping]]] = ...) -> None: ...

class ResourceAnnotations(_message.Message):
    __slots__ = ("application_annotations", "node_annotations")
    APPLICATION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NODE_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    application_annotations: _containers.RepeatedCompositeFieldContainer[_annotations_pb2_1.StreamAnnotation]
    node_annotations: _containers.RepeatedCompositeFieldContainer[ApplicationNodeAnnotation]
    def __init__(self, application_annotations: _Optional[_Iterable[_Union[_annotations_pb2_1.StreamAnnotation, _Mapping]]] = ..., node_annotations: _Optional[_Iterable[_Union[ApplicationNodeAnnotation, _Mapping]]] = ...) -> None: ...

class VideoStreamInputConfig(_message.Message):
    __slots__ = ("streams", "streams_with_annotation")
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    STREAMS_WITH_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedScalarFieldContainer[str]
    streams_with_annotation: _containers.RepeatedCompositeFieldContainer[StreamWithAnnotation]
    def __init__(self, streams: _Optional[_Iterable[str]] = ..., streams_with_annotation: _Optional[_Iterable[_Union[StreamWithAnnotation, _Mapping]]] = ...) -> None: ...

class AIEnabledDevicesInputConfig(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MediaWarehouseConfig(_message.Message):
    __slots__ = ("corpus", "region", "ttl")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    corpus: str
    region: str
    ttl: _duration_pb2.Duration
    def __init__(self, corpus: _Optional[str] = ..., region: _Optional[str] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PersonBlurConfig(_message.Message):
    __slots__ = ("person_blur_type", "faces_only")
    class PersonBlurType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSON_BLUR_TYPE_UNSPECIFIED: _ClassVar[PersonBlurConfig.PersonBlurType]
        FULL_OCCULUSION: _ClassVar[PersonBlurConfig.PersonBlurType]
        BLUR_FILTER: _ClassVar[PersonBlurConfig.PersonBlurType]
    PERSON_BLUR_TYPE_UNSPECIFIED: PersonBlurConfig.PersonBlurType
    FULL_OCCULUSION: PersonBlurConfig.PersonBlurType
    BLUR_FILTER: PersonBlurConfig.PersonBlurType
    PERSON_BLUR_TYPE_FIELD_NUMBER: _ClassVar[int]
    FACES_ONLY_FIELD_NUMBER: _ClassVar[int]
    person_blur_type: PersonBlurConfig.PersonBlurType
    faces_only: bool
    def __init__(self, person_blur_type: _Optional[_Union[PersonBlurConfig.PersonBlurType, str]] = ..., faces_only: bool = ...) -> None: ...

class OccupancyCountConfig(_message.Message):
    __slots__ = ("enable_people_counting", "enable_vehicle_counting", "enable_dwelling_time_tracking")
    ENABLE_PEOPLE_COUNTING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VEHICLE_COUNTING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DWELLING_TIME_TRACKING_FIELD_NUMBER: _ClassVar[int]
    enable_people_counting: bool
    enable_vehicle_counting: bool
    enable_dwelling_time_tracking: bool
    def __init__(self, enable_people_counting: bool = ..., enable_vehicle_counting: bool = ..., enable_dwelling_time_tracking: bool = ...) -> None: ...

class PersonVehicleDetectionConfig(_message.Message):
    __slots__ = ("enable_people_counting", "enable_vehicle_counting")
    ENABLE_PEOPLE_COUNTING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VEHICLE_COUNTING_FIELD_NUMBER: _ClassVar[int]
    enable_people_counting: bool
    enable_vehicle_counting: bool
    def __init__(self, enable_people_counting: bool = ..., enable_vehicle_counting: bool = ...) -> None: ...

class PersonalProtectiveEquipmentDetectionConfig(_message.Message):
    __slots__ = ("enable_face_coverage_detection", "enable_head_coverage_detection", "enable_hands_coverage_detection")
    ENABLE_FACE_COVERAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEAD_COVERAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HANDS_COVERAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    enable_face_coverage_detection: bool
    enable_head_coverage_detection: bool
    enable_hands_coverage_detection: bool
    def __init__(self, enable_face_coverage_detection: bool = ..., enable_head_coverage_detection: bool = ..., enable_hands_coverage_detection: bool = ...) -> None: ...

class GeneralObjectDetectionConfig(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BigQueryConfig(_message.Message):
    __slots__ = ("table", "cloud_function_mapping", "create_default_table_if_not_exists")
    class CloudFunctionMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TABLE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_MAPPING_FIELD_NUMBER: _ClassVar[int]
    CREATE_DEFAULT_TABLE_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    table: str
    cloud_function_mapping: _containers.ScalarMap[str, str]
    create_default_table_if_not_exists: bool
    def __init__(self, table: _Optional[str] = ..., cloud_function_mapping: _Optional[_Mapping[str, str]] = ..., create_default_table_if_not_exists: bool = ...) -> None: ...

class VertexAutoMLVisionConfig(_message.Message):
    __slots__ = ("confidence_threshold", "max_predictions")
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float
    max_predictions: int
    def __init__(self, confidence_threshold: _Optional[float] = ..., max_predictions: _Optional[int] = ...) -> None: ...

class VertexAutoMLVideoConfig(_message.Message):
    __slots__ = ("confidence_threshold", "blocked_labels", "max_predictions", "bounding_box_size_limit")
    CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_LABELS_FIELD_NUMBER: _ClassVar[int]
    MAX_PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    confidence_threshold: float
    blocked_labels: _containers.RepeatedScalarFieldContainer[str]
    max_predictions: int
    bounding_box_size_limit: float
    def __init__(self, confidence_threshold: _Optional[float] = ..., blocked_labels: _Optional[_Iterable[str]] = ..., max_predictions: _Optional[int] = ..., bounding_box_size_limit: _Optional[float] = ...) -> None: ...

class VertexCustomConfig(_message.Message):
    __slots__ = ("max_prediction_fps", "dedicated_resources", "post_processing_cloud_function", "attach_application_metadata")
    MAX_PREDICTION_FPS_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ATTACH_APPLICATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    max_prediction_fps: int
    dedicated_resources: DedicatedResources
    post_processing_cloud_function: str
    attach_application_metadata: bool
    def __init__(self, max_prediction_fps: _Optional[int] = ..., dedicated_resources: _Optional[_Union[DedicatedResources, _Mapping]] = ..., post_processing_cloud_function: _Optional[str] = ..., attach_application_metadata: bool = ...) -> None: ...

class MachineSpec(_message.Message):
    __slots__ = ("machine_type", "accelerator_type", "accelerator_count")
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    accelerator_type: AcceleratorType
    accelerator_count: int
    def __init__(self, machine_type: _Optional[str] = ..., accelerator_type: _Optional[_Union[AcceleratorType, str]] = ..., accelerator_count: _Optional[int] = ...) -> None: ...

class AutoscalingMetricSpec(_message.Message):
    __slots__ = ("metric_name", "target")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    target: int
    def __init__(self, metric_name: _Optional[str] = ..., target: _Optional[int] = ...) -> None: ...

class DedicatedResources(_message.Message):
    __slots__ = ("machine_spec", "min_replica_count", "max_replica_count", "autoscaling_metric_specs")
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_METRIC_SPECS_FIELD_NUMBER: _ClassVar[int]
    machine_spec: MachineSpec
    min_replica_count: int
    max_replica_count: int
    autoscaling_metric_specs: _containers.RepeatedCompositeFieldContainer[AutoscalingMetricSpec]
    def __init__(self, machine_spec: _Optional[_Union[MachineSpec, _Mapping]] = ..., min_replica_count: _Optional[int] = ..., max_replica_count: _Optional[int] = ..., autoscaling_metric_specs: _Optional[_Iterable[_Union[AutoscalingMetricSpec, _Mapping]]] = ...) -> None: ...
