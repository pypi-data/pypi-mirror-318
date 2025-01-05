"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/gcs_fileset_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.datacatalog.v1beta1 import timestamps_pb2 as google_dot_cloud_dot_datacatalog_dot_v1beta1_dot_timestamps__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/datacatalog/v1beta1/gcs_fileset_spec.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a1google/cloud/datacatalog/v1beta1/timestamps.proto"\x7f\n\x0eGcsFilesetSpec\x12\x1a\n\rfile_patterns\x18\x01 \x03(\tB\x03\xe0A\x02\x12Q\n\x15sample_gcs_file_specs\x18\x02 \x03(\x0b2-.google.cloud.datacatalog.v1beta1.GcsFileSpecB\x03\xe0A\x03"\x8f\x01\n\x0bGcsFileSpec\x12\x16\n\tfile_path\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\x0egcs_timestamps\x18\x02 \x01(\x0b22.google.cloud.datacatalog.v1beta1.SystemTimestampsB\x03\xe0A\x03\x12\x17\n\nsize_bytes\x18\x04 \x01(\x03B\x03\xe0A\x03B\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.gcs_fileset_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_GCSFILESETSPEC'].fields_by_name['file_patterns']._loaded_options = None
    _globals['_GCSFILESETSPEC'].fields_by_name['file_patterns']._serialized_options = b'\xe0A\x02'
    _globals['_GCSFILESETSPEC'].fields_by_name['sample_gcs_file_specs']._loaded_options = None
    _globals['_GCSFILESETSPEC'].fields_by_name['sample_gcs_file_specs']._serialized_options = b'\xe0A\x03'
    _globals['_GCSFILESPEC'].fields_by_name['file_path']._loaded_options = None
    _globals['_GCSFILESPEC'].fields_by_name['file_path']._serialized_options = b'\xe0A\x02'
    _globals['_GCSFILESPEC'].fields_by_name['gcs_timestamps']._loaded_options = None
    _globals['_GCSFILESPEC'].fields_by_name['gcs_timestamps']._serialized_options = b'\xe0A\x03'
    _globals['_GCSFILESPEC'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_GCSFILESPEC'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_GCSFILESETSPEC']._serialized_start = 177
    _globals['_GCSFILESETSPEC']._serialized_end = 304
    _globals['_GCSFILESPEC']._serialized_start = 307
    _globals['_GCSFILESPEC']._serialized_end = 450