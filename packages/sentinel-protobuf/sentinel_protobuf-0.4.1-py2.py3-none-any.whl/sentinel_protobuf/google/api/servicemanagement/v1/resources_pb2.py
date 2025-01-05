"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/servicemanagement/v1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import config_change_pb2 as google_dot_api_dot_config__change__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/api/servicemanagement/v1/resources.proto\x12\x1fgoogle.api.servicemanagement.v1\x1a\x1egoogle/api/config_change.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"C\n\x0eManagedService\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x1b\n\x13producer_project_id\x18\x03 \x01(\t"\x91\x03\n\x11OperationMetadata\x12\x16\n\x0eresource_names\x18\x01 \x03(\t\x12F\n\x05steps\x18\x02 \x03(\x0b27.google.api.servicemanagement.v1.OperationMetadata.Step\x12\x1b\n\x13progress_percentage\x18\x03 \x01(\x05\x12.\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1af\n\x04Step\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12I\n\x06status\x18\x04 \x01(\x0e29.google.api.servicemanagement.v1.OperationMetadata.Status"g\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04DONE\x10\x01\x12\x0f\n\x0bNOT_STARTED\x10\x02\x12\x0f\n\x0bIN_PROGRESS\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tCANCELLED\x10\x05"\x8f\x01\n\nDiagnostic\x12\x10\n\x08location\x18\x01 \x01(\t\x12>\n\x04kind\x18\x02 \x01(\x0e20.google.api.servicemanagement.v1.Diagnostic.Kind\x12\x0f\n\x07message\x18\x03 \x01(\t"\x1e\n\x04Kind\x12\x0b\n\x07WARNING\x10\x00\x12\t\n\x05ERROR\x10\x01"V\n\x0cConfigSource\x12\n\n\x02id\x18\x05 \x01(\t\x12:\n\x05files\x18\x02 \x03(\x0b2+.google.api.servicemanagement.v1.ConfigFile"\x95\x02\n\nConfigFile\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x15\n\rfile_contents\x18\x03 \x01(\x0c\x12G\n\tfile_type\x18\x04 \x01(\x0e24.google.api.servicemanagement.v1.ConfigFile.FileType"\x93\x01\n\x08FileType\x12\x19\n\x15FILE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SERVICE_CONFIG_YAML\x10\x01\x12\x11\n\rOPEN_API_JSON\x10\x02\x12\x11\n\rOPEN_API_YAML\x10\x03\x12\x1d\n\x19FILE_DESCRIPTOR_SET_PROTO\x10\x04\x12\x0e\n\nPROTO_FILE\x10\x06"\x19\n\tConfigRef\x12\x0c\n\x04name\x18\x01 \x01(\t"@\n\x0cChangeReport\x120\n\x0econfig_changes\x18\x01 \x03(\x0b2\x18.google.api.ConfigChange"\xf9\x05\n\x07Rollout\x12\x17\n\nrollout_id\x18\x01 \x01(\tB\x03\xe0A\x01\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x03 \x01(\t\x12F\n\x06status\x18\x04 \x01(\x0e26.google.api.servicemanagement.v1.Rollout.RolloutStatus\x12c\n\x18traffic_percent_strategy\x18\x05 \x01(\x0b2?.google.api.servicemanagement.v1.Rollout.TrafficPercentStrategyH\x00\x12b\n\x17delete_service_strategy\x18\xc8\x01 \x01(\x0b2>.google.api.servicemanagement.v1.Rollout.DeleteServiceStrategyH\x00\x12\x14\n\x0cservice_name\x18\x08 \x01(\t\x1a\xb3\x01\n\x16TrafficPercentStrategy\x12e\n\x0bpercentages\x18\x01 \x03(\x0b2P.google.api.servicemanagement.v1.Rollout.TrafficPercentStrategy.PercentagesEntry\x1a2\n\x10PercentagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x028\x01\x1a\x17\n\x15DeleteServiceStrategy"\x8d\x01\n\rRolloutStatus\x12\x1e\n\x1aROLLOUT_STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0b\n\x07PENDING\x10\x05\x12\x16\n\x12FAILED_ROLLED_BACK\x10\x06B\n\n\x08strategyB\x82\x02\n#com.google.api.servicemanagement.v1B\x0eResourcesProtoP\x01ZScloud.google.com/go/servicemanagement/apiv1/servicemanagementpb;servicemanagementpb\xa2\x02\x04GASM\xaa\x02!Google.Cloud.ServiceManagement.V1\xca\x02!Google\\Cloud\\ServiceManagement\\V1\xea\x02$Google::Cloud::ServiceManagement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.servicemanagement.v1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.api.servicemanagement.v1B\x0eResourcesProtoP\x01ZScloud.google.com/go/servicemanagement/apiv1/servicemanagementpb;servicemanagementpb\xa2\x02\x04GASM\xaa\x02!Google.Cloud.ServiceManagement.V1\xca\x02!Google\\Cloud\\ServiceManagement\\V1\xea\x02$Google::Cloud::ServiceManagement::V1'
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY_PERCENTAGESENTRY']._loaded_options = None
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY_PERCENTAGESENTRY']._serialized_options = b'8\x01'
    _globals['_ROLLOUT'].fields_by_name['rollout_id']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['rollout_id']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEDSERVICE']._serialized_start = 182
    _globals['_MANAGEDSERVICE']._serialized_end = 249
    _globals['_OPERATIONMETADATA']._serialized_start = 252
    _globals['_OPERATIONMETADATA']._serialized_end = 653
    _globals['_OPERATIONMETADATA_STEP']._serialized_start = 446
    _globals['_OPERATIONMETADATA_STEP']._serialized_end = 548
    _globals['_OPERATIONMETADATA_STATUS']._serialized_start = 550
    _globals['_OPERATIONMETADATA_STATUS']._serialized_end = 653
    _globals['_DIAGNOSTIC']._serialized_start = 656
    _globals['_DIAGNOSTIC']._serialized_end = 799
    _globals['_DIAGNOSTIC_KIND']._serialized_start = 769
    _globals['_DIAGNOSTIC_KIND']._serialized_end = 799
    _globals['_CONFIGSOURCE']._serialized_start = 801
    _globals['_CONFIGSOURCE']._serialized_end = 887
    _globals['_CONFIGFILE']._serialized_start = 890
    _globals['_CONFIGFILE']._serialized_end = 1167
    _globals['_CONFIGFILE_FILETYPE']._serialized_start = 1020
    _globals['_CONFIGFILE_FILETYPE']._serialized_end = 1167
    _globals['_CONFIGREF']._serialized_start = 1169
    _globals['_CONFIGREF']._serialized_end = 1194
    _globals['_CHANGEREPORT']._serialized_start = 1196
    _globals['_CHANGEREPORT']._serialized_end = 1260
    _globals['_ROLLOUT']._serialized_start = 1263
    _globals['_ROLLOUT']._serialized_end = 2024
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY']._serialized_start = 1664
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY']._serialized_end = 1843
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY_PERCENTAGESENTRY']._serialized_start = 1793
    _globals['_ROLLOUT_TRAFFICPERCENTSTRATEGY_PERCENTAGESENTRY']._serialized_end = 1843
    _globals['_ROLLOUT_DELETESERVICESTRATEGY']._serialized_start = 1845
    _globals['_ROLLOUT_DELETESERVICESTRATEGY']._serialized_end = 1868
    _globals['_ROLLOUT_ROLLOUTSTATUS']._serialized_start = 1871
    _globals['_ROLLOUT_ROLLOUTSTATUS']._serialized_end = 2012