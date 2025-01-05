"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/expr/v1alpha1/checked.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1alpha1 import syntax_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_syntax__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/api/expr/v1alpha1/checked.proto\x12\x18google.api.expr.v1alpha1\x1a%google/api/expr/v1alpha1/syntax.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcc\x03\n\x0bCheckedExpr\x12N\n\rreference_map\x18\x02 \x03(\x0b27.google.api.expr.v1alpha1.CheckedExpr.ReferenceMapEntry\x12D\n\x08type_map\x18\x03 \x03(\x0b22.google.api.expr.v1alpha1.CheckedExpr.TypeMapEntry\x129\n\x0bsource_info\x18\x05 \x01(\x0b2$.google.api.expr.v1alpha1.SourceInfo\x12\x14\n\x0cexpr_version\x18\x06 \x01(\t\x12,\n\x04expr\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Expr\x1aX\n\x11ReferenceMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x122\n\x05value\x18\x02 \x01(\x0b2#.google.api.expr.v1alpha1.Reference:\x028\x01\x1aN\n\x0cTypeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12-\n\x05value\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type:\x028\x01"\x82\n\n\x04Type\x12%\n\x03dyn\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12*\n\x04null\x18\x02 \x01(\x0e2\x1a.google.protobuf.NullValueH\x00\x12A\n\tprimitive\x18\x03 \x01(\x0e2,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00\x12?\n\x07wrapper\x18\x04 \x01(\x0e2,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00\x12B\n\nwell_known\x18\x05 \x01(\x0e2,.google.api.expr.v1alpha1.Type.WellKnownTypeH\x00\x12<\n\tlist_type\x18\x06 \x01(\x0b2\'.google.api.expr.v1alpha1.Type.ListTypeH\x00\x12:\n\x08map_type\x18\x07 \x01(\x0b2&.google.api.expr.v1alpha1.Type.MapTypeH\x00\x12?\n\x08function\x18\x08 \x01(\x0b2+.google.api.expr.v1alpha1.Type.FunctionTypeH\x00\x12\x16\n\x0cmessage_type\x18\t \x01(\tH\x00\x12\x14\n\ntype_param\x18\n \x01(\tH\x00\x12.\n\x04type\x18\x0b \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeH\x00\x12\'\n\x05error\x18\x0c \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12D\n\rabstract_type\x18\x0e \x01(\x0b2+.google.api.expr.v1alpha1.Type.AbstractTypeH\x00\x1a=\n\x08ListType\x121\n\telem_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x1ao\n\x07MapType\x120\n\x08key_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x122\n\nvalue_type\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x1av\n\x0cFunctionType\x123\n\x0bresult_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x121\n\targ_types\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.Type\x1aU\n\x0cAbstractType\x12\x0c\n\x04name\x18\x01 \x01(\t\x127\n\x0fparameter_types\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.Type"s\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06UINT64\x10\x03\x12\n\n\x06DOUBLE\x10\x04\x12\n\n\x06STRING\x10\x05\x12\t\n\x05BYTES\x10\x06"V\n\rWellKnownType\x12\x1f\n\x1bWELL_KNOWN_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ANY\x10\x01\x12\r\n\tTIMESTAMP\x10\x02\x12\x0c\n\x08DURATION\x10\x03B\x0b\n\ttype_kind"\xb9\x04\n\x04Decl\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x05ident\x18\x02 \x01(\x0b2(.google.api.expr.v1alpha1.Decl.IdentDeclH\x00\x12?\n\x08function\x18\x03 \x01(\x0b2+.google.api.expr.v1alpha1.Decl.FunctionDeclH\x00\x1ay\n\tIdentDecl\x12,\n\x04type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x121\n\x05value\x18\x02 \x01(\x0b2".google.api.expr.v1alpha1.Constant\x12\x0b\n\x03doc\x18\x03 \x01(\t\x1a\x9e\x02\n\x0cFunctionDecl\x12G\n\toverloads\x18\x01 \x03(\x0b24.google.api.expr.v1alpha1.Decl.FunctionDecl.Overload\x1a\xc4\x01\n\x08Overload\x12\x13\n\x0boverload_id\x18\x01 \x01(\t\x12.\n\x06params\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.Type\x12\x13\n\x0btype_params\x18\x03 \x03(\t\x123\n\x0bresult_type\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.Type\x12\x1c\n\x14is_instance_function\x18\x05 \x01(\x08\x12\x0b\n\x03doc\x18\x06 \x01(\tB\x0b\n\tdecl_kind"a\n\tReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0boverload_id\x18\x03 \x03(\t\x121\n\x05value\x18\x04 \x01(\x0b2".google.api.expr.v1alpha1.ConstantBl\n\x1ccom.google.api.expr.v1alpha1B\tDeclProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.checked_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\tDeclProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._loaded_options = None
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._loaded_options = None
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKEDEXPR']._serialized_start = 167
    _globals['_CHECKEDEXPR']._serialized_end = 627
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_start = 459
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_end = 547
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_start = 549
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_end = 627
    _globals['_TYPE']._serialized_start = 630
    _globals['_TYPE']._serialized_end = 1912
    _globals['_TYPE_LISTTYPE']._serialized_start = 1313
    _globals['_TYPE_LISTTYPE']._serialized_end = 1374
    _globals['_TYPE_MAPTYPE']._serialized_start = 1376
    _globals['_TYPE_MAPTYPE']._serialized_end = 1487
    _globals['_TYPE_FUNCTIONTYPE']._serialized_start = 1489
    _globals['_TYPE_FUNCTIONTYPE']._serialized_end = 1607
    _globals['_TYPE_ABSTRACTTYPE']._serialized_start = 1609
    _globals['_TYPE_ABSTRACTTYPE']._serialized_end = 1694
    _globals['_TYPE_PRIMITIVETYPE']._serialized_start = 1696
    _globals['_TYPE_PRIMITIVETYPE']._serialized_end = 1811
    _globals['_TYPE_WELLKNOWNTYPE']._serialized_start = 1813
    _globals['_TYPE_WELLKNOWNTYPE']._serialized_end = 1899
    _globals['_DECL']._serialized_start = 1915
    _globals['_DECL']._serialized_end = 2484
    _globals['_DECL_IDENTDECL']._serialized_start = 2061
    _globals['_DECL_IDENTDECL']._serialized_end = 2182
    _globals['_DECL_FUNCTIONDECL']._serialized_start = 2185
    _globals['_DECL_FUNCTIONDECL']._serialized_end = 2471
    _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_start = 2275
    _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_end = 2471
    _globals['_REFERENCE']._serialized_start = 2486
    _globals['_REFERENCE']._serialized_end = 2583