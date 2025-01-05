"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/version.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1 import app_yaml_pb2 as google_dot_appengine_dot_v1_dot_app__yaml__pb2
from ....google.appengine.v1 import deploy_pb2 as google_dot_appengine_dot_v1_dot_deploy__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/appengine/v1/version.proto\x12\x13google.appengine.v1\x1a"google/appengine/v1/app_yaml.proto\x1a google/appengine/v1/deploy.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f\x0f\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12B\n\x11automatic_scaling\x18\x03 \x01(\x0b2%.google.appengine.v1.AutomaticScalingH\x00\x12:\n\rbasic_scaling\x18\x04 \x01(\x0b2!.google.appengine.v1.BasicScalingH\x00\x12<\n\x0emanual_scaling\x18\x05 \x01(\x0b2".google.appengine.v1.ManualScalingH\x00\x12A\n\x10inbound_services\x18\x06 \x03(\x0e2\'.google.appengine.v1.InboundServiceType\x12\x16\n\x0einstance_class\x18\x07 \x01(\t\x12-\n\x07network\x18\x08 \x01(\x0b2\x1c.google.appengine.v1.Network\x12\r\n\x05zones\x18v \x03(\t\x121\n\tresources\x18\t \x01(\x0b2\x1e.google.appengine.v1.Resources\x12\x0f\n\x07runtime\x18\n \x01(\t\x12\x17\n\x0fruntime_channel\x18u \x01(\t\x12\x12\n\nthreadsafe\x18\x0b \x01(\x08\x12\n\n\x02vm\x18\x0c \x01(\x08\x12\x18\n\x0fapp_engine_apis\x18\x80\x01 \x01(\x08\x12E\n\rbeta_settings\x18\r \x03(\x0b2..google.appengine.v1.Version.BetaSettingsEntry\x12\x0b\n\x03env\x18\x0e \x01(\t\x12:\n\x0eserving_status\x18\x0f \x01(\x0e2".google.appengine.v1.ServingStatus\x12\x12\n\ncreated_by\x18\x10 \x01(\t\x12/\n\x0bcreate_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x18\n\x10disk_usage_bytes\x18\x12 \x01(\x03\x12\x1b\n\x13runtime_api_version\x18\x15 \x01(\t\x12$\n\x1cruntime_main_executable_path\x18\x16 \x01(\t\x12\x17\n\x0fservice_account\x18\x7f \x01(\t\x12-\n\x08handlers\x18d \x03(\x0b2\x1b.google.appengine.v1.UrlMap\x129\n\x0eerror_handlers\x18e \x03(\x0b2!.google.appengine.v1.ErrorHandler\x12/\n\tlibraries\x18f \x03(\x0b2\x1c.google.appengine.v1.Library\x129\n\napi_config\x18g \x01(\x0b2%.google.appengine.v1.ApiConfigHandler\x12E\n\renv_variables\x18h \x03(\x0b2..google.appengine.v1.Version.EnvVariablesEntry\x12P\n\x13build_env_variables\x18} \x03(\x0b23.google.appengine.v1.Version.BuildEnvVariablesEntry\x125\n\x12default_expiration\x18i \x01(\x0b2\x19.google.protobuf.Duration\x126\n\x0chealth_check\x18j \x01(\x0b2 .google.appengine.v1.HealthCheck\x12<\n\x0freadiness_check\x18p \x01(\x0b2#.google.appengine.v1.ReadinessCheck\x12:\n\x0eliveness_check\x18q \x01(\x0b2".google.appengine.v1.LivenessCheck\x12\x1b\n\x13nobuild_files_regex\x18k \x01(\t\x123\n\ndeployment\x18l \x01(\x0b2\x1f.google.appengine.v1.Deployment\x12\x13\n\x0bversion_url\x18m \x01(\t\x12G\n\x15endpoints_api_service\x18n \x01(\x0b2(.google.appengine.v1.EndpointsApiService\x123\n\nentrypoint\x18z \x01(\x0b2\x1f.google.appengine.v1.Entrypoint\x12E\n\x14vpc_access_connector\x18y \x01(\x0b2\'.google.appengine.v1.VpcAccessConnector\x1a3\n\x11BetaSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a3\n\x11EnvVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a8\n\x16BuildEnvVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\t\n\x07scaling"\xf7\x01\n\x13EndpointsApiService\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tconfig_id\x18\x02 \x01(\t\x12R\n\x10rollout_strategy\x18\x03 \x01(\x0e28.google.appengine.v1.EndpointsApiService.RolloutStrategy\x12\x1e\n\x16disable_trace_sampling\x18\x04 \x01(\x08"K\n\x0fRolloutStrategy\x12 \n\x1cUNSPECIFIED_ROLLOUT_STRATEGY\x10\x00\x12\t\n\x05FIXED\x10\x01\x12\x0b\n\x07MANAGED\x10\x02"\xa9\x05\n\x10AutomaticScaling\x123\n\x10cool_down_period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12<\n\x0fcpu_utilization\x18\x02 \x01(\x0b2#.google.appengine.v1.CpuUtilization\x12\x1f\n\x17max_concurrent_requests\x18\x03 \x01(\x05\x12\x1a\n\x12max_idle_instances\x18\x04 \x01(\x05\x12\x1b\n\x13max_total_instances\x18\x05 \x01(\x05\x126\n\x13max_pending_latency\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\x12min_idle_instances\x18\x07 \x01(\x05\x12\x1b\n\x13min_total_instances\x18\x08 \x01(\x05\x126\n\x13min_pending_latency\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\x13request_utilization\x18\n \x01(\x0b2\'.google.appengine.v1.RequestUtilization\x12>\n\x10disk_utilization\x18\x0b \x01(\x0b2$.google.appengine.v1.DiskUtilization\x12D\n\x13network_utilization\x18\x0c \x01(\x0b2\'.google.appengine.v1.NetworkUtilization\x12S\n\x1bstandard_scheduler_settings\x18\x14 \x01(\x0b2..google.appengine.v1.StandardSchedulerSettings"V\n\x0cBasicScaling\x12/\n\x0cidle_timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rmax_instances\x18\x02 \x01(\x05""\n\rManualScaling\x12\x11\n\tinstances\x18\x01 \x01(\x05"j\n\x0eCpuUtilization\x12<\n\x19aggregation_window_length\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\x12target_utilization\x18\x02 \x01(\x01"a\n\x12RequestUtilization\x12\'\n\x1ftarget_request_count_per_second\x18\x01 \x01(\x05\x12"\n\x1atarget_concurrent_requests\x18\x02 \x01(\x05"\xa7\x01\n\x0fDiskUtilization\x12%\n\x1dtarget_write_bytes_per_second\x18\x0e \x01(\x05\x12#\n\x1btarget_write_ops_per_second\x18\x0f \x01(\x05\x12$\n\x1ctarget_read_bytes_per_second\x18\x10 \x01(\x05\x12"\n\x1atarget_read_ops_per_second\x18\x11 \x01(\x05"\xb8\x01\n\x12NetworkUtilization\x12$\n\x1ctarget_sent_bytes_per_second\x18\x01 \x01(\x05\x12&\n\x1etarget_sent_packets_per_second\x18\x0b \x01(\x05\x12(\n target_received_bytes_per_second\x18\x0c \x01(\x05\x12*\n"target_received_packets_per_second\x18\r \x01(\x05"\x90\x01\n\x19StandardSchedulerSettings\x12\x1e\n\x16target_cpu_utilization\x18\x01 \x01(\x01\x12%\n\x1dtarget_throughput_utilization\x18\x02 \x01(\x01\x12\x15\n\rmin_instances\x18\x03 \x01(\x05\x12\x15\n\rmax_instances\x18\x04 \x01(\x05"y\n\x07Network\x12\x17\n\x0fforwarded_ports\x18\x01 \x03(\t\x12\x14\n\x0cinstance_tag\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\x0fsubnetwork_name\x18\x04 \x01(\t\x12\x18\n\x10session_affinity\x18\x05 \x01(\x08"<\n\x06Volume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bvolume_type\x18\x02 \x01(\t\x12\x0f\n\x07size_gb\x18\x03 \x01(\x01"\x85\x01\n\tResources\x12\x0b\n\x03cpu\x18\x01 \x01(\x01\x12\x0f\n\x07disk_gb\x18\x02 \x01(\x01\x12\x11\n\tmemory_gb\x18\x03 \x01(\x01\x12,\n\x07volumes\x18\x04 \x03(\x0b2\x1b.google.appengine.v1.Volume\x12\x19\n\x11kms_key_reference\x18\x05 \x01(\t"\xca\x01\n\x12VpcAccessConnector\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x0eegress_setting\x18\x02 \x01(\x0e25.google.appengine.v1.VpcAccessConnector.EgressSetting"W\n\rEgressSetting\x12\x1e\n\x1aEGRESS_SETTING_UNSPECIFIED\x10\x00\x12\x0f\n\x0bALL_TRAFFIC\x10\x01\x12\x15\n\x11PRIVATE_IP_RANGES\x10\x02"(\n\nEntrypoint\x12\x0f\n\x05shell\x18\x01 \x01(\tH\x00B\t\n\x07command*\xbb\x02\n\x12InboundServiceType\x12\x1f\n\x1bINBOUND_SERVICE_UNSPECIFIED\x10\x00\x12\x18\n\x14INBOUND_SERVICE_MAIL\x10\x01\x12\x1f\n\x1bINBOUND_SERVICE_MAIL_BOUNCE\x10\x02\x12\x1e\n\x1aINBOUND_SERVICE_XMPP_ERROR\x10\x03\x12 \n\x1cINBOUND_SERVICE_XMPP_MESSAGE\x10\x04\x12"\n\x1eINBOUND_SERVICE_XMPP_SUBSCRIBE\x10\x05\x12!\n\x1dINBOUND_SERVICE_XMPP_PRESENCE\x10\x06\x12$\n INBOUND_SERVICE_CHANNEL_PRESENCE\x10\x07\x12\x1a\n\x16INBOUND_SERVICE_WARMUP\x10\t*I\n\rServingStatus\x12\x1e\n\x1aSERVING_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0b\n\x07STOPPED\x10\x02B\xbd\x01\n\x17com.google.appengine.v1B\x0cVersionProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x0cVersionProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_VERSION_BETASETTINGSENTRY']._loaded_options = None
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_VERSION_ENVVARIABLESENTRY']._loaded_options = None
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._loaded_options = None
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_INBOUNDSERVICETYPE']._serialized_start = 4469
    _globals['_INBOUNDSERVICETYPE']._serialized_end = 4784
    _globals['_SERVINGSTATUS']._serialized_start = 4786
    _globals['_SERVINGSTATUS']._serialized_end = 4859
    _globals['_VERSION']._serialized_start = 194
    _globals['_VERSION']._serialized_end = 2129
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_start = 1956
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_end = 2007
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_start = 2009
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_end = 2060
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_start = 2062
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_end = 2118
    _globals['_ENDPOINTSAPISERVICE']._serialized_start = 2132
    _globals['_ENDPOINTSAPISERVICE']._serialized_end = 2379
    _globals['_ENDPOINTSAPISERVICE_ROLLOUTSTRATEGY']._serialized_start = 2304
    _globals['_ENDPOINTSAPISERVICE_ROLLOUTSTRATEGY']._serialized_end = 2379
    _globals['_AUTOMATICSCALING']._serialized_start = 2382
    _globals['_AUTOMATICSCALING']._serialized_end = 3063
    _globals['_BASICSCALING']._serialized_start = 3065
    _globals['_BASICSCALING']._serialized_end = 3151
    _globals['_MANUALSCALING']._serialized_start = 3153
    _globals['_MANUALSCALING']._serialized_end = 3187
    _globals['_CPUUTILIZATION']._serialized_start = 3189
    _globals['_CPUUTILIZATION']._serialized_end = 3295
    _globals['_REQUESTUTILIZATION']._serialized_start = 3297
    _globals['_REQUESTUTILIZATION']._serialized_end = 3394
    _globals['_DISKUTILIZATION']._serialized_start = 3397
    _globals['_DISKUTILIZATION']._serialized_end = 3564
    _globals['_NETWORKUTILIZATION']._serialized_start = 3567
    _globals['_NETWORKUTILIZATION']._serialized_end = 3751
    _globals['_STANDARDSCHEDULERSETTINGS']._serialized_start = 3754
    _globals['_STANDARDSCHEDULERSETTINGS']._serialized_end = 3898
    _globals['_NETWORK']._serialized_start = 3900
    _globals['_NETWORK']._serialized_end = 4021
    _globals['_VOLUME']._serialized_start = 4023
    _globals['_VOLUME']._serialized_end = 4083
    _globals['_RESOURCES']._serialized_start = 4086
    _globals['_RESOURCES']._serialized_end = 4219
    _globals['_VPCACCESSCONNECTOR']._serialized_start = 4222
    _globals['_VPCACCESSCONNECTOR']._serialized_end = 4424
    _globals['_VPCACCESSCONNECTOR_EGRESSSETTING']._serialized_start = 4337
    _globals['_VPCACCESSCONNECTOR_EGRESSSETTING']._serialized_end = 4424
    _globals['_ENTRYPOINT']._serialized_start = 4426
    _globals['_ENTRYPOINT']._serialized_end = 4466