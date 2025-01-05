"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/kernel_rootkit.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/securitycenter/v1/kernel_rootkit.proto\x12\x1egoogle.cloud.securitycenter.v1"\xd7\x02\n\rKernelRootkit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x1cunexpected_code_modification\x18\x02 \x01(\x08\x12.\n&unexpected_read_only_data_modification\x18\x03 \x01(\x08\x12!\n\x19unexpected_ftrace_handler\x18\x04 \x01(\x08\x12!\n\x19unexpected_kprobe_handler\x18\x05 \x01(\x08\x12$\n\x1cunexpected_kernel_code_pages\x18\x06 \x01(\x08\x12&\n\x1eunexpected_system_call_handler\x18\x07 \x01(\x08\x12$\n\x1cunexpected_interrupt_handler\x18\x08 \x01(\x08\x12(\n unexpected_processes_in_runqueue\x18\t \x01(\x08B\xec\x01\n"com.google.cloud.securitycenter.v1B\x12KernelRootkitProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.kernel_rootkit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x12KernelRootkitProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_KERNELROOTKIT']._serialized_start = 88
    _globals['_KERNELROOTKIT']._serialized_end = 431