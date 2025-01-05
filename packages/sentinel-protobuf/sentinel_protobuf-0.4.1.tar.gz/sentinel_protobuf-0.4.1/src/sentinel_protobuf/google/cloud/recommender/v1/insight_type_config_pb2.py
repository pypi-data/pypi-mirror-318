"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommender/v1/insight_type_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/recommender/v1/insight_type_config.proto\x12\x1bgoogle.cloud.recommender.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x05\n\x11InsightTypeConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12`\n\x1einsight_type_generation_config\x18\x02 \x01(\x0b28.google.cloud.recommender.v1.InsightTypeGenerationConfig\x12\x0c\n\x04etag\x18\x03 \x01(\t\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1b\n\x0brevision_id\x18\x05 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12T\n\x0bannotations\x18\x06 \x03(\x0b2?.google.cloud.recommender.v1.InsightTypeConfig.AnnotationsEntry\x12\x14\n\x0cdisplay_name\x18\x07 \x01(\t\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xaf\x02\xeaA\xab\x02\n,recommender.googleapis.com/InsightTypeConfig\x12Jprojects/{project}/locations/{location}/insightTypes/{insight_type}/config\x12Torganizations/{organization}/locations/{location}/insightTypes/{insight_type}/config\x12YbillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}/config"F\n\x1bInsightTypeGenerationConfig\x12\'\n\x06params\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\xa3\x01\n\x1fcom.google.cloud.recommender.v1B\x16InsightTypeConfigProtoP\x01ZAcloud.google.com/go/recommender/apiv1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02\x1bGoogle.Cloud.Recommender.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommender.v1.insight_type_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.recommender.v1B\x16InsightTypeConfigProtoP\x01ZAcloud.google.com/go/recommender/apiv1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02\x1bGoogle.Cloud.Recommender.V1'
    _globals['_INSIGHTTYPECONFIG_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_INSIGHTTYPECONFIG_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHTTYPECONFIG'].fields_by_name['revision_id']._loaded_options = None
    _globals['_INSIGHTTYPECONFIG'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_INSIGHTTYPECONFIG']._loaded_options = None
    _globals['_INSIGHTTYPECONFIG']._serialized_options = b'\xeaA\xab\x02\n,recommender.googleapis.com/InsightTypeConfig\x12Jprojects/{project}/locations/{location}/insightTypes/{insight_type}/config\x12Torganizations/{organization}/locations/{location}/insightTypes/{insight_type}/config\x12YbillingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}/config'
    _globals['_INSIGHTTYPECONFIG']._serialized_start = 210
    _globals['_INSIGHTTYPECONFIG']._serialized_end = 899
    _globals['_INSIGHTTYPECONFIG_ANNOTATIONSENTRY']._serialized_start = 543
    _globals['_INSIGHTTYPECONFIG_ANNOTATIONSENTRY']._serialized_end = 593
    _globals['_INSIGHTTYPEGENERATIONCONFIG']._serialized_start = 901
    _globals['_INSIGHTTYPEGENERATIONCONFIG']._serialized_end = 971