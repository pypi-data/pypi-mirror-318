"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apphub/v1/attributes.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/apphub/v1/attributes.proto\x12\x16google.cloud.apphub.v1\x1a\x1fgoogle/api/field_behavior.proto"\xd4\x02\n\nAttributes\x12=\n\x0bcriticality\x18\x01 \x01(\x0b2#.google.cloud.apphub.v1.CriticalityB\x03\xe0A\x01\x12=\n\x0benvironment\x18\x02 \x01(\x0b2#.google.cloud.apphub.v1.EnvironmentB\x03\xe0A\x01\x12B\n\x10developer_owners\x18\x03 \x03(\x0b2#.google.cloud.apphub.v1.ContactInfoB\x03\xe0A\x01\x12A\n\x0foperator_owners\x18\x04 \x03(\x0b2#.google.cloud.apphub.v1.ContactInfoB\x03\xe0A\x01\x12A\n\x0fbusiness_owners\x18\x05 \x03(\x0b2#.google.cloud.apphub.v1.ContactInfoB\x03\xe0A\x01"\x9d\x01\n\x0bCriticality\x12;\n\x04type\x18\x03 \x01(\x0e2(.google.cloud.apphub.v1.Criticality.TypeB\x03\xe0A\x02"Q\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10MISSION_CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04"\xa0\x01\n\x0bEnvironment\x12;\n\x04type\x18\x02 \x01(\x0e2(.google.cloud.apphub.v1.Environment.TypeB\x03\xe0A\x02"T\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\x0b\n\x07STAGING\x10\x02\x12\x08\n\x04TEST\x10\x03\x12\x0f\n\x0bDEVELOPMENT\x10\x04"<\n\x0bContactInfo\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05email\x18\x02 \x01(\tB\x03\xe0A\x02B\xb1\x01\n\x1acom.google.cloud.apphub.v1B\x0fAttributesProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apphub.v1.attributes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apphub.v1B\x0fAttributesProtoP\x01Z2cloud.google.com/go/apphub/apiv1/apphubpb;apphubpb\xaa\x02\x16Google.Cloud.AppHub.V1\xca\x02\x16Google\\Cloud\\AppHub\\V1\xea\x02\x19Google::Cloud::AppHub::V1'
    _globals['_ATTRIBUTES'].fields_by_name['criticality']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['criticality']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['environment']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['environment']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['developer_owners']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['developer_owners']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['operator_owners']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['operator_owners']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['business_owners']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['business_owners']._serialized_options = b'\xe0A\x01'
    _globals['_CRITICALITY'].fields_by_name['type']._loaded_options = None
    _globals['_CRITICALITY'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT'].fields_by_name['type']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CONTACTINFO'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONTACTINFO'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CONTACTINFO'].fields_by_name['email']._loaded_options = None
    _globals['_CONTACTINFO'].fields_by_name['email']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES']._serialized_start = 101
    _globals['_ATTRIBUTES']._serialized_end = 441
    _globals['_CRITICALITY']._serialized_start = 444
    _globals['_CRITICALITY']._serialized_end = 601
    _globals['_CRITICALITY_TYPE']._serialized_start = 520
    _globals['_CRITICALITY_TYPE']._serialized_end = 601
    _globals['_ENVIRONMENT']._serialized_start = 604
    _globals['_ENVIRONMENT']._serialized_end = 764
    _globals['_ENVIRONMENT_TYPE']._serialized_start = 680
    _globals['_ENVIRONMENT_TYPE']._serialized_end = 764
    _globals['_CONTACTINFO']._serialized_start = 766
    _globals['_CONTACTINFO']._serialized_end = 826