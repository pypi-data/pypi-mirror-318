"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/settings/v1beta1/billing_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/securitycenter/settings/v1beta1/billing_settings.proto\x12,google.cloud.securitycenter.settings.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x02\n\x0fBillingSettings\x12T\n\x0cbilling_tier\x18\x01 \x01(\x0e29.google.cloud.securitycenter.settings.v1beta1.BillingTierB\x03\xe0A\x03\x12T\n\x0cbilling_type\x18\x02 \x01(\x0e29.google.cloud.securitycenter.settings.v1beta1.BillingTypeB\x03\xe0A\x03\x123\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03*F\n\x0bBillingTier\x12\x1c\n\x18BILLING_TIER_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x0b\n\x07PREMIUM\x10\x02*`\n\x0bBillingType\x12\x1c\n\x18BILLING_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cSUBSCRIPTION\x10\x01\x12\x16\n\x12TRIAL_SUBSCRIPTION\x10\x02\x12\t\n\x05ALPHA\x10\x03B\xac\x02\n0com.google.cloud.securitycenter.settings.v1beta1B\x14BillingSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.settings.v1beta1.billing_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.securitycenter.settings.v1beta1B\x14BillingSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1'
    _globals['_BILLINGSETTINGS'].fields_by_name['billing_tier']._loaded_options = None
    _globals['_BILLINGSETTINGS'].fields_by_name['billing_tier']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGSETTINGS'].fields_by_name['billing_type']._loaded_options = None
    _globals['_BILLINGSETTINGS'].fields_by_name['billing_type']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGSETTINGS'].fields_by_name['start_time']._loaded_options = None
    _globals['_BILLINGSETTINGS'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGSETTINGS'].fields_by_name['expire_time']._loaded_options = None
    _globals['_BILLINGSETTINGS'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGTIER']._serialized_start = 482
    _globals['_BILLINGTIER']._serialized_end = 552
    _globals['_BILLINGTYPE']._serialized_start = 554
    _globals['_BILLINGTYPE']._serialized_end = 650
    _globals['_BILLINGSETTINGS']._serialized_start = 184
    _globals['_BILLINGSETTINGS']._serialized_end = 480