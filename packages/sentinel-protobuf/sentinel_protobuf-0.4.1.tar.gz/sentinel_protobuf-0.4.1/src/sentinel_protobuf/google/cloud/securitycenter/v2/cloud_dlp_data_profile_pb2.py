"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/cloud_dlp_data_profile.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/securitycenter/v2/cloud_dlp_data_profile.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x19google/api/resource.proto"\xf4\x01\n\x13CloudDlpDataProfile\x12>\n\x0cdata_profile\x18\x01 \x01(\tB(\xfaA%\n#dlp.googleapis.com/TableDataProfile\x12S\n\x0bparent_type\x18\x02 \x01(\x0e2>.google.cloud.securitycenter.v2.CloudDlpDataProfile.ParentType"H\n\nParentType\x12\x1b\n\x17PARENT_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cORGANIZATION\x10\x01\x12\x0b\n\x07PROJECT\x10\x02B\x94\x03\n"com.google.cloud.securitycenter.v2B\x18CloudDlpDataProfileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2\xeaA\x9e\x01\n#dlp.googleapis.com/TableDataProfile\x120projects/{project}/tableProfiles/{table_profile}\x12Eprojects/{project}/locations/{location}/tableProfiles/{table_profile}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.cloud_dlp_data_profile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x18CloudDlpDataProfileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2\xeaA\x9e\x01\n#dlp.googleapis.com/TableDataProfile\x120projects/{project}/tableProfiles/{table_profile}\x12Eprojects/{project}/locations/{location}/tableProfiles/{table_profile}'
    _globals['_CLOUDDLPDATAPROFILE'].fields_by_name['data_profile']._loaded_options = None
    _globals['_CLOUDDLPDATAPROFILE'].fields_by_name['data_profile']._serialized_options = b'\xfaA%\n#dlp.googleapis.com/TableDataProfile'
    _globals['_CLOUDDLPDATAPROFILE']._serialized_start = 123
    _globals['_CLOUDDLPDATAPROFILE']._serialized_end = 367
    _globals['_CLOUDDLPDATAPROFILE_PARENTTYPE']._serialized_start = 295
    _globals['_CLOUDDLPDATAPROFILE_PARENTTYPE']._serialized_end = 367