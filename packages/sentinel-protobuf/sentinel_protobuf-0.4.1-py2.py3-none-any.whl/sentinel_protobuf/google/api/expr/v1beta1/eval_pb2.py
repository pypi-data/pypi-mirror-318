"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/expr/v1beta1/eval.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1beta1 import value_pb2 as google_dot_api_dot_expr_dot_v1beta1_dot_value__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/api/expr/v1beta1/eval.proto\x12\x17google.api.expr.v1beta1\x1a#google/api/expr/v1beta1/value.proto\x1a\x17google/rpc/status.proto"\xc2\x01\n\tEvalState\x122\n\x06values\x18\x01 \x03(\x0b2".google.api.expr.v1beta1.ExprValue\x12:\n\x07results\x18\x03 \x03(\x0b2).google.api.expr.v1beta1.EvalState.Result\x1aE\n\x06Result\x12,\n\x04expr\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1beta1.IdRef\x12\r\n\x05value\x18\x02 \x01(\x05"\xb0\x01\n\tExprValue\x12/\n\x05value\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1beta1.ValueH\x00\x122\n\x05error\x18\x02 \x01(\x0b2!.google.api.expr.v1beta1.ErrorSetH\x00\x126\n\x07unknown\x18\x03 \x01(\x0b2#.google.api.expr.v1beta1.UnknownSetH\x00B\x06\n\x04kind".\n\x08ErrorSet\x12"\n\x06errors\x18\x01 \x03(\x0b2\x12.google.rpc.Status";\n\nUnknownSet\x12-\n\x05exprs\x18\x01 \x03(\x0b2\x1e.google.api.expr.v1beta1.IdRef"\x13\n\x05IdRef\x12\n\n\x02id\x18\x01 \x01(\x05Bj\n\x1bcom.google.api.expr.v1beta1B\tEvalProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1beta1.eval_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.api.expr.v1beta1B\tEvalProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01'
    _globals['_EVALSTATE']._serialized_start = 126
    _globals['_EVALSTATE']._serialized_end = 320
    _globals['_EVALSTATE_RESULT']._serialized_start = 251
    _globals['_EVALSTATE_RESULT']._serialized_end = 320
    _globals['_EXPRVALUE']._serialized_start = 323
    _globals['_EXPRVALUE']._serialized_end = 499
    _globals['_ERRORSET']._serialized_start = 501
    _globals['_ERRORSET']._serialized_end = 547
    _globals['_UNKNOWNSET']._serialized_start = 549
    _globals['_UNKNOWNSET']._serialized_end = 608
    _globals['_IDREF']._serialized_start = 610
    _globals['_IDREF']._serialized_end = 629