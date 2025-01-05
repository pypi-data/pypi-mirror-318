from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securityposture.v1 import org_policy_constraints_pb2 as _org_policy_constraints_pb2
from google.cloud.securityposture.v1 import sha_constraints_pb2 as _sha_constraints_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version', 'error_message')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    error_message: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
        ...

class Posture(_message.Message):
    __slots__ = ('name', 'state', 'revision_id', 'create_time', 'update_time', 'description', 'policy_sets', 'etag', 'annotations', 'reconciling')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Posture.State]
        DEPRECATED: _ClassVar[Posture.State]
        DRAFT: _ClassVar[Posture.State]
        ACTIVE: _ClassVar[Posture.State]
    STATE_UNSPECIFIED: Posture.State
    DEPRECATED: Posture.State
    DRAFT: Posture.State
    ACTIVE: Posture.State

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_SETS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Posture.State
    revision_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    policy_sets: _containers.RepeatedCompositeFieldContainer[PolicySet]
    etag: str
    annotations: _containers.ScalarMap[str, str]
    reconciling: bool

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[Posture.State, str]]=..., revision_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., policy_sets: _Optional[_Iterable[_Union[PolicySet, _Mapping]]]=..., etag: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., reconciling: bool=...) -> None:
        ...

class PolicySet(_message.Message):
    __slots__ = ('policy_set_id', 'description', 'policies')
    POLICY_SET_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policy_set_id: str
    description: str
    policies: _containers.RepeatedCompositeFieldContainer[Policy]

    def __init__(self, policy_set_id: _Optional[str]=..., description: _Optional[str]=..., policies: _Optional[_Iterable[_Union[Policy, _Mapping]]]=...) -> None:
        ...

