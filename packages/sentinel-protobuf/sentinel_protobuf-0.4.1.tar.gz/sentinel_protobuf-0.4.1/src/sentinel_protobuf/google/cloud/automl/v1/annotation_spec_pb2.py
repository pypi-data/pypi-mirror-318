"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/annotation_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1/annotation_spec.proto\x12\x16google.cloud.automl.v1\x1a\x19google/api/resource.proto"\xd6\x01\n\x0eAnnotationSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x15\n\rexample_count\x18\t \x01(\x05:\x88\x01\xeaA\x84\x01\n$automl.googleapis.com/AnnotationSpec\x12\\projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}B\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.annotation_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_ANNOTATIONSPEC']._loaded_options = None
    _globals['_ANNOTATIONSPEC']._serialized_options = b'\xeaA\x84\x01\n$automl.googleapis.com/AnnotationSpec\x12\\projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}'
    _globals['_ANNOTATIONSPEC']._serialized_start = 100
    _globals['_ANNOTATIONSPEC']._serialized_end = 314