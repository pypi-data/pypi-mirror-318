"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicehealth/v1/event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.servicehealth.v1 import event_resources_pb2 as google_dot_cloud_dot_servicehealth_dot_v1_dot_event__resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/servicehealth/v1/event_service.proto\x12\x1dgoogle.cloud.servicehealth.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a3google/cloud/servicehealth/v1/event_resources.proto2\xaa\n\n\rServiceHealth\x12\xae\x01\n\nListEvents\x120.google.cloud.servicehealth.v1.ListEventsRequest\x1a1.google.cloud.servicehealth.v1.ListEventsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/events\x12\x9b\x01\n\x08GetEvent\x12..google.cloud.servicehealth.v1.GetEventRequest\x1a$.google.cloud.servicehealth.v1.Event"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/events/*}\x12\xe3\x01\n\x16ListOrganizationEvents\x12<.google.cloud.servicehealth.v1.ListOrganizationEventsRequest\x1a=.google.cloud.servicehealth.v1.ListOrganizationEventsResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=organizations/*/locations/*}/organizationEvents\x12\xd0\x01\n\x14GetOrganizationEvent\x12:.google.cloud.servicehealth.v1.GetOrganizationEventRequest\x1a0.google.cloud.servicehealth.v1.OrganizationEvent"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=organizations/*/locations/*/organizationEvents/*}\x12\xe7\x01\n\x17ListOrganizationImpacts\x12=.google.cloud.servicehealth.v1.ListOrganizationImpactsRequest\x1a>.google.cloud.servicehealth.v1.ListOrganizationImpactsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=organizations/*/locations/*}/organizationImpacts\x12\xd4\x01\n\x15GetOrganizationImpact\x12;.google.cloud.servicehealth.v1.GetOrganizationImpactRequest\x1a1.google.cloud.servicehealth.v1.OrganizationImpact"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=organizations/*/locations/*/organizationImpacts/*}\x1aP\xcaA\x1cservicehealth.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe4\x01\n!com.google.cloud.servicehealth.v1B\x11EventServiceProtoP\x01ZGcloud.google.com/go/servicehealth/apiv1/servicehealthpb;servicehealthpb\xaa\x02\x1dGoogle.Cloud.ServiceHealth.V1\xca\x02\x1dGoogle\\Cloud\\ServiceHealth\\V1\xea\x02 Google::Cloud::ServiceHealth::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicehealth.v1.event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.servicehealth.v1B\x11EventServiceProtoP\x01ZGcloud.google.com/go/servicehealth/apiv1/servicehealthpb;servicehealthpb\xaa\x02\x1dGoogle.Cloud.ServiceHealth.V1\xca\x02\x1dGoogle\\Cloud\\ServiceHealth\\V1\xea\x02 Google::Cloud::ServiceHealth::V1'
    _globals['_SERVICEHEALTH']._loaded_options = None
    _globals['_SERVICEHEALTH']._serialized_options = b'\xcaA\x1cservicehealth.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SERVICEHEALTH'].methods_by_name['ListEvents']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['ListEvents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/events'
    _globals['_SERVICEHEALTH'].methods_by_name['GetEvent']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['GetEvent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/events/*}'
    _globals['_SERVICEHEALTH'].methods_by_name['ListOrganizationEvents']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['ListOrganizationEvents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=organizations/*/locations/*}/organizationEvents'
    _globals['_SERVICEHEALTH'].methods_by_name['GetOrganizationEvent']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['GetOrganizationEvent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=organizations/*/locations/*/organizationEvents/*}'
    _globals['_SERVICEHEALTH'].methods_by_name['ListOrganizationImpacts']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['ListOrganizationImpacts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=organizations/*/locations/*}/organizationImpacts'
    _globals['_SERVICEHEALTH'].methods_by_name['GetOrganizationImpact']._loaded_options = None
    _globals['_SERVICEHEALTH'].methods_by_name['GetOrganizationImpact']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=organizations/*/locations/*/organizationImpacts/*}'
    _globals['_SERVICEHEALTH']._serialized_start = 193
    _globals['_SERVICEHEALTH']._serialized_end = 1515