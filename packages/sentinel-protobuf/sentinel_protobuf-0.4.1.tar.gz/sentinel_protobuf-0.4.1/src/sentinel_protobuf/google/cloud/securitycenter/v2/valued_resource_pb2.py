"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/valued_resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/securitycenter/v2/valued_resource.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x19google/api/resource.proto"\xc6\x05\n\x0eValuedResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x02 \x01(\t\x12\x15\n\rresource_type\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12T\n\x0eresource_value\x18\x05 \x01(\x0e2<.google.cloud.securitycenter.v2.ValuedResource.ResourceValue\x12\x15\n\rexposed_score\x18\x06 \x01(\x01\x12`\n\x1bresource_value_configs_used\x18\x07 \x03(\x0b2;.google.cloud.securitycenter.v2.ResourceValueConfigMetadata"{\n\rResourceValue\x12\x1e\n\x1aRESOURCE_VALUE_UNSPECIFIED\x10\x00\x12\x16\n\x12RESOURCE_VALUE_LOW\x10\x01\x12\x19\n\x15RESOURCE_VALUE_MEDIUM\x10\x02\x12\x17\n\x13RESOURCE_VALUE_HIGH\x10\x03:\x9a\x02\xeaA\x96\x02\n,securitycenter.googleapis.com/ValuedResource\x12Worganizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}\x12lorganizations/{organization}/locations/{location}/simulations/{simluation}/valuedResources/{valued_resource}*\x0fvaluedResources2\x0evaluedResource"+\n\x1bResourceValueConfigMetadata\x12\x0c\n\x04name\x18\x01 \x01(\tB\xed\x01\n"com.google.cloud.securitycenter.v2B\x13ValuedResourceProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.valued_resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x13ValuedResourceProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_VALUEDRESOURCE']._loaded_options = None
    _globals['_VALUEDRESOURCE']._serialized_options = b'\xeaA\x96\x02\n,securitycenter.googleapis.com/ValuedResource\x12Worganizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}\x12lorganizations/{organization}/locations/{location}/simulations/{simluation}/valuedResources/{valued_resource}*\x0fvaluedResources2\x0evaluedResource'
    _globals['_VALUEDRESOURCE']._serialized_start = 116
    _globals['_VALUEDRESOURCE']._serialized_end = 826
    _globals['_VALUEDRESOURCE_RESOURCEVALUE']._serialized_start = 418
    _globals['_VALUEDRESOURCE_RESOURCEVALUE']._serialized_end = 541
    _globals['_RESOURCEVALUECONFIGMETADATA']._serialized_start = 828
    _globals['_RESOURCEVALUECONFIGMETADATA']._serialized_end = 871