"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/videointelligence/v1p2beta1/video_intelligence.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/videointelligence/v1p2beta1/video_intelligence.proto\x12(google.cloud.videointelligence.v1p2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x8c\x02\n\x14AnnotateVideoRequest\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x15\n\rinput_content\x18\x06 \x01(\x0c\x12H\n\x08features\x18\x02 \x03(\x0e21.google.cloud.videointelligence.v1p2beta1.FeatureB\x03\xe0A\x02\x12M\n\rvideo_context\x18\x03 \x01(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoContext\x12\x17\n\noutput_uri\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0blocation_id\x18\x05 \x01(\tB\x03\xe0A\x01"\xf6\x03\n\x0cVideoContext\x12H\n\x08segments\x18\x01 \x03(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoSegment\x12^\n\x16label_detection_config\x18\x02 \x01(\x0b2>.google.cloud.videointelligence.v1p2beta1.LabelDetectionConfig\x12i\n\x1cshot_change_detection_config\x18\x03 \x01(\x0b2C.google.cloud.videointelligence.v1p2beta1.ShotChangeDetectionConfig\x12s\n!explicit_content_detection_config\x18\x04 \x01(\x0b2H.google.cloud.videointelligence.v1p2beta1.ExplicitContentDetectionConfig\x12\\\n\x15text_detection_config\x18\x08 \x01(\x0b2=.google.cloud.videointelligence.v1p2beta1.TextDetectionConfig"\x9c\x01\n\x14LabelDetectionConfig\x12Z\n\x14label_detection_mode\x18\x01 \x01(\x0e2<.google.cloud.videointelligence.v1p2beta1.LabelDetectionMode\x12\x19\n\x11stationary_camera\x18\x02 \x01(\x08\x12\r\n\x05model\x18\x03 \x01(\t"*\n\x19ShotChangeDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"/\n\x1eExplicitContentDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"-\n\x13TextDetectionConfig\x12\x16\n\x0elanguage_hints\x18\x01 \x03(\t"x\n\x0cVideoSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"k\n\x0cLabelSegment\x12G\n\x07segment\x18\x01 \x01(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02"P\n\nLabelFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x02 \x01(\x02"G\n\x06Entity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xb0\x02\n\x0fLabelAnnotation\x12@\n\x06entity\x18\x01 \x01(\x0b20.google.cloud.videointelligence.v1p2beta1.Entity\x12K\n\x11category_entities\x18\x02 \x03(\x0b20.google.cloud.videointelligence.v1p2beta1.Entity\x12H\n\x08segments\x18\x03 \x03(\x0b26.google.cloud.videointelligence.v1p2beta1.LabelSegment\x12D\n\x06frames\x18\x04 \x03(\x0b24.google.cloud.videointelligence.v1p2beta1.LabelFrame"\x9c\x01\n\x14ExplicitContentFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12T\n\x16pornography_likelihood\x18\x02 \x01(\x0e24.google.cloud.videointelligence.v1p2beta1.Likelihood"k\n\x19ExplicitContentAnnotation\x12N\n\x06frames\x18\x01 \x03(\x0b2>.google.cloud.videointelligence.v1p2beta1.ExplicitContentFrame"Q\n\x15NormalizedBoundingBox\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\x0b\n\x03top\x18\x02 \x01(\x02\x12\r\n\x05right\x18\x03 \x01(\x02\x12\x0e\n\x06bottom\x18\x04 \x01(\x02"\xcb\x05\n\x16VideoAnnotationResults\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\\\n\x19segment_label_annotations\x18\x02 \x03(\x0b29.google.cloud.videointelligence.v1p2beta1.LabelAnnotation\x12Y\n\x16shot_label_annotations\x18\x03 \x03(\x0b29.google.cloud.videointelligence.v1p2beta1.LabelAnnotation\x12Z\n\x17frame_label_annotations\x18\x04 \x03(\x0b29.google.cloud.videointelligence.v1p2beta1.LabelAnnotation\x12P\n\x10shot_annotations\x18\x06 \x03(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoSegment\x12`\n\x13explicit_annotation\x18\x07 \x01(\x0b2C.google.cloud.videointelligence.v1p2beta1.ExplicitContentAnnotation\x12R\n\x10text_annotations\x18\x0c \x03(\x0b28.google.cloud.videointelligence.v1p2beta1.TextAnnotation\x12^\n\x12object_annotations\x18\x0e \x03(\x0b2B.google.cloud.videointelligence.v1p2beta1.ObjectTrackingAnnotation\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status"u\n\x15AnnotateVideoResponse\x12\\\n\x12annotation_results\x18\x01 \x03(\x0b2@.google.cloud.videointelligence.v1p2beta1.VideoAnnotationResults"\xa7\x01\n\x17VideoAnnotationProgress\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x18\n\x10progress_percent\x18\x02 \x01(\x05\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"w\n\x15AnnotateVideoProgress\x12^\n\x13annotation_progress\x18\x01 \x03(\x0b2A.google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"f\n\x16NormalizedBoundingPoly\x12L\n\x08vertices\x18\x01 \x03(\x0b2:.google.cloud.videointelligence.v1p2beta1.NormalizedVertex"\xaf\x01\n\x0bTextSegment\x12G\n\x07segment\x18\x01 \x01(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12C\n\x06frames\x18\x03 \x03(\x0b23.google.cloud.videointelligence.v1p2beta1.TextFrame"\x9b\x01\n\tTextFrame\x12^\n\x14rotated_bounding_box\x18\x01 \x01(\x0b2@.google.cloud.videointelligence.v1p2beta1.NormalizedBoundingPoly\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"g\n\x0eTextAnnotation\x12\x0c\n\x04text\x18\x01 \x01(\t\x12G\n\x08segments\x18\x02 \x03(\x0b25.google.cloud.videointelligence.v1p2beta1.TextSegment"\xa7\x01\n\x13ObjectTrackingFrame\x12`\n\x17normalized_bounding_box\x18\x01 \x01(\x0b2?.google.cloud.videointelligence.v1p2beta1.NormalizedBoundingBox\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xac\x02\n\x18ObjectTrackingAnnotation\x12I\n\x07segment\x18\x03 \x01(\x0b26.google.cloud.videointelligence.v1p2beta1.VideoSegmentH\x00\x12\x12\n\x08track_id\x18\x05 \x01(\x03H\x00\x12@\n\x06entity\x18\x01 \x01(\x0b20.google.cloud.videointelligence.v1p2beta1.Entity\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12M\n\x06frames\x18\x02 \x03(\x0b2=.google.cloud.videointelligence.v1p2beta1.ObjectTrackingFrameB\x0c\n\ntrack_info*\x9b\x01\n\x07Feature\x12\x17\n\x13FEATURE_UNSPECIFIED\x10\x00\x12\x13\n\x0fLABEL_DETECTION\x10\x01\x12\x19\n\x15SHOT_CHANGE_DETECTION\x10\x02\x12\x1e\n\x1aEXPLICIT_CONTENT_DETECTION\x10\x03\x12\x12\n\x0eTEXT_DETECTION\x10\x07\x12\x13\n\x0fOBJECT_TRACKING\x10\t*r\n\x12LabelDetectionMode\x12$\n LABEL_DETECTION_MODE_UNSPECIFIED\x10\x00\x12\r\n\tSHOT_MODE\x10\x01\x12\x0e\n\nFRAME_MODE\x10\x02\x12\x17\n\x13SHOT_AND_FRAME_MODE\x10\x03*t\n\nLikelihood\x12\x1a\n\x16LIKELIHOOD_UNSPECIFIED\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xce\x02\n\x18VideoIntelligenceService\x12\xdb\x01\n\rAnnotateVideo\x12>.google.cloud.videointelligence.v1p2beta1.AnnotateVideoRequest\x1a\x1d.google.longrunning.Operation"k\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p2beta1/videos:annotate:\x01*\x1aT\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xaf\x02\n,com.google.cloud.videointelligence.v1p2beta1B\x1dVideoIntelligenceServiceProtoP\x01ZZcloud.google.com/go/videointelligence/apiv1p2beta1/videointelligencepb;videointelligencepb\xaa\x02(Google.Cloud.VideoIntelligence.V1P2Beta1\xca\x02(Google\\Cloud\\VideoIntelligence\\V1p2beta1\xea\x02+Google::Cloud::VideoIntelligence::V1p2beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.videointelligence.v1p2beta1.video_intelligence_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.videointelligence.v1p2beta1B\x1dVideoIntelligenceServiceProtoP\x01ZZcloud.google.com/go/videointelligence/apiv1p2beta1/videointelligencepb;videointelligencepb\xaa\x02(Google.Cloud.VideoIntelligence.V1P2Beta1\xca\x02(Google\\Cloud\\VideoIntelligence\\V1p2beta1\xea\x02+Google::Cloud::VideoIntelligence::V1p2beta1'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOINTELLIGENCESERVICE']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_options = b'\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._serialized_options = b'\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p2beta1/videos:annotate:\x01*'
    _globals['_FEATURE']._serialized_start = 4634
    _globals['_FEATURE']._serialized_end = 4789
    _globals['_LABELDETECTIONMODE']._serialized_start = 4791
    _globals['_LABELDETECTIONMODE']._serialized_end = 4905
    _globals['_LIKELIHOOD']._serialized_start = 4907
    _globals['_LIKELIHOOD']._serialized_end = 5023
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_start = 327
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_end = 595
    _globals['_VIDEOCONTEXT']._serialized_start = 598
    _globals['_VIDEOCONTEXT']._serialized_end = 1100
    _globals['_LABELDETECTIONCONFIG']._serialized_start = 1103
    _globals['_LABELDETECTIONCONFIG']._serialized_end = 1259
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_start = 1261
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_end = 1303
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_start = 1305
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_end = 1352
    _globals['_TEXTDETECTIONCONFIG']._serialized_start = 1354
    _globals['_TEXTDETECTIONCONFIG']._serialized_end = 1399
    _globals['_VIDEOSEGMENT']._serialized_start = 1401
    _globals['_VIDEOSEGMENT']._serialized_end = 1521
    _globals['_LABELSEGMENT']._serialized_start = 1523
    _globals['_LABELSEGMENT']._serialized_end = 1630
    _globals['_LABELFRAME']._serialized_start = 1632
    _globals['_LABELFRAME']._serialized_end = 1712
    _globals['_ENTITY']._serialized_start = 1714
    _globals['_ENTITY']._serialized_end = 1785
    _globals['_LABELANNOTATION']._serialized_start = 1788
    _globals['_LABELANNOTATION']._serialized_end = 2092
    _globals['_EXPLICITCONTENTFRAME']._serialized_start = 2095
    _globals['_EXPLICITCONTENTFRAME']._serialized_end = 2251
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_start = 2253
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_end = 2360
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_start = 2362
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_end = 2443
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_start = 2446
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_end = 3161
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_start = 3163
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_end = 3280
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_start = 3283
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_end = 3450
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_start = 3452
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_end = 3571
    _globals['_NORMALIZEDVERTEX']._serialized_start = 3573
    _globals['_NORMALIZEDVERTEX']._serialized_end = 3613
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_start = 3615
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_end = 3717
    _globals['_TEXTSEGMENT']._serialized_start = 3720
    _globals['_TEXTSEGMENT']._serialized_end = 3895
    _globals['_TEXTFRAME']._serialized_start = 3898
    _globals['_TEXTFRAME']._serialized_end = 4053
    _globals['_TEXTANNOTATION']._serialized_start = 4055
    _globals['_TEXTANNOTATION']._serialized_end = 4158
    _globals['_OBJECTTRACKINGFRAME']._serialized_start = 4161
    _globals['_OBJECTTRACKINGFRAME']._serialized_end = 4328
    _globals['_OBJECTTRACKINGANNOTATION']._serialized_start = 4331
    _globals['_OBJECTTRACKINGANNOTATION']._serialized_end = 4631
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_start = 5026
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_end = 5360