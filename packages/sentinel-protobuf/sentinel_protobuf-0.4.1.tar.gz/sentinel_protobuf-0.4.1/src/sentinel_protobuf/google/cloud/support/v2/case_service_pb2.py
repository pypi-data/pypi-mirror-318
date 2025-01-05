"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/case_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2 import case_pb2 as google_dot_cloud_dot_support_dot_v2_dot_case__pb2
from .....google.cloud.support.v2 import escalation_pb2 as google_dot_cloud_dot_support_dot_v2_dot_escalation__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/support/v2/case_service.proto\x12\x17google.cloud.support.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/cloud/support/v2/case.proto\x1a(google/cloud/support/v2/escalation.proto\x1a google/protobuf/field_mask.proto"H\n\x0eGetCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case"\x7f\n\x11CreateCaseRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case\x120\n\x04case\x18\x02 \x01(\x0b2\x1d.google.cloud.support.v2.CaseB\x03\xe0A\x02"\x83\x01\n\x10ListCasesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"Z\n\x11ListCasesResponse\x12,\n\x05cases\x18\x01 \x03(\x0b2\x1d.google.cloud.support.v2.Case\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x12SearchCasesRequest\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\r\n\x05query\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\\\n\x13SearchCasesResponse\x12,\n\x05cases\x18\x01 \x03(\x0b2\x1d.google.cloud.support.v2.Case\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x86\x01\n\x13EscalateCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x127\n\nescalation\x18\x02 \x01(\x0b2#.google.cloud.support.v2.Escalation"v\n\x11UpdateCaseRequest\x120\n\x04case\x18\x01 \x01(\x0b2\x1d.google.cloud.support.v2.CaseB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"J\n\x10CloseCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case"X\n SearchCaseClassificationsRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x87\x01\n!SearchCaseClassificationsResponse\x12I\n\x14case_classifications\x18\x01 \x03(\x0b2+.google.cloud.support.v2.CaseClassification\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcf\x0c\n\x0bCaseService\x12\xa5\x01\n\x07GetCase\x12\'.google.cloud.support.v2.GetCaseRequest\x1a\x1d.google.cloud.support.v2.Case"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12\x1d/v2/{name=projects/*/cases/*}Z$\x12"/v2/{name=organizations/*/cases/*}\x12\xb8\x01\n\tListCases\x12).google.cloud.support.v2.ListCasesRequest\x1a*.google.cloud.support.v2.ListCasesResponse"T\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12\x1d/v2/{parent=projects/*}/casesZ$\x12"/v2/{parent=organizations/*}/cases\x12\xc3\x01\n\x0bSearchCases\x12+.google.cloud.support.v2.SearchCasesRequest\x1a,.google.cloud.support.v2.SearchCasesResponse"Y\x82\xd3\xe4\x93\x02S\x12$/v2/{parent=projects/*}/cases:searchZ+\x12)/v2/{parent=organizations/*}/cases:search\x12\xbe\x01\n\nCreateCase\x12*.google.cloud.support.v2.CreateCaseRequest\x1a\x1d.google.cloud.support.v2.Case"e\xdaA\x0bparent,case\x82\xd3\xe4\x93\x02Q"\x1d/v2/{parent=projects/*}/cases:\x04caseZ*""/v2/{parent=organizations/*}/cases:\x04case\x12\xcd\x01\n\nUpdateCase\x12*.google.cloud.support.v2.UpdateCaseRequest\x1a\x1d.google.cloud.support.v2.Case"t\xdaA\x10case,update_mask\x82\xd3\xe4\x93\x02[2"/v2/{case.name=projects/*/cases/*}:\x04caseZ/2\'/v2/{case.name=organizations/*/cases/*}:\x04case\x12\xc0\x01\n\x0cEscalateCase\x12,.google.cloud.support.v2.EscalateCaseRequest\x1a\x1d.google.cloud.support.v2.Case"c\x82\xd3\xe4\x93\x02]"&/v2/{name=projects/*/cases/*}:escalate:\x01*Z0"+/v2/{name=organizations/*/cases/*}:escalate:\x01*\x12\xb4\x01\n\tCloseCase\x12).google.cloud.support.v2.CloseCaseRequest\x1a\x1d.google.cloud.support.v2.Case"]\x82\xd3\xe4\x93\x02W"#/v2/{name=projects/*/cases/*}:close:\x01*Z-"(/v2/{name=organizations/*/cases/*}:close:\x01*\x12\xba\x01\n\x19SearchCaseClassifications\x129.google.cloud.support.v2.SearchCaseClassificationsRequest\x1a:.google.cloud.support.v2.SearchCaseClassificationsResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/v2/caseClassifications:search\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb9\x01\n\x1bcom.google.cloud.support.v2B\x10CaseServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.case_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\x10CaseServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_GETCASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case'
    _globals['_CREATECASEREQUEST'].fields_by_name['case']._loaded_options = None
    _globals['_CREATECASEREQUEST'].fields_by_name['case']._serialized_options = b'\xe0A\x02'
    _globals['_LISTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case'
    _globals['_ESCALATECASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ESCALATECASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_UPDATECASEREQUEST'].fields_by_name['case']._loaded_options = None
    _globals['_UPDATECASEREQUEST'].fields_by_name['case']._serialized_options = b'\xe0A\x02'
    _globals['_CLOSECASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CLOSECASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CASESERVICE']._loaded_options = None
    _globals['_CASESERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CASESERVICE'].methods_by_name['GetCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['GetCase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12\x1d/v2/{name=projects/*/cases/*}Z$\x12"/v2/{name=organizations/*/cases/*}'
    _globals['_CASESERVICE'].methods_by_name['ListCases']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['ListCases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12\x1d/v2/{parent=projects/*}/casesZ$\x12"/v2/{parent=organizations/*}/cases'
    _globals['_CASESERVICE'].methods_by_name['SearchCases']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['SearchCases']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12$/v2/{parent=projects/*}/cases:searchZ+\x12)/v2/{parent=organizations/*}/cases:search'
    _globals['_CASESERVICE'].methods_by_name['CreateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['CreateCase']._serialized_options = b'\xdaA\x0bparent,case\x82\xd3\xe4\x93\x02Q"\x1d/v2/{parent=projects/*}/cases:\x04caseZ*""/v2/{parent=organizations/*}/cases:\x04case'
    _globals['_CASESERVICE'].methods_by_name['UpdateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['UpdateCase']._serialized_options = b'\xdaA\x10case,update_mask\x82\xd3\xe4\x93\x02[2"/v2/{case.name=projects/*/cases/*}:\x04caseZ/2\'/v2/{case.name=organizations/*/cases/*}:\x04case'
    _globals['_CASESERVICE'].methods_by_name['EscalateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['EscalateCase']._serialized_options = b'\x82\xd3\xe4\x93\x02]"&/v2/{name=projects/*/cases/*}:escalate:\x01*Z0"+/v2/{name=organizations/*/cases/*}:escalate:\x01*'
    _globals['_CASESERVICE'].methods_by_name['CloseCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['CloseCase']._serialized_options = b'\x82\xd3\xe4\x93\x02W"#/v2/{name=projects/*/cases/*}:close:\x01*Z-"(/v2/{name=organizations/*/cases/*}:close:\x01*'
    _globals['_CASESERVICE'].methods_by_name['SearchCaseClassifications']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['SearchCaseClassifications']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/v2/caseClassifications:search'
    _globals['_GETCASEREQUEST']._serialized_start = 298
    _globals['_GETCASEREQUEST']._serialized_end = 370
    _globals['_CREATECASEREQUEST']._serialized_start = 372
    _globals['_CREATECASEREQUEST']._serialized_end = 499
    _globals['_LISTCASESREQUEST']._serialized_start = 502
    _globals['_LISTCASESREQUEST']._serialized_end = 633
    _globals['_LISTCASESRESPONSE']._serialized_start = 635
    _globals['_LISTCASESRESPONSE']._serialized_end = 725
    _globals['_SEARCHCASESREQUEST']._serialized_start = 727
    _globals['_SEARCHCASESREQUEST']._serialized_end = 817
    _globals['_SEARCHCASESRESPONSE']._serialized_start = 819
    _globals['_SEARCHCASESRESPONSE']._serialized_end = 911
    _globals['_ESCALATECASEREQUEST']._serialized_start = 914
    _globals['_ESCALATECASEREQUEST']._serialized_end = 1048
    _globals['_UPDATECASEREQUEST']._serialized_start = 1050
    _globals['_UPDATECASEREQUEST']._serialized_end = 1168
    _globals['_CLOSECASEREQUEST']._serialized_start = 1170
    _globals['_CLOSECASEREQUEST']._serialized_end = 1244
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST']._serialized_start = 1246
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST']._serialized_end = 1334
    _globals['_SEARCHCASECLASSIFICATIONSRESPONSE']._serialized_start = 1337
    _globals['_SEARCHCASECLASSIFICATIONSRESPONSE']._serialized_end = 1472
    _globals['_CASESERVICE']._serialized_start = 1475
    _globals['_CASESERVICE']._serialized_end = 3090