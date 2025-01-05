"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/audit_data.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1 import appengine_pb2 as google_dot_appengine_dot_v1_dot_appengine__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/appengine/v1/audit_data.proto\x12\x13google.appengine.v1\x1a#google/appengine/v1/appengine.proto"\x9d\x01\n\tAuditData\x12B\n\x0eupdate_service\x18\x01 \x01(\x0b2(.google.appengine.v1.UpdateServiceMethodH\x00\x12B\n\x0ecreate_version\x18\x02 \x01(\x0b2(.google.appengine.v1.CreateVersionMethodH\x00B\x08\n\x06method"Q\n\x13UpdateServiceMethod\x12:\n\x07request\x18\x01 \x01(\x0b2).google.appengine.v1.UpdateServiceRequest"Q\n\x13CreateVersionMethod\x12:\n\x07request\x18\x01 \x01(\x0b2).google.appengine.v1.CreateVersionRequestB\xbf\x01\n\x17com.google.appengine.v1B\x0eAuditDataProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x0eAuditDataProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_AUDITDATA']._serialized_start = 99
    _globals['_AUDITDATA']._serialized_end = 256
    _globals['_UPDATESERVICEMETHOD']._serialized_start = 258
    _globals['_UPDATESERVICEMETHOD']._serialized_end = 339
    _globals['_CREATEVERSIONMETHOD']._serialized_start = 341
    _globals['_CREATEVERSIONMETHOD']._serialized_end = 422