"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/process.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.securitycenter.v1 import file_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/securitycenter/v1/process.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a)google/cloud/securitycenter/v1/file.proto"\xf5\x02\n\x07Process\x12\x0c\n\x04name\x18\x0c \x01(\t\x124\n\x06binary\x18\x03 \x01(\x0b2$.google.cloud.securitycenter.v1.File\x127\n\tlibraries\x18\x04 \x03(\x0b2$.google.cloud.securitycenter.v1.File\x124\n\x06script\x18\x05 \x01(\x0b2$.google.cloud.securitycenter.v1.File\x12\x0c\n\x04args\x18\x06 \x03(\t\x12\x1b\n\x13arguments_truncated\x18\x07 \x01(\x08\x12J\n\renv_variables\x18\x08 \x03(\x0b23.google.cloud.securitycenter.v1.EnvironmentVariable\x12\x1f\n\x17env_variables_truncated\x18\t \x01(\x08\x12\x0b\n\x03pid\x18\n \x01(\x03\x12\x12\n\nparent_pid\x18\x0b \x01(\x03"0\n\x13EnvironmentVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\tB\xe6\x01\n"com.google.cloud.securitycenter.v1B\x0cProcessProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.process_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0cProcessProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_PROCESS']._serialized_start = 124
    _globals['_PROCESS']._serialized_end = 497
    _globals['_ENVIRONMENTVARIABLE']._serialized_start = 499
    _globals['_ENVIRONMENTVARIABLE']._serialized_end = 547