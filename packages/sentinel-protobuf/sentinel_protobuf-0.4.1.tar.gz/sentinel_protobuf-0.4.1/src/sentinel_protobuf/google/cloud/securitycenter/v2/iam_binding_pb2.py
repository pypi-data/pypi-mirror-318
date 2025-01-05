"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/iam_binding.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/securitycenter/v2/iam_binding.proto\x12\x1egoogle.cloud.securitycenter.v2"\xa4\x01\n\nIamBinding\x12A\n\x06action\x18\x01 \x01(\x0e21.google.cloud.securitycenter.v2.IamBinding.Action\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x0e\n\x06member\x18\x03 \x01(\t"5\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02B\xe9\x01\n"com.google.cloud.securitycenter.v2B\x0fIamBindingProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.iam_binding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0fIamBindingProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_IAMBINDING']._serialized_start = 85
    _globals['_IAMBINDING']._serialized_end = 249
    _globals['_IAMBINDING_ACTION']._serialized_start = 196
    _globals['_IAMBINDING_ACTION']._serialized_end = 249