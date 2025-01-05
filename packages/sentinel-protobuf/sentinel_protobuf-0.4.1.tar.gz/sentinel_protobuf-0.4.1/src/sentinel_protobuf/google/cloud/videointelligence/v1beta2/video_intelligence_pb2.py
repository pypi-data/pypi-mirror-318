"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/videointelligence/v1beta2/video_intelligence.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/videointelligence/v1beta2/video_intelligence.proto\x12&google.cloud.videointelligence.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x88\x02\n\x14AnnotateVideoRequest\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x15\n\rinput_content\x18\x06 \x01(\x0c\x12F\n\x08features\x18\x02 \x03(\x0e2/.google.cloud.videointelligence.v1beta2.FeatureB\x03\xe0A\x02\x12K\n\rvideo_context\x18\x03 \x01(\x0b24.google.cloud.videointelligence.v1beta2.VideoContext\x12\x17\n\noutput_uri\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0blocation_id\x18\x05 \x01(\tB\x03\xe0A\x01"\xec\x03\n\x0cVideoContext\x12F\n\x08segments\x18\x01 \x03(\x0b24.google.cloud.videointelligence.v1beta2.VideoSegment\x12\\\n\x16label_detection_config\x18\x02 \x01(\x0b2<.google.cloud.videointelligence.v1beta2.LabelDetectionConfig\x12g\n\x1cshot_change_detection_config\x18\x03 \x01(\x0b2A.google.cloud.videointelligence.v1beta2.ShotChangeDetectionConfig\x12q\n!explicit_content_detection_config\x18\x04 \x01(\x0b2F.google.cloud.videointelligence.v1beta2.ExplicitContentDetectionConfig\x12Z\n\x15face_detection_config\x18\x05 \x01(\x0b2;.google.cloud.videointelligence.v1beta2.FaceDetectionConfig"\x9a\x01\n\x14LabelDetectionConfig\x12X\n\x14label_detection_mode\x18\x01 \x01(\x0e2:.google.cloud.videointelligence.v1beta2.LabelDetectionMode\x12\x19\n\x11stationary_camera\x18\x02 \x01(\x08\x12\r\n\x05model\x18\x03 \x01(\t"*\n\x19ShotChangeDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"/\n\x1eExplicitContentDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"D\n\x13FaceDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t\x12\x1e\n\x16include_bounding_boxes\x18\x02 \x01(\x08"x\n\x0cVideoSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"i\n\x0cLabelSegment\x12E\n\x07segment\x18\x01 \x01(\x0b24.google.cloud.videointelligence.v1beta2.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02"P\n\nLabelFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x02 \x01(\x02"G\n\x06Entity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xa8\x02\n\x0fLabelAnnotation\x12>\n\x06entity\x18\x01 \x01(\x0b2..google.cloud.videointelligence.v1beta2.Entity\x12I\n\x11category_entities\x18\x02 \x03(\x0b2..google.cloud.videointelligence.v1beta2.Entity\x12F\n\x08segments\x18\x03 \x03(\x0b24.google.cloud.videointelligence.v1beta2.LabelSegment\x12B\n\x06frames\x18\x04 \x03(\x0b22.google.cloud.videointelligence.v1beta2.LabelFrame"\x9a\x01\n\x14ExplicitContentFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12R\n\x16pornography_likelihood\x18\x02 \x01(\x0e22.google.cloud.videointelligence.v1beta2.Likelihood"i\n\x19ExplicitContentAnnotation\x12L\n\x06frames\x18\x01 \x03(\x0b2<.google.cloud.videointelligence.v1beta2.ExplicitContentFrame"Q\n\x15NormalizedBoundingBox\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\x0b\n\x03top\x18\x02 \x01(\x02\x12\r\n\x05right\x18\x03 \x01(\x02\x12\x0e\n\x06bottom\x18\x04 \x01(\x02"T\n\x0bFaceSegment\x12E\n\x07segment\x18\x01 \x01(\x0b24.google.cloud.videointelligence.v1beta2.VideoSegment"\x9d\x01\n\tFaceFrame\x12`\n\x19normalized_bounding_boxes\x18\x01 \x03(\x0b2=.google.cloud.videointelligence.v1beta2.NormalizedBoundingBox\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xad\x01\n\x0eFaceAnnotation\x12\x11\n\tthumbnail\x18\x01 \x01(\x0c\x12E\n\x08segments\x18\x02 \x03(\x0b23.google.cloud.videointelligence.v1beta2.FaceSegment\x12A\n\x06frames\x18\x03 \x03(\x0b21.google.cloud.videointelligence.v1beta2.FaceFrame"\xdf\x04\n\x16VideoAnnotationResults\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12Z\n\x19segment_label_annotations\x18\x02 \x03(\x0b27.google.cloud.videointelligence.v1beta2.LabelAnnotation\x12W\n\x16shot_label_annotations\x18\x03 \x03(\x0b27.google.cloud.videointelligence.v1beta2.LabelAnnotation\x12X\n\x17frame_label_annotations\x18\x04 \x03(\x0b27.google.cloud.videointelligence.v1beta2.LabelAnnotation\x12P\n\x10face_annotations\x18\x05 \x03(\x0b26.google.cloud.videointelligence.v1beta2.FaceAnnotation\x12N\n\x10shot_annotations\x18\x06 \x03(\x0b24.google.cloud.videointelligence.v1beta2.VideoSegment\x12^\n\x13explicit_annotation\x18\x07 \x01(\x0b2A.google.cloud.videointelligence.v1beta2.ExplicitContentAnnotation\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status"s\n\x15AnnotateVideoResponse\x12Z\n\x12annotation_results\x18\x01 \x03(\x0b2>.google.cloud.videointelligence.v1beta2.VideoAnnotationResults"\xa7\x01\n\x17VideoAnnotationProgress\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x18\n\x10progress_percent\x18\x02 \x01(\x05\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"u\n\x15AnnotateVideoProgress\x12\\\n\x13annotation_progress\x18\x01 \x03(\x0b2?.google.cloud.videointelligence.v1beta2.VideoAnnotationProgress*\x86\x01\n\x07Feature\x12\x17\n\x13FEATURE_UNSPECIFIED\x10\x00\x12\x13\n\x0fLABEL_DETECTION\x10\x01\x12\x19\n\x15SHOT_CHANGE_DETECTION\x10\x02\x12\x1e\n\x1aEXPLICIT_CONTENT_DETECTION\x10\x03\x12\x12\n\x0eFACE_DETECTION\x10\x04*r\n\x12LabelDetectionMode\x12$\n LABEL_DETECTION_MODE_UNSPECIFIED\x10\x00\x12\r\n\tSHOT_MODE\x10\x01\x12\x0e\n\nFRAME_MODE\x10\x02\x12\x17\n\x13SHOT_AND_FRAME_MODE\x10\x03*t\n\nLikelihood\x12\x1a\n\x16LIKELIHOOD_UNSPECIFIED\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xca\x02\n\x18VideoIntelligenceService\x12\xd7\x01\n\rAnnotateVideo\x12<.google.cloud.videointelligence.v1beta2.AnnotateVideoRequest\x1a\x1d.google.longrunning.Operation"i\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1d"\x18/v1beta2/videos:annotate:\x01*\x1aT\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa5\x02\n*com.google.cloud.videointelligence.v1beta2B\x1dVideoIntelligenceServiceProtoP\x01ZXcloud.google.com/go/videointelligence/apiv1beta2/videointelligencepb;videointelligencepb\xaa\x02&Google.Cloud.VideoIntelligence.V1Beta2\xca\x02&Google\\Cloud\\VideoIntelligence\\V1beta2\xea\x02)Google::Cloud::VideoIntelligence::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.videointelligence.v1beta2.video_intelligence_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.videointelligence.v1beta2B\x1dVideoIntelligenceServiceProtoP\x01ZXcloud.google.com/go/videointelligence/apiv1beta2/videointelligencepb;videointelligencepb\xaa\x02&Google.Cloud.VideoIntelligence.V1Beta2\xca\x02&Google\\Cloud\\VideoIntelligence\\V1beta2\xea\x02)Google::Cloud::VideoIntelligence::V1beta2'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOINTELLIGENCESERVICE']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_options = b'\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._serialized_options = b'\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1d"\x18/v1beta2/videos:annotate:\x01*'
    _globals['_FEATURE']._serialized_start = 3873
    _globals['_FEATURE']._serialized_end = 4007
    _globals['_LABELDETECTIONMODE']._serialized_start = 4009
    _globals['_LABELDETECTIONMODE']._serialized_end = 4123
    _globals['_LIKELIHOOD']._serialized_start = 4125
    _globals['_LIKELIHOOD']._serialized_end = 4241
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_start = 323
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_end = 587
    _globals['_VIDEOCONTEXT']._serialized_start = 590
    _globals['_VIDEOCONTEXT']._serialized_end = 1082
    _globals['_LABELDETECTIONCONFIG']._serialized_start = 1085
    _globals['_LABELDETECTIONCONFIG']._serialized_end = 1239
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_start = 1241
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_end = 1283
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_start = 1285
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_end = 1332
    _globals['_FACEDETECTIONCONFIG']._serialized_start = 1334
    _globals['_FACEDETECTIONCONFIG']._serialized_end = 1402
    _globals['_VIDEOSEGMENT']._serialized_start = 1404
    _globals['_VIDEOSEGMENT']._serialized_end = 1524
    _globals['_LABELSEGMENT']._serialized_start = 1526
    _globals['_LABELSEGMENT']._serialized_end = 1631
    _globals['_LABELFRAME']._serialized_start = 1633
    _globals['_LABELFRAME']._serialized_end = 1713
    _globals['_ENTITY']._serialized_start = 1715
    _globals['_ENTITY']._serialized_end = 1786
    _globals['_LABELANNOTATION']._serialized_start = 1789
    _globals['_LABELANNOTATION']._serialized_end = 2085
    _globals['_EXPLICITCONTENTFRAME']._serialized_start = 2088
    _globals['_EXPLICITCONTENTFRAME']._serialized_end = 2242
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_start = 2244
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_end = 2349
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_start = 2351
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_end = 2432
    _globals['_FACESEGMENT']._serialized_start = 2434
    _globals['_FACESEGMENT']._serialized_end = 2518
    _globals['_FACEFRAME']._serialized_start = 2521
    _globals['_FACEFRAME']._serialized_end = 2678
    _globals['_FACEANNOTATION']._serialized_start = 2681
    _globals['_FACEANNOTATION']._serialized_end = 2854
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_start = 2857
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_end = 3464
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_start = 3466
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_end = 3581
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_start = 3584
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_end = 3751
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_start = 3753
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_end = 3870
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_start = 4244
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_end = 4574