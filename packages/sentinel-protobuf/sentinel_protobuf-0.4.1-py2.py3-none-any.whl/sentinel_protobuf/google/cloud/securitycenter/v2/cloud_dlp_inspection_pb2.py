"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/cloud_dlp_inspection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/securitycenter/v2/cloud_dlp_inspection.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x19google/api/resource.proto"\x88\x01\n\x12CloudDlpInspection\x123\n\x0binspect_job\x18\x01 \x01(\tB\x1e\xfaA\x1b\n\x19dlp.googleapis.com/DlpJob\x12\x11\n\tinfo_type\x18\x02 \x01(\t\x12\x17\n\x0finfo_type_count\x18\x03 \x01(\x03\x12\x11\n\tfull_scan\x18\x04 \x01(\x08B\xf0\x02\n"com.google.cloud.securitycenter.v2B\x17CloudDlpInspectionProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2\xeaA|\n\x19dlp.googleapis.com/DlpJob\x12$projects/{project}/dlpJobs/{dlp_job}\x129projects/{project}/locations/{location}/dlpJobs/{dlp_job}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.cloud_dlp_inspection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x17CloudDlpInspectionProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2\xeaA|\n\x19dlp.googleapis.com/DlpJob\x12$projects/{project}/dlpJobs/{dlp_job}\x129projects/{project}/locations/{location}/dlpJobs/{dlp_job}'
    _globals['_CLOUDDLPINSPECTION'].fields_by_name['inspect_job']._loaded_options = None
    _globals['_CLOUDDLPINSPECTION'].fields_by_name['inspect_job']._serialized_options = b'\xfaA\x1b\n\x19dlp.googleapis.com/DlpJob'
    _globals['_CLOUDDLPINSPECTION']._serialized_start = 121
    _globals['_CLOUDDLPINSPECTION']._serialized_end = 257