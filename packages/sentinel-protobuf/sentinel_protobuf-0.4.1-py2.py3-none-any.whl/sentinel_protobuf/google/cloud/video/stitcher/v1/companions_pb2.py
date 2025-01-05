"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/companions.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.video.stitcher.v1 import events_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_events__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/video/stitcher/v1/companions.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a+google/cloud/video/stitcher/v1/events.proto"\x82\x02\n\x0cCompanionAds\x12\\\n\x13display_requirement\x18\x01 \x01(\x0e2?.google.cloud.video.stitcher.v1.CompanionAds.DisplayRequirement\x12=\n\ncompanions\x18\x02 \x03(\x0b2).google.cloud.video.stitcher.v1.Companion"U\n\x12DisplayRequirement\x12#\n\x1fDISPLAY_REQUIREMENT_UNSPECIFIED\x10\x00\x12\x07\n\x03ALL\x10\x01\x12\x07\n\x03ANY\x10\x02\x12\x08\n\x04NONE\x10\x03"\xf5\x03\n\tCompanion\x12N\n\x12iframe_ad_resource\x18\n \x01(\x0b20.google.cloud.video.stitcher.v1.IframeAdResourceH\x00\x12N\n\x12static_ad_resource\x18\x0b \x01(\x0b20.google.cloud.video.stitcher.v1.StaticAdResourceH\x00\x12J\n\x10html_ad_resource\x18\x0c \x01(\x0b2..google.cloud.video.stitcher.v1.HtmlAdResourceH\x00\x12\x15\n\rapi_framework\x18\x01 \x01(\t\x12\x11\n\theight_px\x18\x02 \x01(\x05\x12\x10\n\x08width_px\x18\x03 \x01(\x05\x12\x17\n\x0fasset_height_px\x18\x04 \x01(\x05\x12\x1a\n\x12expanded_height_px\x18\x05 \x01(\x05\x12\x16\n\x0easset_width_px\x18\x06 \x01(\x05\x12\x19\n\x11expanded_width_px\x18\x07 \x01(\x05\x12\x12\n\nad_slot_id\x18\x08 \x01(\t\x125\n\x06events\x18\t \x03(\x0b2%.google.cloud.video.stitcher.v1.EventB\r\n\x0bad_resource"%\n\x0eHtmlAdResource\x12\x13\n\x0bhtml_source\x18\x01 \x01(\t"\x1f\n\x10IframeAdResource\x12\x0b\n\x03uri\x18\x01 \x01(\t"6\n\x10StaticAdResource\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x15\n\rcreative_type\x18\x02 \x01(\tBw\n"com.google.cloud.video.stitcher.v1B\x0fCompanionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.companions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x0fCompanionsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_COMPANIONADS']._serialized_start = 129
    _globals['_COMPANIONADS']._serialized_end = 387
    _globals['_COMPANIONADS_DISPLAYREQUIREMENT']._serialized_start = 302
    _globals['_COMPANIONADS_DISPLAYREQUIREMENT']._serialized_end = 387
    _globals['_COMPANION']._serialized_start = 390
    _globals['_COMPANION']._serialized_end = 891
    _globals['_HTMLADRESOURCE']._serialized_start = 893
    _globals['_HTMLADRESOURCE']._serialized_end = 930
    _globals['_IFRAMEADRESOURCE']._serialized_start = 932
    _globals['_IFRAMEADRESOURCE']._serialized_end = 963
    _globals['_STATICADRESOURCE']._serialized_start = 965
    _globals['_STATICADRESOURCE']._serialized_end = 1019