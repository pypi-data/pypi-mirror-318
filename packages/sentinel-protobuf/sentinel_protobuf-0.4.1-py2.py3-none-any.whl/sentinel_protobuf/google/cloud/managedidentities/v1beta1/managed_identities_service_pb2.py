"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/managedidentities/v1beta1/managed_identities_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.managedidentities.v1beta1 import resource_pb2 as google_dot_cloud_dot_managedidentities_dot_v1beta1_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/cloud/managedidentities/v1beta1/managed_identities_service.proto\x12&google.cloud.managedidentities.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/managedidentities/v1beta1/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x01\n\nOpMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x05 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x06 \x01(\tB\x03\xe0A\x03"\xc0\x01\n\x1eCreateMicrosoftAdDomainRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'managedidentities.googleapis.com/Domain\x12\x18\n\x0bdomain_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\x06domain\x18\x03 \x01(\x0b2..google.cloud.managedidentities.v1beta1.DomainB\x03\xe0A\x02"Z\n\x19ResetAdminPasswordRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain".\n\x1aResetAdminPasswordResponse\x12\x10\n\x08password\x18\x01 \x01(\t"\x9e\x01\n\x12ListDomainsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'managedidentities.googleapis.com/Domain\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x84\x01\n\x13ListDomainsResponse\x12?\n\x07domains\x18\x01 \x03(\x0b2..google.cloud.managedidentities.v1beta1.Domain\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x10GetDomainRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain"\x90\x01\n\x13UpdateDomainRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12C\n\x06domain\x18\x02 \x01(\x0b2..google.cloud.managedidentities.v1beta1.DomainB\x03\xe0A\x02"T\n\x13DeleteDomainRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain"\x96\x01\n\x12AttachTrustRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain\x12A\n\x05trust\x18\x02 \x01(\x0b2-.google.cloud.managedidentities.v1beta1.TrustB\x03\xe0A\x02"\x9f\x01\n\x17ReconfigureTrustRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain\x12\x1f\n\x12target_domain_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12$\n\x17target_dns_ip_addresses\x18\x03 \x03(\tB\x03\xe0A\x02"\x96\x01\n\x12DetachTrustRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain\x12A\n\x05trust\x18\x02 \x01(\x0b2-.google.cloud.managedidentities.v1beta1.TrustB\x03\xe0A\x02"\x98\x01\n\x14ValidateTrustRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'managedidentities.googleapis.com/Domain\x12A\n\x05trust\x18\x02 \x01(\x0b2-.google.cloud.managedidentities.v1beta1.TrustB\x03\xe0A\x022\xe5\x12\n\x18ManagedIdentitiesService\x12\xfa\x01\n\x17CreateMicrosoftAdDomain\x12F.google.cloud.managedidentities.v1beta1.CreateMicrosoftAdDomainRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\x19parent,domain_name,domain\x82\xd3\xe4\x93\x02?"5/v1beta1/{parent=projects/*/locations/global}/domains:\x06domain\x12\xf7\x01\n\x12ResetAdminPassword\x12A.google.cloud.managedidentities.v1beta1.ResetAdminPasswordRequest\x1aB.google.cloud.managedidentities.v1beta1.ResetAdminPasswordResponse"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1beta1/{name=projects/*/locations/global/domains/*}:resetAdminPassword:\x01*\x12\xce\x01\n\x0bListDomains\x12:.google.cloud.managedidentities.v1beta1.ListDomainsRequest\x1a;.google.cloud.managedidentities.v1beta1.ListDomainsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/global}/domains\x12\xbb\x01\n\tGetDomain\x128.google.cloud.managedidentities.v1beta1.GetDomainRequest\x1a..google.cloud.managedidentities.v1beta1.Domain"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/global/domains/*}\x12\xe4\x01\n\x0cUpdateDomain\x12;.google.cloud.managedidentities.v1beta1.UpdateDomainRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\x12domain,update_mask\x82\xd3\xe4\x93\x02F2</v1beta1/{domain.name=projects/*/locations/global/domains/*}:\x06domain\x12\xd6\x01\n\x0cDeleteDomain\x12;.google.cloud.managedidentities.v1beta1.DeleteDomainRequest\x1a\x1d.google.longrunning.Operation"j\xcaA#\n\x15google.protobuf.Empty\x12\nOpMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/global/domains/*}\x12\xda\x01\n\x0bAttachTrust\x12:.google.cloud.managedidentities.v1beta1.AttachTrustRequest\x1a\x1d.google.longrunning.Operation"p\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/global/domains/*}:attachTrust:\x01*\x12\x8f\x02\n\x10ReconfigureTrust\x12?.google.cloud.managedidentities.v1beta1.ReconfigureTrustRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA/name,target_domain_name,target_dns_ip_addresses\x82\xd3\xe4\x93\x02K"F/v1beta1/{name=projects/*/locations/global/domains/*}:reconfigureTrust:\x01*\x12\xda\x01\n\x0bDetachTrust\x12:.google.cloud.managedidentities.v1beta1.DetachTrustRequest\x1a\x1d.google.longrunning.Operation"p\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/global/domains/*}:detachTrust:\x01*\x12\xe0\x01\n\rValidateTrust\x12<.google.cloud.managedidentities.v1beta1.ValidateTrustRequest\x1a\x1d.google.longrunning.Operation"r\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/global/domains/*}:validateTrust:\x01*\x1aT\xcaA managedidentities.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xac\x02\n*com.google.cloud.managedidentities.v1beta1B\x1dManagedIdentitiesServiceProtoP\x01ZXcloud.google.com/go/managedidentities/apiv1beta1/managedidentitiespb;managedidentitiespb\xa2\x02\x04GCMI\xaa\x02&Google.Cloud.ManagedIdentities.V1Beta1\xca\x02&Google\\Cloud\\ManagedIdentities\\V1beta1\xea\x02)Google::Cloud::ManagedIdentities::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.managedidentities.v1beta1.managed_identities_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.managedidentities.v1beta1B\x1dManagedIdentitiesServiceProtoP\x01ZXcloud.google.com/go/managedidentities/apiv1beta1/managedidentitiespb;managedidentitiespb\xa2\x02\x04GCMI\xaa\x02&Google.Cloud.ManagedIdentities.V1Beta1\xca\x02&Google\\Cloud\\ManagedIdentities\\V1beta1\xea\x02)Google::Cloud::ManagedIdentities::V1beta1'
    _globals['_OPMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'managedidentities.googleapis.com/Domain"
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['domain_name']._loaded_options = None
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['domain_name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['domain']._loaded_options = None
    _globals['_CREATEMICROSOFTADDOMAINREQUEST'].fields_by_name['domain']._serialized_options = b'\xe0A\x02'
    _globals['_RESETADMINPASSWORDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESETADMINPASSWORDREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_LISTDOMAINSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOMAINSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'managedidentities.googleapis.com/Domain"
    _globals['_GETDOMAINREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOMAINREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_UPDATEDOMAINREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDOMAINREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDOMAINREQUEST'].fields_by_name['domain']._loaded_options = None
    _globals['_UPDATEDOMAINREQUEST'].fields_by_name['domain']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOMAINREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOMAINREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_ATTACHTRUSTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ATTACHTRUSTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_ATTACHTRUSTREQUEST'].fields_by_name['trust']._loaded_options = None
    _globals['_ATTACHTRUSTREQUEST'].fields_by_name['trust']._serialized_options = b'\xe0A\x02'
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['target_domain_name']._loaded_options = None
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['target_domain_name']._serialized_options = b'\xe0A\x02'
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['target_dns_ip_addresses']._loaded_options = None
    _globals['_RECONFIGURETRUSTREQUEST'].fields_by_name['target_dns_ip_addresses']._serialized_options = b'\xe0A\x02'
    _globals['_DETACHTRUSTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DETACHTRUSTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_DETACHTRUSTREQUEST'].fields_by_name['trust']._loaded_options = None
    _globals['_DETACHTRUSTREQUEST'].fields_by_name['trust']._serialized_options = b'\xe0A\x02'
    _globals['_VALIDATETRUSTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VALIDATETRUSTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'managedidentities.googleapis.com/Domain"
    _globals['_VALIDATETRUSTREQUEST'].fields_by_name['trust']._loaded_options = None
    _globals['_VALIDATETRUSTREQUEST'].fields_by_name['trust']._serialized_options = b'\xe0A\x02'
    _globals['_MANAGEDIDENTITIESSERVICE']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE']._serialized_options = b'\xcaA managedidentities.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['CreateMicrosoftAdDomain']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['CreateMicrosoftAdDomain']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\x19parent,domain_name,domain\x82\xd3\xe4\x93\x02?"5/v1beta1/{parent=projects/*/locations/global}/domains:\x06domain'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ResetAdminPassword']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ResetAdminPassword']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1beta1/{name=projects/*/locations/global/domains/*}:resetAdminPassword:\x01*'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ListDomains']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ListDomains']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/global}/domains'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['GetDomain']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['GetDomain']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/global/domains/*}'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['UpdateDomain']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['UpdateDomain']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\x12domain,update_mask\x82\xd3\xe4\x93\x02F2</v1beta1/{domain.name=projects/*/locations/global/domains/*}:\x06domain'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['DeleteDomain']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['DeleteDomain']._serialized_options = b'\xcaA#\n\x15google.protobuf.Empty\x12\nOpMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/global/domains/*}'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['AttachTrust']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['AttachTrust']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/global/domains/*}:attachTrust:\x01*'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ReconfigureTrust']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ReconfigureTrust']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA/name,target_domain_name,target_dns_ip_addresses\x82\xd3\xe4\x93\x02K"F/v1beta1/{name=projects/*/locations/global/domains/*}:reconfigureTrust:\x01*'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['DetachTrust']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['DetachTrust']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/global/domains/*}:detachTrust:\x01*'
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ValidateTrust']._loaded_options = None
    _globals['_MANAGEDIDENTITIESSERVICE'].methods_by_name['ValidateTrust']._serialized_options = b'\xcaA\x14\n\x06Domain\x12\nOpMetadata\xdaA\nname,trust\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/global/domains/*}:validateTrust:\x01*'
    _globals['_OPMETADATA']._serialized_start = 390
    _globals['_OPMETADATA']._serialized_end = 610
    _globals['_CREATEMICROSOFTADDOMAINREQUEST']._serialized_start = 613
    _globals['_CREATEMICROSOFTADDOMAINREQUEST']._serialized_end = 805
    _globals['_RESETADMINPASSWORDREQUEST']._serialized_start = 807
    _globals['_RESETADMINPASSWORDREQUEST']._serialized_end = 897
    _globals['_RESETADMINPASSWORDRESPONSE']._serialized_start = 899
    _globals['_RESETADMINPASSWORDRESPONSE']._serialized_end = 945
    _globals['_LISTDOMAINSREQUEST']._serialized_start = 948
    _globals['_LISTDOMAINSREQUEST']._serialized_end = 1106
    _globals['_LISTDOMAINSRESPONSE']._serialized_start = 1109
    _globals['_LISTDOMAINSRESPONSE']._serialized_end = 1241
    _globals['_GETDOMAINREQUEST']._serialized_start = 1243
    _globals['_GETDOMAINREQUEST']._serialized_end = 1324
    _globals['_UPDATEDOMAINREQUEST']._serialized_start = 1327
    _globals['_UPDATEDOMAINREQUEST']._serialized_end = 1471
    _globals['_DELETEDOMAINREQUEST']._serialized_start = 1473
    _globals['_DELETEDOMAINREQUEST']._serialized_end = 1557
    _globals['_ATTACHTRUSTREQUEST']._serialized_start = 1560
    _globals['_ATTACHTRUSTREQUEST']._serialized_end = 1710
    _globals['_RECONFIGURETRUSTREQUEST']._serialized_start = 1713
    _globals['_RECONFIGURETRUSTREQUEST']._serialized_end = 1872
    _globals['_DETACHTRUSTREQUEST']._serialized_start = 1875
    _globals['_DETACHTRUSTREQUEST']._serialized_end = 2025
    _globals['_VALIDATETRUSTREQUEST']._serialized_start = 2028
    _globals['_VALIDATETRUSTREQUEST']._serialized_end = 2180
    _globals['_MANAGEDIDENTITIESSERVICE']._serialized_start = 2183
    _globals['_MANAGEDIDENTITIESSERVICE']._serialized_end = 4588