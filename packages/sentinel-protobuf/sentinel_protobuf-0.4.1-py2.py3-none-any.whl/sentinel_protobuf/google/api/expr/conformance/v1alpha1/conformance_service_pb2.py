"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/expr/conformance/v1alpha1/conformance_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api.expr.v1alpha1 import checked_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_checked__pb2
from ......google.api.expr.v1alpha1 import eval_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_eval__pb2
from ......google.api.expr.v1alpha1 import syntax_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_syntax__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/api/expr/conformance/v1alpha1/conformance_service.proto\x12$google.api.expr.conformance.v1alpha1\x1a\x17google/api/client.proto\x1a&google/api/expr/v1alpha1/checked.proto\x1a#google/api/expr/v1alpha1/eval.proto\x1a%google/api/expr/v1alpha1/syntax.proto\x1a\x17google/rpc/status.proto"k\n\x0cParseRequest\x12\x12\n\ncel_source\x18\x01 \x01(\t\x12\x16\n\x0esyntax_version\x18\x02 \x01(\t\x12\x17\n\x0fsource_location\x18\x03 \x01(\t\x12\x16\n\x0edisable_macros\x18\x04 \x01(\x08"n\n\rParseResponse\x129\n\x0bparsed_expr\x18\x01 \x01(\x0b2$.google.api.expr.v1alpha1.ParsedExpr\x12"\n\x06issues\x18\x02 \x03(\x0b2\x12.google.rpc.Status"\xa2\x01\n\x0cCheckRequest\x129\n\x0bparsed_expr\x18\x01 \x01(\x0b2$.google.api.expr.v1alpha1.ParsedExpr\x120\n\x08type_env\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.Decl\x12\x11\n\tcontainer\x18\x03 \x01(\t\x12\x12\n\nno_std_env\x18\x04 \x01(\x08"p\n\rCheckResponse\x12;\n\x0cchecked_expr\x18\x01 \x01(\x0b2%.google.api.expr.v1alpha1.CheckedExpr\x12"\n\x06issues\x18\x02 \x03(\x0b2\x12.google.rpc.Status"\xd2\x02\n\x0bEvalRequest\x12;\n\x0bparsed_expr\x18\x01 \x01(\x0b2$.google.api.expr.v1alpha1.ParsedExprH\x00\x12=\n\x0cchecked_expr\x18\x02 \x01(\x0b2%.google.api.expr.v1alpha1.CheckedExprH\x00\x12Q\n\x08bindings\x18\x03 \x03(\x0b2?.google.api.expr.conformance.v1alpha1.EvalRequest.BindingsEntry\x12\x11\n\tcontainer\x18\x04 \x01(\t\x1aT\n\rBindingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x122\n\x05value\x18\x02 \x01(\x0b2#.google.api.expr.v1alpha1.ExprValue:\x028\x01B\x0b\n\texpr_kind"g\n\x0cEvalResponse\x123\n\x06result\x18\x01 \x01(\x0b2#.google.api.expr.v1alpha1.ExprValue\x12"\n\x06issues\x18\x02 \x03(\x0b2\x12.google.rpc.Status"P\n\x0eSourcePosition\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0c\n\x04line\x18\x03 \x01(\x05\x12\x0e\n\x06column\x18\x04 \x01(\x05"\x80\x02\n\x0cIssueDetails\x12M\n\x08severity\x18\x01 \x01(\x0e2;.google.api.expr.conformance.v1alpha1.IssueDetails.Severity\x12F\n\x08position\x18\x02 \x01(\x0b24.google.api.expr.conformance.v1alpha1.SourcePosition\x12\n\n\x02id\x18\x03 \x01(\x03"M\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bDEPRECATION\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x032\x84\x03\n\x12ConformanceService\x12r\n\x05Parse\x122.google.api.expr.conformance.v1alpha1.ParseRequest\x1a3.google.api.expr.conformance.v1alpha1.ParseResponse"\x00\x12r\n\x05Check\x122.google.api.expr.conformance.v1alpha1.CheckRequest\x1a3.google.api.expr.conformance.v1alpha1.CheckResponse"\x00\x12o\n\x04Eval\x121.google.api.expr.conformance.v1alpha1.EvalRequest\x1a2.google.api.expr.conformance.v1alpha1.EvalResponse"\x00\x1a\x15\xcaA\x12cel.googleapis.comB\x94\x01\n(com.google.api.expr.conformance.v1alpha1B\x17ConformanceServiceProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/expr/conformance/v1alpha1;confpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.conformance.v1alpha1.conformance_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.api.expr.conformance.v1alpha1B\x17ConformanceServiceProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/expr/conformance/v1alpha1;confpb\xf8\x01\x01'
    _globals['_EVALREQUEST_BINDINGSENTRY']._loaded_options = None
    _globals['_EVALREQUEST_BINDINGSENTRY']._serialized_options = b'8\x01'
    _globals['_CONFORMANCESERVICE']._loaded_options = None
    _globals['_CONFORMANCESERVICE']._serialized_options = b'\xcaA\x12cel.googleapis.com'
    _globals['_PARSEREQUEST']._serialized_start = 270
    _globals['_PARSEREQUEST']._serialized_end = 377
    _globals['_PARSERESPONSE']._serialized_start = 379
    _globals['_PARSERESPONSE']._serialized_end = 489
    _globals['_CHECKREQUEST']._serialized_start = 492
    _globals['_CHECKREQUEST']._serialized_end = 654
    _globals['_CHECKRESPONSE']._serialized_start = 656
    _globals['_CHECKRESPONSE']._serialized_end = 768
    _globals['_EVALREQUEST']._serialized_start = 771
    _globals['_EVALREQUEST']._serialized_end = 1109
    _globals['_EVALREQUEST_BINDINGSENTRY']._serialized_start = 1012
    _globals['_EVALREQUEST_BINDINGSENTRY']._serialized_end = 1096
    _globals['_EVALRESPONSE']._serialized_start = 1111
    _globals['_EVALRESPONSE']._serialized_end = 1214
    _globals['_SOURCEPOSITION']._serialized_start = 1216
    _globals['_SOURCEPOSITION']._serialized_end = 1296
    _globals['_ISSUEDETAILS']._serialized_start = 1299
    _globals['_ISSUEDETAILS']._serialized_end = 1555
    _globals['_ISSUEDETAILS_SEVERITY']._serialized_start = 1478
    _globals['_ISSUEDETAILS_SEVERITY']._serialized_end = 1555
    _globals['_CONFORMANCESERVICE']._serialized_start = 1558
    _globals['_CONFORMANCESERVICE']._serialized_end = 1946