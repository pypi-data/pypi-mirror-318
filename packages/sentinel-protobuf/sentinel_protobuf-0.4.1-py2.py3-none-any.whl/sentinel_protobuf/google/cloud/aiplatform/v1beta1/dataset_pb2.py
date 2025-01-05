"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import saved_query_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_saved__query__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/dataset.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a1google/cloud/aiplatform/v1beta1/saved_query.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\x06\n\x07Dataset\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x10 \x01(\t\x12 \n\x13metadata_schema_uri\x18\x03 \x01(\tB\x03\xe0A\x02\x12-\n\x08metadata\x18\x08 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12\x1c\n\x0fdata_item_count\x18\n \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x06 \x01(\t\x12D\n\x06labels\x18\x07 \x03(\x0b24.google.cloud.aiplatform.v1beta1.Dataset.LabelsEntry\x12B\n\rsaved_queries\x18\t \x03(\x0b2+.google.cloud.aiplatform.v1beta1.SavedQuery\x12H\n\x0fencryption_spec\x18\x0b \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12\x1e\n\x11metadata_artifact\x18\x11 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fmodel_reference\x18\x12 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x13 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x14 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:b\xeaA_\n!aiplatform.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}"\xb3\x03\n\x10ImportDataConfig\x12@\n\ngcs_source\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.GcsSourceH\x00\x12_\n\x10data_item_labels\x18\x02 \x03(\x0b2E.google.cloud.aiplatform.v1beta1.ImportDataConfig.DataItemLabelsEntry\x12b\n\x11annotation_labels\x18\x03 \x03(\x0b2G.google.cloud.aiplatform.v1beta1.ImportDataConfig.AnnotationLabelsEntry\x12\x1e\n\x11import_schema_uri\x18\x04 \x01(\tB\x03\xe0A\x02\x1a5\n\x13DataItemLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a7\n\x15AnnotationLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06source"\xe2\x01\n\x10ExportDataConfig\x12J\n\x0fgcs_destination\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestinationH\x00\x12N\n\x0efraction_split\x18\x05 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ExportFractionSplitH\x01\x12\x1a\n\x12annotations_filter\x18\x02 \x01(\tB\r\n\x0bdestinationB\x07\n\x05split"d\n\x13ExportFractionSplit\x12\x19\n\x11training_fraction\x18\x01 \x01(\x01\x12\x1b\n\x13validation_fraction\x18\x02 \x01(\x01\x12\x15\n\rtest_fraction\x18\x03 \x01(\x01B\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cDatasetProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cDatasetProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_DATASET_LABELSENTRY']._loaded_options = None
    _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET'].fields_by_name['name']._loaded_options = None
    _globals['_DATASET'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_DATASET'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATASET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['metadata_schema_uri']._loaded_options = None
    _globals['_DATASET'].fields_by_name['metadata_schema_uri']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['metadata']._loaded_options = None
    _globals['_DATASET'].fields_by_name['metadata']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['data_item_count']._loaded_options = None
    _globals['_DATASET'].fields_by_name['data_item_count']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['metadata_artifact']._loaded_options = None
    _globals['_DATASET'].fields_by_name['metadata_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['model_reference']._loaded_options = None
    _globals['_DATASET'].fields_by_name['model_reference']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaA_\n!aiplatform.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}'
    _globals['_IMPORTDATACONFIG_DATAITEMLABELSENTRY']._loaded_options = None
    _globals['_IMPORTDATACONFIG_DATAITEMLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTDATACONFIG_ANNOTATIONLABELSENTRY']._loaded_options = None
    _globals['_IMPORTDATACONFIG_ANNOTATIONLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTDATACONFIG'].fields_by_name['import_schema_uri']._loaded_options = None
    _globals['_IMPORTDATACONFIG'].fields_by_name['import_schema_uri']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET']._serialized_start = 354
    _globals['_DATASET']._serialized_end = 1143
    _globals['_DATASET_LABELSENTRY']._serialized_start = 998
    _globals['_DATASET_LABELSENTRY']._serialized_end = 1043
    _globals['_IMPORTDATACONFIG']._serialized_start = 1146
    _globals['_IMPORTDATACONFIG']._serialized_end = 1581
    _globals['_IMPORTDATACONFIG_DATAITEMLABELSENTRY']._serialized_start = 1461
    _globals['_IMPORTDATACONFIG_DATAITEMLABELSENTRY']._serialized_end = 1514
    _globals['_IMPORTDATACONFIG_ANNOTATIONLABELSENTRY']._serialized_start = 1516
    _globals['_IMPORTDATACONFIG_ANNOTATIONLABELSENTRY']._serialized_end = 1571
    _globals['_EXPORTDATACONFIG']._serialized_start = 1584
    _globals['_EXPORTDATACONFIG']._serialized_end = 1810
    _globals['_EXPORTFRACTIONSPLIT']._serialized_start = 1812
    _globals['_EXPORTFRACTIONSPLIT']._serialized_end = 1912