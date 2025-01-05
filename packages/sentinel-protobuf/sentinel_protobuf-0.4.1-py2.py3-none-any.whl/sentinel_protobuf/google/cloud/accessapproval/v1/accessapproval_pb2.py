"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/accessapproval/v1/accessapproval.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/accessapproval/v1/accessapproval.proto\x12\x1egoogle.cloud.accessapproval.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"`\n\x0fAccessLocations\x12 \n\x18principal_office_country\x18\x01 \x01(\t\x12+\n#principal_physical_location_country\x18\x02 \x01(\t"\xa0\x02\n\x0cAccessReason\x12?\n\x04type\x18\x01 \x01(\x0e21.google.cloud.accessapproval.v1.AccessReason.Type\x12\x0e\n\x06detail\x18\x02 \x01(\t"\xbe\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aCUSTOMER_INITIATED_SUPPORT\x10\x01\x12\x1c\n\x18GOOGLE_INITIATED_SERVICE\x10\x02\x12\x1b\n\x17GOOGLE_INITIATED_REVIEW\x10\x03\x12\x1c\n\x18THIRD_PARTY_DATA_REQUEST\x10\x04\x12\'\n#GOOGLE_RESPONSE_TO_PRODUCTION_ALERT\x10\x05"|\n\rSignatureInfo\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x1f\n\x15google_public_key_pem\x18\x02 \x01(\tH\x00\x12"\n\x18customer_kms_key_version\x18\x03 \x01(\tH\x00B\x13\n\x11verification_info"\x87\x02\n\x0fApproveDecision\x120\n\x0capprove_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0finvalidate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\x0esignature_info\x18\x04 \x01(\x0b2-.google.cloud.accessapproval.v1.SignatureInfo\x12\x15\n\rauto_approved\x18\x05 \x01(\x08"U\n\x0fDismissDecision\x120\n\x0cdismiss_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08implicit\x18\x02 \x01(\x08"2\n\x12ResourceProperties\x12\x1c\n\x14excludes_descendants\x18\x01 \x01(\x08"\x97\x06\n\x0fApprovalRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x17requested_resource_name\x18\x02 \x01(\t\x12Y\n\x1drequested_resource_properties\x18\t \x01(\x0b22.google.cloud.accessapproval.v1.ResourceProperties\x12F\n\x10requested_reason\x18\x03 \x01(\x0b2,.google.cloud.accessapproval.v1.AccessReason\x12L\n\x13requested_locations\x18\x04 \x01(\x0b2/.google.cloud.accessapproval.v1.AccessLocations\x120\n\x0crequest_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x128\n\x14requested_expiration\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x07approve\x18\x07 \x01(\x0b2/.google.cloud.accessapproval.v1.ApproveDecisionH\x00\x12B\n\x07dismiss\x18\x08 \x01(\x0b2/.google.cloud.accessapproval.v1.DismissDecisionH\x00:\xe3\x01\xeaA\xdf\x01\n-accessapproval.googleapis.com/ApprovalRequest\x126projects/{project}/approvalRequests/{approval_request}\x124folders/{folder}/approvalRequests/{approval_request}\x12@organizations/{organization}/approvalRequests/{approval_request}B\n\n\x08decision"s\n\x0fEnrolledService\x12\x15\n\rcloud_product\x18\x01 \x01(\t\x12I\n\x10enrollment_level\x18\x02 \x01(\x0e2/.google.cloud.accessapproval.v1.EnrollmentLevel"\x9c\x04\n\x16AccessApprovalSettings\x12G\n\x04name\x18\x01 \x01(\tB9\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings\x12\x1b\n\x13notification_emails\x18\x02 \x03(\t\x12J\n\x11enrolled_services\x18\x03 \x03(\x0b2/.google.cloud.accessapproval.v1.EnrolledService\x12\x1e\n\x11enrolled_ancestor\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\x12active_key_version\x18\x06 \x01(\t\x12,\n\x1fancestor_has_active_key_version\x18\x07 \x01(\x08B\x03\xe0A\x03\x12 \n\x13invalid_key_version\x18\x08 \x01(\x08B\x03\xe0A\x03:\xc3\x01\xeaA\xbf\x01\n4accessapproval.googleapis.com/AccessApprovalSettings\x12)projects/{project}/accessApprovalSettings\x12\'folders/{folder}/accessApprovalSettings\x123organizations/{organization}/accessApprovalSettings"\xb8\x02\n\x1cAccessApprovalServiceAccount\x12M\n\x04name\x18\x01 \x01(\tB?\xfaA<\n:accessapproval.googleapis.com/AccessApprovalServiceAccount\x12\x15\n\raccount_email\x18\x02 \x01(\t:\xb1\x01\xeaA\xad\x01\n:accessapproval.googleapis.com/AccessApprovalServiceAccount\x12!projects/{project}/serviceAccount\x12\x1ffolders/{folder}/serviceAccount\x12+organizations/{organization}/serviceAccount"\x98\x01\n\x1bListApprovalRequestsMessage\x12B\n\x06parent\x18\x01 \x01(\tB2\xfaA/\x12-accessapproval.googleapis.com/ApprovalRequest\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\x83\x01\n\x1cListApprovalRequestsResponse\x12J\n\x11approval_requests\x18\x01 \x03(\x0b2/.google.cloud.accessapproval.v1.ApprovalRequest\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x19GetApprovalRequestMessage\x12@\n\x04name\x18\x01 \x01(\tB2\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest"\x92\x01\n\x1dApproveApprovalRequestMessage\x12@\n\x04name\x18\x01 \x01(\tB2\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"a\n\x1dDismissApprovalRequestMessage\x12@\n\x04name\x18\x01 \x01(\tB2\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest"d\n InvalidateApprovalRequestMessage\x12@\n\x04name\x18\x01 \x01(\tB2\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest"k\n GetAccessApprovalSettingsMessage\x12G\n\x04name\x18\x01 \x01(\tB9\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings"\xa0\x01\n#UpdateAccessApprovalSettingsMessage\x12H\n\x08settings\x18\x01 \x01(\x0b26.google.cloud.accessapproval.v1.AccessApprovalSettings\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"n\n#DeleteAccessApprovalSettingsMessage\x12G\n\x04name\x18\x01 \x01(\tB9\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings"6\n&GetAccessApprovalServiceAccountMessage\x12\x0c\n\x04name\x18\x01 \x01(\t*B\n\x0fEnrollmentLevel\x12 \n\x1cENROLLMENT_LEVEL_UNSPECIFIED\x10\x00\x12\r\n\tBLOCK_ALL\x10\x012\x87\x17\n\x0eAccessApproval\x12\xaa\x02\n\x14ListApprovalRequests\x12;.google.cloud.accessapproval.v1.ListApprovalRequestsMessage\x1a<.google.cloud.accessapproval.v1.ListApprovalRequestsResponse"\x96\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{parent=projects/*}/approvalRequestsZ)\x12\'/v1/{parent=folders/*}/approvalRequestsZ/\x12-/v1/{parent=organizations/*}/approvalRequests\x12\x97\x02\n\x12GetApprovalRequest\x129.google.cloud.accessapproval.v1.GetApprovalRequestMessage\x1a/.google.cloud.accessapproval.v1.ApprovalRequest"\x94\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{name=projects/*/approvalRequests/*}Z)\x12\'/v1/{name=folders/*/approvalRequests/*}Z/\x12-/v1/{name=organizations/*/approvalRequests/*}\x12\xb9\x02\n\x16ApproveApprovalRequest\x12=.google.cloud.accessapproval.v1.ApproveApprovalRequestMessage\x1a/.google.cloud.accessapproval.v1.ApprovalRequest"\xae\x01\x82\xd3\xe4\x93\x02\xa7\x01"0/v1/{name=projects/*/approvalRequests/*}:approve:\x01*Z4"//v1/{name=folders/*/approvalRequests/*}:approve:\x01*Z:"5/v1/{name=organizations/*/approvalRequests/*}:approve:\x01*\x12\xb9\x02\n\x16DismissApprovalRequest\x12=.google.cloud.accessapproval.v1.DismissApprovalRequestMessage\x1a/.google.cloud.accessapproval.v1.ApprovalRequest"\xae\x01\x82\xd3\xe4\x93\x02\xa7\x01"0/v1/{name=projects/*/approvalRequests/*}:dismiss:\x01*Z4"//v1/{name=folders/*/approvalRequests/*}:dismiss:\x01*Z:"5/v1/{name=organizations/*/approvalRequests/*}:dismiss:\x01*\x12\xc8\x02\n\x19InvalidateApprovalRequest\x12@.google.cloud.accessapproval.v1.InvalidateApprovalRequestMessage\x1a/.google.cloud.accessapproval.v1.ApprovalRequest"\xb7\x01\x82\xd3\xe4\x93\x02\xb0\x01"3/v1/{name=projects/*/approvalRequests/*}:invalidate:\x01*Z7"2/v1/{name=folders/*/approvalRequests/*}:invalidate:\x01*Z="8/v1/{name=organizations/*/approvalRequests/*}:invalidate:\x01*\x12\xb8\x02\n\x19GetAccessApprovalSettings\x12@.google.cloud.accessapproval.v1.GetAccessApprovalSettingsMessage\x1a6.google.cloud.accessapproval.v1.AccessApprovalSettings"\xa0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12,/v1/{name=projects/*/accessApprovalSettings}Z-\x12+/v1/{name=folders/*/accessApprovalSettings}Z3\x121/v1/{name=organizations/*/accessApprovalSettings}\x12\x87\x03\n\x1cUpdateAccessApprovalSettings\x12C.google.cloud.accessapproval.v1.UpdateAccessApprovalSettingsMessage\x1a6.google.cloud.accessapproval.v1.AccessApprovalSettings"\xe9\x01\xdaA\x14settings,update_mask\x82\xd3\xe4\x93\x02\xcb\x0125/v1/{settings.name=projects/*/accessApprovalSettings}:\x08settingsZ@24/v1/{settings.name=folders/*/accessApprovalSettings}:\x08settingsZF2:/v1/{settings.name=organizations/*/accessApprovalSettings}:\x08settings\x12\x9e\x02\n\x1cDeleteAccessApprovalSettings\x12C.google.cloud.accessapproval.v1.DeleteAccessApprovalSettingsMessage\x1a\x16.google.protobuf.Empty"\xa0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01*,/v1/{name=projects/*/accessApprovalSettings}Z-*+/v1/{name=folders/*/accessApprovalSettings}Z3*1/v1/{name=organizations/*/accessApprovalSettings}\x12\xb1\x02\n\x1fGetAccessApprovalServiceAccount\x12F.google.cloud.accessapproval.v1.GetAccessApprovalServiceAccountMessage\x1a<.google.cloud.accessapproval.v1.AccessApprovalServiceAccount"\x87\x01\xdaA\x04name\x82\xd3\xe4\x93\x02z\x12$/v1/{name=projects/*/serviceAccount}Z%\x12#/v1/{name=folders/*/serviceAccount}Z+\x12)/v1/{name=organizations/*/serviceAccount}\x1aQ\xcaA\x1daccessapproval.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n"com.google.cloud.accessapproval.v1B\x13AccessApprovalProtoP\x01ZJcloud.google.com/go/accessapproval/apiv1/accessapprovalpb;accessapprovalpb\xaa\x02\x1eGoogle.Cloud.AccessApproval.V1\xca\x02\x1eGoogle\\Cloud\\AccessApproval\\V1\xea\x02!Google::Cloud::AccessApproval::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.accessapproval.v1.accessapproval_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.accessapproval.v1B\x13AccessApprovalProtoP\x01ZJcloud.google.com/go/accessapproval/apiv1/accessapprovalpb;accessapprovalpb\xaa\x02\x1eGoogle.Cloud.AccessApproval.V1\xca\x02\x1eGoogle\\Cloud\\AccessApproval\\V1\xea\x02!Google::Cloud::AccessApproval::V1'
    _globals['_APPROVALREQUEST']._loaded_options = None
    _globals['_APPROVALREQUEST']._serialized_options = b'\xeaA\xdf\x01\n-accessapproval.googleapis.com/ApprovalRequest\x126projects/{project}/approvalRequests/{approval_request}\x124folders/{folder}/approvalRequests/{approval_request}\x12@organizations/{organization}/approvalRequests/{approval_request}'
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['name']._serialized_options = b'\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings'
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['enrolled_ancestor']._loaded_options = None
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['enrolled_ancestor']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['ancestor_has_active_key_version']._loaded_options = None
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['ancestor_has_active_key_version']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['invalid_key_version']._loaded_options = None
    _globals['_ACCESSAPPROVALSETTINGS'].fields_by_name['invalid_key_version']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSAPPROVALSETTINGS']._loaded_options = None
    _globals['_ACCESSAPPROVALSETTINGS']._serialized_options = b"\xeaA\xbf\x01\n4accessapproval.googleapis.com/AccessApprovalSettings\x12)projects/{project}/accessApprovalSettings\x12'folders/{folder}/accessApprovalSettings\x123organizations/{organization}/accessApprovalSettings"
    _globals['_ACCESSAPPROVALSERVICEACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSAPPROVALSERVICEACCOUNT'].fields_by_name['name']._serialized_options = b'\xfaA<\n:accessapproval.googleapis.com/AccessApprovalServiceAccount'
    _globals['_ACCESSAPPROVALSERVICEACCOUNT']._loaded_options = None
    _globals['_ACCESSAPPROVALSERVICEACCOUNT']._serialized_options = b'\xeaA\xad\x01\n:accessapproval.googleapis.com/AccessApprovalServiceAccount\x12!projects/{project}/serviceAccount\x12\x1ffolders/{folder}/serviceAccount\x12+organizations/{organization}/serviceAccount'
    _globals['_LISTAPPROVALREQUESTSMESSAGE'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAPPROVALREQUESTSMESSAGE'].fields_by_name['parent']._serialized_options = b'\xfaA/\x12-accessapproval.googleapis.com/ApprovalRequest'
    _globals['_GETAPPROVALREQUESTMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_GETAPPROVALREQUESTMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest'
    _globals['_APPROVEAPPROVALREQUESTMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_APPROVEAPPROVALREQUESTMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest'
    _globals['_DISMISSAPPROVALREQUESTMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_DISMISSAPPROVALREQUESTMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest'
    _globals['_INVALIDATEAPPROVALREQUESTMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_INVALIDATEAPPROVALREQUESTMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA/\n-accessapproval.googleapis.com/ApprovalRequest'
    _globals['_GETACCESSAPPROVALSETTINGSMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCESSAPPROVALSETTINGSMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings'
    _globals['_DELETEACCESSAPPROVALSETTINGSMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCESSAPPROVALSETTINGSMESSAGE'].fields_by_name['name']._serialized_options = b'\xfaA6\n4accessapproval.googleapis.com/AccessApprovalSettings'
    _globals['_ACCESSAPPROVAL']._loaded_options = None
    _globals['_ACCESSAPPROVAL']._serialized_options = b'\xcaA\x1daccessapproval.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACCESSAPPROVAL'].methods_by_name['ListApprovalRequests']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['ListApprovalRequests']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{parent=projects/*}/approvalRequestsZ)\x12'/v1/{parent=folders/*}/approvalRequestsZ/\x12-/v1/{parent=organizations/*}/approvalRequests"
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetApprovalRequest']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetApprovalRequest']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01\x12(/v1/{name=projects/*/approvalRequests/*}Z)\x12'/v1/{name=folders/*/approvalRequests/*}Z/\x12-/v1/{name=organizations/*/approvalRequests/*}"
    _globals['_ACCESSAPPROVAL'].methods_by_name['ApproveApprovalRequest']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['ApproveApprovalRequest']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa7\x01"0/v1/{name=projects/*/approvalRequests/*}:approve:\x01*Z4"//v1/{name=folders/*/approvalRequests/*}:approve:\x01*Z:"5/v1/{name=organizations/*/approvalRequests/*}:approve:\x01*'
    _globals['_ACCESSAPPROVAL'].methods_by_name['DismissApprovalRequest']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['DismissApprovalRequest']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa7\x01"0/v1/{name=projects/*/approvalRequests/*}:dismiss:\x01*Z4"//v1/{name=folders/*/approvalRequests/*}:dismiss:\x01*Z:"5/v1/{name=organizations/*/approvalRequests/*}:dismiss:\x01*'
    _globals['_ACCESSAPPROVAL'].methods_by_name['InvalidateApprovalRequest']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['InvalidateApprovalRequest']._serialized_options = b'\x82\xd3\xe4\x93\x02\xb0\x01"3/v1/{name=projects/*/approvalRequests/*}:invalidate:\x01*Z7"2/v1/{name=folders/*/approvalRequests/*}:invalidate:\x01*Z="8/v1/{name=organizations/*/approvalRequests/*}:invalidate:\x01*'
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetAccessApprovalSettings']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetAccessApprovalSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01\x12,/v1/{name=projects/*/accessApprovalSettings}Z-\x12+/v1/{name=folders/*/accessApprovalSettings}Z3\x121/v1/{name=organizations/*/accessApprovalSettings}'
    _globals['_ACCESSAPPROVAL'].methods_by_name['UpdateAccessApprovalSettings']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['UpdateAccessApprovalSettings']._serialized_options = b'\xdaA\x14settings,update_mask\x82\xd3\xe4\x93\x02\xcb\x0125/v1/{settings.name=projects/*/accessApprovalSettings}:\x08settingsZ@24/v1/{settings.name=folders/*/accessApprovalSettings}:\x08settingsZF2:/v1/{settings.name=organizations/*/accessApprovalSettings}:\x08settings'
    _globals['_ACCESSAPPROVAL'].methods_by_name['DeleteAccessApprovalSettings']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['DeleteAccessApprovalSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x92\x01*,/v1/{name=projects/*/accessApprovalSettings}Z-*+/v1/{name=folders/*/accessApprovalSettings}Z3*1/v1/{name=organizations/*/accessApprovalSettings}'
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetAccessApprovalServiceAccount']._loaded_options = None
    _globals['_ACCESSAPPROVAL'].methods_by_name['GetAccessApprovalServiceAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02z\x12$/v1/{name=projects/*/serviceAccount}Z%\x12#/v1/{name=folders/*/serviceAccount}Z+\x12)/v1/{name=organizations/*/serviceAccount}'
    _globals['_ENROLLMENTLEVEL']._serialized_start = 4161
    _globals['_ENROLLMENTLEVEL']._serialized_end = 4227
    _globals['_ACCESSLOCATIONS']._serialized_start = 298
    _globals['_ACCESSLOCATIONS']._serialized_end = 394
    _globals['_ACCESSREASON']._serialized_start = 397
    _globals['_ACCESSREASON']._serialized_end = 685
    _globals['_ACCESSREASON_TYPE']._serialized_start = 495
    _globals['_ACCESSREASON_TYPE']._serialized_end = 685
    _globals['_SIGNATUREINFO']._serialized_start = 687
    _globals['_SIGNATUREINFO']._serialized_end = 811
    _globals['_APPROVEDECISION']._serialized_start = 814
    _globals['_APPROVEDECISION']._serialized_end = 1077
    _globals['_DISMISSDECISION']._serialized_start = 1079
    _globals['_DISMISSDECISION']._serialized_end = 1164
    _globals['_RESOURCEPROPERTIES']._serialized_start = 1166
    _globals['_RESOURCEPROPERTIES']._serialized_end = 1216
    _globals['_APPROVALREQUEST']._serialized_start = 1219
    _globals['_APPROVALREQUEST']._serialized_end = 2010
    _globals['_ENROLLEDSERVICE']._serialized_start = 2012
    _globals['_ENROLLEDSERVICE']._serialized_end = 2127
    _globals['_ACCESSAPPROVALSETTINGS']._serialized_start = 2130
    _globals['_ACCESSAPPROVALSETTINGS']._serialized_end = 2670
    _globals['_ACCESSAPPROVALSERVICEACCOUNT']._serialized_start = 2673
    _globals['_ACCESSAPPROVALSERVICEACCOUNT']._serialized_end = 2985
    _globals['_LISTAPPROVALREQUESTSMESSAGE']._serialized_start = 2988
    _globals['_LISTAPPROVALREQUESTSMESSAGE']._serialized_end = 3140
    _globals['_LISTAPPROVALREQUESTSRESPONSE']._serialized_start = 3143
    _globals['_LISTAPPROVALREQUESTSRESPONSE']._serialized_end = 3274
    _globals['_GETAPPROVALREQUESTMESSAGE']._serialized_start = 3276
    _globals['_GETAPPROVALREQUESTMESSAGE']._serialized_end = 3369
    _globals['_APPROVEAPPROVALREQUESTMESSAGE']._serialized_start = 3372
    _globals['_APPROVEAPPROVALREQUESTMESSAGE']._serialized_end = 3518
    _globals['_DISMISSAPPROVALREQUESTMESSAGE']._serialized_start = 3520
    _globals['_DISMISSAPPROVALREQUESTMESSAGE']._serialized_end = 3617
    _globals['_INVALIDATEAPPROVALREQUESTMESSAGE']._serialized_start = 3619
    _globals['_INVALIDATEAPPROVALREQUESTMESSAGE']._serialized_end = 3719
    _globals['_GETACCESSAPPROVALSETTINGSMESSAGE']._serialized_start = 3721
    _globals['_GETACCESSAPPROVALSETTINGSMESSAGE']._serialized_end = 3828
    _globals['_UPDATEACCESSAPPROVALSETTINGSMESSAGE']._serialized_start = 3831
    _globals['_UPDATEACCESSAPPROVALSETTINGSMESSAGE']._serialized_end = 3991
    _globals['_DELETEACCESSAPPROVALSETTINGSMESSAGE']._serialized_start = 3993
    _globals['_DELETEACCESSAPPROVALSETTINGSMESSAGE']._serialized_end = 4103
    _globals['_GETACCESSAPPROVALSERVICEACCOUNTMESSAGE']._serialized_start = 4105
    _globals['_GETACCESSAPPROVALSERVICEACCOUNTMESSAGE']._serialized_end = 4159
    _globals['_ACCESSAPPROVAL']._serialized_start = 4230
    _globals['_ACCESSAPPROVAL']._serialized_end = 7181