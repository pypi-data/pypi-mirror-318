"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/settings/v1beta1/detector.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.securitycenter.settings.v1beta1 import billing_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_settings_dot_v1beta1_dot_billing__settings__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/securitycenter/settings/v1beta1/detector.proto\x12,google.cloud.securitycenter.settings.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1aCgoogle/cloud/securitycenter/settings/v1beta1/billing_settings.proto"\xad\x01\n\x08Detector\x12\x15\n\x08detector\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\tcomponent\x18\x02 \x01(\tB\x03\xe0A\x03\x12T\n\x0cbilling_tier\x18\x03 \x01(\x0e29.google.cloud.securitycenter.settings.v1beta1.BillingTierB\x03\xe0A\x03\x12\x1c\n\x0fdetector_labels\x18\x04 \x03(\tB\x03\xe0A\x03B\xa6\x02\n0com.google.cloud.securitycenter.settings.v1beta1B\x0eDetectorsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.settings.v1beta1.detector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.securitycenter.settings.v1beta1B\x0eDetectorsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1'
    _globals['_DETECTOR'].fields_by_name['detector']._loaded_options = None
    _globals['_DETECTOR'].fields_by_name['detector']._serialized_options = b'\xe0A\x03'
    _globals['_DETECTOR'].fields_by_name['component']._loaded_options = None
    _globals['_DETECTOR'].fields_by_name['component']._serialized_options = b'\xe0A\x03'
    _globals['_DETECTOR'].fields_by_name['billing_tier']._loaded_options = None
    _globals['_DETECTOR'].fields_by_name['billing_tier']._serialized_options = b'\xe0A\x03'
    _globals['_DETECTOR'].fields_by_name['detector_labels']._loaded_options = None
    _globals['_DETECTOR'].fields_by_name['detector_labels']._serialized_options = b'\xe0A\x03'
    _globals['_DETECTOR']._serialized_start = 212
    _globals['_DETECTOR']._serialized_end = 385