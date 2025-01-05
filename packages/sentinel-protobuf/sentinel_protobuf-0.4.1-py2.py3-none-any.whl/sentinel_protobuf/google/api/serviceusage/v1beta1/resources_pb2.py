"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/serviceusage/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import auth_pb2 as google_dot_api_dot_auth__pb2
from .....google.api import documentation_pb2 as google_dot_api_dot_documentation__pb2
from .....google.api import endpoint_pb2 as google_dot_api_dot_endpoint__pb2
from .....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from .....google.api import monitoring_pb2 as google_dot_api_dot_monitoring__pb2
from .....google.api import quota_pb2 as google_dot_api_dot_quota__pb2
from .....google.api import usage_pb2 as google_dot_api_dot_usage__pb2
from google.protobuf import api_pb2 as google_dot_protobuf_dot_api__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/api/serviceusage/v1beta1/resources.proto\x12\x1fgoogle.api.serviceusage.v1beta1\x1a\x15google/api/auth.proto\x1a\x1egoogle/api/documentation.proto\x1a\x19google/api/endpoint.proto\x1a#google/api/monitored_resource.proto\x1a\x1bgoogle/api/monitoring.proto\x1a\x16google/api/quota.proto\x1a\x16google/api/usage.proto\x1a\x19google/protobuf/api.proto"\x9e\x01\n\x07Service\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12>\n\x06config\x18\x02 \x01(\x0b2..google.api.serviceusage.v1beta1.ServiceConfig\x125\n\x05state\x18\x04 \x01(\x0e2&.google.api.serviceusage.v1beta1.State"\x95\x03\n\rServiceConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12"\n\x04apis\x18\x03 \x03(\x0b2\x14.google.protobuf.Api\x120\n\rdocumentation\x18\x06 \x01(\x0b2\x19.google.api.Documentation\x12 \n\x05quota\x18\n \x01(\x0b2\x11.google.api.Quota\x122\n\x0eauthentication\x18\x0b \x01(\x0b2\x1a.google.api.Authentication\x12 \n\x05usage\x18\x0f \x01(\x0b2\x11.google.api.Usage\x12\'\n\tendpoints\x18\x12 \x03(\x0b2\x14.google.api.Endpoint\x12D\n\x13monitored_resources\x18\x19 \x03(\x0b2\'.google.api.MonitoredResourceDescriptor\x12*\n\nmonitoring\x18\x1c \x01(\x0b2\x16.google.api.Monitoring"+\n\x11OperationMetadata\x12\x16\n\x0eresource_names\x18\x02 \x03(\t"\x8a\x02\n\x13ConsumerQuotaMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x04 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12R\n\x15consumer_quota_limits\x18\x03 \x03(\x0b23.google.api.serviceusage.v1beta1.ConsumerQuotaLimit\x12]\n descendant_consumer_quota_limits\x18\x06 \x03(\x0b23.google.api.serviceusage.v1beta1.ConsumerQuotaLimit\x12\x0c\n\x04unit\x18\x05 \x01(\t"\xd6\x01\n\x12ConsumerQuotaLimit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x08 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x12\n\nis_precise\x18\x03 \x01(\x08\x12\x1e\n\x16allows_admin_overrides\x18\x07 \x01(\x08\x12C\n\rquota_buckets\x18\t \x03(\x0b2,.google.api.serviceusage.v1beta1.QuotaBucket\x12\x1b\n\x13supported_locations\x18\x0b \x03(\t"\xf5\x03\n\x0bQuotaBucket\x12\x17\n\x0feffective_limit\x18\x01 \x01(\x03\x12\x15\n\rdefault_limit\x18\x02 \x01(\x03\x12I\n\x11producer_override\x18\x03 \x01(\x0b2..google.api.serviceusage.v1beta1.QuotaOverride\x12I\n\x11consumer_override\x18\x04 \x01(\x0b2..google.api.serviceusage.v1beta1.QuotaOverride\x12F\n\x0eadmin_override\x18\x05 \x01(\x0b2..google.api.serviceusage.v1beta1.QuotaOverride\x12S\n\x15producer_quota_policy\x18\x07 \x01(\x0b24.google.api.serviceusage.v1beta1.ProducerQuotaPolicy\x12P\n\ndimensions\x18\x06 \x03(\x0b2<.google.api.serviceusage.v1beta1.QuotaBucket.DimensionsEntry\x1a1\n\x0fDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xfb\x01\n\rQuotaOverride\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eoverride_value\x18\x02 \x01(\x03\x12R\n\ndimensions\x18\x03 \x03(\x0b2>.google.api.serviceusage.v1beta1.QuotaOverride.DimensionsEntry\x12\x0e\n\x06metric\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x1f\n\x17admin_override_ancestor\x18\x06 \x01(\t\x1a1\n\x0fDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"Y\n\x14OverrideInlineSource\x12A\n\toverrides\x18\x01 \x03(\x0b2..google.api.serviceusage.v1beta1.QuotaOverride"\xf7\x01\n\x13ProducerQuotaPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpolicy_value\x18\x02 \x01(\x03\x12X\n\ndimensions\x18\x03 \x03(\x0b2D.google.api.serviceusage.v1beta1.ProducerQuotaPolicy.DimensionsEntry\x12\x0e\n\x06metric\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x11\n\tcontainer\x18\x06 \x01(\t\x1a1\n\x0fDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xf1\x01\n\x10AdminQuotaPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpolicy_value\x18\x02 \x01(\x03\x12U\n\ndimensions\x18\x03 \x03(\x0b2A.google.api.serviceusage.v1beta1.AdminQuotaPolicy.DimensionsEntry\x12\x0e\n\x06metric\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x11\n\tcontainer\x18\x06 \x01(\t\x1a1\n\x0fDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"3\n\x0fServiceIdentity\x12\r\n\x05email\x18\x01 \x01(\t\x12\x11\n\tunique_id\x18\x02 \x01(\t*9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x0b\n\x07ENABLED\x10\x02*<\n\tQuotaView\x12\x1a\n\x16QUOTA_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02*~\n\x10QuotaSafetyCheck\x12"\n\x1eQUOTA_SAFETY_CHECK_UNSPECIFIED\x10\x00\x12\x1e\n\x1aLIMIT_DECREASE_BELOW_USAGE\x10\x01\x12&\n"LIMIT_DECREASE_PERCENTAGE_TOO_HIGH\x10\x02B\xed\x01\n#com.google.api.serviceusage.v1beta1B\x0eResourcesProtoP\x01ZKgoogle.golang.org/genproto/googleapis/api/serviceusage/v1beta1;serviceusage\xaa\x02\x1fGoogle.Api.ServiceUsage.V1Beta1\xca\x02\x1fGoogle\\Api\\ServiceUsage\\V1beta1\xea\x02"Google::Api::ServiceUsage::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.serviceusage.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.api.serviceusage.v1beta1B\x0eResourcesProtoP\x01ZKgoogle.golang.org/genproto/googleapis/api/serviceusage/v1beta1;serviceusage\xaa\x02\x1fGoogle.Api.ServiceUsage.V1Beta1\xca\x02\x1fGoogle\\Api\\ServiceUsage\\V1beta1\xea\x02"Google::Api::ServiceUsage::V1beta1'
    _globals['_QUOTABUCKET_DIMENSIONSENTRY']._loaded_options = None
    _globals['_QUOTABUCKET_DIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTAOVERRIDE_DIMENSIONSENTRY']._loaded_options = None
    _globals['_QUOTAOVERRIDE_DIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PRODUCERQUOTAPOLICY_DIMENSIONSENTRY']._loaded_options = None
    _globals['_PRODUCERQUOTAPOLICY_DIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ADMINQUOTAPOLICY_DIMENSIONSENTRY']._loaded_options = None
    _globals['_ADMINQUOTAPOLICY_DIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_STATE']._serialized_start = 2803
    _globals['_STATE']._serialized_end = 2860
    _globals['_QUOTAVIEW']._serialized_start = 2862
    _globals['_QUOTAVIEW']._serialized_end = 2922
    _globals['_QUOTASAFETYCHECK']._serialized_start = 2924
    _globals['_QUOTASAFETYCHECK']._serialized_end = 3050
    _globals['_SERVICE']._serialized_start = 308
    _globals['_SERVICE']._serialized_end = 466
    _globals['_SERVICECONFIG']._serialized_start = 469
    _globals['_SERVICECONFIG']._serialized_end = 874
    _globals['_OPERATIONMETADATA']._serialized_start = 876
    _globals['_OPERATIONMETADATA']._serialized_end = 919
    _globals['_CONSUMERQUOTAMETRIC']._serialized_start = 922
    _globals['_CONSUMERQUOTAMETRIC']._serialized_end = 1188
    _globals['_CONSUMERQUOTALIMIT']._serialized_start = 1191
    _globals['_CONSUMERQUOTALIMIT']._serialized_end = 1405
    _globals['_QUOTABUCKET']._serialized_start = 1408
    _globals['_QUOTABUCKET']._serialized_end = 1909
    _globals['_QUOTABUCKET_DIMENSIONSENTRY']._serialized_start = 1860
    _globals['_QUOTABUCKET_DIMENSIONSENTRY']._serialized_end = 1909
    _globals['_QUOTAOVERRIDE']._serialized_start = 1912
    _globals['_QUOTAOVERRIDE']._serialized_end = 2163
    _globals['_QUOTAOVERRIDE_DIMENSIONSENTRY']._serialized_start = 1860
    _globals['_QUOTAOVERRIDE_DIMENSIONSENTRY']._serialized_end = 1909
    _globals['_OVERRIDEINLINESOURCE']._serialized_start = 2165
    _globals['_OVERRIDEINLINESOURCE']._serialized_end = 2254
    _globals['_PRODUCERQUOTAPOLICY']._serialized_start = 2257
    _globals['_PRODUCERQUOTAPOLICY']._serialized_end = 2504
    _globals['_PRODUCERQUOTAPOLICY_DIMENSIONSENTRY']._serialized_start = 1860
    _globals['_PRODUCERQUOTAPOLICY_DIMENSIONSENTRY']._serialized_end = 1909
    _globals['_ADMINQUOTAPOLICY']._serialized_start = 2507
    _globals['_ADMINQUOTAPOLICY']._serialized_end = 2748
    _globals['_ADMINQUOTAPOLICY_DIMENSIONSENTRY']._serialized_start = 1860
    _globals['_ADMINQUOTAPOLICY_DIMENSIONSENTRY']._serialized_end = 1909
    _globals['_SERVICEIDENTITY']._serialized_start = 2750
    _globals['_SERVICEIDENTITY']._serialized_end = 2801