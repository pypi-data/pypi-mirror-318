"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/policysimulator/v1/simulator.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.policysimulator.v1 import explanations_pb2 as google_dot_cloud_dot_policysimulator_dot_v1_dot_explanations__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/policysimulator/v1/simulator.proto\x12\x1fgoogle.cloud.policysimulator.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/policysimulator/v1/explanations.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"\xef\x05\n\x06Replay\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12A\n\x05state\x18\x02 \x01(\x0e2-.google.cloud.policysimulator.v1.Replay.StateB\x03\xe0A\x03\x12B\n\x06config\x18\x03 \x01(\x0b2-.google.cloud.policysimulator.v1.ReplayConfigB\x03\xe0A\x02\x12T\n\x0fresults_summary\x18\x05 \x01(\x0b26.google.cloud.policysimulator.v1.Replay.ResultsSummaryB\x03\xe0A\x03\x1a\xbb\x01\n\x0eResultsSummary\x12\x11\n\tlog_count\x18\x01 \x01(\x05\x12\x17\n\x0funchanged_count\x18\x02 \x01(\x05\x12\x18\n\x10difference_count\x18\x03 \x01(\x05\x12\x13\n\x0berror_count\x18\x04 \x01(\x05\x12&\n\x0boldest_date\x18\x05 \x01(\x0b2\x11.google.type.Date\x12&\n\x0bnewest_date\x18\x06 \x01(\x0b2\x11.google.type.Date"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04:\xe1\x01\xeaA\xdd\x01\n%policysimulator.googleapis.com/Replay\x128projects/{project}/locations/{location}/replays/{replay}\x126folders/{folder}/locations/{location}/replays/{replay}\x12Borganizations/{organization}/locations/{location}/replays/{replay}"\xe5\x04\n\x0cReplayResult\x12;\n\x04diff\x18\x05 \x01(\x0b2+.google.cloud.policysimulator.v1.ReplayDiffH\x00\x12#\n\x05error\x18\x06 \x01(\x0b2\x12.google.rpc.StatusH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x06parent\x18\x02 \x01(\tB*\xfaA\'\n%policysimulator.googleapis.com/Replay\x12B\n\x0caccess_tuple\x18\x03 \x01(\x0b2,.google.cloud.policysimulator.v1.AccessTuple\x12)\n\x0elast_seen_date\x18\x04 \x01(\x0b2\x11.google.type.Date:\xaf\x02\xeaA\xab\x02\n+policysimulator.googleapis.com/ReplayResult\x12Pprojects/{project}/locations/{location}/replays/{replay}/results/{replay_result}\x12Nfolders/{folder}/locations/{location}/replays/{replay}/results/{replay_result}\x12Zorganizations/{organization}/locations/{location}/replays/{replay}/results/{replay_result}B\x08\n\x06result"h\n\x13CreateReplayRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12<\n\x06replay\x18\x02 \x01(\x0b2\'.google.cloud.policysimulator.v1.ReplayB\x03\xe0A\x02"I\n\x17ReplayOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp"O\n\x10GetReplayRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%policysimulator.googleapis.com/Replay"\x80\x01\n\x18ListReplayResultsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%policysimulator.googleapis.com/Replay\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"{\n\x19ListReplayResultsResponse\x12E\n\x0ereplay_results\x18\x01 \x03(\x0b2-.google.cloud.policysimulator.v1.ReplayResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc0\x02\n\x0cReplayConfig\x12X\n\x0epolicy_overlay\x18\x01 \x03(\x0b2@.google.cloud.policysimulator.v1.ReplayConfig.PolicyOverlayEntry\x12K\n\nlog_source\x18\x02 \x01(\x0e27.google.cloud.policysimulator.v1.ReplayConfig.LogSource\x1aK\n\x12PolicyOverlayEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b2\x15.google.iam.v1.Policy:\x028\x01"<\n\tLogSource\x12\x1a\n\x16LOG_SOURCE_UNSPECIFIED\x10\x00\x12\x13\n\x0fRECENT_ACCESSES\x10\x01"S\n\nReplayDiff\x12E\n\x0baccess_diff\x18\x02 \x01(\x0b20.google.cloud.policysimulator.v1.AccessStateDiff"\xaa\x03\n\x0fAccessStateDiff\x12B\n\x08baseline\x18\x01 \x01(\x0b20.google.cloud.policysimulator.v1.ExplainedAccess\x12C\n\tsimulated\x18\x02 \x01(\x0b20.google.cloud.policysimulator.v1.ExplainedAccess\x12X\n\raccess_change\x18\x03 \x01(\x0e2A.google.cloud.policysimulator.v1.AccessStateDiff.AccessChangeType"\xb3\x01\n\x10AccessChangeType\x12"\n\x1eACCESS_CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tNO_CHANGE\x10\x01\x12\x12\n\x0eUNKNOWN_CHANGE\x10\x02\x12\x12\n\x0eACCESS_REVOKED\x10\x03\x12\x11\n\rACCESS_GAINED\x10\x04\x12\x18\n\x14ACCESS_MAYBE_REVOKED\x10\x05\x12\x17\n\x13ACCESS_MAYBE_GAINED\x10\x06"\xbd\x01\n\x0fExplainedAccess\x12B\n\x0caccess_state\x18\x01 \x01(\x0e2,.google.cloud.policysimulator.v1.AccessState\x12B\n\x08policies\x18\x02 \x03(\x0b20.google.cloud.policysimulator.v1.ExplainedPolicy\x12"\n\x06errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status2\x81\x08\n\tSimulator\x12\x87\x02\n\tGetReplay\x121.google.cloud.policysimulator.v1.GetReplayRequest\x1a\'.google.cloud.policysimulator.v1.Replay"\x9d\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8f\x01\x12+/v1/{name=projects/*/locations/*/replays/*}Z,\x12*/v1/{name=folders/*/locations/*/replays/*}Z2\x120/v1/{name=organizations/*/locations/*/replays/*}\x12\xc8\x02\n\x0cCreateReplay\x124.google.cloud.policysimulator.v1.CreateReplayRequest\x1a\x1d.google.longrunning.Operation"\xe2\x01\xcaA!\n\x06Replay\x12\x17ReplayOperationMetadata\xdaA\rparent,replay\x82\xd3\xe4\x93\x02\xa7\x01"+/v1/{parent=projects/*/locations/*}/replays:\x06replayZ4"*/v1/{parent=folders/*/locations/*}/replays:\x06replayZ:"0/v1/{parent=organizations/*/locations/*}/replays:\x06replay\x12\xca\x02\n\x11ListReplayResults\x129.google.cloud.policysimulator.v1.ListReplayResultsRequest\x1a:.google.cloud.policysimulator.v1.ListReplayResultsResponse"\xbd\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xad\x01\x125/v1/{parent=projects/*/locations/*/replays/*}/resultsZ6\x124/v1/{parent=folders/*/locations/*/replays/*}/resultsZ<\x12:/v1/{parent=organizations/*/locations/*/replays/*}/results\x1aR\xcaA\x1epolicysimulator.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf2\x01\n#com.google.cloud.policysimulator.v1B\x0eSimulatorProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policysimulator.v1.simulator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.policysimulator.v1B\x0eSimulatorProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xf8\x01\x01\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1'
    _globals['_REPLAY'].fields_by_name['name']._loaded_options = None
    _globals['_REPLAY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_REPLAY'].fields_by_name['state']._loaded_options = None
    _globals['_REPLAY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_REPLAY'].fields_by_name['config']._loaded_options = None
    _globals['_REPLAY'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_REPLAY'].fields_by_name['results_summary']._loaded_options = None
    _globals['_REPLAY'].fields_by_name['results_summary']._serialized_options = b'\xe0A\x03'
    _globals['_REPLAY']._loaded_options = None
    _globals['_REPLAY']._serialized_options = b'\xeaA\xdd\x01\n%policysimulator.googleapis.com/Replay\x128projects/{project}/locations/{location}/replays/{replay}\x126folders/{folder}/locations/{location}/replays/{replay}\x12Borganizations/{organization}/locations/{location}/replays/{replay}'
    _globals['_REPLAYRESULT'].fields_by_name['parent']._loaded_options = None
    _globals['_REPLAYRESULT'].fields_by_name['parent']._serialized_options = b"\xfaA'\n%policysimulator.googleapis.com/Replay"
    _globals['_REPLAYRESULT']._loaded_options = None
    _globals['_REPLAYRESULT']._serialized_options = b'\xeaA\xab\x02\n+policysimulator.googleapis.com/ReplayResult\x12Pprojects/{project}/locations/{location}/replays/{replay}/results/{replay_result}\x12Nfolders/{folder}/locations/{location}/replays/{replay}/results/{replay_result}\x12Zorganizations/{organization}/locations/{location}/replays/{replay}/results/{replay_result}'
    _globals['_CREATEREPLAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREPLAYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREPLAYREQUEST'].fields_by_name['replay']._loaded_options = None
    _globals['_CREATEREPLAYREQUEST'].fields_by_name['replay']._serialized_options = b'\xe0A\x02'
    _globals['_GETREPLAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPLAYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%policysimulator.googleapis.com/Replay"
    _globals['_LISTREPLAYRESULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPLAYRESULTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%policysimulator.googleapis.com/Replay"
    _globals['_REPLAYCONFIG_POLICYOVERLAYENTRY']._loaded_options = None
    _globals['_REPLAYCONFIG_POLICYOVERLAYENTRY']._serialized_options = b'8\x01'
    _globals['_SIMULATOR']._loaded_options = None
    _globals['_SIMULATOR']._serialized_options = b'\xcaA\x1epolicysimulator.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SIMULATOR'].methods_by_name['GetReplay']._loaded_options = None
    _globals['_SIMULATOR'].methods_by_name['GetReplay']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8f\x01\x12+/v1/{name=projects/*/locations/*/replays/*}Z,\x12*/v1/{name=folders/*/locations/*/replays/*}Z2\x120/v1/{name=organizations/*/locations/*/replays/*}'
    _globals['_SIMULATOR'].methods_by_name['CreateReplay']._loaded_options = None
    _globals['_SIMULATOR'].methods_by_name['CreateReplay']._serialized_options = b'\xcaA!\n\x06Replay\x12\x17ReplayOperationMetadata\xdaA\rparent,replay\x82\xd3\xe4\x93\x02\xa7\x01"+/v1/{parent=projects/*/locations/*}/replays:\x06replayZ4"*/v1/{parent=folders/*/locations/*}/replays:\x06replayZ:"0/v1/{parent=organizations/*/locations/*}/replays:\x06replay'
    _globals['_SIMULATOR'].methods_by_name['ListReplayResults']._loaded_options = None
    _globals['_SIMULATOR'].methods_by_name['ListReplayResults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xad\x01\x125/v1/{parent=projects/*/locations/*/replays/*}/resultsZ6\x124/v1/{parent=folders/*/locations/*/replays/*}/resultsZ<\x12:/v1/{parent=organizations/*/locations/*/replays/*}/results'
    _globals['_REPLAY']._serialized_start = 399
    _globals['_REPLAY']._serialized_end = 1150
    _globals['_REPLAY_RESULTSSUMMARY']._serialized_start = 650
    _globals['_REPLAY_RESULTSSUMMARY']._serialized_end = 837
    _globals['_REPLAY_STATE']._serialized_start = 839
    _globals['_REPLAY_STATE']._serialized_end = 922
    _globals['_REPLAYRESULT']._serialized_start = 1153
    _globals['_REPLAYRESULT']._serialized_end = 1766
    _globals['_CREATEREPLAYREQUEST']._serialized_start = 1768
    _globals['_CREATEREPLAYREQUEST']._serialized_end = 1872
    _globals['_REPLAYOPERATIONMETADATA']._serialized_start = 1874
    _globals['_REPLAYOPERATIONMETADATA']._serialized_end = 1947
    _globals['_GETREPLAYREQUEST']._serialized_start = 1949
    _globals['_GETREPLAYREQUEST']._serialized_end = 2028
    _globals['_LISTREPLAYRESULTSREQUEST']._serialized_start = 2031
    _globals['_LISTREPLAYRESULTSREQUEST']._serialized_end = 2159
    _globals['_LISTREPLAYRESULTSRESPONSE']._serialized_start = 2161
    _globals['_LISTREPLAYRESULTSRESPONSE']._serialized_end = 2284
    _globals['_REPLAYCONFIG']._serialized_start = 2287
    _globals['_REPLAYCONFIG']._serialized_end = 2607
    _globals['_REPLAYCONFIG_POLICYOVERLAYENTRY']._serialized_start = 2470
    _globals['_REPLAYCONFIG_POLICYOVERLAYENTRY']._serialized_end = 2545
    _globals['_REPLAYCONFIG_LOGSOURCE']._serialized_start = 2547
    _globals['_REPLAYCONFIG_LOGSOURCE']._serialized_end = 2607
    _globals['_REPLAYDIFF']._serialized_start = 2609
    _globals['_REPLAYDIFF']._serialized_end = 2692
    _globals['_ACCESSSTATEDIFF']._serialized_start = 2695
    _globals['_ACCESSSTATEDIFF']._serialized_end = 3121
    _globals['_ACCESSSTATEDIFF_ACCESSCHANGETYPE']._serialized_start = 2942
    _globals['_ACCESSSTATEDIFF_ACCESSCHANGETYPE']._serialized_end = 3121
    _globals['_EXPLAINEDACCESS']._serialized_start = 3124
    _globals['_EXPLAINEDACCESS']._serialized_end = 3313
    _globals['_SIMULATOR']._serialized_start = 3316
    _globals['_SIMULATOR']._serialized_end = 4341