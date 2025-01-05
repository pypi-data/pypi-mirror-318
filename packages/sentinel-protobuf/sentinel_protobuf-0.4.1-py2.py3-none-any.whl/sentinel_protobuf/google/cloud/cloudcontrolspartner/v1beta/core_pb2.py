"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1beta/core.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import access_approval_requests_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_access__approval__requests__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import customer_workloads_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_customer__workloads__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import customers_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_customers__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import ekm_connections_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_ekm__connections__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import partner_permissions_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_partner__permissions__pb2
from .....google.cloud.cloudcontrolspartner.v1beta import partners_pb2 as google_dot_cloud_dot_cloudcontrolspartner_dot_v1beta_dot_partners__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/cloudcontrolspartner/v1beta/core.proto\x12(google.cloud.cloudcontrolspartner.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aGgoogle/cloud/cloudcontrolspartner/v1beta/access_approval_requests.proto\x1aAgoogle/cloud/cloudcontrolspartner/v1beta/customer_workloads.proto\x1a8google/cloud/cloudcontrolspartner/v1beta/customers.proto\x1a>google/cloud/cloudcontrolspartner/v1beta/ekm_connections.proto\x1aBgoogle/cloud/cloudcontrolspartner/v1beta/partner_permissions.proto\x1a7google/cloud/cloudcontrolspartner/v1beta/partners.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xbe\x0f\n\x18CloudControlsPartnerCore\x12\xd2\x01\n\x0bGetWorkload\x12<.google.cloud.cloudcontrolspartner.v1beta.GetWorkloadRequest\x1a2.google.cloud.cloudcontrolspartner.v1beta.Workload"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*}\x12\xe5\x01\n\rListWorkloads\x12>.google.cloud.cloudcontrolspartner.v1beta.ListWorkloadsRequest\x1a?.google.cloud.cloudcontrolspartner.v1beta.ListWorkloadsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1beta/{parent=organizations/*/locations/*/customers/*}/workloads\x12\xc6\x01\n\x0bGetCustomer\x12<.google.cloud.cloudcontrolspartner.v1beta.GetCustomerRequest\x1a2.google.cloud.cloudcontrolspartner.v1beta.Customer"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta/{name=organizations/*/locations/*/customers/*}\x12\xd9\x01\n\rListCustomers\x12>.google.cloud.cloudcontrolspartner.v1beta.ListCustomersRequest\x1a?.google.cloud.cloudcontrolspartner.v1beta.ListCustomersResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta/{parent=organizations/*/locations/*}/customers\x12\xf3\x01\n\x11GetEkmConnections\x12B.google.cloud.cloudcontrolspartner.v1beta.GetEkmConnectionsRequest\x1a8.google.cloud.cloudcontrolspartner.v1beta.EkmConnections"`\xdaA\x04name\x82\xd3\xe4\x93\x02S\x12Q/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/ekmConnections}\x12\x83\x02\n\x15GetPartnerPermissions\x12F.google.cloud.cloudcontrolspartner.v1beta.GetPartnerPermissionsRequest\x1a<.google.cloud.cloudcontrolspartner.v1beta.PartnerPermissions"d\xdaA\x04name\x82\xd3\xe4\x93\x02W\x12U/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/partnerPermissions}\x12\xa8\x02\n\x1aListAccessApprovalRequests\x12K.google.cloud.cloudcontrolspartner.v1beta.ListAccessApprovalRequestsRequest\x1aL.google.cloud.cloudcontrolspartner.v1beta.ListAccessApprovalRequestsResponse"o\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02]\x12[/v1beta/{parent=organizations/*/locations/*/customers/*/workloads/*}/accessApprovalRequests\x12\xbf\x01\n\nGetPartner\x12;.google.cloud.cloudcontrolspartner.v1beta.GetPartnerRequest\x1a1.google.cloud.cloudcontrolspartner.v1beta.Partner"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=organizations/*/locations/*/partner}\x1aW\xcaA#cloudcontrolspartner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x91\x03\n,com.google.cloud.cloudcontrolspartner.v1betaB\tCoreProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1beta\xeaAm\n8cloudcontrolspartner.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1beta.core_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.cloudcontrolspartner.v1betaB\tCoreProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1beta\xeaAm\n8cloudcontrolspartner.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDCONTROLSPARTNERCORE']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE']._serialized_options = b'\xcaA#cloudcontrolspartner.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetWorkload']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetWorkload']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*}'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListWorkloads']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListWorkloads']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1beta/{parent=organizations/*/locations/*/customers/*}/workloads'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetCustomer']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetCustomer']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta/{name=organizations/*/locations/*/customers/*}'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListCustomers']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListCustomers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta/{parent=organizations/*/locations/*}/customers'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetEkmConnections']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetEkmConnections']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02S\x12Q/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/ekmConnections}'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetPartnerPermissions']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetPartnerPermissions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02W\x12U/v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/partnerPermissions}'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListAccessApprovalRequests']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['ListAccessApprovalRequests']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02]\x12[/v1beta/{parent=organizations/*/locations/*/customers/*/workloads/*}/accessApprovalRequests'
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetPartner']._loaded_options = None
    _globals['_CLOUDCONTROLSPARTNERCORE'].methods_by_name['GetPartner']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=organizations/*/locations/*/partner}'
    _globals['_OPERATIONMETADATA']._serialized_start = 633
    _globals['_OPERATIONMETADATA']._serialized_end = 889
    _globals['_CLOUDCONTROLSPARTNERCORE']._serialized_start = 892
    _globals['_CLOUDCONTROLSPARTNERCORE']._serialized_end = 2874