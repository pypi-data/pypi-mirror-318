"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/videointelligence/v1/video_intelligence.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/videointelligence/v1/video_intelligence.proto\x12!google.cloud.videointelligence.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xfe\x01\n\x14AnnotateVideoRequest\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x15\n\rinput_content\x18\x06 \x01(\x0c\x12A\n\x08features\x18\x02 \x03(\x0e2*.google.cloud.videointelligence.v1.FeatureB\x03\xe0A\x02\x12F\n\rvideo_context\x18\x03 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoContext\x12\x17\n\noutput_uri\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0blocation_id\x18\x05 \x01(\tB\x03\xe0A\x01"\xc1\x06\n\x0cVideoContext\x12A\n\x08segments\x18\x01 \x03(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12W\n\x16label_detection_config\x18\x02 \x01(\x0b27.google.cloud.videointelligence.v1.LabelDetectionConfig\x12b\n\x1cshot_change_detection_config\x18\x03 \x01(\x0b2<.google.cloud.videointelligence.v1.ShotChangeDetectionConfig\x12l\n!explicit_content_detection_config\x18\x04 \x01(\x0b2A.google.cloud.videointelligence.v1.ExplicitContentDetectionConfig\x12U\n\x15face_detection_config\x18\x05 \x01(\x0b26.google.cloud.videointelligence.v1.FaceDetectionConfig\x12a\n\x1bspeech_transcription_config\x18\x06 \x01(\x0b2<.google.cloud.videointelligence.v1.SpeechTranscriptionConfig\x12U\n\x15text_detection_config\x18\x08 \x01(\x0b26.google.cloud.videointelligence.v1.TextDetectionConfig\x12Y\n\x17person_detection_config\x18\x0b \x01(\x0b28.google.cloud.videointelligence.v1.PersonDetectionConfig\x12W\n\x16object_tracking_config\x18\r \x01(\x0b27.google.cloud.videointelligence.v1.ObjectTrackingConfig"\xdd\x01\n\x14LabelDetectionConfig\x12S\n\x14label_detection_mode\x18\x01 \x01(\x0e25.google.cloud.videointelligence.v1.LabelDetectionMode\x12\x19\n\x11stationary_camera\x18\x02 \x01(\x08\x12\r\n\x05model\x18\x03 \x01(\t\x12"\n\x1aframe_confidence_threshold\x18\x04 \x01(\x02\x12"\n\x1avideo_confidence_threshold\x18\x05 \x01(\x02"*\n\x19ShotChangeDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"%\n\x14ObjectTrackingConfig\x12\r\n\x05model\x18\x01 \x01(\t"`\n\x13FaceDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t\x12\x1e\n\x16include_bounding_boxes\x18\x02 \x01(\x08\x12\x1a\n\x12include_attributes\x18\x05 \x01(\x08"s\n\x15PersonDetectionConfig\x12\x1e\n\x16include_bounding_boxes\x18\x01 \x01(\x08\x12\x1e\n\x16include_pose_landmarks\x18\x02 \x01(\x08\x12\x1a\n\x12include_attributes\x18\x03 \x01(\x08"/\n\x1eExplicitContentDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"<\n\x13TextDetectionConfig\x12\x16\n\x0elanguage_hints\x18\x01 \x03(\t\x12\r\n\x05model\x18\x02 \x01(\t"x\n\x0cVideoSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"d\n\x0cLabelSegment\x12@\n\x07segment\x18\x01 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02"P\n\nLabelFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x02 \x01(\x02"G\n\x06Entity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xa5\x02\n\x0fLabelAnnotation\x129\n\x06entity\x18\x01 \x01(\x0b2).google.cloud.videointelligence.v1.Entity\x12D\n\x11category_entities\x18\x02 \x03(\x0b2).google.cloud.videointelligence.v1.Entity\x12A\n\x08segments\x18\x03 \x03(\x0b2/.google.cloud.videointelligence.v1.LabelSegment\x12=\n\x06frames\x18\x04 \x03(\x0b2-.google.cloud.videointelligence.v1.LabelFrame\x12\x0f\n\x07version\x18\x05 \x01(\t"\x95\x01\n\x14ExplicitContentFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12M\n\x16pornography_likelihood\x18\x02 \x01(\x0e2-.google.cloud.videointelligence.v1.Likelihood"u\n\x19ExplicitContentAnnotation\x12G\n\x06frames\x18\x01 \x03(\x0b27.google.cloud.videointelligence.v1.ExplicitContentFrame\x12\x0f\n\x07version\x18\x02 \x01(\t"Q\n\x15NormalizedBoundingBox\x12\x0c\n\x04left\x18\x01 \x01(\x02\x12\x0b\n\x03top\x18\x02 \x01(\x02\x12\r\n\x05right\x18\x03 \x01(\x02\x12\x0e\n\x06bottom\x18\x04 \x01(\x02"w\n\x17FaceDetectionAnnotation\x128\n\x06tracks\x18\x03 \x03(\x0b2(.google.cloud.videointelligence.v1.Track\x12\x11\n\tthumbnail\x18\x04 \x01(\x0c\x12\x0f\n\x07version\x18\x05 \x01(\t"f\n\x19PersonDetectionAnnotation\x128\n\x06tracks\x18\x01 \x03(\x0b2(.google.cloud.videointelligence.v1.Track\x12\x0f\n\x07version\x18\x02 \x01(\t"O\n\x0bFaceSegment\x12@\n\x07segment\x18\x01 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment"\x9c\x01\n\tFaceFrame\x12[\n\x19normalized_bounding_boxes\x18\x01 \x03(\x0b28.google.cloud.videointelligence.v1.NormalizedBoundingBox\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration:\x02\x18\x01"\xa7\x01\n\x0eFaceAnnotation\x12\x11\n\tthumbnail\x18\x01 \x01(\x0c\x12@\n\x08segments\x18\x02 \x03(\x0b2..google.cloud.videointelligence.v1.FaceSegment\x12<\n\x06frames\x18\x03 \x03(\x0b2,.google.cloud.videointelligence.v1.FaceFrame:\x02\x18\x01"\xba\x02\n\x11TimestampedObject\x12Y\n\x17normalized_bounding_box\x18\x01 \x01(\x0b28.google.cloud.videointelligence.v1.NormalizedBoundingBox\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12M\n\nattributes\x18\x03 \x03(\x0b24.google.cloud.videointelligence.v1.DetectedAttributeB\x03\xe0A\x01\x12K\n\tlandmarks\x18\x04 \x03(\x0b23.google.cloud.videointelligence.v1.DetectedLandmarkB\x03\xe0A\x01"\x84\x02\n\x05Track\x12@\n\x07segment\x18\x01 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12Q\n\x13timestamped_objects\x18\x02 \x03(\x0b24.google.cloud.videointelligence.v1.TimestampedObject\x12M\n\nattributes\x18\x03 \x03(\x0b24.google.cloud.videointelligence.v1.DetectedAttributeB\x03\xe0A\x01\x12\x17\n\nconfidence\x18\x04 \x01(\x02B\x03\xe0A\x01"D\n\x11DetectedAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\r\n\x05value\x18\x03 \x01(\t"x\n\x10DetectedLandmark\x12\x0c\n\x04name\x18\x01 \x01(\t\x12B\n\x05point\x18\x02 \x01(\x0b23.google.cloud.videointelligence.v1.NormalizedVertex\x12\x12\n\nconfidence\x18\x03 \x01(\x02"\xe9\n\n\x16VideoAnnotationResults\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12@\n\x07segment\x18\n \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12U\n\x19segment_label_annotations\x18\x02 \x03(\x0b22.google.cloud.videointelligence.v1.LabelAnnotation\x12^\n"segment_presence_label_annotations\x18\x17 \x03(\x0b22.google.cloud.videointelligence.v1.LabelAnnotation\x12R\n\x16shot_label_annotations\x18\x03 \x03(\x0b22.google.cloud.videointelligence.v1.LabelAnnotation\x12[\n\x1fshot_presence_label_annotations\x18\x18 \x03(\x0b22.google.cloud.videointelligence.v1.LabelAnnotation\x12S\n\x17frame_label_annotations\x18\x04 \x03(\x0b22.google.cloud.videointelligence.v1.LabelAnnotation\x12O\n\x10face_annotations\x18\x05 \x03(\x0b21.google.cloud.videointelligence.v1.FaceAnnotationB\x02\x18\x01\x12^\n\x1aface_detection_annotations\x18\r \x03(\x0b2:.google.cloud.videointelligence.v1.FaceDetectionAnnotation\x12I\n\x10shot_annotations\x18\x06 \x03(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12Y\n\x13explicit_annotation\x18\x07 \x01(\x0b2<.google.cloud.videointelligence.v1.ExplicitContentAnnotation\x12U\n\x15speech_transcriptions\x18\x0b \x03(\x0b26.google.cloud.videointelligence.v1.SpeechTranscription\x12K\n\x10text_annotations\x18\x0c \x03(\x0b21.google.cloud.videointelligence.v1.TextAnnotation\x12W\n\x12object_annotations\x18\x0e \x03(\x0b2;.google.cloud.videointelligence.v1.ObjectTrackingAnnotation\x12b\n\x1clogo_recognition_annotations\x18\x13 \x03(\x0b2<.google.cloud.videointelligence.v1.LogoRecognitionAnnotation\x12b\n\x1cperson_detection_annotations\x18\x14 \x03(\x0b2<.google.cloud.videointelligence.v1.PersonDetectionAnnotation\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status"n\n\x15AnnotateVideoResponse\x12U\n\x12annotation_results\x18\x01 \x03(\x0b29.google.cloud.videointelligence.v1.VideoAnnotationResults"\xa6\x02\n\x17VideoAnnotationProgress\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x18\n\x10progress_percent\x18\x02 \x01(\x05\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12;\n\x07feature\x18\x05 \x01(\x0e2*.google.cloud.videointelligence.v1.Feature\x12@\n\x07segment\x18\x06 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment"p\n\x15AnnotateVideoProgress\x12W\n\x13annotation_progress\x18\x01 \x03(\x0b2:.google.cloud.videointelligence.v1.VideoAnnotationProgress"\x81\x03\n\x19SpeechTranscriptionConfig\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10max_alternatives\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1d\n\x10filter_profanity\x18\x03 \x01(\x08B\x03\xe0A\x01\x12N\n\x0fspeech_contexts\x18\x04 \x03(\x0b20.google.cloud.videointelligence.v1.SpeechContextB\x03\xe0A\x01\x12)\n\x1cenable_automatic_punctuation\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x19\n\x0caudio_tracks\x18\x06 \x03(\x05B\x03\xe0A\x01\x12\'\n\x1aenable_speaker_diarization\x18\x07 \x01(\x08B\x03\xe0A\x01\x12&\n\x19diarization_speaker_count\x18\x08 \x01(\x05B\x03\xe0A\x01\x12#\n\x16enable_word_confidence\x18\t \x01(\x08B\x03\xe0A\x01"%\n\rSpeechContext\x12\x14\n\x07phrases\x18\x01 \x03(\tB\x03\xe0A\x01"\x88\x01\n\x13SpeechTranscription\x12U\n\x0calternatives\x18\x01 \x03(\x0b2?.google.cloud.videointelligence.v1.SpeechRecognitionAlternative\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x03"\x8c\x01\n\x1cSpeechRecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x17\n\nconfidence\x18\x02 \x01(\x02B\x03\xe0A\x03\x12?\n\x05words\x18\x03 \x03(\x0b2+.google.cloud.videointelligence.v1.WordInfoB\x03\xe0A\x03"\xa7\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08end_time\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x17\n\nconfidence\x18\x04 \x01(\x02B\x03\xe0A\x03\x12\x18\n\x0bspeaker_tag\x18\x05 \x01(\x05B\x03\xe0A\x03"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"_\n\x16NormalizedBoundingPoly\x12E\n\x08vertices\x18\x01 \x03(\x0b23.google.cloud.videointelligence.v1.NormalizedVertex"\xa1\x01\n\x0bTextSegment\x12@\n\x07segment\x18\x01 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12<\n\x06frames\x18\x03 \x03(\x0b2,.google.cloud.videointelligence.v1.TextFrame"\x94\x01\n\tTextFrame\x12W\n\x14rotated_bounding_box\x18\x01 \x01(\x0b29.google.cloud.videointelligence.v1.NormalizedBoundingPoly\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"q\n\x0eTextAnnotation\x12\x0c\n\x04text\x18\x01 \x01(\t\x12@\n\x08segments\x18\x02 \x03(\x0b2..google.cloud.videointelligence.v1.TextSegment\x12\x0f\n\x07version\x18\x03 \x01(\t"\xa0\x01\n\x13ObjectTrackingFrame\x12Y\n\x17normalized_bounding_box\x18\x01 \x01(\x0b28.google.cloud.videointelligence.v1.NormalizedBoundingBox\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xa8\x02\n\x18ObjectTrackingAnnotation\x12B\n\x07segment\x18\x03 \x01(\x0b2/.google.cloud.videointelligence.v1.VideoSegmentH\x00\x12\x12\n\x08track_id\x18\x05 \x01(\x03H\x00\x129\n\x06entity\x18\x01 \x01(\x0b2).google.cloud.videointelligence.v1.Entity\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12F\n\x06frames\x18\x02 \x03(\x0b26.google.cloud.videointelligence.v1.ObjectTrackingFrame\x12\x0f\n\x07version\x18\x06 \x01(\tB\x0c\n\ntrack_info"\xd3\x01\n\x19LogoRecognitionAnnotation\x129\n\x06entity\x18\x01 \x01(\x0b2).google.cloud.videointelligence.v1.Entity\x128\n\x06tracks\x18\x02 \x03(\x0b2(.google.cloud.videointelligence.v1.Track\x12A\n\x08segments\x18\x03 \x03(\x0b2/.google.cloud.videointelligence.v1.VideoSegment*\xf5\x01\n\x07Feature\x12\x17\n\x13FEATURE_UNSPECIFIED\x10\x00\x12\x13\n\x0fLABEL_DETECTION\x10\x01\x12\x19\n\x15SHOT_CHANGE_DETECTION\x10\x02\x12\x1e\n\x1aEXPLICIT_CONTENT_DETECTION\x10\x03\x12\x12\n\x0eFACE_DETECTION\x10\x04\x12\x18\n\x14SPEECH_TRANSCRIPTION\x10\x06\x12\x12\n\x0eTEXT_DETECTION\x10\x07\x12\x13\n\x0fOBJECT_TRACKING\x10\t\x12\x14\n\x10LOGO_RECOGNITION\x10\x0c\x12\x14\n\x10PERSON_DETECTION\x10\x0e*r\n\x12LabelDetectionMode\x12$\n LABEL_DETECTION_MODE_UNSPECIFIED\x10\x00\x12\r\n\tSHOT_MODE\x10\x01\x12\x0e\n\nFRAME_MODE\x10\x02\x12\x17\n\x13SHOT_AND_FRAME_MODE\x10\x03*t\n\nLikelihood\x12\x1a\n\x16LIKELIHOOD_UNSPECIFIED\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xc0\x02\n\x18VideoIntelligenceService\x12\xcd\x01\n\rAnnotateVideo\x127.google.cloud.videointelligence.v1.AnnotateVideoRequest\x1a\x1d.google.longrunning.Operation"d\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x18"\x13/v1/videos:annotate:\x01*\x1aT\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8c\x02\n%com.google.cloud.videointelligence.v1B\x1dVideoIntelligenceServiceProtoP\x01ZScloud.google.com/go/videointelligence/apiv1/videointelligencepb;videointelligencepb\xaa\x02!Google.Cloud.VideoIntelligence.V1\xca\x02!Google\\Cloud\\VideoIntelligence\\V1\xea\x02$Google::Cloud::VideoIntelligence::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.videointelligence.v1.video_intelligence_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.videointelligence.v1B\x1dVideoIntelligenceServiceProtoP\x01ZScloud.google.com/go/videointelligence/apiv1/videointelligencepb;videointelligencepb\xaa\x02!Google.Cloud.VideoIntelligence.V1\xca\x02!Google\\Cloud\\VideoIntelligence\\V1\xea\x02$Google::Cloud::VideoIntelligence::V1'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._serialized_options = b'\xe0A\x01'
    _globals['_FACEFRAME']._loaded_options = None
    _globals['_FACEFRAME']._serialized_options = b'\x18\x01'
    _globals['_FACEANNOTATION']._loaded_options = None
    _globals['_FACEANNOTATION']._serialized_options = b'\x18\x01'
    _globals['_TIMESTAMPEDOBJECT'].fields_by_name['attributes']._loaded_options = None
    _globals['_TIMESTAMPEDOBJECT'].fields_by_name['attributes']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESTAMPEDOBJECT'].fields_by_name['landmarks']._loaded_options = None
    _globals['_TIMESTAMPEDOBJECT'].fields_by_name['landmarks']._serialized_options = b'\xe0A\x01'
    _globals['_TRACK'].fields_by_name['attributes']._loaded_options = None
    _globals['_TRACK'].fields_by_name['attributes']._serialized_options = b'\xe0A\x01'
    _globals['_TRACK'].fields_by_name['confidence']._loaded_options = None
    _globals['_TRACK'].fields_by_name['confidence']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOANNOTATIONRESULTS'].fields_by_name['face_annotations']._loaded_options = None
    _globals['_VIDEOANNOTATIONRESULTS'].fields_by_name['face_annotations']._serialized_options = b'\x18\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['language_code']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['max_alternatives']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['max_alternatives']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['filter_profanity']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['filter_profanity']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['speech_contexts']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['speech_contexts']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_automatic_punctuation']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_automatic_punctuation']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['audio_tracks']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['audio_tracks']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_speaker_diarization']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_speaker_diarization']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['diarization_speaker_count']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['diarization_speaker_count']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_word_confidence']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTIONCONFIG'].fields_by_name['enable_word_confidence']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._loaded_options = None
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHTRANSCRIPTION'].fields_by_name['language_code']._loaded_options = None
    _globals['_SPEECHTRANSCRIPTION'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['confidence']._loaded_options = None
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['confidence']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['words']._loaded_options = None
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['words']._serialized_options = b'\xe0A\x03'
    _globals['_WORDINFO'].fields_by_name['confidence']._loaded_options = None
    _globals['_WORDINFO'].fields_by_name['confidence']._serialized_options = b'\xe0A\x03'
    _globals['_WORDINFO'].fields_by_name['speaker_tag']._loaded_options = None
    _globals['_WORDINFO'].fields_by_name['speaker_tag']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOINTELLIGENCESERVICE']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_options = b'\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._serialized_options = b'\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x18"\x13/v1/videos:annotate:\x01*'
    _globals['_FEATURE']._serialized_start = 8510
    _globals['_FEATURE']._serialized_end = 8755
    _globals['_LABELDETECTIONMODE']._serialized_start = 8757
    _globals['_LABELDETECTIONMODE']._serialized_end = 8871
    _globals['_LIKELIHOOD']._serialized_start = 8873
    _globals['_LIKELIHOOD']._serialized_end = 8989
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_start = 313
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_end = 567
    _globals['_VIDEOCONTEXT']._serialized_start = 570
    _globals['_VIDEOCONTEXT']._serialized_end = 1403
    _globals['_LABELDETECTIONCONFIG']._serialized_start = 1406
    _globals['_LABELDETECTIONCONFIG']._serialized_end = 1627
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_start = 1629
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_end = 1671
    _globals['_OBJECTTRACKINGCONFIG']._serialized_start = 1673
    _globals['_OBJECTTRACKINGCONFIG']._serialized_end = 1710
    _globals['_FACEDETECTIONCONFIG']._serialized_start = 1712
    _globals['_FACEDETECTIONCONFIG']._serialized_end = 1808
    _globals['_PERSONDETECTIONCONFIG']._serialized_start = 1810
    _globals['_PERSONDETECTIONCONFIG']._serialized_end = 1925
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_start = 1927
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_end = 1974
    _globals['_TEXTDETECTIONCONFIG']._serialized_start = 1976
    _globals['_TEXTDETECTIONCONFIG']._serialized_end = 2036
    _globals['_VIDEOSEGMENT']._serialized_start = 2038
    _globals['_VIDEOSEGMENT']._serialized_end = 2158
    _globals['_LABELSEGMENT']._serialized_start = 2160
    _globals['_LABELSEGMENT']._serialized_end = 2260
    _globals['_LABELFRAME']._serialized_start = 2262
    _globals['_LABELFRAME']._serialized_end = 2342
    _globals['_ENTITY']._serialized_start = 2344
    _globals['_ENTITY']._serialized_end = 2415
    _globals['_LABELANNOTATION']._serialized_start = 2418
    _globals['_LABELANNOTATION']._serialized_end = 2711
    _globals['_EXPLICITCONTENTFRAME']._serialized_start = 2714
    _globals['_EXPLICITCONTENTFRAME']._serialized_end = 2863
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_start = 2865
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_end = 2982
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_start = 2984
    _globals['_NORMALIZEDBOUNDINGBOX']._serialized_end = 3065
    _globals['_FACEDETECTIONANNOTATION']._serialized_start = 3067
    _globals['_FACEDETECTIONANNOTATION']._serialized_end = 3186
    _globals['_PERSONDETECTIONANNOTATION']._serialized_start = 3188
    _globals['_PERSONDETECTIONANNOTATION']._serialized_end = 3290
    _globals['_FACESEGMENT']._serialized_start = 3292
    _globals['_FACESEGMENT']._serialized_end = 3371
    _globals['_FACEFRAME']._serialized_start = 3374
    _globals['_FACEFRAME']._serialized_end = 3530
    _globals['_FACEANNOTATION']._serialized_start = 3533
    _globals['_FACEANNOTATION']._serialized_end = 3700
    _globals['_TIMESTAMPEDOBJECT']._serialized_start = 3703
    _globals['_TIMESTAMPEDOBJECT']._serialized_end = 4017
    _globals['_TRACK']._serialized_start = 4020
    _globals['_TRACK']._serialized_end = 4280
    _globals['_DETECTEDATTRIBUTE']._serialized_start = 4282
    _globals['_DETECTEDATTRIBUTE']._serialized_end = 4350
    _globals['_DETECTEDLANDMARK']._serialized_start = 4352
    _globals['_DETECTEDLANDMARK']._serialized_end = 4472
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_start = 4475
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_end = 5860
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_start = 5862
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_end = 5972
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_start = 5975
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_end = 6269
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_start = 6271
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_end = 6383
    _globals['_SPEECHTRANSCRIPTIONCONFIG']._serialized_start = 6386
    _globals['_SPEECHTRANSCRIPTIONCONFIG']._serialized_end = 6771
    _globals['_SPEECHCONTEXT']._serialized_start = 6773
    _globals['_SPEECHCONTEXT']._serialized_end = 6810
    _globals['_SPEECHTRANSCRIPTION']._serialized_start = 6813
    _globals['_SPEECHTRANSCRIPTION']._serialized_end = 6949
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_start = 6952
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_end = 7092
    _globals['_WORDINFO']._serialized_start = 7095
    _globals['_WORDINFO']._serialized_end = 7262
    _globals['_NORMALIZEDVERTEX']._serialized_start = 7264
    _globals['_NORMALIZEDVERTEX']._serialized_end = 7304
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_start = 7306
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_end = 7401
    _globals['_TEXTSEGMENT']._serialized_start = 7404
    _globals['_TEXTSEGMENT']._serialized_end = 7565
    _globals['_TEXTFRAME']._serialized_start = 7568
    _globals['_TEXTFRAME']._serialized_end = 7716
    _globals['_TEXTANNOTATION']._serialized_start = 7718
    _globals['_TEXTANNOTATION']._serialized_end = 7831
    _globals['_OBJECTTRACKINGFRAME']._serialized_start = 7834
    _globals['_OBJECTTRACKINGFRAME']._serialized_end = 7994
    _globals['_OBJECTTRACKINGANNOTATION']._serialized_start = 7997
    _globals['_OBJECTTRACKINGANNOTATION']._serialized_end = 8293
    _globals['_LOGORECOGNITIONANNOTATION']._serialized_start = 8296
    _globals['_LOGORECOGNITIONANNOTATION']._serialized_end = 8507
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_start = 8992
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_end = 9312