class Policy(_message.Message):
    __slots__ = ('policy_id', 'compliance_standards', 'constraint', 'description')

    class ComplianceStandard(_message.Message):
        __slots__ = ('standard', 'control')
        STANDARD_FIELD_NUMBER: _ClassVar[int]
        CONTROL_FIELD_NUMBER: _ClassVar[int]
        standard: str
        control: str

        def __init__(self, standard: _Optional[str]=..., control: _Optional[str]=...) -> None:
            ...
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_STANDARDS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    compliance_standards: _containers.RepeatedCompositeFieldContainer[Policy.ComplianceStandard]
    constraint: Constraint
    description: str

    def __init__(self, policy_id: _Optional[str]=..., compliance_standards: _Optional[_Iterable[_Union[Policy.ComplianceStandard, _Mapping]]]=..., constraint: _Optional[_Union[Constraint, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class Constraint(_message.Message):
    __slots__ = ('security_health_analytics_module', 'security_health_analytics_custom_module', 'org_policy_constraint', 'org_policy_constraint_custom')
    SECURITY_HEALTH_ANALYTICS_MODULE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_CONSTRAINT_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    security_health_analytics_module: _sha_constraints_pb2.SecurityHealthAnalyticsModule
    security_health_analytics_custom_module: _sha_constraints_pb2.SecurityHealthAnalyticsCustomModule
    org_policy_constraint: _org_policy_constraints_pb2.OrgPolicyConstraint
    org_policy_constraint_custom: _org_policy_constraints_pb2.OrgPolicyConstraintCustom

    def __init__(self, security_health_analytics_module: _Optional[_Union[_sha_constraints_pb2.SecurityHealthAnalyticsModule, _Mapping]]=..., security_health_analytics_custom_module: _Optional[_Union[_sha_constraints_pb2.SecurityHealthAnalyticsCustomModule, _Mapping]]=..., org_policy_constraint: _Optional[_Union[_org_policy_constraints_pb2.OrgPolicyConstraint, _Mapping]]=..., org_policy_constraint_custom: _Optional[_Union[_org_policy_constraints_pb2.OrgPolicyConstraintCustom, _Mapping]]=...) -> None:
        ...

class ListPosturesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPosturesResponse(_message.Message):
    __slots__ = ('postures', 'next_page_token', 'unreachable')
    POSTURES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    postures: _containers.RepeatedCompositeFieldContainer[Posture]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, postures: _Optional[_Iterable[_Union[Posture, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListPostureRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPostureRevisionsResponse(_message.Message):
    __slots__ = ('revisions', 'next_page_token')
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[Posture]
    next_page_token: str

    def __init__(self, revisions: _Optional[_Iterable[_Union[Posture, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPostureRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...

class CreatePostureRequest(_message.Message):
    __slots__ = ('parent', 'posture_id', 'posture')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POSTURE_ID_FIELD_NUMBER: _ClassVar[int]
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    posture_id: str
    posture: Posture

    def __init__(self, parent: _Optional[str]=..., posture_id: _Optional[str]=..., posture: _Optional[_Union[Posture, _Mapping]]=...) -> None:
        ...

class UpdatePostureRequest(_message.Message):
    __slots__ = ('update_mask', 'posture', 'revision_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    POSTURE_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    posture: Posture
    revision_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., posture: _Optional[_Union[Posture, _Mapping]]=..., revision_id: _Optional[str]=...) -> None:
        ...

class DeletePostureRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ExtractPostureRequest(_message.Message):
    __slots__ = ('parent', 'posture_id', 'workload')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POSTURE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    posture_id: str
    workload: str

    def __init__(self, parent: _Optional[str]=..., posture_id: _Optional[str]=..., workload: _Optional[str]=...) -> None:
        ...

class PostureDeployment(_message.Message):
    __slots__ = ('name', 'target_resource', 'state', 'posture_id', 'posture_revision_id', 'create_time', 'update_time', 'description', 'etag', 'annotations', 'reconciling', 'desired_posture_id', 'desired_posture_revision_id', 'failure_message')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PostureDeployment.State]
        CREATING: _ClassVar[PostureDeployment.State]
        DELETING: _ClassVar[PostureDeployment.State]
        UPDATING: _ClassVar[PostureDeployment.State]
        ACTIVE: _ClassVar[PostureDeployment.State]
        CREATE_FAILED: _ClassVar[PostureDeployment.State]
        UPDATE_FAILED: _ClassVar[PostureDeployment.State]
        DELETE_FAILED: _ClassVar[PostureDeployment.State]
    STATE_UNSPECIFIED: PostureDeployment.State
    CREATING: PostureDeployment.State
    DELETING: PostureDeployment.State
    UPDATING: PostureDeployment.State
    ACTIVE: PostureDeployment.State
    CREATE_FAILED: PostureDeployment.State
    UPDATE_FAILED: PostureDeployment.State
    DELETE_FAILED: PostureDeployment.State

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTURE_ID_FIELD_NUMBER: _ClassVar[int]
    POSTURE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POSTURE_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POSTURE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_resource: str
    state: PostureDeployment.State
    posture_id: str
    posture_revision_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    etag: str
    annotations: _containers.ScalarMap[str, str]
    reconciling: bool
    desired_posture_id: str
    desired_posture_revision_id: str
    failure_message: str

    def __init__(self, name: _Optional[str]=..., target_resource: _Optional[str]=..., state: _Optional[_Union[PostureDeployment.State, str]]=..., posture_id: _Optional[str]=..., posture_revision_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., etag: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., reconciling: bool=..., desired_posture_id: _Optional[str]=..., desired_posture_revision_id: _Optional[str]=..., failure_message: _Optional[str]=...) -> None:
        ...

class ListPostureDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPostureDeploymentsResponse(_message.Message):
    __slots__ = ('posture_deployments', 'next_page_token', 'unreachable')
    POSTURE_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    posture_deployments: _containers.RepeatedCompositeFieldContainer[PostureDeployment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, posture_deployments: _Optional[_Iterable[_Union[PostureDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetPostureDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePostureDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'posture_deployment_id', 'posture_deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POSTURE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    POSTURE_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    posture_deployment_id: str
    posture_deployment: PostureDeployment

    def __init__(self, parent: _Optional[str]=..., posture_deployment_id: _Optional[str]=..., posture_deployment: _Optional[_Union[PostureDeployment, _Mapping]]=...) -> None:
        ...

class UpdatePostureDeploymentRequest(_message.Message):
    __slots__ = ('update_mask', 'posture_deployment')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    POSTURE_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    posture_deployment: PostureDeployment

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., posture_deployment: _Optional[_Union[PostureDeployment, _Mapping]]=...) -> None:
        ...

class DeletePostureDeploymentRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class PostureTemplate(_message.Message):
    __slots__ = ('name', 'revision_id', 'description', 'state', 'policy_sets')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PostureTemplate.State]
        ACTIVE: _ClassVar[PostureTemplate.State]
        DEPRECATED: _ClassVar[PostureTemplate.State]
    STATE_UNSPECIFIED: PostureTemplate.State
    ACTIVE: PostureTemplate.State
    DEPRECATED: PostureTemplate.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_SETS_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    description: str
    state: PostureTemplate.State
    policy_sets: _containers.RepeatedCompositeFieldContainer[PolicySet]

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[PostureTemplate.State, str]]=..., policy_sets: _Optional[_Iterable[_Union[PolicySet, _Mapping]]]=...) -> None:
        ...

class ListPostureTemplatesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListPostureTemplatesResponse(_message.Message):
    __slots__ = ('posture_templates', 'next_page_token')
    POSTURE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    posture_templates: _containers.RepeatedCompositeFieldContainer[PostureTemplate]
    next_page_token: str

    def __init__(self, posture_templates: _Optional[_Iterable[_Union[PostureTemplate, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPostureTemplateRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
        ...