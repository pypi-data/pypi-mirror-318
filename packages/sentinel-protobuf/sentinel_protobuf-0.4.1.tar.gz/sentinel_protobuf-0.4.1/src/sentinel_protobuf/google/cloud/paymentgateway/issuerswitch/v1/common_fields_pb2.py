"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
from ......google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x12+google.cloud.paymentgateway.issuerswitch.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/type/latlng.proto\x1a\x17google/type/money.proto"S\n\x10AccountReference\x12\x0c\n\x04ifsc\x18\x01 \x01(\t\x12\x19\n\x0caccount_type\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x16\n\x0eaccount_number\x18\x03 \x01(\t"\xd5\x03\n\x15SettlementParticipant\x12M\n\x0bparticipant\x18\x01 \x01(\x0b28.google.cloud.paymentgateway.issuerswitch.v1.Participant\x12P\n\rmerchant_info\x18\x02 \x01(\x0b29.google.cloud.paymentgateway.issuerswitch.v1.MerchantInfo\x12\x15\n\x06mobile\x18\x03 \x01(\tB\x05\x18\x01\xe0A\x03\x12j\n\x07details\x18\x04 \x01(\x0b2T.google.cloud.paymentgateway.issuerswitch.v1.SettlementParticipant.SettlementDetailsB\x03\xe0A\x03\x1a\x97\x01\n\x11SettlementDetails\x12"\n\x15backend_settlement_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rreversal_code\x18\x03 \x01(\tB\x03\xe0A\x03\x12/\n\x0esettled_amount\x18\x04 \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x03"\xd3\x01\n\rDeviceDetails\x12\x13\n\x0bpayment_app\x18\x01 \x01(\t\x12\x12\n\ncapability\x18\x02 \x01(\t\x12%\n\x08geo_code\x18\x03 \x01(\x0b2\x13.google.type.LatLng\x12\n\n\x02id\x18\x04 \x01(\t\x12\x12\n\nip_address\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x18\n\x10operating_system\x18\x07 \x01(\t\x12\x18\n\x10telecom_provider\x18\x08 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t"\x8d\x03\n\x0bParticipant\x12\x17\n\x0fpayment_address\x18\x01 \x01(\t\x12Q\n\x07persona\x18\x02 \x01(\x0e2@.google.cloud.paymentgateway.issuerswitch.v1.Participant.Persona\x12\x0c\n\x04user\x18\x03 \x01(\t\x12S\n\x07account\x18\x04 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceB\x03\xe0A\x03\x12W\n\x0edevice_details\x18\x05 \x01(\x0b2:.google.cloud.paymentgateway.issuerswitch.v1.DeviceDetailsB\x03\xe0A\x03\x12\x1a\n\rmobile_number\x18\x06 \x01(\tB\x03\xe0A\x03":\n\x07Persona\x12\x17\n\x13PERSONA_UNSPECIFIED\x10\x00\x12\n\n\x06ENTITY\x10\x01\x12\n\n\x06PERSON\x10\x02"\xc5\x01\n\x0cMerchantInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12K\n\x08merchant\x18\x02 \x01(\x0b29.google.cloud.paymentgateway.issuerswitch.v1.MerchantName\x12\\\n\x0fadditional_info\x18\x03 \x01(\x0b2C.google.cloud.paymentgateway.issuerswitch.v1.MerchantAdditionalInfo"?\n\x0cMerchantName\x12\r\n\x05brand\x18\x01 \x01(\t\x12\r\n\x05legal\x18\x02 \x01(\t\x12\x11\n\tfranchise\x18\x03 \x01(\t"\xa9\x06\n\x16MerchantAdditionalInfo\x12\x15\n\rcategory_code\x18\x01 \x01(\t\x12\x10\n\x08store_id\x18\x02 \x01(\t\x12\x13\n\x0bterminal_id\x18\x03 \x01(\t\x12V\n\x04type\x18\x04 \x01(\x0e2H.google.cloud.paymentgateway.issuerswitch.v1.MerchantAdditionalInfo.Type\x12X\n\x05genre\x18\x05 \x01(\x0e2I.google.cloud.paymentgateway.issuerswitch.v1.MerchantAdditionalInfo.Genre\x12k\n\x0fonboarding_type\x18\x06 \x01(\x0e2R.google.cloud.paymentgateway.issuerswitch.v1.MerchantAdditionalInfo.OnboardingType\x12i\n\x0eownership_type\x18\x07 \x01(\x0e2Q.google.cloud.paymentgateway.issuerswitch.v1.MerchantAdditionalInfo.OwnershipType"2\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05LARGE\x10\x01\x12\t\n\x05SMALL\x10\x02"7\n\x05Genre\x12\x15\n\x11GENRE_UNSPECIFIED\x10\x00\x12\x0b\n\x07OFFLINE\x10\x01\x12\n\n\x06ONLINE\x10\x02"b\n\x0eOnboardingType\x12\x1f\n\x1bONBOARDING_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nAGGREGATOR\x10\x01\x12\x08\n\x04BANK\x10\x02\x12\x0b\n\x07NETWORK\x10\x03\x12\x08\n\x04TPAP\x10\x04"v\n\rOwnershipType\x12\x1e\n\x1aOWNERSHIP_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPROPRIETARY\x10\x01\x12\x0f\n\x0bPARTNERSHIP\x10\x02\x12\n\n\x06PUBLIC\x10\x03\x12\x0b\n\x07PRIVATE\x10\x04\x12\n\n\x06OTHERS\x10\x05*\xcb\x02\n\x07ApiType\x12\x18\n\x14API_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07BALANCE\x10\x01\x12\x10\n\x0cCHECK_STATUS\x10\x02\x12\r\n\tCOMPLAINT\x10\x03\x12\x0e\n\nHEART_BEAT\x10\x04\x12\x19\n\x15INITIATE_REGISTRATION\x10\x05\x12\x11\n\rLIST_ACCOUNTS\x10\x06\x12\x0b\n\x07MANDATE\x10\x07\x12\x18\n\x14MANDATE_CONFIRMATION\x10\x08\x12\x12\n\x0eSETTLE_PAYMENT\x10\t\x12\x16\n\x12UPDATE_CREDENTIALS\x10\n\x12\x19\n\x15VALIDATE_REGISTRATION\x10\x0b\x12\x15\n\x11VALIDATE_CUSTOMER\x10\x0c\x12\x0b\n\x07VOUCHER\x10\r\x12\x18\n\x14VOUCHER_CONFIRMATION\x10\x0e\x12\x0e\n\nACTIVATION\x10\x0f*\xcc\x07\n\x0fTransactionType\x12 \n\x1cTRANSACTION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTRANSACTION_TYPE_AUTOUPDATE\x10\x01\x12"\n\x1eTRANSACTION_TYPE_BALANCE_CHECK\x10\x02\x12$\n TRANSACTION_TYPE_BALANCE_ENQUIRY\x10\x03\x12!\n\x1dTRANSACTION_TYPE_CHECK_STATUS\x10\x04\x12&\n"TRANSACTION_TYPE_CHECK_TRANSACTION\x10\x05\x12\x1e\n\x1aTRANSACTION_TYPE_COMPLAINT\x10\x06\x12\x1b\n\x17TRANSACTION_TYPE_CREATE\x10\x07\x12\x1b\n\x17TRANSACTION_TYPE_CREDIT\x10\x08\x12\x1a\n\x16TRANSACTION_TYPE_DEBIT\x10\t\x12\x1c\n\x18TRANSACTION_TYPE_DISPUTE\x10\n\x12\x1f\n\x1bTRANSACTION_TYPE_HEART_BEAT\x10\x0b\x12"\n\x1eTRANSACTION_TYPE_LIST_ACCOUNTS\x10\x0c\x12)\n%TRANSACTION_TYPE_MANDATE_NOTIFICATION\x10\r\x12\x18\n\x14TRANSACTION_TYPE_OTP\x10\x0e\x12\x1a\n\x16TRANSACTION_TYPE_PAUSE\x10\x0f\x12\x1b\n\x17TRANSACTION_TYPE_REDEEM\x10\x10\x12\x1b\n\x17TRANSACTION_TYPE_REFUND\x10\x11\x12$\n TRANSACTION_TYPE_REGISTER_MOBILE\x10\x12\x12\x1d\n\x19TRANSACTION_TYPE_REVERSAL\x10\x13\x12\x1b\n\x17TRANSACTION_TYPE_REVOKE\x10\x14\x12"\n\x1eTRANSACTION_TYPE_STATUS_UPDATE\x10\x15\x12\x1c\n\x18TRANSACTION_TYPE_UNPAUSE\x10\x16\x12\x1b\n\x17TRANSACTION_TYPE_UPDATE\x10\x17\x12\'\n#TRANSACTION_TYPE_UPDATE_CREDENTIALS\x10\x18\x12&\n"TRANSACTION_TYPE_VALIDATE_CUSTOMER\x10\x19\x12-\n)TRANSACTION_TYPE_ACTIVATION_INTERNATIONAL\x10\x1a\x12,\n(TRANSACTION_TYPE_ACTIVATION_UPI_SERVICES\x10\x1b*\x9e\x05\n\nXmlApiType\x12\x1c\n\x18XML_API_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bREQ_BAL_ENQ\x10\x01\x12\x0f\n\x0bREQ_CHK_TXN\x10\x02\x12\x11\n\rREQ_COMPLAINT\x10\x03\x12\x0b\n\x07REQ_HBT\x10\x04\x12\x14\n\x10REQ_LIST_ACCOUNT\x10\x05\x12\x0f\n\x0bREQ_MANDATE\x10\x06\x12\x1c\n\x18REQ_MANDATE_CONFIRMATION\x10\x07\x12\x0b\n\x07REQ_OTP\x10\x08\x12\x0b\n\x07REQ_PAY\x10\t\x12\x0f\n\x0bREQ_REG_MOB\x10\n\x12\x0f\n\x0bREQ_SET_CRE\x10\x0b\x12\x10\n\x0cREQ_VAL_CUST\x10\x0c\x12\x0f\n\x0bREQ_VOUCHER\x10\r\x12\x1c\n\x18REQ_VOUCHER_CONFIRMATION\x10\x0e\x12\x18\n\x14REQ_TXN_CONFIRMATION\x10\x0f\x12\x10\n\x0cRESP_BAL_ENQ\x10\x10\x12\x10\n\x0cRESP_CHK_TXN\x10\x11\x12\x12\n\x0eRESP_COMPLAINT\x10\x12\x12\x0c\n\x08RESP_HBT\x10\x13\x12\x15\n\x11RESP_LIST_ACCOUNT\x10\x14\x12\x10\n\x0cRESP_MANDATE\x10\x15\x12\x1d\n\x19RESP_MANDATE_CONFIRMATION\x10\x16\x12\x0c\n\x08RESP_OTP\x10\x17\x12\x0c\n\x08RESP_PAY\x10\x18\x12\x10\n\x0cRESP_REG_MOB\x10\x19\x12\x10\n\x0cRESP_SET_CRE\x10\x1a\x12\x11\n\rRESP_VAL_CUST\x10\x1b\x12\x10\n\x0cRESP_VOUCHER\x10\x1c\x12\x1d\n\x19RESP_VOUCHER_CONFIRMATION\x10\x1d\x12\x19\n\x15RESP_TXN_CONFIRMATION\x10\x1e\x12\x12\n\x0eREQ_ACTIVATION\x10\x1f\x12\x13\n\x0fRESP_ACTIVATION\x10 B\xa9\x02\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x11CommonFieldsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.v1.common_fields_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x11CommonFieldsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1'
    _globals['_ACCOUNTREFERENCE'].fields_by_name['account_type']._loaded_options = None
    _globals['_ACCOUNTREFERENCE'].fields_by_name['account_type']._serialized_options = b'\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['backend_settlement_id']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['backend_settlement_id']._serialized_options = b'\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['code']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['reversal_code']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['reversal_code']._serialized_options = b'\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['settled_amount']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS'].fields_by_name['settled_amount']._serialized_options = b'\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT'].fields_by_name['mobile']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT'].fields_by_name['mobile']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_SETTLEMENTPARTICIPANT'].fields_by_name['details']._loaded_options = None
    _globals['_SETTLEMENTPARTICIPANT'].fields_by_name['details']._serialized_options = b'\xe0A\x03'
    _globals['_PARTICIPANT'].fields_by_name['account']._loaded_options = None
    _globals['_PARTICIPANT'].fields_by_name['account']._serialized_options = b'\xe0A\x03'
    _globals['_PARTICIPANT'].fields_by_name['device_details']._loaded_options = None
    _globals['_PARTICIPANT'].fields_by_name['device_details']._serialized_options = b'\xe0A\x03'
    _globals['_PARTICIPANT'].fields_by_name['mobile_number']._loaded_options = None
    _globals['_PARTICIPANT'].fields_by_name['mobile_number']._serialized_options = b'\xe0A\x03'
    _globals['_APITYPE']._serialized_start = 2445
    _globals['_APITYPE']._serialized_end = 2776
    _globals['_TRANSACTIONTYPE']._serialized_start = 2779
    _globals['_TRANSACTIONTYPE']._serialized_end = 3751
    _globals['_XMLAPITYPE']._serialized_start = 3754
    _globals['_XMLAPITYPE']._serialized_end = 4424
    _globals['_ACCOUNTREFERENCE']._serialized_start = 196
    _globals['_ACCOUNTREFERENCE']._serialized_end = 279
    _globals['_SETTLEMENTPARTICIPANT']._serialized_start = 282
    _globals['_SETTLEMENTPARTICIPANT']._serialized_end = 751
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS']._serialized_start = 600
    _globals['_SETTLEMENTPARTICIPANT_SETTLEMENTDETAILS']._serialized_end = 751
    _globals['_DEVICEDETAILS']._serialized_start = 754
    _globals['_DEVICEDETAILS']._serialized_end = 965
    _globals['_PARTICIPANT']._serialized_start = 968
    _globals['_PARTICIPANT']._serialized_end = 1365
    _globals['_PARTICIPANT_PERSONA']._serialized_start = 1307
    _globals['_PARTICIPANT_PERSONA']._serialized_end = 1365
    _globals['_MERCHANTINFO']._serialized_start = 1368
    _globals['_MERCHANTINFO']._serialized_end = 1565
    _globals['_MERCHANTNAME']._serialized_start = 1567
    _globals['_MERCHANTNAME']._serialized_end = 1630
    _globals['_MERCHANTADDITIONALINFO']._serialized_start = 1633
    _globals['_MERCHANTADDITIONALINFO']._serialized_end = 2442
    _globals['_MERCHANTADDITIONALINFO_TYPE']._serialized_start = 2115
    _globals['_MERCHANTADDITIONALINFO_TYPE']._serialized_end = 2165
    _globals['_MERCHANTADDITIONALINFO_GENRE']._serialized_start = 2167
    _globals['_MERCHANTADDITIONALINFO_GENRE']._serialized_end = 2222
    _globals['_MERCHANTADDITIONALINFO_ONBOARDINGTYPE']._serialized_start = 2224
    _globals['_MERCHANTADDITIONALINFO_ONBOARDINGTYPE']._serialized_end = 2322
    _globals['_MERCHANTADDITIONALINFO_OWNERSHIPTYPE']._serialized_start = 2324
    _globals['_MERCHANTADDITIONALINFO_OWNERSHIPTYPE']._serialized_end = 2442