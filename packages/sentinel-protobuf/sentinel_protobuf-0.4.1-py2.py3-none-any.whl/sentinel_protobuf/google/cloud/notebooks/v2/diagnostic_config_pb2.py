"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v2/diagnostic_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/notebooks/v2/diagnostic_config.proto\x12\x19google.cloud.notebooks.v2\x1a\x1fgoogle/api/field_behavior.proto"\xbb\x01\n\x10DiagnosticConfig\x12\x17\n\ngcs_bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rrelative_path\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12enable_repair_flag\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\'\n\x1aenable_packet_capture_flag\x18\x04 \x01(\x08B\x03\xe0A\x01\x12(\n\x1benable_copy_home_files_flag\x18\x05 \x01(\x08B\x03\xe0A\x01B\xcc\x01\n\x1dcom.google.cloud.notebooks.v2B\x15DiagnosticConfigProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v2.diagnostic_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v2B\x15DiagnosticConfigProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2'
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['gcs_bucket']._loaded_options = None
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['gcs_bucket']._serialized_options = b'\xe0A\x02'
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['relative_path']._loaded_options = None
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['relative_path']._serialized_options = b'\xe0A\x01'
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_repair_flag']._loaded_options = None
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_repair_flag']._serialized_options = b'\xe0A\x01'
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_packet_capture_flag']._loaded_options = None
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_packet_capture_flag']._serialized_options = b'\xe0A\x01'
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_copy_home_files_flag']._loaded_options = None
    _globals['_DIAGNOSTICCONFIG'].fields_by_name['enable_copy_home_files_flag']._serialized_options = b'\xe0A\x01'
    _globals['_DIAGNOSTICCONFIG']._serialized_start = 114
    _globals['_DIAGNOSTICCONFIG']._serialized_end = 301