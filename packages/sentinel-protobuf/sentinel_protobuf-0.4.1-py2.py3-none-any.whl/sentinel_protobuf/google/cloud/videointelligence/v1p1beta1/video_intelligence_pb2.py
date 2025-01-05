"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/videointelligence/v1p1beta1/video_intelligence.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/videointelligence/v1p1beta1/video_intelligence.proto\x12(google.cloud.videointelligence.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x8c\x02\n\x14AnnotateVideoRequest\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x15\n\rinput_content\x18\x06 \x01(\x0c\x12H\n\x08features\x18\x02 \x03(\x0e21.google.cloud.videointelligence.v1p1beta1.FeatureB\x03\xe0A\x02\x12M\n\rvideo_context\x18\x03 \x01(\x0b26.google.cloud.videointelligence.v1p1beta1.VideoContext\x12\x17\n\noutput_uri\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0blocation_id\x18\x05 \x01(\tB\x03\xe0A\x01"\x82\x04\n\x0cVideoContext\x12H\n\x08segments\x18\x01 \x03(\x0b26.google.cloud.videointelligence.v1p1beta1.VideoSegment\x12^\n\x16label_detection_config\x18\x02 \x01(\x0b2>.google.cloud.videointelligence.v1p1beta1.LabelDetectionConfig\x12i\n\x1cshot_change_detection_config\x18\x03 \x01(\x0b2C.google.cloud.videointelligence.v1p1beta1.ShotChangeDetectionConfig\x12s\n!explicit_content_detection_config\x18\x04 \x01(\x0b2H.google.cloud.videointelligence.v1p1beta1.ExplicitContentDetectionConfig\x12h\n\x1bspeech_transcription_config\x18\x06 \x01(\x0b2C.google.cloud.videointelligence.v1p1beta1.SpeechTranscriptionConfig"\x9c\x01\n\x14LabelDetectionConfig\x12Z\n\x14label_detection_mode\x18\x01 \x01(\x0e2<.google.cloud.videointelligence.v1p1beta1.LabelDetectionMode\x12\x19\n\x11stationary_camera\x18\x02 \x01(\x08\x12\r\n\x05model\x18\x03 \x01(\t"*\n\x19ShotChangeDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"/\n\x1eExplicitContentDetectionConfig\x12\r\n\x05model\x18\x01 \x01(\t"x\n\x0cVideoSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"k\n\x0cLabelSegment\x12G\n\x07segment\x18\x01 \x01(\x0b26.google.cloud.videointelligence.v1p1beta1.VideoSegment\x12\x12\n\nconfidence\x18\x02 \x01(\x02"P\n\nLabelFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\nconfidence\x18\x02 \x01(\x02"G\n\x06Entity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xb0\x02\n\x0fLabelAnnotation\x12@\n\x06entity\x18\x01 \x01(\x0b20.google.cloud.videointelligence.v1p1beta1.Entity\x12K\n\x11category_entities\x18\x02 \x03(\x0b20.google.cloud.videointelligence.v1p1beta1.Entity\x12H\n\x08segments\x18\x03 \x03(\x0b26.google.cloud.videointelligence.v1p1beta1.LabelSegment\x12D\n\x06frames\x18\x04 \x03(\x0b24.google.cloud.videointelligence.v1p1beta1.LabelFrame"\x9c\x01\n\x14ExplicitContentFrame\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12T\n\x16pornography_likelihood\x18\x02 \x01(\x0e24.google.cloud.videointelligence.v1p1beta1.Likelihood"k\n\x19ExplicitContentAnnotation\x12N\n\x06frames\x18\x01 \x03(\x0b2>.google.cloud.videointelligence.v1p1beta1.ExplicitContentFrame"\xf5\x04\n\x16VideoAnnotationResults\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\\\n\x19segment_label_annotations\x18\x02 \x03(\x0b29.google.cloud.videointelligence.v1p1beta1.LabelAnnotation\x12Y\n\x16shot_label_annotations\x18\x03 \x03(\x0b29.google.cloud.videointelligence.v1p1beta1.LabelAnnotation\x12Z\n\x17frame_label_annotations\x18\x04 \x03(\x0b29.google.cloud.videointelligence.v1p1beta1.LabelAnnotation\x12P\n\x10shot_annotations\x18\x06 \x03(\x0b26.google.cloud.videointelligence.v1p1beta1.VideoSegment\x12`\n\x13explicit_annotation\x18\x07 \x01(\x0b2C.google.cloud.videointelligence.v1p1beta1.ExplicitContentAnnotation\x12\\\n\x15speech_transcriptions\x18\x0b \x03(\x0b2=.google.cloud.videointelligence.v1p1beta1.SpeechTranscription\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status"u\n\x15AnnotateVideoResponse\x12\\\n\x12annotation_results\x18\x01 \x03(\x0b2@.google.cloud.videointelligence.v1p1beta1.VideoAnnotationResults"\xa7\x01\n\x17VideoAnnotationProgress\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x18\n\x10progress_percent\x18\x02 \x01(\x05\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"w\n\x15AnnotateVideoProgress\x12^\n\x13annotation_progress\x18\x01 \x03(\x0b2A.google.cloud.videointelligence.v1p1beta1.VideoAnnotationProgress"\x92\x02\n\x19SpeechTranscriptionConfig\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10max_alternatives\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1d\n\x10filter_profanity\x18\x03 \x01(\x08B\x03\xe0A\x01\x12U\n\x0fspeech_contexts\x18\x04 \x03(\x0b27.google.cloud.videointelligence.v1p1beta1.SpeechContextB\x03\xe0A\x01\x12)\n\x1cenable_automatic_punctuation\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x19\n\x0caudio_tracks\x18\x06 \x03(\x05B\x03\xe0A\x01"%\n\rSpeechContext\x12\x14\n\x07phrases\x18\x01 \x03(\tB\x03\xe0A\x01"s\n\x13SpeechTranscription\x12\\\n\x0calternatives\x18\x01 \x03(\x0b2F.google.cloud.videointelligence.v1p1beta1.SpeechRecognitionAlternative"\x8e\x01\n\x1cSpeechRecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x17\n\nconfidence\x18\x02 \x01(\x02B\x03\xe0A\x03\x12A\n\x05words\x18\x03 \x03(\x0b22.google.cloud.videointelligence.v1p1beta1.WordInfo"t\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08end_time\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t*\x8c\x01\n\x07Feature\x12\x17\n\x13FEATURE_UNSPECIFIED\x10\x00\x12\x13\n\x0fLABEL_DETECTION\x10\x01\x12\x19\n\x15SHOT_CHANGE_DETECTION\x10\x02\x12\x1e\n\x1aEXPLICIT_CONTENT_DETECTION\x10\x03\x12\x18\n\x14SPEECH_TRANSCRIPTION\x10\x06*r\n\x12LabelDetectionMode\x12$\n LABEL_DETECTION_MODE_UNSPECIFIED\x10\x00\x12\r\n\tSHOT_MODE\x10\x01\x12\x0e\n\nFRAME_MODE\x10\x02\x12\x17\n\x13SHOT_AND_FRAME_MODE\x10\x03*t\n\nLikelihood\x12\x1a\n\x16LIKELIHOOD_UNSPECIFIED\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xce\x02\n\x18VideoIntelligenceService\x12\xdb\x01\n\rAnnotateVideo\x12>.google.cloud.videointelligence.v1p1beta1.AnnotateVideoRequest\x1a\x1d.google.longrunning.Operation"k\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p1beta1/videos:annotate:\x01*\x1aT\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xaf\x02\n,com.google.cloud.videointelligence.v1p1beta1B\x1dVideoIntelligenceServiceProtoP\x01ZZcloud.google.com/go/videointelligence/apiv1p1beta1/videointelligencepb;videointelligencepb\xaa\x02(Google.Cloud.VideoIntelligence.V1P1Beta1\xca\x02(Google\\Cloud\\VideoIntelligence\\V1p1beta1\xea\x02+Google::Cloud::VideoIntelligence::V1p1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.videointelligence.v1p1beta1.video_intelligence_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.videointelligence.v1p1beta1B\x1dVideoIntelligenceServiceProtoP\x01ZZcloud.google.com/go/videointelligence/apiv1p1beta1/videointelligencepb;videointelligencepb\xaa\x02(Google.Cloud.VideoIntelligence.V1P1Beta1\xca\x02(Google\\Cloud\\VideoIntelligence\\V1p1beta1\xea\x02+Google::Cloud::VideoIntelligence::V1p1beta1'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['features']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['output_uri']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._loaded_options = None
    _globals['_ANNOTATEVIDEOREQUEST'].fields_by_name['location_id']._serialized_options = b'\xe0A\x01'
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
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._loaded_options = None
    _globals['_SPEECHCONTEXT'].fields_by_name['phrases']._serialized_options = b'\xe0A\x01'
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['confidence']._loaded_options = None
    _globals['_SPEECHRECOGNITIONALTERNATIVE'].fields_by_name['confidence']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOINTELLIGENCESERVICE']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_options = b'\xcaA videointelligence.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._loaded_options = None
    _globals['_VIDEOINTELLIGENCESERVICE'].methods_by_name['AnnotateVideo']._serialized_options = b'\xcaA.\n\x15AnnotateVideoResponse\x12\x15AnnotateVideoProgress\xdaA\x12input_uri,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p1beta1/videos:annotate:\x01*'
    _globals['_FEATURE']._serialized_start = 4066
    _globals['_FEATURE']._serialized_end = 4206
    _globals['_LABELDETECTIONMODE']._serialized_start = 4208
    _globals['_LABELDETECTIONMODE']._serialized_end = 4322
    _globals['_LIKELIHOOD']._serialized_start = 4324
    _globals['_LIKELIHOOD']._serialized_end = 4440
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_start = 327
    _globals['_ANNOTATEVIDEOREQUEST']._serialized_end = 595
    _globals['_VIDEOCONTEXT']._serialized_start = 598
    _globals['_VIDEOCONTEXT']._serialized_end = 1112
    _globals['_LABELDETECTIONCONFIG']._serialized_start = 1115
    _globals['_LABELDETECTIONCONFIG']._serialized_end = 1271
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_start = 1273
    _globals['_SHOTCHANGEDETECTIONCONFIG']._serialized_end = 1315
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_start = 1317
    _globals['_EXPLICITCONTENTDETECTIONCONFIG']._serialized_end = 1364
    _globals['_VIDEOSEGMENT']._serialized_start = 1366
    _globals['_VIDEOSEGMENT']._serialized_end = 1486
    _globals['_LABELSEGMENT']._serialized_start = 1488
    _globals['_LABELSEGMENT']._serialized_end = 1595
    _globals['_LABELFRAME']._serialized_start = 1597
    _globals['_LABELFRAME']._serialized_end = 1677
    _globals['_ENTITY']._serialized_start = 1679
    _globals['_ENTITY']._serialized_end = 1750
    _globals['_LABELANNOTATION']._serialized_start = 1753
    _globals['_LABELANNOTATION']._serialized_end = 2057
    _globals['_EXPLICITCONTENTFRAME']._serialized_start = 2060
    _globals['_EXPLICITCONTENTFRAME']._serialized_end = 2216
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_start = 2218
    _globals['_EXPLICITCONTENTANNOTATION']._serialized_end = 2325
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_start = 2328
    _globals['_VIDEOANNOTATIONRESULTS']._serialized_end = 2957
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_start = 2959
    _globals['_ANNOTATEVIDEORESPONSE']._serialized_end = 3076
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_start = 3079
    _globals['_VIDEOANNOTATIONPROGRESS']._serialized_end = 3246
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_start = 3248
    _globals['_ANNOTATEVIDEOPROGRESS']._serialized_end = 3367
    _globals['_SPEECHTRANSCRIPTIONCONFIG']._serialized_start = 3370
    _globals['_SPEECHTRANSCRIPTIONCONFIG']._serialized_end = 3644
    _globals['_SPEECHCONTEXT']._serialized_start = 3646
    _globals['_SPEECHCONTEXT']._serialized_end = 3683
    _globals['_SPEECHTRANSCRIPTION']._serialized_start = 3685
    _globals['_SPEECHTRANSCRIPTION']._serialized_end = 3800
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_start = 3803
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_end = 3945
    _globals['_WORDINFO']._serialized_start = 3947
    _globals['_WORDINFO']._serialized_end = 4063
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_start = 4443
    _globals['_VIDEOINTELLIGENCESERVICE']._serialized_end = 4777