from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
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

class Instance(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'private_config', 'state', 'state_note', 'kms_key', 'host_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        PAUSED: _ClassVar[Instance.State]
        UNKNOWN: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    DELETING: Instance.State
    PAUSED: Instance.State
    UNKNOWN: Instance.State

    class StateNote(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NOTE_UNSPECIFIED: _ClassVar[Instance.StateNote]
        PAUSED_CMEK_UNAVAILABLE: _ClassVar[Instance.StateNote]
        INSTANCE_RESUMING: _ClassVar[Instance.StateNote]
    STATE_NOTE_UNSPECIFIED: Instance.StateNote
    PAUSED_CMEK_UNAVAILABLE: Instance.StateNote
    INSTANCE_RESUMING: Instance.StateNote

    class HostConfig(_message.Message):
        __slots__ = ('html', 'api', 'git_http', 'git_ssh')
        HTML_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        GIT_HTTP_FIELD_NUMBER: _ClassVar[int]
        GIT_SSH_FIELD_NUMBER: _ClassVar[int]
        html: str
        api: str
        git_http: str
        git_ssh: str

        def __init__(self, html: _Optional[str]=..., api: _Optional[str]=..., git_http: _Optional[str]=..., git_ssh: _Optional[str]=...) -> None:
            ...

    class PrivateConfig(_message.Message):
        __slots__ = ('is_private', 'ca_pool', 'http_service_attachment', 'ssh_service_attachment', 'psc_allowed_projects')
        IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        CA_POOL_FIELD_NUMBER: _ClassVar[int]
        HTTP_SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        SSH_SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        PSC_ALLOWED_PROJECTS_FIELD_NUMBER: _ClassVar[int]
        is_private: bool
        ca_pool: str
        http_service_attachment: str
        ssh_service_attachment: str
        psc_allowed_projects: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, is_private: bool=..., ca_pool: _Optional[str]=..., http_service_attachment: _Optional[str]=..., ssh_service_attachment: _Optional[str]=..., psc_allowed_projects: _Optional[_Iterable[str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_NOTE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    private_config: Instance.PrivateConfig
    state: Instance.State
    state_note: Instance.StateNote
    kms_key: str
    host_config: Instance.HostConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., private_config: _Optional[_Union[Instance.PrivateConfig, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., state_note: _Optional[_Union[Instance.StateNote, str]]=..., kms_key: _Optional[str]=..., host_config: _Optional[_Union[Instance.HostConfig, _Mapping]]=...) -> None:
        ...

class Repository(_message.Message):
    __slots__ = ('name', 'description', 'instance', 'uid', 'create_time', 'update_time', 'etag', 'uris', 'initial_config')

    class URIs(_message.Message):
        __slots__ = ('html', 'git_https', 'api')
        HTML_FIELD_NUMBER: _ClassVar[int]
        GIT_HTTPS_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        html: str
        git_https: str
        api: str

        def __init__(self, html: _Optional[str]=..., git_https: _Optional[str]=..., api: _Optional[str]=...) -> None:
            ...

    class InitialConfig(_message.Message):
        __slots__ = ('default_branch', 'gitignores', 'license', 'readme')
        DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
        GITIGNORES_FIELD_NUMBER: _ClassVar[int]
        LICENSE_FIELD_NUMBER: _ClassVar[int]
        README_FIELD_NUMBER: _ClassVar[int]
        default_branch: str
        gitignores: _containers.RepeatedScalarFieldContainer[str]
        license: str
        readme: str

        def __init__(self, default_branch: _Optional[str]=..., gitignores: _Optional[_Iterable[str]]=..., license: _Optional[str]=..., readme: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    URIS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    instance: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    uris: Repository.URIs
    initial_config: Repository.InitialConfig

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., instance: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., uris: _Optional[_Union[Repository.URIs, _Mapping]]=..., initial_config: _Optional[_Union[Repository.InitialConfig, _Mapping]]=...) -> None:
        ...

class BranchRule(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'annotations', 'etag', 'include_pattern', 'disabled', 'require_pull_request', 'minimum_reviews_count', 'minimum_approvals_count', 'require_comments_resolved', 'allow_stale_reviews', 'require_linear_history', 'required_status_checks')

    class Check(_message.Message):
        __slots__ = ('context',)
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        context: str

        def __init__(self, context: _Optional[str]=...) -> None:
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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REVIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_APPROVALS_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_COMMENTS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_STALE_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_LINEAR_HISTORY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_STATUS_CHECKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    include_pattern: str
    disabled: bool
    require_pull_request: bool
    minimum_reviews_count: int
    minimum_approvals_count: int
    require_comments_resolved: bool
    allow_stale_reviews: bool
    require_linear_history: bool
    required_status_checks: _containers.RepeatedCompositeFieldContainer[BranchRule.Check]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., include_pattern: _Optional[str]=..., disabled: bool=..., require_pull_request: bool=..., minimum_reviews_count: _Optional[int]=..., minimum_approvals_count: _Optional[int]=..., require_comments_resolved: bool=..., allow_stale_reviews: bool=..., require_linear_history: bool=..., required_status_checks: _Optional[_Iterable[_Union[BranchRule.Check, _Mapping]]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    request_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
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

class ListRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    instance: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., instance: _Optional[str]=...) -> None:
        ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRepositoryRequest(_message.Message):
    __slots__ = ('parent', 'repository', 'repository_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repository: Repository
    repository_id: str

    def __init__(self, parent: _Optional[str]=..., repository: _Optional[_Union[Repository, _Mapping]]=..., repository_id: _Optional[str]=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class GetBranchRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateBranchRuleRequest(_message.Message):
    __slots__ = ('parent', 'branch_rule', 'branch_rule_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_RULE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    branch_rule: BranchRule
    branch_rule_id: str

    def __init__(self, parent: _Optional[str]=..., branch_rule: _Optional[_Union[BranchRule, _Mapping]]=..., branch_rule_id: _Optional[str]=...) -> None:
        ...

class ListBranchRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class DeleteBranchRuleRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class UpdateBranchRuleRequest(_message.Message):
    __slots__ = ('branch_rule', 'validate_only', 'update_mask')
    BRANCH_RULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    branch_rule: BranchRule
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, branch_rule: _Optional[_Union[BranchRule, _Mapping]]=..., validate_only: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListBranchRulesResponse(_message.Message):
    __slots__ = ('branch_rules', 'next_page_token')
    BRANCH_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    branch_rules: _containers.RepeatedCompositeFieldContainer[BranchRule]
    next_page_token: str

    def __init__(self, branch_rules: _Optional[_Iterable[_Union[BranchRule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...