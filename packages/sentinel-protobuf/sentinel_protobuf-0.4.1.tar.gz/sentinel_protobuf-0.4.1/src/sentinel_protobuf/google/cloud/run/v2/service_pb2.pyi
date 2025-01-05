from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import launch_stage_pb2 as _launch_stage_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.cloud.run.v2 import condition_pb2 as _condition_pb2
from google.cloud.run.v2 import revision_template_pb2 as _revision_template_pb2
from google.cloud.run.v2 import traffic_target_pb2 as _traffic_target_pb2
from google.cloud.run.v2 import vendor_settings_pb2 as _vendor_settings_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceRequest(_message.Message):
    __slots__ = ("parent", "service", "service_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service: Service
    service_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., service: _Optional[_Union[Service, _Mapping]] = ..., service_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ("update_mask", "service", "validate_only", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service: Service
    validate_only: bool
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., service: _Optional[_Union[Service, _Mapping]] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class ListServicesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "show_deleted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListServicesResponse(_message.Message):
    __slots__ = ("services", "next_page_token")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    next_page_token: str
    def __init__(self, services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetServiceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ("name", "validate_only", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("name", "description", "uid", "generation", "labels", "annotations", "create_time", "update_time", "delete_time", "expire_time", "creator", "last_modifier", "client", "client_version", "ingress", "launch_stage", "binary_authorization", "template", "traffic", "scaling", "invoker_iam_disabled", "default_uri_disabled", "urls", "custom_audiences", "observed_generation", "terminal_condition", "conditions", "latest_ready_revision", "latest_created_revision", "traffic_statuses", "uri", "satisfies_pzs", "reconciling", "etag")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    SCALING_FIELD_NUMBER: _ClassVar[int]
    INVOKER_IAM_DISABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_URI_DISABLED_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_GENERATION_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_CONDITION_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    LATEST_READY_REVISION_FIELD_NUMBER: _ClassVar[int]
    LATEST_CREATED_REVISION_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_STATUSES_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    uid: str
    generation: int
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    creator: str
    last_modifier: str
    client: str
    client_version: str
    ingress: _vendor_settings_pb2.IngressTraffic
    launch_stage: _launch_stage_pb2.LaunchStage
    binary_authorization: _vendor_settings_pb2.BinaryAuthorization
    template: _revision_template_pb2.RevisionTemplate
    traffic: _containers.RepeatedCompositeFieldContainer[_traffic_target_pb2.TrafficTarget]
    scaling: _vendor_settings_pb2.ServiceScaling
    invoker_iam_disabled: bool
    default_uri_disabled: bool
    urls: _containers.RepeatedScalarFieldContainer[str]
    custom_audiences: _containers.RepeatedScalarFieldContainer[str]
    observed_generation: int
    terminal_condition: _condition_pb2.Condition
    conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.Condition]
    latest_ready_revision: str
    latest_created_revision: str
    traffic_statuses: _containers.RepeatedCompositeFieldContainer[_traffic_target_pb2.TrafficTargetStatus]
    uri: str
    satisfies_pzs: bool
    reconciling: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., uid: _Optional[str] = ..., generation: _Optional[int] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creator: _Optional[str] = ..., last_modifier: _Optional[str] = ..., client: _Optional[str] = ..., client_version: _Optional[str] = ..., ingress: _Optional[_Union[_vendor_settings_pb2.IngressTraffic, str]] = ..., launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]] = ..., binary_authorization: _Optional[_Union[_vendor_settings_pb2.BinaryAuthorization, _Mapping]] = ..., template: _Optional[_Union[_revision_template_pb2.RevisionTemplate, _Mapping]] = ..., traffic: _Optional[_Iterable[_Union[_traffic_target_pb2.TrafficTarget, _Mapping]]] = ..., scaling: _Optional[_Union[_vendor_settings_pb2.ServiceScaling, _Mapping]] = ..., invoker_iam_disabled: bool = ..., default_uri_disabled: bool = ..., urls: _Optional[_Iterable[str]] = ..., custom_audiences: _Optional[_Iterable[str]] = ..., observed_generation: _Optional[int] = ..., terminal_condition: _Optional[_Union[_condition_pb2.Condition, _Mapping]] = ..., conditions: _Optional[_Iterable[_Union[_condition_pb2.Condition, _Mapping]]] = ..., latest_ready_revision: _Optional[str] = ..., latest_created_revision: _Optional[str] = ..., traffic_statuses: _Optional[_Iterable[_Union[_traffic_target_pb2.TrafficTargetStatus, _Mapping]]] = ..., uri: _Optional[str] = ..., satisfies_pzs: bool = ..., reconciling: bool = ..., etag: _Optional[str] = ...) -> None: ...
