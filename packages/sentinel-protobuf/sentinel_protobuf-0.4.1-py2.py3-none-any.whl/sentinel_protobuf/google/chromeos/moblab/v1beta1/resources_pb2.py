"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chromeos/moblab/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/chromeos/moblab/v1beta1/resources.proto\x12\x1egoogle.chromeos.moblab.v1beta1\x1a\x19google/api/resource.proto"h\n\x0bBuildTarget\x12\x0c\n\x04name\x18\x01 \x01(\t:K\xeaAH\n)chromeosmoblab.googleapis.com/BuildTarget\x12\x1bbuildTargets/{build_target}"k\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t:T\xeaAQ\n#chromeosmoblab.googleapis.com/Model\x12*buildTargets/{build_target}/models/{model}"_\n\tMilestone\x12\x0c\n\x04name\x18\x01 \x01(\t:D\xeaAA\n\'chromeosmoblab.googleapis.com/Milestone\x12\x16milestones/{milestone}"\xb0\x04\n\x05Build\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\tmilestone\x18\x02 \x01(\tB,\xfaA)\n\'chromeosmoblab.googleapis.com/Milestone\x12\x15\n\rbuild_version\x18\x03 \x01(\t\x12A\n\x06status\x18\x04 \x01(\x0e21.google.chromeos.moblab.v1beta1.Build.BuildStatus\x12=\n\x04type\x18\x05 \x01(\x0e2/.google.chromeos.moblab.v1beta1.Build.BuildType\x12\x0e\n\x06branch\x18\x06 \x01(\t\x12\x1b\n\x13rw_firmware_version\x18\x07 \x01(\t\x12\x0e\n\x06labels\x18\x08 \x03(\t"Y\n\x0bBuildStatus\x12\x1c\n\x18BUILD_STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04PASS\x10\x01\x12\x08\n\x04FAIL\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0b\n\x07ABORTED\x10\x04"B\n\tBuildType\x12\x1a\n\x16BUILD_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RELEASE\x10\x01\x12\x0c\n\x08FIRMWARE\x10\x02:c\xeaA`\n#chromeosmoblab.googleapis.com/Build\x129buildTargets/{build_target}/models/{model}/builds/{build}"\x8d\x02\n\rBuildArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x127\n\x05build\x18\x02 \x01(\tB(\xfaA%\n#chromeosmoblab.googleapis.com/Build\x12\x0e\n\x06bucket\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x14\n\x0cobject_count\x18\x05 \x01(\r:\x80\x01\xeaA}\n+chromeosmoblab.googleapis.com/BuildArtifact\x12NbuildTargets/{build_target}/models/{model}/builds/{build}/artifacts/{artifact}B~\n"com.google.chromeos.moblab.v1beta1B\x0eResourcesProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblabb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chromeos.moblab.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.chromeos.moblab.v1beta1B\x0eResourcesProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblab'
    _globals['_BUILDTARGET']._loaded_options = None
    _globals['_BUILDTARGET']._serialized_options = b'\xeaAH\n)chromeosmoblab.googleapis.com/BuildTarget\x12\x1bbuildTargets/{build_target}'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAQ\n#chromeosmoblab.googleapis.com/Model\x12*buildTargets/{build_target}/models/{model}'
    _globals['_MILESTONE']._loaded_options = None
    _globals['_MILESTONE']._serialized_options = b"\xeaAA\n'chromeosmoblab.googleapis.com/Milestone\x12\x16milestones/{milestone}"
    _globals['_BUILD'].fields_by_name['milestone']._loaded_options = None
    _globals['_BUILD'].fields_by_name['milestone']._serialized_options = b"\xfaA)\n'chromeosmoblab.googleapis.com/Milestone"
    _globals['_BUILD']._loaded_options = None
    _globals['_BUILD']._serialized_options = b'\xeaA`\n#chromeosmoblab.googleapis.com/Build\x129buildTargets/{build_target}/models/{model}/builds/{build}'
    _globals['_BUILDARTIFACT'].fields_by_name['build']._loaded_options = None
    _globals['_BUILDARTIFACT'].fields_by_name['build']._serialized_options = b'\xfaA%\n#chromeosmoblab.googleapis.com/Build'
    _globals['_BUILDARTIFACT']._loaded_options = None
    _globals['_BUILDARTIFACT']._serialized_options = b'\xeaA}\n+chromeosmoblab.googleapis.com/BuildArtifact\x12NbuildTargets/{build_target}/models/{model}/builds/{build}/artifacts/{artifact}'
    _globals['_BUILDTARGET']._serialized_start = 109
    _globals['_BUILDTARGET']._serialized_end = 213
    _globals['_MODEL']._serialized_start = 215
    _globals['_MODEL']._serialized_end = 322
    _globals['_MILESTONE']._serialized_start = 324
    _globals['_MILESTONE']._serialized_end = 419
    _globals['_BUILD']._serialized_start = 422
    _globals['_BUILD']._serialized_end = 982
    _globals['_BUILD_BUILDSTATUS']._serialized_start = 724
    _globals['_BUILD_BUILDSTATUS']._serialized_end = 813
    _globals['_BUILD_BUILDTYPE']._serialized_start = 815
    _globals['_BUILD_BUILDTYPE']._serialized_end = 881
    _globals['_BUILDARTIFACT']._serialized_start = 985
    _globals['_BUILDARTIFACT']._serialized_end = 1254