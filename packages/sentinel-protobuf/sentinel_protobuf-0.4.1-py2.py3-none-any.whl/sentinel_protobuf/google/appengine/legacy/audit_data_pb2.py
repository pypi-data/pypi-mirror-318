"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/legacy/audit_data.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/appengine/legacy/audit_data.proto\x12\x17google.appengine.legacy"\x9b\x01\n\tAuditData\x12\x15\n\revent_message\x18\x01 \x01(\t\x12E\n\nevent_data\x18\x02 \x03(\x0b21.google.appengine.legacy.AuditData.EventDataEntry\x1a0\n\x0eEventDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01Bn\n\x1bcom.google.appengine.legacyB\x0eAuditDataProtoP\x01Z=google.golang.org/genproto/googleapis/appengine/legacy;legacyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.legacy.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.legacyB\x0eAuditDataProtoP\x01Z=google.golang.org/genproto/googleapis/appengine/legacy;legacy'
    _globals['_AUDITDATA_EVENTDATAENTRY']._loaded_options = None
    _globals['_AUDITDATA_EVENTDATAENTRY']._serialized_options = b'8\x01'
    _globals['_AUDITDATA']._serialized_start = 70
    _globals['_AUDITDATA']._serialized_end = 225
    _globals['_AUDITDATA_EVENTDATAENTRY']._serialized_start = 177
    _globals['_AUDITDATA_EVENTDATAENTRY']._serialized_end = 225