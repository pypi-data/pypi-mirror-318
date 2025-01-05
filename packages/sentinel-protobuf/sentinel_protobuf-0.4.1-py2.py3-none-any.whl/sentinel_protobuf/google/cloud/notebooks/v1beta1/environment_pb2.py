"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1beta1/environment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/notebooks/v1beta1/environment.proto\x12\x1egoogle.cloud.notebooks.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x03\n\x0bEnvironment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12;\n\x08vm_image\x18\x06 \x01(\x0b2\'.google.cloud.notebooks.v1beta1.VmImageH\x00\x12I\n\x0fcontainer_image\x18\x07 \x01(\x0b2..google.cloud.notebooks.v1beta1.ContainerImageH\x00\x12\x1b\n\x13post_startup_script\x18\x08 \x01(\t\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:X\xeaAU\n$notebooks.googleapis.com/Environment\x12-projects/{project}/environments/{environment}B\x0c\n\nimage_type"V\n\x07VmImage\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\nimage_name\x18\x02 \x01(\tH\x00\x12\x16\n\x0cimage_family\x18\x03 \x01(\tH\x00B\x07\n\x05image"6\n\x0eContainerImage\x12\x17\n\nrepository\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03tag\x18\x02 \x01(\tB\xe0\x01\n"com.google.cloud.notebooks.v1beta1B\x10EnvironmentProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1beta1.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.notebooks.v1beta1B\x10EnvironmentProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1'
    _globals['_ENVIRONMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT']._loaded_options = None
    _globals['_ENVIRONMENT']._serialized_options = b'\xeaAU\n$notebooks.googleapis.com/Environment\x12-projects/{project}/environments/{environment}'
    _globals['_VMIMAGE'].fields_by_name['project']._loaded_options = None
    _globals['_VMIMAGE'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_CONTAINERIMAGE'].fields_by_name['repository']._loaded_options = None
    _globals['_CONTAINERIMAGE'].fields_by_name['repository']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT']._serialized_start = 178
    _globals['_ENVIRONMENT']._serialized_end = 576
    _globals['_VMIMAGE']._serialized_start = 578
    _globals['_VMIMAGE']._serialized_end = 664
    _globals['_CONTAINERIMAGE']._serialized_start = 666
    _globals['_CONTAINERIMAGE']._serialized_end = 720