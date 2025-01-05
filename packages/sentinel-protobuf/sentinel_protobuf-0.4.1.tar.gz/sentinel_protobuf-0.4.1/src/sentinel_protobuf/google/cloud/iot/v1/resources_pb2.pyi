from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MqttState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MQTT_STATE_UNSPECIFIED: _ClassVar[MqttState]
    MQTT_ENABLED: _ClassVar[MqttState]
    MQTT_DISABLED: _ClassVar[MqttState]

class HttpState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_STATE_UNSPECIFIED: _ClassVar[HttpState]
    HTTP_ENABLED: _ClassVar[HttpState]
    HTTP_DISABLED: _ClassVar[HttpState]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LEVEL_UNSPECIFIED: _ClassVar[LogLevel]
    NONE: _ClassVar[LogLevel]
    ERROR: _ClassVar[LogLevel]
    INFO: _ClassVar[LogLevel]
    DEBUG: _ClassVar[LogLevel]

class GatewayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATEWAY_TYPE_UNSPECIFIED: _ClassVar[GatewayType]
    GATEWAY: _ClassVar[GatewayType]
    NON_GATEWAY: _ClassVar[GatewayType]

class GatewayAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATEWAY_AUTH_METHOD_UNSPECIFIED: _ClassVar[GatewayAuthMethod]
    ASSOCIATION_ONLY: _ClassVar[GatewayAuthMethod]
    DEVICE_AUTH_TOKEN_ONLY: _ClassVar[GatewayAuthMethod]
    ASSOCIATION_AND_DEVICE_AUTH_TOKEN: _ClassVar[GatewayAuthMethod]

class PublicKeyCertificateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT: _ClassVar[PublicKeyCertificateFormat]
    X509_CERTIFICATE_PEM: _ClassVar[PublicKeyCertificateFormat]

class PublicKeyFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED_PUBLIC_KEY_FORMAT: _ClassVar[PublicKeyFormat]
    RSA_PEM: _ClassVar[PublicKeyFormat]
    RSA_X509_PEM: _ClassVar[PublicKeyFormat]
    ES256_PEM: _ClassVar[PublicKeyFormat]
    ES256_X509_PEM: _ClassVar[PublicKeyFormat]
MQTT_STATE_UNSPECIFIED: MqttState
MQTT_ENABLED: MqttState
MQTT_DISABLED: MqttState
HTTP_STATE_UNSPECIFIED: HttpState
HTTP_ENABLED: HttpState
HTTP_DISABLED: HttpState
LOG_LEVEL_UNSPECIFIED: LogLevel
NONE: LogLevel
ERROR: LogLevel
INFO: LogLevel
DEBUG: LogLevel
GATEWAY_TYPE_UNSPECIFIED: GatewayType
GATEWAY: GatewayType
NON_GATEWAY: GatewayType
GATEWAY_AUTH_METHOD_UNSPECIFIED: GatewayAuthMethod
ASSOCIATION_ONLY: GatewayAuthMethod
DEVICE_AUTH_TOKEN_ONLY: GatewayAuthMethod
ASSOCIATION_AND_DEVICE_AUTH_TOKEN: GatewayAuthMethod
UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT: PublicKeyCertificateFormat
X509_CERTIFICATE_PEM: PublicKeyCertificateFormat
UNSPECIFIED_PUBLIC_KEY_FORMAT: PublicKeyFormat
RSA_PEM: PublicKeyFormat
RSA_X509_PEM: PublicKeyFormat
ES256_PEM: PublicKeyFormat
ES256_X509_PEM: PublicKeyFormat

