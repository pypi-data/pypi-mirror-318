from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuotaValidation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUOTA_VALIDATION_UNSPECIFIED: _ClassVar[QuotaValidation]
    ENABLED: _ClassVar[QuotaValidation]
    ENFORCED: _ClassVar[QuotaValidation]
QUOTA_VALIDATION_UNSPECIFIED: QuotaValidation
ENABLED: QuotaValidation
ENFORCED: QuotaValidation

class Deployment(_message.Message):
    __slots__ = ("terraform_blueprint", "name", "create_time", "update_time", "labels", "state", "latest_revision", "state_detail", "error_code", "delete_results", "delete_build", "delete_logs", "tf_errors", "error_logs", "artifacts_gcs_bucket", "service_account", "import_existing_resources", "worker_pool", "lock_state", "tf_version_constraint", "tf_version", "quota_validation", "annotations")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Deployment.State]
        CREATING: _ClassVar[Deployment.State]
        ACTIVE: _ClassVar[Deployment.State]
        UPDATING: _ClassVar[Deployment.State]
        DELETING: _ClassVar[Deployment.State]
        FAILED: _ClassVar[Deployment.State]
        SUSPENDED: _ClassVar[Deployment.State]
        DELETED: _ClassVar[Deployment.State]
    STATE_UNSPECIFIED: Deployment.State
    CREATING: Deployment.State
    ACTIVE: Deployment.State
    UPDATING: Deployment.State
    DELETING: Deployment.State
    FAILED: Deployment.State
    SUSPENDED: Deployment.State
    DELETED: Deployment.State
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[Deployment.ErrorCode]
        REVISION_FAILED: _ClassVar[Deployment.ErrorCode]
        CLOUD_BUILD_PERMISSION_DENIED: _ClassVar[Deployment.ErrorCode]
        DELETE_BUILD_API_FAILED: _ClassVar[Deployment.ErrorCode]
        DELETE_BUILD_RUN_FAILED: _ClassVar[Deployment.ErrorCode]
        BUCKET_CREATION_PERMISSION_DENIED: _ClassVar[Deployment.ErrorCode]
        BUCKET_CREATION_FAILED: _ClassVar[Deployment.ErrorCode]
    ERROR_CODE_UNSPECIFIED: Deployment.ErrorCode
    REVISION_FAILED: Deployment.ErrorCode
    CLOUD_BUILD_PERMISSION_DENIED: Deployment.ErrorCode
    DELETE_BUILD_API_FAILED: Deployment.ErrorCode
    DELETE_BUILD_RUN_FAILED: Deployment.ErrorCode
    BUCKET_CREATION_PERMISSION_DENIED: Deployment.ErrorCode
    BUCKET_CREATION_FAILED: Deployment.ErrorCode
    class LockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCK_STATE_UNSPECIFIED: _ClassVar[Deployment.LockState]
        LOCKED: _ClassVar[Deployment.LockState]
        UNLOCKED: _ClassVar[Deployment.LockState]
        LOCKING: _ClassVar[Deployment.LockState]
        UNLOCKING: _ClassVar[Deployment.LockState]
        LOCK_FAILED: _ClassVar[Deployment.LockState]
        UNLOCK_FAILED: _ClassVar[Deployment.LockState]
    LOCK_STATE_UNSPECIFIED: Deployment.LockState
    LOCKED: Deployment.LockState
    UNLOCKED: Deployment.LockState
    LOCKING: Deployment.LockState
    UNLOCKING: Deployment.LockState
    LOCK_FAILED: Deployment.LockState
    UNLOCK_FAILED: Deployment.LockState
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
    TERRAFORM_BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LATEST_REVISION_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DELETE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DELETE_BUILD_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOGS_FIELD_NUMBER: _ClassVar[int]
    TF_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOGS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXISTING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_FIELD_NUMBER: _ClassVar[int]
    QUOTA_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    terraform_blueprint: TerraformBlueprint
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Deployment.State
    latest_revision: str
    state_detail: str
    error_code: Deployment.ErrorCode
    delete_results: ApplyResults
    delete_build: str
    delete_logs: str
    tf_errors: _containers.RepeatedCompositeFieldContainer[TerraformError]
    error_logs: str
    artifacts_gcs_bucket: str
    service_account: str
    import_existing_resources: bool
    worker_pool: str
    lock_state: Deployment.LockState
    tf_version_constraint: str
    tf_version: str
    quota_validation: QuotaValidation
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, terraform_blueprint: _Optional[_Union[TerraformBlueprint, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[Deployment.State, str]] = ..., latest_revision: _Optional[str] = ..., state_detail: _Optional[str] = ..., error_code: _Optional[_Union[Deployment.ErrorCode, str]] = ..., delete_results: _Optional[_Union[ApplyResults, _Mapping]] = ..., delete_build: _Optional[str] = ..., delete_logs: _Optional[str] = ..., tf_errors: _Optional[_Iterable[_Union[TerraformError, _Mapping]]] = ..., error_logs: _Optional[str] = ..., artifacts_gcs_bucket: _Optional[str] = ..., service_account: _Optional[str] = ..., import_existing_resources: bool = ..., worker_pool: _Optional[str] = ..., lock_state: _Optional[_Union[Deployment.LockState, str]] = ..., tf_version_constraint: _Optional[str] = ..., tf_version: _Optional[str] = ..., quota_validation: _Optional[_Union[QuotaValidation, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TerraformBlueprint(_message.Message):
    __slots__ = ("gcs_source", "git_source", "input_values")
    class InputValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TerraformVariable
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TerraformVariable, _Mapping]] = ...) -> None: ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GIT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_VALUES_FIELD_NUMBER: _ClassVar[int]
    gcs_source: str
    git_source: GitSource
    input_values: _containers.MessageMap[str, TerraformVariable]
    def __init__(self, gcs_source: _Optional[str] = ..., git_source: _Optional[_Union[GitSource, _Mapping]] = ..., input_values: _Optional[_Mapping[str, TerraformVariable]] = ...) -> None: ...

