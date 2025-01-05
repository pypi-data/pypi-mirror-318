"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/places/v1/fuel_options.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/maps/places/v1/fuel_options.proto\x12\x15google.maps.places.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xff\x03\n\x0bFuelOptions\x12A\n\x0bfuel_prices\x18\x01 \x03(\x0b2,.google.maps.places.v1.FuelOptions.FuelPrice\x1a\xac\x03\n\tFuelPrice\x12C\n\x04type\x18\x01 \x01(\x0e25.google.maps.places.v1.FuelOptions.FuelPrice.FuelType\x12!\n\x05price\x18\x02 \x01(\x0b2\x12.google.type.Money\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x85\x02\n\x08FuelType\x12\x19\n\x15FUEL_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06DIESEL\x10\x01\x12\x14\n\x10REGULAR_UNLEADED\x10\x02\x12\x0c\n\x08MIDGRADE\x10\x03\x12\x0b\n\x07PREMIUM\x10\x04\x12\x08\n\x04SP91\x10\x05\x12\x0c\n\x08SP91_E10\x10\x06\x12\x08\n\x04SP92\x10\x07\x12\x08\n\x04SP95\x10\x08\x12\x0c\n\x08SP95_E10\x10\t\x12\x08\n\x04SP98\x10\n\x12\x08\n\x04SP99\x10\x0b\x12\t\n\x05SP100\x10\x0c\x12\x07\n\x03LPG\x10\r\x12\x07\n\x03E80\x10\x0e\x12\x07\n\x03E85\x10\x0f\x12\x0b\n\x07METHANE\x10\x10\x12\x0e\n\nBIO_DIESEL\x10\x11\x12\x10\n\x0cTRUCK_DIESEL\x10\x12B\xa1\x01\n\x19com.google.maps.places.v1B\x10FuelOptionsProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.fuel_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x10FuelOptionsProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_FUELOPTIONS']._serialized_start = 126
    _globals['_FUELOPTIONS']._serialized_end = 637
    _globals['_FUELOPTIONS_FUELPRICE']._serialized_start = 209
    _globals['_FUELOPTIONS_FUELPRICE']._serialized_end = 637
    _globals['_FUELOPTIONS_FUELPRICE_FUELTYPE']._serialized_start = 376
    _globals['_FUELOPTIONS_FUELPRICE_FUELTYPE']._serialized_end = 637