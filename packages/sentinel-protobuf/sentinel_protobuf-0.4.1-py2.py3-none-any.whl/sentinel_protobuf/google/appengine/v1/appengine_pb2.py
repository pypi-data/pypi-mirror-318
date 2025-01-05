"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/appengine.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.appengine.v1 import application_pb2 as google_dot_appengine_dot_v1_dot_application__pb2
from ....google.appengine.v1 import certificate_pb2 as google_dot_appengine_dot_v1_dot_certificate__pb2
from ....google.appengine.v1 import domain_pb2 as google_dot_appengine_dot_v1_dot_domain__pb2
from ....google.appengine.v1 import domain_mapping_pb2 as google_dot_appengine_dot_v1_dot_domain__mapping__pb2
from ....google.appengine.v1 import firewall_pb2 as google_dot_appengine_dot_v1_dot_firewall__pb2
from ....google.appengine.v1 import instance_pb2 as google_dot_appengine_dot_v1_dot_instance__pb2
from ....google.appengine.v1 import service_pb2 as google_dot_appengine_dot_v1_dot_service__pb2
from ....google.appengine.v1 import version_pb2 as google_dot_appengine_dot_v1_dot_version__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/appengine/v1/appengine.proto\x12\x13google.appengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a%google/appengine/v1/application.proto\x1a%google/appengine/v1/certificate.proto\x1a google/appengine/v1/domain.proto\x1a(google/appengine/v1/domain_mapping.proto\x1a"google/appengine/v1/firewall.proto\x1a"google/appengine/v1/instance.proto\x1a!google/appengine/v1/service.proto\x1a!google/appengine/v1/version.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"%\n\x15GetApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Q\n\x18CreateApplicationRequest\x125\n\x0bapplication\x18\x02 \x01(\x0b2 .google.appengine.v1.Application"\x90\x01\n\x18UpdateApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x125\n\x0bapplication\x18\x02 \x01(\x0b2 .google.appengine.v1.Application\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"(\n\x18RepairApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"L\n\x13ListServicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"_\n\x14ListServicesResponse\x12.\n\x08services\x18\x01 \x03(\x0b2\x1c.google.appengine.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x9d\x01\n\x14UpdateServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07service\x18\x02 \x01(\x0b2\x1c.google.appengine.v1.Service\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x17\n\x0fmigrate_traffic\x18\x04 \x01(\x08"$\n\x14DeleteServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"|\n\x13ListVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12.\n\x04view\x18\x02 \x01(\x0e2 .google.appengine.v1.VersionView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"_\n\x14ListVersionsResponse\x12.\n\x08versions\x18\x01 \x03(\x0b2\x1c.google.appengine.v1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x11GetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x04view\x18\x02 \x01(\x0e2 .google.appengine.v1.VersionView"U\n\x14CreateVersionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b2\x1c.google.appengine.v1.Version"\x84\x01\n\x14UpdateVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x07version\x18\x02 \x01(\x0b2\x1c.google.appengine.v1.Version\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"$\n\x14DeleteVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"M\n\x14ListInstancesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"b\n\x15ListInstancesResponse\x120\n\tinstances\x18\x01 \x03(\x0b2\x1d.google.appengine.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t""\n\x12GetInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"%\n\x15DeleteInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"5\n\x14DebugInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07ssh_key\x18\x02 \x01(\t"j\n\x17ListIngressRulesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x18\n\x10matching_address\x18\x04 \x01(\t"m\n\x18ListIngressRulesResponse\x128\n\ringress_rules\x18\x01 \x03(\x0b2!.google.appengine.v1.FirewallRule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"h\n\x1eBatchUpdateIngressRulesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x128\n\ringress_rules\x18\x02 \x03(\x0b2!.google.appengine.v1.FirewallRule"[\n\x1fBatchUpdateIngressRulesResponse\x128\n\ringress_rules\x18\x01 \x03(\x0b2!.google.appengine.v1.FirewallRule"[\n\x18CreateIngressRuleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12/\n\x04rule\x18\x02 \x01(\x0b2!.google.appengine.v1.FirewallRule"%\n\x15GetIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x8a\x01\n\x18UpdateIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04rule\x18\x02 \x01(\x0b2!.google.appengine.v1.FirewallRule\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"(\n\x18DeleteIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"U\n\x1cListAuthorizedDomainsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"p\n\x1dListAuthorizedDomainsResponse\x126\n\x07domains\x18\x01 \x03(\x0b2%.google.appengine.v1.AuthorizedDomain\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x98\x01\n!ListAuthorizedCertificatesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12<\n\x04view\x18\x04 \x01(\x0e2..google.appengine.v1.AuthorizedCertificateView\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x7f\n"ListAuthorizedCertificatesResponse\x12@\n\x0ccertificates\x18\x01 \x03(\x0b2*.google.appengine.v1.AuthorizedCertificate\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"m\n\x1fGetAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x04view\x18\x02 \x01(\x0e2..google.appengine.v1.AuthorizedCertificateView"u\n"CreateAuthorizedCertificateRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12?\n\x0bcertificate\x18\x02 \x01(\x0b2*.google.appengine.v1.AuthorizedCertificate"\xa4\x01\n"UpdateAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x0bcertificate\x18\x02 \x01(\x0b2*.google.appengine.v1.AuthorizedCertificate\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"2\n"DeleteAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"R\n\x19ListDomainMappingsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x1aListDomainMappingsResponse\x12;\n\x0fdomain_mappings\x18\x01 \x03(\x0b2".google.appengine.v1.DomainMapping\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\'\n\x17GetDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xb0\x01\n\x1aCreateDomainMappingRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12:\n\x0edomain_mapping\x18\x02 \x01(\x0b2".google.appengine.v1.DomainMapping\x12F\n\x11override_strategy\x18\x04 \x01(\x0e2+.google.appengine.v1.DomainOverrideStrategy"\x97\x01\n\x1aUpdateDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x0edomain_mapping\x18\x02 \x01(\x0b2".google.appengine.v1.DomainMapping\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"*\n\x1aDeleteDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t*"\n\x0bVersionView\x12\t\n\x05BASIC\x10\x00\x12\x08\n\x04FULL\x10\x01*H\n\x19AuthorizedCertificateView\x12\x15\n\x11BASIC_CERTIFICATE\x10\x00\x12\x14\n\x10FULL_CERTIFICATE\x10\x01*\\\n\x16DomainOverrideStrategy\x12(\n$UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY\x10\x00\x12\n\n\x06STRICT\x10\x01\x12\x0c\n\x08OVERRIDE\x10\x022\xd1\x06\n\x0cApplications\x12\x80\x01\n\x0eGetApplication\x12*.google.appengine.v1.GetApplicationRequest\x1a .google.appengine.v1.Application" \xdaA\x04name\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/{name=apps/*}\x12\xa5\x01\n\x11CreateApplication\x12-.google.appengine.v1.CreateApplicationRequest\x1a\x1d.google.longrunning.Operation"B\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x17"\x08/v1/apps:\x0bapplication\x12\xae\x01\n\x11UpdateApplication\x12-.google.appengine.v1.UpdateApplicationRequest\x1a\x1d.google.longrunning.Operation"K\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02 2\x11/v1/{name=apps/*}:\x0bapplication\x12\xab\x01\n\x11RepairApplication\x12-.google.appengine.v1.RepairApplicationRequest\x1a\x1d.google.longrunning.Operation"H\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x1d"\x18/v1/{name=apps/*}:repair:\x01*\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xa6\x06\n\x08Services\x12\x89\x01\n\x0cListServices\x12(.google.appengine.v1.ListServicesRequest\x1a).google.appengine.v1.ListServicesResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=apps/*}/services\x12x\n\nGetService\x12&.google.appengine.v1.GetServiceRequest\x1a\x1c.google.appengine.v1.Service"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=apps/*/services/*}\x12\xa9\x01\n\rUpdateService\x12).google.appengine.v1.UpdateServiceRequest\x1a\x1d.google.longrunning.Operation"N\xcaA\x1e\n\x07Service\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\'2\x1c/v1/{name=apps/*/services/*}:\x07service\x12\xae\x01\n\rDeleteService\x12).google.appengine.v1.DeleteServiceRequest\x1a\x1d.google.longrunning.Operation"S\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x1e*\x1c/v1/{name=apps/*/services/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\x8e\x08\n\x08Versions\x12\x94\x01\n\x0cListVersions\x12(.google.appengine.v1.ListVersionsRequest\x1a).google.appengine.v1.ListVersionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/v1/{parent=apps/*/services/*}/versions\x12\x83\x01\n\nGetVersion\x12&.google.appengine.v1.GetVersionRequest\x1a\x1c.google.appengine.v1.Version"/\x82\xd3\xe4\x93\x02)\x12\'/v1/{name=apps/*/services/*/versions/*}\x12\xb8\x01\n\rCreateVersion\x12).google.appengine.v1.CreateVersionRequest\x1a\x1d.google.longrunning.Operation"]\xcaA"\n\x07Version\x12\x17CreateVersionMetadataV1\x82\xd3\xe4\x93\x022"\'/v1/{parent=apps/*/services/*}/versions:\x07version\x12\xb4\x01\n\rUpdateVersion\x12).google.appengine.v1.UpdateVersionRequest\x1a\x1d.google.longrunning.Operation"Y\xcaA\x1e\n\x07Version\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x0222\'/v1/{name=apps/*/services/*/versions/*}:\x07version\x12\xb9\x01\n\rDeleteVersion\x12).google.appengine.v1.DeleteVersionRequest\x1a\x1d.google.longrunning.Operation"^\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02)*\'/v1/{name=apps/*/services/*/versions/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\x8d\x07\n\tInstances\x12\xa3\x01\n\rListInstances\x12).google.appengine.v1.ListInstancesRequest\x1a*.google.appengine.v1.ListInstancesResponse";\x82\xd3\xe4\x93\x025\x123/v1/{parent=apps/*/services/*/versions/*}/instances\x12\x92\x01\n\x0bGetInstance\x12\'.google.appengine.v1.GetInstanceRequest\x1a\x1d.google.appengine.v1.Instance";\x82\xd3\xe4\x93\x025\x123/v1/{name=apps/*/services/*/versions/*/instances/*}\x12\xc7\x01\n\x0eDeleteInstance\x12*.google.appengine.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"j\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x025*3/v1/{name=apps/*/services/*/versions/*/instances/*}\x12\xc1\x01\n\rDebugInstance\x12).google.appengine.v1.DebugInstanceRequest\x1a\x1d.google.longrunning.Operation"f\xcaA\x1f\n\x08Instance\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02>"9/v1/{name=apps/*/services/*/versions/*/instances/*}:debug:\x01*\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\x96\t\n\x08Firewall\x12\xa2\x01\n\x10ListIngressRules\x12,.google.appengine.v1.ListIngressRulesRequest\x1a-.google.appengine.v1.ListIngressRulesResponse"1\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=apps/*}/firewall/ingressRules\x12\xc4\x01\n\x17BatchUpdateIngressRules\x123.google.appengine.v1.BatchUpdateIngressRulesRequest\x1a4.google.appengine.v1.BatchUpdateIngressRulesResponse">\x82\xd3\xe4\x93\x028"3/v1/{name=apps/*/firewall/ingressRules}:batchUpdate:\x01*\x12\x9e\x01\n\x11CreateIngressRule\x12-.google.appengine.v1.CreateIngressRuleRequest\x1a!.google.appengine.v1.FirewallRule"7\x82\xd3\xe4\x93\x021")/v1/{parent=apps/*}/firewall/ingressRules:\x04rule\x12\x92\x01\n\x0eGetIngressRule\x12*.google.appengine.v1.GetIngressRuleRequest\x1a!.google.appengine.v1.FirewallRule"1\x82\xd3\xe4\x93\x02+\x12)/v1/{name=apps/*/firewall/ingressRules/*}\x12\x9e\x01\n\x11UpdateIngressRule\x12-.google.appengine.v1.UpdateIngressRuleRequest\x1a!.google.appengine.v1.FirewallRule"7\x82\xd3\xe4\x93\x0212)/v1/{name=apps/*/firewall/ingressRules/*}:\x04rule\x12\x8d\x01\n\x11DeleteIngressRule\x12-.google.appengine.v1.DeleteIngressRuleRequest\x1a\x16.google.protobuf.Empty"1\x82\xd3\xe4\x93\x02+*)/v1/{name=apps/*/firewall/ingressRules/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xfc\x02\n\x11AuthorizedDomains\x12\xad\x01\n\x15ListAuthorizedDomains\x121.google.appengine.v1.ListAuthorizedDomainsRequest\x1a2.google.appengine.v1.ListAuthorizedDomainsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/v1/{parent=apps/*}/authorizedDomains\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xf9\x08\n\x16AuthorizedCertificates\x12\xc1\x01\n\x1aListAuthorizedCertificates\x126.google.appengine.v1.ListAuthorizedCertificatesRequest\x1a7.google.appengine.v1.ListAuthorizedCertificatesResponse"2\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=apps/*}/authorizedCertificates\x12\xb0\x01\n\x18GetAuthorizedCertificate\x124.google.appengine.v1.GetAuthorizedCertificateRequest\x1a*.google.appengine.v1.AuthorizedCertificate"2\x82\xd3\xe4\x93\x02,\x12*/v1/{name=apps/*/authorizedCertificates/*}\x12\xc3\x01\n\x1bCreateAuthorizedCertificate\x127.google.appengine.v1.CreateAuthorizedCertificateRequest\x1a*.google.appengine.v1.AuthorizedCertificate"?\x82\xd3\xe4\x93\x029"*/v1/{parent=apps/*}/authorizedCertificates:\x0bcertificate\x12\xc3\x01\n\x1bUpdateAuthorizedCertificate\x127.google.appengine.v1.UpdateAuthorizedCertificateRequest\x1a*.google.appengine.v1.AuthorizedCertificate"?\x82\xd3\xe4\x93\x0292*/v1/{name=apps/*/authorizedCertificates/*}:\x0bcertificate\x12\xa2\x01\n\x1bDeleteAuthorizedCertificate\x127.google.appengine.v1.DeleteAuthorizedCertificateRequest\x1a\x16.google.protobuf.Empty"2\x82\xd3\xe4\x93\x02,**/v1/{name=apps/*/authorizedCertificates/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xd9\x08\n\x0eDomainMappings\x12\xa1\x01\n\x12ListDomainMappings\x12..google.appengine.v1.ListDomainMappingsRequest\x1a/.google.appengine.v1.ListDomainMappingsResponse"*\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=apps/*}/domainMappings\x12\x90\x01\n\x10GetDomainMapping\x12,.google.appengine.v1.GetDomainMappingRequest\x1a".google.appengine.v1.DomainMapping"*\x82\xd3\xe4\x93\x02$\x12"/v1/{name=apps/*/domainMappings/*}\x12\xc8\x01\n\x13CreateDomainMapping\x12/.google.appengine.v1.CreateDomainMappingRequest\x1a\x1d.google.longrunning.Operation"a\xcaA$\n\rDomainMapping\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x024""/v1/{parent=apps/*}/domainMappings:\x0edomain_mapping\x12\xc8\x01\n\x13UpdateDomainMapping\x12/.google.appengine.v1.UpdateDomainMappingRequest\x1a\x1d.google.longrunning.Operation"a\xcaA$\n\rDomainMapping\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x0242"/v1/{name=apps/*/domainMappings/*}:\x0edomain_mapping\x12\xc0\x01\n\x13DeleteDomainMapping\x12/.google.appengine.v1.DeleteDomainMappingRequest\x1a\x1d.google.longrunning.Operation"Y\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02$*"/v1/{name=apps/*/domainMappings/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xbf\x01\n\x17com.google.appengine.v1B\x0eAppengineProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.appengine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x0eAppengineProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_APPLICATIONS']._loaded_options = None
    _globals['_APPLICATIONS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_APPLICATIONS'].methods_by_name['GetApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['GetApplication']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/{name=apps/*}'
    _globals['_APPLICATIONS'].methods_by_name['CreateApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['CreateApplication']._serialized_options = b'\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x17"\x08/v1/apps:\x0bapplication'
    _globals['_APPLICATIONS'].methods_by_name['UpdateApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['UpdateApplication']._serialized_options = b'\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02 2\x11/v1/{name=apps/*}:\x0bapplication'
    _globals['_APPLICATIONS'].methods_by_name['RepairApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['RepairApplication']._serialized_options = b'\xcaA"\n\x0bApplication\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x1d"\x18/v1/{name=apps/*}:repair:\x01*'
    _globals['_SERVICES']._loaded_options = None
    _globals['_SERVICES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_SERVICES'].methods_by_name['ListServices']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['ListServices']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=apps/*}/services'
    _globals['_SERVICES'].methods_by_name['GetService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['GetService']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=apps/*/services/*}'
    _globals['_SERVICES'].methods_by_name['UpdateService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['UpdateService']._serialized_options = b"\xcaA\x1e\n\x07Service\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02'2\x1c/v1/{name=apps/*/services/*}:\x07service"
    _globals['_SERVICES'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['DeleteService']._serialized_options = b'\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02\x1e*\x1c/v1/{name=apps/*/services/*}'
    _globals['_VERSIONS']._loaded_options = None
    _globals['_VERSIONS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_VERSIONS'].methods_by_name['ListVersions']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['ListVersions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/v1/{parent=apps/*/services/*}/versions"
    _globals['_VERSIONS'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['GetVersion']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/v1/{name=apps/*/services/*/versions/*}"
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._serialized_options = b'\xcaA"\n\x07Version\x12\x17CreateVersionMetadataV1\x82\xd3\xe4\x93\x022"\'/v1/{parent=apps/*/services/*}/versions:\x07version'
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._serialized_options = b"\xcaA\x1e\n\x07Version\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x0222'/v1/{name=apps/*/services/*/versions/*}:\x07version"
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._serialized_options = b"\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02)*'/v1/{name=apps/*/services/*/versions/*}"
    _globals['_INSTANCES']._loaded_options = None
    _globals['_INSTANCES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_INSTANCES'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['ListInstances']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/v1/{parent=apps/*/services/*/versions/*}/instances'
    _globals['_INSTANCES'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['GetInstance']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/v1/{name=apps/*/services/*/versions/*/instances/*}'
    _globals['_INSTANCES'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x025*3/v1/{name=apps/*/services/*/versions/*/instances/*}'
    _globals['_INSTANCES'].methods_by_name['DebugInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['DebugInstance']._serialized_options = b'\xcaA\x1f\n\x08Instance\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02>"9/v1/{name=apps/*/services/*/versions/*/instances/*}:debug:\x01*'
    _globals['_FIREWALL']._loaded_options = None
    _globals['_FIREWALL']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_FIREWALL'].methods_by_name['ListIngressRules']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['ListIngressRules']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=apps/*}/firewall/ingressRules'
    _globals['_FIREWALL'].methods_by_name['BatchUpdateIngressRules']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['BatchUpdateIngressRules']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/v1/{name=apps/*/firewall/ingressRules}:batchUpdate:\x01*'
    _globals['_FIREWALL'].methods_by_name['CreateIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['CreateIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x021")/v1/{parent=apps/*}/firewall/ingressRules:\x04rule'
    _globals['_FIREWALL'].methods_by_name['GetIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['GetIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/v1/{name=apps/*/firewall/ingressRules/*}'
    _globals['_FIREWALL'].methods_by_name['UpdateIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['UpdateIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x0212)/v1/{name=apps/*/firewall/ingressRules/*}:\x04rule'
    _globals['_FIREWALL'].methods_by_name['DeleteIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['DeleteIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x02+*)/v1/{name=apps/*/firewall/ingressRules/*}'
    _globals['_AUTHORIZEDDOMAINS']._loaded_options = None
    _globals['_AUTHORIZEDDOMAINS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_AUTHORIZEDDOMAINS'].methods_by_name['ListAuthorizedDomains']._loaded_options = None
    _globals['_AUTHORIZEDDOMAINS'].methods_by_name['ListAuthorizedDomains']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1/{parent=apps/*}/authorizedDomains"
    _globals['_AUTHORIZEDCERTIFICATES']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['ListAuthorizedCertificates']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['ListAuthorizedCertificates']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=apps/*}/authorizedCertificates'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['GetAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['GetAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/v1/{name=apps/*/authorizedCertificates/*}'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['CreateAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['CreateAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x029"*/v1/{parent=apps/*}/authorizedCertificates:\x0bcertificate'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['UpdateAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['UpdateAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x0292*/v1/{name=apps/*/authorizedCertificates/*}:\x0bcertificate'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['DeleteAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['DeleteAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x02,**/v1/{name=apps/*/authorizedCertificates/*}'
    _globals['_DOMAINMAPPINGS']._loaded_options = None
    _globals['_DOMAINMAPPINGS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_DOMAINMAPPINGS'].methods_by_name['ListDomainMappings']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['ListDomainMappings']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=apps/*}/domainMappings'
    _globals['_DOMAINMAPPINGS'].methods_by_name['GetDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['GetDomainMapping']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1/{name=apps/*/domainMappings/*}'
    _globals['_DOMAINMAPPINGS'].methods_by_name['CreateDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['CreateDomainMapping']._serialized_options = b'\xcaA$\n\rDomainMapping\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x024""/v1/{parent=apps/*}/domainMappings:\x0edomain_mapping'
    _globals['_DOMAINMAPPINGS'].methods_by_name['UpdateDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['UpdateDomainMapping']._serialized_options = b'\xcaA$\n\rDomainMapping\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x0242"/v1/{name=apps/*/domainMappings/*}:\x0edomain_mapping'
    _globals['_DOMAINMAPPINGS'].methods_by_name['DeleteDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['DeleteDomainMapping']._serialized_options = b'\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\x82\xd3\xe4\x93\x02$*"/v1/{name=apps/*/domainMappings/*}'
    _globals['_VERSIONVIEW']._serialized_start = 4390
    _globals['_VERSIONVIEW']._serialized_end = 4424
    _globals['_AUTHORIZEDCERTIFICATEVIEW']._serialized_start = 4426
    _globals['_AUTHORIZEDCERTIFICATEVIEW']._serialized_end = 4498
    _globals['_DOMAINOVERRIDESTRATEGY']._serialized_start = 4500
    _globals['_DOMAINOVERRIDESTRATEGY']._serialized_end = 4592
    _globals['_GETAPPLICATIONREQUEST']._serialized_start = 511
    _globals['_GETAPPLICATIONREQUEST']._serialized_end = 548
    _globals['_CREATEAPPLICATIONREQUEST']._serialized_start = 550
    _globals['_CREATEAPPLICATIONREQUEST']._serialized_end = 631
    _globals['_UPDATEAPPLICATIONREQUEST']._serialized_start = 634
    _globals['_UPDATEAPPLICATIONREQUEST']._serialized_end = 778
    _globals['_REPAIRAPPLICATIONREQUEST']._serialized_start = 780
    _globals['_REPAIRAPPLICATIONREQUEST']._serialized_end = 820
    _globals['_LISTSERVICESREQUEST']._serialized_start = 822
    _globals['_LISTSERVICESREQUEST']._serialized_end = 898
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 900
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 995
    _globals['_GETSERVICEREQUEST']._serialized_start = 997
    _globals['_GETSERVICEREQUEST']._serialized_end = 1030
    _globals['_UPDATESERVICEREQUEST']._serialized_start = 1033
    _globals['_UPDATESERVICEREQUEST']._serialized_end = 1190
    _globals['_DELETESERVICEREQUEST']._serialized_start = 1192
    _globals['_DELETESERVICEREQUEST']._serialized_end = 1228
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 1230
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 1354
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 1356
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 1451
    _globals['_GETVERSIONREQUEST']._serialized_start = 1453
    _globals['_GETVERSIONREQUEST']._serialized_end = 1534
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1536
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1621
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1624
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1756
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1758
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1794
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1796
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1873
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1875
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1973
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1975
    _globals['_GETINSTANCEREQUEST']._serialized_end = 2009
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 2011
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 2048
    _globals['_DEBUGINSTANCEREQUEST']._serialized_start = 2050
    _globals['_DEBUGINSTANCEREQUEST']._serialized_end = 2103
    _globals['_LISTINGRESSRULESREQUEST']._serialized_start = 2105
    _globals['_LISTINGRESSRULESREQUEST']._serialized_end = 2211
    _globals['_LISTINGRESSRULESRESPONSE']._serialized_start = 2213
    _globals['_LISTINGRESSRULESRESPONSE']._serialized_end = 2322
    _globals['_BATCHUPDATEINGRESSRULESREQUEST']._serialized_start = 2324
    _globals['_BATCHUPDATEINGRESSRULESREQUEST']._serialized_end = 2428
    _globals['_BATCHUPDATEINGRESSRULESRESPONSE']._serialized_start = 2430
    _globals['_BATCHUPDATEINGRESSRULESRESPONSE']._serialized_end = 2521
    _globals['_CREATEINGRESSRULEREQUEST']._serialized_start = 2523
    _globals['_CREATEINGRESSRULEREQUEST']._serialized_end = 2614
    _globals['_GETINGRESSRULEREQUEST']._serialized_start = 2616
    _globals['_GETINGRESSRULEREQUEST']._serialized_end = 2653
    _globals['_UPDATEINGRESSRULEREQUEST']._serialized_start = 2656
    _globals['_UPDATEINGRESSRULEREQUEST']._serialized_end = 2794
    _globals['_DELETEINGRESSRULEREQUEST']._serialized_start = 2796
    _globals['_DELETEINGRESSRULEREQUEST']._serialized_end = 2836
    _globals['_LISTAUTHORIZEDDOMAINSREQUEST']._serialized_start = 2838
    _globals['_LISTAUTHORIZEDDOMAINSREQUEST']._serialized_end = 2923
    _globals['_LISTAUTHORIZEDDOMAINSRESPONSE']._serialized_start = 2925
    _globals['_LISTAUTHORIZEDDOMAINSRESPONSE']._serialized_end = 3037
    _globals['_LISTAUTHORIZEDCERTIFICATESREQUEST']._serialized_start = 3040
    _globals['_LISTAUTHORIZEDCERTIFICATESREQUEST']._serialized_end = 3192
    _globals['_LISTAUTHORIZEDCERTIFICATESRESPONSE']._serialized_start = 3194
    _globals['_LISTAUTHORIZEDCERTIFICATESRESPONSE']._serialized_end = 3321
    _globals['_GETAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3323
    _globals['_GETAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3432
    _globals['_CREATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3434
    _globals['_CREATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3551
    _globals['_UPDATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3554
    _globals['_UPDATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3718
    _globals['_DELETEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3720
    _globals['_DELETEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3770
    _globals['_LISTDOMAINMAPPINGSREQUEST']._serialized_start = 3772
    _globals['_LISTDOMAINMAPPINGSREQUEST']._serialized_end = 3854
    _globals['_LISTDOMAINMAPPINGSRESPONSE']._serialized_start = 3856
    _globals['_LISTDOMAINMAPPINGSRESPONSE']._serialized_end = 3970
    _globals['_GETDOMAINMAPPINGREQUEST']._serialized_start = 3972
    _globals['_GETDOMAINMAPPINGREQUEST']._serialized_end = 4011
    _globals['_CREATEDOMAINMAPPINGREQUEST']._serialized_start = 4014
    _globals['_CREATEDOMAINMAPPINGREQUEST']._serialized_end = 4190
    _globals['_UPDATEDOMAINMAPPINGREQUEST']._serialized_start = 4193
    _globals['_UPDATEDOMAINMAPPINGREQUEST']._serialized_end = 4344
    _globals['_DELETEDOMAINMAPPINGREQUEST']._serialized_start = 4346
    _globals['_DELETEDOMAINMAPPINGREQUEST']._serialized_end = 4388
    _globals['_APPLICATIONS']._serialized_start = 4595
    _globals['_APPLICATIONS']._serialized_end = 5444
    _globals['_SERVICES']._serialized_start = 5447
    _globals['_SERVICES']._serialized_end = 6253
    _globals['_VERSIONS']._serialized_start = 6256
    _globals['_VERSIONS']._serialized_end = 7294
    _globals['_INSTANCES']._serialized_start = 7297
    _globals['_INSTANCES']._serialized_end = 8206
    _globals['_FIREWALL']._serialized_start = 8209
    _globals['_FIREWALL']._serialized_end = 9383
    _globals['_AUTHORIZEDDOMAINS']._serialized_start = 9386
    _globals['_AUTHORIZEDDOMAINS']._serialized_end = 9766
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_start = 9769
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_end = 10914
    _globals['_DOMAINMAPPINGS']._serialized_start = 10917
    _globals['_DOMAINMAPPINGS']._serialized_end = 12030