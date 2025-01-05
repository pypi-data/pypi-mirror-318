"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/configuration.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/resultstore/v2/configuration.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto"\xe8\x03\n\rConfiguration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x02id\x18\x02 \x01(\x0b20.google.devtools.resultstore.v2.Configuration.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.StatusAttributes\x12Y\n\x18configuration_attributes\x18\x05 \x01(\x0b27.google.devtools.resultstore.v2.ConfigurationAttributes\x12<\n\nproperties\x18\x06 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x12\x14\n\x0cdisplay_name\x18\x08 \x01(\t\x1a5\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x18\n\x10configuration_id\x18\x02 \x01(\t:X\xeaAU\n(resultstore.googleapis.com/Configuration\x12)invocations/{invocation}/configs/{config}"&\n\x17ConfigurationAttributes\x12\x0b\n\x03cpu\x18\x01 \x01(\tB\x85\x01\n"com.google.devtools.resultstore.v2B\x12ConfigurationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.configuration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x12ConfigurationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_CONFIGURATION']._loaded_options = None
    _globals['_CONFIGURATION']._serialized_options = b'\xeaAU\n(resultstore.googleapis.com/Configuration\x12)invocations/{invocation}/configs/{config}'
    _globals['_CONFIGURATION']._serialized_start = 159
    _globals['_CONFIGURATION']._serialized_end = 647
    _globals['_CONFIGURATION_ID']._serialized_start = 504
    _globals['_CONFIGURATION_ID']._serialized_end = 557
    _globals['_CONFIGURATIONATTRIBUTES']._serialized_start = 649
    _globals['_CONFIGURATIONATTRIBUTES']._serialized_end = 687