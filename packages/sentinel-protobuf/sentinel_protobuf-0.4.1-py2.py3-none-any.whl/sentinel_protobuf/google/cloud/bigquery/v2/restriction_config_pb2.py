"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/restriction_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/v2/restriction_config.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xb4\x01\n\x11RestrictionConfig\x12N\n\x04type\x18\x01 \x01(\x0e2;.google.cloud.bigquery.v2.RestrictionConfig.RestrictionTypeB\x03\xe0A\x03"O\n\x0fRestrictionType\x12 \n\x1cRESTRICTION_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16RESTRICTED_DATA_EGRESS\x10\x01Br\n\x1ccom.google.cloud.bigquery.v2B\x16RestrictionConfigProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.restriction_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x16RestrictionConfigProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_RESTRICTIONCONFIG'].fields_by_name['type']._loaded_options = None
    _globals['_RESTRICTIONCONFIG'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_RESTRICTIONCONFIG']._serialized_start = 113
    _globals['_RESTRICTIONCONFIG']._serialized_end = 293
    _globals['_RESTRICTIONCONFIG_RESTRICTIONTYPE']._serialized_start = 214
    _globals['_RESTRICTIONCONFIG_RESTRICTIONTYPE']._serialized_end = 293