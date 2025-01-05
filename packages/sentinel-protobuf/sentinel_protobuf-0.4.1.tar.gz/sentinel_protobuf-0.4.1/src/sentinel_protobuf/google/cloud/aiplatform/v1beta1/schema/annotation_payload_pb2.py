"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/schema/annotation_payload.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.aiplatform.v1beta1.schema import annotation_spec_color_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schema_dot_annotation__spec__color__pb2
from ......google.cloud.aiplatform.v1beta1.schema import geometry_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schema_dot_geometry__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/aiplatform/v1beta1/schema/annotation_payload.proto\x12&google.cloud.aiplatform.v1beta1.schema\x1aBgoogle/cloud/aiplatform/v1beta1/schema/annotation_spec_color.proto\x1a5google/cloud/aiplatform/v1beta1/schema/geometry.proto\x1a\x1egoogle/protobuf/duration.proto"Q\n\x1dImageClassificationAnnotation\x12\x1a\n\x12annotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"\x8a\x01\n\x1aImageBoundingBoxAnnotation\x12\x1a\n\x12annotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\r\n\x05x_min\x18\x03 \x01(\x01\x12\r\n\x05x_max\x18\x04 \x01(\x01\x12\r\n\x05y_min\x18\x05 \x01(\x01\x12\r\n\x05y_max\x18\x06 \x01(\x01"\xa1\x06\n\x1bImageSegmentationAnnotation\x12m\n\x0fmask_annotation\x18\x03 \x01(\x0b2R.google.cloud.aiplatform.v1beta1.schema.ImageSegmentationAnnotation.MaskAnnotationH\x00\x12s\n\x12polygon_annotation\x18\x04 \x01(\x0b2U.google.cloud.aiplatform.v1beta1.schema.ImageSegmentationAnnotation.PolygonAnnotationH\x00\x12u\n\x13polyline_annotation\x18\x05 \x01(\x0b2V.google.cloud.aiplatform.v1beta1.schema.ImageSegmentationAnnotation.PolylineAnnotationH\x00\x1a\x83\x01\n\x0eMaskAnnotation\x12\x14\n\x0cmask_gcs_uri\x18\x01 \x01(\t\x12[\n\x16annotation_spec_colors\x18\x02 \x03(\x0b2;.google.cloud.aiplatform.v1beta1.schema.AnnotationSpecColor\x1a\x87\x01\n\x11PolygonAnnotation\x12@\n\x08vertexes\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1beta1.schema.Vertex\x12\x1a\n\x12annotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x1a\x88\x01\n\x12PolylineAnnotation\x12@\n\x08vertexes\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1beta1.schema.Vertex\x12\x1a\n\x12annotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\tB\x0c\n\nannotation"P\n\x1cTextClassificationAnnotation\x12\x1a\n\x12annotation_spec_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"\x97\x01\n\x18TextExtractionAnnotation\x12I\n\x0ctext_segment\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.schema.TextSegment\x12\x1a\n\x12annotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t"H\n\x0bTextSegment\x12\x14\n\x0cstart_offset\x18\x01 \x01(\x04\x12\x12\n\nend_offset\x18\x02 \x01(\x04\x12\x0f\n\x07content\x18\x03 \x01(\t"u\n\x17TextSentimentAnnotation\x12\x11\n\tsentiment\x18\x01 \x01(\x05\x12\x15\n\rsentiment_max\x18\x02 \x01(\x05\x12\x1a\n\x12annotation_spec_id\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t"\x9c\x01\n\x1dVideoClassificationAnnotation\x12I\n\x0ctime_segment\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.schema.TimeSegment\x12\x1a\n\x12annotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t"w\n\x0bTimeSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xd2\x01\n\x1dVideoObjectTrackingAnnotation\x12.\n\x0btime_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\r\n\x05x_min\x18\x02 \x01(\x01\x12\r\n\x05x_max\x18\x03 \x01(\x01\x12\r\n\x05y_min\x18\x04 \x01(\x01\x12\r\n\x05y_max\x18\x05 \x01(\x01\x12\x13\n\x0binstance_id\x18\x06 \x01(\x03\x12\x1a\n\x12annotation_spec_id\x18\x07 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x08 \x01(\t"\x9f\x01\n VideoActionRecognitionAnnotation\x12I\n\x0ctime_segment\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.schema.TimeSegment\x12\x1a\n\x12annotation_spec_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\tB\x89\x02\n*com.google.cloud.aiplatform.v1beta1.schemaB\x16AnnotationPayloadProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schemab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schema.annotation_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.aiplatform.v1beta1.schemaB\x16AnnotationPayloadProtoP\x01ZBcloud.google.com/go/aiplatform/apiv1beta1/schema/schemapb;schemapb\xaa\x02&Google.Cloud.AIPlatform.V1Beta1.Schema\xca\x02&Google\\Cloud\\AIPlatform\\V1beta1\\Schema\xea\x02*Google::Cloud::AIPlatform::V1beta1::Schema'
    _globals['_IMAGECLASSIFICATIONANNOTATION']._serialized_start = 262
    _globals['_IMAGECLASSIFICATIONANNOTATION']._serialized_end = 343
    _globals['_IMAGEBOUNDINGBOXANNOTATION']._serialized_start = 346
    _globals['_IMAGEBOUNDINGBOXANNOTATION']._serialized_end = 484
    _globals['_IMAGESEGMENTATIONANNOTATION']._serialized_start = 487
    _globals['_IMAGESEGMENTATIONANNOTATION']._serialized_end = 1288
    _globals['_IMAGESEGMENTATIONANNOTATION_MASKANNOTATION']._serialized_start = 866
    _globals['_IMAGESEGMENTATIONANNOTATION_MASKANNOTATION']._serialized_end = 997
    _globals['_IMAGESEGMENTATIONANNOTATION_POLYGONANNOTATION']._serialized_start = 1000
    _globals['_IMAGESEGMENTATIONANNOTATION_POLYGONANNOTATION']._serialized_end = 1135
    _globals['_IMAGESEGMENTATIONANNOTATION_POLYLINEANNOTATION']._serialized_start = 1138
    _globals['_IMAGESEGMENTATIONANNOTATION_POLYLINEANNOTATION']._serialized_end = 1274
    _globals['_TEXTCLASSIFICATIONANNOTATION']._serialized_start = 1290
    _globals['_TEXTCLASSIFICATIONANNOTATION']._serialized_end = 1370
    _globals['_TEXTEXTRACTIONANNOTATION']._serialized_start = 1373
    _globals['_TEXTEXTRACTIONANNOTATION']._serialized_end = 1524
    _globals['_TEXTSEGMENT']._serialized_start = 1526
    _globals['_TEXTSEGMENT']._serialized_end = 1598
    _globals['_TEXTSENTIMENTANNOTATION']._serialized_start = 1600
    _globals['_TEXTSENTIMENTANNOTATION']._serialized_end = 1717
    _globals['_VIDEOCLASSIFICATIONANNOTATION']._serialized_start = 1720
    _globals['_VIDEOCLASSIFICATIONANNOTATION']._serialized_end = 1876
    _globals['_TIMESEGMENT']._serialized_start = 1878
    _globals['_TIMESEGMENT']._serialized_end = 1997
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_start = 2000
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_end = 2210
    _globals['_VIDEOACTIONRECOGNITIONANNOTATION']._serialized_start = 2213
    _globals['_VIDEOACTIONRECOGNITIONANNOTATION']._serialized_end = 2372