"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v2/deny.proto')
_sym_db = _symbol_database.Default()
from ....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/iam/v2/deny.proto\x12\rgoogle.iam.v2\x1a\x16google/type/expr.proto"\xab\x01\n\x08DenyRule\x12\x19\n\x11denied_principals\x18\x01 \x03(\t\x12\x1c\n\x14exception_principals\x18\x02 \x03(\t\x12\x1a\n\x12denied_permissions\x18\x03 \x03(\t\x12\x1d\n\x15exception_permissions\x18\x04 \x03(\t\x12+\n\x10denial_condition\x18\x05 \x01(\x0b2\x11.google.type.ExprB{\n\x11com.google.iam.v2B\rDenyRuleProtoP\x01Z)cloud.google.com/go/iam/apiv2/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V2\xca\x02\x13Google\\Cloud\\Iam\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v2.deny_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.google.iam.v2B\rDenyRuleProtoP\x01Z)cloud.google.com/go/iam/apiv2/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V2\xca\x02\x13Google\\Cloud\\Iam\\V2'
    _globals['_DENYRULE']._serialized_start = 68
    _globals['_DENYRULE']._serialized_end = 239