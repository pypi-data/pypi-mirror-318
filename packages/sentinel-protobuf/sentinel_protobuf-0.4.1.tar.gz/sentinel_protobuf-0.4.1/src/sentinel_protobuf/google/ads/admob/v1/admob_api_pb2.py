"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admob/v1/admob_api.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admob.v1 import admob_resources_pb2 as google_dot_ads_dot_admob_dot_v1_dot_admob__resources__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/ads/admob/v1/admob_api.proto\x12\x13google.ads.admob.v1\x1a)google/ads/admob/v1/admob_resources.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"*\n\x1aGetPublisherAccountRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"E\n\x1cListPublisherAccountsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"p\n\x1dListPublisherAccountsResponse\x126\n\x07account\x18\x01 \x03(\x0b2%.google.ads.admob.v1.PublisherAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"o\n\x1eGenerateMediationReportRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12=\n\x0breport_spec\x18\x02 \x01(\x0b2(.google.ads.admob.v1.MediationReportSpec"\xc5\x01\n\x1fGenerateMediationReportResponse\x123\n\x06header\x18\x01 \x01(\x0b2!.google.ads.admob.v1.ReportHeaderH\x00\x12-\n\x03row\x18\x02 \x01(\x0b2\x1e.google.ads.admob.v1.ReportRowH\x00\x123\n\x06footer\x18\x03 \x01(\x0b2!.google.ads.admob.v1.ReportFooterH\x00B\t\n\x07payload"k\n\x1cGenerateNetworkReportRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12;\n\x0breport_spec\x18\x02 \x01(\x0b2&.google.ads.admob.v1.NetworkReportSpec"\xc3\x01\n\x1dGenerateNetworkReportResponse\x123\n\x06header\x18\x01 \x01(\x0b2!.google.ads.admob.v1.ReportHeaderH\x00\x12-\n\x03row\x18\x02 \x01(\x0b2\x1e.google.ads.admob.v1.ReportRowH\x00\x123\n\x06footer\x18\x03 \x01(\x0b2!.google.ads.admob.v1.ReportFooterH\x00B\t\n\x07payload2\x83\x06\n\x08AdMobApi\x12\x93\x01\n\x13GetPublisherAccount\x12/.google.ads.admob.v1.GetPublisherAccountRequest\x1a%.google.ads.admob.v1.PublisherAccount"$\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=accounts/*}\x12\x94\x01\n\x15ListPublisherAccounts\x121.google.ads.admob.v1.ListPublisherAccountsRequest\x1a2.google.ads.admob.v1.ListPublisherAccountsResponse"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/accounts\x12\xbb\x01\n\x15GenerateNetworkReport\x121.google.ads.admob.v1.GenerateNetworkReportRequest\x1a2.google.ads.admob.v1.GenerateNetworkReportResponse"9\x82\xd3\xe4\x93\x023"./v1/{parent=accounts/*}/networkReport:generate:\x01*0\x01\x12\xc3\x01\n\x17GenerateMediationReport\x123.google.ads.admob.v1.GenerateMediationReportRequest\x1a4.google.ads.admob.v1.GenerateMediationReportResponse";\x82\xd3\xe4\x93\x025"0/v1/{parent=accounts/*}/mediationReport:generate:\x01*0\x01\x1aF\xcaA\x14admob.googleapis.com\xd2A,https://www.googleapis.com/auth/admob.reportBb\n\x17com.google.ads.admob.v1B\rAdMobApiProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admobb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admob.v1.admob_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.ads.admob.v1B\rAdMobApiProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admob'
    _globals['_ADMOBAPI']._loaded_options = None
    _globals['_ADMOBAPI']._serialized_options = b'\xcaA\x14admob.googleapis.com\xd2A,https://www.googleapis.com/auth/admob.report'
    _globals['_ADMOBAPI'].methods_by_name['GetPublisherAccount']._loaded_options = None
    _globals['_ADMOBAPI'].methods_by_name['GetPublisherAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=accounts/*}'
    _globals['_ADMOBAPI'].methods_by_name['ListPublisherAccounts']._loaded_options = None
    _globals['_ADMOBAPI'].methods_by_name['ListPublisherAccounts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/accounts'
    _globals['_ADMOBAPI'].methods_by_name['GenerateNetworkReport']._loaded_options = None
    _globals['_ADMOBAPI'].methods_by_name['GenerateNetworkReport']._serialized_options = b'\x82\xd3\xe4\x93\x023"./v1/{parent=accounts/*}/networkReport:generate:\x01*'
    _globals['_ADMOBAPI'].methods_by_name['GenerateMediationReport']._loaded_options = None
    _globals['_ADMOBAPI'].methods_by_name['GenerateMediationReport']._serialized_options = b'\x82\xd3\xe4\x93\x025"0/v1/{parent=accounts/*}/mediationReport:generate:\x01*'
    _globals['_GETPUBLISHERACCOUNTREQUEST']._serialized_start = 218
    _globals['_GETPUBLISHERACCOUNTREQUEST']._serialized_end = 260
    _globals['_LISTPUBLISHERACCOUNTSREQUEST']._serialized_start = 262
    _globals['_LISTPUBLISHERACCOUNTSREQUEST']._serialized_end = 331
    _globals['_LISTPUBLISHERACCOUNTSRESPONSE']._serialized_start = 333
    _globals['_LISTPUBLISHERACCOUNTSRESPONSE']._serialized_end = 445
    _globals['_GENERATEMEDIATIONREPORTREQUEST']._serialized_start = 447
    _globals['_GENERATEMEDIATIONREPORTREQUEST']._serialized_end = 558
    _globals['_GENERATEMEDIATIONREPORTRESPONSE']._serialized_start = 561
    _globals['_GENERATEMEDIATIONREPORTRESPONSE']._serialized_end = 758
    _globals['_GENERATENETWORKREPORTREQUEST']._serialized_start = 760
    _globals['_GENERATENETWORKREPORTREQUEST']._serialized_end = 867
    _globals['_GENERATENETWORKREPORTRESPONSE']._serialized_start = 870
    _globals['_GENERATENETWORKREPORTRESPONSE']._serialized_end = 1065
    _globals['_ADMOBAPI']._serialized_start = 1068
    _globals['_ADMOBAPI']._serialized_end = 1839