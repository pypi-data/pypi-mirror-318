"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/servicedirectory/v1beta1/registration_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.servicedirectory.v1beta1 import endpoint_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1beta1_dot_endpoint__pb2
from .....google.cloud.servicedirectory.v1beta1 import namespace_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1beta1_dot_namespace__pb2
from .....google.cloud.servicedirectory.v1beta1 import service_pb2 as google_dot_cloud_dot_servicedirectory_dot_v1beta1_dot_service__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/servicedirectory/v1beta1/registration_service.proto\x12%google.cloud.servicedirectory.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/servicedirectory/v1beta1/endpoint.proto\x1a5google/cloud/servicedirectory/v1beta1/namespace.proto\x1a3google/cloud/servicedirectory/v1beta1/service.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb8\x01\n\x16CreateNamespaceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cnamespace_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\tnamespace\x18\x03 \x01(\x0b20.google.cloud.servicedirectory.v1beta1.NamespaceB\x03\xe0A\x02"\xaf\x01\n\x15ListNamespacesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"w\n\x16ListNamespacesResponse\x12D\n\nnamespaces\x18\x01 \x03(\x0b20.google.cloud.servicedirectory.v1beta1.Namespace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x13GetNamespaceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace"\x98\x01\n\x16UpdateNamespaceRequest\x12H\n\tnamespace\x18\x01 \x01(\x0b20.google.cloud.servicedirectory.v1beta1.NamespaceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"Y\n\x16DeleteNamespaceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace"\xb8\x01\n\x14CreateServiceRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace\x12\x17\n\nservice_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\x07service\x18\x03 \x01(\x0b2..google.cloud.servicedirectory.v1beta1.ServiceB\x03\xe0A\x02"\xb5\x01\n\x13ListServicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)servicedirectory.googleapis.com/Namespace\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"q\n\x14ListServicesResponse\x12@\n\x08services\x18\x01 \x03(\x0b2..google.cloud.servicedirectory.v1beta1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x11GetServiceRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service"\x92\x01\n\x14UpdateServiceRequest\x12D\n\x07service\x18\x01 \x01(\x0b2..google.cloud.servicedirectory.v1beta1.ServiceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x14DeleteServiceRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service"\xba\x01\n\x15CreateEndpointRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x18\n\x0bendpoint_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12F\n\x08endpoint\x18\x03 \x01(\x0b2/.google.cloud.servicedirectory.v1beta1.EndpointB\x03\xe0A\x02"\xb4\x01\n\x14ListEndpointsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"t\n\x15ListEndpointsResponse\x12B\n\tendpoints\x18\x01 \x03(\x0b2/.google.cloud.servicedirectory.v1beta1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x12GetEndpointRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint"\x95\x01\n\x15UpdateEndpointRequest\x12F\n\x08endpoint\x18\x01 \x01(\x0b2/.google.cloud.servicedirectory.v1beta1.EndpointB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x15DeleteEndpointRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(servicedirectory.googleapis.com/Endpoint2\xda"\n\x13RegistrationService\x12\xea\x01\n\x0fCreateNamespace\x12=.google.cloud.servicedirectory.v1beta1.CreateNamespaceRequest\x1a0.google.cloud.servicedirectory.v1beta1.Namespace"f\xdaA\x1dparent,namespace,namespace_id\x82\xd3\xe4\x93\x02@"3/v1beta1/{parent=projects/*/locations/*}/namespaces:\tnamespace\x12\xd3\x01\n\x0eListNamespaces\x12<.google.cloud.servicedirectory.v1beta1.ListNamespacesRequest\x1a=.google.cloud.servicedirectory.v1beta1.ListNamespacesResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/namespaces\x12\xc0\x01\n\x0cGetNamespace\x12:.google.cloud.servicedirectory.v1beta1.GetNamespaceRequest\x1a0.google.cloud.servicedirectory.v1beta1.Namespace"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/namespaces/*}\x12\xec\x01\n\x0fUpdateNamespace\x12=.google.cloud.servicedirectory.v1beta1.UpdateNamespaceRequest\x1a0.google.cloud.servicedirectory.v1beta1.Namespace"h\xdaA\x15namespace,update_mask\x82\xd3\xe4\x93\x02J2=/v1beta1/{namespace.name=projects/*/locations/*/namespaces/*}:\tnamespace\x12\xac\x01\n\x0fDeleteNamespace\x12=.google.cloud.servicedirectory.v1beta1.DeleteNamespaceRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/namespaces/*}\x12\xe9\x01\n\rCreateService\x12;.google.cloud.servicedirectory.v1beta1.CreateServiceRequest\x1a..google.cloud.servicedirectory.v1beta1.Service"k\xdaA\x19parent,service,service_id\x82\xd3\xe4\x93\x02I">/v1beta1/{parent=projects/*/locations/*/namespaces/*}/services:\x07service\x12\xd8\x01\n\x0cListServices\x12:.google.cloud.servicedirectory.v1beta1.ListServicesRequest\x1a;.google.cloud.servicedirectory.v1beta1.ListServicesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/namespaces/*}/services\x12\xc5\x01\n\nGetService\x128.google.cloud.servicedirectory.v1beta1.GetServiceRequest\x1a..google.cloud.servicedirectory.v1beta1.Service"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}\x12\xeb\x01\n\rUpdateService\x12;.google.cloud.servicedirectory.v1beta1.UpdateServiceRequest\x1a..google.cloud.servicedirectory.v1beta1.Service"m\xdaA\x13service,update_mask\x82\xd3\xe4\x93\x02Q2F/v1beta1/{service.name=projects/*/locations/*/namespaces/*/services/*}:\x07service\x12\xb3\x01\n\rDeleteService\x12;.google.cloud.servicedirectory.v1beta1.DeleteServiceRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}\x12\xfb\x01\n\x0eCreateEndpoint\x12<.google.cloud.servicedirectory.v1beta1.CreateEndpointRequest\x1a/.google.cloud.servicedirectory.v1beta1.Endpoint"z\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02V"J/v1beta1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints:\x08endpoint\x12\xe7\x01\n\rListEndpoints\x12;.google.cloud.servicedirectory.v1beta1.ListEndpointsRequest\x1a<.google.cloud.servicedirectory.v1beta1.ListEndpointsResponse"[\xdaA\x06parent\x82\xd3\xe4\x93\x02L\x12J/v1beta1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints\x12\xd4\x01\n\x0bGetEndpoint\x129.google.cloud.servicedirectory.v1beta1.GetEndpointRequest\x1a/.google.cloud.servicedirectory.v1beta1.Endpoint"Y\xdaA\x04name\x82\xd3\xe4\x93\x02L\x12J/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}\x12\xfd\x01\n\x0eUpdateEndpoint\x12<.google.cloud.servicedirectory.v1beta1.UpdateEndpointRequest\x1a/.google.cloud.servicedirectory.v1beta1.Endpoint"|\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02_2S/v1beta1/{endpoint.name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}:\x08endpoint\x12\xc1\x01\n\x0eDeleteEndpoint\x12<.google.cloud.servicedirectory.v1beta1.DeleteEndpointRequest\x1a\x16.google.protobuf.Empty"Y\xdaA\x04name\x82\xd3\xe4\x93\x02L*J/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}\x12\xc9\x02\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xfd\x01\x82\xd3\xe4\x93\x02\xf6\x01"D/v1beta1/{resource=projects/*/locations/*/namespaces/*}:getIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:getIamPolicy:\x01*ZU"P/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:getIamPolicy:\x01*\x12\xc9\x02\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xfd\x01\x82\xd3\xe4\x93\x02\xf6\x01"D/v1beta1/{resource=projects/*/locations/*/namespaces/*}:setIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:setIamPolicy:\x01*ZU"P/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:setIamPolicy:\x01*\x12\xfb\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\x8f\x02\x82\xd3\xe4\x93\x02\x88\x02"J/v1beta1/{resource=projects/*/locations/*/namespaces/*}:testIamPermissions:\x01*ZZ"U/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:testIamPermissions:\x01*Z["V/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:testIamPermissions:\x01*\x1aS\xcaA\x1fservicedirectory.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x99\x02\n)com.google.cloud.servicedirectory.v1beta1B\x18RegistrationServiceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.servicedirectory.v1beta1.registration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.servicedirectory.v1beta1B\x18RegistrationServiceProtoP\x01ZUcloud.google.com/go/servicedirectory/apiv1beta1/servicedirectorypb;servicedirectorypb\xaa\x02%Google.Cloud.ServiceDirectory.V1Beta1\xca\x02%Google\\Cloud\\ServiceDirectory\\V1beta1\xea\x02(Google::Cloud::ServiceDirectory::V1beta1'
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
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateNamespace']._serialized_options = b'\xdaA\x1dparent,namespace,namespace_id\x82\xd3\xe4\x93\x02@"3/v1beta1/{parent=projects/*/locations/*}/namespaces:\tnamespace'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListNamespaces']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListNamespaces']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/namespaces'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/namespaces/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateNamespace']._serialized_options = b'\xdaA\x15namespace,update_mask\x82\xd3\xe4\x93\x02J2=/v1beta1/{namespace.name=projects/*/locations/*/namespaces/*}:\tnamespace'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteNamespace']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/namespaces/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateService']._serialized_options = b'\xdaA\x19parent,service,service_id\x82\xd3\xe4\x93\x02I">/v1beta1/{parent=projects/*/locations/*/namespaces/*}/services:\x07service'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListServices']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListServices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/namespaces/*}/services'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateService']._serialized_options = b'\xdaA\x13service,update_mask\x82\xd3\xe4\x93\x02Q2F/v1beta1/{service.name=projects/*/locations/*/namespaces/*/services/*}:\x07service'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['CreateEndpoint']._serialized_options = b'\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02V"J/v1beta1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints:\x08endpoint'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListEndpoints']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['ListEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02L\x12J/v1beta1/{parent=projects/*/locations/*/namespaces/*/services/*}/endpoints'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02L\x12J/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['UpdateEndpoint']._serialized_options = b'\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02_2S/v1beta1/{endpoint.name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}:\x08endpoint'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteEndpoint']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['DeleteEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02L*J/v1beta1/{name=projects/*/locations/*/namespaces/*/services/*/endpoints/*}'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\xf6\x01"D/v1beta1/{resource=projects/*/locations/*/namespaces/*}:getIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:getIamPolicy:\x01*ZU"P/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:getIamPolicy:\x01*'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\xf6\x01"D/v1beta1/{resource=projects/*/locations/*/namespaces/*}:setIamPolicy:\x01*ZT"O/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:setIamPolicy:\x01*ZU"P/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:setIamPolicy:\x01*'
    _globals['_REGISTRATIONSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_REGISTRATIONSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x88\x02"J/v1beta1/{resource=projects/*/locations/*/namespaces/*}:testIamPermissions:\x01*ZZ"U/v1beta1/{resource=projects/*/locations/*/namespaces/*/services/*}:testIamPermissions:\x01*Z["V/v1beta1/{resource=projects/*/locations/*/namespaces/*/workloads/*}:testIamPermissions:\x01*'
    _globals['_CREATENAMESPACEREQUEST']._serialized_start = 508
    _globals['_CREATENAMESPACEREQUEST']._serialized_end = 692
    _globals['_LISTNAMESPACESREQUEST']._serialized_start = 695
    _globals['_LISTNAMESPACESREQUEST']._serialized_end = 870
    _globals['_LISTNAMESPACESRESPONSE']._serialized_start = 872
    _globals['_LISTNAMESPACESRESPONSE']._serialized_end = 991
    _globals['_GETNAMESPACEREQUEST']._serialized_start = 993
    _globals['_GETNAMESPACEREQUEST']._serialized_end = 1079
    _globals['_UPDATENAMESPACEREQUEST']._serialized_start = 1082
    _globals['_UPDATENAMESPACEREQUEST']._serialized_end = 1234
    _globals['_DELETENAMESPACEREQUEST']._serialized_start = 1236
    _globals['_DELETENAMESPACEREQUEST']._serialized_end = 1325
    _globals['_CREATESERVICEREQUEST']._serialized_start = 1328
    _globals['_CREATESERVICEREQUEST']._serialized_end = 1512
    _globals['_LISTSERVICESREQUEST']._serialized_start = 1515
    _globals['_LISTSERVICESREQUEST']._serialized_end = 1696
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 1698
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 1811
    _globals['_GETSERVICEREQUEST']._serialized_start = 1813
    _globals['_GETSERVICEREQUEST']._serialized_end = 1895
    _globals['_UPDATESERVICEREQUEST']._serialized_start = 1898
    _globals['_UPDATESERVICEREQUEST']._serialized_end = 2044
    _globals['_DELETESERVICEREQUEST']._serialized_start = 2046
    _globals['_DELETESERVICEREQUEST']._serialized_end = 2131
    _globals['_CREATEENDPOINTREQUEST']._serialized_start = 2134
    _globals['_CREATEENDPOINTREQUEST']._serialized_end = 2320
    _globals['_LISTENDPOINTSREQUEST']._serialized_start = 2323
    _globals['_LISTENDPOINTSREQUEST']._serialized_end = 2503
    _globals['_LISTENDPOINTSRESPONSE']._serialized_start = 2505
    _globals['_LISTENDPOINTSRESPONSE']._serialized_end = 2621
    _globals['_GETENDPOINTREQUEST']._serialized_start = 2623
    _globals['_GETENDPOINTREQUEST']._serialized_end = 2707
    _globals['_UPDATEENDPOINTREQUEST']._serialized_start = 2710
    _globals['_UPDATEENDPOINTREQUEST']._serialized_end = 2859
    _globals['_DELETEENDPOINTREQUEST']._serialized_start = 2861
    _globals['_DELETEENDPOINTREQUEST']._serialized_end = 2948
    _globals['_REGISTRATIONSERVICE']._serialized_start = 2951
    _globals['_REGISTRATIONSERVICE']._serialized_end = 7393