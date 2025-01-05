"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/identitytoolkit/v2/account_management_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.identitytoolkit.v2 import mfa_info_pb2 as google_dot_cloud_dot_identitytoolkit_dot_v2_dot_mfa__info__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/identitytoolkit/v2/account_management_service.proto\x12\x1fgoogle.cloud.identitytoolkit.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/identitytoolkit/v2/mfa_info.proto"\xd4\x01\n\x1cFinalizeMfaEnrollmentRequest\x12\x15\n\x08id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12_\n\x17phone_verification_info\x18\x04 \x01(\x0b2<.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneRequestInfoH\x00\x12\x11\n\ttenant_id\x18\x05 \x01(\tB\x13\n\x11verification_info"\xb9\x01\n\x1dFinalizeMfaEnrollmentResponse\x12\x10\n\x08id_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12X\n\x0fphone_auth_info\x18\x03 \x01(\x0b2=.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneResponseInfoH\x00B\x15\n\x13auxiliary_auth_info"\xb4\x01\n\x19StartMfaEnrollmentRequest\x12\x15\n\x08id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12Z\n\x15phone_enrollment_info\x18\x03 \x01(\x0b29.google.cloud.identitytoolkit.v2.StartMfaPhoneRequestInfoH\x00\x12\x11\n\ttenant_id\x18\x04 \x01(\tB\x11\n\x0fenrollment_info"\x8d\x01\n\x1aStartMfaEnrollmentResponse\x12X\n\x12phone_session_info\x18\x01 \x01(\x0b2:.google.cloud.identitytoolkit.v2.StartMfaPhoneResponseInfoH\x00B\x15\n\x13enrollment_response"^\n\x12WithdrawMfaRequest\x12\x15\n\x08id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11mfa_enrollment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\ttenant_id\x18\x03 \x01(\t">\n\x13WithdrawMfaResponse\x12\x10\n\x08id_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t2\x9f\x05\n\x18AccountManagementService\x12\xc6\x01\n\x15FinalizeMfaEnrollment\x12=.google.cloud.identitytoolkit.v2.FinalizeMfaEnrollmentRequest\x1a>.google.cloud.identitytoolkit.v2.FinalizeMfaEnrollmentResponse".\x82\xd3\xe4\x93\x02("#/v2/accounts/mfaEnrollment:finalize:\x01*\x12\xba\x01\n\x12StartMfaEnrollment\x12:.google.cloud.identitytoolkit.v2.StartMfaEnrollmentRequest\x1a;.google.cloud.identitytoolkit.v2.StartMfaEnrollmentResponse"+\x82\xd3\xe4\x93\x02%" /v2/accounts/mfaEnrollment:start:\x01*\x12\xa8\x01\n\x0bWithdrawMfa\x123.google.cloud.identitytoolkit.v2.WithdrawMfaRequest\x1a4.google.cloud.identitytoolkit.v2.WithdrawMfaResponse".\x82\xd3\xe4\x93\x02("#/v2/accounts/mfaEnrollment:withdraw:\x01*\x1aR\xcaA\x1eidentitytoolkit.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdf\x01\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.identitytoolkit.v2.account_management_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2'
    _globals['_FINALIZEMFAENROLLMENTREQUEST'].fields_by_name['id_token']._loaded_options = None
    _globals['_FINALIZEMFAENROLLMENTREQUEST'].fields_by_name['id_token']._serialized_options = b'\xe0A\x02'
    _globals['_STARTMFAENROLLMENTREQUEST'].fields_by_name['id_token']._loaded_options = None
    _globals['_STARTMFAENROLLMENTREQUEST'].fields_by_name['id_token']._serialized_options = b'\xe0A\x02'
    _globals['_WITHDRAWMFAREQUEST'].fields_by_name['id_token']._loaded_options = None
    _globals['_WITHDRAWMFAREQUEST'].fields_by_name['id_token']._serialized_options = b'\xe0A\x02'
    _globals['_WITHDRAWMFAREQUEST'].fields_by_name['mfa_enrollment_id']._loaded_options = None
    _globals['_WITHDRAWMFAREQUEST'].fields_by_name['mfa_enrollment_id']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNTMANAGEMENTSERVICE']._loaded_options = None
    _globals['_ACCOUNTMANAGEMENTSERVICE']._serialized_options = b'\xcaA\x1eidentitytoolkit.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['FinalizeMfaEnrollment']._loaded_options = None
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['FinalizeMfaEnrollment']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v2/accounts/mfaEnrollment:finalize:\x01*'
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['StartMfaEnrollment']._loaded_options = None
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['StartMfaEnrollment']._serialized_options = b'\x82\xd3\xe4\x93\x02%" /v2/accounts/mfaEnrollment:start:\x01*'
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['WithdrawMfa']._loaded_options = None
    _globals['_ACCOUNTMANAGEMENTSERVICE'].methods_by_name['WithdrawMfa']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v2/accounts/mfaEnrollment:withdraw:\x01*'
    _globals['_FINALIZEMFAENROLLMENTREQUEST']._serialized_start = 238
    _globals['_FINALIZEMFAENROLLMENTREQUEST']._serialized_end = 450
    _globals['_FINALIZEMFAENROLLMENTRESPONSE']._serialized_start = 453
    _globals['_FINALIZEMFAENROLLMENTRESPONSE']._serialized_end = 638
    _globals['_STARTMFAENROLLMENTREQUEST']._serialized_start = 641
    _globals['_STARTMFAENROLLMENTREQUEST']._serialized_end = 821
    _globals['_STARTMFAENROLLMENTRESPONSE']._serialized_start = 824
    _globals['_STARTMFAENROLLMENTRESPONSE']._serialized_end = 965
    _globals['_WITHDRAWMFAREQUEST']._serialized_start = 967
    _globals['_WITHDRAWMFAREQUEST']._serialized_end = 1061
    _globals['_WITHDRAWMFARESPONSE']._serialized_start = 1063
    _globals['_WITHDRAWMFARESPONSE']._serialized_end = 1125
    _globals['_ACCOUNTMANAGEMENTSERVICE']._serialized_start = 1128
    _globals['_ACCOUNTMANAGEMENTSERVICE']._serialized_end = 1799