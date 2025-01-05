"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/project.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/retail/v2beta/project.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf8\x03\n\x0bAlertConfig\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12K\n\x0ealert_policies\x18\x02 \x03(\x0b23.google.cloud.retail.v2beta.AlertConfig.AlertPolicy\x1a\xbd\x02\n\x0bAlertPolicy\x12\x13\n\x0balert_group\x18\x01 \x01(\t\x12W\n\renroll_status\x18\x02 \x01(\x0e2@.google.cloud.retail.v2beta.AlertConfig.AlertPolicy.EnrollStatus\x12Q\n\nrecipients\x18\x03 \x03(\x0b2=.google.cloud.retail.v2beta.AlertConfig.AlertPolicy.Recipient\x1a"\n\tRecipient\x12\x15\n\remail_address\x18\x01 \x01(\t"I\n\x0cEnrollStatus\x12\x1d\n\x19ENROLL_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENROLLED\x10\x01\x12\x0c\n\x08DECLINED\x10\x02:F\xeaAC\n!retail.googleapis.com/AlertConfig\x12\x1eprojects/{project}/alertConfigB\xcb\x01\n\x1ecom.google.cloud.retail.v2betaB\x0cProjectProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x0cProjectProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_ALERTCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ALERTCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ALERTCONFIG']._loaded_options = None
    _globals['_ALERTCONFIG']._serialized_options = b'\xeaAC\n!retail.googleapis.com/AlertConfig\x12\x1eprojects/{project}/alertConfig'
    _globals['_ALERTCONFIG']._serialized_start = 133
    _globals['_ALERTCONFIG']._serialized_end = 637
    _globals['_ALERTCONFIG_ALERTPOLICY']._serialized_start = 248
    _globals['_ALERTCONFIG_ALERTPOLICY']._serialized_end = 565
    _globals['_ALERTCONFIG_ALERTPOLICY_RECIPIENT']._serialized_start = 456
    _globals['_ALERTCONFIG_ALERTPOLICY_RECIPIENT']._serialized_end = 490
    _globals['_ALERTCONFIG_ALERTPOLICY_ENROLLSTATUS']._serialized_start = 492
    _globals['_ALERTCONFIG_ALERTPOLICY_ENROLLSTATUS']._serialized_end = 565