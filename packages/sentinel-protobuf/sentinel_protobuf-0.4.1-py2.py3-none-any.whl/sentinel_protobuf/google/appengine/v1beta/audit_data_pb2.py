"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/audit_data.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1beta import appengine_pb2 as google_dot_appengine_dot_v1beta_dot_appengine__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/appengine/v1beta/audit_data.proto\x12\x17google.appengine.v1beta\x1a\'google/appengine/v1beta/appengine.proto"\xa5\x01\n\tAuditData\x12F\n\x0eupdate_service\x18\x01 \x01(\x0b2,.google.appengine.v1beta.UpdateServiceMethodH\x00\x12F\n\x0ecreate_version\x18\x02 \x01(\x0b2,.google.appengine.v1beta.CreateVersionMethodH\x00B\x08\n\x06method"U\n\x13UpdateServiceMethod\x12>\n\x07request\x18\x01 \x01(\x0b2-.google.appengine.v1beta.UpdateServiceRequest"U\n\x13CreateVersionMethod\x12>\n\x07request\x18\x01 \x01(\x0b2-.google.appengine.v1beta.CreateVersionRequestB\xd4\x01\n\x1bcom.google.appengine.v1betaB\x0eAuditDataProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0eAuditDataProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_AUDITDATA']._serialized_start = 111
    _globals['_AUDITDATA']._serialized_end = 276
    _globals['_UPDATESERVICEMETHOD']._serialized_start = 278
    _globals['_UPDATESERVICEMETHOD']._serialized_end = 363
    _globals['_CREATEVERSIONMETHOD']._serialized_start = 365
    _globals['_CREATEVERSIONMETHOD']._serialized_end = 450