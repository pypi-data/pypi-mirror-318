"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1p1beta1/security_marks.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/securitycenter/v1p1beta1/security_marks.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a\x19google/api/resource.proto"\xdc\x04\n\rSecurityMarks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x05marks\x18\x02 \x03(\x0b2?.google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry\x12\x16\n\x0ecanonical_name\x18\x03 \x01(\t\x1a,\n\nMarksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xa6\x03\xeaA\xa2\x03\n+securitycenter.googleapis.com/SecurityMarks\x129organizations/{organization}/assets/{asset}/securityMarks\x12Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarks\x12-folders/{folder}/assets/{asset}/securityMarks\x12/projects/{project}/assets/{asset}/securityMarks\x12Bfolders/{folder}/sources/{source}/findings/{finding}/securityMarks\x12Dprojects/{project}/sources/{source}/findings/{finding}/securityMarksB\xfb\x01\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1p1beta1.security_marks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1'
    _globals['_SECURITYMARKS_MARKSENTRY']._loaded_options = None
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_options = b'8\x01'
    _globals['_SECURITYMARKS']._loaded_options = None
    _globals['_SECURITYMARKS']._serialized_options = b'\xeaA\xa2\x03\n+securitycenter.googleapis.com/SecurityMarks\x129organizations/{organization}/assets/{asset}/securityMarks\x12Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarks\x12-folders/{folder}/assets/{asset}/securityMarks\x12/projects/{project}/assets/{asset}/securityMarks\x12Bfolders/{folder}/sources/{source}/findings/{finding}/securityMarks\x12Dprojects/{project}/sources/{source}/findings/{finding}/securityMarks'
    _globals['_SECURITYMARKS']._serialized_start = 129
    _globals['_SECURITYMARKS']._serialized_end = 733
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_start = 264
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_end = 308