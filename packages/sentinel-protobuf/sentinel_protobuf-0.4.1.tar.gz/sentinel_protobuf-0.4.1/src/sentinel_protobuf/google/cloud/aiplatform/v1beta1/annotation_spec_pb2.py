"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/annotation_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1beta1/annotation_spec.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcc\x02\n\x0eAnnotationSpec\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x01:\x8c\x01\xeaA\x88\x01\n(aiplatform.googleapis.com/AnnotationSpec\x12\\projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}B\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13AnnotationSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.annotation_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13AnnotationSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_ANNOTATIONSPEC'].fields_by_name['name']._loaded_options = None
    _globals['_ANNOTATIONSPEC'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATIONSPEC'].fields_by_name['display_name']._loaded_options = None
    _globals['_ANNOTATIONSPEC'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATIONSPEC'].fields_by_name['create_time']._loaded_options = None
    _globals['_ANNOTATIONSPEC'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATIONSPEC'].fields_by_name['update_time']._loaded_options = None
    _globals['_ANNOTATIONSPEC'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANNOTATIONSPEC'].fields_by_name['etag']._loaded_options = None
    _globals['_ANNOTATIONSPEC'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATIONSPEC']._loaded_options = None
    _globals['_ANNOTATIONSPEC']._serialized_options = b'\xeaA\x88\x01\n(aiplatform.googleapis.com/AnnotationSpec\x12\\projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}'
    _globals['_ANNOTATIONSPEC']._serialized_start = 184
    _globals['_ANNOTATIONSPEC']._serialized_end = 516