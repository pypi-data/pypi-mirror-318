"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datalabeling.v1beta1 import annotation_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_annotation__pb2
from .....google.cloud.datalabeling.v1beta1 import annotation_spec_set_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_annotation__spec__set__pb2
from .....google.cloud.datalabeling.v1beta1 import data_payloads_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_data__payloads__pb2
from .....google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/datalabeling/v1beta1/dataset.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x19google/api/resource.proto\x1a2google/cloud/datalabeling/v1beta1/annotation.proto\x1a;google/cloud/datalabeling/v1beta1/annotation_spec_set.proto\x1a5google/cloud/datalabeling/v1beta1/data_payloads.proto\x1a?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc0\x02\n\x07Dataset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\rinput_configs\x18\x05 \x03(\x0b2..google.cloud.datalabeling.v1beta1.InputConfig\x12\x1a\n\x12blocking_resources\x18\x06 \x03(\t\x12\x17\n\x0fdata_item_count\x18\x07 \x01(\x03:O\xeaAL\n#datalabeling.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}"\xf1\x03\n\x0bInputConfig\x12H\n\rtext_metadata\x18\x06 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.TextMetadataH\x00\x12B\n\ngcs_source\x18\x02 \x01(\x0b2,.google.cloud.datalabeling.v1beta1.GcsSourceH\x01\x12L\n\x0fbigquery_source\x18\x05 \x01(\x0b21.google.cloud.datalabeling.v1beta1.BigQuerySourceH\x01\x12>\n\tdata_type\x18\x01 \x01(\x0e2+.google.cloud.datalabeling.v1beta1.DataType\x12J\n\x0fannotation_type\x18\x03 \x01(\x0e21.google.cloud.datalabeling.v1beta1.AnnotationType\x12Z\n\x17classification_metadata\x18\x04 \x01(\x0b29.google.cloud.datalabeling.v1beta1.ClassificationMetadataB\x14\n\x12data_type_metadataB\x08\n\x06source"%\n\x0cTextMetadata\x12\x15\n\rlanguage_code\x18\x01 \x01(\t"0\n\x16ClassificationMetadata\x12\x16\n\x0eis_multi_label\x18\x01 \x01(\x08"1\n\tGcsSource\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t"#\n\x0eBigQuerySource\x12\x11\n\tinput_uri\x18\x01 \x01(\t"\xc6\x01\n\x0cOutputConfig\x12L\n\x0fgcs_destination\x18\x01 \x01(\x0b21.google.cloud.datalabeling.v1beta1.GcsDestinationH\x00\x12Y\n\x16gcs_folder_destination\x18\x02 \x01(\x0b27.google.cloud.datalabeling.v1beta1.GcsFolderDestinationH\x00B\r\n\x0bdestination"7\n\x0eGcsDestination\x12\x12\n\noutput_uri\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t"1\n\x14GcsFolderDestination\x12\x19\n\x11output_folder_uri\x18\x01 \x01(\t"\xe7\x02\n\x08DataItem\x12H\n\rimage_payload\x18\x02 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.ImagePayloadH\x00\x12F\n\x0ctext_payload\x18\x03 \x01(\x0b2..google.cloud.datalabeling.v1beta1.TextPayloadH\x00\x12H\n\rvideo_payload\x18\x04 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.VideoPayloadH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t:f\xeaAc\n$datalabeling.googleapis.com/DataItem\x12;projects/{project}/datasets/{dataset}/dataItems/{data_item}B\t\n\x07payload"\xff\x04\n\x10AnnotatedDataset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\t \x01(\t\x12N\n\x11annotation_source\x18\x03 \x01(\x0e23.google.cloud.datalabeling.v1beta1.AnnotationSource\x12J\n\x0fannotation_type\x18\x08 \x01(\x0e21.google.cloud.datalabeling.v1beta1.AnnotationType\x12\x15\n\rexample_count\x18\x04 \x01(\x03\x12\x1f\n\x17completed_example_count\x18\x05 \x01(\x03\x12B\n\x0blabel_stats\x18\x06 \x01(\x0b2-.google.cloud.datalabeling.v1beta1.LabelStats\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12M\n\x08metadata\x18\n \x01(\x0b2;.google.cloud.datalabeling.v1beta1.AnnotatedDatasetMetadata\x12\x1a\n\x12blocking_resources\x18\x0b \x03(\t:~\xeaA{\n,datalabeling.googleapis.com/AnnotatedDataset\x12Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}"\x99\x01\n\nLabelStats\x12V\n\rexample_count\x18\x01 \x03(\x0b2?.google.cloud.datalabeling.v1beta1.LabelStats.ExampleCountEntry\x1a3\n\x11ExampleCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01"\xa2\x08\n\x18AnnotatedDatasetMetadata\x12c\n\x1bimage_classification_config\x18\x02 \x01(\x0b2<.google.cloud.datalabeling.v1beta1.ImageClassificationConfigH\x00\x12U\n\x14bounding_poly_config\x18\x03 \x01(\x0b25.google.cloud.datalabeling.v1beta1.BoundingPolyConfigH\x00\x12L\n\x0fpolyline_config\x18\x04 \x01(\x0b21.google.cloud.datalabeling.v1beta1.PolylineConfigH\x00\x12T\n\x13segmentation_config\x18\x05 \x01(\x0b25.google.cloud.datalabeling.v1beta1.SegmentationConfigH\x00\x12c\n\x1bvideo_classification_config\x18\x06 \x01(\x0b2<.google.cloud.datalabeling.v1beta1.VideoClassificationConfigH\x00\x12[\n\x17object_detection_config\x18\x07 \x01(\x0b28.google.cloud.datalabeling.v1beta1.ObjectDetectionConfigH\x00\x12Y\n\x16object_tracking_config\x18\x08 \x01(\x0b27.google.cloud.datalabeling.v1beta1.ObjectTrackingConfigH\x00\x12F\n\x0cevent_config\x18\t \x01(\x0b2..google.cloud.datalabeling.v1beta1.EventConfigH\x00\x12a\n\x1atext_classification_config\x18\n \x01(\x0b2;.google.cloud.datalabeling.v1beta1.TextClassificationConfigH\x00\x12f\n\x1dtext_entity_extraction_config\x18\x0b \x01(\x0b2=.google.cloud.datalabeling.v1beta1.TextEntityExtractionConfigH\x00\x12Y\n\x17human_annotation_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigB\x1b\n\x19annotation_request_config"\xce\x03\n\x07Example\x12H\n\rimage_payload\x18\x02 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.ImagePayloadH\x00\x12F\n\x0ctext_payload\x18\x06 \x01(\x0b2..google.cloud.datalabeling.v1beta1.TextPayloadH\x00\x12H\n\rvideo_payload\x18\x07 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.VideoPayloadH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12B\n\x0bannotations\x18\x05 \x03(\x0b2-.google.cloud.datalabeling.v1beta1.Annotation:\x89\x01\xeaA\x85\x01\n#datalabeling.googleapis.com/Example\x12^projects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}/examples/{example}B\t\n\x07payload*W\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\t\n\x05VIDEO\x10\x02\x12\x08\n\x04TEXT\x10\x04\x12\x10\n\x0cGENERAL_DATA\x10\x06B\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaAL\n#datalabeling.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}'
    _globals['_DATAITEM']._loaded_options = None
    _globals['_DATAITEM']._serialized_options = b'\xeaAc\n$datalabeling.googleapis.com/DataItem\x12;projects/{project}/datasets/{dataset}/dataItems/{data_item}'
    _globals['_ANNOTATEDDATASET']._loaded_options = None
    _globals['_ANNOTATEDDATASET']._serialized_options = b'\xeaA{\n,datalabeling.googleapis.com/AnnotatedDataset\x12Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}'
    _globals['_LABELSTATS_EXAMPLECOUNTENTRY']._loaded_options = None
    _globals['_LABELSTATS_EXAMPLECOUNTENTRY']._serialized_options = b'8\x01'
    _globals['_EXAMPLE']._loaded_options = None
    _globals['_EXAMPLE']._serialized_options = b'\xeaA\x85\x01\n#datalabeling.googleapis.com/Example\x12^projects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}/examples/{example}'
    _globals['_DATATYPE']._serialized_start = 4374
    _globals['_DATATYPE']._serialized_end = 4461
    _globals['_DATASET']._serialized_start = 380
    _globals['_DATASET']._serialized_end = 700
    _globals['_INPUTCONFIG']._serialized_start = 703
    _globals['_INPUTCONFIG']._serialized_end = 1200
    _globals['_TEXTMETADATA']._serialized_start = 1202
    _globals['_TEXTMETADATA']._serialized_end = 1239
    _globals['_CLASSIFICATIONMETADATA']._serialized_start = 1241
    _globals['_CLASSIFICATIONMETADATA']._serialized_end = 1289
    _globals['_GCSSOURCE']._serialized_start = 1291
    _globals['_GCSSOURCE']._serialized_end = 1340
    _globals['_BIGQUERYSOURCE']._serialized_start = 1342
    _globals['_BIGQUERYSOURCE']._serialized_end = 1377
    _globals['_OUTPUTCONFIG']._serialized_start = 1380
    _globals['_OUTPUTCONFIG']._serialized_end = 1578
    _globals['_GCSDESTINATION']._serialized_start = 1580
    _globals['_GCSDESTINATION']._serialized_end = 1635
    _globals['_GCSFOLDERDESTINATION']._serialized_start = 1637
    _globals['_GCSFOLDERDESTINATION']._serialized_end = 1686
    _globals['_DATAITEM']._serialized_start = 1689
    _globals['_DATAITEM']._serialized_end = 2048
    _globals['_ANNOTATEDDATASET']._serialized_start = 2051
    _globals['_ANNOTATEDDATASET']._serialized_end = 2690
    _globals['_LABELSTATS']._serialized_start = 2693
    _globals['_LABELSTATS']._serialized_end = 2846
    _globals['_LABELSTATS_EXAMPLECOUNTENTRY']._serialized_start = 2795
    _globals['_LABELSTATS_EXAMPLECOUNTENTRY']._serialized_end = 2846
    _globals['_ANNOTATEDDATASETMETADATA']._serialized_start = 2849
    _globals['_ANNOTATEDDATASETMETADATA']._serialized_end = 3907
    _globals['_EXAMPLE']._serialized_start = 3910
    _globals['_EXAMPLE']._serialized_end = 4372