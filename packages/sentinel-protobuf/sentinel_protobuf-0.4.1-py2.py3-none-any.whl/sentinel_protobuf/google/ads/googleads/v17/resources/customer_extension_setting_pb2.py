"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/customer_extension_setting.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_extension__setting__device__pb2
from ......google.ads.googleads.v17.enums import extension_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_extension__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v17/resources/customer_extension_setting.proto\x12"google.ads.googleads.v17.resources\x1a=google/ads/googleads/v17/enums/extension_setting_device.proto\x1a3google/ads/googleads/v17/enums/extension_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf8\x03\n\x18CustomerExtensionSetting\x12P\n\rresource_name\x18\x01 \x01(\tB9\xe0A\x05\xfaA3\n1googleads.googleapis.com/CustomerExtensionSetting\x12\\\n\x0eextension_type\x18\x02 \x01(\x0e2?.google.ads.googleads.v17.enums.ExtensionTypeEnum.ExtensionTypeB\x03\xe0A\x05\x12M\n\x14extension_feed_items\x18\x05 \x03(\tB/\xfaA,\n*googleads.googleapis.com/ExtensionFeedItem\x12a\n\x06device\x18\x04 \x01(\x0e2Q.google.ads.googleads.v17.enums.ExtensionSettingDeviceEnum.ExtensionSettingDevice:z\xeaAw\n1googleads.googleapis.com/CustomerExtensionSetting\x12Bcustomers/{customer_id}/customerExtensionSettings/{extension_type}B\x8f\x02\n&com.google.ads.googleads.v17.resourcesB\x1dCustomerExtensionSettingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.customer_extension_setting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x1dCustomerExtensionSettingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA3\n1googleads.googleapis.com/CustomerExtensionSetting'
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['extension_type']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['extension_type']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['extension_feed_items']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTING'].fields_by_name['extension_feed_items']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/ExtensionFeedItem'
    _globals['_CUSTOMEREXTENSIONSETTING']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTING']._serialized_options = b'\xeaAw\n1googleads.googleapis.com/CustomerExtensionSetting\x12Bcustomers/{customer_id}/customerExtensionSettings/{extension_type}'
    _globals['_CUSTOMEREXTENSIONSETTING']._serialized_start = 284
    _globals['_CUSTOMEREXTENSIONSETTING']._serialized_end = 788