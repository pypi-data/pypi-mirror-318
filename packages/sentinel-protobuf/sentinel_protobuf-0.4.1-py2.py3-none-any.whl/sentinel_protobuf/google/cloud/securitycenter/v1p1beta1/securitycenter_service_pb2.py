"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1p1beta1/securitycenter_service.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.securitycenter.v1p1beta1 import notification_message_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_notification__message__pb2
from .....google.cloud.securitycenter.v1p1beta1 import run_asset_discovery_response_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_run__asset__discovery__response__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1p1beta1 import asset_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_asset__pb2
from .....google.cloud.securitycenter.v1p1beta1 import finding_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_finding__pb2
from .....google.cloud.securitycenter.v1p1beta1 import folder_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_folder__pb2
from .....google.cloud.securitycenter.v1p1beta1 import notification_config_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_notification__config__pb2
from .....google.cloud.securitycenter.v1p1beta1 import organization_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_organization__settings__pb2
from .....google.cloud.securitycenter.v1p1beta1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_security__marks__pb2
from .....google.cloud.securitycenter.v1p1beta1 import source_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_source__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.cloud.securitycenter.v1p1beta1.notification_message_pb2 import *
from ....google.cloud.securitycenter.v1p1beta1.run_asset_discovery_response_pb2 import *
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/securitycenter/v1p1beta1/securitycenter_service.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a@google/cloud/securitycenter/v1p1beta1/notification_message.proto\x1aHgoogle/cloud/securitycenter/v1p1beta1/run_asset_discovery_response.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/securitycenter/v1p1beta1/asset.proto\x1a3google/cloud/securitycenter/v1p1beta1/finding.proto\x1a2google/cloud/securitycenter/v1p1beta1/folder.proto\x1a?google/cloud/securitycenter/v1p1beta1/notification_config.proto\x1aAgoogle/cloud/securitycenter/v1p1beta1/organization_settings.proto\x1a:google/cloud/securitycenter/v1p1beta1/security_marks.proto\x1a2google/cloud/securitycenter/v1p1beta1/source.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x01\n\x14CreateFindingRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x17\n\nfinding_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\x07finding\x18\x03 \x01(\x0b2..google.cloud.securitycenter.v1p1beta1.FindingB\x03\xe0A\x02"\xe0\x01\n\x1fCreateNotificationConfigRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x16\n\tconfig_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12[\n\x13notification_config\x18\x03 \x01(\x0b29.google.cloud.securitycenter.v1p1beta1.NotificationConfigB\x03\xe0A\x02"\xa3\x01\n\x13CreateSourceRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12B\n\x06source\x18\x02 \x01(\x0b2-.google.cloud.securitycenter.v1p1beta1.SourceB\x03\xe0A\x02"i\n\x1fDeleteNotificationConfigRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0securitycenter.googleapis.com/NotificationConfig"f\n\x1cGetNotificationConfigRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0securitycenter.googleapis.com/NotificationConfig"j\n\x1eGetOrganizationSettingsRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2securitycenter.googleapis.com/OrganizationSettings"N\n\x10GetSourceRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source"\x83\x02\n\x12GroupAssetsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#securitycenter.googleapis.com/Asset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x15\n\x08group_by\x18\x03 \x01(\tB\x03\xe0A\x02\x123\n\x10compare_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12-\n\tread_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x11\n\tpage_size\x18\x08 \x01(\x05"\xbf\x01\n\x13GroupAssetsResponse\x12L\n\x10group_by_results\x18\x01 \x03(\x0b22.google.cloud.securitycenter.v1p1beta1.GroupResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05"\x86\x02\n\x14GroupFindingsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x15\n\x08group_by\x18\x03 \x01(\tB\x03\xe0A\x02\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x10compare_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x11\n\tpage_size\x18\x08 \x01(\x05"\xc1\x01\n\x15GroupFindingsResponse\x12L\n\x10group_by_results\x18\x01 \x03(\x0b22.google.cloud.securitycenter.v1p1beta1.GroupResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05"\xbf\x01\n\x0bGroupResult\x12V\n\nproperties\x18\x01 \x03(\x0b2B.google.cloud.securitycenter.v1p1beta1.GroupResult.PropertiesEntry\x12\r\n\x05count\x18\x02 \x01(\x03\x1aI\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01"\x91\x01\n\x1eListNotificationConfigsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x93\x01\n\x1fListNotificationConfigsResponse\x12W\n\x14notification_configs\x18\x01 \x03(\x0b29.google.cloud.securitycenter.v1p1beta1.NotificationConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"y\n\x12ListSourcesRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$securitycenter.googleapis.com/Source\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x07 \x01(\x05"n\n\x13ListSourcesResponse\x12>\n\x07sources\x18\x01 \x03(\x0b2-.google.cloud.securitycenter.v1p1beta1.Source\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xad\x02\n\x11ListAssetsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#securitycenter.googleapis.com/Asset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x10compare_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\nfield_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x12\n\npage_token\x18\x08 \x01(\t\x12\x11\n\tpage_size\x18\t \x01(\x05"\xd8\x03\n\x12ListAssetsResponse\x12g\n\x13list_assets_results\x18\x01 \x03(\x0b2J.google.cloud.securitycenter.v1p1beta1.ListAssetsResponse.ListAssetsResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05\x1a\xfc\x01\n\x10ListAssetsResult\x12;\n\x05asset\x18\x01 \x01(\x0b2,.google.cloud.securitycenter.v1p1beta1.Asset\x12l\n\x0cstate_change\x18\x02 \x01(\x0e2V.google.cloud.securitycenter.v1p1beta1.ListAssetsResponse.ListAssetsResult.StateChange"=\n\x0bStateChange\x12\n\n\x06UNUSED\x10\x00\x12\t\n\x05ADDED\x10\x01\x12\x0b\n\x07REMOVED\x10\x02\x12\n\n\x06ACTIVE\x10\x03"\xb0\x02\n\x13ListFindingsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x10compare_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\nfield_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x12\n\npage_token\x18\x08 \x01(\t\x12\x11\n\tpage_size\x18\t \x01(\x05"\xab\x06\n\x14ListFindingsResponse\x12m\n\x15list_findings_results\x18\x01 \x03(\x0b2N.google.cloud.securitycenter.v1p1beta1.ListFindingsResponse.ListFindingsResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05\x1a\xc7\x04\n\x12ListFindingsResult\x12?\n\x07finding\x18\x01 \x01(\x0b2..google.cloud.securitycenter.v1p1beta1.Finding\x12p\n\x0cstate_change\x18\x02 \x01(\x0e2Z.google.cloud.securitycenter.v1p1beta1.ListFindingsResponse.ListFindingsResult.StateChange\x12n\n\x08resource\x18\x03 \x01(\x0b2W.google.cloud.securitycenter.v1p1beta1.ListFindingsResponse.ListFindingsResult.ResourceB\x03\xe0A\x03\x1a\xbe\x01\n\x08Resource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cproject_name\x18\x02 \x01(\t\x12\x1c\n\x14project_display_name\x18\x03 \x01(\t\x12\x13\n\x0bparent_name\x18\x04 \x01(\t\x12\x1b\n\x13parent_display_name\x18\x05 \x01(\t\x12>\n\x07folders\x18\n \x03(\x0b2-.google.cloud.securitycenter.v1p1beta1.Folder"M\n\x0bStateChange\x12\n\n\x06UNUSED\x10\x00\x12\x0b\n\x07CHANGED\x10\x01\x12\r\n\tUNCHANGED\x10\x02\x12\t\n\x05ADDED\x10\x03\x12\x0b\n\x07REMOVED\x10\x04"\xd4\x01\n\x16SetFindingStateRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%securitycenter.googleapis.com/Finding\x12H\n\x05state\x18\x02 \x01(\x0e24.google.cloud.securitycenter.v1p1beta1.Finding.StateB\x03\xe0A\x02\x123\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"d\n\x18RunAssetDiscoveryRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization"\x8d\x01\n\x14UpdateFindingRequest\x12D\n\x07finding\x18\x01 \x01(\x0b2..google.cloud.securitycenter.v1p1beta1.FindingB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xaf\x01\n\x1fUpdateNotificationConfigRequest\x12[\n\x13notification_config\x18\x01 \x01(\x0b29.google.cloud.securitycenter.v1p1beta1.NotificationConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb5\x01\n!UpdateOrganizationSettingsRequest\x12_\n\x15organization_settings\x18\x01 \x01(\x0b2;.google.cloud.securitycenter.v1p1beta1.OrganizationSettingsB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8a\x01\n\x13UpdateSourceRequest\x12B\n\x06source\x18\x01 \x01(\x0b2-.google.cloud.securitycenter.v1p1beta1.SourceB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xd0\x01\n\x1aUpdateSecurityMarksRequest\x12Q\n\x0esecurity_marks\x18\x01 \x01(\x0b24.google.cloud.securitycenter.v1p1beta1.SecurityMarksB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xf83\n\x0eSecurityCenter\x12\xc6\x01\n\x0cCreateSource\x12:.google.cloud.securitycenter.v1p1beta1.CreateSourceRequest\x1a-.google.cloud.securitycenter.v1p1beta1.Source"K\xdaA\rparent,source\x82\xd3\xe4\x93\x025"+/v1p1beta1/{parent=organizations/*}/sources:\x06source\x12\xfd\x01\n\rCreateFinding\x12;.google.cloud.securitycenter.v1p1beta1.CreateFindingRequest\x1a..google.cloud.securitycenter.v1p1beta1.Finding"\x7f\xdaA\x19parent,finding_id,finding\xdaA\x19parent,finding,finding_id\x82\xd3\xe4\x93\x02A"6/v1p1beta1/{parent=organizations/*/sources/*}/findings:\x07finding\x12\xb8\x02\n\x18CreateNotificationConfig\x12F.google.cloud.securitycenter.v1p1beta1.CreateNotificationConfigRequest\x1a9.google.cloud.securitycenter.v1p1beta1.NotificationConfig"\x98\x01\xdaA$parent,config_id,notification_config\xdaA\x1aparent,notification_config\x82\xd3\xe4\x93\x02N"7/v1p1beta1/{parent=organizations/*}/notificationConfigs:\x13notification_config\x12\xc2\x01\n\x18DeleteNotificationConfig\x12F.google.cloud.securitycenter.v1p1beta1.DeleteNotificationConfigRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1p1beta1/{name=organizations/*/notificationConfigs/*}\x12\x9d\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"R\xdaA\x08resource\x82\xd3\xe4\x93\x02A"</v1p1beta1/{resource=organizations/*/sources/*}:getIamPolicy:\x01*\x12\xdf\x01\n\x15GetNotificationConfig\x12C.google.cloud.securitycenter.v1p1beta1.GetNotificationConfigRequest\x1a9.google.cloud.securitycenter.v1p1beta1.NotificationConfig"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1p1beta1/{name=organizations/*/notificationConfigs/*}\x12\xe4\x01\n\x17GetOrganizationSettings\x12E.google.cloud.securitycenter.v1p1beta1.GetOrganizationSettingsRequest\x1a;.google.cloud.securitycenter.v1p1beta1.OrganizationSettings"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1p1beta1/{name=organizations/*/organizationSettings}\x12\xaf\x01\n\tGetSource\x127.google.cloud.securitycenter.v1p1beta1.GetSourceRequest\x1a-.google.cloud.securitycenter.v1p1beta1.Source":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1p1beta1/{name=organizations/*/sources/*}\x12\xa6\x02\n\x0bGroupAssets\x129.google.cloud.securitycenter.v1p1beta1.GroupAssetsRequest\x1a:.google.cloud.securitycenter.v1p1beta1.GroupAssetsResponse"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x01"0/v1p1beta1/{parent=organizations/*}/assets:group:\x01*Z/"*/v1p1beta1/{parent=folders/*}/assets:group:\x01*Z0"+/v1p1beta1/{parent=projects/*}/assets:group:\x01*\x12\xe2\x02\n\rGroupFindings\x12;.google.cloud.securitycenter.v1p1beta1.GroupFindingsRequest\x1a<.google.cloud.securitycenter.v1p1beta1.GroupFindingsResponse"\xd5\x01\xdaA\x0fparent,group_by\x82\xd3\xe4\x93\x02\xbc\x01"</v1p1beta1/{parent=organizations/*/sources/*}/findings:group:\x01*Z;"6/v1p1beta1/{parent=folders/*/sources/*}/findings:group:\x01*Z<"7/v1p1beta1/{parent=projects/*/sources/*}/findings:group:\x01*\x12\x90\x02\n\nListAssets\x128.google.cloud.securitycenter.v1p1beta1.ListAssetsRequest\x1a9.google.cloud.securitycenter.v1p1beta1.ListAssetsResponse"\x8c\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02}\x12*/v1p1beta1/{parent=organizations/*}/assetsZ&\x12$/v1p1beta1/{parent=folders/*}/assetsZ\'\x12%/v1p1beta1/{parent=projects/*}/assets\x12\xbb\x02\n\x0cListFindings\x12:.google.cloud.securitycenter.v1p1beta1.ListFindingsRequest\x1a;.google.cloud.securitycenter.v1p1beta1.ListFindingsResponse"\xb1\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa1\x01\x126/v1p1beta1/{parent=organizations/*/sources/*}/findingsZ2\x120/v1p1beta1/{parent=folders/*/sources/*}/findingsZ3\x121/v1p1beta1/{parent=projects/*/sources/*}/findings\x12\xf2\x01\n\x17ListNotificationConfigs\x12E.google.cloud.securitycenter.v1p1beta1.ListNotificationConfigsRequest\x1aF.google.cloud.securitycenter.v1p1beta1.ListNotificationConfigsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1p1beta1/{parent=organizations/*}/notificationConfigs\x12\x97\x02\n\x0bListSources\x129.google.cloud.securitycenter.v1p1beta1.ListSourcesRequest\x1a:.google.cloud.securitycenter.v1p1beta1.ListSourcesResponse"\x90\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x80\x01\x12+/v1p1beta1/{parent=organizations/*}/sourcesZ\'\x12%/v1p1beta1/{parent=folders/*}/sourcesZ(\x12&/v1p1beta1/{parent=projects/*}/sources\x12\x9c\x02\n\x11RunAssetDiscovery\x12?.google.cloud.securitycenter.v1p1beta1.RunAssetDiscoveryRequest\x1a\x1d.google.longrunning.Operation"\xa6\x01\xcaAX\n?google.cloud.securitycenter.v1p1beta1.RunAssetDiscoveryResponse\x12\x15google.protobuf.Empty\xdaA\x06parent\x82\xd3\xe4\x93\x02<"7/v1p1beta1/{parent=organizations/*}/assets:runDiscovery:\x01*\x12\xe7\x02\n\x0fSetFindingState\x12=.google.cloud.securitycenter.v1p1beta1.SetFindingStateRequest\x1a..google.cloud.securitycenter.v1p1beta1.Finding"\xe4\x01\xdaA\x15name,state,start_time\x82\xd3\xe4\x93\x02\xc5\x01"?/v1p1beta1/{name=organizations/*/sources/*/findings/*}:setState:\x01*Z>"9/v1p1beta1/{name=folders/*/sources/*/findings/*}:setState:\x01*Z?":/v1p1beta1/{name=projects/*/sources/*/findings/*}:setState:\x01*\x12\xa4\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Y\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02A"</v1p1beta1/{resource=organizations/*/sources/*}:setIamPolicy:\x01*\x12\xcf\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"d\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02G"B/v1p1beta1/{resource=organizations/*/sources/*}:testIamPermissions:\x01*\x12\xfa\x02\n\rUpdateFinding\x12;.google.cloud.securitycenter.v1p1beta1.UpdateFindingRequest\x1a..google.cloud.securitycenter.v1p1beta1.Finding"\xfb\x01\xdaA\x07finding\xdaA\x13finding,update_mask\x82\xd3\xe4\x93\x02\xd4\x012>/v1p1beta1/{finding.name=organizations/*/sources/*/findings/*}:\x07findingZC28/v1p1beta1/{finding.name=folders/*/sources/*/findings/*}:\x07findingZD29/v1p1beta1/{finding.name=projects/*/sources/*/findings/*}:\x07finding\x12\xc0\x02\n\x18UpdateNotificationConfig\x12F.google.cloud.securitycenter.v1p1beta1.UpdateNotificationConfigRequest\x1a9.google.cloud.securitycenter.v1p1beta1.NotificationConfig"\xa0\x01\xdaA\x13notification_config\xdaA\x1fnotification_config,update_mask\x82\xd3\xe4\x93\x02b2K/v1p1beta1/{notification_config.name=organizations/*/notificationConfigs/*}:\x13notification_config\x12\xa9\x02\n\x1aUpdateOrganizationSettings\x12H.google.cloud.securitycenter.v1p1beta1.UpdateOrganizationSettingsRequest\x1a;.google.cloud.securitycenter.v1p1beta1.OrganizationSettings"\x83\x01\xdaA\x15organization_settings\x82\xd3\xe4\x93\x02e2L/v1p1beta1/{organization_settings.name=organizations/*/organizationSettings}:\x15organization_settings\x12\xdb\x01\n\x0cUpdateSource\x12:.google.cloud.securitycenter.v1p1beta1.UpdateSourceRequest\x1a-.google.cloud.securitycenter.v1p1beta1.Source"`\xdaA\x06source\xdaA\x12source,update_mask\x82\xd3\xe4\x93\x02<22/v1p1beta1/{source.name=organizations/*/sources/*}:\x06source\x12\xf4\x05\n\x13UpdateSecurityMarks\x12A.google.cloud.securitycenter.v1p1beta1.UpdateSecurityMarksRequest\x1a4.google.cloud.securitycenter.v1p1beta1.SecurityMarks"\xe3\x04\xdaA\x0esecurity_marks\xdaA\x1asecurity_marks,update_mask\x82\xd3\xe4\x93\x02\xae\x042G/v1p1beta1/{security_marks.name=organizations/*/assets/*/securityMarks}:\x0esecurity_marksZS2A/v1p1beta1/{security_marks.name=folders/*/assets/*/securityMarks}:\x0esecurity_marksZT2B/v1p1beta1/{security_marks.name=projects/*/assets/*/securityMarks}:\x0esecurity_marksZe2S/v1p1beta1/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}:\x0esecurity_marksZ_2M/v1p1beta1/{security_marks.name=folders/*/sources/*/findings/*/securityMarks}:\x0esecurity_marksZ`2N/v1p1beta1/{security_marks.name=projects/*/sources/*/findings/*/securityMarks}:\x0esecurity_marks\x1aQ\xcaA\x1dsecuritycenter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfb\x01\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1P\x00P\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1p1beta1.securitycenter_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1'
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding_id']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['config_id']._loaded_options = None
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['notification_config']._loaded_options = None
    _globals['_CREATENOTIFICATIONCONFIGREQUEST'].fields_by_name['notification_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESOURCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESOURCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_CREATESOURCEREQUEST'].fields_by_name['source']._loaded_options = None
    _globals['_CREATESOURCEREQUEST'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENOTIFICATIONCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENOTIFICATIONCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0securitycenter.googleapis.com/NotificationConfig'
    _globals['_GETNOTIFICATIONCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0securitycenter.googleapis.com/NotificationConfig'
    _globals['_GETORGANIZATIONSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORGANIZATIONSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2securitycenter.googleapis.com/OrganizationSettings'
    _globals['_GETSOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_GROUPASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GROUPASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#securitycenter.googleapis.com/Asset'
    _globals['_GROUPASSETSREQUEST'].fields_by_name['group_by']._loaded_options = None
    _globals['_GROUPASSETSREQUEST'].fields_by_name['group_by']._serialized_options = b'\xe0A\x02'
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['group_by']._loaded_options = None
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['group_by']._serialized_options = b'\xe0A\x02'
    _globals['_GROUPRESULT_PROPERTIESENTRY']._loaded_options = None
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_LISTNOTIFICATIONCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNOTIFICATIONCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_LISTSOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$securitycenter.googleapis.com/Source'
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#securitycenter.googleapis.com/Asset'
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT'].fields_by_name['resource']._loaded_options = None
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT'].fields_by_name['resource']._serialized_options = b'\xe0A\x03'
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%securitycenter.googleapis.com/Finding"
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['state']._loaded_options = None
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['start_time']._loaded_options = None
    _globals['_SETFINDINGSTATEREQUEST'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_RUNASSETDISCOVERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RUNASSETDISCOVERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_UPDATEFINDINGREQUEST'].fields_by_name['finding']._loaded_options = None
    _globals['_UPDATEFINDINGREQUEST'].fields_by_name['finding']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATENOTIFICATIONCONFIGREQUEST'].fields_by_name['notification_config']._loaded_options = None
    _globals['_UPDATENOTIFICATIONCONFIGREQUEST'].fields_by_name['notification_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST'].fields_by_name['organization_settings']._loaded_options = None
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST'].fields_by_name['organization_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESOURCEREQUEST'].fields_by_name['source']._loaded_options = None
    _globals['_UPDATESOURCEREQUEST'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESECURITYMARKSREQUEST'].fields_by_name['security_marks']._loaded_options = None
    _globals['_UPDATESECURITYMARKSREQUEST'].fields_by_name['security_marks']._serialized_options = b'\xe0A\x02'
    _globals['_SECURITYCENTER']._loaded_options = None
    _globals['_SECURITYCENTER']._serialized_options = b'\xcaA\x1dsecuritycenter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SECURITYCENTER'].methods_by_name['CreateSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['CreateSource']._serialized_options = b'\xdaA\rparent,source\x82\xd3\xe4\x93\x025"+/v1p1beta1/{parent=organizations/*}/sources:\x06source'
    _globals['_SECURITYCENTER'].methods_by_name['CreateFinding']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['CreateFinding']._serialized_options = b'\xdaA\x19parent,finding_id,finding\xdaA\x19parent,finding,finding_id\x82\xd3\xe4\x93\x02A"6/v1p1beta1/{parent=organizations/*/sources/*}/findings:\x07finding'
    _globals['_SECURITYCENTER'].methods_by_name['CreateNotificationConfig']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['CreateNotificationConfig']._serialized_options = b'\xdaA$parent,config_id,notification_config\xdaA\x1aparent,notification_config\x82\xd3\xe4\x93\x02N"7/v1p1beta1/{parent=organizations/*}/notificationConfigs:\x13notification_config'
    _globals['_SECURITYCENTER'].methods_by_name['DeleteNotificationConfig']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['DeleteNotificationConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1p1beta1/{name=organizations/*/notificationConfigs/*}'
    _globals['_SECURITYCENTER'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02A"</v1p1beta1/{resource=organizations/*/sources/*}:getIamPolicy:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['GetNotificationConfig']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetNotificationConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1p1beta1/{name=organizations/*/notificationConfigs/*}'
    _globals['_SECURITYCENTER'].methods_by_name['GetOrganizationSettings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetOrganizationSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1p1beta1/{name=organizations/*/organizationSettings}'
    _globals['_SECURITYCENTER'].methods_by_name['GetSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1p1beta1/{name=organizations/*/sources/*}'
    _globals['_SECURITYCENTER'].methods_by_name['GroupAssets']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GroupAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x98\x01"0/v1p1beta1/{parent=organizations/*}/assets:group:\x01*Z/"*/v1p1beta1/{parent=folders/*}/assets:group:\x01*Z0"+/v1p1beta1/{parent=projects/*}/assets:group:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['GroupFindings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GroupFindings']._serialized_options = b'\xdaA\x0fparent,group_by\x82\xd3\xe4\x93\x02\xbc\x01"</v1p1beta1/{parent=organizations/*/sources/*}/findings:group:\x01*Z;"6/v1p1beta1/{parent=folders/*/sources/*}/findings:group:\x01*Z<"7/v1p1beta1/{parent=projects/*/sources/*}/findings:group:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['ListAssets']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListAssets']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02}\x12*/v1p1beta1/{parent=organizations/*}/assetsZ&\x12$/v1p1beta1/{parent=folders/*}/assetsZ'\x12%/v1p1beta1/{parent=projects/*}/assets"
    _globals['_SECURITYCENTER'].methods_by_name['ListFindings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListFindings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa1\x01\x126/v1p1beta1/{parent=organizations/*/sources/*}/findingsZ2\x120/v1p1beta1/{parent=folders/*/sources/*}/findingsZ3\x121/v1p1beta1/{parent=projects/*/sources/*}/findings'
    _globals['_SECURITYCENTER'].methods_by_name['ListNotificationConfigs']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListNotificationConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1p1beta1/{parent=organizations/*}/notificationConfigs'
    _globals['_SECURITYCENTER'].methods_by_name['ListSources']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListSources']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02\x80\x01\x12+/v1p1beta1/{parent=organizations/*}/sourcesZ'\x12%/v1p1beta1/{parent=folders/*}/sourcesZ(\x12&/v1p1beta1/{parent=projects/*}/sources"
    _globals['_SECURITYCENTER'].methods_by_name['RunAssetDiscovery']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['RunAssetDiscovery']._serialized_options = b'\xcaAX\n?google.cloud.securitycenter.v1p1beta1.RunAssetDiscoveryResponse\x12\x15google.protobuf.Empty\xdaA\x06parent\x82\xd3\xe4\x93\x02<"7/v1p1beta1/{parent=organizations/*}/assets:runDiscovery:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['SetFindingState']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['SetFindingState']._serialized_options = b'\xdaA\x15name,state,start_time\x82\xd3\xe4\x93\x02\xc5\x01"?/v1p1beta1/{name=organizations/*/sources/*/findings/*}:setState:\x01*Z>"9/v1p1beta1/{name=folders/*/sources/*/findings/*}:setState:\x01*Z?":/v1p1beta1/{name=projects/*/sources/*/findings/*}:setState:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02A"</v1p1beta1/{resource=organizations/*/sources/*}:setIamPolicy:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02G"B/v1p1beta1/{resource=organizations/*/sources/*}:testIamPermissions:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateFinding']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateFinding']._serialized_options = b'\xdaA\x07finding\xdaA\x13finding,update_mask\x82\xd3\xe4\x93\x02\xd4\x012>/v1p1beta1/{finding.name=organizations/*/sources/*/findings/*}:\x07findingZC28/v1p1beta1/{finding.name=folders/*/sources/*/findings/*}:\x07findingZD29/v1p1beta1/{finding.name=projects/*/sources/*/findings/*}:\x07finding'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateNotificationConfig']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateNotificationConfig']._serialized_options = b'\xdaA\x13notification_config\xdaA\x1fnotification_config,update_mask\x82\xd3\xe4\x93\x02b2K/v1p1beta1/{notification_config.name=organizations/*/notificationConfigs/*}:\x13notification_config'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateOrganizationSettings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateOrganizationSettings']._serialized_options = b'\xdaA\x15organization_settings\x82\xd3\xe4\x93\x02e2L/v1p1beta1/{organization_settings.name=organizations/*/organizationSettings}:\x15organization_settings'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSource']._serialized_options = b'\xdaA\x06source\xdaA\x12source,update_mask\x82\xd3\xe4\x93\x02<22/v1p1beta1/{source.name=organizations/*/sources/*}:\x06source'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSecurityMarks']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSecurityMarks']._serialized_options = b'\xdaA\x0esecurity_marks\xdaA\x1asecurity_marks,update_mask\x82\xd3\xe4\x93\x02\xae\x042G/v1p1beta1/{security_marks.name=organizations/*/assets/*/securityMarks}:\x0esecurity_marksZS2A/v1p1beta1/{security_marks.name=folders/*/assets/*/securityMarks}:\x0esecurity_marksZT2B/v1p1beta1/{security_marks.name=projects/*/assets/*/securityMarks}:\x0esecurity_marksZe2S/v1p1beta1/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}:\x0esecurity_marksZ_2M/v1p1beta1/{security_marks.name=folders/*/sources/*/findings/*/securityMarks}:\x0esecurity_marksZ`2N/v1p1beta1/{security_marks.name=projects/*/sources/*/findings/*/securityMarks}:\x0esecurity_marks'
    _globals['_CREATEFINDINGREQUEST']._serialized_start = 1020
    _globals['_CREATEFINDINGREQUEST']._serialized_end = 1199
    _globals['_CREATENOTIFICATIONCONFIGREQUEST']._serialized_start = 1202
    _globals['_CREATENOTIFICATIONCONFIGREQUEST']._serialized_end = 1426
    _globals['_CREATESOURCEREQUEST']._serialized_start = 1429
    _globals['_CREATESOURCEREQUEST']._serialized_end = 1592
    _globals['_DELETENOTIFICATIONCONFIGREQUEST']._serialized_start = 1594
    _globals['_DELETENOTIFICATIONCONFIGREQUEST']._serialized_end = 1699
    _globals['_GETNOTIFICATIONCONFIGREQUEST']._serialized_start = 1701
    _globals['_GETNOTIFICATIONCONFIGREQUEST']._serialized_end = 1803
    _globals['_GETORGANIZATIONSETTINGSREQUEST']._serialized_start = 1805
    _globals['_GETORGANIZATIONSETTINGSREQUEST']._serialized_end = 1911
    _globals['_GETSOURCEREQUEST']._serialized_start = 1913
    _globals['_GETSOURCEREQUEST']._serialized_end = 1991
    _globals['_GROUPASSETSREQUEST']._serialized_start = 1994
    _globals['_GROUPASSETSREQUEST']._serialized_end = 2253
    _globals['_GROUPASSETSRESPONSE']._serialized_start = 2256
    _globals['_GROUPASSETSRESPONSE']._serialized_end = 2447
    _globals['_GROUPFINDINGSREQUEST']._serialized_start = 2450
    _globals['_GROUPFINDINGSREQUEST']._serialized_end = 2712
    _globals['_GROUPFINDINGSRESPONSE']._serialized_start = 2715
    _globals['_GROUPFINDINGSRESPONSE']._serialized_end = 2908
    _globals['_GROUPRESULT']._serialized_start = 2911
    _globals['_GROUPRESULT']._serialized_end = 3102
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_start = 3029
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_end = 3102
    _globals['_LISTNOTIFICATIONCONFIGSREQUEST']._serialized_start = 3105
    _globals['_LISTNOTIFICATIONCONFIGSREQUEST']._serialized_end = 3250
    _globals['_LISTNOTIFICATIONCONFIGSRESPONSE']._serialized_start = 3253
    _globals['_LISTNOTIFICATIONCONFIGSRESPONSE']._serialized_end = 3400
    _globals['_LISTSOURCESREQUEST']._serialized_start = 3402
    _globals['_LISTSOURCESREQUEST']._serialized_end = 3523
    _globals['_LISTSOURCESRESPONSE']._serialized_start = 3525
    _globals['_LISTSOURCESRESPONSE']._serialized_end = 3635
    _globals['_LISTASSETSREQUEST']._serialized_start = 3638
    _globals['_LISTASSETSREQUEST']._serialized_end = 3939
    _globals['_LISTASSETSRESPONSE']._serialized_start = 3942
    _globals['_LISTASSETSRESPONSE']._serialized_end = 4414
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT']._serialized_start = 4162
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT']._serialized_end = 4414
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT_STATECHANGE']._serialized_start = 4353
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT_STATECHANGE']._serialized_end = 4414
    _globals['_LISTFINDINGSREQUEST']._serialized_start = 4417
    _globals['_LISTFINDINGSREQUEST']._serialized_end = 4721
    _globals['_LISTFINDINGSRESPONSE']._serialized_start = 4724
    _globals['_LISTFINDINGSRESPONSE']._serialized_end = 5535
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT']._serialized_start = 4952
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT']._serialized_end = 5535
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT_RESOURCE']._serialized_start = 5266
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT_RESOURCE']._serialized_end = 5456
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT_STATECHANGE']._serialized_start = 5458
    _globals['_LISTFINDINGSRESPONSE_LISTFINDINGSRESULT_STATECHANGE']._serialized_end = 5535
    _globals['_SETFINDINGSTATEREQUEST']._serialized_start = 5538
    _globals['_SETFINDINGSTATEREQUEST']._serialized_end = 5750
    _globals['_RUNASSETDISCOVERYREQUEST']._serialized_start = 5752
    _globals['_RUNASSETDISCOVERYREQUEST']._serialized_end = 5852
    _globals['_UPDATEFINDINGREQUEST']._serialized_start = 5855
    _globals['_UPDATEFINDINGREQUEST']._serialized_end = 5996
    _globals['_UPDATENOTIFICATIONCONFIGREQUEST']._serialized_start = 5999
    _globals['_UPDATENOTIFICATIONCONFIGREQUEST']._serialized_end = 6174
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST']._serialized_start = 6177
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST']._serialized_end = 6358
    _globals['_UPDATESOURCEREQUEST']._serialized_start = 6361
    _globals['_UPDATESOURCEREQUEST']._serialized_end = 6499
    _globals['_UPDATESECURITYMARKSREQUEST']._serialized_start = 6502
    _globals['_UPDATESECURITYMARKSREQUEST']._serialized_end = 6710
    _globals['_SECURITYCENTER']._serialized_start = 6713
    _globals['_SECURITYCENTER']._serialized_end = 13361