"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1beta1/security_marks.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/securitycenter/v1beta1/security_marks.proto\x12#google.cloud.securitycenter.v1beta1\x1a\x19google/api/resource.proto"\xd8\x02\n\rSecurityMarks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\x05marks\x18\x02 \x03(\x0b2=.google.cloud.securitycenter.v1beta1.SecurityMarks.MarksEntry\x1a,\n\nMarksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xbc\x01\xeaA\xb8\x01\n+securitycenter.googleapis.com/SecurityMarks\x129organizations/{organization}/assets/{asset}/securityMarks\x12Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarksB|\n\'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1beta1.security_marks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpb"
    _globals['_SECURITYMARKS_MARKSENTRY']._loaded_options = None
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_options = b'8\x01'
    _globals['_SECURITYMARKS']._loaded_options = None
    _globals['_SECURITYMARKS']._serialized_options = b'\xeaA\xb8\x01\n+securitycenter.googleapis.com/SecurityMarks\x129organizations/{organization}/assets/{asset}/securityMarks\x12Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarks'
    _globals['_SECURITYMARKS']._serialized_start = 125
    _globals['_SECURITYMARKS']._serialized_end = 469
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_start = 234
    _globals['_SECURITYMARKS_MARKSENTRY']._serialized_end = 278