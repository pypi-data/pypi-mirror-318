"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/experiment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dialogflow/cx/v3/experiment.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfb\x10\n\nExperiment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12>\n\x05state\x18\x04 \x01(\x0e2/.google.cloud.dialogflow.cx.v3.Experiment.State\x12H\n\ndefinition\x18\x05 \x01(\x0b24.google.cloud.dialogflow.cx.v3.Experiment.Definition\x12D\n\x0erollout_config\x18\x0e \x01(\x0b2,.google.cloud.dialogflow.cx.v3.RolloutConfig\x12B\n\rrollout_state\x18\x0f \x01(\x0b2+.google.cloud.dialogflow.cx.v3.RolloutState\x12\x1e\n\x16rollout_failure_reason\x18\x10 \x01(\t\x12@\n\x06result\x18\x06 \x01(\x0b20.google.cloud.dialogflow.cx.v3.Experiment.Result\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x11experiment_length\x18\x0b \x01(\x0b2\x19.google.protobuf.Duration\x12H\n\x10variants_history\x18\x0c \x03(\x0b2..google.cloud.dialogflow.cx.v3.VariantsHistory\x1aw\n\nDefinition\x12\x11\n\tcondition\x18\x01 \x01(\t\x12J\n\x10version_variants\x18\x02 \x01(\x0b2..google.cloud.dialogflow.cx.v3.VersionVariantsH\x00B\n\n\x08variants\x1a\x8b\x08\n\x06Result\x12X\n\x0fversion_metrics\x18\x01 \x03(\x0b2?.google.cloud.dialogflow.cx.v3.Experiment.Result.VersionMetrics\x124\n\x10last_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1ag\n\x12ConfidenceInterval\x12\x18\n\x10confidence_level\x18\x01 \x01(\x01\x12\r\n\x05ratio\x18\x02 \x01(\x01\x12\x13\n\x0blower_bound\x18\x03 \x01(\x01\x12\x13\n\x0bupper_bound\x18\x04 \x01(\x01\x1a\xb0\x02\n\x06Metric\x12I\n\x04type\x18\x01 \x01(\x0e2;.google.cloud.dialogflow.cx.v3.Experiment.Result.MetricType\x12N\n\ncount_type\x18\x05 \x01(\x0e2:.google.cloud.dialogflow.cx.v3.Experiment.Result.CountType\x12\x0f\n\x05ratio\x18\x02 \x01(\x01H\x00\x12\x0f\n\x05count\x18\x04 \x01(\x01H\x00\x12`\n\x13confidence_interval\x18\x03 \x01(\x0b2C.google.cloud.dialogflow.cx.v3.Experiment.Result.ConfidenceIntervalB\x07\n\x05value\x1a\xaa\x01\n\x0eVersionMetrics\x127\n\x07version\x18\x01 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Version\x12H\n\x07metrics\x18\x02 \x03(\x0b27.google.cloud.dialogflow.cx.v3.Experiment.Result.Metric\x12\x15\n\rsession_count\x18\x03 \x01(\x05"\xb6\x01\n\nMetricType\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12&\n"CONTAINED_SESSION_NO_CALLBACK_RATE\x10\x01\x12\x1b\n\x17LIVE_AGENT_HANDOFF_RATE\x10\x02\x12\x19\n\x15CALLBACK_SESSION_RATE\x10\x03\x12\x1a\n\x16ABANDONED_SESSION_RATE\x10\x04\x12\x14\n\x10SESSION_END_RATE\x10\x05"o\n\tCountType\x12\x1a\n\x16COUNT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14TOTAL_NO_MATCH_COUNT\x10\x01\x12\x14\n\x10TOTAL_TURN_COUNT\x10\x02\x12\x16\n\x12AVERAGE_TURN_COUNT\x10\x03"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05DRAFT\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03\x12\x12\n\x0eROLLOUT_FAILED\x10\x04:\x96\x01\xeaA\x92\x01\n$dialogflow.googleapis.com/Experiment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/experiments/{experiment}"\xad\x01\n\x0fVersionVariants\x12H\n\x08variants\x18\x01 \x03(\x0b26.google.cloud.dialogflow.cx.v3.VersionVariants.Variant\x1aP\n\x07Variant\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1a\n\x12traffic_allocation\x18\x02 \x01(\x02\x12\x18\n\x10is_control_group\x18\x03 \x01(\x08"\x9a\x01\n\x0fVariantsHistory\x12J\n\x10version_variants\x18\x01 \x01(\x0b2..google.cloud.dialogflow.cx.v3.VersionVariantsH\x00\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\n\n\x08variants"\x85\x02\n\rRolloutConfig\x12O\n\rrollout_steps\x18\x01 \x03(\x0b28.google.cloud.dialogflow.cx.v3.RolloutConfig.RolloutStep\x12\x19\n\x11rollout_condition\x18\x02 \x01(\t\x12\x19\n\x11failure_condition\x18\x03 \x01(\t\x1am\n\x0bRolloutStep\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0ftraffic_percent\x18\x02 \x01(\x05\x12/\n\x0cmin_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"`\n\x0cRolloutState\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x12\n\nstep_index\x18\x03 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"}\n\x16ListExperimentsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x17ListExperimentsResponse\x12>\n\x0bexperiments\x18\x01 \x03(\x0b2).google.cloud.dialogflow.cx.v3.Experiment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x14GetExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"\x9b\x01\n\x17CreateExperimentRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment\x12B\n\nexperiment\x18\x02 \x01(\x0b2).google.cloud.dialogflow.cx.v3.ExperimentB\x03\xe0A\x02"\x93\x01\n\x17UpdateExperimentRequest\x12B\n\nexperiment\x18\x01 \x01(\x0b2).google.cloud.dialogflow.cx.v3.ExperimentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x17DeleteExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"T\n\x16StartExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"S\n\x15StopExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment2\xf8\x0c\n\x0bExperiments\x12\xda\x01\n\x0fListExperiments\x125.google.cloud.dialogflow.cx.v3.ListExperimentsRequest\x1a6.google.cloud.dialogflow.cx.v3.ListExperimentsResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments\x12\xc7\x01\n\rGetExperiment\x123.google.cloud.dialogflow.cx.v3.GetExperimentRequest\x1a).google.cloud.dialogflow.cx.v3.Experiment"V\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}\x12\xe6\x01\n\x10CreateExperiment\x126.google.cloud.dialogflow.cx.v3.CreateExperimentRequest\x1a).google.cloud.dialogflow.cx.v3.Experiment"o\xdaA\x11parent,experiment\x82\xd3\xe4\x93\x02U"G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments:\nexperiment\x12\xf6\x01\n\x10UpdateExperiment\x126.google.cloud.dialogflow.cx.v3.UpdateExperimentRequest\x1a).google.cloud.dialogflow.cx.v3.Experiment"\x7f\xdaA\x16experiment,update_mask\x82\xd3\xe4\x93\x02`2R/v3/{experiment.name=projects/*/locations/*/agents/*/environments/*/experiments/*}:\nexperiment\x12\xba\x01\n\x10DeleteExperiment\x126.google.cloud.dialogflow.cx.v3.DeleteExperimentRequest\x1a\x16.google.protobuf.Empty"V\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}\x12\xd4\x01\n\x0fStartExperiment\x125.google.cloud.dialogflow.cx.v3.StartExperimentRequest\x1a).google.cloud.dialogflow.cx.v3.Experiment"_\xdaA\x04name\x82\xd3\xe4\x93\x02R"M/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:start:\x01*\x12\xd1\x01\n\x0eStopExperiment\x124.google.cloud.dialogflow.cx.v3.StopExperimentRequest\x1a).google.cloud.dialogflow.cx.v3.Experiment"^\xdaA\x04name\x82\xd3\xe4\x93\x02Q"L/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:stop:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xb2\x01\n!com.google.cloud.dialogflow.cx.v3B\x0fExperimentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.experiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x0fExperimentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS'].fields_by_name['version']._loaded_options = None
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS'].fields_by_name['version']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_EXPERIMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENT']._loaded_options = None
    _globals['_EXPERIMENT']._serialized_options = b'\xeaA\x92\x01\n$dialogflow.googleapis.com/Experiment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/experiments/{experiment}'
    _globals['_LISTEXPERIMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXPERIMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment'
    _globals['_GETEXPERIMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEXPERIMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment'
    _globals['_CREATEEXPERIMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEXPERIMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment'
    _globals['_CREATEEXPERIMENTREQUEST'].fields_by_name['experiment']._loaded_options = None
    _globals['_CREATEEXPERIMENTREQUEST'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXPERIMENTREQUEST'].fields_by_name['experiment']._loaded_options = None
    _globals['_UPDATEEXPERIMENTREQUEST'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXPERIMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEXPERIMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEEXPERIMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEXPERIMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment'
    _globals['_STARTEXPERIMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTEXPERIMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment'
    _globals['_STOPEXPERIMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPEXPERIMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment'
    _globals['_EXPERIMENTS']._loaded_options = None
    _globals['_EXPERIMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_EXPERIMENTS'].methods_by_name['ListExperiments']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['ListExperiments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments'
    _globals['_EXPERIMENTS'].methods_by_name['GetExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['GetExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}'
    _globals['_EXPERIMENTS'].methods_by_name['CreateExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['CreateExperiment']._serialized_options = b'\xdaA\x11parent,experiment\x82\xd3\xe4\x93\x02U"G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/experiments:\nexperiment'
    _globals['_EXPERIMENTS'].methods_by_name['UpdateExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['UpdateExperiment']._serialized_options = b'\xdaA\x16experiment,update_mask\x82\xd3\xe4\x93\x02`2R/v3/{experiment.name=projects/*/locations/*/agents/*/environments/*/experiments/*}:\nexperiment'
    _globals['_EXPERIMENTS'].methods_by_name['DeleteExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['DeleteExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}'
    _globals['_EXPERIMENTS'].methods_by_name['StartExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['StartExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02R"M/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:start:\x01*'
    _globals['_EXPERIMENTS'].methods_by_name['StopExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['StopExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Q"L/v3/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:stop:\x01*'
    _globals['_EXPERIMENT']._serialized_start = 325
    _globals['_EXPERIMENT']._serialized_end = 2496
    _globals['_EXPERIMENT_DEFINITION']._serialized_start = 1100
    _globals['_EXPERIMENT_DEFINITION']._serialized_end = 1219
    _globals['_EXPERIMENT_RESULT']._serialized_start = 1222
    _globals['_EXPERIMENT_RESULT']._serialized_end = 2257
    _globals['_EXPERIMENT_RESULT_CONFIDENCEINTERVAL']._serialized_start = 1376
    _globals['_EXPERIMENT_RESULT_CONFIDENCEINTERVAL']._serialized_end = 1479
    _globals['_EXPERIMENT_RESULT_METRIC']._serialized_start = 1482
    _globals['_EXPERIMENT_RESULT_METRIC']._serialized_end = 1786
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS']._serialized_start = 1789
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS']._serialized_end = 1959
    _globals['_EXPERIMENT_RESULT_METRICTYPE']._serialized_start = 1962
    _globals['_EXPERIMENT_RESULT_METRICTYPE']._serialized_end = 2144
    _globals['_EXPERIMENT_RESULT_COUNTTYPE']._serialized_start = 2146
    _globals['_EXPERIMENT_RESULT_COUNTTYPE']._serialized_end = 2257
    _globals['_EXPERIMENT_STATE']._serialized_start = 2259
    _globals['_EXPERIMENT_STATE']._serialized_end = 2343
    _globals['_VERSIONVARIANTS']._serialized_start = 2499
    _globals['_VERSIONVARIANTS']._serialized_end = 2672
    _globals['_VERSIONVARIANTS_VARIANT']._serialized_start = 2592
    _globals['_VERSIONVARIANTS_VARIANT']._serialized_end = 2672
    _globals['_VARIANTSHISTORY']._serialized_start = 2675
    _globals['_VARIANTSHISTORY']._serialized_end = 2829
    _globals['_ROLLOUTCONFIG']._serialized_start = 2832
    _globals['_ROLLOUTCONFIG']._serialized_end = 3093
    _globals['_ROLLOUTCONFIG_ROLLOUTSTEP']._serialized_start = 2984
    _globals['_ROLLOUTCONFIG_ROLLOUTSTEP']._serialized_end = 3093
    _globals['_ROLLOUTSTATE']._serialized_start = 3095
    _globals['_ROLLOUTSTATE']._serialized_end = 3191
    _globals['_LISTEXPERIMENTSREQUEST']._serialized_start = 3193
    _globals['_LISTEXPERIMENTSREQUEST']._serialized_end = 3318
    _globals['_LISTEXPERIMENTSRESPONSE']._serialized_start = 3320
    _globals['_LISTEXPERIMENTSRESPONSE']._serialized_end = 3434
    _globals['_GETEXPERIMENTREQUEST']._serialized_start = 3436
    _globals['_GETEXPERIMENTREQUEST']._serialized_end = 3518
    _globals['_CREATEEXPERIMENTREQUEST']._serialized_start = 3521
    _globals['_CREATEEXPERIMENTREQUEST']._serialized_end = 3676
    _globals['_UPDATEEXPERIMENTREQUEST']._serialized_start = 3679
    _globals['_UPDATEEXPERIMENTREQUEST']._serialized_end = 3826
    _globals['_DELETEEXPERIMENTREQUEST']._serialized_start = 3828
    _globals['_DELETEEXPERIMENTREQUEST']._serialized_end = 3913
    _globals['_STARTEXPERIMENTREQUEST']._serialized_start = 3915
    _globals['_STARTEXPERIMENTREQUEST']._serialized_end = 3999
    _globals['_STOPEXPERIMENTREQUEST']._serialized_start = 4001
    _globals['_STOPEXPERIMENTREQUEST']._serialized_end = 4084
    _globals['_EXPERIMENTS']._serialized_start = 4087
    _globals['_EXPERIMENTS']._serialized_end = 5743