"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/reasoning_engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/reasoning_engine.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\x02\n\x13ReasoningEngineSpec\x12[\n\x0cpackage_spec\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpecB\x03\xe0A\x02\x123\n\rclass_methods\x18\x03 \x03(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a\x98\x01\n\x0bPackageSpec\x12"\n\x15pickle_object_gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12%\n\x18dependency_files_gcs_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12!\n\x14requirements_gcs_uri\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0epython_version\x18\x04 \x01(\tB\x03\xe0A\x01"\xc3\x03\n\x0fReasoningEngine\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x07 \x01(\tB\x03\xe0A\x01\x12G\n\x04spec\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ReasoningEngineSpecB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x06 \x01(\tB\x03\xe0A\x01:\x9f\x01\xeaA\x9b\x01\n)aiplatform.googleapis.com/ReasoningEngine\x12Kprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}*\x10reasoningEngines2\x0freasoningEngineB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14ReasoningEngineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.reasoning_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14ReasoningEngineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['pickle_object_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['pickle_object_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['dependency_files_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['dependency_files_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['requirements_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['requirements_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['python_version']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['python_version']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['package_spec']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['package_spec']._serialized_options = b'\xe0A\x02'
    _globals['_REASONINGENGINESPEC'].fields_by_name['class_methods']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['class_methods']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['name']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REASONINGENGINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_REASONINGENGINE'].fields_by_name['description']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['spec']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['spec']._serialized_options = b'\xe0A\x02'
    _globals['_REASONINGENGINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_REASONINGENGINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_REASONINGENGINE'].fields_by_name['etag']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE']._loaded_options = None
    _globals['_REASONINGENGINE']._serialized_options = b'\xeaA\x9b\x01\n)aiplatform.googleapis.com/ReasoningEngine\x12Kprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}*\x10reasoningEngines2\x0freasoningEngine'
    _globals['_REASONINGENGINESPEC']._serialized_start = 215
    _globals['_REASONINGENGINESPEC']._serialized_end = 537
    _globals['_REASONINGENGINESPEC_PACKAGESPEC']._serialized_start = 385
    _globals['_REASONINGENGINESPEC_PACKAGESPEC']._serialized_end = 537
    _globals['_REASONINGENGINE']._serialized_start = 540
    _globals['_REASONINGENGINE']._serialized_end = 991