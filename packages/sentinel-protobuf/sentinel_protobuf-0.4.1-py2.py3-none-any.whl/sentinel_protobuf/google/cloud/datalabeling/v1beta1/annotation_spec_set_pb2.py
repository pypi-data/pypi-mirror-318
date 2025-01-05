"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/annotation_spec_set.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/datalabeling/v1beta1/annotation_spec_set.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x19google/api/resource.proto"\xa6\x02\n\x11AnnotationSpecSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12K\n\x10annotation_specs\x18\x04 \x03(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12\x1a\n\x12blocking_resources\x18\x05 \x03(\t:o\xeaAl\n-datalabeling.googleapis.com/AnnotationSpecSet\x12;projects/{project}/annotationSpecSets/{annotation_spec_set}";\n\x0eAnnotationSpec\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\tB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.annotation_spec_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_ANNOTATIONSPECSET']._loaded_options = None
    _globals['_ANNOTATIONSPECSET']._serialized_options = b'\xeaAl\n-datalabeling.googleapis.com/AnnotationSpecSet\x12;projects/{project}/annotationSpecSets/{annotation_spec_set}'
    _globals['_ANNOTATIONSPECSET']._serialized_start = 126
    _globals['_ANNOTATIONSPECSET']._serialized_end = 420
    _globals['_ANNOTATIONSPEC']._serialized_start = 422
    _globals['_ANNOTATIONSPEC']._serialized_end = 481