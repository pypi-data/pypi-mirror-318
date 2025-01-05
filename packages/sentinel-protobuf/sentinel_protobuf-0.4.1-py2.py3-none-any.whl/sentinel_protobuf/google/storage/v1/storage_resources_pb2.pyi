from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Bucket(_message.Message):
    __slots__ = ('acl', 'default_object_acl', 'lifecycle', 'time_created', 'id', 'name', 'project_number', 'metageneration', 'cors', 'location', 'storage_class', 'etag', 'updated', 'default_event_based_hold', 'labels', 'website', 'versioning', 'logging', 'owner', 'encryption', 'billing', 'retention_policy', 'location_type', 'iam_configuration', 'zone_affinity', 'satisfies_pzs', 'autoclass')

    class Billing(_message.Message):
        __slots__ = ('requester_pays',)
        REQUESTER_PAYS_FIELD_NUMBER: _ClassVar[int]
        requester_pays: bool

        def __init__(self, requester_pays: bool=...) -> None:
            ...

    class Cors(_message.Message):
        __slots__ = ('origin', 'method', 'response_header', 'max_age_seconds')
        ORIGIN_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_HEADER_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
        origin: _containers.RepeatedScalarFieldContainer[str]
        method: _containers.RepeatedScalarFieldContainer[str]
        response_header: _containers.RepeatedScalarFieldContainer[str]
        max_age_seconds: int

        def __init__(self, origin: _Optional[_Iterable[str]]=..., method: _Optional[_Iterable[str]]=..., response_header: _Optional[_Iterable[str]]=..., max_age_seconds: _Optional[int]=...) -> None:
            ...

    class Encryption(_message.Message):
        __slots__ = ('default_kms_key_name',)
        DEFAULT_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        default_kms_key_name: str

        def __init__(self, default_kms_key_name: _Optional[str]=...) -> None:
            ...

    class IamConfiguration(_message.Message):
        __slots__ = ('uniform_bucket_level_access', 'public_access_prevention')

        class PublicAccessPrevention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PUBLIC_ACCESS_PREVENTION_UNSPECIFIED: _ClassVar[Bucket.IamConfiguration.PublicAccessPrevention]
            ENFORCED: _ClassVar[Bucket.IamConfiguration.PublicAccessPrevention]
            INHERITED: _ClassVar[Bucket.IamConfiguration.PublicAccessPrevention]
        PUBLIC_ACCESS_PREVENTION_UNSPECIFIED: Bucket.IamConfiguration.PublicAccessPrevention
        ENFORCED: Bucket.IamConfiguration.PublicAccessPrevention
        INHERITED: Bucket.IamConfiguration.PublicAccessPrevention

        class UniformBucketLevelAccess(_message.Message):
            __slots__ = ('enabled', 'locked_time')
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            LOCKED_TIME_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            locked_time: _timestamp_pb2.Timestamp

            def __init__(self, enabled: bool=..., locked_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                ...
        UNIFORM_BUCKET_LEVEL_ACCESS_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_ACCESS_PREVENTION_FIELD_NUMBER: _ClassVar[int]
        uniform_bucket_level_access: Bucket.IamConfiguration.UniformBucketLevelAccess
        public_access_prevention: Bucket.IamConfiguration.PublicAccessPrevention

        def __init__(self, uniform_bucket_level_access: _Optional[_Union[Bucket.IamConfiguration.UniformBucketLevelAccess, _Mapping]]=..., public_access_prevention: _Optional[_Union[Bucket.IamConfiguration.PublicAccessPrevention, str]]=...) -> None:
            ...

    class Lifecycle(_message.Message):
        __slots__ = ('rule',)

        class Rule(_message.Message):
            __slots__ = ('action', 'condition')

            class Action(_message.Message):
                __slots__ = ('type', 'storage_class')
                TYPE_FIELD_NUMBER: _ClassVar[int]
                STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
                type: str
                storage_class: str

                def __init__(self, type: _Optional[str]=..., storage_class: _Optional[str]=...) -> None:
                    ...

            class Condition(_message.Message):
                __slots__ = ('age', 'created_before', 'is_live', 'num_newer_versions', 'matches_storage_class', 'matches_pattern', 'days_since_custom_time', 'custom_time_before', 'days_since_noncurrent_time', 'noncurrent_time_before', 'matches_prefix', 'matches_suffix')
                AGE_FIELD_NUMBER: _ClassVar[int]
                CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
                IS_LIVE_FIELD_NUMBER: _ClassVar[int]
                NUM_NEWER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
                MATCHES_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
                MATCHES_PATTERN_FIELD_NUMBER: _ClassVar[int]
                DAYS_SINCE_CUSTOM_TIME_FIELD_NUMBER: _ClassVar[int]
                CUSTOM_TIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
                DAYS_SINCE_NONCURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
                NONCURRENT_TIME_BEFORE_FIELD_NUMBER: _ClassVar[int]
                MATCHES_PREFIX_FIELD_NUMBER: _ClassVar[int]
                MATCHES_SUFFIX_FIELD_NUMBER: _ClassVar[int]
                age: int
                created_before: _timestamp_pb2.Timestamp
                is_live: _wrappers_pb2.BoolValue
                num_newer_versions: int
                matches_storage_class: _containers.RepeatedScalarFieldContainer[str]
                matches_pattern: str
                days_since_custom_time: int
                custom_time_before: _timestamp_pb2.Timestamp
                days_since_noncurrent_time: int
                noncurrent_time_before: _timestamp_pb2.Timestamp
                matches_prefix: _containers.RepeatedScalarFieldContainer[str]
                matches_suffix: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, age: _Optional[int]=..., created_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., is_live: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., num_newer_versions: _Optional[int]=..., matches_storage_class: _Optional[_Iterable[str]]=..., matches_pattern: _Optional[str]=..., days_since_custom_time: _Optional[int]=..., custom_time_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., days_since_noncurrent_time: _Optional[int]=..., noncurrent_time_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., matches_prefix: _Optional[_Iterable[str]]=..., matches_suffix: _Optional[_Iterable[str]]=...) -> None:
                    ...
            ACTION_FIELD_NUMBER: _ClassVar[int]
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            action: Bucket.Lifecycle.Rule.Action
            condition: Bucket.Lifecycle.Rule.Condition

            def __init__(self, action: _Optional[_Union[Bucket.Lifecycle.Rule.Action, _Mapping]]=..., condition: _Optional[_Union[Bucket.Lifecycle.Rule.Condition, _Mapping]]=...) -> None:
                ...
        RULE_FIELD_NUMBER: _ClassVar[int]
        rule: _containers.RepeatedCompositeFieldContainer[Bucket.Lifecycle.Rule]

        def __init__(self, rule: _Optional[_Iterable[_Union[Bucket.Lifecycle.Rule, _Mapping]]]=...) -> None:
            ...

    class Logging(_message.Message):
        __slots__ = ('log_bucket', 'log_object_prefix')
        LOG_BUCKET_FIELD_NUMBER: _ClassVar[int]
        LOG_OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
        log_bucket: str
        log_object_prefix: str

        def __init__(self, log_bucket: _Optional[str]=..., log_object_prefix: _Optional[str]=...) -> None:
            ...

    class RetentionPolicy(_message.Message):
        __slots__ = ('effective_time', 'is_locked', 'retention_period')
        EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
        IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
        RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
        effective_time: _timestamp_pb2.Timestamp
        is_locked: bool
        retention_period: int

        def __init__(self, effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., is_locked: bool=..., retention_period: _Optional[int]=...) -> None:
            ...

    class Versioning(_message.Message):
        __slots__ = ('enabled',)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool

        def __init__(self, enabled: bool=...) -> None:
            ...

    class Website(_message.Message):
        __slots__ = ('main_page_suffix', 'not_found_page')
        MAIN_PAGE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_PAGE_FIELD_NUMBER: _ClassVar[int]
        main_page_suffix: str
        not_found_page: str

        def __init__(self, main_page_suffix: _Optional[str]=..., not_found_page: _Optional[str]=...) -> None:
            ...

    class Autoclass(_message.Message):
        __slots__ = ('enabled', 'toggle_time')
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_TIME_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        toggle_time: _timestamp_pb2.Timestamp

        def __init__(self, enabled: bool=..., toggle_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ACL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_OBJECT_ACL_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CORS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EVENT_BASED_HOLD_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    VERSIONING_FIELD_NUMBER: _ClassVar[int]
    LOGGING_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    BILLING_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IAM_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ZONE_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    AUTOCLASS_FIELD_NUMBER: _ClassVar[int]
    acl: _containers.RepeatedCompositeFieldContainer[BucketAccessControl]
    default_object_acl: _containers.RepeatedCompositeFieldContainer[ObjectAccessControl]
    lifecycle: Bucket.Lifecycle
    time_created: _timestamp_pb2.Timestamp
    id: str
    name: str
    project_number: int
    metageneration: int
    cors: _containers.RepeatedCompositeFieldContainer[Bucket.Cors]
    location: str
    storage_class: str
    etag: str
    updated: _timestamp_pb2.Timestamp
    default_event_based_hold: bool
    labels: _containers.ScalarMap[str, str]
    website: Bucket.Website
    versioning: Bucket.Versioning
    logging: Bucket.Logging
    owner: Owner
    encryption: Bucket.Encryption
    billing: Bucket.Billing
    retention_policy: Bucket.RetentionPolicy
    location_type: str
    iam_configuration: Bucket.IamConfiguration
    zone_affinity: _containers.RepeatedScalarFieldContainer[str]
    satisfies_pzs: bool
    autoclass: Bucket.Autoclass

    def __init__(self, acl: _Optional[_Iterable[_Union[BucketAccessControl, _Mapping]]]=..., default_object_acl: _Optional[_Iterable[_Union[ObjectAccessControl, _Mapping]]]=..., lifecycle: _Optional[_Union[Bucket.Lifecycle, _Mapping]]=..., time_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., id: _Optional[str]=..., name: _Optional[str]=..., project_number: _Optional[int]=..., metageneration: _Optional[int]=..., cors: _Optional[_Iterable[_Union[Bucket.Cors, _Mapping]]]=..., location: _Optional[str]=..., storage_class: _Optional[str]=..., etag: _Optional[str]=..., updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., default_event_based_hold: bool=..., labels: _Optional[_Mapping[str, str]]=..., website: _Optional[_Union[Bucket.Website, _Mapping]]=..., versioning: _Optional[_Union[Bucket.Versioning, _Mapping]]=..., logging: _Optional[_Union[Bucket.Logging, _Mapping]]=..., owner: _Optional[_Union[Owner, _Mapping]]=..., encryption: _Optional[_Union[Bucket.Encryption, _Mapping]]=..., billing: _Optional[_Union[Bucket.Billing, _Mapping]]=..., retention_policy: _Optional[_Union[Bucket.RetentionPolicy, _Mapping]]=..., location_type: _Optional[str]=..., iam_configuration: _Optional[_Union[Bucket.IamConfiguration, _Mapping]]=..., zone_affinity: _Optional[_Iterable[str]]=..., satisfies_pzs: bool=..., autoclass: _Optional[_Union[Bucket.Autoclass, _Mapping]]=...) -> None:
        ...

class BucketAccessControl(_message.Message):
    __slots__ = ('role', 'etag', 'id', 'bucket', 'entity', 'entity_id', 'email', 'domain', 'project_team')
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TEAM_FIELD_NUMBER: _ClassVar[int]
    role: str
    etag: str
    id: str
    bucket: str
    entity: str
    entity_id: str
    email: str
    domain: str
    project_team: ProjectTeam

    def __init__(self, role: _Optional[str]=..., etag: _Optional[str]=..., id: _Optional[str]=..., bucket: _Optional[str]=..., entity: _Optional[str]=..., entity_id: _Optional[str]=..., email: _Optional[str]=..., domain: _Optional[str]=..., project_team: _Optional[_Union[ProjectTeam, _Mapping]]=...) -> None:
        ...

class ListBucketAccessControlsResponse(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BucketAccessControl]

    def __init__(self, items: _Optional[_Iterable[_Union[BucketAccessControl, _Mapping]]]=...) -> None:
        ...

class ListBucketsResponse(_message.Message):
    __slots__ = ('items', 'next_page_token')
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Bucket]
    next_page_token: str

    def __init__(self, items: _Optional[_Iterable[_Union[Bucket, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Channel(_message.Message):
    __slots__ = ('id', 'resource_id', 'resource_uri', 'token', 'expiration', 'type', 'address', 'params', 'payload')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_id: str
    resource_uri: str
    token: str
    expiration: _timestamp_pb2.Timestamp
    type: str
    address: str
    params: _containers.ScalarMap[str, str]
    payload: bool

    def __init__(self, id: _Optional[str]=..., resource_id: _Optional[str]=..., resource_uri: _Optional[str]=..., token: _Optional[str]=..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[str]=..., address: _Optional[str]=..., params: _Optional[_Mapping[str, str]]=..., payload: bool=...) -> None:
        ...

class ListChannelsResponse(_message.Message):
    __slots__ = ('items',)

    class Items(_message.Message):
        __slots__ = ('channel_id', 'resource_id', 'push_url', 'subscriber_email', 'creation_time')
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        PUSH_URL_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIBER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
        channel_id: str
        resource_id: str
        push_url: str
        subscriber_email: str
        creation_time: _timestamp_pb2.Timestamp

        def __init__(self, channel_id: _Optional[str]=..., resource_id: _Optional[str]=..., push_url: _Optional[str]=..., subscriber_email: _Optional[str]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ListChannelsResponse.Items]

    def __init__(self, items: _Optional[_Iterable[_Union[ListChannelsResponse.Items, _Mapping]]]=...) -> None:
        ...

class ChecksummedData(_message.Message):
    __slots__ = ('content', 'crc32c')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    crc32c: _wrappers_pb2.UInt32Value

    def __init__(self, content: _Optional[bytes]=..., crc32c: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=...) -> None:
        ...

class ObjectChecksums(_message.Message):
    __slots__ = ('crc32c', 'md5_hash')
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    MD5_HASH_FIELD_NUMBER: _ClassVar[int]
    crc32c: _wrappers_pb2.UInt32Value
    md5_hash: str

    def __init__(self, crc32c: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=..., md5_hash: _Optional[str]=...) -> None:
        ...

class CommonEnums(_message.Message):
    __slots__ = ()

    class Projection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROJECTION_UNSPECIFIED: _ClassVar[CommonEnums.Projection]
        NO_ACL: _ClassVar[CommonEnums.Projection]
        FULL: _ClassVar[CommonEnums.Projection]
    PROJECTION_UNSPECIFIED: CommonEnums.Projection
    NO_ACL: CommonEnums.Projection
    FULL: CommonEnums.Projection

    class PredefinedBucketAcl(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREDEFINED_BUCKET_ACL_UNSPECIFIED: _ClassVar[CommonEnums.PredefinedBucketAcl]
        BUCKET_ACL_AUTHENTICATED_READ: _ClassVar[CommonEnums.PredefinedBucketAcl]
        BUCKET_ACL_PRIVATE: _ClassVar[CommonEnums.PredefinedBucketAcl]
        BUCKET_ACL_PROJECT_PRIVATE: _ClassVar[CommonEnums.PredefinedBucketAcl]
        BUCKET_ACL_PUBLIC_READ: _ClassVar[CommonEnums.PredefinedBucketAcl]
        BUCKET_ACL_PUBLIC_READ_WRITE: _ClassVar[CommonEnums.PredefinedBucketAcl]
    PREDEFINED_BUCKET_ACL_UNSPECIFIED: CommonEnums.PredefinedBucketAcl
    BUCKET_ACL_AUTHENTICATED_READ: CommonEnums.PredefinedBucketAcl
    BUCKET_ACL_PRIVATE: CommonEnums.PredefinedBucketAcl
    BUCKET_ACL_PROJECT_PRIVATE: CommonEnums.PredefinedBucketAcl
    BUCKET_ACL_PUBLIC_READ: CommonEnums.PredefinedBucketAcl
    BUCKET_ACL_PUBLIC_READ_WRITE: CommonEnums.PredefinedBucketAcl

    class PredefinedObjectAcl(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREDEFINED_OBJECT_ACL_UNSPECIFIED: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_AUTHENTICATED_READ: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_BUCKET_OWNER_FULL_CONTROL: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_BUCKET_OWNER_READ: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_PRIVATE: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_PROJECT_PRIVATE: _ClassVar[CommonEnums.PredefinedObjectAcl]
        OBJECT_ACL_PUBLIC_READ: _ClassVar[CommonEnums.PredefinedObjectAcl]
    PREDEFINED_OBJECT_ACL_UNSPECIFIED: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_AUTHENTICATED_READ: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_BUCKET_OWNER_FULL_CONTROL: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_BUCKET_OWNER_READ: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_PRIVATE: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_PROJECT_PRIVATE: CommonEnums.PredefinedObjectAcl
    OBJECT_ACL_PUBLIC_READ: CommonEnums.PredefinedObjectAcl

    def __init__(self) -> None:
        ...

class ContentRange(_message.Message):
    __slots__ = ('start', 'end', 'complete_length')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    complete_length: int

    def __init__(self, start: _Optional[int]=..., end: _Optional[int]=..., complete_length: _Optional[int]=...) -> None:
        ...

class HmacKeyMetadata(_message.Message):
    __slots__ = ('id', 'access_id', 'project_id', 'service_account_email', 'state', 'time_created', 'updated', 'etag')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    access_id: str
    project_id: str
    service_account_email: str
    state: str
    time_created: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, id: _Optional[str]=..., access_id: _Optional[str]=..., project_id: _Optional[str]=..., service_account_email: _Optional[str]=..., state: _Optional[str]=..., time_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class Notification(_message.Message):
    __slots__ = ('topic', 'event_types', 'custom_attributes', 'etag', 'object_name_prefix', 'payload_format', 'id')

    class CustomAttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    topic: str
    event_types: _containers.RepeatedScalarFieldContainer[str]
    custom_attributes: _containers.ScalarMap[str, str]
    etag: str
    object_name_prefix: str
    payload_format: str
    id: str

    def __init__(self, topic: _Optional[str]=..., event_types: _Optional[_Iterable[str]]=..., custom_attributes: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., object_name_prefix: _Optional[str]=..., payload_format: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...

class ListNotificationsResponse(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Notification]

    def __init__(self, items: _Optional[_Iterable[_Union[Notification, _Mapping]]]=...) -> None:
        ...

class Object(_message.Message):
    __slots__ = ('content_encoding', 'content_disposition', 'cache_control', 'acl', 'content_language', 'metageneration', 'time_deleted', 'content_type', 'size', 'time_created', 'crc32c', 'component_count', 'md5_hash', 'etag', 'updated', 'storage_class', 'kms_key_name', 'time_storage_class_updated', 'temporary_hold', 'retention_expiration_time', 'metadata', 'event_based_hold', 'name', 'id', 'bucket', 'generation', 'owner', 'customer_encryption', 'custom_time')

    class CustomerEncryption(_message.Message):
        __slots__ = ('encryption_algorithm', 'key_sha256')
        ENCRYPTION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
        KEY_SHA256_FIELD_NUMBER: _ClassVar[int]
        encryption_algorithm: str
        key_sha256: str

        def __init__(self, encryption_algorithm: _Optional[str]=..., key_sha256: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    TIME_DELETED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MD5_HASH_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_STORAGE_CLASS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_HOLD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_BASED_HOLD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TIME_FIELD_NUMBER: _ClassVar[int]
    content_encoding: str
    content_disposition: str
    cache_control: str
    acl: _containers.RepeatedCompositeFieldContainer[ObjectAccessControl]
    content_language: str
    metageneration: int
    time_deleted: _timestamp_pb2.Timestamp
    content_type: str
    size: int
    time_created: _timestamp_pb2.Timestamp
    crc32c: _wrappers_pb2.UInt32Value
    component_count: int
    md5_hash: str
    etag: str
    updated: _timestamp_pb2.Timestamp
    storage_class: str
    kms_key_name: str
    time_storage_class_updated: _timestamp_pb2.Timestamp
    temporary_hold: bool
    retention_expiration_time: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    event_based_hold: _wrappers_pb2.BoolValue
    name: str
    id: str
    bucket: str
    generation: int
    owner: Owner
    customer_encryption: Object.CustomerEncryption
    custom_time: _timestamp_pb2.Timestamp

    def __init__(self, content_encoding: _Optional[str]=..., content_disposition: _Optional[str]=..., cache_control: _Optional[str]=..., acl: _Optional[_Iterable[_Union[ObjectAccessControl, _Mapping]]]=..., content_language: _Optional[str]=..., metageneration: _Optional[int]=..., time_deleted: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., content_type: _Optional[str]=..., size: _Optional[int]=..., time_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., crc32c: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]]=..., component_count: _Optional[int]=..., md5_hash: _Optional[str]=..., etag: _Optional[str]=..., updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., storage_class: _Optional[str]=..., kms_key_name: _Optional[str]=..., time_storage_class_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., temporary_hold: bool=..., retention_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., event_based_hold: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., name: _Optional[str]=..., id: _Optional[str]=..., bucket: _Optional[str]=..., generation: _Optional[int]=..., owner: _Optional[_Union[Owner, _Mapping]]=..., customer_encryption: _Optional[_Union[Object.CustomerEncryption, _Mapping]]=..., custom_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ObjectAccessControl(_message.Message):
    __slots__ = ('role', 'etag', 'id', 'bucket', 'object', 'generation', 'entity', 'entity_id', 'email', 'domain', 'project_team')
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TEAM_FIELD_NUMBER: _ClassVar[int]
    role: str
    etag: str
    id: str
    bucket: str
    object: str
    generation: int
    entity: str
    entity_id: str
    email: str
    domain: str
    project_team: ProjectTeam

    def __init__(self, role: _Optional[str]=..., etag: _Optional[str]=..., id: _Optional[str]=..., bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., entity: _Optional[str]=..., entity_id: _Optional[str]=..., email: _Optional[str]=..., domain: _Optional[str]=..., project_team: _Optional[_Union[ProjectTeam, _Mapping]]=...) -> None:
        ...

class ListObjectAccessControlsResponse(_message.Message):
    __slots__ = ('items',)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ObjectAccessControl]

    def __init__(self, items: _Optional[_Iterable[_Union[ObjectAccessControl, _Mapping]]]=...) -> None:
        ...

class ListObjectsResponse(_message.Message):
    __slots__ = ('prefixes', 'items', 'next_page_token')
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    items: _containers.RepeatedCompositeFieldContainer[Object]
    next_page_token: str

    def __init__(self, prefixes: _Optional[_Iterable[str]]=..., items: _Optional[_Iterable[_Union[Object, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ProjectTeam(_message.Message):
    __slots__ = ('project_number', 'team')
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    project_number: str
    team: str

    def __init__(self, project_number: _Optional[str]=..., team: _Optional[str]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email_address',)
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    email_address: str

    def __init__(self, email_address: _Optional[str]=...) -> None:
        ...

class Owner(_message.Message):
    __slots__ = ('entity', 'entity_id')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity: str
    entity_id: str

    def __init__(self, entity: _Optional[str]=..., entity_id: _Optional[str]=...) -> None:
        ...