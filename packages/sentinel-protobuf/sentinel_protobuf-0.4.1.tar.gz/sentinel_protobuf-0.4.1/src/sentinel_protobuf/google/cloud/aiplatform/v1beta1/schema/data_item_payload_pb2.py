"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/data_item_payload.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/aiplatform/v1beta1/schema/data_item_payload.proto\x12&google.cloud.aiplatform.v1beta1.schema\x1a\x1fgoogle/api/field_behavior.proto"=\n\rImageDataItem\x12\x14\n\x07gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tmime_type\x18\x02 \x01(\tB\x03\xe0A\x03"=\n\rVideoDataItem\x12\x14\n\x07gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tmime_type\x18\x02 \x01(\tB\x03\xe0A\x03"$\n\x0cTextDataItem\x12\x14\n\x07gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x03B\x87\x02\n*com.google.cloud.aiplatform.v1beta1.schemaB\x14DataItemPayloadProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schemab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.data_item_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.aiplatform.v1beta1.schemaB\x14DataItemPayloadProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schema'
    _globals['_IMAGEDATAITEM'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_IMAGEDATAITEM'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_IMAGEDATAITEM'].fields_by_name['mime_type']._loaded_options = None
    _globals['_IMAGEDATAITEM'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEODATAITEM'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_VIDEODATAITEM'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEODATAITEM'].fields_by_name['mime_type']._loaded_options = None
    _globals['_VIDEODATAITEM'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x03'
    _globals['_TEXTDATAITEM'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_TEXTDATAITEM'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGEDATAITEM']._serialized_start = 139
    _globals['_IMAGEDATAITEM']._serialized_end = 200
    _globals['_VIDEODATAITEM']._serialized_start = 202
    _globals['_VIDEODATAITEM']._serialized_end = 263
    _globals['_TEXTDATAITEM']._serialized_start = 265
    _globals['_TEXTDATAITEM']._serialized_end = 301