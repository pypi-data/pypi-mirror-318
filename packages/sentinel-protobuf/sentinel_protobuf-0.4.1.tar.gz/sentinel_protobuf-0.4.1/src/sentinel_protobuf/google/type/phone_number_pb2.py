"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/type/phone_number.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/type/phone_number.proto\x12\x0bgoogle.type"\xab\x01\n\x0bPhoneNumber\x12\x15\n\x0be164_number\x18\x01 \x01(\tH\x00\x128\n\nshort_code\x18\x02 \x01(\x0b2".google.type.PhoneNumber.ShortCodeH\x00\x12\x11\n\textension\x18\x03 \x01(\t\x1a0\n\tShortCode\x12\x13\n\x0bregion_code\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\tB\x06\n\x04kindBt\n\x0fcom.google.typeB\x10PhoneNumberProtoP\x01ZDgoogle.golang.org/genproto/googleapis/type/phone_number;phone_number\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.type.phone_number_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0fcom.google.typeB\x10PhoneNumberProtoP\x01ZDgoogle.golang.org/genproto/googleapis/type/phone_number;phone_number\xf8\x01\x01\xa2\x02\x03GTP'
    _globals['_PHONENUMBER']._serialized_start = 48
    _globals['_PHONENUMBER']._serialized_end = 219
    _globals['_PHONENUMBER_SHORTCODE']._serialized_start = 163
    _globals['_PHONENUMBER_SHORTCODE']._serialized_end = 211