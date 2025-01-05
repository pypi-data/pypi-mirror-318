"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/datasources/v1beta/fileuploads.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/shopping/merchant/datasources/v1beta/fileuploads.proto\x12+google.shopping.merchant.datasources.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8a\x07\n\nFileUpload\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1b\n\x0edata_source_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12f\n\x10processing_state\x18\x03 \x01(\x0e2G.google.shopping.merchant.datasources.v1beta.FileUpload.ProcessingStateB\x03\xe0A\x03\x12R\n\x06issues\x18\x04 \x03(\x0b2=.google.shopping.merchant.datasources.v1beta.FileUpload.IssueB\x03\xe0A\x03\x12\x18\n\x0bitems_total\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\ritems_created\x18\x06 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\ritems_updated\x18\x07 \x01(\x03B\x03\xe0A\x03\x124\n\x0bupload_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\x99\x02\n\x05Issue\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04code\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05count\x18\x04 \x01(\x03B\x03\xe0A\x03\x12]\n\x08severity\x18\x05 \x01(\x0e2F.google.shopping.merchant.datasources.v1beta.FileUpload.Issue.SeverityB\x03\xe0A\x03\x12\x1e\n\x11documentation_uri\x18\x06 \x01(\tB\x03\xe0A\x03"<\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05ERROR\x10\x02"_\n\x0fProcessingState\x12 \n\x1cPROCESSING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06FAILED\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03:\x8a\x01\xeaA\x86\x01\n%merchantapi.googleapis.com/FileUpload\x12Daccounts/{account}/dataSources/{datasource}/fileUploads/{fileupload}*\x0bfileUploads2\nfileUpload"S\n\x14GetFileUploadRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%merchantapi.googleapis.com/FileUpload2\xbd\x02\n\x12FileUploadsService\x12\xdd\x01\n\rGetFileUpload\x12A.google.shopping.merchant.datasources.v1beta.GetFileUploadRequest\x1a7.google.shopping.merchant.datasources.v1beta.FileUpload"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/datasources/v1beta/{name=accounts/*/dataSources/*/fileUploads/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xac\x02\n/com.google.shopping.merchant.datasources.v1betaB\x10FileUploadsProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.datasources.v1beta.fileuploads_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.datasources.v1betaB\x10FileUploadsProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1beta'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['title']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['description']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['code']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['count']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['count']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['severity']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['severity']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['documentation_uri']._loaded_options = None
    _globals['_FILEUPLOAD_ISSUE'].fields_by_name['documentation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['name']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FILEUPLOAD'].fields_by_name['data_source_id']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['data_source_id']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['processing_state']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['processing_state']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['issues']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['issues']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['items_total']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['items_total']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['items_created']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['items_created']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['items_updated']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['items_updated']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD'].fields_by_name['upload_time']._loaded_options = None
    _globals['_FILEUPLOAD'].fields_by_name['upload_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILEUPLOAD']._loaded_options = None
    _globals['_FILEUPLOAD']._serialized_options = b'\xeaA\x86\x01\n%merchantapi.googleapis.com/FileUpload\x12Daccounts/{account}/dataSources/{datasource}/fileUploads/{fileupload}*\x0bfileUploads2\nfileUpload'
    _globals['_GETFILEUPLOADREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFILEUPLOADREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%merchantapi.googleapis.com/FileUpload"
    _globals['_FILEUPLOADSSERVICE']._loaded_options = None
    _globals['_FILEUPLOADSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_FILEUPLOADSSERVICE'].methods_by_name['GetFileUpload']._loaded_options = None
    _globals['_FILEUPLOADSSERVICE'].methods_by_name['GetFileUpload']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/datasources/v1beta/{name=accounts/*/dataSources/*/fileUploads/*}'
    _globals['_FILEUPLOAD']._serialized_start = 259
    _globals['_FILEUPLOAD']._serialized_end = 1165
    _globals['_FILEUPLOAD_ISSUE']._serialized_start = 646
    _globals['_FILEUPLOAD_ISSUE']._serialized_end = 927
    _globals['_FILEUPLOAD_ISSUE_SEVERITY']._serialized_start = 867
    _globals['_FILEUPLOAD_ISSUE_SEVERITY']._serialized_end = 927
    _globals['_FILEUPLOAD_PROCESSINGSTATE']._serialized_start = 929
    _globals['_FILEUPLOAD_PROCESSINGSTATE']._serialized_end = 1024
    _globals['_GETFILEUPLOADREQUEST']._serialized_start = 1167
    _globals['_GETFILEUPLOADREQUEST']._serialized_end = 1250
    _globals['_FILEUPLOADSSERVICE']._serialized_start = 1253
    _globals['_FILEUPLOADSSERVICE']._serialized_end = 1570