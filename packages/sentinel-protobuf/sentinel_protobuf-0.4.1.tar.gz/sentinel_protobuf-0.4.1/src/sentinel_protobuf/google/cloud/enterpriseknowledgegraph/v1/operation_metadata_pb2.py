"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/enterpriseknowledgegraph/v1/operation_metadata.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/enterpriseknowledgegraph/v1/operation_metadata.proto\x12(google.cloud.enterpriseknowledgegraph.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xc7\x02\n\x17CommonOperationMetadata\x12V\n\x05state\x18\x01 \x01(\x0e2G.google.cloud.enterpriseknowledgegraph.v1.CommonOperationMetadata.State\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"r\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0e\n\nCANCELLING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x0b\n\x07PENDING\x10\x06B\xb6\x02\n,com.google.cloud.enterpriseknowledgegraph.v1B\x16OperationMetadataProtoP\x01Zhcloud.google.com/go/enterpriseknowledgegraph/apiv1/enterpriseknowledgegraphpb;enterpriseknowledgegraphpb\xaa\x02(Google.Cloud.EnterpriseKnowledgeGraph.V1\xca\x02(Google\\Cloud\\EnterpriseKnowledgeGraph\\V1\xea\x02+Google::Cloud::EnterpriseKnowledgeGraph::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.enterpriseknowledgegraph.v1.operation_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.enterpriseknowledgegraph.v1B\x16OperationMetadataProtoP\x01Zhcloud.google.com/go/enterpriseknowledgegraph/apiv1/enterpriseknowledgegraphpb;enterpriseknowledgegraphpb\xaa\x02(Google.Cloud.EnterpriseKnowledgeGraph.V1\xca\x02(Google\\Cloud\\EnterpriseKnowledgeGraph\\V1\xea\x02+Google::Cloud::EnterpriseKnowledgeGraph::V1'
    _globals['_COMMONOPERATIONMETADATA']._serialized_start = 145
    _globals['_COMMONOPERATIONMETADATA']._serialized_end = 472
    _globals['_COMMONOPERATIONMETADATA_STATE']._serialized_start = 358
    _globals['_COMMONOPERATIONMETADATA_STATE']._serialized_end = 472