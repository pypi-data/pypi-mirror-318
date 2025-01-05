from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Application(_message.Message):
    __slots__ = ('name', 'id', 'dispatch_rules', 'auth_domain', 'location_id', 'code_bucket', 'default_cookie_expiration', 'serving_status', 'default_hostname', 'default_bucket', 'service_account', 'iap', 'gcr_domain', 'database_type', 'feature_settings')

    class ServingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Application.ServingStatus]
        SERVING: _ClassVar[Application.ServingStatus]
        USER_DISABLED: _ClassVar[Application.ServingStatus]
        SYSTEM_DISABLED: _ClassVar[Application.ServingStatus]
    UNSPECIFIED: Application.ServingStatus
    SERVING: Application.ServingStatus
    USER_DISABLED: Application.ServingStatus
    SYSTEM_DISABLED: Application.ServingStatus

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[Application.DatabaseType]
        CLOUD_DATASTORE: _ClassVar[Application.DatabaseType]
        CLOUD_FIRESTORE: _ClassVar[Application.DatabaseType]
        CLOUD_DATASTORE_COMPATIBILITY: _ClassVar[Application.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: Application.DatabaseType
    CLOUD_DATASTORE: Application.DatabaseType
    CLOUD_FIRESTORE: Application.DatabaseType
    CLOUD_DATASTORE_COMPATIBILITY: Application.DatabaseType

    class IdentityAwareProxy(_message.Message):
        __slots__ = ('enabled', 'oauth2_client_id', 'oauth2_client_secret', 'oauth2_client_secret_sha256')
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        OAUTH2_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        OAUTH2_CLIENT_SECRET_SHA256_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        oauth2_client_id: str
        oauth2_client_secret: str
        oauth2_client_secret_sha256: str

        def __init__(self, enabled: bool=..., oauth2_client_id: _Optional[str]=..., oauth2_client_secret: _Optional[str]=..., oauth2_client_secret_sha256: _Optional[str]=...) -> None:
            ...

    class FeatureSettings(_message.Message):
        __slots__ = ('split_health_checks', 'use_container_optimized_os')
        SPLIT_HEALTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
        USE_CONTAINER_OPTIMIZED_OS_FIELD_NUMBER: _ClassVar[int]
        split_health_checks: bool
        use_container_optimized_os: bool

        def __init__(self, split_health_checks: bool=..., use_container_optimized_os: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_RULES_FIELD_NUMBER: _ClassVar[int]
    AUTH_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COOKIE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    SERVING_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IAP_FIELD_NUMBER: _ClassVar[int]
    GCR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DATABASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    dispatch_rules: _containers.RepeatedCompositeFieldContainer[UrlDispatchRule]
    auth_domain: str
    location_id: str
    code_bucket: str
    default_cookie_expiration: _duration_pb2.Duration
    serving_status: Application.ServingStatus
    default_hostname: str
    default_bucket: str
    service_account: str
    iap: Application.IdentityAwareProxy
    gcr_domain: str
    database_type: Application.DatabaseType
    feature_settings: Application.FeatureSettings

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., dispatch_rules: _Optional[_Iterable[_Union[UrlDispatchRule, _Mapping]]]=..., auth_domain: _Optional[str]=..., location_id: _Optional[str]=..., code_bucket: _Optional[str]=..., default_cookie_expiration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., serving_status: _Optional[_Union[Application.ServingStatus, str]]=..., default_hostname: _Optional[str]=..., default_bucket: _Optional[str]=..., service_account: _Optional[str]=..., iap: _Optional[_Union[Application.IdentityAwareProxy, _Mapping]]=..., gcr_domain: _Optional[str]=..., database_type: _Optional[_Union[Application.DatabaseType, str]]=..., feature_settings: _Optional[_Union[Application.FeatureSettings, _Mapping]]=...) -> None:
        ...

class UrlDispatchRule(_message.Message):
    __slots__ = ('domain', 'path', 'service')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    domain: str
    path: str
    service: str

    def __init__(self, domain: _Optional[str]=..., path: _Optional[str]=..., service: _Optional[str]=...) -> None:
        ...