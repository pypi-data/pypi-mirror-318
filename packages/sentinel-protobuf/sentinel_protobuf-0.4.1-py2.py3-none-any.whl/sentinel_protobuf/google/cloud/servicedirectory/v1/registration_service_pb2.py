"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicedirectory/v1/registration_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.servicedirectory.v1 import endpoint_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1_dot_endpoint__pb2
from .....google.cloud.servicedirectory.v1 import namespace_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1_dot_namespace__pb2
from .....google.cloud.servicedirectory.v1 import service_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1_dot_service__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/servicedirectory/v1/registration_service.proto\x12 google.cloud.servicedirectory.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/servicedirectory/v1/endpoint.proto\x1a0google/cloud/servicedirectory/v1/namespace.proto\x1a.google/cloud/servicedirectory/v1/service.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb3\x01\n\x16CreateNamespaceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cnamespace_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\tnamespace\x18\x03 \x01(\x0b2+.google.cloud.servicedirectory.v1.NamespaceB\x03\xe0A\x02"\xaf\x01\n\x15ListNamespacesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"r\n\x16ListNamespacesResponse\x12?\n\nnamespaces\x18\x01 \x03(\x0b2+.google.cloud.servicedirectory.v1.Namespace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x13GetNamespaceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace"\x93\x01\n\x16UpdateNamespaceRequest\x12C\n\tnamespace\x18\x01 \x01(\x0b2+.google.cloud.servicedirectory.v1.NamespaceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"Y\n\x16DeleteNamespaceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace"\xb3\x01\n\x14CreateServiceRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace\x12\x17\n\nservice_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x07service\x18\x03 \x01(\x0b2).google.cloud.servicedirectory.v1.ServiceB\x03\xe0A\x02"\xb5\x01\n\x13ListServicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"l\n\x14ListServicesResponse\x12;\n\x08services\x18\x01 \x03(\x0b2).google.cloud.servicedirectory.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x11GetServiceRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service"\x8d\x01\n\x14UpdateServiceRequest\x12?\n\x07service\x18\x01 \x01(\x0b2).google.cloud.servicedirectory.v1.ServiceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x14DeleteServiceRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service"\xb5\x01\n\x15CreateEndpointRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x18\n\x0bendpoint_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x08endpoint\x18\x03 \x01(\x0b2*.google.cloud.servicedirectory.v1.EndpointB\x03\xe0A\x02"\xb4\x01\n\x14ListEndpointsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"o\n\x15ListEndpointsResponse\x12=\n\tendpoints\x18\x01 \x03(\x0b2*.google.cloud.servicedirectory.v1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x12GetEndpointRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint"\x90\x01\n\x15UpdateEndpointRequest\x12A\n\x08endpoint\x18\x01 \x01(\x0b2*.google.cloud.servicedirectory.v1.EndpointB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x15DeleteEndpointRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint2\xdf\x1e\n\x13RegistrationService\x12\xdb\x01\n\x0fCreateNamespace\x128.google.cloud.servicedirectory.v1.CreateNamespaceRequest\x1a+.google.cloud.servicedirectory.v1.Namespace"a\xdaA\x1dparent,namespace,namespace_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/namespaces:\tnamespace\x12\xc4\x01\n\x0eListNamespaces\x127.google.cloud.servicedirectory.v1.ListNamespacesRequest\x1a8.google.cloud.servicedirectory.v1.ListNamespacesResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/namespaces\x12\xb1\x01\n\x0cGetNamespace\x125.google.cloud.servicedirectory.v1.GetNamespaceRequest\x1a+.google.cloud.servicedirectory.v1.Namespace"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/namespaces/*}\x12\xdd\x01\n\x0fUpdateNamespace\x128.google.cloud.servicedirectory.v1.UpdateNamespaceRequest\x1a+.google.cloud.servicedirectory.v1.Namespace"c\xdaA\x15namespace,update_mask\x82\xd3\xe4\x93\x02E28/v1/{namespace.name=projects/*/locations/*/namespaces/*}:\tnamespace\x12\xa2\x01\n\x0fDeleteNamespace\x128.google.cloud.servicedirectory.v1.DeleteNamespaceRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/namespaces/*}\x12\xda\x01\n\rCreateService\x126.google.cloud.servicedirectory.v1.CreateServiceRequest\x1a).google.cloud.servicedirectory.v1.Service"f\xdaA\x19parent,service,service_id\x82\xd3\xe4\x93\x02D"9/v1/{parent=projects/*/locations/*/namespaces/*}/services:\x07service\x12\xc9\x01\n\x0cListServices\x125.google.cloud.servicedirectory.v1.ListServicesRequest\x1a6.google.cloud.servicedirectory.v1.ListServicesResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/namespaces/*}/services\x12\xb6\x01\n\nGetService\x123.google.cloud.servicedirectory.v1.GetServiceRequest\x1a).google.cloud.servicedirectory.v1.Service"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/namespaces/*/services/*}\x12\xdc\x01\n\rUpdateService\x126.google.cloud.servicedirectory.v1.UpdateServiceRequest\x1a).google.cloud.servicedirectory.v1.Service"h\xdaA\x13service,update_mask\x82\xd3\xe4\x93\x02L2A/v1/{service.name=projects/*/locations/*/namespaces/*/services/*}:\x07service\x12\xa9\x01\n\rDeleteService\x126.google.cloud.servicedirectory.v1.DeleteServiceRequest\x1a\x16.google.protobuf.Empty"H\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/namespaces/*/services/*}\x12\xec\x01\n\x0eCreateEndpoint\x127.google.cloud.servicedirectory.v1.CreateEndpointRequest\x1a*.google.cloud.servicedirectory.v1.Endpoint"u\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02Q"E/v1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints:\x08endpoint\x12\xd8\x01\n\rListEndpoints\x126.google.cloud.servicedirectory.v1.ListEndpointsRequest\x1a7.google.cloud.servicedirectory.v1.ListEndpointsResponse"V\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints\x12\xc5\x01\n\x0bGetEndpoint\x124.google.cloud.servicedirectory.v1.GetEndpointRequest\x1a*.google.cloud.servicedirectory.v1.Endpoint"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}\x12\xee\x01\n\x0eUpdateEndpoint\x127.google.cloud.servicedirectory.v1.UpdateEndpointRequest\x1a*.google.cloud.servicedirectory.v1.Endpoint"w\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02Z2N/v1/{endpoint.name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}:\x08endpoint\x12\xb7\x01\n\x0eDeleteEndpoint\x127.google.cloud.servicedirectory.v1.DeleteEndpointRequest\x1a\x16.google.protobuf.Empty"T\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}\x12\xe8\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x9c\x01\x82\xd3\xe4\x93\x02\x95\x01"?/v1/{resource=projects/*/locations/*/namespaces/*}:getIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:getIamPolicy:\x01*\x12\xe8\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x9c\x01\x82\xd3\xe4\x93\x02\x95\x01"?/v1/{resource=projects/*/locations/*/namespaces/*}:setIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:setIamPolicy:\x01*\x12\x94\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xa8\x01\x82\xd3\xe4\x93\x02\xa1\x01"E/v1/{resource=projects/*/locations/*/namespaces/*}:testIamPermissions:\x01*ZU"P/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:testIamPermissions:\x01*\x1aS\xcaA\x1fservicedirectory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x02\n$com.google.cloud.servicedirectory.v1B\x18RegistrationServiceProtoP\x01ZPcloud.google.com/go/servicedirectory/apiv1/servicedirectorypb;servicedirectorypb\xaa\x02 Google.Cloud.ServiceDirectory.V1\xca\x02 Google\\Cloud\\ServiceDirectory\\V1\xea\x02#Google::Cloud::ServiceDirectory::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicedirectory.v1.registration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.servicedirectory.v1B\x18RegistrationServiceProtoP\x01ZPcloud.google.com/go/servicedirectory/apiv1/servicedirectorypb;servicedirectorypb\xaa\x02 Google.Cloud.ServiceDirectory.V1\xca\x02 Google\\Cloud\\ServiceDirectory\\V1\xea\x02#Google::Cloud::ServiceDirectory::V1'
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['namespace_id']._loaded_options = None
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['namespace_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['namespace']._loaded_options = None
    _globals['_CREATENAMESPACEREQUEST'].fields_by_name['namespace']._serialized_options = b'\xe0A\x02'
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTNAMESPACESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETNAMESPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNAMESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace'
    _globals['_UPDATENAMESPACEREQUEST'].fields_by_name['namespace']._loaded_options = None
    _globals['_UPDATENAMESPACEREQUEST'].fields_by_name['namespace']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATENAMESPACEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATENAMESPACEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENAMESPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENAMESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service_id']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_CREATESERVICEREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVICESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTSERVICESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERVICEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint'
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint'
    _globals['_REGISTRATIONSERVICE']._loaded_options = None
    _globals['_REGISTRATIONSERVICE']._serialized_options = b'\xcaA\x1fservicedirectory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateNamespace']._serialized_options = b'\xdaA\x1dparent,namespace,namespace_id\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/namespaces:\tnamespace'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListNamespaces']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListNamespaces']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/namespaces'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/namespaces/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateNamespace']._serialized_options = b'\xdaA\x15namespace,update_mask\x82\xd3\xe4\x93\x02E28/v1/{namespace.name=projects/*/locations/*/namespaces/*}:\tnamespace'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/namespaces/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateService']._serialized_options = b'\xdaA\x19parent,service,service_id\x82\xd3\xe4\x93\x02D"9/v1/{parent=projects/*/locations/*/namespaces/*}/services:\x07service'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListServices']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListServices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/namespaces/*}/services'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/namespaces/*/services/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateService']._serialized_options = b'\xdaA\x13service,update_mask\x82\xd3\xe4\x93\x02L2A/v1/{service.name=projects/*/locations/*/namespaces/*/services/*}:\x07service'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/namespaces/*/services/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateEndpoint']._serialized_options = b'\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02Q"E/v1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints:\x08endpoint'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListEndpoints']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02G\x12E/v1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12E/v1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateEndpoint']._serialized_options = b'\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02Z2N/v1/{endpoint.name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}:\x08endpoint'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G*E/v1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x95\x01"?/v1/{resource=projects/*/locations/*/namespaces/*}:getIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:getIamPolicy:\x01*'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x95\x01"?/v1/{resource=projects/*/locations/*/namespaces/*}:setIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:setIamPolicy:\x01*'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa1\x01"E/v1/{resource=projects/*/locations/*/namespaces/*}:testIamPermissions:\x01*ZU"P/v1/{resource=projects/*/locations/*/namespaces/*/services/*}:testIamPermissions:\x01*'
    _globals['_CREATENAMESPACEREQUEST']._serialized_start = 483
    _globals['_CREATENAMESPACEREQUEST']._serialized_end = 662
    _globals['_LISTNAMESPACESREQUEST']._serialized_start = 665
    _globals['_LISTNAMESPACESREQUEST']._serialized_end = 840
    _globals['_LISTNAMESPACESRESPONSE']._serialized_start = 842
    _globals['_LISTNAMESPACESRESPONSE']._serialized_end = 956
    _globals['_GETNAMESPACEREQUEST']._serialized_start = 958
    _globals['_GETNAMESPACEREQUEST']._serialized_end = 1044
    _globals['_UPDATENAMESPACEREQUEST']._serialized_start = 1047
    _globals['_UPDATENAMESPACEREQUEST']._serialized_end = 1194
    _globals['_DELETENAMESPACEREQUEST']._serialized_start = 1196
    _globals['_DELETENAMESPACEREQUEST']._serialized_end = 1285
    _globals['_CREATESERVICEREQUEST']._serialized_start = 1288
    _globals['_CREATESERVICEREQUEST']._serialized_end = 1467
    _globals['_LISTSERVICESREQUEST']._serialized_start = 1470
    _globals['_LISTSERVICESREQUEST']._serialized_end = 1651
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 1653
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 1761
    _globals['_GETSERVICEREQUEST']._serialized_start = 1763
    _globals['_GETSERVICEREQUEST']._serialized_end = 1845
    _globals['_UPDATESERVICEREQUEST']._serialized_start = 1848
    _globals['_UPDATESERVICEREQUEST']._serialized_end = 1989
    _globals['_DELETESERVICEREQUEST']._serialized_start = 1991
    _globals['_DELETESERVICEREQUEST']._serialized_end = 2076
    _globals['_CREATEENDPOINTREQUEST']._serialized_start = 2079
    _globals['_CREATEENDPOINTREQUEST']._serialized_end = 2260
    _globals['_LISTENDPOINTSREQUEST']._serialized_start = 2263
    _globals['_LISTENDPOINTSREQUEST']._serialized_end = 2443
    _globals['_LISTENDPOINTSRESPONSE']._serialized_start = 2445
    _globals['_LISTENDPOINTSRESPONSE']._serialized_end = 2556
    _globals['_GETENDPOINTREQUEST']._serialized_start = 2558
    _globals['_GETENDPOINTREQUEST']._serialized_end = 2642
    _globals['_UPDATEENDPOINTREQUEST']._serialized_start = 2645
    _globals['_UPDATEENDPOINTREQUEST']._serialized_end = 2789
    _globals['_DELETEENDPOINTREQUEST']._serialized_start = 2791
    _globals['_DELETEENDPOINTREQUEST']._serialized_end = 2878
    _globals['_REGISTRATIONSERVICE']._serialized_start = 2881
    _globals['_REGISTRATIONSERVICE']._serialized_end = 6816