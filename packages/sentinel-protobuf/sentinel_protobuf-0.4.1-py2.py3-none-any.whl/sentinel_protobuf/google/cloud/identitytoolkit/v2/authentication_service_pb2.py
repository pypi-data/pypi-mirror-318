"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/identitytoolkit/v2/authentication_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.identitytoolkit.v2 import mfa_info_pb2 as google_dot_cloud_dot_identitytoolkit_dot_v2_dot_mfa__info__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/identitytoolkit/v2/authentication_service.proto\x12\x1fgoogle.cloud.identitytoolkit.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/identitytoolkit/v2/mfa_info.proto"\xc8\x01\n\x18FinalizeMfaSignInRequest\x12#\n\x16mfa_pending_credential\x18\x02 \x01(\tB\x03\xe0A\x02\x12_\n\x17phone_verification_info\x18\x03 \x01(\x0b2<.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneRequestInfoH\x00\x12\x11\n\ttenant_id\x18\x04 \x01(\tB\x13\n\x11verification_info"\xb5\x01\n\x19FinalizeMfaSignInResponse\x12\x10\n\x08id_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12X\n\x0fphone_auth_info\x18\x03 \x01(\x0b2=.google.cloud.identitytoolkit.v2.FinalizeMfaPhoneResponseInfoH\x00B\x15\n\x13auxiliary_auth_info"\xd8\x01\n\x15StartMfaSignInRequest\x12#\n\x16mfa_pending_credential\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11mfa_enrollment_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12W\n\x12phone_sign_in_info\x18\x04 \x01(\x0b29.google.cloud.identitytoolkit.v2.StartMfaPhoneRequestInfoH\x00\x12\x11\n\ttenant_id\x18\x05 \x01(\tB\x0e\n\x0csign_in_info"\x84\x01\n\x16StartMfaSignInResponse\x12Y\n\x13phone_response_info\x18\x01 \x01(\x0b2:.google.cloud.identitytoolkit.v2.StartMfaPhoneResponseInfoH\x00B\x0f\n\rresponse_info2\xd1\x03\n\x15AuthenticationService\x12\xb6\x01\n\x11FinalizeMfaSignIn\x129.google.cloud.identitytoolkit.v2.FinalizeMfaSignInRequest\x1a:.google.cloud.identitytoolkit.v2.FinalizeMfaSignInResponse"*\x82\xd3\xe4\x93\x02$"\x1f/v2/accounts/mfaSignIn:finalize:\x01*\x12\xaa\x01\n\x0eStartMfaSignIn\x126.google.cloud.identitytoolkit.v2.StartMfaSignInRequest\x1a7.google.cloud.identitytoolkit.v2.StartMfaSignInResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/v2/accounts/mfaSignIn:start:\x01*\x1aR\xcaA\x1eidentitytoolkit.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdf\x01\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.identitytoolkit.v2.authentication_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.identitytoolkit.v2P\x01ZMcloud.google.com/go/identitytoolkit/apiv2/identitytoolkitpb;identitytoolkitpb\xaa\x02\x1fGoogle.Cloud.IdentityToolkit.V2\xca\x02\x1fGoogle\\Cloud\\IdentityToolkit\\V2\xea\x02"Google::Cloud::IdentityToolkit::V2'
    _globals['_FINALIZEMFASIGNINREQUEST'].fields_by_name['mfa_pending_credential']._loaded_options = None
    _globals['_FINALIZEMFASIGNINREQUEST'].fields_by_name['mfa_pending_credential']._serialized_options = b'\xe0A\x02'
    _globals['_STARTMFASIGNINREQUEST'].fields_by_name['mfa_pending_credential']._loaded_options = None
    _globals['_STARTMFASIGNINREQUEST'].fields_by_name['mfa_pending_credential']._serialized_options = b'\xe0A\x02'
    _globals['_STARTMFASIGNINREQUEST'].fields_by_name['mfa_enrollment_id']._loaded_options = None
    _globals['_STARTMFASIGNINREQUEST'].fields_by_name['mfa_enrollment_id']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHENTICATIONSERVICE']._loaded_options = None
    _globals['_AUTHENTICATIONSERVICE']._serialized_options = b'\xcaA\x1eidentitytoolkit.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AUTHENTICATIONSERVICE'].methods_by_name['FinalizeMfaSignIn']._loaded_options = None
    _globals['_AUTHENTICATIONSERVICE'].methods_by_name['FinalizeMfaSignIn']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x1f/v2/accounts/mfaSignIn:finalize:\x01*'
    _globals['_AUTHENTICATIONSERVICE'].methods_by_name['StartMfaSignIn']._loaded_options = None
    _globals['_AUTHENTICATIONSERVICE'].methods_by_name['StartMfaSignIn']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/v2/accounts/mfaSignIn:start:\x01*'
    _globals['_FINALIZEMFASIGNINREQUEST']._serialized_start = 234
    _globals['_FINALIZEMFASIGNINREQUEST']._serialized_end = 434
    _globals['_FINALIZEMFASIGNINRESPONSE']._serialized_start = 437
    _globals['_FINALIZEMFASIGNINRESPONSE']._serialized_end = 618
    _globals['_STARTMFASIGNINREQUEST']._serialized_start = 621
    _globals['_STARTMFASIGNINREQUEST']._serialized_end = 837
    _globals['_STARTMFASIGNINRESPONSE']._serialized_start = 840
    _globals['_STARTMFASIGNINRESPONSE']._serialized_end = 972
    _globals['_AUTHENTICATIONSERVICE']._serialized_start = 975
    _globals['_AUTHENTICATIONSERVICE']._serialized_end = 1440