"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/playablelocations/v3/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/maps/playablelocations/v3/resources.proto\x12 google.maps.playablelocations.v3\x1a\x1fgoogle/api/field_behavior.proto"\xe9\x02\n\x0cPlayerReport\x12\x1a\n\rlocation_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\x07reasons\x18\x02 \x03(\x0e2@.google.maps.playablelocations.v3.PlayerReport.BadLocationReasonB\x03\xe0A\x02\x12\x1b\n\x0ereason_details\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x04 \x01(\t"\xb0\x01\n\x11BadLocationReason\x12#\n\x1fBAD_LOCATION_REASON_UNSPECIFIED\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\x1d\n\x19NOT_PEDESTRIAN_ACCESSIBLE\x10\x02\x12\x16\n\x12NOT_OPEN_TO_PUBLIC\x10\x04\x12\x16\n\x12PERMANENTLY_CLOSED\x10\x05\x12\x1c\n\x18TEMPORARILY_INACCESSIBLE\x10\x06"\xef\x01\n\nImpression\x12\x1a\n\rlocation_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\x0fimpression_type\x18\x02 \x01(\x0e2;.google.maps.playablelocations.v3.Impression.ImpressionTypeB\x03\xe0A\x02\x12\x18\n\x10game_object_type\x18\x04 \x01(\x05"P\n\x0eImpressionType\x12\x1f\n\x1bIMPRESSION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tPRESENTED\x10\x01\x12\x0e\n\nINTERACTED\x10\x02B\xdf\x01\n$com.google.maps.playablelocations.v3B\x0eResourcesProtoP\x01ZXcloud.google.com/go/maps/playablelocations/apiv3/playablelocationspb;playablelocationspb\xa2\x02\x04GMPL\xaa\x02 Google.Maps.PlayableLocations.V3\xca\x02 Google\\Maps\\PlayableLocations\\V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.playablelocations.v3.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.playablelocations.v3B\x0eResourcesProtoP\x01ZXcloud.google.com/go/maps/playablelocations/apiv3/playablelocationspb;playablelocationspb\xa2\x02\x04GMPL\xaa\x02 Google.Maps.PlayableLocations.V3\xca\x02 Google\\Maps\\PlayableLocations\\V3'
    _globals['_PLAYERREPORT'].fields_by_name['location_name']._loaded_options = None
    _globals['_PLAYERREPORT'].fields_by_name['location_name']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYERREPORT'].fields_by_name['reasons']._loaded_options = None
    _globals['_PLAYERREPORT'].fields_by_name['reasons']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYERREPORT'].fields_by_name['reason_details']._loaded_options = None
    _globals['_PLAYERREPORT'].fields_by_name['reason_details']._serialized_options = b'\xe0A\x02'
    _globals['_IMPRESSION'].fields_by_name['location_name']._loaded_options = None
    _globals['_IMPRESSION'].fields_by_name['location_name']._serialized_options = b'\xe0A\x02'
    _globals['_IMPRESSION'].fields_by_name['impression_type']._loaded_options = None
    _globals['_IMPRESSION'].fields_by_name['impression_type']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYERREPORT']._serialized_start = 120
    _globals['_PLAYERREPORT']._serialized_end = 481
    _globals['_PLAYERREPORT_BADLOCATIONREASON']._serialized_start = 305
    _globals['_PLAYERREPORT_BADLOCATIONREASON']._serialized_end = 481
    _globals['_IMPRESSION']._serialized_start = 484
    _globals['_IMPRESSION']._serialized_end = 723
    _globals['_IMPRESSION_IMPRESSIONTYPE']._serialized_start = 643
    _globals['_IMPRESSION_IMPRESSIONTYPE']._serialized_end = 723