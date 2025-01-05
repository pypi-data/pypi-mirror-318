"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/phishingprotection/v1beta1/phishingprotection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/phishingprotection/v1beta1/phishingprotection.proto\x12\'google.cloud.phishingprotection.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"n\n\x15ReportPhishingRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02"\x18\n\x16ReportPhishingResponse2\xd3\x02\n PhishingProtectionServiceV1Beta1\x12\xd7\x01\n\x0eReportPhishing\x12>.google.cloud.phishingprotection.v1beta1.ReportPhishingRequest\x1a?.google.cloud.phishingprotection.v1beta1.ReportPhishingResponse"D\xdaA\nparent,uri\x82\xd3\xe4\x93\x021",/v1beta1/{parent=projects/*}/phishing:report:\x01*\x1aU\xcaA!phishingprotection.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa7\x02\n%com.google.phishingprotection.v1beta1B\x17PhishingProtectionProtoP\x01Z[cloud.google.com/go/phishingprotection/apiv1beta1/phishingprotectionpb;phishingprotectionpb\xa2\x02\x04GCPP\xaa\x02\'Google.Cloud.PhishingProtection.V1Beta1\xca\x02\'Google\\Cloud\\PhishingProtection\\V1beta1\xea\x02*Google::Cloud::PhishingProtection::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.phishingprotection.v1beta1.phishingprotection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n%com.google.phishingprotection.v1beta1B\x17PhishingProtectionProtoP\x01Z[cloud.google.com/go/phishingprotection/apiv1beta1/phishingprotectionpb;phishingprotectionpb\xa2\x02\x04GCPP\xaa\x02'Google.Cloud.PhishingProtection.V1Beta1\xca\x02'Google\\Cloud\\PhishingProtection\\V1beta1\xea\x02*Google::Cloud::PhishingProtection::V1beta1"
    _globals['_REPORTPHISHINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REPORTPHISHINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_REPORTPHISHINGREQUEST'].fields_by_name['uri']._loaded_options = None
    _globals['_REPORTPHISHINGREQUEST'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1']._loaded_options = None
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1']._serialized_options = b'\xcaA!phishingprotection.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1'].methods_by_name['ReportPhishing']._loaded_options = None
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1'].methods_by_name['ReportPhishing']._serialized_options = b'\xdaA\nparent,uri\x82\xd3\xe4\x93\x021",/v1beta1/{parent=projects/*}/phishing:report:\x01*'
    _globals['_REPORTPHISHINGREQUEST']._serialized_start = 224
    _globals['_REPORTPHISHINGREQUEST']._serialized_end = 334
    _globals['_REPORTPHISHINGRESPONSE']._serialized_start = 336
    _globals['_REPORTPHISHINGRESPONSE']._serialized_end = 360
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1']._serialized_start = 363
    _globals['_PHISHINGPROTECTIONSERVICEV1BETA1']._serialized_end = 702