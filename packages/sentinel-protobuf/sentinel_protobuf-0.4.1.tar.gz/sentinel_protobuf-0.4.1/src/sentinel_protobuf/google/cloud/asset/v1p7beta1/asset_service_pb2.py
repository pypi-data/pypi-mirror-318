"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/asset/v1p7beta1/asset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/asset/v1p7beta1/asset_service.proto\x12\x1cgoogle.cloud.asset.v1p7beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x02\n\x13ExportAssetsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudasset.googleapis.com/Asset\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0basset_types\x18\x03 \x03(\t\x12?\n\x0ccontent_type\x18\x04 \x01(\x0e2).google.cloud.asset.v1p7beta1.ContentType\x12F\n\routput_config\x18\x05 \x01(\x0b2*.google.cloud.asset.v1p7beta1.OutputConfigB\x03\xe0A\x02\x12\x1a\n\x12relationship_types\x18\x06 \x03(\t"\xcb\x01\n\x14ExportAssetsResponse\x12-\n\tread_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\routput_config\x18\x02 \x01(\x0b2*.google.cloud.asset.v1p7beta1.OutputConfig\x12A\n\routput_result\x18\x03 \x01(\x0b2*.google.cloud.asset.v1p7beta1.OutputResult"\xb9\x01\n\x0cOutputConfig\x12G\n\x0fgcs_destination\x18\x01 \x01(\x0b2,.google.cloud.asset.v1p7beta1.GcsDestinationH\x00\x12Q\n\x14bigquery_destination\x18\x02 \x01(\x0b21.google.cloud.asset.v1p7beta1.BigQueryDestinationH\x00B\r\n\x0bdestination"]\n\x0cOutputResult\x12C\n\ngcs_result\x18\x01 \x01(\x0b2-.google.cloud.asset.v1p7beta1.GcsOutputResultH\x00B\x08\n\x06result"\x1f\n\x0fGcsOutputResult\x12\x0c\n\x04uris\x18\x01 \x03(\t"C\n\x0eGcsDestination\x12\r\n\x03uri\x18\x01 \x01(\tH\x00\x12\x14\n\nuri_prefix\x18\x02 \x01(\tH\x00B\x0c\n\nobject_uri"\xbb\x01\n\x13BigQueryDestination\x12\x14\n\x07dataset\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05table\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05force\x18\x03 \x01(\x08\x12C\n\x0epartition_spec\x18\x04 \x01(\x0b2+.google.cloud.asset.v1p7beta1.PartitionSpec\x12&\n\x1eseparate_tables_per_asset_type\x18\x05 \x01(\x08"\xb0\x01\n\rPartitionSpec\x12O\n\rpartition_key\x18\x01 \x01(\x0e28.google.cloud.asset.v1p7beta1.PartitionSpec.PartitionKey"N\n\x0cPartitionKey\x12\x1d\n\x19PARTITION_KEY_UNSPECIFIED\x10\x00\x12\r\n\tREAD_TIME\x10\x01\x12\x10\n\x0cREQUEST_TIME\x10\x02*~\n\x0bContentType\x12\x1c\n\x18CONTENT_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08RESOURCE\x10\x01\x12\x0e\n\nIAM_POLICY\x10\x02\x12\x0e\n\nORG_POLICY\x10\x04\x12\x11\n\rACCESS_POLICY\x10\x05\x12\x10\n\x0cRELATIONSHIP\x10\x072\xda\x02\n\x0cAssetService\x12\xfa\x01\n\x0cExportAssets\x121.google.cloud.asset.v1p7beta1.ExportAssetsRequest\x1a\x1d.google.longrunning.Operation"\x97\x01\xcaAe\n1google.cloud.asset.v1p7beta1.ExportAssetsResponse\x120google.cloud.asset.v1p7beta1.ExportAssetsRequest\x82\xd3\xe4\x93\x02)"$/v1p7beta1/{parent=*/*}:exportAssets:\x01*\x1aM\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x01\n com.google.cloud.asset.v1p7beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p7beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P7Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p7beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1p7beta1.asset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.asset.v1p7beta1B\x11AssetServiceProtoP\x01Z6cloud.google.com/go/asset/apiv1p7beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1P7Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p7beta1'
    _globals['_EXPORTASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudasset.googleapis.com/Asset'
    _globals['_EXPORTASSETSREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTASSETSREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYDESTINATION'].fields_by_name['dataset']._loaded_options = None
    _globals['_BIGQUERYDESTINATION'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYDESTINATION'].fields_by_name['table']._loaded_options = None
    _globals['_BIGQUERYDESTINATION'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETSERVICE']._loaded_options = None
    _globals['_ASSETSERVICE']._serialized_options = b'\xcaA\x19cloudasset.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSETSERVICE'].methods_by_name['ExportAssets']._loaded_options = None
    _globals['_ASSETSERVICE'].methods_by_name['ExportAssets']._serialized_options = b'\xcaAe\n1google.cloud.asset.v1p7beta1.ExportAssetsResponse\x120google.cloud.asset.v1p7beta1.ExportAssetsRequest\x82\xd3\xe4\x93\x02)"$/v1p7beta1/{parent=*/*}:exportAssets:\x01*'
    _globals['_CONTENTTYPE']._serialized_start = 1541
    _globals['_CONTENTTYPE']._serialized_end = 1667
    _globals['_EXPORTASSETSREQUEST']._serialized_start = 268
    _globals['_EXPORTASSETSREQUEST']._serialized_end = 579
    _globals['_EXPORTASSETSRESPONSE']._serialized_start = 582
    _globals['_EXPORTASSETSRESPONSE']._serialized_end = 785
    _globals['_OUTPUTCONFIG']._serialized_start = 788
    _globals['_OUTPUTCONFIG']._serialized_end = 973
    _globals['_OUTPUTRESULT']._serialized_start = 975
    _globals['_OUTPUTRESULT']._serialized_end = 1068
    _globals['_GCSOUTPUTRESULT']._serialized_start = 1070
    _globals['_GCSOUTPUTRESULT']._serialized_end = 1101
    _globals['_GCSDESTINATION']._serialized_start = 1103
    _globals['_GCSDESTINATION']._serialized_end = 1170
    _globals['_BIGQUERYDESTINATION']._serialized_start = 1173
    _globals['_BIGQUERYDESTINATION']._serialized_end = 1360
    _globals['_PARTITIONSPEC']._serialized_start = 1363
    _globals['_PARTITIONSPEC']._serialized_end = 1539
    _globals['_PARTITIONSPEC_PARTITIONKEY']._serialized_start = 1461
    _globals['_PARTITIONSPEC_PARTITIONKEY']._serialized_end = 1539
    _globals['_ASSETSERVICE']._serialized_start = 1670
    _globals['_ASSETSERVICE']._serialized_end = 2016