class TerraformVariable(_message.Message):
    __slots__ = ("input_value",)
    INPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    input_value: _struct_pb2.Value
    def __init__(self, input_value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ApplyResults(_message.Message):
    __slots__ = ("content", "artifacts", "outputs")
    class OutputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TerraformOutput
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TerraformOutput, _Mapping]] = ...) -> None: ...
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    content: str
    artifacts: str
    outputs: _containers.MessageMap[str, TerraformOutput]
    def __init__(self, content: _Optional[str] = ..., artifacts: _Optional[str] = ..., outputs: _Optional[_Mapping[str, TerraformOutput]] = ...) -> None: ...

class TerraformOutput(_message.Message):
    __slots__ = ("sensitive", "value")
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    sensitive: bool
    value: _struct_pb2.Value
    def __init__(self, sensitive: bool = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ListDeploymentsRequest(_message.Message):
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

class ListDeploymentsResponse(_message.Message):
    __slots__ = ("deployments", "next_page_token", "unreachable")
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRevisionsRequest(_message.Message):
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

class ListRevisionsResponse(_message.Message):
    __slots__ = ("revisions", "next_page_token", "unreachable")
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[Revision]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, revisions: _Optional[_Iterable[_Union[Revision, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRevisionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ("parent", "deployment_id", "deployment", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_id: str
    deployment: Deployment
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., deployment_id: _Optional[str] = ..., deployment: _Optional[_Union[Deployment, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ("update_mask", "deployment", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    deployment: Deployment
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., deployment: _Optional[_Union[Deployment, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteDeploymentRequest(_message.Message):
    __slots__ = ("name", "request_id", "force", "delete_policy")
    class DeletePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELETE_POLICY_UNSPECIFIED: _ClassVar[DeleteDeploymentRequest.DeletePolicy]
        DELETE: _ClassVar[DeleteDeploymentRequest.DeletePolicy]
        ABANDON: _ClassVar[DeleteDeploymentRequest.DeletePolicy]
    DELETE_POLICY_UNSPECIFIED: DeleteDeploymentRequest.DeletePolicy
    DELETE: DeleteDeploymentRequest.DeletePolicy
    ABANDON: DeleteDeploymentRequest.DeletePolicy
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    DELETE_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    delete_policy: DeleteDeploymentRequest.DeletePolicy
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ..., delete_policy: _Optional[_Union[DeleteDeploymentRequest.DeletePolicy, str]] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("deployment_metadata", "preview_metadata", "create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    DEPLOYMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    deployment_metadata: DeploymentOperationMetadata
    preview_metadata: PreviewOperationMetadata
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, deployment_metadata: _Optional[_Union[DeploymentOperationMetadata, _Mapping]] = ..., preview_metadata: _Optional[_Union[PreviewOperationMetadata, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class Revision(_message.Message):
    __slots__ = ("terraform_blueprint", "name", "create_time", "update_time", "action", "state", "apply_results", "state_detail", "error_code", "build", "logs", "tf_errors", "error_logs", "service_account", "import_existing_resources", "worker_pool", "tf_version_constraint", "tf_version", "quota_validation_results", "quota_validation")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[Revision.Action]
        CREATE: _ClassVar[Revision.Action]
        UPDATE: _ClassVar[Revision.Action]
        DELETE: _ClassVar[Revision.Action]
    ACTION_UNSPECIFIED: Revision.Action
    CREATE: Revision.Action
    UPDATE: Revision.Action
    DELETE: Revision.Action
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Revision.State]
        APPLYING: _ClassVar[Revision.State]
        APPLIED: _ClassVar[Revision.State]
        FAILED: _ClassVar[Revision.State]
    STATE_UNSPECIFIED: Revision.State
    APPLYING: Revision.State
    APPLIED: Revision.State
    FAILED: Revision.State
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[Revision.ErrorCode]
        CLOUD_BUILD_PERMISSION_DENIED: _ClassVar[Revision.ErrorCode]
        APPLY_BUILD_API_FAILED: _ClassVar[Revision.ErrorCode]
        APPLY_BUILD_RUN_FAILED: _ClassVar[Revision.ErrorCode]
        QUOTA_VALIDATION_FAILED: _ClassVar[Revision.ErrorCode]
    ERROR_CODE_UNSPECIFIED: Revision.ErrorCode
    CLOUD_BUILD_PERMISSION_DENIED: Revision.ErrorCode
    APPLY_BUILD_API_FAILED: Revision.ErrorCode
    APPLY_BUILD_RUN_FAILED: Revision.ErrorCode
    QUOTA_VALIDATION_FAILED: Revision.ErrorCode
    TERRAFORM_BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    APPLY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    TF_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOGS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXISTING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_FIELD_NUMBER: _ClassVar[int]
    QUOTA_VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    terraform_blueprint: TerraformBlueprint
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    action: Revision.Action
    state: Revision.State
    apply_results: ApplyResults
    state_detail: str
    error_code: Revision.ErrorCode
    build: str
    logs: str
    tf_errors: _containers.RepeatedCompositeFieldContainer[TerraformError]
    error_logs: str
    service_account: str
    import_existing_resources: bool
    worker_pool: str
    tf_version_constraint: str
    tf_version: str
    quota_validation_results: str
    quota_validation: QuotaValidation
    def __init__(self, terraform_blueprint: _Optional[_Union[TerraformBlueprint, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., action: _Optional[_Union[Revision.Action, str]] = ..., state: _Optional[_Union[Revision.State, str]] = ..., apply_results: _Optional[_Union[ApplyResults, _Mapping]] = ..., state_detail: _Optional[str] = ..., error_code: _Optional[_Union[Revision.ErrorCode, str]] = ..., build: _Optional[str] = ..., logs: _Optional[str] = ..., tf_errors: _Optional[_Iterable[_Union[TerraformError, _Mapping]]] = ..., error_logs: _Optional[str] = ..., service_account: _Optional[str] = ..., import_existing_resources: bool = ..., worker_pool: _Optional[str] = ..., tf_version_constraint: _Optional[str] = ..., tf_version: _Optional[str] = ..., quota_validation_results: _Optional[str] = ..., quota_validation: _Optional[_Union[QuotaValidation, str]] = ...) -> None: ...

class TerraformError(_message.Message):
    __slots__ = ("resource_address", "http_response_code", "error_description", "error")
    RESOURCE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HTTP_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    resource_address: str
    http_response_code: int
    error_description: str
    error: _status_pb2.Status
    def __init__(self, resource_address: _Optional[str] = ..., http_response_code: _Optional[int] = ..., error_description: _Optional[str] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class GitSource(_message.Message):
    __slots__ = ("repo", "directory", "ref")
    REPO_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    repo: str
    directory: str
    ref: str
    def __init__(self, repo: _Optional[str] = ..., directory: _Optional[str] = ..., ref: _Optional[str] = ...) -> None: ...

class DeploymentOperationMetadata(_message.Message):
    __slots__ = ("step", "apply_results", "build", "logs")
    class DeploymentStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPLOYMENT_STEP_UNSPECIFIED: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        PREPARING_STORAGE_BUCKET: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        DOWNLOADING_BLUEPRINT: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_TF_INIT: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_TF_PLAN: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_TF_APPLY: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_TF_DESTROY: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_TF_VALIDATE: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        UNLOCKING_DEPLOYMENT: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        SUCCEEDED: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        FAILED: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        VALIDATING_REPOSITORY: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
        RUNNING_QUOTA_VALIDATION: _ClassVar[DeploymentOperationMetadata.DeploymentStep]
    DEPLOYMENT_STEP_UNSPECIFIED: DeploymentOperationMetadata.DeploymentStep
    PREPARING_STORAGE_BUCKET: DeploymentOperationMetadata.DeploymentStep
    DOWNLOADING_BLUEPRINT: DeploymentOperationMetadata.DeploymentStep
    RUNNING_TF_INIT: DeploymentOperationMetadata.DeploymentStep
    RUNNING_TF_PLAN: DeploymentOperationMetadata.DeploymentStep
    RUNNING_TF_APPLY: DeploymentOperationMetadata.DeploymentStep
    RUNNING_TF_DESTROY: DeploymentOperationMetadata.DeploymentStep
    RUNNING_TF_VALIDATE: DeploymentOperationMetadata.DeploymentStep
    UNLOCKING_DEPLOYMENT: DeploymentOperationMetadata.DeploymentStep
    SUCCEEDED: DeploymentOperationMetadata.DeploymentStep
    FAILED: DeploymentOperationMetadata.DeploymentStep
    VALIDATING_REPOSITORY: DeploymentOperationMetadata.DeploymentStep
    RUNNING_QUOTA_VALIDATION: DeploymentOperationMetadata.DeploymentStep
    STEP_FIELD_NUMBER: _ClassVar[int]
    APPLY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    step: DeploymentOperationMetadata.DeploymentStep
    apply_results: ApplyResults
    build: str
    logs: str
    def __init__(self, step: _Optional[_Union[DeploymentOperationMetadata.DeploymentStep, str]] = ..., apply_results: _Optional[_Union[ApplyResults, _Mapping]] = ..., build: _Optional[str] = ..., logs: _Optional[str] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("name", "terraform_info", "cai_assets", "intent", "state")
    class Intent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTENT_UNSPECIFIED: _ClassVar[Resource.Intent]
        CREATE: _ClassVar[Resource.Intent]
        UPDATE: _ClassVar[Resource.Intent]
        DELETE: _ClassVar[Resource.Intent]
        RECREATE: _ClassVar[Resource.Intent]
        UNCHANGED: _ClassVar[Resource.Intent]
    INTENT_UNSPECIFIED: Resource.Intent
    CREATE: Resource.Intent
    UPDATE: Resource.Intent
    DELETE: Resource.Intent
    RECREATE: Resource.Intent
    UNCHANGED: Resource.Intent
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Resource.State]
        PLANNED: _ClassVar[Resource.State]
        IN_PROGRESS: _ClassVar[Resource.State]
        RECONCILED: _ClassVar[Resource.State]
        FAILED: _ClassVar[Resource.State]
    STATE_UNSPECIFIED: Resource.State
    PLANNED: Resource.State
    IN_PROGRESS: Resource.State
    RECONCILED: Resource.State
    FAILED: Resource.State
    class CaiAssetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ResourceCAIInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ResourceCAIInfo, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERRAFORM_INFO_FIELD_NUMBER: _ClassVar[int]
    CAI_ASSETS_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    terraform_info: ResourceTerraformInfo
    cai_assets: _containers.MessageMap[str, ResourceCAIInfo]
    intent: Resource.Intent
    state: Resource.State
    def __init__(self, name: _Optional[str] = ..., terraform_info: _Optional[_Union[ResourceTerraformInfo, _Mapping]] = ..., cai_assets: _Optional[_Mapping[str, ResourceCAIInfo]] = ..., intent: _Optional[_Union[Resource.Intent, str]] = ..., state: _Optional[_Union[Resource.State, str]] = ...) -> None: ...

class ResourceTerraformInfo(_message.Message):
    __slots__ = ("address", "type", "id")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    type: str
    id: str
    def __init__(self, address: _Optional[str] = ..., type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ResourceCAIInfo(_message.Message):
    __slots__ = ("full_resource_name",)
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    full_resource_name: str
    def __init__(self, full_resource_name: _Optional[str] = ...) -> None: ...

class GetResourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListResourcesRequest(_message.Message):
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

class ListResourcesResponse(_message.Message):
    __slots__ = ("resources", "next_page_token", "unreachable")
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Resource]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resources: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class Statefile(_message.Message):
    __slots__ = ("signed_uri",)
    SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    signed_uri: str
    def __init__(self, signed_uri: _Optional[str] = ...) -> None: ...

class ExportDeploymentStatefileRequest(_message.Message):
    __slots__ = ("parent", "draft")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    draft: bool
    def __init__(self, parent: _Optional[str] = ..., draft: bool = ...) -> None: ...

class ExportRevisionStatefileRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ImportStatefileRequest(_message.Message):
    __slots__ = ("parent", "lock_id", "skip_draft")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_DRAFT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lock_id: int
    skip_draft: bool
    def __init__(self, parent: _Optional[str] = ..., lock_id: _Optional[int] = ..., skip_draft: bool = ...) -> None: ...

class DeleteStatefileRequest(_message.Message):
    __slots__ = ("name", "lock_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    lock_id: int
    def __init__(self, name: _Optional[str] = ..., lock_id: _Optional[int] = ...) -> None: ...

class LockDeploymentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UnlockDeploymentRequest(_message.Message):
    __slots__ = ("name", "lock_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    lock_id: int
    def __init__(self, name: _Optional[str] = ..., lock_id: _Optional[int] = ...) -> None: ...

class ExportLockInfoRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LockInfo(_message.Message):
    __slots__ = ("lock_id", "operation", "info", "who", "version", "create_time")
    LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    WHO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    lock_id: int
    operation: str
    info: str
    who: str
    version: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, lock_id: _Optional[int] = ..., operation: _Optional[str] = ..., info: _Optional[str] = ..., who: _Optional[str] = ..., version: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Preview(_message.Message):
    __slots__ = ("terraform_blueprint", "name", "create_time", "labels", "state", "deployment", "preview_mode", "service_account", "artifacts_gcs_bucket", "worker_pool", "error_code", "error_status", "build", "tf_errors", "error_logs", "preview_artifacts", "logs", "tf_version", "tf_version_constraint", "annotations")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Preview.State]
        CREATING: _ClassVar[Preview.State]
        SUCCEEDED: _ClassVar[Preview.State]
        APPLYING: _ClassVar[Preview.State]
        STALE: _ClassVar[Preview.State]
        DELETING: _ClassVar[Preview.State]
        FAILED: _ClassVar[Preview.State]
        DELETED: _ClassVar[Preview.State]
    STATE_UNSPECIFIED: Preview.State
    CREATING: Preview.State
    SUCCEEDED: Preview.State
    APPLYING: Preview.State
    STALE: Preview.State
    DELETING: Preview.State
    FAILED: Preview.State
    DELETED: Preview.State
    class PreviewMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREVIEW_MODE_UNSPECIFIED: _ClassVar[Preview.PreviewMode]
        DEFAULT: _ClassVar[Preview.PreviewMode]
        DELETE: _ClassVar[Preview.PreviewMode]
    PREVIEW_MODE_UNSPECIFIED: Preview.PreviewMode
    DEFAULT: Preview.PreviewMode
    DELETE: Preview.PreviewMode
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[Preview.ErrorCode]
        CLOUD_BUILD_PERMISSION_DENIED: _ClassVar[Preview.ErrorCode]
        BUCKET_CREATION_PERMISSION_DENIED: _ClassVar[Preview.ErrorCode]
        BUCKET_CREATION_FAILED: _ClassVar[Preview.ErrorCode]
        DEPLOYMENT_LOCK_ACQUIRE_FAILED: _ClassVar[Preview.ErrorCode]
        PREVIEW_BUILD_API_FAILED: _ClassVar[Preview.ErrorCode]
        PREVIEW_BUILD_RUN_FAILED: _ClassVar[Preview.ErrorCode]
    ERROR_CODE_UNSPECIFIED: Preview.ErrorCode
    CLOUD_BUILD_PERMISSION_DENIED: Preview.ErrorCode
    BUCKET_CREATION_PERMISSION_DENIED: Preview.ErrorCode
    BUCKET_CREATION_FAILED: Preview.ErrorCode
    DEPLOYMENT_LOCK_ACQUIRE_FAILED: Preview.ErrorCode
    PREVIEW_BUILD_API_FAILED: Preview.ErrorCode
    PREVIEW_BUILD_RUN_FAILED: Preview.ErrorCode
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
    TERRAFORM_BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_MODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    TF_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOGS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_FIELD_NUMBER: _ClassVar[int]
    TF_VERSION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    terraform_blueprint: TerraformBlueprint
    name: str
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Preview.State
    deployment: str
    preview_mode: Preview.PreviewMode
    service_account: str
    artifacts_gcs_bucket: str
    worker_pool: str
    error_code: Preview.ErrorCode
    error_status: _status_pb2.Status
    build: str
    tf_errors: _containers.RepeatedCompositeFieldContainer[TerraformError]
    error_logs: str
    preview_artifacts: PreviewArtifacts
    logs: str
    tf_version: str
    tf_version_constraint: str
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, terraform_blueprint: _Optional[_Union[TerraformBlueprint, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[Preview.State, str]] = ..., deployment: _Optional[str] = ..., preview_mode: _Optional[_Union[Preview.PreviewMode, str]] = ..., service_account: _Optional[str] = ..., artifacts_gcs_bucket: _Optional[str] = ..., worker_pool: _Optional[str] = ..., error_code: _Optional[_Union[Preview.ErrorCode, str]] = ..., error_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., build: _Optional[str] = ..., tf_errors: _Optional[_Iterable[_Union[TerraformError, _Mapping]]] = ..., error_logs: _Optional[str] = ..., preview_artifacts: _Optional[_Union[PreviewArtifacts, _Mapping]] = ..., logs: _Optional[str] = ..., tf_version: _Optional[str] = ..., tf_version_constraint: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PreviewOperationMetadata(_message.Message):
    __slots__ = ("step", "preview_artifacts", "logs", "build")
    class PreviewStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREVIEW_STEP_UNSPECIFIED: _ClassVar[PreviewOperationMetadata.PreviewStep]
        PREPARING_STORAGE_BUCKET: _ClassVar[PreviewOperationMetadata.PreviewStep]
        DOWNLOADING_BLUEPRINT: _ClassVar[PreviewOperationMetadata.PreviewStep]
        RUNNING_TF_INIT: _ClassVar[PreviewOperationMetadata.PreviewStep]
        RUNNING_TF_PLAN: _ClassVar[PreviewOperationMetadata.PreviewStep]
        FETCHING_DEPLOYMENT: _ClassVar[PreviewOperationMetadata.PreviewStep]
        LOCKING_DEPLOYMENT: _ClassVar[PreviewOperationMetadata.PreviewStep]
        UNLOCKING_DEPLOYMENT: _ClassVar[PreviewOperationMetadata.PreviewStep]
        SUCCEEDED: _ClassVar[PreviewOperationMetadata.PreviewStep]
        FAILED: _ClassVar[PreviewOperationMetadata.PreviewStep]
        VALIDATING_REPOSITORY: _ClassVar[PreviewOperationMetadata.PreviewStep]
    PREVIEW_STEP_UNSPECIFIED: PreviewOperationMetadata.PreviewStep
    PREPARING_STORAGE_BUCKET: PreviewOperationMetadata.PreviewStep
    DOWNLOADING_BLUEPRINT: PreviewOperationMetadata.PreviewStep
    RUNNING_TF_INIT: PreviewOperationMetadata.PreviewStep
    RUNNING_TF_PLAN: PreviewOperationMetadata.PreviewStep
    FETCHING_DEPLOYMENT: PreviewOperationMetadata.PreviewStep
    LOCKING_DEPLOYMENT: PreviewOperationMetadata.PreviewStep
    UNLOCKING_DEPLOYMENT: PreviewOperationMetadata.PreviewStep
    SUCCEEDED: PreviewOperationMetadata.PreviewStep
    FAILED: PreviewOperationMetadata.PreviewStep
    VALIDATING_REPOSITORY: PreviewOperationMetadata.PreviewStep
    STEP_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    step: PreviewOperationMetadata.PreviewStep
    preview_artifacts: PreviewArtifacts
    logs: str
    build: str
    def __init__(self, step: _Optional[_Union[PreviewOperationMetadata.PreviewStep, str]] = ..., preview_artifacts: _Optional[_Union[PreviewArtifacts, _Mapping]] = ..., logs: _Optional[str] = ..., build: _Optional[str] = ...) -> None: ...

class PreviewArtifacts(_message.Message):
    __slots__ = ("content", "artifacts")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    content: str
    artifacts: str
    def __init__(self, content: _Optional[str] = ..., artifacts: _Optional[str] = ...) -> None: ...

class CreatePreviewRequest(_message.Message):
    __slots__ = ("parent", "preview_id", "preview", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    preview_id: str
    preview: Preview
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., preview_id: _Optional[str] = ..., preview: _Optional[_Union[Preview, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetPreviewRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPreviewsRequest(_message.Message):
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

class ListPreviewsResponse(_message.Message):
    __slots__ = ("previews", "next_page_token", "unreachable")
    PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    previews: _containers.RepeatedCompositeFieldContainer[Preview]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, previews: _Optional[_Iterable[_Union[Preview, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class DeletePreviewRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ExportPreviewResultRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ExportPreviewResultResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: PreviewResult
    def __init__(self, result: _Optional[_Union[PreviewResult, _Mapping]] = ...) -> None: ...

class PreviewResult(_message.Message):
    __slots__ = ("binary_signed_uri", "json_signed_uri")
    BINARY_SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    JSON_SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    binary_signed_uri: str
    json_signed_uri: str
    def __init__(self, binary_signed_uri: _Optional[str] = ..., json_signed_uri: _Optional[str] = ...) -> None: ...

class GetTerraformVersionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTerraformVersionsRequest(_message.Message):
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

class ListTerraformVersionsResponse(_message.Message):
    __slots__ = ("terraform_versions", "next_page_token", "unreachable")
    TERRAFORM_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    terraform_versions: _containers.RepeatedCompositeFieldContainer[TerraformVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, terraform_versions: _Optional[_Iterable[_Union[TerraformVersion, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class TerraformVersion(_message.Message):
    __slots__ = ("name", "state", "support_time", "deprecate_time", "obsolete_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[TerraformVersion.State]
        ACTIVE: _ClassVar[TerraformVersion.State]
        DEPRECATED: _ClassVar[TerraformVersion.State]
        OBSOLETE: _ClassVar[TerraformVersion.State]
    STATE_UNSPECIFIED: TerraformVersion.State
    ACTIVE: TerraformVersion.State
    DEPRECATED: TerraformVersion.State
    OBSOLETE: TerraformVersion.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATE_TIME_FIELD_NUMBER: _ClassVar[int]
    OBSOLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: TerraformVersion.State
    support_time: _timestamp_pb2.Timestamp
    deprecate_time: _timestamp_pb2.Timestamp
    obsolete_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[TerraformVersion.State, str]] = ..., support_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deprecate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., obsolete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
