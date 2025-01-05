"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/abuseevent/logging/v1/abuse_event.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/abuseevent/logging/v1/abuse_event.proto\x12"google.cloud.abuseevent.logging.v1\x1a\x1bgoogle/api/field_info.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x07\n\nAbuseEvent\x12T\n\x0edetection_type\x18\x01 \x01(\x0e2<.google.cloud.abuseevent.logging.v1.AbuseEvent.DetectionType\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12I\n\x06action\x18\x03 \x01(\x0e29.google.cloud.abuseevent.logging.v1.AbuseEvent.ActionType\x12T\n\x13crypto_mining_event\x18\x04 \x01(\x0b25.google.cloud.abuseevent.logging.v1.CryptoMiningEventH\x00\x12\\\n\x17leaked_credential_event\x18\x05 \x01(\x0b29.google.cloud.abuseevent.logging.v1.LeakedCredentialEventH\x00\x12X\n\x15harmful_content_event\x18\x06 \x01(\x0b27.google.cloud.abuseevent.logging.v1.HarmfulContentEventH\x00\x12U\n\x13reinstatement_event\x18\x08 \x01(\x0b26.google.cloud.abuseevent.logging.v1.ReinstatementEventH\x00\x12`\n\x19decision_escalation_event\x18\t \x01(\x0b2;.google.cloud.abuseevent.logging.v1.DecisionEscalationEventH\x00\x12\x18\n\x10remediation_link\x18\x07 \x01(\t"\x83\x01\n\rDetectionType\x12\x1e\n\x1aDETECTION_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rCRYPTO_MINING\x10\x01\x12\x16\n\x12LEAKED_CREDENTIALS\x10\x02\x12\x0c\n\x08PHISHING\x10\x03\x12\x0b\n\x07MALWARE\x10\x04\x12\x0c\n\x08NO_ABUSE\x10\x05"\x7f\n\nActionType\x12\x1b\n\x17ACTION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06NOTIFY\x10\x01\x12\x16\n\x12PROJECT_SUSPENSION\x10\x02\x12\r\n\tREINSTATE\x10\x03\x12\x08\n\x04WARN\x10\x04\x12\x17\n\x13RESOURCE_SUSPENSION\x10\x05B\x0c\n\nevent_type"\xbf\x01\n\x11CryptoMiningEvent\x12\x13\n\x0bvm_resource\x18\x01 \x03(\t\x12>\n\x1adetected_mining_start_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x18detected_mining_end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x05vm_ip\x18\x04 \x03(\tB\x08\xe2\x8c\xcf\xd7\x08\x02\x08\x04"\xf8\x01\n\x15LeakedCredentialEvent\x12b\n\x1aservice_account_credential\x18\x01 \x01(\x0b2<.google.cloud.abuseevent.logging.v1.ServiceAccountCredentialH\x00\x12R\n\x12api_key_credential\x18\x02 \x01(\x0b24.google.cloud.abuseevent.logging.v1.ApiKeyCredentialH\x00\x12\x14\n\x0cdetected_uri\x18\x03 \x01(\tB\x11\n\x0fcredential_type"C\n\x18ServiceAccountCredential\x12\x17\n\x0fservice_account\x18\x01 \x01(\t\x12\x0e\n\x06key_id\x18\x02 \x01(\t"#\n\x10ApiKeyCredential\x12\x0f\n\x07api_key\x18\x01 \x01(\t""\n\x13HarmfulContentEvent\x12\x0b\n\x03uri\x18\x01 \x03(\t"\x14\n\x12ReinstatementEvent"\x19\n\x17DecisionEscalationEventB\xa5\x01\n&com.google.cloud.abuseevent.logging.v1B\x0fAbuseEventProtoP\x01Z@cloud.google.com/go/abuseevent/logging/apiv1/loggingpb;loggingpb\xf8\x01\x01\xaa\x02"Google.Cloud.AbuseEvent.Logging.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.abuseevent.logging.v1.abuse_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.abuseevent.logging.v1B\x0fAbuseEventProtoP\x01Z@cloud.google.com/go/abuseevent/logging/apiv1/loggingpb;loggingpb\xf8\x01\x01\xaa\x02"Google.Cloud.AbuseEvent.Logging.V1'
    _globals['_CRYPTOMININGEVENT'].fields_by_name['vm_ip']._loaded_options = None
    _globals['_CRYPTOMININGEVENT'].fields_by_name['vm_ip']._serialized_options = b'\xe2\x8c\xcf\xd7\x08\x02\x08\x04'
    _globals['_ABUSEEVENT']._serialized_start = 155
    _globals['_ABUSEEVENT']._serialized_end = 1102
    _globals['_ABUSEEVENT_DETECTIONTYPE']._serialized_start = 828
    _globals['_ABUSEEVENT_DETECTIONTYPE']._serialized_end = 959
    _globals['_ABUSEEVENT_ACTIONTYPE']._serialized_start = 961
    _globals['_ABUSEEVENT_ACTIONTYPE']._serialized_end = 1088
    _globals['_CRYPTOMININGEVENT']._serialized_start = 1105
    _globals['_CRYPTOMININGEVENT']._serialized_end = 1296
    _globals['_LEAKEDCREDENTIALEVENT']._serialized_start = 1299
    _globals['_LEAKEDCREDENTIALEVENT']._serialized_end = 1547
    _globals['_SERVICEACCOUNTCREDENTIAL']._serialized_start = 1549
    _globals['_SERVICEACCOUNTCREDENTIAL']._serialized_end = 1616
    _globals['_APIKEYCREDENTIAL']._serialized_start = 1618
    _globals['_APIKEYCREDENTIAL']._serialized_end = 1653
    _globals['_HARMFULCONTENTEVENT']._serialized_start = 1655
    _globals['_HARMFULCONTENTEVENT']._serialized_end = 1689
    _globals['_REINSTATEMENTEVENT']._serialized_start = 1691
    _globals['_REINSTATEMENTEVENT']._serialized_end = 1711
    _globals['_DECISIONESCALATIONEVENT']._serialized_start = 1713
    _globals['_DECISIONESCALATIONEVENT']._serialized_end = 1738