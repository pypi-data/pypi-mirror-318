"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/synonymset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/contentwarehouse/v1/synonymset.proto\x12 google.cloud.contentwarehouse.v1\x1a\x19google/api/resource.proto"\xfd\x01\n\nSynonymSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07context\x18\x02 \x01(\t\x12F\n\x08synonyms\x18\x03 \x03(\x0b24.google.cloud.contentwarehouse.v1.SynonymSet.Synonym\x1a\x18\n\x07Synonym\x12\r\n\x05words\x18\x01 \x03(\t:n\xeaAk\n*contentwarehouse.googleapis.com/SynonymSet\x12=projects/{project}/locations/{location}/synonymSets/{context}B\xf7\x01\n$com.google.cloud.contentwarehouse.v1B\x0fSynonymSetProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.synonymset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x0fSynonymSetProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_SYNONYMSET']._loaded_options = None
    _globals['_SYNONYMSET']._serialized_options = b'\xeaAk\n*contentwarehouse.googleapis.com/SynonymSet\x12=projects/{project}/locations/{location}/synonymSets/{context}'
    _globals['_SYNONYMSET']._serialized_start = 115
    _globals['_SYNONYMSET']._serialized_end = 368
    _globals['_SYNONYMSET_SYNONYM']._serialized_start = 232
    _globals['_SYNONYMSET_SYNONYM']._serialized_end = 256