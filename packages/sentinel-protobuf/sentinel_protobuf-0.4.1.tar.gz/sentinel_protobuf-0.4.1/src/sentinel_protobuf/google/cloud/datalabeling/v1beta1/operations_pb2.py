"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/operations.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.datalabeling.v1beta1 import dataset_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2
from .....google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/datalabeling/v1beta1/operations.proto\x12!google.cloud.datalabeling.v1beta1\x1a/google/cloud/datalabeling/v1beta1/dataset.proto\x1a?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"Y\n\x1bImportDataOperationResponse\x12\x0f\n\x07dataset\x18\x01 \x01(\t\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x12\x14\n\x0cimport_count\x18\x03 \x01(\x05"\xe5\x01\n\x1bExportDataOperationResponse\x12\x0f\n\x07dataset\x18\x01 \x01(\t\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x12\x14\n\x0cexport_count\x18\x03 \x01(\x05\x12B\n\x0blabel_stats\x18\x04 \x01(\x0b2-.google.cloud.datalabeling.v1beta1.LabelStats\x12F\n\routput_config\x18\x05 \x01(\x0b2/.google.cloud.datalabeling.v1beta1.OutputConfig"\x8d\x01\n\x1bImportDataOperationMetadata\x12\x0f\n\x07dataset\x18\x01 \x01(\t\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8d\x01\n\x1bExportDataOperationMetadata\x12\x0f\n\x07dataset\x18\x01 \x01(\t\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8c\x0c\n\x16LabelOperationMetadata\x12t\n\x1cimage_classification_details\x18\x03 \x01(\x0b2L.google.cloud.datalabeling.v1beta1.LabelImageClassificationOperationMetadataH\x00\x12o\n\x1aimage_bounding_box_details\x18\x04 \x01(\x0b2I.google.cloud.datalabeling.v1beta1.LabelImageBoundingBoxOperationMetadataH\x00\x12q\n\x1bimage_bounding_poly_details\x18\x0b \x01(\x0b2J.google.cloud.datalabeling.v1beta1.LabelImageBoundingPolyOperationMetadataH\x00\x12\x80\x01\n#image_oriented_bounding_box_details\x18\x0e \x01(\x0b2Q.google.cloud.datalabeling.v1beta1.LabelImageOrientedBoundingBoxOperationMetadataH\x00\x12h\n\x16image_polyline_details\x18\x0c \x01(\x0b2F.google.cloud.datalabeling.v1beta1.LabelImagePolylineOperationMetadataH\x00\x12p\n\x1aimage_segmentation_details\x18\x0f \x01(\x0b2J.google.cloud.datalabeling.v1beta1.LabelImageSegmentationOperationMetadataH\x00\x12t\n\x1cvideo_classification_details\x18\x05 \x01(\x0b2L.google.cloud.datalabeling.v1beta1.LabelVideoClassificationOperationMetadataH\x00\x12w\n\x1evideo_object_detection_details\x18\x06 \x01(\x0b2M.google.cloud.datalabeling.v1beta1.LabelVideoObjectDetectionOperationMetadataH\x00\x12u\n\x1dvideo_object_tracking_details\x18\x07 \x01(\x0b2L.google.cloud.datalabeling.v1beta1.LabelVideoObjectTrackingOperationMetadataH\x00\x12b\n\x13video_event_details\x18\x08 \x01(\x0b2C.google.cloud.datalabeling.v1beta1.LabelVideoEventOperationMetadataH\x00\x12r\n\x1btext_classification_details\x18\t \x01(\x0b2K.google.cloud.datalabeling.v1beta1.LabelTextClassificationOperationMetadataH\x00\x12w\n\x1etext_entity_extraction_details\x18\r \x01(\x0b2M.google.cloud.datalabeling.v1beta1.LabelTextEntityExtractionOperationMetadataH\x00\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\t\n\x07details"{\n)LabelImageClassificationOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"x\n&LabelImageBoundingBoxOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"\x80\x01\n.LabelImageOrientedBoundingBoxOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"y\n\'LabelImageBoundingPolyOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"u\n#LabelImagePolylineOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"y\n\'LabelImageSegmentationOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"{\n)LabelVideoClassificationOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"|\n*LabelVideoObjectDetectionOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"{\n)LabelVideoObjectTrackingOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"r\n LabelVideoEventOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"z\n(LabelTextClassificationOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"|\n*LabelTextEntityExtractionOperationMetadata\x12N\n\x0cbasic_config\x18\x01 \x01(\x0b28.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig"\x8f\x01\n\x19CreateInstructionMetadata\x12\x13\n\x0binstruction\x18\x01 \x01(\t\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_IMPORTDATAOPERATIONRESPONSE']._serialized_start = 261
    _globals['_IMPORTDATAOPERATIONRESPONSE']._serialized_end = 350
    _globals['_EXPORTDATAOPERATIONRESPONSE']._serialized_start = 353
    _globals['_EXPORTDATAOPERATIONRESPONSE']._serialized_end = 582
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_start = 585
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_end = 726
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_start = 729
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_end = 870
    _globals['_LABELOPERATIONMETADATA']._serialized_start = 873
    _globals['_LABELOPERATIONMETADATA']._serialized_end = 2421
    _globals['_LABELIMAGECLASSIFICATIONOPERATIONMETADATA']._serialized_start = 2423
    _globals['_LABELIMAGECLASSIFICATIONOPERATIONMETADATA']._serialized_end = 2546
    _globals['_LABELIMAGEBOUNDINGBOXOPERATIONMETADATA']._serialized_start = 2548
    _globals['_LABELIMAGEBOUNDINGBOXOPERATIONMETADATA']._serialized_end = 2668
    _globals['_LABELIMAGEORIENTEDBOUNDINGBOXOPERATIONMETADATA']._serialized_start = 2671
    _globals['_LABELIMAGEORIENTEDBOUNDINGBOXOPERATIONMETADATA']._serialized_end = 2799
    _globals['_LABELIMAGEBOUNDINGPOLYOPERATIONMETADATA']._serialized_start = 2801
    _globals['_LABELIMAGEBOUNDINGPOLYOPERATIONMETADATA']._serialized_end = 2922
    _globals['_LABELIMAGEPOLYLINEOPERATIONMETADATA']._serialized_start = 2924
    _globals['_LABELIMAGEPOLYLINEOPERATIONMETADATA']._serialized_end = 3041
    _globals['_LABELIMAGESEGMENTATIONOPERATIONMETADATA']._serialized_start = 3043
    _globals['_LABELIMAGESEGMENTATIONOPERATIONMETADATA']._serialized_end = 3164
    _globals['_LABELVIDEOCLASSIFICATIONOPERATIONMETADATA']._serialized_start = 3166
    _globals['_LABELVIDEOCLASSIFICATIONOPERATIONMETADATA']._serialized_end = 3289
    _globals['_LABELVIDEOOBJECTDETECTIONOPERATIONMETADATA']._serialized_start = 3291
    _globals['_LABELVIDEOOBJECTDETECTIONOPERATIONMETADATA']._serialized_end = 3415
    _globals['_LABELVIDEOOBJECTTRACKINGOPERATIONMETADATA']._serialized_start = 3417
    _globals['_LABELVIDEOOBJECTTRACKINGOPERATIONMETADATA']._serialized_end = 3540
    _globals['_LABELVIDEOEVENTOPERATIONMETADATA']._serialized_start = 3542
    _globals['_LABELVIDEOEVENTOPERATIONMETADATA']._serialized_end = 3656
    _globals['_LABELTEXTCLASSIFICATIONOPERATIONMETADATA']._serialized_start = 3658
    _globals['_LABELTEXTCLASSIFICATIONOPERATIONMETADATA']._serialized_end = 3780
    _globals['_LABELTEXTENTITYEXTRACTIONOPERATIONMETADATA']._serialized_start = 3782
    _globals['_LABELTEXTENTITYEXTRACTIONOPERATIONMETADATA']._serialized_end = 3906
    _globals['_CREATEINSTRUCTIONMETADATA']._serialized_start = 3909
    _globals['_CREATEINSTRUCTIONMETADATA']._serialized_end = 4052