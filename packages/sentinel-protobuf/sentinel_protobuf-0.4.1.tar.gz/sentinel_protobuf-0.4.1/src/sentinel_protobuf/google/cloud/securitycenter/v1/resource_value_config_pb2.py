"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/resource_value_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1 import resource_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/securitycenter/v1/resource_value_config.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/securitycenter/v1/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9e\x08\n\x13ResourceValueConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12J\n\x0eresource_value\x18\x02 \x01(\x0e2-.google.cloud.securitycenter.v1.ResourceValueB\x03\xe0A\x02\x12\x17\n\ntag_values\x18\x03 \x03(\tB\x03\xe0A\x02\x12\x15\n\rresource_type\x18\x04 \x01(\t\x12\r\n\x05scope\x18\x05 \x01(\t\x12q\n\x18resource_labels_selector\x18\x06 \x03(\x0b2O.google.cloud.securitycenter.v1.ResourceValueConfig.ResourceLabelsSelectorEntry\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x0ecloud_provider\x18\n \x01(\x0e2-.google.cloud.securitycenter.v1.CloudProvider\x12}\n!sensitive_data_protection_mapping\x18\x0b \x01(\x0b2R.google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMapping\x1a\xc4\x01\n\x1eSensitiveDataProtectionMapping\x12O\n\x18high_sensitivity_mapping\x18\x01 \x01(\x0e2-.google.cloud.securitycenter.v1.ResourceValue\x12Q\n\x1amedium_sensitivity_mapping\x18\x02 \x01(\x0e2-.google.cloud.securitycenter.v1.ResourceValue\x1a=\n\x1bResourceLabelsSelectorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xad\x01\xeaA\xa9\x01\n1securitycenter.googleapis.com/ResourceValueConfig\x12Iorganizations/{organization}/resourceValueConfigs/{resource_value_config}*\x14resourceValueConfigs2\x13resourceValueConfig*X\n\rResourceValue\x12\x1e\n\x1aRESOURCE_VALUE_UNSPECIFIED\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x07\n\x03LOW\x10\x03\x12\x08\n\x04NONE\x10\x04B\xf2\x01\n"com.google.cloud.securitycenter.v1B\x18ResourceValueConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.resource_value_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x18ResourceValueConfigProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_RESOURCEVALUECONFIG_RESOURCELABELSSELECTORENTRY']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG_RESOURCELABELSSELECTORENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['resource_value']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['resource_value']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['tag_values']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['tag_values']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEVALUECONFIG']._loaded_options = None
    _globals['_RESOURCEVALUECONFIG']._serialized_options = b'\xeaA\xa9\x01\n1securitycenter.googleapis.com/ResourceValueConfig\x12Iorganizations/{organization}/resourceValueConfigs/{resource_value_config}*\x14resourceValueConfigs2\x13resourceValueConfig'
    _globals['_RESOURCEVALUE']._serialized_start = 1291
    _globals['_RESOURCEVALUE']._serialized_end = 1379
    _globals['_RESOURCEVALUECONFIG']._serialized_start = 235
    _globals['_RESOURCEVALUECONFIG']._serialized_end = 1289
    _globals['_RESOURCEVALUECONFIG_SENSITIVEDATAPROTECTIONMAPPING']._serialized_start = 854
    _globals['_RESOURCEVALUECONFIG_SENSITIVEDATAPROTECTIONMAPPING']._serialized_end = 1050
    _globals['_RESOURCEVALUECONFIG_RESOURCELABELSSELECTORENTRY']._serialized_start = 1052
    _globals['_RESOURCEVALUECONFIG_RESOURCELABELSSELECTORENTRY']._serialized_end = 1113