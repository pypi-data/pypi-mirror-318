"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/accountmanager/v1/managed_accounts.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .......google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQgoogle/cloud/paymentgateway/issuerswitch/accountmanager/v1/managed_accounts.proto\x12:google.cloud.paymentgateway.issuerswitch.accountmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\x8d\x07\n\x0eManagedAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12]\n\x11account_reference\x18\x02 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceB\x03\xe0A\x02\x12d\n\x05state\x18\x03 \x01(\x0e2P.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ManagedAccount.StateB\x03\xe0A\x03\x12(\n\x07balance\x18\x04 \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x02\x12\x8d\x01\n\x19last_reconciliation_state\x18\x05 \x01(\x0e2e.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ManagedAccount.AccountReconciliationStateB\x03\xe0A\x03\x12A\n\x18last_reconciliation_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03";\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0f\n\x0bDEACTIVATED\x10\x02"e\n\x1aAccountReconciliationState\x12,\n(ACCOUNT_RECONCILIATION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02:\x9a\x01\xeaA\x96\x01\n*issuerswitch.googleapis.com/ManagedAccount\x12Gprojects/{project}/accountManagers/{account_manager}/accounts/{account}*\x0fmanagedAccounts2\x0emanagedAccount"\xf5\x01\n%ReconcileManagedAccountBalanceRequest\x12`\n\x07account\x18\x01 \x01(\x0b2J.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ManagedAccountB\x03\xe0A\x02\x121\n\x10expected_balance\x18\x02 \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x02\x127\n\x0ereference_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\xbb\x01\n*BatchReconcileManagedAccountBalanceRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12x\n\x08requests\x18\x02 \x03(\x0b2a.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ReconcileManagedAccountBalanceRequestB\x03\xe0A\x02"\x8b\x01\n+BatchReconcileManagedAccountBalanceResponse\x12\\\n\x08accounts\x18\x01 \x03(\x0b2J.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ManagedAccount"\\\n\x18GetManagedAccountRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*issuerswitch.googleapis.com/ManagedAccount2\xbd\x05\n\x0fManagedAccounts\x12\xdd\x02\n#BatchReconcileManagedAccountBalance\x12f.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.BatchReconcileManagedAccountBalanceRequest\x1ag.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.BatchReconcileManagedAccountBalanceResponse"e\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/accountManagers/*}/accounts:batchReconcileBalance:\x01*\x12\xf8\x01\n\x11GetManagedAccount\x12T.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.GetManagedAccountRequest\x1aJ.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ManagedAccount"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/accountManagers/*/accounts/*}\x1aO\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfc\x02\n>com.google.cloud.paymentgateway.issuerswitch.accountmanager.v1B\x14ManagedAccountsProtoP\x01Zfcloud.google.com/go/paymentgateway/issuerswitch/accountmanager/apiv1/accountmanagerpb;accountmanagerpb\xaa\x02:Google.Cloud.PaymentGateway.IssuerSwitch.AccountManager.V1\xca\x02:Google\\Cloud\\PaymentGateway\\IssuerSwitch\\AccountManager\\V1\xea\x02?Google::Cloud::PaymentGateway::IssuerSwitch::AccountManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.accountmanager.v1.managed_accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n>com.google.cloud.paymentgateway.issuerswitch.accountmanager.v1B\x14ManagedAccountsProtoP\x01Zfcloud.google.com/go/paymentgateway/issuerswitch/accountmanager/apiv1/accountmanagerpb;accountmanagerpb\xaa\x02:Google.Cloud.PaymentGateway.IssuerSwitch.AccountManager.V1\xca\x02:Google\\Cloud\\PaymentGateway\\IssuerSwitch\\AccountManager\\V1\xea\x02?Google::Cloud::PaymentGateway::IssuerSwitch::AccountManager::V1'
    _globals['_MANAGEDACCOUNT'].fields_by_name['account_reference']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['account_reference']._serialized_options = b'\xe0A\x02'
    _globals['_MANAGEDACCOUNT'].fields_by_name['state']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEDACCOUNT'].fields_by_name['balance']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['balance']._serialized_options = b'\xe0A\x02'
    _globals['_MANAGEDACCOUNT'].fields_by_name['last_reconciliation_state']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['last_reconciliation_state']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEDACCOUNT'].fields_by_name['last_reconciliation_time']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['last_reconciliation_time']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEDACCOUNT'].fields_by_name['create_time']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEDACCOUNT'].fields_by_name['update_time']._loaded_options = None
    _globals['_MANAGEDACCOUNT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEDACCOUNT']._loaded_options = None
    _globals['_MANAGEDACCOUNT']._serialized_options = b'\xeaA\x96\x01\n*issuerswitch.googleapis.com/ManagedAccount\x12Gprojects/{project}/accountManagers/{account_manager}/accounts/{account}*\x0fmanagedAccounts2\x0emanagedAccount'
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['expected_balance']._loaded_options = None
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['expected_balance']._serialized_options = b'\xe0A\x02'
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['reference_time']._loaded_options = None
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['reference_time']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_GETMANAGEDACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMANAGEDACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*issuerswitch.googleapis.com/ManagedAccount'
    _globals['_MANAGEDACCOUNTS']._loaded_options = None
    _globals['_MANAGEDACCOUNTS']._serialized_options = b'\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MANAGEDACCOUNTS'].methods_by_name['BatchReconcileManagedAccountBalance']._loaded_options = None
    _globals['_MANAGEDACCOUNTS'].methods_by_name['BatchReconcileManagedAccountBalance']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/accountManagers/*}/accounts:batchReconcileBalance:\x01*'
    _globals['_MANAGEDACCOUNTS'].methods_by_name['GetManagedAccount']._loaded_options = None
    _globals['_MANAGEDACCOUNTS'].methods_by_name['GetManagedAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/accountManagers/*/accounts/*}'
    _globals['_MANAGEDACCOUNT']._serialized_start = 384
    _globals['_MANAGEDACCOUNT']._serialized_end = 1293
    _globals['_MANAGEDACCOUNT_STATE']._serialized_start = 974
    _globals['_MANAGEDACCOUNT_STATE']._serialized_end = 1033
    _globals['_MANAGEDACCOUNT_ACCOUNTRECONCILIATIONSTATE']._serialized_start = 1035
    _globals['_MANAGEDACCOUNT_ACCOUNTRECONCILIATIONSTATE']._serialized_end = 1136
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST']._serialized_start = 1296
    _globals['_RECONCILEMANAGEDACCOUNTBALANCEREQUEST']._serialized_end = 1541
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST']._serialized_start = 1544
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCEREQUEST']._serialized_end = 1731
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCERESPONSE']._serialized_start = 1734
    _globals['_BATCHRECONCILEMANAGEDACCOUNTBALANCERESPONSE']._serialized_end = 1873
    _globals['_GETMANAGEDACCOUNTREQUEST']._serialized_start = 1875
    _globals['_GETMANAGEDACCOUNTREQUEST']._serialized_end = 1967
    _globals['_MANAGEDACCOUNTS']._serialized_start = 1970
    _globals['_MANAGEDACCOUNTS']._serialized_end = 2671