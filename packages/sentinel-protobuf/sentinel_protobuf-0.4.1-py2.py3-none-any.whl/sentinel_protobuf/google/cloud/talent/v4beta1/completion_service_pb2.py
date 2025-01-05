"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/completion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/talent/v4beta1/completion_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/talent/v4beta1/common.proto"\x93\x04\n\x14CompleteQueryRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0elanguage_codes\x18\x03 \x03(\t\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x02\x121\n\x07company\x18\x05 \x01(\tB \xfaA\x1d\n\x1bjobs.googleapis.com/Company\x12P\n\x05scope\x18\x06 \x01(\x0e2A.google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionScope\x12N\n\x04type\x18\x07 \x01(\x0e2@.google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType"K\n\x0fCompletionScope\x12 \n\x1cCOMPLETION_SCOPE_UNSPECIFIED\x10\x00\x12\n\n\x06TENANT\x10\x01\x12\n\n\x06PUBLIC\x10\x02"`\n\x0eCompletionType\x12\x1f\n\x1bCOMPLETION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tJOB_TITLE\x10\x01\x12\x10\n\x0cCOMPANY_NAME\x10\x02\x12\x0c\n\x08COMBINED\x10\x03"\xc5\x02\n\x15CompleteQueryResponse\x12_\n\x12completion_results\x18\x01 \x03(\x0b2C.google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult\x12?\n\x08metadata\x18\x02 \x01(\x0b2-.google.cloud.talent.v4beta1.ResponseMetadata\x1a\x89\x01\n\x10CompletionResult\x12\x12\n\nsuggestion\x18\x01 \x01(\t\x12N\n\x04type\x18\x02 \x01(\x0e2@.google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType\x12\x11\n\timage_uri\x18\x03 \x01(\t2\xd5\x02\n\nCompletion\x12\xd8\x01\n\rCompleteQuery\x121.google.cloud.talent.v4beta1.CompleteQueryRequest\x1a2.google.cloud.talent.v4beta1.CompleteQueryResponse"`\x82\xd3\xe4\x93\x02Z\x12//v4beta1/{parent=projects/*/tenants/*}:completeZ\'\x12%/v4beta1/{parent=projects/*}:complete\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBz\n\x1fcom.google.cloud.talent.v4beta1B\x16CompletionServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.completion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x16CompletionServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bjobs.googleapis.com/Company'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['company']._serialized_options = b'\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_COMPLETION']._loaded_options = None
    _globals['_COMPLETION']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_COMPLETION'].methods_by_name['CompleteQuery']._loaded_options = None
    _globals['_COMPLETION'].methods_by_name['CompleteQuery']._serialized_options = b"\x82\xd3\xe4\x93\x02Z\x12//v4beta1/{parent=projects/*/tenants/*}:completeZ'\x12%/v4beta1/{parent=projects/*}:complete"
    _globals['_COMPLETEQUERYREQUEST']._serialized_start = 243
    _globals['_COMPLETEQUERYREQUEST']._serialized_end = 774
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONSCOPE']._serialized_start = 601
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONSCOPE']._serialized_end = 676
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONTYPE']._serialized_start = 678
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONTYPE']._serialized_end = 774
    _globals['_COMPLETEQUERYRESPONSE']._serialized_start = 777
    _globals['_COMPLETEQUERYRESPONSE']._serialized_end = 1102
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_start = 965
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_end = 1102
    _globals['_COMPLETION']._serialized_start = 1105
    _globals['_COMPLETION']._serialized_end = 1446