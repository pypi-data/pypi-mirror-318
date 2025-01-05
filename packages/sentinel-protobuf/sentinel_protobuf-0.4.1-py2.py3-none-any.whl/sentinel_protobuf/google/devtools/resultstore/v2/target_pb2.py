"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/resultstore/v2/target.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\x1a)google/devtools/resultstore/v2/file.proto"\xf3\x04\n\x06Target\x12\x0c\n\x04name\x18\x01 \x01(\t\x125\n\x02id\x18\x02 \x01(\x0b2).google.devtools.resultstore.v2.Target.Id\x12O\n\x11status_attributes\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.StatusAttributesB\x02\x18\x01\x126\n\x06timing\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12K\n\x11target_attributes\x18\x05 \x01(\x0b20.google.devtools.resultstore.v2.TargetAttributes\x12G\n\x0ftest_attributes\x18\x06 \x01(\x0b2..google.devtools.resultstore.v2.TestAttributes\x12<\n\nproperties\x18\x07 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\x08 \x03(\x0b2$.google.devtools.resultstore.v2.File\x12\x0f\n\x07visible\x18\n \x01(\x08\x1a.\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t:Q\xeaAN\n!resultstore.googleapis.com/Target\x12)invocations/{invocation}/targets/{target}"\x96\x01\n\x10TargetAttributes\x128\n\x04type\x18\x01 \x01(\x0e2*.google.devtools.resultstore.v2.TargetType\x12:\n\x08language\x18\x02 \x01(\x0e2(.google.devtools.resultstore.v2.Language\x12\x0c\n\x04tags\x18\x03 \x03(\t"H\n\x0eTestAttributes\x126\n\x04size\x18\x01 \x01(\x0e2(.google.devtools.resultstore.v2.TestSize*j\n\nTargetType\x12\x1b\n\x17TARGET_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bAPPLICATION\x10\x01\x12\n\n\x06BINARY\x10\x02\x12\x0b\n\x07LIBRARY\x10\x03\x12\x0b\n\x07PACKAGE\x10\x04\x12\x08\n\x04TEST\x10\x05*e\n\x08TestSize\x12\x19\n\x15TEST_SIZE_UNSPECIFIED\x10\x00\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LARGE\x10\x03\x12\x0c\n\x08ENORMOUS\x10\x04\x12\x0e\n\nOTHER_SIZE\x10\x05B~\n"com.google.devtools.resultstore.v2B\x0bTargetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0bTargetProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_TARGET'].fields_by_name['status_attributes']._loaded_options = None
    _globals['_TARGET'].fields_by_name['status_attributes']._serialized_options = b'\x18\x01'
    _globals['_TARGET']._loaded_options = None
    _globals['_TARGET']._serialized_options = b'\xeaAN\n!resultstore.googleapis.com/Target\x12)invocations/{invocation}/targets/{target}'
    _globals['_TARGETTYPE']._serialized_start = 1051
    _globals['_TARGETTYPE']._serialized_end = 1157
    _globals['_TESTSIZE']._serialized_start = 1159
    _globals['_TESTSIZE']._serialized_end = 1260
    _globals['_TARGET']._serialized_start = 195
    _globals['_TARGET']._serialized_end = 822
    _globals['_TARGET_ID']._serialized_start = 693
    _globals['_TARGET_ID']._serialized_end = 739
    _globals['_TARGETATTRIBUTES']._serialized_start = 825
    _globals['_TARGETATTRIBUTES']._serialized_end = 975
    _globals['_TESTATTRIBUTES']._serialized_start = 977
    _globals['_TESTATTRIBUTES']._serialized_end = 1049