"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/entitlement_changes.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import entitlements_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_entitlements__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/channel/v1/entitlement_changes.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/channel/v1/entitlements.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbe\x0c\n\x11EntitlementChange\x12R\n\x11suspension_reason\x18\t \x01(\x0e25.google.cloud.channel.v1.Entitlement.SuspensionReasonH\x00\x12\\\n\x13cancellation_reason\x18\n \x01(\x0e2=.google.cloud.channel.v1.EntitlementChange.CancellationReasonH\x00\x12X\n\x11activation_reason\x18\x0b \x01(\x0e2;.google.cloud.channel.v1.EntitlementChange.ActivationReasonH\x00\x12\x1d\n\x13other_change_reason\x18d \x01(\tH\x00\x12D\n\x0bentitlement\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'cloudchannel.googleapis.com/Entitlement\x128\n\x05offer\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!cloudchannel.googleapis.com/Offer\x12H\n\x13provisioned_service\x18\x03 \x01(\x0b2+.google.cloud.channel.v1.ProvisionedService\x12J\n\x0bchange_type\x18\x04 \x01(\x0e25.google.cloud.channel.v1.EntitlementChange.ChangeType\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n\roperator_type\x18\x06 \x01(\x0e27.google.cloud.channel.v1.EntitlementChange.OperatorType\x126\n\nparameters\x18\x08 \x03(\x0b2".google.cloud.channel.v1.Parameter\x12\x10\n\x08operator\x18\x0c \x01(\t"\xd7\x02\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATED\x10\x01\x12\x17\n\x13PRICE_PLAN_SWITCHED\x10\x03\x12\x16\n\x12COMMITMENT_CHANGED\x10\x04\x12\x0b\n\x07RENEWED\x10\x05\x12\r\n\tSUSPENDED\x10\x06\x12\r\n\tACTIVATED\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x0f\n\x0bSKU_CHANGED\x10\t\x12\x1b\n\x17RENEWAL_SETTING_CHANGED\x10\n\x12\x1d\n\x19PAID_SUBSCRIPTION_STARTED\x10\x0b\x12\x17\n\x13LICENSE_CAP_CHANGED\x10\x0c\x12\x1e\n\x1aSUSPENSION_DETAILS_CHANGED\x10\r\x12\x1b\n\x17TRIAL_END_DATE_EXTENDED\x10\x0e\x12\x11\n\rTRIAL_STARTED\x10\x0f"z\n\x0cOperatorType\x12\x1d\n\x19OPERATOR_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fCUSTOMER_SERVICE_REPRESENTATIVE\x10\x01\x12\n\n\x06SYSTEM\x10\x02\x12\x0c\n\x08CUSTOMER\x10\x03\x12\x0c\n\x08RESELLER\x10\x04"\x7f\n\x12CancellationReason\x12#\n\x1fCANCELLATION_REASON_UNSPECIFIED\x10\x00\x12\x16\n\x12SERVICE_TERMINATED\x10\x01\x12\x16\n\x12RELATIONSHIP_ENDED\x10\x02\x12\x14\n\x10PARTIAL_TRANSFER\x10\x03"\xb4\x01\n\x10ActivationReason\x12!\n\x1dACTIVATION_REASON_UNSPECIFIED\x10\x00\x12\x1f\n\x1bRESELLER_REVOKED_SUSPENSION\x10\x01\x12!\n\x1dCUSTOMER_ACCEPTED_PENDING_TOS\x10\x02\x12\x1c\n\x18RENEWAL_SETTINGS_CHANGED\x10\x03\x12\x1b\n\x17OTHER_ACTIVATION_REASON\x10dB\x0f\n\rchange_reasonBo\n\x1bcom.google.cloud.channel.v1B\x17EntitlementChangesProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.entitlement_changes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x17EntitlementChangesProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_ENTITLEMENTCHANGE'].fields_by_name['entitlement']._loaded_options = None
    _globals['_ENTITLEMENTCHANGE'].fields_by_name['entitlement']._serialized_options = b"\xe0A\x02\xfaA)\n'cloudchannel.googleapis.com/Entitlement"
    _globals['_ENTITLEMENTCHANGE'].fields_by_name['offer']._loaded_options = None
    _globals['_ENTITLEMENTCHANGE'].fields_by_name['offer']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudchannel.googleapis.com/Offer'
    _globals['_ENTITLEMENTCHANGE']._serialized_start = 216
    _globals['_ENTITLEMENTCHANGE']._serialized_end = 1814
    _globals['_ENTITLEMENTCHANGE_CHANGETYPE']._serialized_start = 1018
    _globals['_ENTITLEMENTCHANGE_CHANGETYPE']._serialized_end = 1361
    _globals['_ENTITLEMENTCHANGE_OPERATORTYPE']._serialized_start = 1363
    _globals['_ENTITLEMENTCHANGE_OPERATORTYPE']._serialized_end = 1485
    _globals['_ENTITLEMENTCHANGE_CANCELLATIONREASON']._serialized_start = 1487
    _globals['_ENTITLEMENTCHANGE_CANCELLATIONREASON']._serialized_end = 1614
    _globals['_ENTITLEMENTCHANGE_ACTIVATIONREASON']._serialized_start = 1617
    _globals['_ENTITLEMENTCHANGE_ACTIVATIONREASON']._serialized_end = 1797