"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/fleetengine/delivery/v1/header.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/maps/fleetengine/delivery/v1/header.proto\x12\x1cmaps.fleetengine.delivery.v1\x1a\x1fgoogle/api/field_behavior.proto"\xb0\x04\n\x15DeliveryRequestHeader\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x18\n\x0bregion_code\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bsdk_version\x18\x03 \x01(\t\x12\x12\n\nos_version\x18\x04 \x01(\t\x12\x14\n\x0cdevice_model\x18\x05 \x01(\t\x12M\n\x08sdk_type\x18\x06 \x01(\x0e2;.maps.fleetengine.delivery.v1.DeliveryRequestHeader.SdkType\x12\x18\n\x10maps_sdk_version\x18\x07 \x01(\t\x12\x17\n\x0fnav_sdk_version\x18\x08 \x01(\t\x12N\n\x08platform\x18\t \x01(\x0e2<.maps.fleetengine.delivery.v1.DeliveryRequestHeader.Platform\x12\x14\n\x0cmanufacturer\x18\n \x01(\t\x12\x19\n\x11android_api_level\x18\x0b \x01(\x05\x12\x10\n\x08trace_id\x18\x0c \x01(\t"M\n\x07SdkType\x12\x18\n\x14SDK_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CONSUMER\x10\x01\x12\n\n\x06DRIVER\x10\x02\x12\x0e\n\nJAVASCRIPT\x10\x03"C\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x0b\n\x07ANDROID\x10\x01\x12\x07\n\x03IOS\x10\x02\x12\x07\n\x03WEB\x10\x03B\xfc\x01\n\'com.google.maps.fleetengine.delivery.v1B\x07HeadersP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02\'Google::Maps::FleetEngine::Delivery::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.fleetengine.delivery.v1.header_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.fleetengine.delivery.v1B\x07HeadersP\x01ZIcloud.google.com/go/maps/fleetengine/delivery/apiv1/deliverypb;deliverypb\xa2\x02\x04CFED\xaa\x02#Google.Maps.FleetEngine.Delivery.V1\xca\x02#Google\\Maps\\FleetEngine\\Delivery\\V1\xea\x02'Google::Maps::FleetEngine::Delivery::V1"
    _globals['_DELIVERYREQUESTHEADER'].fields_by_name['region_code']._loaded_options = None
    _globals['_DELIVERYREQUESTHEADER'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_DELIVERYREQUESTHEADER']._serialized_start = 116
    _globals['_DELIVERYREQUESTHEADER']._serialized_end = 676
    _globals['_DELIVERYREQUESTHEADER_SDKTYPE']._serialized_start = 530
    _globals['_DELIVERYREQUESTHEADER_SDKTYPE']._serialized_end = 607
    _globals['_DELIVERYREQUESTHEADER_PLATFORM']._serialized_start = 609
    _globals['_DELIVERYREQUESTHEADER_PLATFORM']._serialized_end = 676