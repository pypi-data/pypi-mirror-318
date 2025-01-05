"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/sessions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.video.stitcher.v1 import companions_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_companions__pb2
from ......google.cloud.video.stitcher.v1 import events_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_events__pb2
from ......google.cloud.video.stitcher.v1 import live_configs_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_live__configs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/video/stitcher/v1/sessions.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/video/stitcher/v1/companions.proto\x1a+google/cloud/video/stitcher/v1/events.proto\x1a1google/cloud/video/stitcher/v1/live_configs.proto\x1a\x1egoogle/protobuf/duration.proto"\xa2\x06\n\nVodSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12I\n\rinterstitials\x18\x02 \x01(\x0b2-.google.cloud.video.stitcher.v1.InterstitialsB\x03\xe0A\x03\x12\x15\n\x08play_uri\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12\x12\n\nad_tag_uri\x18\x06 \x01(\t\x12W\n\x10ad_tag_macro_map\x18\x07 \x03(\x0b2=.google.cloud.video.stitcher.v1.VodSession.AdTagMacroMapEntry\x12I\n\x10manifest_options\x18\t \x01(\x0b2/.google.cloud.video.stitcher.v1.ManifestOptions\x12\x15\n\x08asset_id\x18\n \x01(\tB\x03\xe0A\x03\x12D\n\x0bad_tracking\x18\x0b \x01(\x0e2*.google.cloud.video.stitcher.v1.AdTrackingB\x03\xe0A\x02\x12L\n\x0cgam_settings\x18\r \x01(\x0b26.google.cloud.video.stitcher.v1.VodSession.GamSettings\x12?\n\nvod_config\x18\x0e \x01(\tB+\xfaA(\n&videostitcher.googleapis.com/VodConfig\x1a@\n\x0bGamSettings\x12\x19\n\x0cnetwork_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tstream_id\x18\x02 \x01(\tB\x03\xe0A\x02\x1a4\n\x12AdTagMacroMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:o\xeaAl\n\'videostitcher.googleapis.com/VodSession\x12Aprojects/{project}/locations/{location}/vodSessions/{vod_session}"\xa1\x01\n\rInterstitials\x12D\n\tad_breaks\x18\x01 \x03(\x0b21.google.cloud.video.stitcher.v1.VodSessionAdBreak\x12J\n\x0fsession_content\x18\x02 \x01(\x0b21.google.cloud.video.stitcher.v1.VodSessionContent"\xc0\x01\n\x0cVodSessionAd\x12+\n\x08duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12C\n\rcompanion_ads\x18\x02 \x01(\x0b2,.google.cloud.video.stitcher.v1.CompanionAds\x12>\n\x0factivity_events\x18\x03 \x03(\x0b2%.google.cloud.video.stitcher.v1.Event"@\n\x11VodSessionContent\x12+\n\x08duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\x80\x02\n\x11VodSessionAdBreak\x12F\n\x0fprogress_events\x18\x01 \x03(\x0b2-.google.cloud.video.stitcher.v1.ProgressEvent\x129\n\x03ads\x18\x02 \x03(\x0b2,.google.cloud.video.stitcher.v1.VodSessionAd\x122\n\x0fend_time_offset\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11start_time_offset\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration"\xa9\x06\n\x0bLiveSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08play_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12S\n\rad_tag_macros\x18\x06 \x03(\x0b2<.google.cloud.video.stitcher.v1.LiveSession.AdTagMacrosEntry\x12I\n\x10manifest_options\x18\n \x01(\x0b2/.google.cloud.video.stitcher.v1.ManifestOptions\x12M\n\x0cgam_settings\x18\x0f \x01(\x0b27.google.cloud.video.stitcher.v1.LiveSession.GamSettings\x12D\n\x0blive_config\x18\x10 \x01(\tB/\xe0A\x02\xfaA)\n\'videostitcher.googleapis.com/LiveConfig\x12?\n\x0bad_tracking\x18\x11 \x01(\x0e2*.google.cloud.video.stitcher.v1.AdTracking\x1a\xd1\x01\n\x0bGamSettings\x12\x16\n\tstream_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12n\n\x14targeting_parameters\x18\x04 \x03(\x0b2P.google.cloud.video.stitcher.v1.LiveSession.GamSettings.TargetingParametersEntry\x1a:\n\x18TargetingParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AdTagMacrosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:r\xeaAo\n(videostitcher.googleapis.com/LiveSession\x12Cprojects/{project}/locations/{location}/liveSessions/{live_session}"\xfe\x01\n\x0fManifestOptions\x12K\n\x12include_renditions\x18\x01 \x03(\x0b2/.google.cloud.video.stitcher.v1.RenditionFilter\x12R\n\rbitrate_order\x18\x02 \x01(\x0e2;.google.cloud.video.stitcher.v1.ManifestOptions.OrderPolicy"J\n\x0bOrderPolicy\x12\x1c\n\x18ORDER_POLICY_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"6\n\x0fRenditionFilter\x12\x13\n\x0bbitrate_bps\x18\x01 \x01(\x05\x12\x0e\n\x06codecs\x18\x02 \x01(\tBu\n"com.google.cloud.video.stitcher.v1B\rSessionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.sessions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\rSessionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_VODSESSION_GAMSETTINGS'].fields_by_name['network_code']._loaded_options = None
    _globals['_VODSESSION_GAMSETTINGS'].fields_by_name['network_code']._serialized_options = b'\xe0A\x02'
    _globals['_VODSESSION_GAMSETTINGS'].fields_by_name['stream_id']._loaded_options = None
    _globals['_VODSESSION_GAMSETTINGS'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_VODSESSION_ADTAGMACROMAPENTRY']._loaded_options = None
    _globals['_VODSESSION_ADTAGMACROMAPENTRY']._serialized_options = b'8\x01'
    _globals['_VODSESSION'].fields_by_name['name']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VODSESSION'].fields_by_name['interstitials']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['interstitials']._serialized_options = b'\xe0A\x03'
    _globals['_VODSESSION'].fields_by_name['play_uri']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['play_uri']._serialized_options = b'\xe0A\x03'
    _globals['_VODSESSION'].fields_by_name['asset_id']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['asset_id']._serialized_options = b'\xe0A\x03'
    _globals['_VODSESSION'].fields_by_name['ad_tracking']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['ad_tracking']._serialized_options = b'\xe0A\x02'
    _globals['_VODSESSION'].fields_by_name['vod_config']._loaded_options = None
    _globals['_VODSESSION'].fields_by_name['vod_config']._serialized_options = b'\xfaA(\n&videostitcher.googleapis.com/VodConfig'
    _globals['_VODSESSION']._loaded_options = None
    _globals['_VODSESSION']._serialized_options = b"\xeaAl\n'videostitcher.googleapis.com/VodSession\x12Aprojects/{project}/locations/{location}/vodSessions/{vod_session}"
    _globals['_LIVESESSION_GAMSETTINGS_TARGETINGPARAMETERSENTRY']._loaded_options = None
    _globals['_LIVESESSION_GAMSETTINGS_TARGETINGPARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_LIVESESSION_GAMSETTINGS'].fields_by_name['stream_id']._loaded_options = None
    _globals['_LIVESESSION_GAMSETTINGS'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_LIVESESSION_ADTAGMACROSENTRY']._loaded_options = None
    _globals['_LIVESESSION_ADTAGMACROSENTRY']._serialized_options = b'8\x01'
    _globals['_LIVESESSION'].fields_by_name['name']._loaded_options = None
    _globals['_LIVESESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LIVESESSION'].fields_by_name['play_uri']._loaded_options = None
    _globals['_LIVESESSION'].fields_by_name['play_uri']._serialized_options = b'\xe0A\x03'
    _globals['_LIVESESSION'].fields_by_name['live_config']._loaded_options = None
    _globals['_LIVESESSION'].fields_by_name['live_config']._serialized_options = b"\xe0A\x02\xfaA)\n'videostitcher.googleapis.com/LiveConfig"
    _globals['_LIVESESSION']._loaded_options = None
    _globals['_LIVESESSION']._serialized_options = b'\xeaAo\n(videostitcher.googleapis.com/LiveSession\x12Cprojects/{project}/locations/{location}/liveSessions/{live_session}'
    _globals['_VODSESSION']._serialized_start = 319
    _globals['_VODSESSION']._serialized_end = 1121
    _globals['_VODSESSION_GAMSETTINGS']._serialized_start = 890
    _globals['_VODSESSION_GAMSETTINGS']._serialized_end = 954
    _globals['_VODSESSION_ADTAGMACROMAPENTRY']._serialized_start = 956
    _globals['_VODSESSION_ADTAGMACROMAPENTRY']._serialized_end = 1008
    _globals['_INTERSTITIALS']._serialized_start = 1124
    _globals['_INTERSTITIALS']._serialized_end = 1285
    _globals['_VODSESSIONAD']._serialized_start = 1288
    _globals['_VODSESSIONAD']._serialized_end = 1480
    _globals['_VODSESSIONCONTENT']._serialized_start = 1482
    _globals['_VODSESSIONCONTENT']._serialized_end = 1546
    _globals['_VODSESSIONADBREAK']._serialized_start = 1549
    _globals['_VODSESSIONADBREAK']._serialized_end = 1805
    _globals['_LIVESESSION']._serialized_start = 1808
    _globals['_LIVESESSION']._serialized_end = 2617
    _globals['_LIVESESSION_GAMSETTINGS']._serialized_start = 2240
    _globals['_LIVESESSION_GAMSETTINGS']._serialized_end = 2449
    _globals['_LIVESESSION_GAMSETTINGS_TARGETINGPARAMETERSENTRY']._serialized_start = 2391
    _globals['_LIVESESSION_GAMSETTINGS_TARGETINGPARAMETERSENTRY']._serialized_end = 2449
    _globals['_LIVESESSION_ADTAGMACROSENTRY']._serialized_start = 2451
    _globals['_LIVESESSION_ADTAGMACROSENTRY']._serialized_end = 2501
    _globals['_MANIFESTOPTIONS']._serialized_start = 2620
    _globals['_MANIFESTOPTIONS']._serialized_end = 2874
    _globals['_MANIFESTOPTIONS_ORDERPOLICY']._serialized_start = 2800
    _globals['_MANIFESTOPTIONS_ORDERPOLICY']._serialized_end = 2874
    _globals['_RENDITIONFILTER']._serialized_start = 2876
    _globals['_RENDITIONFILTER']._serialized_end = 2930