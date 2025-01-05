"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/company.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import common_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/talent/v4/company.proto\x12\x16google.cloud.talent.v4\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/talent/v4/common.proto"\xc8\x04\n\x07Company\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bexternal_id\x18\x03 \x01(\tB\x03\xe0A\x02\x121\n\x04size\x18\x04 \x01(\x0e2#.google.cloud.talent.v4.CompanySize\x12\x1c\n\x14headquarters_address\x18\x05 \x01(\t\x12\x15\n\rhiring_agency\x18\x06 \x01(\x08\x12\x10\n\x08eeo_text\x18\x07 \x01(\t\x12\x13\n\x0bwebsite_uri\x18\x08 \x01(\t\x12\x17\n\x0fcareer_site_uri\x18\t \x01(\t\x12\x11\n\timage_uri\x18\n \x01(\t\x124\n(keyword_searchable_job_custom_attributes\x18\x0b \x03(\tB\x02\x18\x01\x12F\n\x0cderived_info\x18\x0c \x01(\x0b2+.google.cloud.talent.v4.Company.DerivedInfoB\x03\xe0A\x03\x12\x16\n\tsuspended\x18\r \x01(\x08B\x03\xe0A\x03\x1aN\n\x0bDerivedInfo\x12?\n\x15headquarters_location\x18\x01 \x01(\x0b2 .google.cloud.talent.v4.Location:Y\xeaAV\n\x1bjobs.googleapis.com/Company\x127projects/{project}/tenants/{tenant}/companies/{company}Bf\n\x1acom.google.cloud.talent.v4B\x0cCompanyProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.company_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x0cCompanyProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_COMPANY'].fields_by_name['display_name']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_COMPANY'].fields_by_name['external_id']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['external_id']._serialized_options = b'\xe0A\x02'
    _globals['_COMPANY'].fields_by_name['keyword_searchable_job_custom_attributes']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['keyword_searchable_job_custom_attributes']._serialized_options = b'\x18\x01'
    _globals['_COMPANY'].fields_by_name['derived_info']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['derived_info']._serialized_options = b'\xe0A\x03'
    _globals['_COMPANY'].fields_by_name['suspended']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['suspended']._serialized_options = b'\xe0A\x03'
    _globals['_COMPANY']._loaded_options = None
    _globals['_COMPANY']._serialized_options = b'\xeaAV\n\x1bjobs.googleapis.com/Company\x127projects/{project}/tenants/{tenant}/companies/{company}'
    _globals['_COMPANY']._serialized_start = 162
    _globals['_COMPANY']._serialized_end = 746
    _globals['_COMPANY_DERIVEDINFO']._serialized_start = 577
    _globals['_COMPANY_DERIVEDINFO']._serialized_end = 655