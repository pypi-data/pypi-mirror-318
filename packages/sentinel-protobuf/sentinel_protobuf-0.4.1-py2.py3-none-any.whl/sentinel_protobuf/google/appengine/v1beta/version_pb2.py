"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/version.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1beta import app_yaml_pb2 as google_dot_appengine_dot_v1beta_dot_app__yaml__pb2
from ....google.appengine.v1beta import deploy_pb2 as google_dot_appengine_dot_v1beta_dot_deploy__pb2
from ....google.appengine.v1beta import network_settings_pb2 as google_dot_appengine_dot_v1beta_dot_network__settings__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/appengine/v1beta/version.proto\x12\x17google.appengine.v1beta\x1a&google/appengine/v1beta/app_yaml.proto\x1a$google/appengine/v1beta/deploy.proto\x1a.google/appengine/v1beta/network_settings.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x0f\n\x07Version\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12F\n\x11automatic_scaling\x18\x03 \x01(\x0b2).google.appengine.v1beta.AutomaticScalingH\x00\x12>\n\rbasic_scaling\x18\x04 \x01(\x0b2%.google.appengine.v1beta.BasicScalingH\x00\x12@\n\x0emanual_scaling\x18\x05 \x01(\x0b2&.google.appengine.v1beta.ManualScalingH\x00\x12E\n\x10inbound_services\x18\x06 \x03(\x0e2+.google.appengine.v1beta.InboundServiceType\x12\x16\n\x0einstance_class\x18\x07 \x01(\t\x121\n\x07network\x18\x08 \x01(\x0b2 .google.appengine.v1beta.Network\x12\r\n\x05zones\x18v \x03(\t\x125\n\tresources\x18\t \x01(\x0b2".google.appengine.v1beta.Resources\x12\x0f\n\x07runtime\x18\n \x01(\t\x12\x17\n\x0fruntime_channel\x18u \x01(\t\x12\x12\n\nthreadsafe\x18\x0b \x01(\x08\x12\n\n\x02vm\x18\x0c \x01(\x08\x12\x18\n\x0fapp_engine_apis\x18\x80\x01 \x01(\x08\x12I\n\rbeta_settings\x18\r \x03(\x0b22.google.appengine.v1beta.Version.BetaSettingsEntry\x12\x0b\n\x03env\x18\x0e \x01(\t\x12>\n\x0eserving_status\x18\x0f \x01(\x0e2&.google.appengine.v1beta.ServingStatus\x12\x12\n\ncreated_by\x18\x10 \x01(\t\x12/\n\x0bcreate_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x18\n\x10disk_usage_bytes\x18\x12 \x01(\x03\x12\x1b\n\x13runtime_api_version\x18\x15 \x01(\t\x12$\n\x1cruntime_main_executable_path\x18\x16 \x01(\t\x12\x17\n\x0fservice_account\x18\x7f \x01(\t\x121\n\x08handlers\x18d \x03(\x0b2\x1f.google.appengine.v1beta.UrlMap\x12=\n\x0eerror_handlers\x18e \x03(\x0b2%.google.appengine.v1beta.ErrorHandler\x123\n\tlibraries\x18f \x03(\x0b2 .google.appengine.v1beta.Library\x12=\n\napi_config\x18g \x01(\x0b2).google.appengine.v1beta.ApiConfigHandler\x12I\n\renv_variables\x18h \x03(\x0b22.google.appengine.v1beta.Version.EnvVariablesEntry\x12T\n\x13build_env_variables\x18} \x03(\x0b27.google.appengine.v1beta.Version.BuildEnvVariablesEntry\x125\n\x12default_expiration\x18i \x01(\x0b2\x19.google.protobuf.Duration\x12:\n\x0chealth_check\x18j \x01(\x0b2$.google.appengine.v1beta.HealthCheck\x12@\n\x0freadiness_check\x18p \x01(\x0b2\'.google.appengine.v1beta.ReadinessCheck\x12>\n\x0eliveness_check\x18q \x01(\x0b2&.google.appengine.v1beta.LivenessCheck\x12\x1b\n\x13nobuild_files_regex\x18k \x01(\t\x127\n\ndeployment\x18l \x01(\x0b2#.google.appengine.v1beta.Deployment\x12\x13\n\x0bversion_url\x18m \x01(\t\x12K\n\x15endpoints_api_service\x18n \x01(\x0b2,.google.appengine.v1beta.EndpointsApiService\x127\n\nentrypoint\x18z \x01(\x0b2#.google.appengine.v1beta.Entrypoint\x12I\n\x14vpc_access_connector\x18y \x01(\x0b2+.google.appengine.v1beta.VpcAccessConnector\x1a3\n\x11BetaSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a3\n\x11EnvVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a8\n\x16BuildEnvVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\t\n\x07scaling"\xfb\x01\n\x13EndpointsApiService\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tconfig_id\x18\x02 \x01(\t\x12V\n\x10rollout_strategy\x18\x03 \x01(\x0e2<.google.appengine.v1beta.EndpointsApiService.RolloutStrategy\x12\x1e\n\x16disable_trace_sampling\x18\x04 \x01(\x08"K\n\x0fRolloutStrategy\x12 \n\x1cUNSPECIFIED_ROLLOUT_STRATEGY\x10\x00\x12\t\n\x05FIXED\x10\x01\x12\x0b\n\x07MANAGED\x10\x02"\xfc\x05\n\x10AutomaticScaling\x123\n\x10cool_down_period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12@\n\x0fcpu_utilization\x18\x02 \x01(\x0b2\'.google.appengine.v1beta.CpuUtilization\x12\x1f\n\x17max_concurrent_requests\x18\x03 \x01(\x05\x12\x1a\n\x12max_idle_instances\x18\x04 \x01(\x05\x12\x1b\n\x13max_total_instances\x18\x05 \x01(\x05\x126\n\x13max_pending_latency\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\x12min_idle_instances\x18\x07 \x01(\x05\x12\x1b\n\x13min_total_instances\x18\x08 \x01(\x05\x126\n\x13min_pending_latency\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x12H\n\x13request_utilization\x18\n \x01(\x0b2+.google.appengine.v1beta.RequestUtilization\x12B\n\x10disk_utilization\x18\x0b \x01(\x0b2(.google.appengine.v1beta.DiskUtilization\x12H\n\x13network_utilization\x18\x0c \x01(\x0b2+.google.appengine.v1beta.NetworkUtilization\x12=\n\x0ecustom_metrics\x18\x15 \x03(\x0b2%.google.appengine.v1beta.CustomMetric\x12W\n\x1bstandard_scheduler_settings\x18\x14 \x01(\x0b22.google.appengine.v1beta.StandardSchedulerSettings"V\n\x0cBasicScaling\x12/\n\x0cidle_timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rmax_instances\x18\x02 \x01(\x05""\n\rManualScaling\x12\x11\n\tinstances\x18\x01 \x01(\x05"j\n\x0eCpuUtilization\x12<\n\x19aggregation_window_length\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\x12target_utilization\x18\x02 \x01(\x01"a\n\x12RequestUtilization\x12\'\n\x1ftarget_request_count_per_second\x18\x01 \x01(\x05\x12"\n\x1atarget_concurrent_requests\x18\x02 \x01(\x05"\xa7\x01\n\x0fDiskUtilization\x12%\n\x1dtarget_write_bytes_per_second\x18\x0e \x01(\x05\x12#\n\x1btarget_write_ops_per_second\x18\x0f \x01(\x05\x12$\n\x1ctarget_read_bytes_per_second\x18\x10 \x01(\x05\x12"\n\x1atarget_read_ops_per_second\x18\x11 \x01(\x05"\xb8\x01\n\x12NetworkUtilization\x12$\n\x1ctarget_sent_bytes_per_second\x18\x01 \x01(\x05\x12&\n\x1etarget_sent_packets_per_second\x18\x0b \x01(\x05\x12(\n target_received_bytes_per_second\x18\x0c \x01(\x05\x12*\n"target_received_packets_per_second\x18\r \x01(\x05"\x9b\x01\n\x0cCustomMetric\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x12\x13\n\x0btarget_type\x18\x02 \x01(\t\x12\x1c\n\x12target_utilization\x18\x03 \x01(\x01H\x00\x12$\n\x1asingle_instance_assignment\x18\x04 \x01(\x01H\x00\x12\x0e\n\x06filter\x18\x05 \x01(\tB\r\n\x0btarget_spec"\x90\x01\n\x19StandardSchedulerSettings\x12\x1e\n\x16target_cpu_utilization\x18\x01 \x01(\x01\x12%\n\x1dtarget_throughput_utilization\x18\x02 \x01(\x01\x12\x15\n\rmin_instances\x18\x03 \x01(\x05\x12\x15\n\rmax_instances\x18\x04 \x01(\x05"y\n\x07Network\x12\x17\n\x0fforwarded_ports\x18\x01 \x03(\t\x12\x14\n\x0cinstance_tag\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\x0fsubnetwork_name\x18\x04 \x01(\t\x12\x18\n\x10session_affinity\x18\x05 \x01(\x08"<\n\x06Volume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bvolume_type\x18\x02 \x01(\t\x12\x0f\n\x07size_gb\x18\x03 \x01(\x01"\x89\x01\n\tResources\x12\x0b\n\x03cpu\x18\x01 \x01(\x01\x12\x0f\n\x07disk_gb\x18\x02 \x01(\x01\x12\x11\n\tmemory_gb\x18\x03 \x01(\x01\x120\n\x07volumes\x18\x04 \x03(\x0b2\x1f.google.appengine.v1beta.Volume\x12\x19\n\x11kms_key_reference\x18\x05 \x01(\t""\n\x12VpcAccessConnector\x12\x0c\n\x04name\x18\x01 \x01(\t"(\n\nEntrypoint\x12\x0f\n\x05shell\x18\x01 \x01(\tH\x00B\t\n\x07command*\xbb\x02\n\x12InboundServiceType\x12\x1f\n\x1bINBOUND_SERVICE_UNSPECIFIED\x10\x00\x12\x18\n\x14INBOUND_SERVICE_MAIL\x10\x01\x12\x1f\n\x1bINBOUND_SERVICE_MAIL_BOUNCE\x10\x02\x12\x1e\n\x1aINBOUND_SERVICE_XMPP_ERROR\x10\x03\x12 \n\x1cINBOUND_SERVICE_XMPP_MESSAGE\x10\x04\x12"\n\x1eINBOUND_SERVICE_XMPP_SUBSCRIBE\x10\x05\x12!\n\x1dINBOUND_SERVICE_XMPP_PRESENCE\x10\x06\x12$\n INBOUND_SERVICE_CHANNEL_PRESENCE\x10\x07\x12\x1a\n\x16INBOUND_SERVICE_WARMUP\x10\t*I\n\rServingStatus\x12\x1e\n\x1aSERVING_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0b\n\x07STOPPED\x10\x02B\xd2\x01\n\x1bcom.google.appengine.v1betaB\x0cVersionProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0cVersionProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_VERSION_BETASETTINGSENTRY']._loaded_options = None
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_VERSION_ENVVARIABLESENTRY']._loaded_options = None
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._loaded_options = None
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_INBOUNDSERVICETYPE']._serialized_start = 4697
    _globals['_INBOUNDSERVICETYPE']._serialized_end = 5012
    _globals['_SERVINGSTATUS']._serialized_start = 5014
    _globals['_SERVINGSTATUS']._serialized_end = 5087
    _globals['_VERSION']._serialized_start = 258
    _globals['_VERSION']._serialized_end = 2277
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_start = 2104
    _globals['_VERSION_BETASETTINGSENTRY']._serialized_end = 2155
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_start = 2157
    _globals['_VERSION_ENVVARIABLESENTRY']._serialized_end = 2208
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_start = 2210
    _globals['_VERSION_BUILDENVVARIABLESENTRY']._serialized_end = 2266
    _globals['_ENDPOINTSAPISERVICE']._serialized_start = 2280
    _globals['_ENDPOINTSAPISERVICE']._serialized_end = 2531
    _globals['_ENDPOINTSAPISERVICE_ROLLOUTSTRATEGY']._serialized_start = 2456
    _globals['_ENDPOINTSAPISERVICE_ROLLOUTSTRATEGY']._serialized_end = 2531
    _globals['_AUTOMATICSCALING']._serialized_start = 2534
    _globals['_AUTOMATICSCALING']._serialized_end = 3298
    _globals['_BASICSCALING']._serialized_start = 3300
    _globals['_BASICSCALING']._serialized_end = 3386
    _globals['_MANUALSCALING']._serialized_start = 3388
    _globals['_MANUALSCALING']._serialized_end = 3422
    _globals['_CPUUTILIZATION']._serialized_start = 3424
    _globals['_CPUUTILIZATION']._serialized_end = 3530
    _globals['_REQUESTUTILIZATION']._serialized_start = 3532
    _globals['_REQUESTUTILIZATION']._serialized_end = 3629
    _globals['_DISKUTILIZATION']._serialized_start = 3632
    _globals['_DISKUTILIZATION']._serialized_end = 3799
    _globals['_NETWORKUTILIZATION']._serialized_start = 3802
    _globals['_NETWORKUTILIZATION']._serialized_end = 3986
    _globals['_CUSTOMMETRIC']._serialized_start = 3989
    _globals['_CUSTOMMETRIC']._serialized_end = 4144
    _globals['_STANDARDSCHEDULERSETTINGS']._serialized_start = 4147
    _globals['_STANDARDSCHEDULERSETTINGS']._serialized_end = 4291
    _globals['_NETWORK']._serialized_start = 4293
    _globals['_NETWORK']._serialized_end = 4414
    _globals['_VOLUME']._serialized_start = 4416
    _globals['_VOLUME']._serialized_end = 4476
    _globals['_RESOURCES']._serialized_start = 4479
    _globals['_RESOURCES']._serialized_end = 4616
    _globals['_VPCACCESSCONNECTOR']._serialized_start = 4618
    _globals['_VPCACCESSCONNECTOR']._serialized_end = 4652
    _globals['_ENTRYPOINT']._serialized_start = 4654
    _globals['_ENTRYPOINT']._serialized_end = 4694