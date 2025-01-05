"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/company_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import common_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_common__pb2
from .....google.cloud.talent.v4 import company_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_company__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/talent/v4/company_service.proto\x12\x16google.cloud.talent.v4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/talent/v4/common.proto\x1a$google/cloud/talent/v4/company.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x81\x01\n\x14CreateCompanyRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant\x125\n\x07company\x18\x02 \x01(\x0b2\x1f.google.cloud.talent.v4.CompanyB\x03\xe0A\x02"F\n\x11GetCompanyRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company"~\n\x14UpdateCompanyRequest\x125\n\x07company\x18\x01 \x01(\x0b2\x1f.google.cloud.talent.v4.CompanyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"I\n\x14DeleteCompanyRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company"\x8c\x01\n\x14ListCompaniesRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x19\n\x11require_open_jobs\x18\x04 \x01(\x08"\xa0\x01\n\x15ListCompaniesResponse\x122\n\tcompanies\x18\x01 \x03(\x0b2\x1f.google.cloud.talent.v4.Company\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12:\n\x08metadata\x18\x03 \x01(\x0b2(.google.cloud.talent.v4.ResponseMetadata2\xc3\x07\n\x0eCompanyService\x12\xad\x01\n\rCreateCompany\x12,.google.cloud.talent.v4.CreateCompanyRequest\x1a\x1f.google.cloud.talent.v4.Company"M\xdaA\x0eparent,company\x82\xd3\xe4\x93\x026"+/v4/{parent=projects/*/tenants/*}/companies:\x07company\x12\x94\x01\n\nGetCompany\x12).google.cloud.talent.v4.GetCompanyRequest\x1a\x1f.google.cloud.talent.v4.Company":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v4/{name=projects/*/tenants/*/companies/*}\x12\xba\x01\n\rUpdateCompany\x12,.google.cloud.talent.v4.UpdateCompanyRequest\x1a\x1f.google.cloud.talent.v4.Company"Z\xdaA\x13company,update_mask\x82\xd3\xe4\x93\x02>23/v4/{company.name=projects/*/tenants/*/companies/*}:\x07company\x12\x91\x01\n\rDeleteCompany\x12,.google.cloud.talent.v4.DeleteCompanyRequest\x1a\x16.google.protobuf.Empty":\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v4/{name=projects/*/tenants/*/companies/*}\x12\xaa\x01\n\rListCompanies\x12,.google.cloud.talent.v4.ListCompaniesRequest\x1a-.google.cloud.talent.v4.ListCompaniesResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v4/{parent=projects/*/tenants/*}/companies\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBm\n\x1acom.google.cloud.talent.v4B\x13CompanyServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.company_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x13CompanyServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['company']._serialized_options = b'\xe0A\x02'
    _globals['_GETCOMPANYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOMPANYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_UPDATECOMPANYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_UPDATECOMPANYREQUEST'].fields_by_name['company']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECOMPANYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECOMPANYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_LISTCOMPANIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOMPANIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_COMPANYSERVICE']._loaded_options = None
    _globals['_COMPANYSERVICE']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_COMPANYSERVICE'].methods_by_name['CreateCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['CreateCompany']._serialized_options = b'\xdaA\x0eparent,company\x82\xd3\xe4\x93\x026"+/v4/{parent=projects/*/tenants/*}/companies:\x07company'
    _globals['_COMPANYSERVICE'].methods_by_name['GetCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['GetCompany']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v4/{name=projects/*/tenants/*/companies/*}'
    _globals['_COMPANYSERVICE'].methods_by_name['UpdateCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['UpdateCompany']._serialized_options = b'\xdaA\x13company,update_mask\x82\xd3\xe4\x93\x02>23/v4/{company.name=projects/*/tenants/*/companies/*}:\x07company'
    _globals['_COMPANYSERVICE'].methods_by_name['DeleteCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['DeleteCompany']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v4/{name=projects/*/tenants/*/companies/*}'
    _globals['_COMPANYSERVICE'].methods_by_name['ListCompanies']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['ListCompanies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v4/{parent=projects/*/tenants/*}/companies'
    _globals['_CREATECOMPANYREQUEST']._serialized_start = 326
    _globals['_CREATECOMPANYREQUEST']._serialized_end = 455
    _globals['_GETCOMPANYREQUEST']._serialized_start = 457
    _globals['_GETCOMPANYREQUEST']._serialized_end = 527
    _globals['_UPDATECOMPANYREQUEST']._serialized_start = 529
    _globals['_UPDATECOMPANYREQUEST']._serialized_end = 655
    _globals['_DELETECOMPANYREQUEST']._serialized_start = 657
    _globals['_DELETECOMPANYREQUEST']._serialized_end = 730
    _globals['_LISTCOMPANIESREQUEST']._serialized_start = 733
    _globals['_LISTCOMPANIESREQUEST']._serialized_end = 873
    _globals['_LISTCOMPANIESRESPONSE']._serialized_start = 876
    _globals['_LISTCOMPANIESRESPONSE']._serialized_end = 1036
    _globals['_COMPANYSERVICE']._serialized_start = 1039
    _globals['_COMPANYSERVICE']._serialized_end = 2002