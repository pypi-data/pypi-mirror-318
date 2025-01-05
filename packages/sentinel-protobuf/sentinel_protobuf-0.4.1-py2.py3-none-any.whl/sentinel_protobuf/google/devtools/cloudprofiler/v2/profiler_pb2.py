"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/cloudprofiler/v2/profiler.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/devtools/cloudprofiler/v2/profiler.proto\x12 google.devtools.cloudprofiler.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdf\x01\n\x14CreateProfileRequest\x12@\n\x06parent\x18\x04 \x01(\tB0\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12@\n\ndeployment\x18\x01 \x01(\x0b2,.google.devtools.cloudprofiler.v2.Deployment\x12C\n\x0cprofile_type\x18\x02 \x03(\x0e2-.google.devtools.cloudprofiler.v2.ProfileType"\x9b\x01\n\x1bCreateOfflineProfileRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12:\n\x07profile\x18\x02 \x01(\x0b2).google.devtools.cloudprofiler.v2.Profile"\x83\x01\n\x14UpdateProfileRequest\x12:\n\x07profile\x18\x01 \x01(\x0b2).google.devtools.cloudprofiler.v2.Profile\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xee\x03\n\x07Profile\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12C\n\x0cprofile_type\x18\x02 \x01(\x0e2-.google.devtools.cloudprofiler.v2.ProfileType\x12@\n\ndeployment\x18\x03 \x01(\x0b2,.google.devtools.cloudprofiler.v2.Deployment\x12+\n\x08duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\rprofile_bytes\x18\x05 \x01(\x0cB\x03\xe0A\x04\x12J\n\x06labels\x18\x06 \x03(\x0b25.google.devtools.cloudprofiler.v2.Profile.LabelsEntryB\x03\xe0A\x04\x123\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:P\xeaAM\n$cloudprofiler.googleapis.com/Profile\x12%projects/{project}/profiles/{profile}"\xa9\x01\n\nDeployment\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12H\n\x06labels\x18\x03 \x03(\x0b28.google.devtools.cloudprofiler.v2.Deployment.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x81\x01\n\x13ListProfilesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x86\x01\n\x14ListProfilesResponse\x12;\n\x08profiles\x18\x01 \x03(\x0b2).google.devtools.cloudprofiler.v2.Profile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x10skipped_profiles\x18\x03 \x01(\x05*\x84\x01\n\x0bProfileType\x12\x1c\n\x18PROFILE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03CPU\x10\x01\x12\x08\n\x04WALL\x10\x02\x12\x08\n\x04HEAP\x10\x03\x12\x0b\n\x07THREADS\x10\x04\x12\x0e\n\nCONTENTION\x10\x05\x12\r\n\tPEAK_HEAP\x10\x06\x12\x0e\n\nHEAP_ALLOC\x10\x072\xfe\x05\n\x0fProfilerService\x12\x9f\x01\n\rCreateProfile\x126.google.devtools.cloudprofiler.v2.CreateProfileRequest\x1a).google.devtools.cloudprofiler.v2.Profile"+\x82\xd3\xe4\x93\x02%" /v2/{parent=projects/*}/profiles:\x01*\x12\xd2\x01\n\x14CreateOfflineProfile\x12=.google.devtools.cloudprofiler.v2.CreateOfflineProfileRequest\x1a).google.devtools.cloudprofiler.v2.Profile"P\xdaA\x0eparent,profile\x82\xd3\xe4\x93\x029"./v2/{parent=projects/*}/profiles:createOffline:\x07profile\x12\xc3\x01\n\rUpdateProfile\x126.google.devtools.cloudprofiler.v2.UpdateProfileRequest\x1a).google.devtools.cloudprofiler.v2.Profile"O\xdaA\x13profile,update_mask\x82\xd3\xe4\x93\x0232(/v2/{profile.name=projects/*/profiles/*}:\x07profile\x1a\xad\x01\xcaA\x1ccloudprofiler.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.write2\xf2\x02\n\rExportService\x12\xb0\x01\n\x0cListProfiles\x125.google.devtools.cloudprofiler.v2.ListProfilesRequest\x1a6.google.devtools.cloudprofiler.v2.ListProfilesResponse"1\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v2/{parent=projects/*}/profiles\x1a\xad\x01\xcaA\x1ccloudprofiler.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.writeB\xd4\x01\n$com.google.devtools.cloudprofiler.v2B\rProfilerProtoP\x01ZGcloud.google.com/go/cloudprofiler/apiv2/cloudprofilerpb;cloudprofilerpb\xaa\x02\x18Google.Cloud.Profiler.V2\xca\x02\x18Google\\Cloud\\Profiler\\V2\xea\x02\x1bGoogle::Cloud::Profiler::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.cloudprofiler.v2.profiler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.devtools.cloudprofiler.v2B\rProfilerProtoP\x01ZGcloud.google.com/go/cloudprofiler/apiv2/cloudprofilerpb;cloudprofilerpb\xaa\x02\x18Google.Cloud.Profiler.V2\xca\x02\x18Google\\Cloud\\Profiler\\V2\xea\x02\x1bGoogle::Cloud::Profiler::V2'
    _globals['_CREATEPROFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPROFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEOFFLINEPROFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEOFFLINEPROFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_PROFILE_LABELSENTRY']._loaded_options = None
    _globals['_PROFILE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PROFILE'].fields_by_name['name']._loaded_options = None
    _globals['_PROFILE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROFILE'].fields_by_name['profile_bytes']._loaded_options = None
    _globals['_PROFILE'].fields_by_name['profile_bytes']._serialized_options = b'\xe0A\x04'
    _globals['_PROFILE'].fields_by_name['labels']._loaded_options = None
    _globals['_PROFILE'].fields_by_name['labels']._serialized_options = b'\xe0A\x04'
    _globals['_PROFILE'].fields_by_name['start_time']._loaded_options = None
    _globals['_PROFILE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROFILE']._loaded_options = None
    _globals['_PROFILE']._serialized_options = b'\xeaAM\n$cloudprofiler.googleapis.com/Profile\x12%projects/{project}/profiles/{profile}'
    _globals['_DEPLOYMENT_LABELSENTRY']._loaded_options = None
    _globals['_DEPLOYMENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LISTPROFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_PROFILERSERVICE']._loaded_options = None
    _globals['_PROFILERSERVICE']._serialized_options = b'\xcaA\x1ccloudprofiler.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.write'
    _globals['_PROFILERSERVICE'].methods_by_name['CreateProfile']._loaded_options = None
    _globals['_PROFILERSERVICE'].methods_by_name['CreateProfile']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /v2/{parent=projects/*}/profiles:\x01*'
    _globals['_PROFILERSERVICE'].methods_by_name['CreateOfflineProfile']._loaded_options = None
    _globals['_PROFILERSERVICE'].methods_by_name['CreateOfflineProfile']._serialized_options = b'\xdaA\x0eparent,profile\x82\xd3\xe4\x93\x029"./v2/{parent=projects/*}/profiles:createOffline:\x07profile'
    _globals['_PROFILERSERVICE'].methods_by_name['UpdateProfile']._loaded_options = None
    _globals['_PROFILERSERVICE'].methods_by_name['UpdateProfile']._serialized_options = b'\xdaA\x13profile,update_mask\x82\xd3\xe4\x93\x0232(/v2/{profile.name=projects/*/profiles/*}:\x07profile'
    _globals['_EXPORTSERVICE']._loaded_options = None
    _globals['_EXPORTSERVICE']._serialized_options = b'\xcaA\x1ccloudprofiler.googleapis.com\xd2A\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.write'
    _globals['_EXPORTSERVICE'].methods_by_name['ListProfiles']._loaded_options = None
    _globals['_EXPORTSERVICE'].methods_by_name['ListProfiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v2/{parent=projects/*}/profiles'
    _globals['_PROFILETYPE']._serialized_start = 1756
    _globals['_PROFILETYPE']._serialized_end = 1888
    _globals['_CREATEPROFILEREQUEST']._serialized_start = 300
    _globals['_CREATEPROFILEREQUEST']._serialized_end = 523
    _globals['_CREATEOFFLINEPROFILEREQUEST']._serialized_start = 526
    _globals['_CREATEOFFLINEPROFILEREQUEST']._serialized_end = 681
    _globals['_UPDATEPROFILEREQUEST']._serialized_start = 684
    _globals['_UPDATEPROFILEREQUEST']._serialized_end = 815
    _globals['_PROFILE']._serialized_start = 818
    _globals['_PROFILE']._serialized_end = 1312
    _globals['_PROFILE_LABELSENTRY']._serialized_start = 1185
    _globals['_PROFILE_LABELSENTRY']._serialized_end = 1230
    _globals['_DEPLOYMENT']._serialized_start = 1315
    _globals['_DEPLOYMENT']._serialized_end = 1484
    _globals['_DEPLOYMENT_LABELSENTRY']._serialized_start = 1185
    _globals['_DEPLOYMENT_LABELSENTRY']._serialized_end = 1230
    _globals['_LISTPROFILESREQUEST']._serialized_start = 1487
    _globals['_LISTPROFILESREQUEST']._serialized_end = 1616
    _globals['_LISTPROFILESRESPONSE']._serialized_start = 1619
    _globals['_LISTPROFILESRESPONSE']._serialized_end = 1753
    _globals['_PROFILERSERVICE']._serialized_start = 1891
    _globals['_PROFILERSERVICE']._serialized_end = 2657
    _globals['_EXPORTSERVICE']._serialized_start = 2660
    _globals['_EXPORTSERVICE']._serialized_end = 3030