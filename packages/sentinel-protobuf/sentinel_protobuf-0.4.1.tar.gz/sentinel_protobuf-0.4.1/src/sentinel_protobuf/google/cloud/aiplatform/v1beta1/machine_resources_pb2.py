"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/machine_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1beta1 import accelerator_type_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_accelerator__type__pb2
from .....google.cloud.aiplatform.v1beta1 import reservation_affinity_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_reservation__affinity__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/aiplatform/v1beta1/machine_resources.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a6google/cloud/aiplatform/v1beta1/accelerator_type.proto\x1a:google/cloud/aiplatform/v1beta1/reservation_affinity.proto"\x8b\x02\n\x0bMachineSpec\x12\x19\n\x0cmachine_type\x18\x01 \x01(\tB\x03\xe0A\x05\x12O\n\x10accelerator_type\x18\x02 \x01(\x0e20.google.cloud.aiplatform.v1beta1.AcceleratorTypeB\x03\xe0A\x05\x12\x19\n\x11accelerator_count\x18\x03 \x01(\x05\x12\x19\n\x0ctpu_topology\x18\x04 \x01(\tB\x03\xe0A\x05\x12Z\n\x14reservation_affinity\x18\x05 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ReservationAffinityB\x06\xe0A\x05\xe0A\x01"\xba\x02\n\x12DedicatedResources\x12J\n\x0cmachine_spec\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpecB\x06\xe0A\x02\xe0A\x05\x12!\n\x11min_replica_count\x18\x02 \x01(\x05B\x06\xe0A\x02\xe0A\x05\x12\x1e\n\x11max_replica_count\x18\x03 \x01(\x05B\x03\xe0A\x05\x12#\n\x16required_replica_count\x18\t \x01(\x05B\x03\xe0A\x01\x12]\n\x18autoscaling_metric_specs\x18\x04 \x03(\x0b26.google.cloud.aiplatform.v1beta1.AutoscalingMetricSpecB\x03\xe0A\x05\x12\x11\n\x04spot\x18\x05 \x01(\x08B\x03\xe0A\x01"T\n\x12AutomaticResources\x12\x1e\n\x11min_replica_count\x18\x01 \x01(\x05B\x03\xe0A\x05\x12\x1e\n\x11max_replica_count\x18\x02 \x01(\x05B\x03\xe0A\x05"\xaa\x01\n\x17BatchDedicatedResources\x12J\n\x0cmachine_spec\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpecB\x06\xe0A\x02\xe0A\x05\x12#\n\x16starting_replica_count\x18\x02 \x01(\x05B\x03\xe0A\x05\x12\x1e\n\x11max_replica_count\x18\x03 \x01(\x05B\x03\xe0A\x05"/\n\x11ResourcesConsumed\x12\x1a\n\rreplica_hours\x18\x01 \x01(\x01B\x03\xe0A\x03"=\n\x08DiskSpec\x12\x16\n\x0eboot_disk_type\x18\x01 \x01(\t\x12\x19\n\x11boot_disk_size_gb\x18\x02 \x01(\x05"=\n\x12PersistentDiskSpec\x12\x11\n\tdisk_type\x18\x01 \x01(\t\x12\x14\n\x0cdisk_size_gb\x18\x02 \x01(\x03"L\n\x08NfsMount\x12\x13\n\x06server\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04path\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bmount_point\x18\x03 \x01(\tB\x03\xe0A\x02"A\n\x15AutoscalingMetricSpec\x12\x18\n\x0bmetric_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0e\n\x06target\x18\x02 \x01(\x05".\n\x10ShieldedVmConfig\x12\x1a\n\x12enable_secure_boot\x18\x01 \x01(\x08B\xec\x01\n#com.google.cloud.aiplatform.v1beta1B\x15MachineResourcesProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.machine_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x15MachineResourcesProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MACHINESPEC'].fields_by_name['machine_type']._loaded_options = None
    _globals['_MACHINESPEC'].fields_by_name['machine_type']._serialized_options = b'\xe0A\x05'
    _globals['_MACHINESPEC'].fields_by_name['accelerator_type']._loaded_options = None
    _globals['_MACHINESPEC'].fields_by_name['accelerator_type']._serialized_options = b'\xe0A\x05'
    _globals['_MACHINESPEC'].fields_by_name['tpu_topology']._loaded_options = None
    _globals['_MACHINESPEC'].fields_by_name['tpu_topology']._serialized_options = b'\xe0A\x05'
    _globals['_MACHINESPEC'].fields_by_name['reservation_affinity']._loaded_options = None
    _globals['_MACHINESPEC'].fields_by_name['reservation_affinity']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['min_replica_count']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['min_replica_count']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['max_replica_count']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['max_replica_count']._serialized_options = b'\xe0A\x05'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['required_replica_count']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['required_replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['autoscaling_metric_specs']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['autoscaling_metric_specs']._serialized_options = b'\xe0A\x05'
    _globals['_DEDICATEDRESOURCES'].fields_by_name['spot']._loaded_options = None
    _globals['_DEDICATEDRESOURCES'].fields_by_name['spot']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOMATICRESOURCES'].fields_by_name['min_replica_count']._loaded_options = None
    _globals['_AUTOMATICRESOURCES'].fields_by_name['min_replica_count']._serialized_options = b'\xe0A\x05'
    _globals['_AUTOMATICRESOURCES'].fields_by_name['max_replica_count']._loaded_options = None
    _globals['_AUTOMATICRESOURCES'].fields_by_name['max_replica_count']._serialized_options = b'\xe0A\x05'
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['starting_replica_count']._loaded_options = None
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['starting_replica_count']._serialized_options = b'\xe0A\x05'
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['max_replica_count']._loaded_options = None
    _globals['_BATCHDEDICATEDRESOURCES'].fields_by_name['max_replica_count']._serialized_options = b'\xe0A\x05'
    _globals['_RESOURCESCONSUMED'].fields_by_name['replica_hours']._loaded_options = None
    _globals['_RESOURCESCONSUMED'].fields_by_name['replica_hours']._serialized_options = b'\xe0A\x03'
    _globals['_NFSMOUNT'].fields_by_name['server']._loaded_options = None
    _globals['_NFSMOUNT'].fields_by_name['server']._serialized_options = b'\xe0A\x02'
    _globals['_NFSMOUNT'].fields_by_name['path']._loaded_options = None
    _globals['_NFSMOUNT'].fields_by_name['path']._serialized_options = b'\xe0A\x02'
    _globals['_NFSMOUNT'].fields_by_name['mount_point']._loaded_options = None
    _globals['_NFSMOUNT'].fields_by_name['mount_point']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOSCALINGMETRICSPEC'].fields_by_name['metric_name']._loaded_options = None
    _globals['_AUTOSCALINGMETRICSPEC'].fields_by_name['metric_name']._serialized_options = b'\xe0A\x02'
    _globals['_MACHINESPEC']._serialized_start = 242
    _globals['_MACHINESPEC']._serialized_end = 509
    _globals['_DEDICATEDRESOURCES']._serialized_start = 512
    _globals['_DEDICATEDRESOURCES']._serialized_end = 826
    _globals['_AUTOMATICRESOURCES']._serialized_start = 828
    _globals['_AUTOMATICRESOURCES']._serialized_end = 912
    _globals['_BATCHDEDICATEDRESOURCES']._serialized_start = 915
    _globals['_BATCHDEDICATEDRESOURCES']._serialized_end = 1085
    _globals['_RESOURCESCONSUMED']._serialized_start = 1087
    _globals['_RESOURCESCONSUMED']._serialized_end = 1134
    _globals['_DISKSPEC']._serialized_start = 1136
    _globals['_DISKSPEC']._serialized_end = 1197
    _globals['_PERSISTENTDISKSPEC']._serialized_start = 1199
    _globals['_PERSISTENTDISKSPEC']._serialized_end = 1260
    _globals['_NFSMOUNT']._serialized_start = 1262
    _globals['_NFSMOUNT']._serialized_end = 1338
    _globals['_AUTOSCALINGMETRICSPEC']._serialized_start = 1340
    _globals['_AUTOSCALINGMETRICSPEC']._serialized_end = 1405
    _globals['_SHIELDEDVMCONFIG']._serialized_start = 1407
    _globals['_SHIELDEDVMCONFIG']._serialized_end = 1453