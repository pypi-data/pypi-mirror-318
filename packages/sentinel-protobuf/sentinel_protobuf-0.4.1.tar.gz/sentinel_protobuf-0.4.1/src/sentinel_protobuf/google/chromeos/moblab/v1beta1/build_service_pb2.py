"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chromeos/moblab/v1beta1/build_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.chromeos.moblab.v1beta1 import resources_pb2 as google_dot_chromeos_dot_moblab_dot_v1beta1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/chromeos/moblab/v1beta1/build_service.proto\x12\x1egoogle.chromeos.moblab.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/chromeos/moblab/v1beta1/resources.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"e\n\x1aFindMostStableBuildRequest\x12G\n\x0cbuild_target\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)chromeosmoblab.googleapis.com/BuildTarget"S\n\x1bFindMostStableBuildResponse\x124\n\x05build\x18\x01 \x01(\x0b2%.google.chromeos.moblab.v1beta1.Build"J\n\x17ListBuildTargetsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01"\x8b\x01\n\x18ListBuildTargetsResponse\x12B\n\rbuild_targets\x18\x01 \x03(\x0b2+.google.chromeos.moblab.v1beta1.BuildTarget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x87\x01\n\x11ListModelsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)chromeosmoblab.googleapis.com/BuildTarget\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"x\n\x12ListModelsResponse\x125\n\x06models\x18\x01 \x03(\x0b2%.google.chromeos.moblab.v1beta1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xfd\x01\n\x11ListBuildsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#chromeosmoblab.googleapis.com/Model\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x121\n\x08group_by\x18\x06 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"x\n\x12ListBuildsResponse\x125\n\x06builds\x18\x01 \x03(\x0b2%.google.chromeos.moblab.v1beta1.Build\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"v\n\x1cCheckBuildStageStatusRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+chromeosmoblab.googleapis.com/BuildArtifact\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01"\xd4\x01\n\x1dCheckBuildStageStatusResponse\x12\x17\n\x0fis_build_staged\x18\x01 \x01(\x08\x12L\n\x15staged_build_artifact\x18\x02 \x01(\x0b2-.google.chromeos.moblab.v1beta1.BuildArtifact\x12L\n\x15source_build_artifact\x18\x03 \x01(\x0b2-.google.chromeos.moblab.v1beta1.BuildArtifact"k\n\x11StageBuildRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+chromeosmoblab.googleapis.com/BuildArtifact\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01"b\n\x12StageBuildResponse\x12L\n\x15staged_build_artifact\x18\x01 \x01(\x0b2-.google.chromeos.moblab.v1beta1.BuildArtifact"\x8c\x01\n\x12StageBuildMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x02\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\x9c\n\n\x0cBuildService\x12\xa4\x01\n\x10ListBuildTargets\x127.google.chromeos.moblab.v1beta1.ListBuildTargetsRequest\x1a8.google.chromeos.moblab.v1beta1.ListBuildTargetsResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/buildTargets\x12\xad\x01\n\nListModels\x121.google.chromeos.moblab.v1beta1.ListModelsRequest\x1a2.google.chromeos.moblab.v1beta1.ListModelsResponse"8\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12\'/v1beta1/{parent=buildTargets/*}/models\x12\xb6\x01\n\nListBuilds\x121.google.chromeos.moblab.v1beta1.ListBuildsRequest\x1a2.google.chromeos.moblab.v1beta1.ListBuildsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=buildTargets/*/models/*}/builds\x12\xe7\x01\n\x15CheckBuildStageStatus\x12<.google.chromeos.moblab.v1beta1.CheckBuildStageStatusRequest\x1a=.google.chromeos.moblab.v1beta1.CheckBuildStageStatusResponse"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{name=buildTargets/*/models/*/builds/*/artifacts/*}:check\x12\xdf\x01\n\nStageBuild\x121.google.chromeos.moblab.v1beta1.StageBuildRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA(\n\x12StageBuildResponse\x12\x12StageBuildMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=buildTargets/*/models/*/builds/*/artifacts/*}:stage:\x01*\x12\xe1\x01\n\x13FindMostStableBuild\x12:.google.chromeos.moblab.v1beta1.FindMostStableBuildRequest\x1a;.google.chromeos.moblab.v1beta1.FindMostStableBuildResponse"Q\xdaA\x0cbuild_target\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{build_target=buildTargets/*}:findMostStableBuild\x1aL\xcaA\x1dchromeosmoblab.googleapis.com\xd2A)https://www.googleapis.com/auth/moblabapiB\x81\x01\n"com.google.chromeos.moblab.v1beta1B\x11BuildServiceProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblabb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chromeos.moblab.v1beta1.build_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.chromeos.moblab.v1beta1B\x11BuildServiceProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblab'
    _globals['_FINDMOSTSTABLEBUILDREQUEST'].fields_by_name['build_target']._loaded_options = None
    _globals['_FINDMOSTSTABLEBUILDREQUEST'].fields_by_name['build_target']._serialized_options = b'\xe0A\x02\xfaA+\n)chromeosmoblab.googleapis.com/BuildTarget'
    _globals['_LISTBUILDTARGETSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBUILDTARGETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDTARGETSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBUILDTARGETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)chromeosmoblab.googleapis.com/BuildTarget'
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#chromeosmoblab.googleapis.com/Model'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUILDSREQUEST'].fields_by_name['group_by']._loaded_options = None
    _globals['_LISTBUILDSREQUEST'].fields_by_name['group_by']._serialized_options = b'\xe0A\x01'
    _globals['_CHECKBUILDSTAGESTATUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CHECKBUILDSTAGESTATUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+chromeosmoblab.googleapis.com/BuildArtifact'
    _globals['_CHECKBUILDSTAGESTATUSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_CHECKBUILDSTAGESTATUSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_STAGEBUILDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STAGEBUILDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+chromeosmoblab.googleapis.com/BuildArtifact'
    _globals['_STAGEBUILDREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_STAGEBUILDREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDSERVICE']._loaded_options = None
    _globals['_BUILDSERVICE']._serialized_options = b'\xcaA\x1dchromeosmoblab.googleapis.com\xd2A)https://www.googleapis.com/auth/moblabapi'
    _globals['_BUILDSERVICE'].methods_by_name['ListBuildTargets']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['ListBuildTargets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/buildTargets'
    _globals['_BUILDSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['ListModels']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12'/v1beta1/{parent=buildTargets/*}/models"
    _globals['_BUILDSERVICE'].methods_by_name['ListBuilds']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['ListBuilds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=buildTargets/*/models/*}/builds'
    _globals['_BUILDSERVICE'].methods_by_name['CheckBuildStageStatus']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['CheckBuildStageStatus']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{name=buildTargets/*/models/*/builds/*/artifacts/*}:check'
    _globals['_BUILDSERVICE'].methods_by_name['StageBuild']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['StageBuild']._serialized_options = b'\xcaA(\n\x12StageBuildResponse\x12\x12StageBuildMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=buildTargets/*/models/*/builds/*/artifacts/*}:stage:\x01*'
    _globals['_BUILDSERVICE'].methods_by_name['FindMostStableBuild']._loaded_options = None
    _globals['_BUILDSERVICE'].methods_by_name['FindMostStableBuild']._serialized_options = b'\xdaA\x0cbuild_target\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{build_target=buildTargets/*}:findMostStableBuild'
    _globals['_FINDMOSTSTABLEBUILDREQUEST']._serialized_start = 353
    _globals['_FINDMOSTSTABLEBUILDREQUEST']._serialized_end = 454
    _globals['_FINDMOSTSTABLEBUILDRESPONSE']._serialized_start = 456
    _globals['_FINDMOSTSTABLEBUILDRESPONSE']._serialized_end = 539
    _globals['_LISTBUILDTARGETSREQUEST']._serialized_start = 541
    _globals['_LISTBUILDTARGETSREQUEST']._serialized_end = 615
    _globals['_LISTBUILDTARGETSRESPONSE']._serialized_start = 618
    _globals['_LISTBUILDTARGETSRESPONSE']._serialized_end = 757
    _globals['_LISTMODELSREQUEST']._serialized_start = 760
    _globals['_LISTMODELSREQUEST']._serialized_end = 895
    _globals['_LISTMODELSRESPONSE']._serialized_start = 897
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1017
    _globals['_LISTBUILDSREQUEST']._serialized_start = 1020
    _globals['_LISTBUILDSREQUEST']._serialized_end = 1273
    _globals['_LISTBUILDSRESPONSE']._serialized_start = 1275
    _globals['_LISTBUILDSRESPONSE']._serialized_end = 1395
    _globals['_CHECKBUILDSTAGESTATUSREQUEST']._serialized_start = 1397
    _globals['_CHECKBUILDSTAGESTATUSREQUEST']._serialized_end = 1515
    _globals['_CHECKBUILDSTAGESTATUSRESPONSE']._serialized_start = 1518
    _globals['_CHECKBUILDSTAGESTATUSRESPONSE']._serialized_end = 1730
    _globals['_STAGEBUILDREQUEST']._serialized_start = 1732
    _globals['_STAGEBUILDREQUEST']._serialized_end = 1839
    _globals['_STAGEBUILDRESPONSE']._serialized_start = 1841
    _globals['_STAGEBUILDRESPONSE']._serialized_end = 1939
    _globals['_STAGEBUILDMETADATA']._serialized_start = 1942
    _globals['_STAGEBUILDMETADATA']._serialized_end = 2082
    _globals['_BUILDSERVICE']._serialized_start = 2085
    _globals['_BUILDSERVICE']._serialized_end = 3393