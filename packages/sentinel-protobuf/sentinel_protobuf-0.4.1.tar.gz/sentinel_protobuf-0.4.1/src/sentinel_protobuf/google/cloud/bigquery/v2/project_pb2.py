"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/project.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/bigquery/v2/project.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"3\n\x18GetServiceAccountRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02"8\n\x19GetServiceAccountResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t2\xfd\x02\n\x0eProjectService\x12\xb9\x01\n\x11GetServiceAccount\x122.google.cloud.bigquery.v2.GetServiceAccountRequest\x1a3.google.cloud.bigquery.v2.GetServiceAccountResponse";\x82\xd3\xe4\x93\x025\x123/bigquery/v2/projects/{project_id=*}/serviceAccount\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBf\n\x1ccom.google.cloud.bigquery.v2B\x0cProjectProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x0cProjectProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_GETSERVICEACCOUNTREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETSERVICEACCOUNTREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PROJECTSERVICE']._loaded_options = None
    _globals['_PROJECTSERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_PROJECTSERVICE'].methods_by_name['GetServiceAccount']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetServiceAccount']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/bigquery/v2/projects/{project_id=*}/serviceAccount'
    _globals['_GETSERVICEACCOUNTREQUEST']._serialized_start = 156
    _globals['_GETSERVICEACCOUNTREQUEST']._serialized_end = 207
    _globals['_GETSERVICEACCOUNTRESPONSE']._serialized_start = 209
    _globals['_GETSERVICEACCOUNTRESPONSE']._serialized_end = 265
    _globals['_PROJECTSERVICE']._serialized_start = 268
    _globals['_PROJECTSERVICE']._serialized_end = 649