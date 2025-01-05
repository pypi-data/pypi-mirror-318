"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/playablelocations/v3/sample/resources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/maps/playablelocations/v3/sample/resources.proto\x12\'google.maps.playablelocations.v3.sample\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a\x18google/type/latlng.proto"\xbe\x01\n\x10PlayableLocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x08place_id\x18\x02 \x01(\tH\x00\x12\x13\n\tplus_code\x18\x03 \x01(\tH\x00\x12\r\n\x05types\x18\x04 \x03(\t\x12)\n\x0ccenter_point\x18\x05 \x01(\x0b2\x13.google.type.LatLng\x12*\n\rsnapped_point\x18\x06 \x01(\x0b2\x13.google.type.LatLngB\r\n\x0blocation_id"\xd6\x01\n\x0eSpacingOptions\x12\x1f\n\x12min_spacing_meters\x18\x01 \x01(\x01B\x03\xe0A\x02\x12U\n\npoint_type\x18\x02 \x01(\x0e2A.google.maps.playablelocations.v3.sample.SpacingOptions.PointType"L\n\tPointType\x12\x1a\n\x16POINT_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cCENTER_POINT\x10\x01\x12\x11\n\rSNAPPED_POINT\x10\x02"\x86\x01\n\x06Filter\x12\x1a\n\x12max_location_count\x18\x01 \x01(\x05\x12H\n\x07spacing\x18\x02 \x01(\x0b27.google.maps.playablelocations.v3.sample.SpacingOptions\x12\x16\n\x0eincluded_types\x18\x03 \x03(\t"\xa1\x01\n\tCriterion\x12\x1d\n\x10game_object_type\x18\x01 \x01(\x05B\x03\xe0A\x02\x12?\n\x06filter\x18\x02 \x01(\x0b2/.google.maps.playablelocations.v3.sample.Filter\x124\n\x10fields_to_return\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"%\n\nAreaFilter\x12\x17\n\ns2_cell_id\x18\x01 \x01(\x06B\x03\xe0A\x02"d\n\x14PlayableLocationList\x12L\n\tlocations\x18\x01 \x03(\x0b29.google.maps.playablelocations.v3.sample.PlayableLocationB\xbb\x01\n+com.google.maps.playablelocations.v3.sampleB\x0eResourcesProtoP\x01ZIcloud.google.com/go/maps/playablelocations/apiv3/sample/samplepb;samplepb\xa2\x02\x04GMPL\xaa\x02\'Google.Maps.PlayableLocations.V3.Sampleb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.playablelocations.v3.sample.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.maps.playablelocations.v3.sampleB\x0eResourcesProtoP\x01ZIcloud.google.com/go/maps/playablelocations/apiv3/sample/samplepb;samplepb\xa2\x02\x04GMPL\xaa\x02'Google.Maps.PlayableLocations.V3.Sample"
    _globals['_SPACINGOPTIONS'].fields_by_name['min_spacing_meters']._loaded_options = None
    _globals['_SPACINGOPTIONS'].fields_by_name['min_spacing_meters']._serialized_options = b'\xe0A\x02'
    _globals['_CRITERION'].fields_by_name['game_object_type']._loaded_options = None
    _globals['_CRITERION'].fields_by_name['game_object_type']._serialized_options = b'\xe0A\x02'
    _globals['_AREAFILTER'].fields_by_name['s2_cell_id']._loaded_options = None
    _globals['_AREAFILTER'].fields_by_name['s2_cell_id']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYABLELOCATION']._serialized_start = 194
    _globals['_PLAYABLELOCATION']._serialized_end = 384
    _globals['_SPACINGOPTIONS']._serialized_start = 387
    _globals['_SPACINGOPTIONS']._serialized_end = 601
    _globals['_SPACINGOPTIONS_POINTTYPE']._serialized_start = 525
    _globals['_SPACINGOPTIONS_POINTTYPE']._serialized_end = 601
    _globals['_FILTER']._serialized_start = 604
    _globals['_FILTER']._serialized_end = 738
    _globals['_CRITERION']._serialized_start = 741
    _globals['_CRITERION']._serialized_end = 902
    _globals['_AREAFILTER']._serialized_start = 904
    _globals['_AREAFILTER']._serialized_end = 941
    _globals['_PLAYABLELOCATIONLIST']._serialized_start = 943
    _globals['_PLAYABLELOCATIONLIST']._serialized_end = 1043