from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.clouddms.v1 import clouddms_resources_pb2 as _clouddms_resources_pb2
from google.cloud.clouddms.v1 import conversionworkspace_resources_pb2 as _conversionworkspace_resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseEntityView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ENTITY_VIEW_UNSPECIFIED: _ClassVar[DatabaseEntityView]
    DATABASE_ENTITY_VIEW_BASIC: _ClassVar[DatabaseEntityView]
    DATABASE_ENTITY_VIEW_FULL: _ClassVar[DatabaseEntityView]
    DATABASE_ENTITY_VIEW_ROOT_SUMMARY: _ClassVar[DatabaseEntityView]
DATABASE_ENTITY_VIEW_UNSPECIFIED: DatabaseEntityView
DATABASE_ENTITY_VIEW_BASIC: DatabaseEntityView
DATABASE_ENTITY_VIEW_FULL: DatabaseEntityView
DATABASE_ENTITY_VIEW_ROOT_SUMMARY: DatabaseEntityView

class ListMigrationJobsRequest(_message.Message):
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

class ListMigrationJobsResponse(_message.Message):
    __slots__ = ("migration_jobs", "next_page_token", "unreachable")
    MIGRATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    migration_jobs: _containers.RepeatedCompositeFieldContainer[_clouddms_resources_pb2.MigrationJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, migration_jobs: _Optional[_Iterable[_Union[_clouddms_resources_pb2.MigrationJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMigrationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateMigrationJobRequest(_message.Message):
    __slots__ = ("parent", "migration_job_id", "migration_job", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    migration_job_id: str
    migration_job: _clouddms_resources_pb2.MigrationJob
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., migration_job_id: _Optional[str] = ..., migration_job: _Optional[_Union[_clouddms_resources_pb2.MigrationJob, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateMigrationJobRequest(_message.Message):
    __slots__ = ("update_mask", "migration_job", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    migration_job: _clouddms_resources_pb2.MigrationJob
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., migration_job: _Optional[_Union[_clouddms_resources_pb2.MigrationJob, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteMigrationJobRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class StartMigrationJobRequest(_message.Message):
    __slots__ = ("name", "skip_validation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    skip_validation: bool
    def __init__(self, name: _Optional[str] = ..., skip_validation: bool = ...) -> None: ...

class StopMigrationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeMigrationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PromoteMigrationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class VerifyMigrationJobRequest(_message.Message):
    __slots__ = ("name", "update_mask", "migration_job")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    migration_job: _clouddms_resources_pb2.MigrationJob
    def __init__(self, name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., migration_job: _Optional[_Union[_clouddms_resources_pb2.MigrationJob, _Mapping]] = ...) -> None: ...

class RestartMigrationJobRequest(_message.Message):
    __slots__ = ("name", "skip_validation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    skip_validation: bool
    def __init__(self, name: _Optional[str] = ..., skip_validation: bool = ...) -> None: ...

class GenerateSshScriptRequest(_message.Message):
    __slots__ = ("migration_job", "vm", "vm_creation_config", "vm_selection_config", "vm_port")
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    VM_CREATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VM_SELECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VM_PORT_FIELD_NUMBER: _ClassVar[int]
    migration_job: str
    vm: str
    vm_creation_config: VmCreationConfig
    vm_selection_config: VmSelectionConfig
    vm_port: int
    def __init__(self, migration_job: _Optional[str] = ..., vm: _Optional[str] = ..., vm_creation_config: _Optional[_Union[VmCreationConfig, _Mapping]] = ..., vm_selection_config: _Optional[_Union[VmSelectionConfig, _Mapping]] = ..., vm_port: _Optional[int] = ...) -> None: ...

class VmCreationConfig(_message.Message):
    __slots__ = ("vm_machine_type", "vm_zone", "subnet")
    VM_MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_ZONE_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    vm_machine_type: str
    vm_zone: str
    subnet: str
    def __init__(self, vm_machine_type: _Optional[str] = ..., vm_zone: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...

class VmSelectionConfig(_message.Message):
    __slots__ = ("vm_zone",)
    VM_ZONE_FIELD_NUMBER: _ClassVar[int]
    vm_zone: str
    def __init__(self, vm_zone: _Optional[str] = ...) -> None: ...

class SshScript(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: str
    def __init__(self, script: _Optional[str] = ...) -> None: ...

class GenerateTcpProxyScriptRequest(_message.Message):
    __slots__ = ("migration_job", "vm_name", "vm_machine_type", "vm_zone", "vm_subnet")
    MIGRATION_JOB_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_ZONE_FIELD_NUMBER: _ClassVar[int]
    VM_SUBNET_FIELD_NUMBER: _ClassVar[int]
    migration_job: str
    vm_name: str
    vm_machine_type: str
    vm_zone: str
    vm_subnet: str
    def __init__(self, migration_job: _Optional[str] = ..., vm_name: _Optional[str] = ..., vm_machine_type: _Optional[str] = ..., vm_zone: _Optional[str] = ..., vm_subnet: _Optional[str] = ...) -> None: ...

class TcpProxyScript(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: str
    def __init__(self, script: _Optional[str] = ...) -> None: ...

class ListConnectionProfilesRequest(_message.Message):
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

class ListConnectionProfilesResponse(_message.Message):
    __slots__ = ("connection_profiles", "next_page_token", "unreachable")
    CONNECTION_PROFILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connection_profiles: _containers.RepeatedCompositeFieldContainer[_clouddms_resources_pb2.ConnectionProfile]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection_profiles: _Optional[_Iterable[_Union[_clouddms_resources_pb2.ConnectionProfile, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConnectionProfileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateConnectionProfileRequest(_message.Message):
    __slots__ = ("parent", "connection_profile_id", "connection_profile", "request_id", "validate_only", "skip_validation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_profile_id: str
    connection_profile: _clouddms_resources_pb2.ConnectionProfile
    request_id: str
    validate_only: bool
    skip_validation: bool
    def __init__(self, parent: _Optional[str] = ..., connection_profile_id: _Optional[str] = ..., connection_profile: _Optional[_Union[_clouddms_resources_pb2.ConnectionProfile, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., skip_validation: bool = ...) -> None: ...

class UpdateConnectionProfileRequest(_message.Message):
    __slots__ = ("update_mask", "connection_profile", "request_id", "validate_only", "skip_validation")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    connection_profile: _clouddms_resources_pb2.ConnectionProfile
    request_id: str
    validate_only: bool
    skip_validation: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., connection_profile: _Optional[_Union[_clouddms_resources_pb2.ConnectionProfile, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., skip_validation: bool = ...) -> None: ...

class DeleteConnectionProfileRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class CreatePrivateConnectionRequest(_message.Message):
    __slots__ = ("parent", "private_connection_id", "private_connection", "request_id", "skip_validation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_connection_id: str
    private_connection: _clouddms_resources_pb2.PrivateConnection
    request_id: str
    skip_validation: bool
    def __init__(self, parent: _Optional[str] = ..., private_connection_id: _Optional[str] = ..., private_connection: _Optional[_Union[_clouddms_resources_pb2.PrivateConnection, _Mapping]] = ..., request_id: _Optional[str] = ..., skip_validation: bool = ...) -> None: ...

class ListPrivateConnectionsRequest(_message.Message):
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

class ListPrivateConnectionsResponse(_message.Message):
    __slots__ = ("private_connections", "next_page_token", "unreachable")
    PRIVATE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    private_connections: _containers.RepeatedCompositeFieldContainer[_clouddms_resources_pb2.PrivateConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, private_connections: _Optional[_Iterable[_Union[_clouddms_resources_pb2.PrivateConnection, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class DeletePrivateConnectionRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetPrivateConnectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
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
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class ListConversionWorkspacesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListConversionWorkspacesResponse(_message.Message):
    __slots__ = ("conversion_workspaces", "next_page_token", "unreachable")
    CONVERSION_WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    conversion_workspaces: _containers.RepeatedCompositeFieldContainer[_conversionworkspace_resources_pb2.ConversionWorkspace]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, conversion_workspaces: _Optional[_Iterable[_Union[_conversionworkspace_resources_pb2.ConversionWorkspace, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateConversionWorkspaceRequest(_message.Message):
    __slots__ = ("parent", "conversion_workspace_id", "conversion_workspace", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversion_workspace_id: str
    conversion_workspace: _conversionworkspace_resources_pb2.ConversionWorkspace
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., conversion_workspace_id: _Optional[str] = ..., conversion_workspace: _Optional[_Union[_conversionworkspace_resources_pb2.ConversionWorkspace, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class UpdateConversionWorkspaceRequest(_message.Message):
    __slots__ = ("update_mask", "conversion_workspace", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    conversion_workspace: _conversionworkspace_resources_pb2.ConversionWorkspace
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., conversion_workspace: _Optional[_Union[_conversionworkspace_resources_pb2.ConversionWorkspace, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class CommitConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name", "commit_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_name: str
    def __init__(self, name: _Optional[str] = ..., commit_name: _Optional[str] = ...) -> None: ...

class RollbackConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ApplyConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name", "filter", "dry_run", "auto_commit", "connection_profile")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    dry_run: bool
    auto_commit: bool
    connection_profile: str
    def __init__(self, name: _Optional[str] = ..., filter: _Optional[str] = ..., dry_run: bool = ..., auto_commit: bool = ..., connection_profile: _Optional[str] = ...) -> None: ...

class ListMappingRulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMappingRulesResponse(_message.Message):
    __slots__ = ("mapping_rules", "next_page_token")
    MAPPING_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    mapping_rules: _containers.RepeatedCompositeFieldContainer[_conversionworkspace_resources_pb2.MappingRule]
    next_page_token: str
    def __init__(self, mapping_rules: _Optional[_Iterable[_Union[_conversionworkspace_resources_pb2.MappingRule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetMappingRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SeedConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name", "auto_commit", "source_connection_profile", "destination_connection_profile")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CONNECTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    name: str
    auto_commit: bool
    source_connection_profile: str
    destination_connection_profile: str
    def __init__(self, name: _Optional[str] = ..., auto_commit: bool = ..., source_connection_profile: _Optional[str] = ..., destination_connection_profile: _Optional[str] = ...) -> None: ...

class ConvertConversionWorkspaceRequest(_message.Message):
    __slots__ = ("name", "auto_commit", "filter", "convert_full_path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CONVERT_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    auto_commit: bool
    filter: str
    convert_full_path: bool
    def __init__(self, name: _Optional[str] = ..., auto_commit: bool = ..., filter: _Optional[str] = ..., convert_full_path: bool = ...) -> None: ...

class ImportMappingRulesRequest(_message.Message):
    __slots__ = ("parent", "rules_format", "rules_files", "auto_commit")
    class RulesFile(_message.Message):
        __slots__ = ("rules_source_filename", "rules_content")
        RULES_SOURCE_FILENAME_FIELD_NUMBER: _ClassVar[int]
        RULES_CONTENT_FIELD_NUMBER: _ClassVar[int]
        rules_source_filename: str
        rules_content: str
        def __init__(self, rules_source_filename: _Optional[str] = ..., rules_content: _Optional[str] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULES_FORMAT_FIELD_NUMBER: _ClassVar[int]
    RULES_FILES_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rules_format: _conversionworkspace_resources_pb2.ImportRulesFileFormat
    rules_files: _containers.RepeatedCompositeFieldContainer[ImportMappingRulesRequest.RulesFile]
    auto_commit: bool
    def __init__(self, parent: _Optional[str] = ..., rules_format: _Optional[_Union[_conversionworkspace_resources_pb2.ImportRulesFileFormat, str]] = ..., rules_files: _Optional[_Iterable[_Union[ImportMappingRulesRequest.RulesFile, _Mapping]]] = ..., auto_commit: bool = ...) -> None: ...

class DescribeDatabaseEntitiesRequest(_message.Message):
    __slots__ = ("conversion_workspace", "page_size", "page_token", "tree", "uncommitted", "commit_id", "filter", "view")
    class DBTreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DB_TREE_TYPE_UNSPECIFIED: _ClassVar[DescribeDatabaseEntitiesRequest.DBTreeType]
        SOURCE_TREE: _ClassVar[DescribeDatabaseEntitiesRequest.DBTreeType]
        DRAFT_TREE: _ClassVar[DescribeDatabaseEntitiesRequest.DBTreeType]
        DESTINATION_TREE: _ClassVar[DescribeDatabaseEntitiesRequest.DBTreeType]
    DB_TREE_TYPE_UNSPECIFIED: DescribeDatabaseEntitiesRequest.DBTreeType
    SOURCE_TREE: DescribeDatabaseEntitiesRequest.DBTreeType
    DRAFT_TREE: DescribeDatabaseEntitiesRequest.DBTreeType
    DESTINATION_TREE: DescribeDatabaseEntitiesRequest.DBTreeType
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TREE_FIELD_NUMBER: _ClassVar[int]
    UNCOMMITTED_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    conversion_workspace: str
    page_size: int
    page_token: str
    tree: DescribeDatabaseEntitiesRequest.DBTreeType
    uncommitted: bool
    commit_id: str
    filter: str
    view: DatabaseEntityView
    def __init__(self, conversion_workspace: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., tree: _Optional[_Union[DescribeDatabaseEntitiesRequest.DBTreeType, str]] = ..., uncommitted: bool = ..., commit_id: _Optional[str] = ..., filter: _Optional[str] = ..., view: _Optional[_Union[DatabaseEntityView, str]] = ...) -> None: ...

class DescribeDatabaseEntitiesResponse(_message.Message):
    __slots__ = ("database_entities", "next_page_token")
    DATABASE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    database_entities: _containers.RepeatedCompositeFieldContainer[_conversionworkspace_resources_pb2.DatabaseEntity]
    next_page_token: str
    def __init__(self, database_entities: _Optional[_Iterable[_Union[_conversionworkspace_resources_pb2.DatabaseEntity, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchBackgroundJobsRequest(_message.Message):
    __slots__ = ("conversion_workspace", "return_most_recent_per_job_type", "max_size", "completed_until_time")
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    RETURN_MOST_RECENT_PER_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    conversion_workspace: str
    return_most_recent_per_job_type: bool
    max_size: int
    completed_until_time: _timestamp_pb2.Timestamp
    def __init__(self, conversion_workspace: _Optional[str] = ..., return_most_recent_per_job_type: bool = ..., max_size: _Optional[int] = ..., completed_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchBackgroundJobsResponse(_message.Message):
    __slots__ = ("jobs",)
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_conversionworkspace_resources_pb2.BackgroundJobLogEntry]
    def __init__(self, jobs: _Optional[_Iterable[_Union[_conversionworkspace_resources_pb2.BackgroundJobLogEntry, _Mapping]]] = ...) -> None: ...

class DescribeConversionWorkspaceRevisionsRequest(_message.Message):
    __slots__ = ("conversion_workspace", "commit_id")
    CONVERSION_WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    conversion_workspace: str
    commit_id: str
    def __init__(self, conversion_workspace: _Optional[str] = ..., commit_id: _Optional[str] = ...) -> None: ...

class DescribeConversionWorkspaceRevisionsResponse(_message.Message):
    __slots__ = ("revisions",)
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[_conversionworkspace_resources_pb2.ConversionWorkspace]
    def __init__(self, revisions: _Optional[_Iterable[_Union[_conversionworkspace_resources_pb2.ConversionWorkspace, _Mapping]]] = ...) -> None: ...

class CreateMappingRuleRequest(_message.Message):
    __slots__ = ("parent", "mapping_rule_id", "mapping_rule", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MAPPING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPING_RULE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    mapping_rule_id: str
    mapping_rule: _conversionworkspace_resources_pb2.MappingRule
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., mapping_rule_id: _Optional[str] = ..., mapping_rule: _Optional[_Union[_conversionworkspace_resources_pb2.MappingRule, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteMappingRuleRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class FetchStaticIpsRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class FetchStaticIpsResponse(_message.Message):
    __slots__ = ("static_ips", "next_page_token")
    STATIC_IPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    static_ips: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str
    def __init__(self, static_ips: _Optional[_Iterable[str]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
