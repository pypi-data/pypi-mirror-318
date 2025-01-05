from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.eventarc.v1 import logging_config_pb2 as _logging_config_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Pipeline(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'uid', 'annotations', 'display_name', 'destinations', 'mediations', 'crypto_key_name', 'input_payload_format', 'logging_config', 'retry_policy', 'etag')

    class MessagePayloadFormat(_message.Message):
        __slots__ = ('protobuf', 'avro', 'json')

        class JsonFormat(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class ProtobufFormat(_message.Message):
            __slots__ = ('schema_definition',)
            SCHEMA_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            schema_definition: str

            def __init__(self, schema_definition: _Optional[str]=...) -> None:
                ...

        class AvroFormat(_message.Message):
            __slots__ = ('schema_definition',)
            SCHEMA_DEFINITION_FIELD_NUMBER: _ClassVar[int]
            schema_definition: str

            def __init__(self, schema_definition: _Optional[str]=...) -> None:
                ...
        PROTOBUF_FIELD_NUMBER: _ClassVar[int]
        AVRO_FIELD_NUMBER: _ClassVar[int]
        JSON_FIELD_NUMBER: _ClassVar[int]
        protobuf: Pipeline.MessagePayloadFormat.ProtobufFormat
        avro: Pipeline.MessagePayloadFormat.AvroFormat
        json: Pipeline.MessagePayloadFormat.JsonFormat

        def __init__(self, protobuf: _Optional[_Union[Pipeline.MessagePayloadFormat.ProtobufFormat, _Mapping]]=..., avro: _Optional[_Union[Pipeline.MessagePayloadFormat.AvroFormat, _Mapping]]=..., json: _Optional[_Union[Pipeline.MessagePayloadFormat.JsonFormat, _Mapping]]=...) -> None:
            ...

    class Destination(_message.Message):
        __slots__ = ('network_config', 'http_endpoint', 'workflow', 'message_bus', 'topic', 'authentication_config', 'output_payload_format')

        class NetworkConfig(_message.Message):
            __slots__ = ('network_attachment',)
            NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
            network_attachment: str

            def __init__(self, network_attachment: _Optional[str]=...) -> None:
                ...

        class HttpEndpoint(_message.Message):
            __slots__ = ('uri', 'message_binding_template')
            URI_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_BINDING_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            uri: str
            message_binding_template: str

            def __init__(self, uri: _Optional[str]=..., message_binding_template: _Optional[str]=...) -> None:
                ...

        class AuthenticationConfig(_message.Message):
            __slots__ = ('google_oidc', 'oauth_token')

            class OidcToken(_message.Message):
                __slots__ = ('service_account', 'audience')
                SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
                AUDIENCE_FIELD_NUMBER: _ClassVar[int]
                service_account: str
                audience: str

                def __init__(self, service_account: _Optional[str]=..., audience: _Optional[str]=...) -> None:
                    ...

            class OAuthToken(_message.Message):
                __slots__ = ('service_account', 'scope')
                SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
                SCOPE_FIELD_NUMBER: _ClassVar[int]
                service_account: str
                scope: str

                def __init__(self, service_account: _Optional[str]=..., scope: _Optional[str]=...) -> None:
                    ...
            GOOGLE_OIDC_FIELD_NUMBER: _ClassVar[int]
            OAUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
            google_oidc: Pipeline.Destination.AuthenticationConfig.OidcToken
            oauth_token: Pipeline.Destination.AuthenticationConfig.OAuthToken

            def __init__(self, google_oidc: _Optional[_Union[Pipeline.Destination.AuthenticationConfig.OidcToken, _Mapping]]=..., oauth_token: _Optional[_Union[Pipeline.Destination.AuthenticationConfig.OAuthToken, _Mapping]]=...) -> None:
                ...
        NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
        HTTP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        WORKFLOW_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_BUS_FIELD_NUMBER: _ClassVar[int]
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
        network_config: Pipeline.Destination.NetworkConfig
        http_endpoint: Pipeline.Destination.HttpEndpoint
        workflow: str
        message_bus: str
        topic: str
        authentication_config: Pipeline.Destination.AuthenticationConfig
        output_payload_format: Pipeline.MessagePayloadFormat

        def __init__(self, network_config: _Optional[_Union[Pipeline.Destination.NetworkConfig, _Mapping]]=..., http_endpoint: _Optional[_Union[Pipeline.Destination.HttpEndpoint, _Mapping]]=..., workflow: _Optional[str]=..., message_bus: _Optional[str]=..., topic: _Optional[str]=..., authentication_config: _Optional[_Union[Pipeline.Destination.AuthenticationConfig, _Mapping]]=..., output_payload_format: _Optional[_Union[Pipeline.MessagePayloadFormat, _Mapping]]=...) -> None:
            ...

    class Mediation(_message.Message):
        __slots__ = ('transformation',)

        class Transformation(_message.Message):
            __slots__ = ('transformation_template',)
            TRANSFORMATION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            transformation_template: str

            def __init__(self, transformation_template: _Optional[str]=...) -> None:
                ...
        TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
        transformation: Pipeline.Mediation.Transformation

        def __init__(self, transformation: _Optional[_Union[Pipeline.Mediation.Transformation, _Mapping]]=...) -> None:
            ...

    class RetryPolicy(_message.Message):
        __slots__ = ('max_attempts', 'min_retry_delay', 'max_retry_delay')
        MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        MIN_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
        MAX_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
        max_attempts: int
        min_retry_delay: _duration_pb2.Duration
        max_retry_delay: _duration_pb2.Duration

        def __init__(self, max_attempts: _Optional[int]=..., min_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    MEDIATIONS_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    uid: str
    annotations: _containers.ScalarMap[str, str]
    display_name: str
    destinations: _containers.RepeatedCompositeFieldContainer[Pipeline.Destination]
    mediations: _containers.RepeatedCompositeFieldContainer[Pipeline.Mediation]
    crypto_key_name: str
    input_payload_format: Pipeline.MessagePayloadFormat
    logging_config: _logging_config_pb2.LoggingConfig
    retry_policy: Pipeline.RetryPolicy
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., destinations: _Optional[_Iterable[_Union[Pipeline.Destination, _Mapping]]]=..., mediations: _Optional[_Iterable[_Union[Pipeline.Mediation, _Mapping]]]=..., crypto_key_name: _Optional[str]=..., input_payload_format: _Optional[_Union[Pipeline.MessagePayloadFormat, _Mapping]]=..., logging_config: _Optional[_Union[_logging_config_pb2.LoggingConfig, _Mapping]]=..., retry_policy: _Optional[_Union[Pipeline.RetryPolicy, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...