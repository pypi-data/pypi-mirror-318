"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/pipeline.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.eventarc.v1 import logging_config_pb2 as google_dot_cloud_dot_eventarc_dot_v1_dot_logging__config__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/eventarc/v1/pipeline.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/eventarc/v1/logging_config.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe1\x17\n\x08Pipeline\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x06labels\x18\x04 \x03(\x0b2..google.cloud.eventarc.v1.Pipeline.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x03uid\x18\x05 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12M\n\x0bannotations\x18\x06 \x03(\x0b23.google.cloud.eventarc.v1.Pipeline.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x07 \x01(\tB\x03\xe0A\x01\x12I\n\x0cdestinations\x18\x08 \x03(\x0b2..google.cloud.eventarc.v1.Pipeline.DestinationB\x03\xe0A\x02\x12E\n\nmediations\x18\t \x03(\x0b2,.google.cloud.eventarc.v1.Pipeline.MediationB\x03\xe0A\x01\x12B\n\x0fcrypto_key_name\x18\n \x01(\tB)\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12Z\n\x14input_payload_format\x18\x0b \x01(\x0b27.google.cloud.eventarc.v1.Pipeline.MessagePayloadFormatB\x03\xe0A\x01\x12D\n\x0elogging_config\x18\x0c \x01(\x0b2\'.google.cloud.eventarc.v1.LoggingConfigB\x03\xe0A\x01\x12I\n\x0cretry_policy\x18\r \x01(\x0b2..google.cloud.eventarc.v1.Pipeline.RetryPolicyB\x03\xe0A\x01\x12\x0c\n\x04etag\x18c \x01(\t\x1a\x9f\x03\n\x14MessagePayloadFormat\x12_\n\x08protobuf\x18\x01 \x01(\x0b2F.google.cloud.eventarc.v1.Pipeline.MessagePayloadFormat.ProtobufFormatB\x03\xe0A\x01H\x00\x12W\n\x04avro\x18\x02 \x01(\x0b2B.google.cloud.eventarc.v1.Pipeline.MessagePayloadFormat.AvroFormatB\x03\xe0A\x01H\x00\x12W\n\x04json\x18\x03 \x01(\x0b2B.google.cloud.eventarc.v1.Pipeline.MessagePayloadFormat.JsonFormatB\x03\xe0A\x01H\x00\x1a\x0c\n\nJsonFormat\x1a0\n\x0eProtobufFormat\x12\x1e\n\x11schema_definition\x18\x01 \x01(\tB\x03\xe0A\x01\x1a,\n\nAvroFormat\x12\x1e\n\x11schema_definition\x18\x01 \x01(\tB\x03\xe0A\x01B\x06\n\x04kind\x1a\xe5\t\n\x0bDestination\x12Y\n\x0enetwork_config\x18\x01 \x01(\x0b2<.google.cloud.eventarc.v1.Pipeline.Destination.NetworkConfigB\x03\xe0A\x01\x12Y\n\rhttp_endpoint\x18\x02 \x01(\x0b2;.google.cloud.eventarc.v1.Pipeline.Destination.HttpEndpointB\x03\xe0A\x01H\x00\x12=\n\x08workflow\x18\x03 \x01(\tB)\xe0A\x01\xfaA#\n!workflows.googleapis.com/WorkflowH\x00\x12A\n\x0bmessage_bus\x18\x04 \x01(\tB*\xe0A\x01\xfaA$\n"eventarc.googleapis.com/MessageBusH\x00\x124\n\x05topic\x18\x08 \x01(\tB#\xe0A\x01\xfaA\x1d\n\x1bpubsub.googleapis.com/TopicH\x00\x12g\n\x15authentication_config\x18\x05 \x01(\x0b2C.google.cloud.eventarc.v1.Pipeline.Destination.AuthenticationConfigB\x03\xe0A\x01\x12[\n\x15output_payload_format\x18\x06 \x01(\x0b27.google.cloud.eventarc.v1.Pipeline.MessagePayloadFormatB\x03\xe0A\x01\x1a]\n\rNetworkConfig\x12L\n\x12network_attachment\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(compute.googleapis.com/NetworkAttachment\x1aG\n\x0cHttpEndpoint\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12%\n\x18message_binding_template\x18\x03 \x01(\tB\x03\xe0A\x01\x1a\xdf\x03\n\x14AuthenticationConfig\x12i\n\x0bgoogle_oidc\x18\x01 \x01(\x0b2M.google.cloud.eventarc.v1.Pipeline.Destination.AuthenticationConfig.OidcTokenB\x03\xe0A\x01H\x00\x12j\n\x0boauth_token\x18\x02 \x01(\x0b2N.google.cloud.eventarc.v1.Pipeline.Destination.AuthenticationConfig.OAuthTokenB\x03\xe0A\x01H\x00\x1af\n\tOidcToken\x12B\n\x0fservice_account\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x15\n\x08audience\x18\x02 \x01(\tB\x03\xe0A\x01\x1ad\n\nOAuthToken\x12B\n\x0fservice_account\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount\x12\x12\n\x05scope\x18\x02 \x01(\tB\x03\xe0A\x01B"\n authentication_method_descriptorB\x18\n\x16destination_descriptor\x1a\xb7\x01\n\tMediation\x12Z\n\x0etransformation\x18\x01 \x01(\x0b2;.google.cloud.eventarc.v1.Pipeline.Mediation.TransformationB\x03\xe0A\x01H\x00\x1a6\n\x0eTransformation\x12$\n\x17transformation_template\x18\x01 \x01(\tB\x03\xe0A\x01B\x16\n\x14mediation_descriptor\x1a\x9a\x01\n\x0bRetryPolicy\x12\x19\n\x0cmax_attempts\x18\x01 \x01(\x05B\x03\xe0A\x01\x127\n\x0fmin_retry_delay\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x127\n\x0fmax_retry_delay\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:x\xeaAu\n eventarc.googleapis.com/Pipeline\x12<projects/{project}/locations/{location}/pipelines/{pipeline}*\tpipelines2\x08pipelineB\x80\x02\n\x1ccom.google.cloud.eventarc.v1B\rPipelineProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.pipeline_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\rPipelineProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_PROTOBUFFORMAT'].fields_by_name['schema_definition']._loaded_options = None
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_PROTOBUFFORMAT'].fields_by_name['schema_definition']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_AVROFORMAT'].fields_by_name['schema_definition']._loaded_options = None
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_AVROFORMAT'].fields_by_name['schema_definition']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['protobuf']._loaded_options = None
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['protobuf']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['avro']._loaded_options = None
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['avro']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['json']._loaded_options = None
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT'].fields_by_name['json']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION_NETWORKCONFIG'].fields_by_name['network_attachment']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_NETWORKCONFIG'].fields_by_name['network_attachment']._serialized_options = b'\xe0A\x02\xfaA*\n(compute.googleapis.com/NetworkAttachment'
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT'].fields_by_name['uri']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT'].fields_by_name['message_binding_template']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT'].fields_by_name['message_binding_template']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN'].fields_by_name['service_account']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN'].fields_by_name['service_account']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN'].fields_by_name['audience']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN'].fields_by_name['audience']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN'].fields_by_name['service_account']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN'].fields_by_name['service_account']._serialized_options = b'\xe0A\x02\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN'].fields_by_name['scope']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG'].fields_by_name['google_oidc']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG'].fields_by_name['google_oidc']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG'].fields_by_name['oauth_token']._loaded_options = None
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG'].fields_by_name['oauth_token']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['network_config']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['network_config']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['http_endpoint']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['http_endpoint']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['workflow']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['workflow']._serialized_options = b'\xe0A\x01\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['message_bus']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['message_bus']._serialized_options = b'\xe0A\x01\xfaA$\n"eventarc.googleapis.com/MessageBus'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['topic']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['topic']._serialized_options = b'\xe0A\x01\xfaA\x1d\n\x1bpubsub.googleapis.com/Topic'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['authentication_config']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['authentication_config']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_DESTINATION'].fields_by_name['output_payload_format']._loaded_options = None
    _globals['_PIPELINE_DESTINATION'].fields_by_name['output_payload_format']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MEDIATION_TRANSFORMATION'].fields_by_name['transformation_template']._loaded_options = None
    _globals['_PIPELINE_MEDIATION_TRANSFORMATION'].fields_by_name['transformation_template']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_MEDIATION'].fields_by_name['transformation']._loaded_options = None
    _globals['_PIPELINE_MEDIATION'].fields_by_name['transformation']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['max_attempts']._loaded_options = None
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['max_attempts']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['min_retry_delay']._loaded_options = None
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['min_retry_delay']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['max_retry_delay']._loaded_options = None
    _globals['_PIPELINE_RETRYPOLICY'].fields_by_name['max_retry_delay']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE_LABELSENTRY']._loaded_options = None
    _globals['_PIPELINE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_PIPELINE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINE'].fields_by_name['name']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PIPELINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PIPELINE'].fields_by_name['labels']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['uid']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_PIPELINE'].fields_by_name['annotations']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['destinations']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_PIPELINE'].fields_by_name['mediations']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['mediations']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['crypto_key_name']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['crypto_key_name']._serialized_options = b'\xe0A\x01\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_PIPELINE'].fields_by_name['input_payload_format']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['input_payload_format']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['logging_config']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE'].fields_by_name['retry_policy']._loaded_options = None
    _globals['_PIPELINE'].fields_by_name['retry_policy']._serialized_options = b'\xe0A\x01'
    _globals['_PIPELINE']._loaded_options = None
    _globals['_PIPELINE']._serialized_options = b'\xeaAu\n eventarc.googleapis.com/Pipeline\x12<projects/{project}/locations/{location}/pipelines/{pipeline}*\tpipelines2\x08pipeline'
    _globals['_PIPELINE']._serialized_start = 271
    _globals['_PIPELINE']._serialized_end = 3312
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT']._serialized_start = 1077
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT']._serialized_end = 1492
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_JSONFORMAT']._serialized_start = 1376
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_JSONFORMAT']._serialized_end = 1388
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_PROTOBUFFORMAT']._serialized_start = 1390
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_PROTOBUFFORMAT']._serialized_end = 1438
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_AVROFORMAT']._serialized_start = 1440
    _globals['_PIPELINE_MESSAGEPAYLOADFORMAT_AVROFORMAT']._serialized_end = 1484
    _globals['_PIPELINE_DESTINATION']._serialized_start = 1495
    _globals['_PIPELINE_DESTINATION']._serialized_end = 2748
    _globals['_PIPELINE_DESTINATION_NETWORKCONFIG']._serialized_start = 2074
    _globals['_PIPELINE_DESTINATION_NETWORKCONFIG']._serialized_end = 2167
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT']._serialized_start = 2169
    _globals['_PIPELINE_DESTINATION_HTTPENDPOINT']._serialized_end = 2240
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG']._serialized_start = 2243
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG']._serialized_end = 2722
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN']._serialized_start = 2482
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OIDCTOKEN']._serialized_end = 2584
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN']._serialized_start = 2586
    _globals['_PIPELINE_DESTINATION_AUTHENTICATIONCONFIG_OAUTHTOKEN']._serialized_end = 2686
    _globals['_PIPELINE_MEDIATION']._serialized_start = 2751
    _globals['_PIPELINE_MEDIATION']._serialized_end = 2934
    _globals['_PIPELINE_MEDIATION_TRANSFORMATION']._serialized_start = 2856
    _globals['_PIPELINE_MEDIATION_TRANSFORMATION']._serialized_end = 2910
    _globals['_PIPELINE_RETRYPOLICY']._serialized_start = 2937
    _globals['_PIPELINE_RETRYPOLICY']._serialized_end = 3091
    _globals['_PIPELINE_LABELSENTRY']._serialized_start = 3093
    _globals['_PIPELINE_LABELSENTRY']._serialized_end = 3138
    _globals['_PIPELINE_ANNOTATIONSENTRY']._serialized_start = 3140
    _globals['_PIPELINE_ANNOTATIONSENTRY']._serialized_end = 3190