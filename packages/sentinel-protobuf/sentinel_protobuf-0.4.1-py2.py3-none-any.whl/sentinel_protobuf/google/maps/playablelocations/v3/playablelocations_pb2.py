"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/playablelocations/v3/playablelocations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.playablelocations.v3 import resources_pb2 as google_dot_maps_dot_playablelocations_dot_v3_dot_resources__pb2
from .....google.maps.playablelocations.v3.sample import resources_pb2 as google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2
from .....google.maps.unity import clientinfo_pb2 as google_dot_maps_dot_unity_dot_clientinfo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/maps/playablelocations/v3/playablelocations.proto\x12 google.maps.playablelocations.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a0google/maps/playablelocations/v3/resources.proto\x1a7google/maps/playablelocations/v3/sample/resources.proto\x1a"google/maps/unity/clientinfo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/api/client.proto"\xba\x01\n\x1eSamplePlayableLocationsRequest\x12M\n\x0barea_filter\x18\x01 \x01(\x0b23.google.maps.playablelocations.v3.sample.AreaFilterB\x03\xe0A\x02\x12I\n\x08criteria\x18\x02 \x03(\x0b22.google.maps.playablelocations.v3.sample.CriterionB\x03\xe0A\x02"\xd8\x02\n\x1fSamplePlayableLocationsResponse\x12\x89\x01\n\x1elocations_per_game_object_type\x18\x01 \x03(\x0b2a.google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry\x12&\n\x03ttl\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x1a\x80\x01\n\x1fLocationsPerGameObjectTypeEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12L\n\x05value\x18\x02 \x01(\x0b2=.google.maps.playablelocations.v3.sample.PlayableLocationList:\x028\x01"\xb8\x01\n\x17LogPlayerReportsRequest\x12K\n\x0eplayer_reports\x18\x01 \x03(\x0b2..google.maps.playablelocations.v3.PlayerReportB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x0bclient_info\x18\x03 \x01(\x0b2\x1d.google.maps.unity.ClientInfoB\x03\xe0A\x02"\x1a\n\x18LogPlayerReportsResponse"\xb1\x01\n\x15LogImpressionsRequest\x12F\n\x0bimpressions\x18\x01 \x03(\x0b2,.google.maps.playablelocations.v3.ImpressionB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x0bclient_info\x18\x03 \x01(\x0b2\x1d.google.maps.unity.ClientInfoB\x03\xe0A\x02"\x18\n\x16LogImpressionsResponse2\xd3\x04\n\x11PlayableLocations\x12\xc6\x01\n\x17SamplePlayableLocations\x12@.google.maps.playablelocations.v3.SamplePlayableLocationsRequest\x1aA.google.maps.playablelocations.v3.SamplePlayableLocationsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/v3:samplePlayableLocations:\x01*\x12\xaa\x01\n\x10LogPlayerReports\x129.google.maps.playablelocations.v3.LogPlayerReportsRequest\x1a:.google.maps.playablelocations.v3.LogPlayerReportsResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/v3:logPlayerReports:\x01*\x12\xa2\x01\n\x0eLogImpressions\x127.google.maps.playablelocations.v3.LogImpressionsRequest\x1a8.google.maps.playablelocations.v3.LogImpressionsResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/v3:logImpressions:\x01*\x1a#\xcaA playablelocations.googleapis.comB\xe7\x01\n$com.google.maps.playablelocations.v3B\x16PlayableLocationsProtoP\x01ZXcloud.google.com/go/maps/playablelocations/apiv3/playablelocationspb;playablelocationspb\xa2\x02\x04GMPL\xaa\x02 Google.Maps.PlayableLocations.V3\xca\x02 Google\\Maps\\PlayableLocations\\V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.playablelocations.v3.playablelocations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.playablelocations.v3B\x16PlayableLocationsProtoP\x01ZXcloud.google.com/go/maps/playablelocations/apiv3/playablelocationspb;playablelocationspb\xa2\x02\x04GMPL\xaa\x02 Google.Maps.PlayableLocations.V3\xca\x02 Google\\Maps\\PlayableLocations\\V3'
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST'].fields_by_name['area_filter']._loaded_options = None
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST'].fields_by_name['area_filter']._serialized_options = b'\xe0A\x02'
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST'].fields_by_name['criteria']._loaded_options = None
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST'].fields_by_name['criteria']._serialized_options = b'\xe0A\x02'
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY']._loaded_options = None
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY']._serialized_options = b'8\x01'
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['player_reports']._loaded_options = None
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['player_reports']._serialized_options = b'\xe0A\x02'
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x02'
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['client_info']._loaded_options = None
    _globals['_LOGPLAYERREPORTSREQUEST'].fields_by_name['client_info']._serialized_options = b'\xe0A\x02'
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['impressions']._loaded_options = None
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['impressions']._serialized_options = b'\xe0A\x02'
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x02'
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['client_info']._loaded_options = None
    _globals['_LOGIMPRESSIONSREQUEST'].fields_by_name['client_info']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYABLELOCATIONS']._loaded_options = None
    _globals['_PLAYABLELOCATIONS']._serialized_options = b'\xcaA playablelocations.googleapis.com'
    _globals['_PLAYABLELOCATIONS'].methods_by_name['SamplePlayableLocations']._loaded_options = None
    _globals['_PLAYABLELOCATIONS'].methods_by_name['SamplePlayableLocations']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/v3:samplePlayableLocations:\x01*'
    _globals['_PLAYABLELOCATIONS'].methods_by_name['LogPlayerReports']._loaded_options = None
    _globals['_PLAYABLELOCATIONS'].methods_by_name['LogPlayerReports']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/v3:logPlayerReports:\x01*'
    _globals['_PLAYABLELOCATIONS'].methods_by_name['LogImpressions']._loaded_options = None
    _globals['_PLAYABLELOCATIONS'].methods_by_name['LogImpressions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/v3:logImpressions:\x01*'
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST']._serialized_start = 358
    _globals['_SAMPLEPLAYABLELOCATIONSREQUEST']._serialized_end = 544
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE']._serialized_start = 547
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE']._serialized_end = 891
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY']._serialized_start = 763
    _globals['_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY']._serialized_end = 891
    _globals['_LOGPLAYERREPORTSREQUEST']._serialized_start = 894
    _globals['_LOGPLAYERREPORTSREQUEST']._serialized_end = 1078
    _globals['_LOGPLAYERREPORTSRESPONSE']._serialized_start = 1080
    _globals['_LOGPLAYERREPORTSRESPONSE']._serialized_end = 1106
    _globals['_LOGIMPRESSIONSREQUEST']._serialized_start = 1109
    _globals['_LOGIMPRESSIONSREQUEST']._serialized_end = 1286
    _globals['_LOGIMPRESSIONSRESPONSE']._serialized_start = 1288
    _globals['_LOGIMPRESSIONSRESPONSE']._serialized_end = 1312
    _globals['_PLAYABLELOCATIONS']._serialized_start = 1315
    _globals['_PLAYABLELOCATIONS']._serialized_end = 1910