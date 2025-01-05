"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/workstations/logging/v1/platform_logs.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/workstations/logging/v1/platform_logs.proto\x12$google.cloud.workstations.logging.v1"\xd4\x01\n\x10WorkstationEvent\x12V\n\x13vm_assignment_event\x18\x01 \x01(\x0b27.google.cloud.workstations.logging.v1.VmAssignmentEventH\x00\x12Z\n\x15disk_assignment_event\x18\x02 \x01(\x0b29.google.cloud.workstations.logging.v1.DiskAssignmentEventH\x00B\x0c\n\nevent_type"\x1f\n\x11VmAssignmentEvent\x12\n\n\x02vm\x18\x01 \x01(\t"#\n\x13DiskAssignmentEvent\x12\x0c\n\x04disk\x18\x01 \x01(\tB\x83\x01\n(com.google.cloud.workstations.logging.v1B\x11PlatformLogsProtoP\x01ZBcloud.google.com/go/workstations/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.workstations.logging.v1.platform_logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.workstations.logging.v1B\x11PlatformLogsProtoP\x01ZBcloud.google.com/go/workstations/logging/apiv1/loggingpb;loggingpb'
    _globals['_WORKSTATIONEVENT']._serialized_start = 99
    _globals['_WORKSTATIONEVENT']._serialized_end = 311
    _globals['_VMASSIGNMENTEVENT']._serialized_start = 313
    _globals['_VMASSIGNMENTEVENT']._serialized_end = 344
    _globals['_DISKASSIGNMENTEVENT']._serialized_start = 346
    _globals['_DISKASSIGNMENTEVENT']._serialized_end = 381