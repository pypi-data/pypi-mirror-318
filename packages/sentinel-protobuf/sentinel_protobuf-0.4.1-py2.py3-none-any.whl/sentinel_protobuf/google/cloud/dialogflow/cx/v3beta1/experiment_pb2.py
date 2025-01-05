"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/experiment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dialogflow/cx/v3beta1/experiment.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x11\n\nExperiment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12C\n\x05state\x18\x04 \x01(\x0e24.google.cloud.dialogflow.cx.v3beta1.Experiment.State\x12M\n\ndefinition\x18\x05 \x01(\x0b29.google.cloud.dialogflow.cx.v3beta1.Experiment.Definition\x12I\n\x0erollout_config\x18\x0e \x01(\x0b21.google.cloud.dialogflow.cx.v3beta1.RolloutConfig\x12G\n\rrollout_state\x18\x0f \x01(\x0b20.google.cloud.dialogflow.cx.v3beta1.RolloutState\x12\x1e\n\x16rollout_failure_reason\x18\x10 \x01(\t\x12E\n\x06result\x18\x06 \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.Experiment.Result\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x11experiment_length\x18\x0b \x01(\x0b2\x19.google.protobuf.Duration\x12M\n\x10variants_history\x18\x0c \x03(\x0b23.google.cloud.dialogflow.cx.v3beta1.VariantsHistory\x1a|\n\nDefinition\x12\x11\n\tcondition\x18\x01 \x01(\t\x12O\n\x10version_variants\x18\x02 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.VersionVariantsH\x00B\n\n\x08variants\x1a\xa4\x08\n\x06Result\x12]\n\x0fversion_metrics\x18\x01 \x03(\x0b2D.google.cloud.dialogflow.cx.v3beta1.Experiment.Result.VersionMetrics\x124\n\x10last_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1ag\n\x12ConfidenceInterval\x12\x18\n\x10confidence_level\x18\x01 \x01(\x01\x12\r\n\x05ratio\x18\x02 \x01(\x01\x12\x13\n\x0blower_bound\x18\x03 \x01(\x01\x12\x13\n\x0bupper_bound\x18\x04 \x01(\x01\x1a\xbf\x02\n\x06Metric\x12N\n\x04type\x18\x01 \x01(\x0e2@.google.cloud.dialogflow.cx.v3beta1.Experiment.Result.MetricType\x12S\n\ncount_type\x18\x05 \x01(\x0e2?.google.cloud.dialogflow.cx.v3beta1.Experiment.Result.CountType\x12\x0f\n\x05ratio\x18\x02 \x01(\x01H\x00\x12\x0f\n\x05count\x18\x04 \x01(\x01H\x00\x12e\n\x13confidence_interval\x18\x03 \x01(\x0b2H.google.cloud.dialogflow.cx.v3beta1.Experiment.Result.ConfidenceIntervalB\x07\n\x05value\x1a\xaf\x01\n\x0eVersionMetrics\x127\n\x07version\x18\x01 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Version\x12M\n\x07metrics\x18\x02 \x03(\x0b2<.google.cloud.dialogflow.cx.v3beta1.Experiment.Result.Metric\x12\x15\n\rsession_count\x18\x03 \x01(\x05"\xb6\x01\n\nMetricType\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12&\n"CONTAINED_SESSION_NO_CALLBACK_RATE\x10\x01\x12\x1b\n\x17LIVE_AGENT_HANDOFF_RATE\x10\x02\x12\x19\n\x15CALLBACK_SESSION_RATE\x10\x03\x12\x1a\n\x16ABANDONED_SESSION_RATE\x10\x04\x12\x14\n\x10SESSION_END_RATE\x10\x05"o\n\tCountType\x12\x1a\n\x16COUNT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14TOTAL_NO_MATCH_COUNT\x10\x01\x12\x14\n\x10TOTAL_TURN_COUNT\x10\x02\x12\x16\n\x12AVERAGE_TURN_COUNT\x10\x03"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05DRAFT\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03\x12\x12\n\x0eROLLOUT_FAILED\x10\x04:\x96\x01\xeaA\x92\x01\n$dialogflow.googleapis.com/Experiment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/experiments/{experiment}"\xb2\x01\n\x0fVersionVariants\x12M\n\x08variants\x18\x01 \x03(\x0b2;.google.cloud.dialogflow.cx.v3beta1.VersionVariants.Variant\x1aP\n\x07Variant\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1a\n\x12traffic_allocation\x18\x02 \x01(\x02\x12\x18\n\x10is_control_group\x18\x03 \x01(\x08"\x8a\x02\n\rRolloutConfig\x12T\n\rrollout_steps\x18\x01 \x03(\x0b2=.google.cloud.dialogflow.cx.v3beta1.RolloutConfig.RolloutStep\x12\x19\n\x11rollout_condition\x18\x02 \x01(\t\x12\x19\n\x11failure_condition\x18\x03 \x01(\t\x1am\n\x0bRolloutStep\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0ftraffic_percent\x18\x02 \x01(\x05\x12/\n\x0cmin_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"`\n\x0cRolloutState\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x12\n\nstep_index\x18\x03 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9f\x01\n\x0fVariantsHistory\x12O\n\x10version_variants\x18\x01 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.VersionVariantsH\x00\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\n\n\x08variants"}\n\x16ListExperimentsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"w\n\x17ListExperimentsResponse\x12C\n\x0bexperiments\x18\x01 \x03(\x0b2..google.cloud.dialogflow.cx.v3beta1.Experiment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x14GetExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"\xa0\x01\n\x17CreateExperimentRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Experiment\x12G\n\nexperiment\x18\x02 \x01(\x0b2..google.cloud.dialogflow.cx.v3beta1.ExperimentB\x03\xe0A\x02"\x98\x01\n\x17UpdateExperimentRequest\x12G\n\nexperiment\x18\x01 \x01(\x0b2..google.cloud.dialogflow.cx.v3beta1.ExperimentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x17DeleteExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"T\n\x16StartExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment"S\n\x15StopExperimentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Experiment2\xdd\r\n\x0bExperiments\x12\xe9\x01\n\x0fListExperiments\x12:.google.cloud.dialogflow.cx.v3beta1.ListExperimentsRequest\x1a;.google.cloud.dialogflow.cx.v3beta1.ListExperimentsResponse"]\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/experiments\x12\xd6\x01\n\rGetExperiment\x128.google.cloud.dialogflow.cx.v3beta1.GetExperimentRequest\x1a..google.cloud.dialogflow.cx.v3beta1.Experiment"[\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}\x12\xf5\x01\n\x10CreateExperiment\x12;.google.cloud.dialogflow.cx.v3beta1.CreateExperimentRequest\x1a..google.cloud.dialogflow.cx.v3beta1.Experiment"t\xdaA\x11parent,experiment\x82\xd3\xe4\x93\x02Z"L/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/experiments:\nexperiment\x12\x86\x02\n\x10UpdateExperiment\x12;.google.cloud.dialogflow.cx.v3beta1.UpdateExperimentRequest\x1a..google.cloud.dialogflow.cx.v3beta1.Experiment"\x84\x01\xdaA\x16experiment,update_mask\x82\xd3\xe4\x93\x02e2W/v3beta1/{experiment.name=projects/*/locations/*/agents/*/environments/*/experiments/*}:\nexperiment\x12\xc4\x01\n\x10DeleteExperiment\x12;.google.cloud.dialogflow.cx.v3beta1.DeleteExperimentRequest\x1a\x16.google.protobuf.Empty"[\xdaA\x04name\x82\xd3\xe4\x93\x02N*L/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}\x12\xe3\x01\n\x0fStartExperiment\x12:.google.cloud.dialogflow.cx.v3beta1.StartExperimentRequest\x1a..google.cloud.dialogflow.cx.v3beta1.Experiment"d\xdaA\x04name\x82\xd3\xe4\x93\x02W"R/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:start:\x01*\x12\xe0\x01\n\x0eStopExperiment\x129.google.cloud.dialogflow.cx.v3beta1.StopExperimentRequest\x1a..google.cloud.dialogflow.cx.v3beta1.Experiment"c\xdaA\x04name\x82\xd3\xe4\x93\x02V"Q/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:stop:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc6\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0fExperimentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.experiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0fExperimentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
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
    _globals['_EXPERIMENTS'].methods_by_name['ListExperiments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/experiments'
    _globals['_EXPERIMENTS'].methods_by_name['GetExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['GetExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}'
    _globals['_EXPERIMENTS'].methods_by_name['CreateExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['CreateExperiment']._serialized_options = b'\xdaA\x11parent,experiment\x82\xd3\xe4\x93\x02Z"L/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/experiments:\nexperiment'
    _globals['_EXPERIMENTS'].methods_by_name['UpdateExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['UpdateExperiment']._serialized_options = b'\xdaA\x16experiment,update_mask\x82\xd3\xe4\x93\x02e2W/v3beta1/{experiment.name=projects/*/locations/*/agents/*/environments/*/experiments/*}:\nexperiment'
    _globals['_EXPERIMENTS'].methods_by_name['DeleteExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['DeleteExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02N*L/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}'
    _globals['_EXPERIMENTS'].methods_by_name['StartExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['StartExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02W"R/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:start:\x01*'
    _globals['_EXPERIMENTS'].methods_by_name['StopExperiment']._loaded_options = None
    _globals['_EXPERIMENTS'].methods_by_name['StopExperiment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02V"Q/v3beta1/{name=projects/*/locations/*/agents/*/environments/*/experiments/*}:stop:\x01*'
    _globals['_EXPERIMENT']._serialized_start = 335
    _globals['_EXPERIMENT']._serialized_end = 2566
    _globals['_EXPERIMENT_DEFINITION']._serialized_start = 1140
    _globals['_EXPERIMENT_DEFINITION']._serialized_end = 1264
    _globals['_EXPERIMENT_RESULT']._serialized_start = 1267
    _globals['_EXPERIMENT_RESULT']._serialized_end = 2327
    _globals['_EXPERIMENT_RESULT_CONFIDENCEINTERVAL']._serialized_start = 1426
    _globals['_EXPERIMENT_RESULT_CONFIDENCEINTERVAL']._serialized_end = 1529
    _globals['_EXPERIMENT_RESULT_METRIC']._serialized_start = 1532
    _globals['_EXPERIMENT_RESULT_METRIC']._serialized_end = 1851
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS']._serialized_start = 1854
    _globals['_EXPERIMENT_RESULT_VERSIONMETRICS']._serialized_end = 2029
    _globals['_EXPERIMENT_RESULT_METRICTYPE']._serialized_start = 2032
    _globals['_EXPERIMENT_RESULT_METRICTYPE']._serialized_end = 2214
    _globals['_EXPERIMENT_RESULT_COUNTTYPE']._serialized_start = 2216
    _globals['_EXPERIMENT_RESULT_COUNTTYPE']._serialized_end = 2327
    _globals['_EXPERIMENT_STATE']._serialized_start = 2329
    _globals['_EXPERIMENT_STATE']._serialized_end = 2413
    _globals['_VERSIONVARIANTS']._serialized_start = 2569
    _globals['_VERSIONVARIANTS']._serialized_end = 2747
    _globals['_VERSIONVARIANTS_VARIANT']._serialized_start = 2667
    _globals['_VERSIONVARIANTS_VARIANT']._serialized_end = 2747
    _globals['_ROLLOUTCONFIG']._serialized_start = 2750
    _globals['_ROLLOUTCONFIG']._serialized_end = 3016
    _globals['_ROLLOUTCONFIG_ROLLOUTSTEP']._serialized_start = 2907
    _globals['_ROLLOUTCONFIG_ROLLOUTSTEP']._serialized_end = 3016
    _globals['_ROLLOUTSTATE']._serialized_start = 3018
    _globals['_ROLLOUTSTATE']._serialized_end = 3114
    _globals['_VARIANTSHISTORY']._serialized_start = 3117
    _globals['_VARIANTSHISTORY']._serialized_end = 3276
    _globals['_LISTEXPERIMENTSREQUEST']._serialized_start = 3278
    _globals['_LISTEXPERIMENTSREQUEST']._serialized_end = 3403
    _globals['_LISTEXPERIMENTSRESPONSE']._serialized_start = 3405
    _globals['_LISTEXPERIMENTSRESPONSE']._serialized_end = 3524
    _globals['_GETEXPERIMENTREQUEST']._serialized_start = 3526
    _globals['_GETEXPERIMENTREQUEST']._serialized_end = 3608
    _globals['_CREATEEXPERIMENTREQUEST']._serialized_start = 3611
    _globals['_CREATEEXPERIMENTREQUEST']._serialized_end = 3771
    _globals['_UPDATEEXPERIMENTREQUEST']._serialized_start = 3774
    _globals['_UPDATEEXPERIMENTREQUEST']._serialized_end = 3926
    _globals['_DELETEEXPERIMENTREQUEST']._serialized_start = 3928
    _globals['_DELETEEXPERIMENTREQUEST']._serialized_end = 4013
    _globals['_STARTEXPERIMENTREQUEST']._serialized_start = 4015
    _globals['_STARTEXPERIMENTREQUEST']._serialized_end = 4099
    _globals['_STOPEXPERIMENTREQUEST']._serialized_start = 4101
    _globals['_STOPEXPERIMENTREQUEST']._serialized_end = 4184
    _globals['_EXPERIMENTS']._serialized_start = 4187
    _globals['_EXPERIMENTS']._serialized_end = 5944