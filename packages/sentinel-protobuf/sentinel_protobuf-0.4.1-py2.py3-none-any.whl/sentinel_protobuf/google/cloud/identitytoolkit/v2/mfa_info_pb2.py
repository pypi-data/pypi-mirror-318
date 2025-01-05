"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/identitytoolkit/v2/mfa_info.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/identitytoolkit/v2/mfa_info.proto\x12\x1fgoogle.cloud.identitytoolkit.v2\x1a\x1fgoogle/protobuf/timestamp.proto"/\n\x11AutoRetrievalInfo\x12\x1a\n\x12app_signature_hash\x18\x01 \x01(\t"\xdd\x01\n\x18StartMfaPhoneRequestInfo\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x12\x13\n\x0bios_receipt\x18\x02 \x01(\t\x12\x12\n\nios_secret\x18\x03 \x01(\t\x12\x17\n\x0frecaptcha_token\x18\x04 \x01(\t\x12O\n\x13auto_retrieval_info\x18\x05 \x01(\x0b22.google.cloud.identitytoolkit.v2.AutoRetrievalInfo\x12\x18\n\x10safety_net_token\x18\x06 \x01(\t"1\n\x19StartMfaPhoneResponseInfo\x12\x14\n\x0csession_info\x18\x01 \x01(\t"{\n\x1bFinalizeMfaPhoneRequestInfo\x12\x14\n\x0csession_info\x18\x01 \x01(\t\x12\x0c\n\x04code\x18\x02 \x01(\t\x12"\n\x1aandroid_verification_proof\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t"\xa4\x01\n\x1cFinalizeMfaPhoneResponseInfo\x12"\n\x1aandroid_verification_proof\x18\x01 \x01(\t\x12J\n&android_verification_proof_expire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0cphone_number\x18\x03 \x01(\tB\xdf\x01\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.identitytoolkit.v2.mfa_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2'
    _globals['_AUTORETRIEVALINFO']._serialized_start = 116
    _globals['_AUTORETRIEVALINFO']._serialized_end = 163
    _globals['_STARTMFAPHONEREQUESTINFO']._serialized_start = 166
    _globals['_STARTMFAPHONEREQUESTINFO']._serialized_end = 387
    _globals['_STARTMFAPHONERESPONSEINFO']._serialized_start = 389
    _globals['_STARTMFAPHONERESPONSEINFO']._serialized_end = 438
    _globals['_FINALIZEMFAPHONEREQUESTINFO']._serialized_start = 440
    _globals['_FINALIZEMFAPHONEREQUESTINFO']._serialized_end = 563
    _globals['_FINALIZEMFAPHONERESPONSEINFO']._serialized_start = 566
    _globals['_FINALIZEMFAPHONERESPONSEINFO']._serialized_end = 730