"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/logging/patch_job_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/osconfig/logging/patch_job_log.proto\x12\x1dgoogle.cloud.osconfig.logging\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x07\n\x14PatchJobCompletedLog\x12\x11\n\tpatch_job\x18\x01 \x01(\t\x12H\n\x05state\x18\x02 \x01(\x0e29.google.cloud.osconfig.logging.PatchJobCompletedLog.State\x12l\n\x18instance_details_summary\x18\x03 \x01(\x0b2J.google.cloud.osconfig.logging.PatchJobCompletedLog.InstanceDetailsSummary\x12\x0f\n\x07dry_run\x18\x04 \x01(\x08\x12\x15\n\rerror_message\x18\x05 \x01(\t\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\xdd\x03\n\x16InstanceDetailsSummary\x12\x19\n\x11instances_pending\x18\x01 \x01(\x03\x12\x1a\n\x12instances_inactive\x18\x02 \x01(\x03\x12\x1a\n\x12instances_notified\x18\x03 \x01(\x03\x12\x19\n\x11instances_started\x18\x04 \x01(\x03\x12%\n\x1dinstances_downloading_patches\x18\x05 \x01(\x03\x12"\n\x1ainstances_applying_patches\x18\x06 \x01(\x03\x12\x1b\n\x13instances_rebooting\x18\x07 \x01(\x03\x12\x1b\n\x13instances_succeeded\x18\x08 \x01(\x03\x12+\n#instances_succeeded_reboot_required\x18\t \x01(\x03\x12\x18\n\x10instances_failed\x18\n \x01(\x03\x12\x17\n\x0finstances_acked\x18\x0b \x01(\x03\x12\x1b\n\x13instances_timed_out\x18\x0c \x01(\x03\x12(\n instances_running_pre_patch_step\x18\r \x01(\x03\x12)\n!instances_running_post_patch_step\x18\x0e \x01(\x03"\x95\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x13\n\x0fINSTANCE_LOOKUP\x10\x02\x12\x0c\n\x08PATCHING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x19\n\x15COMPLETED_WITH_ERRORS\x10\x05\x12\x0c\n\x08CANCELED\x10\x06\x12\r\n\tTIMED_OUT\x10\x07Bq\n!com.google.cloud.osconfig.loggingB\x10PatchJobLogProtoP\x01Z8cloud.google.com/go/osconfig/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.logging.patch_job_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.osconfig.loggingB\x10PatchJobLogProtoP\x01Z8cloud.google.com/go/osconfig/logging/loggingpb;loggingpb'
    _globals['_PATCHJOBCOMPLETEDLOG']._serialized_start = 118
    _globals['_PATCHJOBCOMPLETEDLOG']._serialized_end = 1113
    _globals['_PATCHJOBCOMPLETEDLOG_INSTANCEDETAILSSUMMARY']._serialized_start = 484
    _globals['_PATCHJOBCOMPLETEDLOG_INSTANCEDETAILSSUMMARY']._serialized_end = 961
    _globals['_PATCHJOBCOMPLETEDLOG_STATE']._serialized_start = 964
    _globals['_PATCHJOBCOMPLETEDLOG_STATE']._serialized_end = 1113