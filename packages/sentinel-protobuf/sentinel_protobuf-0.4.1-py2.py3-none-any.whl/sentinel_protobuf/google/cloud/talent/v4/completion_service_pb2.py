"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/completion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4 import common_pb2 as google_dot_cloud_dot_talent_dot_v4_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/talent/v4/completion_service.proto\x12\x16google.cloud.talent.v4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/talent/v4/common.proto"\x88\x04\n\x14CompleteQueryRequest\x122\n\x06tenant\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0elanguage_codes\x18\x03 \x03(\t\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x02\x121\n\x07company\x18\x05 \x01(\tB \xfaA\x1d\n\x1bjobs.googleapis.com/Company\x12K\n\x05scope\x18\x06 \x01(\x0e2<.google.cloud.talent.v4.CompleteQueryRequest.CompletionScope\x12I\n\x04type\x18\x07 \x01(\x0e2;.google.cloud.talent.v4.CompleteQueryRequest.CompletionType"K\n\x0fCompletionScope\x12 \n\x1cCOMPLETION_SCOPE_UNSPECIFIED\x10\x00\x12\n\n\x06TENANT\x10\x01\x12\n\n\x06PUBLIC\x10\x02"`\n\x0eCompletionType\x12\x1f\n\x1bCOMPLETION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tJOB_TITLE\x10\x01\x12\x10\n\x0cCOMPANY_NAME\x10\x02\x12\x0c\n\x08COMBINED\x10\x03"\xb6\x02\n\x15CompleteQueryResponse\x12Z\n\x12completion_results\x18\x01 \x03(\x0b2>.google.cloud.talent.v4.CompleteQueryResponse.CompletionResult\x12:\n\x08metadata\x18\x02 \x01(\x0b2(.google.cloud.talent.v4.ResponseMetadata\x1a\x84\x01\n\x10CompletionResult\x12\x12\n\nsuggestion\x18\x01 \x01(\t\x12I\n\x04type\x18\x02 \x01(\x0e2;.google.cloud.talent.v4.CompleteQueryRequest.CompletionType\x12\x11\n\timage_uri\x18\x03 \x01(\t2\xa2\x02\n\nCompletion\x12\xa5\x01\n\rCompleteQuery\x12,.google.cloud.talent.v4.CompleteQueryRequest\x1a-.google.cloud.talent.v4.CompleteQueryResponse"7\x82\xd3\xe4\x93\x021\x12//v4/{tenant=projects/*/tenants/*}:completeQuery\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBp\n\x1acom.google.cloud.talent.v4B\x16CompletionServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.completion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x16CompletionServiceProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['tenant']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['tenant']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1ajobs.googleapis.com/Tenant'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['company']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['company']._serialized_options = b'\xfaA\x1d\n\x1bjobs.googleapis.com/Company'
    _globals['_COMPLETION']._loaded_options = None
    _globals['_COMPLETION']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_COMPLETION'].methods_by_name['CompleteQuery']._loaded_options = None
    _globals['_COMPLETION'].methods_by_name['CompleteQuery']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//v4/{tenant=projects/*/tenants/*}:completeQuery'
    _globals['_COMPLETEQUERYREQUEST']._serialized_start = 228
    _globals['_COMPLETEQUERYREQUEST']._serialized_end = 748
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONSCOPE']._serialized_start = 575
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONSCOPE']._serialized_end = 650
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONTYPE']._serialized_start = 652
    _globals['_COMPLETEQUERYREQUEST_COMPLETIONTYPE']._serialized_end = 748
    _globals['_COMPLETEQUERYRESPONSE']._serialized_start = 751
    _globals['_COMPLETEQUERYRESPONSE']._serialized_end = 1061
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_start = 929
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_end = 1061
    _globals['_COMPLETION']._serialized_start = 1064
    _globals['_COMPLETION']._serialized_end = 1354