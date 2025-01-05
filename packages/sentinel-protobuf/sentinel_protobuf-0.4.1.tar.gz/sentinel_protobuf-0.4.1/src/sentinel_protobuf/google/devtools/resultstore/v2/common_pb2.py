"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/resultstore/v2/common.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"_\n\x10StatusAttributes\x126\n\x06status\x18\x01 \x01(\x0e2&.google.devtools.resultstore.v2.Status\x12\x13\n\x0bdescription\x18\x02 \x01(\t"&\n\x08Property\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"e\n\x06Timing\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xf8\x01\n\nDependency\x12\x15\n\x06target\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x12 \n\x11configured_target\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x12\x15\n\x06action\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x129\n\x02id\x18\x05 \x01(\x0b2-.google.devtools.resultstore.v2.Dependency.Id\x12\r\n\x05label\x18\x04 \x01(\t\x1aD\n\x02Id\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x18\n\x10configuration_id\x18\x03 \x01(\t\x12\x11\n\taction_id\x18\x04 \x01(\tB\n\n\x08resource*\xed\x01\n\x08Language\x12\x18\n\x14LANGUAGE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0b\n\x07ANDROID\x10\x02\x12\x06\n\x02AS\x10\x03\x12\x06\n\x02CC\x10\x04\x12\x07\n\x03CSS\x10\x05\x12\x08\n\x04DART\x10\x06\x12\x06\n\x02GO\x10\x07\x12\x07\n\x03GWT\x10\x08\x12\x0b\n\x07HASKELL\x10\t\x12\x08\n\x04JAVA\x10\n\x12\x06\n\x02JS\x10\x0b\x12\x08\n\x04LISP\x10\x0c\x12\x08\n\x04OBJC\x10\r\x12\x06\n\x02PY\x10\x0e\x12\x06\n\x02SH\x10\x0f\x12\t\n\x05SWIFT\x10\x10\x12\x06\n\x02TS\x10\x12\x12\x07\n\x03WEB\x10\x13\x12\t\n\x05SCALA\x10\x14\x12\t\n\x05PROTO\x10\x15\x12\x07\n\x03XML\x10\x16*\xd7\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08BUILDING\x10\x01\x12\t\n\x05BUILT\x10\x02\x12\x13\n\x0fFAILED_TO_BUILD\x10\x03\x12\x0b\n\x07TESTING\x10\x04\x12\n\n\x06PASSED\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tTIMED_OUT\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x0f\n\x0bTOOL_FAILED\x10\t\x12\x0e\n\nINCOMPLETE\x10\n\x12\t\n\x05FLAKY\x10\x0b\x12\x0b\n\x07UNKNOWN\x10\x0c\x12\x0b\n\x07SKIPPED\x10\r*`\n\x0cUploadStatus\x12\x1d\n\x19UPLOAD_STATUS_UNSPECIFIED\x10\x00\x12\r\n\tUPLOADING\x10\x01\x12\x13\n\x0fPOST_PROCESSING\x10\x02\x12\r\n\tIMMUTABLE\x10\x03B~\n"com.google.devtools.resultstore.v2B\x0bCommonProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0bCommonProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_DEPENDENCY'].fields_by_name['target']._loaded_options = None
    _globals['_DEPENDENCY'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_DEPENDENCY'].fields_by_name['configured_target']._loaded_options = None
    _globals['_DEPENDENCY'].fields_by_name['configured_target']._serialized_options = b'\xe0A\x03'
    _globals['_DEPENDENCY'].fields_by_name['action']._loaded_options = None
    _globals['_DEPENDENCY'].fields_by_name['action']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGE']._serialized_start = 669
    _globals['_LANGUAGE']._serialized_end = 906
    _globals['_STATUS']._serialized_start = 909
    _globals['_STATUS']._serialized_end = 1124
    _globals['_UPLOADSTATUS']._serialized_start = 1126
    _globals['_UPLOADSTATUS']._serialized_end = 1222
    _globals['_STATUSATTRIBUTES']._serialized_start = 177
    _globals['_STATUSATTRIBUTES']._serialized_end = 272
    _globals['_PROPERTY']._serialized_start = 274
    _globals['_PROPERTY']._serialized_end = 312
    _globals['_TIMING']._serialized_start = 314
    _globals['_TIMING']._serialized_end = 415
    _globals['_DEPENDENCY']._serialized_start = 418
    _globals['_DEPENDENCY']._serialized_end = 666
    _globals['_DEPENDENCY_ID']._serialized_start = 586
    _globals['_DEPENDENCY_ID']._serialized_end = 654