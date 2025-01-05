"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/human_annotation_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto"\xd4\x02\n\x15HumanAnnotationConfig\x12\x18\n\x0binstruction\x18\x01 \x01(\tB\x03\xe0A\x02\x12+\n\x1eannotated_dataset_display_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12*\n\x1dannotated_dataset_description\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0blabel_group\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rreplica_count\x18\x06 \x01(\x05B\x03\xe0A\x01\x129\n\x11question_duration\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12\x1f\n\x12contributor_emails\x18\t \x03(\tB\x03\xe0A\x01\x12\x1a\n\x12user_email_address\x18\n \x01(\t"\xbd\x01\n\x19ImageClassificationConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11allow_multi_label\x18\x02 \x01(\x08B\x03\xe0A\x01\x12^\n\x17answer_aggregation_type\x18\x03 \x01(\x0e28.google.cloud.datalabeling.v1beta1.StringAggregationTypeB\x03\xe0A\x01"X\n\x12BoundingPolyConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13instruction_message\x18\x02 \x01(\tB\x03\xe0A\x01"T\n\x0ePolylineConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13instruction_message\x18\x02 \x01(\tB\x03\xe0A\x01"S\n\x12SegmentationConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x13instruction_message\x18\x02 \x01(\t"\x9b\x02\n\x19VideoClassificationConfig\x12~\n\x1bannotation_spec_set_configs\x18\x01 \x03(\x0b2T.google.cloud.datalabeling.v1beta1.VideoClassificationConfig.AnnotationSpecSetConfigB\x03\xe0A\x02\x12!\n\x14apply_shot_detection\x18\x02 \x01(\x08B\x03\xe0A\x01\x1a[\n\x17AnnotationSpecSetConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11allow_multi_label\x18\x02 \x01(\x08B\x03\xe0A\x01"]\n\x15ObjectDetectionConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02\x12"\n\x15extraction_frame_rate\x18\x03 \x01(\x01B\x03\xe0A\x02"8\n\x14ObjectTrackingConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02"0\n\x0bEventConfig\x12!\n\x14annotation_spec_sets\x18\x01 \x03(\tB\x03\xe0A\x02"\xaf\x01\n\x18TextClassificationConfig\x12\x1e\n\x11allow_multi_label\x18\x01 \x01(\x08B\x03\xe0A\x01\x12 \n\x13annotation_spec_set\x18\x02 \x01(\tB\x03\xe0A\x02\x12Q\n\x10sentiment_config\x18\x03 \x01(\x0b22.google.cloud.datalabeling.v1beta1.SentimentConfigB\x03\xe0A\x01";\n\x0fSentimentConfig\x12(\n enable_label_sentiment_selection\x18\x01 \x01(\x08">\n\x1aTextEntityExtractionConfig\x12 \n\x13annotation_spec_set\x18\x01 \x01(\tB\x03\xe0A\x02*{\n\x15StringAggregationType\x12\'\n#STRING_AGGREGATION_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMAJORITY_VOTE\x10\x01\x12\x12\n\x0eUNANIMOUS_VOTE\x10\x02\x12\x12\n\x0eNO_AGGREGATION\x10\x03B\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.human_annotation_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['instruction']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['instruction']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['annotated_dataset_display_name']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['annotated_dataset_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['annotated_dataset_description']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['annotated_dataset_description']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['label_group']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['label_group']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['language_code']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['replica_count']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['question_duration']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['question_duration']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['contributor_emails']._loaded_options = None
    _globals['_HUMANANNOTATIONCONFIG'].fields_by_name['contributor_emails']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['allow_multi_label']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['allow_multi_label']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['answer_aggregation_type']._loaded_options = None
    _globals['_IMAGECLASSIFICATIONCONFIG'].fields_by_name['answer_aggregation_type']._serialized_options = b'\xe0A\x01'
    _globals['_BOUNDINGPOLYCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_BOUNDINGPOLYCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_BOUNDINGPOLYCONFIG'].fields_by_name['instruction_message']._loaded_options = None
    _globals['_BOUNDINGPOLYCONFIG'].fields_by_name['instruction_message']._serialized_options = b'\xe0A\x01'
    _globals['_POLYLINECONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_POLYLINECONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_POLYLINECONFIG'].fields_by_name['instruction_message']._loaded_options = None
    _globals['_POLYLINECONFIG'].fields_by_name['instruction_message']._serialized_options = b'\xe0A\x01'
    _globals['_SEGMENTATIONCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_SEGMENTATIONCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG'].fields_by_name['allow_multi_label']._loaded_options = None
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG'].fields_by_name['allow_multi_label']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOCLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set_configs']._loaded_options = None
    _globals['_VIDEOCLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set_configs']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOCLASSIFICATIONCONFIG'].fields_by_name['apply_shot_detection']._loaded_options = None
    _globals['_VIDEOCLASSIFICATIONCONFIG'].fields_by_name['apply_shot_detection']._serialized_options = b'\xe0A\x01'
    _globals['_OBJECTDETECTIONCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_OBJECTDETECTIONCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_OBJECTDETECTIONCONFIG'].fields_by_name['extraction_frame_rate']._loaded_options = None
    _globals['_OBJECTDETECTIONCONFIG'].fields_by_name['extraction_frame_rate']._serialized_options = b'\xe0A\x02'
    _globals['_OBJECTTRACKINGCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_OBJECTTRACKINGCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTCONFIG'].fields_by_name['annotation_spec_sets']._loaded_options = None
    _globals['_EVENTCONFIG'].fields_by_name['annotation_spec_sets']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['allow_multi_label']._loaded_options = None
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['allow_multi_label']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['sentiment_config']._loaded_options = None
    _globals['_TEXTCLASSIFICATIONCONFIG'].fields_by_name['sentiment_config']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTENTITYEXTRACTIONCONFIG'].fields_by_name['annotation_spec_set']._loaded_options = None
    _globals['_TEXTENTITYEXTRACTIONCONFIG'].fields_by_name['annotation_spec_set']._serialized_options = b'\xe0A\x02'
    _globals['_STRINGAGGREGATIONTYPE']._serialized_start = 1755
    _globals['_STRINGAGGREGATIONTYPE']._serialized_end = 1878
    _globals['_HUMANANNOTATIONCONFIG']._serialized_start = 168
    _globals['_HUMANANNOTATIONCONFIG']._serialized_end = 508
    _globals['_IMAGECLASSIFICATIONCONFIG']._serialized_start = 511
    _globals['_IMAGECLASSIFICATIONCONFIG']._serialized_end = 700
    _globals['_BOUNDINGPOLYCONFIG']._serialized_start = 702
    _globals['_BOUNDINGPOLYCONFIG']._serialized_end = 790
    _globals['_POLYLINECONFIG']._serialized_start = 792
    _globals['_POLYLINECONFIG']._serialized_end = 876
    _globals['_SEGMENTATIONCONFIG']._serialized_start = 878
    _globals['_SEGMENTATIONCONFIG']._serialized_end = 961
    _globals['_VIDEOCLASSIFICATIONCONFIG']._serialized_start = 964
    _globals['_VIDEOCLASSIFICATIONCONFIG']._serialized_end = 1247
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG']._serialized_start = 1156
    _globals['_VIDEOCLASSIFICATIONCONFIG_ANNOTATIONSPECSETCONFIG']._serialized_end = 1247
    _globals['_OBJECTDETECTIONCONFIG']._serialized_start = 1249
    _globals['_OBJECTDETECTIONCONFIG']._serialized_end = 1342
    _globals['_OBJECTTRACKINGCONFIG']._serialized_start = 1344
    _globals['_OBJECTTRACKINGCONFIG']._serialized_end = 1400
    _globals['_EVENTCONFIG']._serialized_start = 1402
    _globals['_EVENTCONFIG']._serialized_end = 1450
    _globals['_TEXTCLASSIFICATIONCONFIG']._serialized_start = 1453
    _globals['_TEXTCLASSIFICATIONCONFIG']._serialized_end = 1628
    _globals['_SENTIMENTCONFIG']._serialized_start = 1630
    _globals['_SENTIMENTCONFIG']._serialized_end = 1689
    _globals['_TEXTENTITYEXTRACTIONCONFIG']._serialized_start = 1691
    _globals['_TEXTENTITYEXTRACTIONCONFIG']._serialized_end = 1753