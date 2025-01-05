"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1beta1/securitycenter_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1beta1 import asset_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_asset__pb2
from .....google.cloud.securitycenter.v1beta1 import finding_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_finding__pb2
from .....google.cloud.securitycenter.v1beta1 import organization_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_organization__settings__pb2
from .....google.cloud.securitycenter.v1beta1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_security__marks__pb2
from .....google.cloud.securitycenter.v1beta1 import source_pb2 as google_dot_cloud_dot_securitycenter_dot_v1beta1_dot_source__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/securitycenter/v1beta1/securitycenter_service.proto\x12#google.cloud.securitycenter.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/securitycenter/v1beta1/asset.proto\x1a1google/cloud/securitycenter/v1beta1/finding.proto\x1a?google/cloud/securitycenter/v1beta1/organization_settings.proto\x1a8google/cloud/securitycenter/v1beta1/security_marks.proto\x1a0google/cloud/securitycenter/v1beta1/source.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x01\n\x14CreateFindingRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x17\n\nfinding_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12B\n\x07finding\x18\x03 \x01(\x0b2,.google.cloud.securitycenter.v1beta1.FindingB\x03\xe0A\x02"\xa1\x01\n\x13CreateSourceRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12@\n\x06source\x18\x02 \x01(\x0b2+.google.cloud.securitycenter.v1beta1.SourceB\x03\xe0A\x02"j\n\x1eGetOrganizationSettingsRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2securitycenter.googleapis.com/OrganizationSettings"N\n\x10GetSourceRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source"\x90\x02\n\x12GroupAssetsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x15\n\x08group_by\x18\x03 \x01(\tB\x03\xe0A\x02\x123\n\x10compare_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12-\n\tread_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x11\n\tpage_size\x18\x08 \x01(\x05"\xa9\x01\n\x13GroupAssetsResponse\x12J\n\x10group_by_results\x18\x01 \x03(\x0b20.google.cloud.securitycenter.v1beta1.GroupResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\xd1\x01\n\x14GroupFindingsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x15\n\x08group_by\x18\x03 \x01(\tB\x03\xe0A\x02\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\npage_token\x18\x05 \x01(\t\x12\x11\n\tpage_size\x18\x06 \x01(\x05"\xab\x01\n\x15GroupFindingsResponse\x12J\n\x10group_by_results\x18\x01 \x03(\x0b20.google.cloud.securitycenter.v1beta1.GroupResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\xbd\x01\n\x0bGroupResult\x12T\n\nproperties\x18\x01 \x03(\x0b2@.google.cloud.securitycenter.v1beta1.GroupResult.PropertiesEntry\x12\r\n\x05count\x18\x02 \x01(\x03\x1aI\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01"\x85\x01\n\x12ListSourcesRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x07 \x01(\x05"l\n\x13ListSourcesResponse\x12<\n\x07sources\x18\x01 \x03(\x0b2+.google.cloud.securitycenter.v1beta1.Source\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xbf\x02\n\x11ListAssetsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x10compare_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x123\n\nfield_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x12\n\npage_token\x18\x08 \x01(\t\x12\x11\n\tpage_size\x18\t \x01(\x05"\xd6\x03\n\x12ListAssetsResponse\x12e\n\x13list_assets_results\x18\x01 \x03(\x0b2H.google.cloud.securitycenter.v1beta1.ListAssetsResponse.ListAssetsResult\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05\x1a\xfc\x01\n\x10ListAssetsResult\x129\n\x05asset\x18\x01 \x01(\x0b2*.google.cloud.securitycenter.v1beta1.Asset\x12]\n\x05state\x18\x02 \x01(\x0e2N.google.cloud.securitycenter.v1beta1.ListAssetsResponse.ListAssetsResult.State"N\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06UNUSED\x10\x01\x12\t\n\x05ADDED\x10\x02\x12\x0b\n\x07REMOVED\x10\x03\x12\n\n\x06ACTIVE\x10\x04"\x80\x02\n\x13ListFindingsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\nfield_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x12\n\npage_token\x18\x06 \x01(\t\x12\x11\n\tpage_size\x18\x07 \x01(\x05"\xb2\x01\n\x14ListFindingsResponse\x12>\n\x08findings\x18\x01 \x03(\x0b2,.google.cloud.securitycenter.v1beta1.Finding\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05"\xd2\x01\n\x16SetFindingStateRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%securitycenter.googleapis.com/Finding\x12F\n\x05state\x18\x02 \x01(\x0e22.google.cloud.securitycenter.v1beta1.Finding.StateB\x03\xe0A\x02\x123\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"d\n\x18RunAssetDiscoveryRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization"\x8b\x01\n\x14UpdateFindingRequest\x12B\n\x07finding\x18\x01 \x01(\x0b2,.google.cloud.securitycenter.v1beta1.FindingB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb3\x01\n!UpdateOrganizationSettingsRequest\x12]\n\x15organization_settings\x18\x01 \x01(\x0b29.google.cloud.securitycenter.v1beta1.OrganizationSettingsB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x88\x01\n\x13UpdateSourceRequest\x12@\n\x06source\x18\x01 \x01(\x0b2+.google.cloud.securitycenter.v1beta1.SourceB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xce\x01\n\x1aUpdateSecurityMarksRequest\x12O\n\x0esecurity_marks\x18\x01 \x01(\x0b22.google.cloud.securitycenter.v1beta1.SecurityMarksB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xeb\x1e\n\x0eSecurityCenter\x12\xc0\x01\n\x0cCreateSource\x128.google.cloud.securitycenter.v1beta1.CreateSourceRequest\x1a+.google.cloud.securitycenter.v1beta1.Source"I\xdaA\rparent,source\x82\xd3\xe4\x93\x023")/v1beta1/{parent=organizations/*}/sources:\x06source\x12\xdb\x01\n\rCreateFinding\x129.google.cloud.securitycenter.v1beta1.CreateFindingRequest\x1a,.google.cloud.securitycenter.v1beta1.Finding"a\xdaA\x19parent,finding_id,finding\x82\xd3\xe4\x93\x02?"4/v1beta1/{parent=organizations/*/sources/*}/findings:\x07finding\x12\x9b\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"P\xdaA\x08resource\x82\xd3\xe4\x93\x02?":/v1beta1/{resource=organizations/*/sources/*}:getIamPolicy:\x01*\x12\xde\x01\n\x17GetOrganizationSettings\x12C.google.cloud.securitycenter.v1beta1.GetOrganizationSettingsRequest\x1a9.google.cloud.securitycenter.v1beta1.OrganizationSettings"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=organizations/*/organizationSettings}\x12\xa9\x01\n\tGetSource\x125.google.cloud.securitycenter.v1beta1.GetSourceRequest\x1a+.google.cloud.securitycenter.v1beta1.Source"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1beta1/{name=organizations/*/sources/*}\x12\xbb\x01\n\x0bGroupAssets\x127.google.cloud.securitycenter.v1beta1.GroupAssetsRequest\x1a8.google.cloud.securitycenter.v1beta1.GroupAssetsResponse"9\x82\xd3\xe4\x93\x023"./v1beta1/{parent=organizations/*}/assets:group:\x01*\x12\xdf\x01\n\rGroupFindings\x129.google.cloud.securitycenter.v1beta1.GroupFindingsRequest\x1a:.google.cloud.securitycenter.v1beta1.GroupFindingsResponse"W\xdaA\x0fparent,group_by\x82\xd3\xe4\x93\x02?":/v1beta1/{parent=organizations/*/sources/*}/findings:group:\x01*\x12\xaf\x01\n\nListAssets\x126.google.cloud.securitycenter.v1beta1.ListAssetsRequest\x1a7.google.cloud.securitycenter.v1beta1.ListAssetsResponse"0\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{parent=organizations/*}/assets\x12\xc1\x01\n\x0cListFindings\x128.google.cloud.securitycenter.v1beta1.ListFindingsRequest\x1a9.google.cloud.securitycenter.v1beta1.ListFindingsResponse"<\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=organizations/*/sources/*}/findings\x12\xbc\x01\n\x0bListSources\x127.google.cloud.securitycenter.v1beta1.ListSourcesRequest\x1a8.google.cloud.securitycenter.v1beta1.ListSourcesResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1beta1/{parent=organizations/*}/sources\x12\xed\x01\n\x11RunAssetDiscovery\x12=.google.cloud.securitycenter.v1beta1.RunAssetDiscoveryRequest\x1a\x1d.google.longrunning.Operation"z\xcaA.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\xdaA\x06parent\x82\xd3\xe4\x93\x02:"5/v1beta1/{parent=organizations/*}/assets:runDiscovery:\x01*\x12\xde\x01\n\x0fSetFindingState\x12;.google.cloud.securitycenter.v1beta1.SetFindingStateRequest\x1a,.google.cloud.securitycenter.v1beta1.Finding"`\xdaA\x15name,state,start_time\x82\xd3\xe4\x93\x02B"=/v1beta1/{name=organizations/*/sources/*/findings/*}:setState:\x01*\x12\xa2\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"W\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02?":/v1beta1/{resource=organizations/*/sources/*}:setIamPolicy:\x01*\x12\xcd\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"b\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02E"@/v1beta1/{resource=organizations/*/sources/*}:testIamPermissions:\x01*\x12\xd1\x01\n\rUpdateFinding\x129.google.cloud.securitycenter.v1beta1.UpdateFindingRequest\x1a,.google.cloud.securitycenter.v1beta1.Finding"W\xdaA\x07finding\x82\xd3\xe4\x93\x02G2</v1beta1/{finding.name=organizations/*/sources/*/findings/*}:\x07finding\x12\xa3\x02\n\x1aUpdateOrganizationSettings\x12F.google.cloud.securitycenter.v1beta1.UpdateOrganizationSettingsRequest\x1a9.google.cloud.securitycenter.v1beta1.OrganizationSettings"\x81\x01\xdaA\x15organization_settings\x82\xd3\xe4\x93\x02c2J/v1beta1/{organization_settings.name=organizations/*/organizationSettings}:\x15organization_settings\x12\xc0\x01\n\x0cUpdateSource\x128.google.cloud.securitycenter.v1beta1.UpdateSourceRequest\x1a+.google.cloud.securitycenter.v1beta1.Source"I\xdaA\x06source\x82\xd3\xe4\x93\x02:20/v1beta1/{source.name=organizations/*/sources/*}:\x06source\x12\xe1\x02\n\x13UpdateSecurityMarks\x12?.google.cloud.securitycenter.v1beta1.UpdateSecurityMarksRequest\x1a2.google.cloud.securitycenter.v1beta1.SecurityMarks"\xd4\x01\xdaA\x0esecurity_marks\x82\xd3\xe4\x93\x02\xbc\x012E/v1beta1/{security_marks.name=organizations/*/assets/*/securityMarks}:\x0esecurity_marksZc2Q/v1beta1/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}:\x0esecurity_marks\x1aQ\xcaA\x1dsecuritycenter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB|\n\'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1beta1.securitycenter_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpb"
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding_id']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding']._loaded_options = None
    _globals['_CREATEFINDINGREQUEST'].fields_by_name['finding']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESOURCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESOURCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_CREATESOURCEREQUEST'].fields_by_name['source']._loaded_options = None
    _globals['_CREATESOURCEREQUEST'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_GETORGANIZATIONSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORGANIZATIONSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2securitycenter.googleapis.com/OrganizationSettings'
    _globals['_GETSOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_GROUPASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GROUPASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_GROUPASSETSREQUEST'].fields_by_name['group_by']._loaded_options = None
    _globals['_GROUPASSETSREQUEST'].fields_by_name['group_by']._serialized_options = b'\xe0A\x02'
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['group_by']._loaded_options = None
    _globals['_GROUPFINDINGSREQUEST'].fields_by_name['group_by']._serialized_options = b'\xe0A\x02'
    _globals['_GROUPRESULT_PROPERTIESENTRY']._loaded_options = None
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_LISTSOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTASSETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_LISTASSETSREQUEST'].fields_by_name['field_mask']._loaded_options = None
    _globals['_LISTASSETSREQUEST'].fields_by_name['field_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$securitycenter.googleapis.com/Source'
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['field_mask']._loaded_options = None
    _globals['_LISTFINDINGSREQUEST'].fields_by_name['field_mask']._serialized_options = b'\xe0A\x01'
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
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST'].fields_by_name['organization_settings']._loaded_options = None
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST'].fields_by_name['organization_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESOURCEREQUEST'].fields_by_name['source']._loaded_options = None
    _globals['_UPDATESOURCEREQUEST'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESECURITYMARKSREQUEST'].fields_by_name['security_marks']._loaded_options = None
    _globals['_UPDATESECURITYMARKSREQUEST'].fields_by_name['security_marks']._serialized_options = b'\xe0A\x02'
    _globals['_SECURITYCENTER']._loaded_options = None
    _globals['_SECURITYCENTER']._serialized_options = b'\xcaA\x1dsecuritycenter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SECURITYCENTER'].methods_by_name['CreateSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['CreateSource']._serialized_options = b'\xdaA\rparent,source\x82\xd3\xe4\x93\x023")/v1beta1/{parent=organizations/*}/sources:\x06source'
    _globals['_SECURITYCENTER'].methods_by_name['CreateFinding']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['CreateFinding']._serialized_options = b'\xdaA\x19parent,finding_id,finding\x82\xd3\xe4\x93\x02?"4/v1beta1/{parent=organizations/*/sources/*}/findings:\x07finding'
    _globals['_SECURITYCENTER'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02?":/v1beta1/{resource=organizations/*/sources/*}:getIamPolicy:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['GetOrganizationSettings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetOrganizationSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1beta1/{name=organizations/*/organizationSettings}'
    _globals['_SECURITYCENTER'].methods_by_name['GetSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GetSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1beta1/{name=organizations/*/sources/*}'
    _globals['_SECURITYCENTER'].methods_by_name['GroupAssets']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GroupAssets']._serialized_options = b'\x82\xd3\xe4\x93\x023"./v1beta1/{parent=organizations/*}/assets:group:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['GroupFindings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['GroupFindings']._serialized_options = b'\xdaA\x0fparent,group_by\x82\xd3\xe4\x93\x02?":/v1beta1/{parent=organizations/*/sources/*}/findings:group:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['ListAssets']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{parent=organizations/*}/assets'
    _globals['_SECURITYCENTER'].methods_by_name['ListFindings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListFindings']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/v1beta1/{parent=organizations/*/sources/*}/findings'
    _globals['_SECURITYCENTER'].methods_by_name['ListSources']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['ListSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1beta1/{parent=organizations/*}/sources'
    _globals['_SECURITYCENTER'].methods_by_name['RunAssetDiscovery']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['RunAssetDiscovery']._serialized_options = b'\xcaA.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\xdaA\x06parent\x82\xd3\xe4\x93\x02:"5/v1beta1/{parent=organizations/*}/assets:runDiscovery:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['SetFindingState']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['SetFindingState']._serialized_options = b'\xdaA\x15name,state,start_time\x82\xd3\xe4\x93\x02B"=/v1beta1/{name=organizations/*/sources/*/findings/*}:setState:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02?":/v1beta1/{resource=organizations/*/sources/*}:setIamPolicy:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02E"@/v1beta1/{resource=organizations/*/sources/*}:testIamPermissions:\x01*'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateFinding']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateFinding']._serialized_options = b'\xdaA\x07finding\x82\xd3\xe4\x93\x02G2</v1beta1/{finding.name=organizations/*/sources/*/findings/*}:\x07finding'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateOrganizationSettings']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateOrganizationSettings']._serialized_options = b'\xdaA\x15organization_settings\x82\xd3\xe4\x93\x02c2J/v1beta1/{organization_settings.name=organizations/*/organizationSettings}:\x15organization_settings'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSource']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSource']._serialized_options = b'\xdaA\x06source\x82\xd3\xe4\x93\x02:20/v1beta1/{source.name=organizations/*/sources/*}:\x06source'
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSecurityMarks']._loaded_options = None
    _globals['_SECURITYCENTER'].methods_by_name['UpdateSecurityMarks']._serialized_options = b'\xdaA\x0esecurity_marks\x82\xd3\xe4\x93\x02\xbc\x012E/v1beta1/{security_marks.name=organizations/*/assets/*/securityMarks}:\x0esecurity_marksZc2Q/v1beta1/{security_marks.name=organizations/*/sources/*/findings/*/securityMarks}:\x0esecurity_marks'
    _globals['_CREATEFINDINGREQUEST']._serialized_start = 720
    _globals['_CREATEFINDINGREQUEST']._serialized_end = 897
    _globals['_CREATESOURCEREQUEST']._serialized_start = 900
    _globals['_CREATESOURCEREQUEST']._serialized_end = 1061
    _globals['_GETORGANIZATIONSETTINGSREQUEST']._serialized_start = 1063
    _globals['_GETORGANIZATIONSETTINGSREQUEST']._serialized_end = 1169
    _globals['_GETSOURCEREQUEST']._serialized_start = 1171
    _globals['_GETSOURCEREQUEST']._serialized_end = 1249
    _globals['_GROUPASSETSREQUEST']._serialized_start = 1252
    _globals['_GROUPASSETSREQUEST']._serialized_end = 1524
    _globals['_GROUPASSETSRESPONSE']._serialized_start = 1527
    _globals['_GROUPASSETSRESPONSE']._serialized_end = 1696
    _globals['_GROUPFINDINGSREQUEST']._serialized_start = 1699
    _globals['_GROUPFINDINGSREQUEST']._serialized_end = 1908
    _globals['_GROUPFINDINGSRESPONSE']._serialized_start = 1911
    _globals['_GROUPFINDINGSRESPONSE']._serialized_end = 2082
    _globals['_GROUPRESULT']._serialized_start = 2085
    _globals['_GROUPRESULT']._serialized_end = 2274
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_start = 2201
    _globals['_GROUPRESULT_PROPERTIESENTRY']._serialized_end = 2274
    _globals['_LISTSOURCESREQUEST']._serialized_start = 2277
    _globals['_LISTSOURCESREQUEST']._serialized_end = 2410
    _globals['_LISTSOURCESRESPONSE']._serialized_start = 2412
    _globals['_LISTSOURCESRESPONSE']._serialized_end = 2520
    _globals['_LISTASSETSREQUEST']._serialized_start = 2523
    _globals['_LISTASSETSREQUEST']._serialized_end = 2842
    _globals['_LISTASSETSRESPONSE']._serialized_start = 2845
    _globals['_LISTASSETSRESPONSE']._serialized_end = 3315
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT']._serialized_start = 3063
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT']._serialized_end = 3315
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT_STATE']._serialized_start = 3237
    _globals['_LISTASSETSRESPONSE_LISTASSETSRESULT_STATE']._serialized_end = 3315
    _globals['_LISTFINDINGSREQUEST']._serialized_start = 3318
    _globals['_LISTFINDINGSREQUEST']._serialized_end = 3574
    _globals['_LISTFINDINGSRESPONSE']._serialized_start = 3577
    _globals['_LISTFINDINGSRESPONSE']._serialized_end = 3755
    _globals['_SETFINDINGSTATEREQUEST']._serialized_start = 3758
    _globals['_SETFINDINGSTATEREQUEST']._serialized_end = 3968
    _globals['_RUNASSETDISCOVERYREQUEST']._serialized_start = 3970
    _globals['_RUNASSETDISCOVERYREQUEST']._serialized_end = 4070
    _globals['_UPDATEFINDINGREQUEST']._serialized_start = 4073
    _globals['_UPDATEFINDINGREQUEST']._serialized_end = 4212
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST']._serialized_start = 4215
    _globals['_UPDATEORGANIZATIONSETTINGSREQUEST']._serialized_end = 4394
    _globals['_UPDATESOURCEREQUEST']._serialized_start = 4397
    _globals['_UPDATESOURCEREQUEST']._serialized_end = 4533
    _globals['_UPDATESECURITYMARKSREQUEST']._serialized_start = 4536
    _globals['_UPDATESECURITYMARKSREQUEST']._serialized_end = 4742
    _globals['_SECURITYCENTER']._serialized_start = 4745
    _globals['_SECURITYCENTER']._serialized_end = 8692