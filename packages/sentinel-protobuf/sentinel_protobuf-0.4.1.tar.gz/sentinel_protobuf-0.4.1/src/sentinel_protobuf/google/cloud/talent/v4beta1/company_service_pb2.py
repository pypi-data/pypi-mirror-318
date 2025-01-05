"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/company_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2
from .....google.cloud.talent.v4beta1 import company_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_company__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/talent/v4beta1/company_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/talent/v4beta1/common.proto\x1a)google/cloud/talent/v4beta1/company.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x87\x01\n\x14CreateCompanyRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company\x12:\n\x07company\x18\x02 \x01(\x0b2$.google.cloud.talent.v4beta1.CompanyB\x03\xe0A\x02"F\n\x11GetCompanyRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company"\x83\x01\n\x14UpdateCompanyRequest\x12:\n\x07company\x18\x01 \x01(\x0b2$.google.cloud.talent.v4beta1.CompanyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"I\n\x14DeleteCompanyRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company"\x8d\x01\n\x14ListCompaniesRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x19\n\x11require_open_jobs\x18\x04 \x01(\x08"\xaa\x01\n\x15ListCompaniesResponse\x127\n\tcompanies\x18\x01 \x03(\x0b2$.google.cloud.talent.v4beta1.Company\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12?\n\x08metadata\x18\x03 \x01(\x0b2-.google.cloud.talent.v4beta1.ResponseMetadata2\xd2\t\n\x0eCompanyService\x12\xe3\x01\n\rCreateCompany\x121.google.cloud.talent.v4beta1.CreateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"y\xdaA\x0eparent,company\x82\xd3\xe4\x93\x02b"0/v4beta1/{parent=projects/*/tenants/*}/companies:\x01*Z+"&/v4beta1/{parent=projects/*}/companies:\x01*\x12\xcd\x01\n\nGetCompany\x12..google.cloud.talent.v4beta1.GetCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"i\xdaA\x04name\x82\xd3\xe4\x93\x02\\\x120/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\x12&/v4beta1/{name=projects/*/companies/*}\x12\xed\x01\n\rUpdateCompany\x121.google.cloud.talent.v4beta1.UpdateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"\x82\x01\xdaA\x07company\x82\xd3\xe4\x93\x02r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\x01*Z32./v4beta1/{company.name=projects/*/companies/*}:\x01*\x12\xc5\x01\n\rDeleteCompany\x121.google.cloud.talent.v4beta1.DeleteCompanyRequest\x1a\x16.google.protobuf.Empty"i\xdaA\x04name\x82\xd3\xe4\x93\x02\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}\x12\xe3\x01\n\rListCompanies\x121.google.cloud.talent.v4beta1.ListCompaniesRequest\x1a2.google.cloud.talent.v4beta1.ListCompaniesResponse"k\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x120/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\x12&/v4beta1/{parent=projects/*}/companies\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBw\n\x1fcom.google.cloud.talent.v4beta1B\x13CompanyServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.company_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x13CompanyServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company'
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_CREATECOMPANYREQUEST'].fields_by_name['company']._serialized_options = b'\xe0A\x02'
    _globals['_GETCOMPANYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOMPANYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_UPDATECOMPANYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_UPDATECOMPANYREQUEST'].fields_by_name['company']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECOMPANYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECOMPANYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_LISTCOMPANIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOMPANIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company'
    _globals['_COMPANYSERVICE']._loaded_options = None
    _globals['_COMPANYSERVICE']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_COMPANYSERVICE'].methods_by_name['CreateCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['CreateCompany']._serialized_options = b'\xdaA\x0eparent,company\x82\xd3\xe4\x93\x02b"0/v4beta1/{parent=projects/*/tenants/*}/companies:\x01*Z+"&/v4beta1/{parent=projects/*}/companies:\x01*'
    _globals['_COMPANYSERVICE'].methods_by_name['GetCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['GetCompany']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\\\x120/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\x12&/v4beta1/{name=projects/*/companies/*}'
    _globals['_COMPANYSERVICE'].methods_by_name['UpdateCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['UpdateCompany']._serialized_options = b'\xdaA\x07company\x82\xd3\xe4\x93\x02r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\x01*Z32./v4beta1/{company.name=projects/*/companies/*}:\x01*'
    _globals['_COMPANYSERVICE'].methods_by_name['DeleteCompany']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['DeleteCompany']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}'
    _globals['_COMPANYSERVICE'].methods_by_name['ListCompanies']._loaded_options = None
    _globals['_COMPANYSERVICE'].methods_by_name['ListCompanies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x120/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\x12&/v4beta1/{parent=projects/*}/companies'
    _globals['_CREATECOMPANYREQUEST']._serialized_start = 346
    _globals['_CREATECOMPANYREQUEST']._serialized_end = 481
    _globals['_GETCOMPANYREQUEST']._serialized_start = 483
    _globals['_GETCOMPANYREQUEST']._serialized_end = 553
    _globals['_UPDATECOMPANYREQUEST']._serialized_start = 556
    _globals['_UPDATECOMPANYREQUEST']._serialized_end = 687
    _globals['_DELETECOMPANYREQUEST']._serialized_start = 689
    _globals['_DELETECOMPANYREQUEST']._serialized_end = 762
    _globals['_LISTCOMPANIESREQUEST']._serialized_start = 765
    _globals['_LISTCOMPANIESREQUEST']._serialized_end = 906
    _globals['_LISTCOMPANIESRESPONSE']._serialized_start = 909
    _globals['_LISTCOMPANIESRESPONSE']._serialized_end = 1079
    _globals['_COMPANYSERVICE']._serialized_start = 1082
    _globals['_COMPANYSERVICE']._serialized_end = 2316