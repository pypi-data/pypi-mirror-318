"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/channel/v1/common.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/protobuf/any.proto"\xb0\x03\n\x07EduData\x12F\n\x0einstitute_type\x18\x01 \x01(\x0e2..google.cloud.channel.v1.EduData.InstituteType\x12F\n\x0einstitute_size\x18\x02 \x01(\x0e2..google.cloud.channel.v1.EduData.InstituteSize\x12\x0f\n\x07website\x18\x03 \x01(\t"H\n\rInstituteType\x12\x1e\n\x1aINSTITUTE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03K12\x10\x01\x12\x0e\n\nUNIVERSITY\x10\x02"\xb9\x01\n\rInstituteSize\x12\x1e\n\x1aINSTITUTE_SIZE_UNSPECIFIED\x10\x00\x12\x0e\n\nSIZE_1_100\x10\x01\x12\x10\n\x0cSIZE_101_500\x10\x02\x12\x11\n\rSIZE_501_1000\x10\x03\x12\x12\n\x0eSIZE_1001_2000\x10\x04\x12\x12\n\x0eSIZE_2001_5000\x10\x05\x12\x13\n\x0fSIZE_5001_10000\x10\x06\x12\x16\n\x12SIZE_10001_OR_MORE\x10\x07"\x80\x03\n\x11CloudIdentityInfo\x12N\n\rcustomer_type\x18\x01 \x01(\x0e27.google.cloud.channel.v1.CloudIdentityInfo.CustomerType\x12\x1b\n\x0eprimary_domain\x18\t \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12is_domain_verified\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x17\n\x0falternate_email\x18\x06 \x01(\t\x12\x14\n\x0cphone_number\x18\x07 \x01(\t\x12\x15\n\rlanguage_code\x18\x08 \x01(\t\x12\x1e\n\x11admin_console_uri\x18\n \x01(\tB\x03\xe0A\x03\x122\n\x08edu_data\x18\x16 \x01(\x0b2 .google.cloud.channel.v1.EduData"C\n\x0cCustomerType\x12\x1d\n\x19CUSTOMER_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06DOMAIN\x10\x01\x12\x08\n\x04TEAM\x10\x02"\x99\x01\n\x05Value\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12+\n\x0bproto_value\x18\x04 \x01(\x0b2\x14.google.protobuf.AnyH\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00B\x06\n\x04kind"C\n\tAdminUser\x12\r\n\x05email\x18\x01 \x01(\t\x12\x12\n\ngiven_name\x18\x02 \x01(\t\x12\x13\n\x0bfamily_name\x18\x03 \x01(\tBc\n\x1bcom.google.cloud.channel.v1B\x0bCommonProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x0bCommonProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['primary_domain']._loaded_options = None
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['primary_domain']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['is_domain_verified']._loaded_options = None
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['is_domain_verified']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['admin_console_uri']._loaded_options = None
    _globals['_CLOUDIDENTITYINFO'].fields_by_name['admin_console_uri']._serialized_options = b'\xe0A\x03'
    _globals['_EDUDATA']._serialized_start = 126
    _globals['_EDUDATA']._serialized_end = 558
    _globals['_EDUDATA_INSTITUTETYPE']._serialized_start = 298
    _globals['_EDUDATA_INSTITUTETYPE']._serialized_end = 370
    _globals['_EDUDATA_INSTITUTESIZE']._serialized_start = 373
    _globals['_EDUDATA_INSTITUTESIZE']._serialized_end = 558
    _globals['_CLOUDIDENTITYINFO']._serialized_start = 561
    _globals['_CLOUDIDENTITYINFO']._serialized_end = 945
    _globals['_CLOUDIDENTITYINFO_CUSTOMERTYPE']._serialized_start = 878
    _globals['_CLOUDIDENTITYINFO_CUSTOMERTYPE']._serialized_end = 945
    _globals['_VALUE']._serialized_start = 948
    _globals['_VALUE']._serialized_end = 1101
    _globals['_ADMINUSER']._serialized_start = 1103
    _globals['_ADMINUSER']._serialized_end = 1170