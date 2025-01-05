"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/billing/v1/cloud_billing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/billing/v1/cloud_billing.proto\x12\x17google.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a google/protobuf/field_mask.proto"\x83\x03\n\x0eBillingAccount\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x03\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12\x11\n\x04open\x18\x02 \x01(\x08B\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x1e\n\x16master_billing_account\x18\x04 \x01(\t\x12\x13\n\x06parent\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcurrency_code\x18\x07 \x01(\tB\x03\xe0A\x01:\xb4\x01\xeaA\xb0\x01\n*cloudbilling.googleapis.com/BillingAccount\x12!billingAccounts/{billing_account}\x12>organizations/{organization}/billingAccounts/{billing_account}*\x0fbillingAccounts2\x0ebillingAccount"\xd1\x01\n\x12ProjectBillingInfo\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x14billing_account_name\x18\x03 \x01(\t\x12\x1c\n\x0fbilling_enabled\x18\x04 \x01(\x08B\x03\xe0A\x03:S\xeaAP\n.cloudbilling.googleapis.com/ProjectBillingInfo\x12\x1eprojects/{project}/billingInfo"\\\n\x18GetBillingAccountRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount"h\n\x1aListBillingAccountsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x13\n\x06parent\x18\x04 \x01(\tB\x03\xe0A\x01"y\n\x1bListBillingAccountsResponse\x12A\n\x10billing_accounts\x18\x01 \x03(\x0b2\'.google.cloud.billing.v1.BillingAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"y\n\x1bCreateBillingAccountRequest\x12E\n\x0fbilling_account\x18\x01 \x01(\x0b2\'.google.cloud.billing.v1.BillingAccountB\x03\xe0A\x02\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x01"\xcf\x01\n\x1bUpdateBillingAccountRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12=\n\x07account\x18\x02 \x01(\x0b2\'.google.cloud.billing.v1.BillingAccountB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x88\x01\n\x1dListProjectBillingInfoRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x84\x01\n\x1eListProjectBillingInfoResponse\x12I\n\x14project_billing_info\x18\x01 \x03(\x0b2+.google.cloud.billing.v1.ProjectBillingInfo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x1cGetProjectBillingInfoRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"\x7f\n\x1fUpdateProjectBillingInfoRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12I\n\x14project_billing_info\x18\x02 \x01(\x0b2+.google.cloud.billing.v1.ProjectBillingInfo"\xb3\x01\n\x19MoveBillingAccountRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12T\n\x12destination_parent\x18\x02 \x01(\tB8\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization2\xa1\x13\n\x0cCloudBilling\x12\x9c\x01\n\x11GetBillingAccount\x121.google.cloud.billing.v1.GetBillingAccountRequest\x1a\'.google.cloud.billing.v1.BillingAccount"+\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=billingAccounts/*}\x12\x88\x02\n\x13ListBillingAccounts\x123.google.cloud.billing.v1.ListBillingAccountsRequest\x1a4.google.cloud.billing.v1.ListBillingAccountsResponse"\x85\x01\xdaA\x00\xdaA\x06parent\x82\xd3\xe4\x93\x02s\x12\x13/v1/billingAccountsZ.\x12,/v1/{parent=organizations/*}/billingAccountsZ,\x12*/v1/{parent=billingAccounts/*}/subAccounts\x12\xb3\x01\n\x14UpdateBillingAccount\x124.google.cloud.billing.v1.UpdateBillingAccountRequest\x1a\'.google.cloud.billing.v1.BillingAccount"<\xdaA\x0cname,account\x82\xd3\xe4\x93\x02\'2\x1c/v1/{name=billingAccounts/*}:\x07account\x12\xd0\x02\n\x14CreateBillingAccount\x124.google.cloud.billing.v1.CreateBillingAccountRequest\x1a\'.google.cloud.billing.v1.BillingAccount"\xd8\x01\xdaA\x0fbilling_account\xdaA\x16billing_account,parent\x82\xd3\xe4\x93\x02\xa6\x01"\x13/v1/billingAccounts:\x0fbilling_accountZ?",/v1/{parent=organizations/*}/billingAccounts:\x0fbilling_accountZ="*/v1/{parent=billingAccounts/*}/subAccounts:\x0fbilling_account\x12\xbf\x01\n\x16ListProjectBillingInfo\x126.google.cloud.billing.v1.ListProjectBillingInfoRequest\x1a7.google.cloud.billing.v1.ListProjectBillingInfoResponse"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/v1/{name=billingAccounts/*}/projects\x12\xad\x01\n\x15GetProjectBillingInfo\x125.google.cloud.billing.v1.GetProjectBillingInfoRequest\x1a+.google.cloud.billing.v1.ProjectBillingInfo"0\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*}/billingInfo\x12\xde\x01\n\x18UpdateProjectBillingInfo\x128.google.cloud.billing.v1.UpdateProjectBillingInfoRequest\x1a+.google.cloud.billing.v1.ProjectBillingInfo"[\xdaA\x19name,project_billing_info\x82\xd3\xe4\x93\x029\x1a!/v1/{name=projects/*}/billingInfo:\x14project_billing_info\x12\x8b\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"@\xdaA\x08resource\x82\xd3\xe4\x93\x02/\x12-/v1/{resource=billingAccounts/*}:getIamPolicy\x12\x95\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"J\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x022"-/v1/{resource=billingAccounts/*}:setIamPolicy:\x01*\x12\xc0\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"U\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x028"3/v1/{resource=billingAccounts/*}:testIamPermissions:\x01*\x12\xe9\x01\n\x12MoveBillingAccount\x122.google.cloud.billing.v1.MoveBillingAccountRequest\x1a\'.google.cloud.billing.v1.BillingAccount"v\x82\xd3\xe4\x93\x02p"!/v1/{name=billingAccounts/*}:move:\x01*ZH\x12F/v1/{destination_parent=organizations/*}/{name=billingAccounts/*}:move\x1a\xb5\x01\xcaA\x1bcloudbilling.googleapis.com\xd2A\x93\x01https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-billing.readonly,https://www.googleapis.com/auth/cloud-platformB\x80\x02\n\x1bcom.google.cloud.billing.v1B\x11CloudBillingProtoP\x01Z5cloud.google.com/go/billing/apiv1/billingpb;billingpb\xeaAA\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}\xeaAP\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.billing.v1.cloud_billing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.billing.v1B\x11CloudBillingProtoP\x01Z5cloud.google.com/go/billing/apiv1/billingpb;billingpb\xeaAA\n+cloudresourcemanager.googleapis.com/Project\x12\x12projects/{project}\xeaAP\n0cloudresourcemanager.googleapis.com/Organization\x12\x1corganizations/{organization}'
    _globals['_BILLINGACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_BILLINGACCOUNT'].fields_by_name['open']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['open']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT'].fields_by_name['parent']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['parent']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT'].fields_by_name['currency_code']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x01'
    _globals['_BILLINGACCOUNT']._loaded_options = None
    _globals['_BILLINGACCOUNT']._serialized_options = b'\xeaA\xb0\x01\n*cloudbilling.googleapis.com/BillingAccount\x12!billingAccounts/{billing_account}\x12>organizations/{organization}/billingAccounts/{billing_account}*\x0fbillingAccounts2\x0ebillingAccount'
    _globals['_PROJECTBILLINGINFO'].fields_by_name['name']._loaded_options = None
    _globals['_PROJECTBILLINGINFO'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECTBILLINGINFO'].fields_by_name['project_id']._loaded_options = None
    _globals['_PROJECTBILLINGINFO'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECTBILLINGINFO'].fields_by_name['billing_enabled']._loaded_options = None
    _globals['_PROJECTBILLINGINFO'].fields_by_name['billing_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECTBILLINGINFO']._loaded_options = None
    _globals['_PROJECTBILLINGINFO']._serialized_options = b'\xeaAP\n.cloudbilling.googleapis.com/ProjectBillingInfo\x12\x1eprojects/{project}/billingInfo'
    _globals['_GETBILLINGACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBILLINGACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_LISTBILLINGACCOUNTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBILLINGACCOUNTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEBILLINGACCOUNTREQUEST'].fields_by_name['billing_account']._loaded_options = None
    _globals['_CREATEBILLINGACCOUNTREQUEST'].fields_by_name['billing_account']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBILLINGACCOUNTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBILLINGACCOUNTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEBILLINGACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEBILLINGACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_UPDATEBILLINGACCOUNTREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_UPDATEBILLINGACCOUNTREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_GETPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_UPDATEPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEPROJECTBILLINGINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEBILLINGACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MOVEBILLINGACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_MOVEBILLINGACCOUNTREQUEST'].fields_by_name['destination_parent']._loaded_options = None
    _globals['_MOVEBILLINGACCOUNTREQUEST'].fields_by_name['destination_parent']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudresourcemanager.googleapis.com/Organization'
    _globals['_CLOUDBILLING']._loaded_options = None
    _globals['_CLOUDBILLING']._serialized_options = b'\xcaA\x1bcloudbilling.googleapis.com\xd2A\x93\x01https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-billing.readonly,https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDBILLING'].methods_by_name['GetBillingAccount']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['GetBillingAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=billingAccounts/*}'
    _globals['_CLOUDBILLING'].methods_by_name['ListBillingAccounts']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['ListBillingAccounts']._serialized_options = b'\xdaA\x00\xdaA\x06parent\x82\xd3\xe4\x93\x02s\x12\x13/v1/billingAccountsZ.\x12,/v1/{parent=organizations/*}/billingAccountsZ,\x12*/v1/{parent=billingAccounts/*}/subAccounts'
    _globals['_CLOUDBILLING'].methods_by_name['UpdateBillingAccount']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['UpdateBillingAccount']._serialized_options = b"\xdaA\x0cname,account\x82\xd3\xe4\x93\x02'2\x1c/v1/{name=billingAccounts/*}:\x07account"
    _globals['_CLOUDBILLING'].methods_by_name['CreateBillingAccount']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['CreateBillingAccount']._serialized_options = b'\xdaA\x0fbilling_account\xdaA\x16billing_account,parent\x82\xd3\xe4\x93\x02\xa6\x01"\x13/v1/billingAccounts:\x0fbilling_accountZ?",/v1/{parent=organizations/*}/billingAccounts:\x0fbilling_accountZ="*/v1/{parent=billingAccounts/*}/subAccounts:\x0fbilling_account'
    _globals['_CLOUDBILLING'].methods_by_name['ListProjectBillingInfo']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['ListProjectBillingInfo']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/v1/{name=billingAccounts/*}/projects"
    _globals['_CLOUDBILLING'].methods_by_name['GetProjectBillingInfo']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['GetProjectBillingInfo']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*}/billingInfo'
    _globals['_CLOUDBILLING'].methods_by_name['UpdateProjectBillingInfo']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['UpdateProjectBillingInfo']._serialized_options = b'\xdaA\x19name,project_billing_info\x82\xd3\xe4\x93\x029\x1a!/v1/{name=projects/*}/billingInfo:\x14project_billing_info'
    _globals['_CLOUDBILLING'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02/\x12-/v1/{resource=billingAccounts/*}:getIamPolicy'
    _globals['_CLOUDBILLING'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x022"-/v1/{resource=billingAccounts/*}:setIamPolicy:\x01*'
    _globals['_CLOUDBILLING'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x028"3/v1/{resource=billingAccounts/*}:testIamPermissions:\x01*'
    _globals['_CLOUDBILLING'].methods_by_name['MoveBillingAccount']._loaded_options = None
    _globals['_CLOUDBILLING'].methods_by_name['MoveBillingAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02p"!/v1/{name=billingAccounts/*}:move:\x01*ZH\x12F/v1/{destination_parent=organizations/*}/{name=billingAccounts/*}:move'
    _globals['_BILLINGACCOUNT']._serialized_start = 282
    _globals['_BILLINGACCOUNT']._serialized_end = 669
    _globals['_PROJECTBILLINGINFO']._serialized_start = 672
    _globals['_PROJECTBILLINGINFO']._serialized_end = 881
    _globals['_GETBILLINGACCOUNTREQUEST']._serialized_start = 883
    _globals['_GETBILLINGACCOUNTREQUEST']._serialized_end = 975
    _globals['_LISTBILLINGACCOUNTSREQUEST']._serialized_start = 977
    _globals['_LISTBILLINGACCOUNTSREQUEST']._serialized_end = 1081
    _globals['_LISTBILLINGACCOUNTSRESPONSE']._serialized_start = 1083
    _globals['_LISTBILLINGACCOUNTSRESPONSE']._serialized_end = 1204
    _globals['_CREATEBILLINGACCOUNTREQUEST']._serialized_start = 1206
    _globals['_CREATEBILLINGACCOUNTREQUEST']._serialized_end = 1327
    _globals['_UPDATEBILLINGACCOUNTREQUEST']._serialized_start = 1330
    _globals['_UPDATEBILLINGACCOUNTREQUEST']._serialized_end = 1537
    _globals['_LISTPROJECTBILLINGINFOREQUEST']._serialized_start = 1540
    _globals['_LISTPROJECTBILLINGINFOREQUEST']._serialized_end = 1676
    _globals['_LISTPROJECTBILLINGINFORESPONSE']._serialized_start = 1679
    _globals['_LISTPROJECTBILLINGINFORESPONSE']._serialized_end = 1811
    _globals['_GETPROJECTBILLINGINFOREQUEST']._serialized_start = 1813
    _globals['_GETPROJECTBILLINGINFOREQUEST']._serialized_end = 1910
    _globals['_UPDATEPROJECTBILLINGINFOREQUEST']._serialized_start = 1912
    _globals['_UPDATEPROJECTBILLINGINFOREQUEST']._serialized_end = 2039
    _globals['_MOVEBILLINGACCOUNTREQUEST']._serialized_start = 2042
    _globals['_MOVEBILLINGACCOUNTREQUEST']._serialized_end = 2221
    _globals['_CLOUDBILLING']._serialized_start = 2224
    _globals['_CLOUDBILLING']._serialized_end = 4689