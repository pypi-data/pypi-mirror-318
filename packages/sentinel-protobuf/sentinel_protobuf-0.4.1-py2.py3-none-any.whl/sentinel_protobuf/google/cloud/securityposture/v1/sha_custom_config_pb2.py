"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securityposture/v1/sha_custom_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/securityposture/v1/sha_custom_config.proto\x12\x1fgoogle.cloud.securityposture.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x16google/type/expr.proto"\xc7\x05\n\x0cCustomConfig\x12)\n\tpredicate\x18\x01 \x01(\x0b2\x11.google.type.ExprB\x03\xe0A\x02\x12Z\n\rcustom_output\x18\x02 \x01(\x0b2>.google.cloud.securityposture.v1.CustomConfig.CustomOutputSpecB\x03\xe0A\x01\x12^\n\x11resource_selector\x18\x03 \x01(\x0b2>.google.cloud.securityposture.v1.CustomConfig.ResourceSelectorB\x03\xe0A\x02\x12M\n\x08severity\x18\x04 \x01(\x0e26.google.cloud.securityposture.v1.CustomConfig.SeverityB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0erecommendation\x18\x06 \x01(\tB\x03\xe0A\x01\x1a\xc5\x01\n\x10CustomOutputSpec\x12`\n\nproperties\x18\x01 \x03(\x0b2G.google.cloud.securityposture.v1.CustomConfig.CustomOutputSpec.PropertyB\x03\xe0A\x01\x1aO\n\x08Property\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x120\n\x10value_expression\x18\x02 \x01(\x0b2\x11.google.type.ExprB\x03\xe0A\x01\x1a/\n\x10ResourceSelector\x12\x1b\n\x0eresource_types\x18\x01 \x03(\tB\x03\xe0A\x02"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04B\x8c\x01\n#com.google.cloud.securityposture.v1B\x14ShaCustomConfigProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securityposture.v1.sha_custom_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.securityposture.v1B\x14ShaCustomConfigProtoP\x01ZMcloud.google.com/go/securityposture/apiv1/securityposturepb;securityposturepb'
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY'].fields_by_name['value_expression']._loaded_options = None
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY'].fields_by_name['value_expression']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC'].fields_by_name['properties']._loaded_options = None
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR'].fields_by_name['resource_types']._loaded_options = None
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR'].fields_by_name['resource_types']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONFIG'].fields_by_name['predicate']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['predicate']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONFIG'].fields_by_name['custom_output']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['custom_output']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMCONFIG'].fields_by_name['resource_selector']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['resource_selector']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONFIG'].fields_by_name['severity']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['severity']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONFIG'].fields_by_name['description']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMCONFIG'].fields_by_name['recommendation']._loaded_options = None
    _globals['_CUSTOMCONFIG'].fields_by_name['recommendation']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMCONFIG']._serialized_start = 150
    _globals['_CUSTOMCONFIG']._serialized_end = 861
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC']._serialized_start = 532
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC']._serialized_end = 729
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY']._serialized_start = 650
    _globals['_CUSTOMCONFIG_CUSTOMOUTPUTSPEC_PROPERTY']._serialized_end = 729
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR']._serialized_start = 731
    _globals['_CUSTOMCONFIG_RESOURCESELECTOR']._serialized_end = 778
    _globals['_CUSTOMCONFIG_SEVERITY']._serialized_start = 780
    _globals['_CUSTOMCONFIG_SEVERITY']._serialized_end = 861