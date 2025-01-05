"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/security_health_analytics_custom_config.proto')
_sym_db = _symbol_database.Default()
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/cloud/securitycenter/v1/security_health_analytics_custom_config.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x16google/type/expr.proto"\x91\x05\n\x0cCustomConfig\x12$\n\tpredicate\x18\x01 \x01(\x0b2\x11.google.type.Expr\x12T\n\rcustom_output\x18\x02 \x01(\x0b2=.google.cloud.securitycenter.v1.CustomConfig.CustomOutputSpec\x12X\n\x11resource_selector\x18\x03 \x01(\x0b2=.google.cloud.securitycenter.v1.CustomConfig.ResourceSelector\x12G\n\x08severity\x18\x04 \x01(\x0e25.google.cloud.securitycenter.v1.CustomConfig.Severity\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x16\n\x0erecommendation\x18\x06 \x01(\t\x1a\xb5\x01\n\x10CustomOutputSpec\x12Z\n\nproperties\x18\x01 \x03(\x0b2F.google.cloud.securitycenter.v1.CustomConfig.CustomOutputSpec.Property\x1aE\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x10value_expression\x18\x02 \x01(\x0b2\x11.google.type.Expr\x1a*\n\x10ResourceSelector\x12\x16\n\x0eresource_types\x18\x01 \x03(\t"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04B\x82\x02\n"com.google.cloud.securitycenter.v1B(SecurityHealthAnalyticsCustomConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.security_health_analytics_custom_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B(SecurityHealthAnalyticsCustomConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_CUSTOMCONFIG']._serialized_start = 137
    _globals['_CUSTOMCONFIG']._serialized_end = 794
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC']._serialized_start = 486
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC']._serialized_end = 667
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY']._serialized_start = 598
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY']._serialized_end = 667
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR']._serialized_start = 669
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR']._serialized_end = 711
    _globals['_CUSTOMCONFIG_SEVERITY']._serialized_start = 713
    _globals['_CUSTOMCONFIG_SEVERITY']._serialized_end = 794