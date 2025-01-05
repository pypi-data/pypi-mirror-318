"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/entitlements.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import common_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_common__pb2
from .....google.cloud.channel.v1 import offers_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_offers__pb2
from .....google.cloud.channel.v1 import products_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_products__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/channel/v1/entitlements.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/channel/v1/common.proto\x1a$google/cloud/channel/v1/offers.proto\x1a&google/cloud/channel/v1/products.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfb\x08\n\x0bEntitlement\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x05offer\x18\x08 \x01(\tB)\xe0A\x02\xfaA#\n!cloudchannel.googleapis.com/Offer\x12H\n\x13commitment_settings\x18\x0c \x01(\x0b2+.google.cloud.channel.v1.CommitmentSettings\x12W\n\x12provisioning_state\x18\r \x01(\x0e26.google.cloud.channel.v1.Entitlement.ProvisioningStateB\x03\xe0A\x03\x12M\n\x13provisioned_service\x18\x10 \x01(\x0b2+.google.cloud.channel.v1.ProvisionedServiceB\x03\xe0A\x03\x12V\n\x12suspension_reasons\x18\x12 \x03(\x0e25.google.cloud.channel.v1.Entitlement.SuspensionReasonB\x03\xe0A\x03\x12\x1e\n\x11purchase_order_id\x18\x13 \x01(\tB\x03\xe0A\x01\x12C\n\x0etrial_settings\x18\x15 \x01(\x0b2&.google.cloud.channel.v1.TrialSettingsB\x03\xe0A\x03\x12B\n\x10association_info\x18\x17 \x01(\x0b2(.google.cloud.channel.v1.AssociationInfo\x126\n\nparameters\x18\x1a \x03(\x0b2".google.cloud.channel.v1.Parameter\x12\x1c\n\x0fbilling_account\x18\x1c \x01(\tB\x03\xe0A\x01"R\n\x11ProvisioningState\x12"\n\x1ePROVISIONING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\r\n\tSUSPENDED\x10\x05"\xa3\x01\n\x10SuspensionReason\x12!\n\x1dSUSPENSION_REASON_UNSPECIFIED\x10\x00\x12\x16\n\x12RESELLER_INITIATED\x10\x01\x12\x0f\n\x0bTRIAL_ENDED\x10\x02\x12\x1c\n\x18RENEWAL_WITH_TYPE_CANCEL\x10\x03\x12\x1a\n\x16PENDING_TOS_ACCEPTANCE\x10\x04\x12\t\n\x05OTHER\x10d:p\xeaAm\n\'cloudchannel.googleapis.com/Entitlement\x12Baccounts/{account}/customers/{customer}/entitlements/{entitlement}"_\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b2\x1e.google.cloud.channel.v1.Value\x12\x15\n\x08editable\x18\x03 \x01(\x08B\x03\xe0A\x03"Y\n\x0fAssociationInfo\x12F\n\x10base_entitlement\x18\x01 \x01(\tB,\xfaA)\n\'cloudchannel.googleapis.com/Entitlement"`\n\x12ProvisionedService\x12\x1c\n\x0fprovisioning_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nproduct_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06sku_id\x18\x03 \x01(\tB\x03\xe0A\x03"\xc5\x01\n\x12CommitmentSettings\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x10renewal_settings\x18\x04 \x01(\x0b2(.google.cloud.channel.v1.RenewalSettingsB\x03\xe0A\x01"\xb8\x01\n\x0fRenewalSettings\x12\x16\n\x0eenable_renewal\x18\x01 \x01(\x08\x12\x19\n\x11resize_unit_count\x18\x02 \x01(\x08\x12:\n\x0cpayment_plan\x18\x05 \x01(\x0e2$.google.cloud.channel.v1.PaymentPlan\x126\n\rpayment_cycle\x18\x06 \x01(\x0b2\x1f.google.cloud.channel.v1.Period"L\n\rTrialSettings\x12\r\n\x05trial\x18\x01 \x01(\x08\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xbf\x01\n\x0fTransferableSku\x12J\n\x14transfer_eligibility\x18\t \x01(\x0b2,.google.cloud.channel.v1.TransferEligibility\x12)\n\x03sku\x18\x0b \x01(\x0b2\x1c.google.cloud.channel.v1.Sku\x125\n\nlegacy_sku\x18\x0c \x01(\x0b2\x1c.google.cloud.channel.v1.SkuB\x03\xe0A\x01"\xa6\x02\n\x13TransferEligibility\x12\x13\n\x0bis_eligible\x18\x01 \x01(\x08\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12Q\n\x14ineligibility_reason\x18\x03 \x01(\x0e23.google.cloud.channel.v1.TransferEligibility.Reason"\x91\x01\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x1a\n\x16PENDING_TOS_ACCEPTANCE\x10\x01\x12\x14\n\x10SKU_NOT_ELIGIBLE\x10\x02\x12\x11\n\rSKU_SUSPENDED\x10\x03\x12*\n&CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU\x10\x04Bi\n\x1bcom.google.cloud.channel.v1B\x11EntitlementsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.entitlements_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x11EntitlementsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_ENTITLEMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['offer']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['offer']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudchannel.googleapis.com/Offer'
    _globals['_ENTITLEMENT'].fields_by_name['provisioning_state']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['provisioning_state']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['provisioned_service']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['provisioned_service']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['suspension_reasons']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['suspension_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['purchase_order_id']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['purchase_order_id']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITLEMENT'].fields_by_name['trial_settings']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['trial_settings']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['billing_account']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['billing_account']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITLEMENT']._loaded_options = None
    _globals['_ENTITLEMENT']._serialized_options = b"\xeaAm\n'cloudchannel.googleapis.com/Entitlement\x12Baccounts/{account}/customers/{customer}/entitlements/{entitlement}"
    _globals['_PARAMETER'].fields_by_name['editable']._loaded_options = None
    _globals['_PARAMETER'].fields_by_name['editable']._serialized_options = b'\xe0A\x03'
    _globals['_ASSOCIATIONINFO'].fields_by_name['base_entitlement']._loaded_options = None
    _globals['_ASSOCIATIONINFO'].fields_by_name['base_entitlement']._serialized_options = b"\xfaA)\n'cloudchannel.googleapis.com/Entitlement"
    _globals['_PROVISIONEDSERVICE'].fields_by_name['provisioning_id']._loaded_options = None
    _globals['_PROVISIONEDSERVICE'].fields_by_name['provisioning_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONEDSERVICE'].fields_by_name['product_id']._loaded_options = None
    _globals['_PROVISIONEDSERVICE'].fields_by_name['product_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONEDSERVICE'].fields_by_name['sku_id']._loaded_options = None
    _globals['_PROVISIONEDSERVICE'].fields_by_name['sku_id']._serialized_options = b'\xe0A\x03'
    _globals['_COMMITMENTSETTINGS'].fields_by_name['start_time']._loaded_options = None
    _globals['_COMMITMENTSETTINGS'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMMITMENTSETTINGS'].fields_by_name['end_time']._loaded_options = None
    _globals['_COMMITMENTSETTINGS'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMMITMENTSETTINGS'].fields_by_name['renewal_settings']._loaded_options = None
    _globals['_COMMITMENTSETTINGS'].fields_by_name['renewal_settings']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSFERABLESKU'].fields_by_name['legacy_sku']._loaded_options = None
    _globals['_TRANSFERABLESKU'].fields_by_name['legacy_sku']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITLEMENT']._serialized_start = 281
    _globals['_ENTITLEMENT']._serialized_end = 1428
    _globals['_ENTITLEMENT_PROVISIONINGSTATE']._serialized_start = 1066
    _globals['_ENTITLEMENT_PROVISIONINGSTATE']._serialized_end = 1148
    _globals['_ENTITLEMENT_SUSPENSIONREASON']._serialized_start = 1151
    _globals['_ENTITLEMENT_SUSPENSIONREASON']._serialized_end = 1314
    _globals['_PARAMETER']._serialized_start = 1430
    _globals['_PARAMETER']._serialized_end = 1525
    _globals['_ASSOCIATIONINFO']._serialized_start = 1527
    _globals['_ASSOCIATIONINFO']._serialized_end = 1616
    _globals['_PROVISIONEDSERVICE']._serialized_start = 1618
    _globals['_PROVISIONEDSERVICE']._serialized_end = 1714
    _globals['_COMMITMENTSETTINGS']._serialized_start = 1717
    _globals['_COMMITMENTSETTINGS']._serialized_end = 1914
    _globals['_RENEWALSETTINGS']._serialized_start = 1917
    _globals['_RENEWALSETTINGS']._serialized_end = 2101
    _globals['_TRIALSETTINGS']._serialized_start = 2103
    _globals['_TRIALSETTINGS']._serialized_end = 2179
    _globals['_TRANSFERABLESKU']._serialized_start = 2182
    _globals['_TRANSFERABLESKU']._serialized_end = 2373
    _globals['_TRANSFERELIGIBILITY']._serialized_start = 2376
    _globals['_TRANSFERELIGIBILITY']._serialized_end = 2670
    _globals['_TRANSFERELIGIBILITY_REASON']._serialized_start = 2525
    _globals['_TRANSFERELIGIBILITY_REASON']._serialized_end = 2670