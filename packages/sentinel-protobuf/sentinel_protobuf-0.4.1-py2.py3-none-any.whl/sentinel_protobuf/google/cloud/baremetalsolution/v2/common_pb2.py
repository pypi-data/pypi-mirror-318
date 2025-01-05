"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/baremetalsolution/v2/common.proto\x12!google.cloud.baremetalsolution.v2*\xaa\x01\n\x15VolumePerformanceTier\x12\'\n#VOLUME_PERFORMANCE_TIER_UNSPECIFIED\x10\x00\x12"\n\x1eVOLUME_PERFORMANCE_TIER_SHARED\x10\x01\x12$\n VOLUME_PERFORMANCE_TIER_ASSIGNED\x10\x02\x12\x1e\n\x1aVOLUME_PERFORMANCE_TIER_HT\x10\x03*l\n\x0fWorkloadProfile\x12 \n\x1cWORKLOAD_PROFILE_UNSPECIFIED\x10\x00\x12\x1c\n\x18WORKLOAD_PROFILE_GENERIC\x10\x01\x12\x19\n\x15WORKLOAD_PROFILE_HANA\x10\x02B\xfa\x01\n%com.google.cloud.baremetalsolution.v2B\x0bCommonProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x0bCommonProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_VOLUMEPERFORMANCETIER']._serialized_start = 86
    _globals['_VOLUMEPERFORMANCETIER']._serialized_end = 256
    _globals['_WORKLOADPROFILE']._serialized_start = 258
    _globals['_WORKLOADPROFILE']._serialized_end = 366