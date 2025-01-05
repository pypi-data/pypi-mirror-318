"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/appengine.proto')
_sym_db = _symbol_database.Default()
from ....google.appengine.v1beta import application_pb2 as google_dot_appengine_dot_v1beta_dot_application__pb2
from ....google.appengine.v1beta import certificate_pb2 as google_dot_appengine_dot_v1beta_dot_certificate__pb2
from ....google.appengine.v1beta import domain_pb2 as google_dot_appengine_dot_v1beta_dot_domain__pb2
from ....google.appengine.v1beta import domain_mapping_pb2 as google_dot_appengine_dot_v1beta_dot_domain__mapping__pb2
from ....google.appengine.v1beta import firewall_pb2 as google_dot_appengine_dot_v1beta_dot_firewall__pb2
from ....google.appengine.v1beta import instance_pb2 as google_dot_appengine_dot_v1beta_dot_instance__pb2
from ....google.appengine.v1beta import version_pb2 as google_dot_appengine_dot_v1beta_dot_version__pb2
from ....google.appengine.v1beta import service_pb2 as google_dot_appengine_dot_v1beta_dot_service__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/appengine/v1beta/appengine.proto\x12\x17google.appengine.v1beta\x1a)google/appengine/v1beta/application.proto\x1a)google/appengine/v1beta/certificate.proto\x1a$google/appengine/v1beta/domain.proto\x1a,google/appengine/v1beta/domain_mapping.proto\x1a&google/appengine/v1beta/firewall.proto\x1a&google/appengine/v1beta/instance.proto\x1a%google/appengine/v1beta/version.proto\x1a%google/appengine/v1beta/service.proto\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto"%\n\x15GetApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"U\n\x18CreateApplicationRequest\x129\n\x0bapplication\x18\x02 \x01(\x0b2$.google.appengine.v1beta.Application"\x94\x01\n\x18UpdateApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x0bapplication\x18\x02 \x01(\x0b2$.google.appengine.v1beta.Application\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"(\n\x18RepairApplicationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"L\n\x13ListServicesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"c\n\x14ListServicesResponse\x122\n\x08services\x18\x01 \x03(\x0b2 .google.appengine.v1beta.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xa1\x01\n\x14UpdateServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x121\n\x07service\x18\x02 \x01(\x0b2 .google.appengine.v1beta.Service\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x17\n\x0fmigrate_traffic\x18\x04 \x01(\x08"$\n\x14DeleteServiceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x80\x01\n\x13ListVersionsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x122\n\x04view\x18\x02 \x01(\x0e2$.google.appengine.v1beta.VersionView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"c\n\x14ListVersionsResponse\x122\n\x08versions\x18\x01 \x03(\x0b2 .google.appengine.v1beta.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x11GetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x122\n\x04view\x18\x02 \x01(\x0e2$.google.appengine.v1beta.VersionView"Y\n\x14CreateVersionRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x121\n\x07version\x18\x02 \x01(\x0b2 .google.appengine.v1beta.Version"\x88\x01\n\x14UpdateVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x121\n\x07version\x18\x02 \x01(\x0b2 .google.appengine.v1beta.Version\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"$\n\x14DeleteVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"M\n\x14ListInstancesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"f\n\x15ListInstancesResponse\x124\n\tinstances\x18\x01 \x03(\x0b2!.google.appengine.v1beta.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t""\n\x12GetInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"%\n\x15DeleteInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"5\n\x14DebugInstanceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07ssh_key\x18\x02 \x01(\t"j\n\x17ListIngressRulesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x18\n\x10matching_address\x18\x04 \x01(\t"q\n\x18ListIngressRulesResponse\x12<\n\ringress_rules\x18\x01 \x03(\x0b2%.google.appengine.v1beta.FirewallRule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"l\n\x1eBatchUpdateIngressRulesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\ringress_rules\x18\x02 \x03(\x0b2%.google.appengine.v1beta.FirewallRule"_\n\x1fBatchUpdateIngressRulesResponse\x12<\n\ringress_rules\x18\x01 \x03(\x0b2%.google.appengine.v1beta.FirewallRule"_\n\x18CreateIngressRuleRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x123\n\x04rule\x18\x02 \x01(\x0b2%.google.appengine.v1beta.FirewallRule"%\n\x15GetIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x8e\x01\n\x18UpdateIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x123\n\x04rule\x18\x02 \x01(\x0b2%.google.appengine.v1beta.FirewallRule\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"(\n\x18DeleteIngressRuleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"U\n\x1cListAuthorizedDomainsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"t\n\x1dListAuthorizedDomainsResponse\x12:\n\x07domains\x18\x01 \x03(\x0b2).google.appengine.v1beta.AuthorizedDomain\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9c\x01\n!ListAuthorizedCertificatesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x04view\x18\x04 \x01(\x0e22.google.appengine.v1beta.AuthorizedCertificateView\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x83\x01\n"ListAuthorizedCertificatesResponse\x12D\n\x0ccertificates\x18\x01 \x03(\x0b2..google.appengine.v1beta.AuthorizedCertificate\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"q\n\x1fGetAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x04view\x18\x02 \x01(\x0e22.google.appengine.v1beta.AuthorizedCertificateView"y\n"CreateAuthorizedCertificateRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12C\n\x0bcertificate\x18\x02 \x01(\x0b2..google.appengine.v1beta.AuthorizedCertificate"\xa8\x01\n"UpdateAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\x0bcertificate\x18\x02 \x01(\x0b2..google.appengine.v1beta.AuthorizedCertificate\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"2\n"DeleteAuthorizedCertificateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"R\n\x19ListDomainMappingsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"v\n\x1aListDomainMappingsResponse\x12?\n\x0fdomain_mappings\x18\x01 \x03(\x0b2&.google.appengine.v1beta.DomainMapping\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\'\n\x17GetDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xb8\x01\n\x1aCreateDomainMappingRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12>\n\x0edomain_mapping\x18\x02 \x01(\x0b2&.google.appengine.v1beta.DomainMapping\x12J\n\x11override_strategy\x18\x04 \x01(\x0e2/.google.appengine.v1beta.DomainOverrideStrategy"\x9b\x01\n\x1aUpdateDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0edomain_mapping\x18\x02 \x01(\x0b2&.google.appengine.v1beta.DomainMapping\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"*\n\x1aDeleteDomainMappingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t*"\n\x0bVersionView\x12\t\n\x05BASIC\x10\x00\x12\x08\n\x04FULL\x10\x01*H\n\x19AuthorizedCertificateView\x12\x15\n\x11BASIC_CERTIFICATE\x10\x00\x12\x14\n\x10FULL_CERTIFICATE\x10\x01*\\\n\x16DomainOverrideStrategy\x12(\n$UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY\x10\x00\x12\n\n\x06STRICT\x10\x01\x12\x0c\n\x08OVERRIDE\x10\x022\xfa\x06\n\x0cApplications\x12\x85\x01\n\x0eGetApplication\x12..google.appengine.v1beta.GetApplicationRequest\x1a$.google.appengine.v1beta.Application"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta/{name=apps/*}\x12\xb1\x01\n\x11CreateApplication\x121.google.appengine.v1beta.CreateApplicationRequest\x1a\x1d.google.longrunning.Operation"J\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02\x1b"\x0c/v1beta/apps:\x0bapplication\x12\xba\x01\n\x11UpdateApplication\x121.google.appengine.v1beta.UpdateApplicationRequest\x1a\x1d.google.longrunning.Operation"S\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02$2\x15/v1beta/{name=apps/*}:\x0bapplication\x12\xb7\x01\n\x11RepairApplication\x121.google.appengine.v1beta.RepairApplicationRequest\x1a\x1d.google.longrunning.Operation"P\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02!"\x1c/v1beta/{name=apps/*}:repair:\x01*\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xd7\x06\n\x08Services\x12\x95\x01\n\x0cListServices\x12,.google.appengine.v1beta.ListServicesRequest\x1a-.google.appengine.v1beta.ListServicesResponse"(\x82\xd3\xe4\x93\x02"\x12 /v1beta/{parent=apps/*}/services\x12\x84\x01\n\nGetService\x12*.google.appengine.v1beta.GetServiceRequest\x1a .google.appengine.v1beta.Service"(\x82\xd3\xe4\x93\x02"\x12 /v1beta/{name=apps/*/services/*}\x12\xb5\x01\n\rUpdateService\x12-.google.appengine.v1beta.UpdateServiceRequest\x1a\x1d.google.longrunning.Operation"V\xcaA"\n\x07Service\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02+2 /v1beta/{name=apps/*/services/*}:\x07service\x12\xba\x01\n\rDeleteService\x12-.google.appengine.v1beta.DeleteServiceRequest\x1a\x1d.google.longrunning.Operation"[\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02"* /v1beta/{name=apps/*/services/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xca\x08\n\x08Versions\x12\xa0\x01\n\x0cListVersions\x12,.google.appengine.v1beta.ListVersionsRequest\x1a-.google.appengine.v1beta.ListVersionsResponse"3\x82\xd3\xe4\x93\x02-\x12+/v1beta/{parent=apps/*/services/*}/versions\x12\x8f\x01\n\nGetVersion\x12*.google.appengine.v1beta.GetVersionRequest\x1a .google.appengine.v1beta.Version"3\x82\xd3\xe4\x93\x02-\x12+/v1beta/{name=apps/*/services/*/versions/*}\x12\xc4\x01\n\rCreateVersion\x12-.google.appengine.v1beta.CreateVersionRequest\x1a\x1d.google.longrunning.Operation"e\xcaA&\n\x07Version\x12\x1bCreateVersionMetadataV1Beta\x82\xd3\xe4\x93\x026"+/v1beta/{parent=apps/*/services/*}/versions:\x07version\x12\xc0\x01\n\rUpdateVersion\x12-.google.appengine.v1beta.UpdateVersionRequest\x1a\x1d.google.longrunning.Operation"a\xcaA"\n\x07Version\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x0262+/v1beta/{name=apps/*/services/*/versions/*}:\x07version\x12\xc5\x01\n\rDeleteVersion\x12-.google.appengine.v1beta.DeleteVersionRequest\x1a\x1d.google.longrunning.Operation"f\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02-*+/v1beta/{name=apps/*/services/*/versions/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xbd\x07\n\tInstances\x12\xaf\x01\n\rListInstances\x12-.google.appengine.v1beta.ListInstancesRequest\x1a..google.appengine.v1beta.ListInstancesResponse"?\x82\xd3\xe4\x93\x029\x127/v1beta/{parent=apps/*/services/*/versions/*}/instances\x12\x9e\x01\n\x0bGetInstance\x12+.google.appengine.v1beta.GetInstanceRequest\x1a!.google.appengine.v1beta.Instance"?\x82\xd3\xe4\x93\x029\x127/v1beta/{name=apps/*/services/*/versions/*/instances/*}\x12\xd3\x01\n\x0eDeleteInstance\x12..google.appengine.v1beta.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"r\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x029*7/v1beta/{name=apps/*/services/*/versions/*/instances/*}\x12\xcd\x01\n\rDebugInstance\x12-.google.appengine.v1beta.DebugInstanceRequest\x1a\x1d.google.longrunning.Operation"n\xcaA#\n\x08Instance\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02B"=/v1beta/{name=apps/*/services/*/versions/*/instances/*}:debug:\x01*\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xda\t\n\x08Firewall\x12\xae\x01\n\x10ListIngressRules\x120.google.appengine.v1beta.ListIngressRulesRequest\x1a1.google.appengine.v1beta.ListIngressRulesResponse"5\x82\xd3\xe4\x93\x02/\x12-/v1beta/{parent=apps/*}/firewall/ingressRules\x12\xd0\x01\n\x17BatchUpdateIngressRules\x127.google.appengine.v1beta.BatchUpdateIngressRulesRequest\x1a8.google.appengine.v1beta.BatchUpdateIngressRulesResponse"B\x82\xd3\xe4\x93\x02<"7/v1beta/{name=apps/*/firewall/ingressRules}:batchUpdate:\x01*\x12\xaa\x01\n\x11CreateIngressRule\x121.google.appengine.v1beta.CreateIngressRuleRequest\x1a%.google.appengine.v1beta.FirewallRule";\x82\xd3\xe4\x93\x025"-/v1beta/{parent=apps/*}/firewall/ingressRules:\x04rule\x12\x9e\x01\n\x0eGetIngressRule\x12..google.appengine.v1beta.GetIngressRuleRequest\x1a%.google.appengine.v1beta.FirewallRule"5\x82\xd3\xe4\x93\x02/\x12-/v1beta/{name=apps/*/firewall/ingressRules/*}\x12\xaa\x01\n\x11UpdateIngressRule\x121.google.appengine.v1beta.UpdateIngressRuleRequest\x1a%.google.appengine.v1beta.FirewallRule";\x82\xd3\xe4\x93\x0252-/v1beta/{name=apps/*/firewall/ingressRules/*}:\x04rule\x12\x95\x01\n\x11DeleteIngressRule\x121.google.appengine.v1beta.DeleteIngressRuleRequest\x1a\x16.google.protobuf.Empty"5\x82\xd3\xe4\x93\x02/*-/v1beta/{name=apps/*/firewall/ingressRules/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\x88\x03\n\x11AuthorizedDomains\x12\xb9\x01\n\x15ListAuthorizedDomains\x125.google.appengine.v1beta.ListAuthorizedDomainsRequest\x1a6.google.appengine.v1beta.ListAuthorizedDomainsResponse"1\x82\xd3\xe4\x93\x02+\x12)/v1beta/{parent=apps/*}/authorizedDomains\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\xb1\t\n\x16AuthorizedCertificates\x12\xcd\x01\n\x1aListAuthorizedCertificates\x12:.google.appengine.v1beta.ListAuthorizedCertificatesRequest\x1a;.google.appengine.v1beta.ListAuthorizedCertificatesResponse"6\x82\xd3\xe4\x93\x020\x12./v1beta/{parent=apps/*}/authorizedCertificates\x12\xbc\x01\n\x18GetAuthorizedCertificate\x128.google.appengine.v1beta.GetAuthorizedCertificateRequest\x1a..google.appengine.v1beta.AuthorizedCertificate"6\x82\xd3\xe4\x93\x020\x12./v1beta/{name=apps/*/authorizedCertificates/*}\x12\xcf\x01\n\x1bCreateAuthorizedCertificate\x12;.google.appengine.v1beta.CreateAuthorizedCertificateRequest\x1a..google.appengine.v1beta.AuthorizedCertificate"C\x82\xd3\xe4\x93\x02="./v1beta/{parent=apps/*}/authorizedCertificates:\x0bcertificate\x12\xcf\x01\n\x1bUpdateAuthorizedCertificate\x12;.google.appengine.v1beta.UpdateAuthorizedCertificateRequest\x1a..google.appengine.v1beta.AuthorizedCertificate"C\x82\xd3\xe4\x93\x02=2./v1beta/{name=apps/*/authorizedCertificates/*}:\x0bcertificate\x12\xaa\x01\n\x1bDeleteAuthorizedCertificate\x12;.google.appengine.v1beta.DeleteAuthorizedCertificateRequest\x1a\x16.google.protobuf.Empty"6\x82\xd3\xe4\x93\x020*./v1beta/{name=apps/*/authorizedCertificates/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only2\x95\t\n\x0eDomainMappings\x12\xad\x01\n\x12ListDomainMappings\x122.google.appengine.v1beta.ListDomainMappingsRequest\x1a3.google.appengine.v1beta.ListDomainMappingsResponse".\x82\xd3\xe4\x93\x02(\x12&/v1beta/{parent=apps/*}/domainMappings\x12\x9c\x01\n\x10GetDomainMapping\x120.google.appengine.v1beta.GetDomainMappingRequest\x1a&.google.appengine.v1beta.DomainMapping".\x82\xd3\xe4\x93\x02(\x12&/v1beta/{name=apps/*/domainMappings/*}\x12\xd4\x01\n\x13CreateDomainMapping\x123.google.appengine.v1beta.CreateDomainMappingRequest\x1a\x1d.google.longrunning.Operation"i\xcaA(\n\rDomainMapping\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x028"&/v1beta/{parent=apps/*}/domainMappings:\x0edomain_mapping\x12\xd4\x01\n\x13UpdateDomainMapping\x123.google.appengine.v1beta.UpdateDomainMappingRequest\x1a\x1d.google.longrunning.Operation"i\xcaA(\n\rDomainMapping\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x0282&/v1beta/{name=apps/*/domainMappings/*}:\x0edomain_mapping\x12\xcc\x01\n\x13DeleteDomainMapping\x123.google.appengine.v1beta.DeleteDomainMappingRequest\x1a\x1d.google.longrunning.Operation"a\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02(*&/v1beta/{name=apps/*/domainMappings/*}\x1a\xb6\x01\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xd4\x01\n\x1bcom.google.appengine.v1betaB\x0eAppengineProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.appengine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0eAppengineProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_APPLICATIONS']._loaded_options = None
    _globals['_APPLICATIONS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_APPLICATIONS'].methods_by_name['GetApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['GetApplication']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta/{name=apps/*}'
    _globals['_APPLICATIONS'].methods_by_name['CreateApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['CreateApplication']._serialized_options = b'\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02\x1b"\x0c/v1beta/apps:\x0bapplication'
    _globals['_APPLICATIONS'].methods_by_name['UpdateApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['UpdateApplication']._serialized_options = b'\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02$2\x15/v1beta/{name=apps/*}:\x0bapplication'
    _globals['_APPLICATIONS'].methods_by_name['RepairApplication']._loaded_options = None
    _globals['_APPLICATIONS'].methods_by_name['RepairApplication']._serialized_options = b'\xcaA&\n\x0bApplication\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02!"\x1c/v1beta/{name=apps/*}:repair:\x01*'
    _globals['_SERVICES']._loaded_options = None
    _globals['_SERVICES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_SERVICES'].methods_by_name['ListServices']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['ListServices']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /v1beta/{parent=apps/*}/services'
    _globals['_SERVICES'].methods_by_name['GetService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['GetService']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /v1beta/{name=apps/*/services/*}'
    _globals['_SERVICES'].methods_by_name['UpdateService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['UpdateService']._serialized_options = b'\xcaA"\n\x07Service\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02+2 /v1beta/{name=apps/*/services/*}:\x07service'
    _globals['_SERVICES'].methods_by_name['DeleteService']._loaded_options = None
    _globals['_SERVICES'].methods_by_name['DeleteService']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02"* /v1beta/{name=apps/*/services/*}'
    _globals['_VERSIONS']._loaded_options = None
    _globals['_VERSIONS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_VERSIONS'].methods_by_name['ListVersions']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['ListVersions']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/v1beta/{parent=apps/*/services/*}/versions'
    _globals['_VERSIONS'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['GetVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/v1beta/{name=apps/*/services/*/versions/*}'
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['CreateVersion']._serialized_options = b'\xcaA&\n\x07Version\x12\x1bCreateVersionMetadataV1Beta\x82\xd3\xe4\x93\x026"+/v1beta/{parent=apps/*/services/*}/versions:\x07version'
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['UpdateVersion']._serialized_options = b'\xcaA"\n\x07Version\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x0262+/v1beta/{name=apps/*/services/*/versions/*}:\x07version'
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._loaded_options = None
    _globals['_VERSIONS'].methods_by_name['DeleteVersion']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02-*+/v1beta/{name=apps/*/services/*/versions/*}'
    _globals['_INSTANCES']._loaded_options = None
    _globals['_INSTANCES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_INSTANCES'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['ListInstances']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/v1beta/{parent=apps/*/services/*/versions/*}/instances'
    _globals['_INSTANCES'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['GetInstance']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/v1beta/{name=apps/*/services/*/versions/*/instances/*}'
    _globals['_INSTANCES'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x029*7/v1beta/{name=apps/*/services/*/versions/*/instances/*}'
    _globals['_INSTANCES'].methods_by_name['DebugInstance']._loaded_options = None
    _globals['_INSTANCES'].methods_by_name['DebugInstance']._serialized_options = b'\xcaA#\n\x08Instance\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02B"=/v1beta/{name=apps/*/services/*/versions/*/instances/*}:debug:\x01*'
    _globals['_FIREWALL']._loaded_options = None
    _globals['_FIREWALL']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_FIREWALL'].methods_by_name['ListIngressRules']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['ListIngressRules']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1beta/{parent=apps/*}/firewall/ingressRules'
    _globals['_FIREWALL'].methods_by_name['BatchUpdateIngressRules']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['BatchUpdateIngressRules']._serialized_options = b'\x82\xd3\xe4\x93\x02<"7/v1beta/{name=apps/*/firewall/ingressRules}:batchUpdate:\x01*'
    _globals['_FIREWALL'].methods_by_name['CreateIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['CreateIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x025"-/v1beta/{parent=apps/*}/firewall/ingressRules:\x04rule'
    _globals['_FIREWALL'].methods_by_name['GetIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['GetIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1beta/{name=apps/*/firewall/ingressRules/*}'
    _globals['_FIREWALL'].methods_by_name['UpdateIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['UpdateIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x0252-/v1beta/{name=apps/*/firewall/ingressRules/*}:\x04rule'
    _globals['_FIREWALL'].methods_by_name['DeleteIngressRule']._loaded_options = None
    _globals['_FIREWALL'].methods_by_name['DeleteIngressRule']._serialized_options = b'\x82\xd3\xe4\x93\x02/*-/v1beta/{name=apps/*/firewall/ingressRules/*}'
    _globals['_AUTHORIZEDDOMAINS']._loaded_options = None
    _globals['_AUTHORIZEDDOMAINS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_AUTHORIZEDDOMAINS'].methods_by_name['ListAuthorizedDomains']._loaded_options = None
    _globals['_AUTHORIZEDDOMAINS'].methods_by_name['ListAuthorizedDomains']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/v1beta/{parent=apps/*}/authorizedDomains'
    _globals['_AUTHORIZEDCERTIFICATES']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['ListAuthorizedCertificates']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['ListAuthorizedCertificates']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta/{parent=apps/*}/authorizedCertificates'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['GetAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['GetAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta/{name=apps/*/authorizedCertificates/*}'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['CreateAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['CreateAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x02="./v1beta/{parent=apps/*}/authorizedCertificates:\x0bcertificate'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['UpdateAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['UpdateAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x02=2./v1beta/{name=apps/*/authorizedCertificates/*}:\x0bcertificate'
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['DeleteAuthorizedCertificate']._loaded_options = None
    _globals['_AUTHORIZEDCERTIFICATES'].methods_by_name['DeleteAuthorizedCertificate']._serialized_options = b'\x82\xd3\xe4\x93\x020*./v1beta/{name=apps/*/authorizedCertificates/*}'
    _globals['_DOMAINMAPPINGS']._loaded_options = None
    _globals['_DOMAINMAPPINGS']._serialized_options = b'\xcaA\x18appengine.googleapis.com\xd2A\x97\x01https://www.googleapis.com/auth/appengine.admin,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_DOMAINMAPPINGS'].methods_by_name['ListDomainMappings']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['ListDomainMappings']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/v1beta/{parent=apps/*}/domainMappings'
    _globals['_DOMAINMAPPINGS'].methods_by_name['GetDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['GetDomainMapping']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/v1beta/{name=apps/*/domainMappings/*}'
    _globals['_DOMAINMAPPINGS'].methods_by_name['CreateDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['CreateDomainMapping']._serialized_options = b'\xcaA(\n\rDomainMapping\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x028"&/v1beta/{parent=apps/*}/domainMappings:\x0edomain_mapping'
    _globals['_DOMAINMAPPINGS'].methods_by_name['UpdateDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['UpdateDomainMapping']._serialized_options = b'\xcaA(\n\rDomainMapping\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x0282&/v1beta/{name=apps/*/domainMappings/*}:\x0edomain_mapping'
    _globals['_DOMAINMAPPINGS'].methods_by_name['DeleteDomainMapping']._loaded_options = None
    _globals['_DOMAINMAPPINGS'].methods_by_name['DeleteDomainMapping']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17OperationMetadataV1Beta\x82\xd3\xe4\x93\x02(*&/v1beta/{name=apps/*/domainMappings/*}'
    _globals['_VERSIONVIEW']._serialized_start = 4532
    _globals['_VERSIONVIEW']._serialized_end = 4566
    _globals['_AUTHORIZEDCERTIFICATEVIEW']._serialized_start = 4568
    _globals['_AUTHORIZEDCERTIFICATEVIEW']._serialized_end = 4640
    _globals['_DOMAINOVERRIDESTRATEGY']._serialized_start = 4642
    _globals['_DOMAINOVERRIDESTRATEGY']._serialized_end = 4734
    _globals['_GETAPPLICATIONREQUEST']._serialized_start = 551
    _globals['_GETAPPLICATIONREQUEST']._serialized_end = 588
    _globals['_CREATEAPPLICATIONREQUEST']._serialized_start = 590
    _globals['_CREATEAPPLICATIONREQUEST']._serialized_end = 675
    _globals['_UPDATEAPPLICATIONREQUEST']._serialized_start = 678
    _globals['_UPDATEAPPLICATIONREQUEST']._serialized_end = 826
    _globals['_REPAIRAPPLICATIONREQUEST']._serialized_start = 828
    _globals['_REPAIRAPPLICATIONREQUEST']._serialized_end = 868
    _globals['_LISTSERVICESREQUEST']._serialized_start = 870
    _globals['_LISTSERVICESREQUEST']._serialized_end = 946
    _globals['_LISTSERVICESRESPONSE']._serialized_start = 948
    _globals['_LISTSERVICESRESPONSE']._serialized_end = 1047
    _globals['_GETSERVICEREQUEST']._serialized_start = 1049
    _globals['_GETSERVICEREQUEST']._serialized_end = 1082
    _globals['_UPDATESERVICEREQUEST']._serialized_start = 1085
    _globals['_UPDATESERVICEREQUEST']._serialized_end = 1246
    _globals['_DELETESERVICEREQUEST']._serialized_start = 1248
    _globals['_DELETESERVICEREQUEST']._serialized_end = 1284
    _globals['_LISTVERSIONSREQUEST']._serialized_start = 1287
    _globals['_LISTVERSIONSREQUEST']._serialized_end = 1415
    _globals['_LISTVERSIONSRESPONSE']._serialized_start = 1417
    _globals['_LISTVERSIONSRESPONSE']._serialized_end = 1516
    _globals['_GETVERSIONREQUEST']._serialized_start = 1518
    _globals['_GETVERSIONREQUEST']._serialized_end = 1603
    _globals['_CREATEVERSIONREQUEST']._serialized_start = 1605
    _globals['_CREATEVERSIONREQUEST']._serialized_end = 1694
    _globals['_UPDATEVERSIONREQUEST']._serialized_start = 1697
    _globals['_UPDATEVERSIONREQUEST']._serialized_end = 1833
    _globals['_DELETEVERSIONREQUEST']._serialized_start = 1835
    _globals['_DELETEVERSIONREQUEST']._serialized_end = 1871
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1873
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1950
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1952
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 2054
    _globals['_GETINSTANCEREQUEST']._serialized_start = 2056
    _globals['_GETINSTANCEREQUEST']._serialized_end = 2090
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 2092
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 2129
    _globals['_DEBUGINSTANCEREQUEST']._serialized_start = 2131
    _globals['_DEBUGINSTANCEREQUEST']._serialized_end = 2184
    _globals['_LISTINGRESSRULESREQUEST']._serialized_start = 2186
    _globals['_LISTINGRESSRULESREQUEST']._serialized_end = 2292
    _globals['_LISTINGRESSRULESRESPONSE']._serialized_start = 2294
    _globals['_LISTINGRESSRULESRESPONSE']._serialized_end = 2407
    _globals['_BATCHUPDATEINGRESSRULESREQUEST']._serialized_start = 2409
    _globals['_BATCHUPDATEINGRESSRULESREQUEST']._serialized_end = 2517
    _globals['_BATCHUPDATEINGRESSRULESRESPONSE']._serialized_start = 2519
    _globals['_BATCHUPDATEINGRESSRULESRESPONSE']._serialized_end = 2614
    _globals['_CREATEINGRESSRULEREQUEST']._serialized_start = 2616
    _globals['_CREATEINGRESSRULEREQUEST']._serialized_end = 2711
    _globals['_GETINGRESSRULEREQUEST']._serialized_start = 2713
    _globals['_GETINGRESSRULEREQUEST']._serialized_end = 2750
    _globals['_UPDATEINGRESSRULEREQUEST']._serialized_start = 2753
    _globals['_UPDATEINGRESSRULEREQUEST']._serialized_end = 2895
    _globals['_DELETEINGRESSRULEREQUEST']._serialized_start = 2897
    _globals['_DELETEINGRESSRULEREQUEST']._serialized_end = 2937
    _globals['_LISTAUTHORIZEDDOMAINSREQUEST']._serialized_start = 2939
    _globals['_LISTAUTHORIZEDDOMAINSREQUEST']._serialized_end = 3024
    _globals['_LISTAUTHORIZEDDOMAINSRESPONSE']._serialized_start = 3026
    _globals['_LISTAUTHORIZEDDOMAINSRESPONSE']._serialized_end = 3142
    _globals['_LISTAUTHORIZEDCERTIFICATESREQUEST']._serialized_start = 3145
    _globals['_LISTAUTHORIZEDCERTIFICATESREQUEST']._serialized_end = 3301
    _globals['_LISTAUTHORIZEDCERTIFICATESRESPONSE']._serialized_start = 3304
    _globals['_LISTAUTHORIZEDCERTIFICATESRESPONSE']._serialized_end = 3435
    _globals['_GETAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3437
    _globals['_GETAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3550
    _globals['_CREATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3552
    _globals['_CREATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3673
    _globals['_UPDATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3676
    _globals['_UPDATEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3844
    _globals['_DELETEAUTHORIZEDCERTIFICATEREQUEST']._serialized_start = 3846
    _globals['_DELETEAUTHORIZEDCERTIFICATEREQUEST']._serialized_end = 3896
    _globals['_LISTDOMAINMAPPINGSREQUEST']._serialized_start = 3898
    _globals['_LISTDOMAINMAPPINGSREQUEST']._serialized_end = 3980
    _globals['_LISTDOMAINMAPPINGSRESPONSE']._serialized_start = 3982
    _globals['_LISTDOMAINMAPPINGSRESPONSE']._serialized_end = 4100
    _globals['_GETDOMAINMAPPINGREQUEST']._serialized_start = 4102
    _globals['_GETDOMAINMAPPINGREQUEST']._serialized_end = 4141
    _globals['_CREATEDOMAINMAPPINGREQUEST']._serialized_start = 4144
    _globals['_CREATEDOMAINMAPPINGREQUEST']._serialized_end = 4328
    _globals['_UPDATEDOMAINMAPPINGREQUEST']._serialized_start = 4331
    _globals['_UPDATEDOMAINMAPPINGREQUEST']._serialized_end = 4486
    _globals['_DELETEDOMAINMAPPINGREQUEST']._serialized_start = 4488
    _globals['_DELETEDOMAINMAPPINGREQUEST']._serialized_end = 4530
    _globals['_APPLICATIONS']._serialized_start = 4737
    _globals['_APPLICATIONS']._serialized_end = 5627
    _globals['_SERVICES']._serialized_start = 5630
    _globals['_SERVICES']._serialized_end = 6485
    _globals['_VERSIONS']._serialized_start = 6488
    _globals['_VERSIONS']._serialized_end = 7586
    _globals['_INSTANCES']._serialized_start = 7589
    _globals['_INSTANCES']._serialized_end = 8546
    _globals['_FIREWALL']._serialized_start = 8549
    _globals['_FIREWALL']._serialized_end = 9791
    _globals['_AUTHORIZEDDOMAINS']._serialized_start = 9794
    _globals['_AUTHORIZEDDOMAINS']._serialized_end = 10186
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_start = 10189
    _globals['_AUTHORIZEDCERTIFICATES']._serialized_end = 11390
    _globals['_DOMAINMAPPINGS']._serialized_start = 11393
    _globals['_DOMAINMAPPINGS']._serialized_end = 12566