"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_annotation__spec__set__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/datalabeling/v1beta1/annotation.proto\x12!google.cloud.datalabeling.v1beta1\x1a;google/cloud/datalabeling/v1beta1/annotation_spec_set.proto\x1a\x1egoogle/protobuf/duration.proto"\xe2\x02\n\nAnnotation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x11annotation_source\x18\x02 \x01(\x0e23.google.cloud.datalabeling.v1beta1.AnnotationSource\x12L\n\x10annotation_value\x18\x03 \x01(\x0b22.google.cloud.datalabeling.v1beta1.AnnotationValue\x12R\n\x13annotation_metadata\x18\x04 \x01(\x0b25.google.cloud.datalabeling.v1beta1.AnnotationMetadata\x12T\n\x14annotation_sentiment\x18\x06 \x01(\x0e26.google.cloud.datalabeling.v1beta1.AnnotationSentiment"\xd1\x07\n\x0fAnnotationValue\x12k\n\x1fimage_classification_annotation\x18\x01 \x01(\x0b2@.google.cloud.datalabeling.v1beta1.ImageClassificationAnnotationH\x00\x12h\n\x1eimage_bounding_poly_annotation\x18\x02 \x01(\x0b2>.google.cloud.datalabeling.v1beta1.ImageBoundingPolyAnnotationH\x00\x12_\n\x19image_polyline_annotation\x18\x08 \x01(\x0b2:.google.cloud.datalabeling.v1beta1.ImagePolylineAnnotationH\x00\x12g\n\x1dimage_segmentation_annotation\x18\t \x01(\x0b2>.google.cloud.datalabeling.v1beta1.ImageSegmentationAnnotationH\x00\x12i\n\x1etext_classification_annotation\x18\x03 \x01(\x0b2?.google.cloud.datalabeling.v1beta1.TextClassificationAnnotationH\x00\x12n\n!text_entity_extraction_annotation\x18\n \x01(\x0b2A.google.cloud.datalabeling.v1beta1.TextEntityExtractionAnnotationH\x00\x12k\n\x1fvideo_classification_annotation\x18\x04 \x01(\x0b2@.google.cloud.datalabeling.v1beta1.VideoClassificationAnnotationH\x00\x12l\n video_object_tracking_annotation\x18\x05 \x01(\x0b2@.google.cloud.datalabeling.v1beta1.VideoObjectTrackingAnnotationH\x00\x12Y\n\x16video_event_annotation\x18\x06 \x01(\x0b27.google.cloud.datalabeling.v1beta1.VideoEventAnnotationH\x00B\x0c\n\nvalue_type"k\n\x1dImageClassificationAnnotation\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"K\n\x0cBoundingPoly\x12;\n\x08vertices\x18\x01 \x03(\x0b2).google.cloud.datalabeling.v1beta1.Vertex"j\n\x16NormalizedBoundingPoly\x12P\n\x13normalized_vertices\x18\x01 \x03(\x0b23.google.cloud.datalabeling.v1beta1.NormalizedVertex"\xa2\x02\n\x1bImageBoundingPolyAnnotation\x12H\n\rbounding_poly\x18\x02 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.BoundingPolyH\x00\x12]\n\x18normalized_bounding_poly\x18\x03 \x01(\x0b29.google.cloud.datalabeling.v1beta1.NormalizedBoundingPolyH\x00\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpecB\x0e\n\x0cbounded_area"G\n\x08Polyline\x12;\n\x08vertices\x18\x01 \x03(\x0b2).google.cloud.datalabeling.v1beta1.Vertex"f\n\x12NormalizedPolyline\x12P\n\x13normalized_vertices\x18\x01 \x03(\x0b23.google.cloud.datalabeling.v1beta1.NormalizedVertex"\x84\x02\n\x17ImagePolylineAnnotation\x12?\n\x08polyline\x18\x02 \x01(\x0b2+.google.cloud.datalabeling.v1beta1.PolylineH\x00\x12T\n\x13normalized_polyline\x18\x03 \x01(\x0b25.google.cloud.datalabeling.v1beta1.NormalizedPolylineH\x00\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpecB\x06\n\x04poly"\xa2\x02\n\x1bImageSegmentationAnnotation\x12o\n\x11annotation_colors\x18\x01 \x03(\x0b2T.google.cloud.datalabeling.v1beta1.ImageSegmentationAnnotation.AnnotationColorsEntry\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x13\n\x0bimage_bytes\x18\x03 \x01(\x0c\x1aj\n\x15AnnotationColorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec:\x028\x01"j\n\x1cTextClassificationAnnotation\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec"\xbe\x01\n\x1eTextEntityExtractionAnnotation\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12P\n\x12sequential_segment\x18\x02 \x01(\x0b24.google.cloud.datalabeling.v1beta1.SequentialSegment"/\n\x11SequentialSegment\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03end\x18\x02 \x01(\x05"w\n\x0bTimeSegment\x124\n\x11start_time_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fend_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xb1\x01\n\x1dVideoClassificationAnnotation\x12D\n\x0ctime_segment\x18\x01 \x01(\x0b2..google.cloud.datalabeling.v1beta1.TimeSegment\x12J\n\x0fannotation_spec\x18\x02 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec"\xfe\x01\n\x13ObjectTrackingFrame\x12H\n\rbounding_poly\x18\x01 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.BoundingPolyH\x00\x12]\n\x18normalized_bounding_poly\x18\x02 \x01(\x0b29.google.cloud.datalabeling.v1beta1.NormalizedBoundingPolyH\x00\x12.\n\x0btime_offset\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x0e\n\x0cbounded_area"\x89\x02\n\x1dVideoObjectTrackingAnnotation\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12D\n\x0ctime_segment\x18\x02 \x01(\x0b2..google.cloud.datalabeling.v1beta1.TimeSegment\x12V\n\x16object_tracking_frames\x18\x03 \x03(\x0b26.google.cloud.datalabeling.v1beta1.ObjectTrackingFrame"\xa8\x01\n\x14VideoEventAnnotation\x12J\n\x0fannotation_spec\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.AnnotationSpec\x12D\n\x0ctime_segment\x18\x02 \x01(\x0b2..google.cloud.datalabeling.v1beta1.TimeSegment"d\n\x12AnnotationMetadata\x12N\n\x11operator_metadata\x18\x02 \x01(\x0b23.google.cloud.datalabeling.v1beta1.OperatorMetadata"]\n\x10OperatorMetadata\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x13\n\x0btotal_votes\x18\x02 \x01(\x05\x12\x13\n\x0blabel_votes\x18\x03 \x01(\x05\x12\x10\n\x08comments\x18\x04 \x03(\t*C\n\x10AnnotationSource\x12!\n\x1dANNOTATION_SOURCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08OPERATOR\x10\x03*W\n\x13AnnotationSentiment\x12$\n ANNOTATION_SENTIMENT_UNSPECIFIED\x10\x00\x12\x0c\n\x08NEGATIVE\x10\x01\x12\x0c\n\x08POSITIVE\x10\x02*\x91\x04\n\x0eAnnotationType\x12\x1f\n\x1bANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fIMAGE_CLASSIFICATION_ANNOTATION\x10\x01\x12!\n\x1dIMAGE_BOUNDING_BOX_ANNOTATION\x10\x02\x12*\n&IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION\x10\r\x12"\n\x1eIMAGE_BOUNDING_POLY_ANNOTATION\x10\n\x12\x1d\n\x19IMAGE_POLYLINE_ANNOTATION\x10\x0b\x12!\n\x1dIMAGE_SEGMENTATION_ANNOTATION\x10\x0c\x12)\n%VIDEO_SHOTS_CLASSIFICATION_ANNOTATION\x10\x03\x12$\n VIDEO_OBJECT_TRACKING_ANNOTATION\x10\x04\x12%\n!VIDEO_OBJECT_DETECTION_ANNOTATION\x10\x05\x12\x1a\n\x16VIDEO_EVENT_ANNOTATION\x10\x06\x12"\n\x1eTEXT_CLASSIFICATION_ANNOTATION\x10\x08\x12%\n!TEXT_ENTITY_EXTRACTION_ANNOTATION\x10\t\x12%\n!GENERAL_CLASSIFICATION_ANNOTATION\x10\x0eB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_IMAGESEGMENTATIONANNOTATION_ANNOTATIONCOLORSENTRY']._loaded_options = None
    _globals['_IMAGESEGMENTATIONANNOTATION_ANNOTATIONCOLORSENTRY']._serialized_options = b'8\x01'
    _globals['_ANNOTATIONSOURCE']._serialized_start = 4457
    _globals['_ANNOTATIONSOURCE']._serialized_end = 4524
    _globals['_ANNOTATIONSENTIMENT']._serialized_start = 4526
    _globals['_ANNOTATIONSENTIMENT']._serialized_end = 4613
    _globals['_ANNOTATIONTYPE']._serialized_start = 4616
    _globals['_ANNOTATIONTYPE']._serialized_end = 5145
    _globals['_ANNOTATION']._serialized_start = 183
    _globals['_ANNOTATION']._serialized_end = 537
    _globals['_ANNOTATIONVALUE']._serialized_start = 540
    _globals['_ANNOTATIONVALUE']._serialized_end = 1517
    _globals['_IMAGECLASSIFICATIONANNOTATION']._serialized_start = 1519
    _globals['_IMAGECLASSIFICATIONANNOTATION']._serialized_end = 1626
    _globals['_VERTEX']._serialized_start = 1628
    _globals['_VERTEX']._serialized_end = 1658
    _globals['_NORMALIZEDVERTEX']._serialized_start = 1660
    _globals['_NORMALIZEDVERTEX']._serialized_end = 1700
    _globals['_BOUNDINGPOLY']._serialized_start = 1702
    _globals['_BOUNDINGPOLY']._serialized_end = 1777
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_start = 1779
    _globals['_NORMALIZEDBOUNDINGPOLY']._serialized_end = 1885
    _globals['_IMAGEBOUNDINGPOLYANNOTATION']._serialized_start = 1888
    _globals['_IMAGEBOUNDINGPOLYANNOTATION']._serialized_end = 2178
    _globals['_POLYLINE']._serialized_start = 2180
    _globals['_POLYLINE']._serialized_end = 2251
    _globals['_NORMALIZEDPOLYLINE']._serialized_start = 2253
    _globals['_NORMALIZEDPOLYLINE']._serialized_end = 2355
    _globals['_IMAGEPOLYLINEANNOTATION']._serialized_start = 2358
    _globals['_IMAGEPOLYLINEANNOTATION']._serialized_end = 2618
    _globals['_IMAGESEGMENTATIONANNOTATION']._serialized_start = 2621
    _globals['_IMAGESEGMENTATIONANNOTATION']._serialized_end = 2911
    _globals['_IMAGESEGMENTATIONANNOTATION_ANNOTATIONCOLORSENTRY']._serialized_start = 2805
    _globals['_IMAGESEGMENTATIONANNOTATION_ANNOTATIONCOLORSENTRY']._serialized_end = 2911
    _globals['_TEXTCLASSIFICATIONANNOTATION']._serialized_start = 2913
    _globals['_TEXTCLASSIFICATIONANNOTATION']._serialized_end = 3019
    _globals['_TEXTENTITYEXTRACTIONANNOTATION']._serialized_start = 3022
    _globals['_TEXTENTITYEXTRACTIONANNOTATION']._serialized_end = 3212
    _globals['_SEQUENTIALSEGMENT']._serialized_start = 3214
    _globals['_SEQUENTIALSEGMENT']._serialized_end = 3261
    _globals['_TIMESEGMENT']._serialized_start = 3263
    _globals['_TIMESEGMENT']._serialized_end = 3382
    _globals['_VIDEOCLASSIFICATIONANNOTATION']._serialized_start = 3385
    _globals['_VIDEOCLASSIFICATIONANNOTATION']._serialized_end = 3562
    _globals['_OBJECTTRACKINGFRAME']._serialized_start = 3565
    _globals['_OBJECTTRACKINGFRAME']._serialized_end = 3819
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_start = 3822
    _globals['_VIDEOOBJECTTRACKINGANNOTATION']._serialized_end = 4087
    _globals['_VIDEOEVENTANNOTATION']._serialized_start = 4090
    _globals['_VIDEOEVENTANNOTATION']._serialized_end = 4258
    _globals['_ANNOTATIONMETADATA']._serialized_start = 4260
    _globals['_ANNOTATIONMETADATA']._serialized_end = 4360
    _globals['_OPERATORMETADATA']._serialized_start = 4362
    _globals['_OPERATORMETADATA']._serialized_end = 4455