class Device(_message.Message):
    __slots__ = ('id', 'name', 'num_id', 'credentials', 'last_heartbeat_time', 'last_event_time', 'last_state_time', 'last_config_ack_time', 'last_config_send_time', 'blocked', 'last_error_time', 'last_error_status', 'config', 'state', 'log_level', 'metadata', 'gateway_config')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_CONFIG_ACK_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_CONFIG_SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    num_id: int
    credentials: _containers.RepeatedCompositeFieldContainer[DeviceCredential]
    last_heartbeat_time: _timestamp_pb2.Timestamp
    last_event_time: _timestamp_pb2.Timestamp
    last_state_time: _timestamp_pb2.Timestamp
    last_config_ack_time: _timestamp_pb2.Timestamp
    last_config_send_time: _timestamp_pb2.Timestamp
    blocked: bool
    last_error_time: _timestamp_pb2.Timestamp
    last_error_status: _status_pb2.Status
    config: DeviceConfig
    state: DeviceState
    log_level: LogLevel
    metadata: _containers.ScalarMap[str, str]
    gateway_config: GatewayConfig

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., num_id: _Optional[int]=..., credentials: _Optional[_Iterable[_Union[DeviceCredential, _Mapping]]]=..., last_heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_state_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_config_ack_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_config_send_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., blocked: bool=..., last_error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_error_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., config: _Optional[_Union[DeviceConfig, _Mapping]]=..., state: _Optional[_Union[DeviceState, _Mapping]]=..., log_level: _Optional[_Union[LogLevel, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., gateway_config: _Optional[_Union[GatewayConfig, _Mapping]]=...) -> None:
        ...

class GatewayConfig(_message.Message):
    __slots__ = ('gateway_type', 'gateway_auth_method', 'last_accessed_gateway_id', 'last_accessed_gateway_time')
    GATEWAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_GATEWAY_TIME_FIELD_NUMBER: _ClassVar[int]
    gateway_type: GatewayType
    gateway_auth_method: GatewayAuthMethod
    last_accessed_gateway_id: str
    last_accessed_gateway_time: _timestamp_pb2.Timestamp

    def __init__(self, gateway_type: _Optional[_Union[GatewayType, str]]=..., gateway_auth_method: _Optional[_Union[GatewayAuthMethod, str]]=..., last_accessed_gateway_id: _Optional[str]=..., last_accessed_gateway_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeviceRegistry(_message.Message):
    __slots__ = ('id', 'name', 'event_notification_configs', 'state_notification_config', 'mqtt_config', 'http_config', 'log_level', 'credentials')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NOTIFICATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    STATE_NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MQTT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HTTP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    event_notification_configs: _containers.RepeatedCompositeFieldContainer[EventNotificationConfig]
    state_notification_config: StateNotificationConfig
    mqtt_config: MqttConfig
    http_config: HttpConfig
    log_level: LogLevel
    credentials: _containers.RepeatedCompositeFieldContainer[RegistryCredential]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., event_notification_configs: _Optional[_Iterable[_Union[EventNotificationConfig, _Mapping]]]=..., state_notification_config: _Optional[_Union[StateNotificationConfig, _Mapping]]=..., mqtt_config: _Optional[_Union[MqttConfig, _Mapping]]=..., http_config: _Optional[_Union[HttpConfig, _Mapping]]=..., log_level: _Optional[_Union[LogLevel, str]]=..., credentials: _Optional[_Iterable[_Union[RegistryCredential, _Mapping]]]=...) -> None:
        ...

class MqttConfig(_message.Message):
    __slots__ = ('mqtt_enabled_state',)
    MQTT_ENABLED_STATE_FIELD_NUMBER: _ClassVar[int]
    mqtt_enabled_state: MqttState

    def __init__(self, mqtt_enabled_state: _Optional[_Union[MqttState, str]]=...) -> None:
        ...

class HttpConfig(_message.Message):
    __slots__ = ('http_enabled_state',)
    HTTP_ENABLED_STATE_FIELD_NUMBER: _ClassVar[int]
    http_enabled_state: HttpState

    def __init__(self, http_enabled_state: _Optional[_Union[HttpState, str]]=...) -> None:
        ...

class EventNotificationConfig(_message.Message):
    __slots__ = ('subfolder_matches', 'pubsub_topic_name')
    SUBFOLDER_MATCHES_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    subfolder_matches: str
    pubsub_topic_name: str

    def __init__(self, subfolder_matches: _Optional[str]=..., pubsub_topic_name: _Optional[str]=...) -> None:
        ...

class StateNotificationConfig(_message.Message):
    __slots__ = ('pubsub_topic_name',)
    PUBSUB_TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic_name: str

    def __init__(self, pubsub_topic_name: _Optional[str]=...) -> None:
        ...

class RegistryCredential(_message.Message):
    __slots__ = ('public_key_certificate',)
    PUBLIC_KEY_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    public_key_certificate: PublicKeyCertificate

    def __init__(self, public_key_certificate: _Optional[_Union[PublicKeyCertificate, _Mapping]]=...) -> None:
        ...

class X509CertificateDetails(_message.Message):
    __slots__ = ('issuer', 'subject', 'start_time', 'expiry_time', 'signature_algorithm', 'public_key_type')
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    issuer: str
    subject: str
    start_time: _timestamp_pb2.Timestamp
    expiry_time: _timestamp_pb2.Timestamp
    signature_algorithm: str
    public_key_type: str

    def __init__(self, issuer: _Optional[str]=..., subject: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expiry_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., signature_algorithm: _Optional[str]=..., public_key_type: _Optional[str]=...) -> None:
        ...

class PublicKeyCertificate(_message.Message):
    __slots__ = ('format', 'certificate', 'x509_details')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    X509_DETAILS_FIELD_NUMBER: _ClassVar[int]
    format: PublicKeyCertificateFormat
    certificate: str
    x509_details: X509CertificateDetails

    def __init__(self, format: _Optional[_Union[PublicKeyCertificateFormat, str]]=..., certificate: _Optional[str]=..., x509_details: _Optional[_Union[X509CertificateDetails, _Mapping]]=...) -> None:
        ...

class DeviceCredential(_message.Message):
    __slots__ = ('public_key', 'expiration_time')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    public_key: PublicKeyCredential
    expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, public_key: _Optional[_Union[PublicKeyCredential, _Mapping]]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PublicKeyCredential(_message.Message):
    __slots__ = ('format', 'key')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    format: PublicKeyFormat
    key: str

    def __init__(self, format: _Optional[_Union[PublicKeyFormat, str]]=..., key: _Optional[str]=...) -> None:
        ...

class DeviceConfig(_message.Message):
    __slots__ = ('version', 'cloud_update_time', 'device_ack_time', 'binary_data')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ACK_TIME_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    version: int
    cloud_update_time: _timestamp_pb2.Timestamp
    device_ack_time: _timestamp_pb2.Timestamp
    binary_data: bytes

    def __init__(self, version: _Optional[int]=..., cloud_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., device_ack_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., binary_data: _Optional[bytes]=...) -> None:
        ...

class DeviceState(_message.Message):
    __slots__ = ('update_time', 'binary_data')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BINARY_DATA_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    binary_data: bytes

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., binary_data: _Optional[bytes]=...) -> None:
        ...