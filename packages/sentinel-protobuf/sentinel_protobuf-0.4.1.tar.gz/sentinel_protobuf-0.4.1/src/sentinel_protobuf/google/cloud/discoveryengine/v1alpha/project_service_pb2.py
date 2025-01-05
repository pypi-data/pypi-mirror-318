"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/project_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import project_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_project__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/discoveryengine/v1alpha/project_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/discoveryengine/v1alpha/project.proto\x1a#google/longrunning/operations.proto"Q\n\x11GetProjectRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project"\xa0\x01\n\x17ProvisionProjectRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project\x12"\n\x15accept_data_use_terms\x18\x02 \x01(\x08B\x03\xe0A\x02\x12#\n\x16data_use_terms_version\x18\x03 \x01(\tB\x03\xe0A\x02"\x1a\n\x18ProvisionProjectMetadata"\xe2\x02\n\x1aReportConsentChangeRequest\x12x\n\x15consent_change_action\x18\x01 \x01(\x0e2T.google.cloud.discoveryengine.v1alpha.ReportConsentChangeRequest.ConsentChangeActionB\x03\xe0A\x02\x12?\n\x07project\x18\x02 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project\x12\x1c\n\x0fservice_term_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12!\n\x14service_term_version\x18\x04 \x01(\tB\x03\xe0A\x02"H\n\x13ConsentChangeAction\x12%\n!CONSENT_CHANGE_ACTION_UNSPECIFIED\x10\x00\x12\n\n\x06ACCEPT\x10\x012\xaf\x06\n\x0eProjectService\x12\x9f\x01\n\nGetProject\x127.google.cloud.discoveryengine.v1alpha.GetProjectRequest\x1a-.google.cloud.discoveryengine.v1alpha.Project")\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha/{name=projects/*}\x12\x99\x02\n\x10ProvisionProject\x12=.google.cloud.discoveryengine.v1alpha.ProvisionProjectRequest\x1a\x1d.google.longrunning.Operation"\xa6\x01\xcaAm\n,google.cloud.discoveryengine.v1alpha.Project\x12=google.cloud.discoveryengine.v1alpha.ProvisionProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02)"$/v1alpha/{name=projects/*}:provision:\x01*\x12\x8a\x02\n\x13ReportConsentChange\x12@.google.cloud.discoveryengine.v1alpha.ReportConsentChangeRequest\x1a-.google.cloud.discoveryengine.v1alpha.Project"\x81\x01\xdaABconsent_change_action,project,service_term_id,service_term_version\x82\xd3\xe4\x93\x026"1/v1alpha/{project=projects/*}:reportConsentChange:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9f\x02\n(com.google.cloud.discoveryengine.v1alphaB\x13ProjectServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.project_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x13ProjectServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['accept_data_use_terms']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['accept_data_use_terms']._serialized_options = b'\xe0A\x02'
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['data_use_terms_version']._loaded_options = None
    _globals['_PROVISIONPROJECTREQUEST'].fields_by_name['data_use_terms_version']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['consent_change_action']._loaded_options = None
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['consent_change_action']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Project'
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['service_term_id']._loaded_options = None
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['service_term_id']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['service_term_version']._loaded_options = None
    _globals['_REPORTCONSENTCHANGEREQUEST'].fields_by_name['service_term_version']._serialized_options = b'\xe0A\x02'
    _globals['_PROJECTSERVICE']._loaded_options = None
    _globals['_PROJECTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha/{name=projects/*}'
    _globals['_PROJECTSERVICE'].methods_by_name['ProvisionProject']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['ProvisionProject']._serialized_options = b'\xcaAm\n,google.cloud.discoveryengine.v1alpha.Project\x12=google.cloud.discoveryengine.v1alpha.ProvisionProjectMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02)"$/v1alpha/{name=projects/*}:provision:\x01*'
    _globals['_PROJECTSERVICE'].methods_by_name['ReportConsentChange']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['ReportConsentChange']._serialized_options = b'\xdaABconsent_change_action,project,service_term_id,service_term_version\x82\xd3\xe4\x93\x026"1/v1alpha/{project=projects/*}:reportConsentChange:\x01*'
    _globals['_GETPROJECTREQUEST']._serialized_start = 304
    _globals['_GETPROJECTREQUEST']._serialized_end = 385
    _globals['_PROVISIONPROJECTREQUEST']._serialized_start = 388
    _globals['_PROVISIONPROJECTREQUEST']._serialized_end = 548
    _globals['_PROVISIONPROJECTMETADATA']._serialized_start = 550
    _globals['_PROVISIONPROJECTMETADATA']._serialized_end = 576
    _globals['_REPORTCONSENTCHANGEREQUEST']._serialized_start = 579
    _globals['_REPORTCONSENTCHANGEREQUEST']._serialized_end = 933
    _globals['_REPORTCONSENTCHANGEREQUEST_CONSENTCHANGEACTION']._serialized_start = 861
    _globals['_REPORTCONSENTCHANGEREQUEST_CONSENTCHANGEACTION']._serialized_end = 933
    _globals['_PROJECTSERVICE']._serialized_start = 936
    _globals['_PROJECTSERVICE']._serialized_end = 1751