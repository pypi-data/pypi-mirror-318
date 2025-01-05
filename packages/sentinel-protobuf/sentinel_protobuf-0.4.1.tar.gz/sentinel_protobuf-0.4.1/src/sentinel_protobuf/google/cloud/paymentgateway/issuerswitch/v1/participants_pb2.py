"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/v1/participants.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/paymentgateway/issuerswitch/v1/participants.proto\x12+google.cloud.paymentgateway.issuerswitch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8d\x01\n\x17FetchParticipantRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\x11account_reference\x18\x02 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceB\x03\xe0A\x02"\xdc\x06\n\x11IssuerParticipant\x12]\n\x11account_reference\x18\x01 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceB\x03\xe0A\x02\x12\x1a\n\rmobile_number\x18\x02 \x01(\tB\x03\xe0A\x03\x12X\n\x05state\x18\x03 \x01(\x0e2D.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipant.StateB\x03\xe0A\x03\x12^\n\x08metadata\x18\x04 \x01(\x0b2G.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipant.MetadataB\x03\xe0A\x01\x12\x1f\n\x12mpin_failure_count\x18\x05 \x01(\x05B\x03\xe0A\x03\x129\n\x10mpin_locked_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\xa3\x01\n\x08Metadata\x12h\n\x06values\x18\x01 \x03(\x0b2S.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipant.Metadata.ValuesEntryB\x03\xe0A\x01\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa3\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0f\n\x0bMPIN_LOCKED\x10\x03\x12\x19\n\x15MOBILE_NUMBER_CHANGED\x10\x04\x12\x1e\n\x1aNEW_REGISTRATION_INITIATED\x10\x05\x12\x1d\n\x19RE_REGISTRATION_INITIATED\x10\x06"\xcc\x01\n\x1eUpdateIssuerParticipantRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\x12issuer_participant\x18\x02 \x01(\x0b2>.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipantB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xb9\x01\n\x1dParticipantStateChangeRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\x11account_reference\x18\x02 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceB\x03\xe0A\x01H\x00\x12\x1c\n\rmobile_number\x18\x03 \x01(\tB\x03\xe0A\x01H\x00B\x04\n\x02id"o\n\x12IssuerParticipants\x12Y\n\x0cparticipants\x18\x01 \x03(\x0b2>.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipantB\x03\xe0A\x032\xa1\n\n\x18IssuerSwitchParticipants\x12\xd5\x01\n\x10FetchParticipant\x12D.google.cloud.paymentgateway.issuerswitch.v1.FetchParticipantRequest\x1a>.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipant";\x82\xd3\xe4\x93\x025"0/v1/{parent=projects/*}/issuerParticipants:fetch:\x01*\x12\x9d\x02\n\x17UpdateIssuerParticipant\x12K.google.cloud.paymentgateway.issuerswitch.v1.UpdateIssuerParticipantRequest\x1a>.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipant"u\xdaA%parent,issuer_participant,update_mask\x82\xd3\xe4\x93\x02G"1/v1/{parent=projects/*}/issuerParticipants:update:\x12issuer_participant\x12\xe2\x01\n\x13ActivateParticipant\x12J.google.cloud.paymentgateway.issuerswitch.v1.ParticipantStateChangeRequest\x1a?.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipants">\x82\xd3\xe4\x93\x028"3/v1/{parent=projects/*}/issuerParticipants:activate:\x01*\x12\xe6\x01\n\x15DeactivateParticipant\x12J.google.cloud.paymentgateway.issuerswitch.v1.ParticipantStateChangeRequest\x1a?.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipants"@\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*}/issuerParticipants:deactivate:\x01*\x12\xed\x01\n\x13MobileNumberChanged\x12J.google.cloud.paymentgateway.issuerswitch.v1.ParticipantStateChangeRequest\x1a?.google.cloud.paymentgateway.issuerswitch.v1.IssuerParticipants"I\x82\xd3\xe4\x93\x02C">/v1/{parent=projects/*}/issuerParticipants:mobileNumberChanged:\x01*\x1aO\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa9\x02\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x11ParticipantsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.v1.participants_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x11ParticipantsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1'
    _globals['_FETCHPARTICIPANTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_FETCHPARTICIPANTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_FETCHPARTICIPANTREQUEST'].fields_by_name['account_reference']._loaded_options = None
    _globals['_FETCHPARTICIPANTREQUEST'].fields_by_name['account_reference']._serialized_options = b'\xe0A\x02'
    _globals['_ISSUERPARTICIPANT_METADATA_VALUESENTRY']._loaded_options = None
    _globals['_ISSUERPARTICIPANT_METADATA_VALUESENTRY']._serialized_options = b'8\x01'
    _globals['_ISSUERPARTICIPANT_METADATA'].fields_by_name['values']._loaded_options = None
    _globals['_ISSUERPARTICIPANT_METADATA'].fields_by_name['values']._serialized_options = b'\xe0A\x01'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['account_reference']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['account_reference']._serialized_options = b'\xe0A\x02'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mobile_number']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mobile_number']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['state']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['metadata']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mpin_failure_count']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mpin_failure_count']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mpin_locked_time']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['mpin_locked_time']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERPARTICIPANT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ISSUERPARTICIPANT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['issuer_participant']._loaded_options = None
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['issuer_participant']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEISSUERPARTICIPANTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['account_reference']._loaded_options = None
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['account_reference']._serialized_options = b'\xe0A\x01'
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['mobile_number']._loaded_options = None
    _globals['_PARTICIPANTSTATECHANGEREQUEST'].fields_by_name['mobile_number']._serialized_options = b'\xe0A\x01'
    _globals['_ISSUERPARTICIPANTS'].fields_by_name['participants']._loaded_options = None
    _globals['_ISSUERPARTICIPANTS'].fields_by_name['participants']._serialized_options = b'\xe0A\x03'
    _globals['_ISSUERSWITCHPARTICIPANTS']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS']._serialized_options = b'\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['FetchParticipant']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['FetchParticipant']._serialized_options = b'\x82\xd3\xe4\x93\x025"0/v1/{parent=projects/*}/issuerParticipants:fetch:\x01*'
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['UpdateIssuerParticipant']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['UpdateIssuerParticipant']._serialized_options = b'\xdaA%parent,issuer_participant,update_mask\x82\xd3\xe4\x93\x02G"1/v1/{parent=projects/*}/issuerParticipants:update:\x12issuer_participant'
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['ActivateParticipant']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['ActivateParticipant']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/v1/{parent=projects/*}/issuerParticipants:activate:\x01*'
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['DeactivateParticipant']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['DeactivateParticipant']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1/{parent=projects/*}/issuerParticipants:deactivate:\x01*'
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['MobileNumberChanged']._loaded_options = None
    _globals['_ISSUERSWITCHPARTICIPANTS'].methods_by_name['MobileNumberChanged']._serialized_options = b'\x82\xd3\xe4\x93\x02C">/v1/{parent=projects/*}/issuerParticipants:mobileNumberChanged:\x01*'
    _globals['_FETCHPARTICIPANTREQUEST']._serialized_start = 332
    _globals['_FETCHPARTICIPANTREQUEST']._serialized_end = 473
    _globals['_ISSUERPARTICIPANT']._serialized_start = 476
    _globals['_ISSUERPARTICIPANT']._serialized_end = 1336
    _globals['_ISSUERPARTICIPANT_METADATA']._serialized_start = 1007
    _globals['_ISSUERPARTICIPANT_METADATA']._serialized_end = 1170
    _globals['_ISSUERPARTICIPANT_METADATA_VALUESENTRY']._serialized_start = 1125
    _globals['_ISSUERPARTICIPANT_METADATA_VALUESENTRY']._serialized_end = 1170
    _globals['_ISSUERPARTICIPANT_STATE']._serialized_start = 1173
    _globals['_ISSUERPARTICIPANT_STATE']._serialized_end = 1336
    _globals['_UPDATEISSUERPARTICIPANTREQUEST']._serialized_start = 1339
    _globals['_UPDATEISSUERPARTICIPANTREQUEST']._serialized_end = 1543
    _globals['_PARTICIPANTSTATECHANGEREQUEST']._serialized_start = 1546
    _globals['_PARTICIPANTSTATECHANGEREQUEST']._serialized_end = 1731
    _globals['_ISSUERPARTICIPANTS']._serialized_start = 1733
    _globals['_ISSUERPARTICIPANTS']._serialized_end = 1844
    _globals['_ISSUERSWITCHPARTICIPANTS']._serialized_start = 1847
    _globals['_ISSUERSWITCHPARTICIPANTS']._serialized_end = 3160