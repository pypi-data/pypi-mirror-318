"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/annotations.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/genomics/v1/annotations.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xa1\x02\n\rAnnotationSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x120\n\x04type\x18\x06 \x01(\x0e2".google.genomics.v1.AnnotationType\x129\n\x04info\x18\x11 \x03(\x0b2+.google.genomics.v1.AnnotationSet.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"\xcf\x03\n\nAnnotation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11annotation_set_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0creference_id\x18\x04 \x01(\t\x12\x16\n\x0ereference_name\x18\x05 \x01(\t\x12\r\n\x05start\x18\x06 \x01(\x03\x12\x0b\n\x03end\x18\x07 \x01(\x03\x12\x16\n\x0ereverse_strand\x18\x08 \x01(\x08\x120\n\x04type\x18\t \x01(\x0e2".google.genomics.v1.AnnotationType\x128\n\x07variant\x18\n \x01(\x0b2%.google.genomics.v1.VariantAnnotationH\x00\x124\n\ntranscript\x18\x0b \x01(\x0b2\x1e.google.genomics.v1.TranscriptH\x00\x126\n\x04info\x18\x0c \x03(\x0b2(.google.genomics.v1.Annotation.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01B\x07\n\x05value"\xfc\x08\n\x11VariantAnnotation\x128\n\x04type\x18\x01 \x01(\x0e2*.google.genomics.v1.VariantAnnotation.Type\x12<\n\x06effect\x18\x02 \x01(\x0e2,.google.genomics.v1.VariantAnnotation.Effect\x12\x17\n\x0falternate_bases\x18\x03 \x01(\t\x12\x0f\n\x07gene_id\x18\x04 \x01(\t\x12\x16\n\x0etranscript_ids\x18\x05 \x03(\t\x12K\n\nconditions\x18\x06 \x03(\x0b27.google.genomics.v1.VariantAnnotation.ClinicalCondition\x12Y\n\x15clinical_significance\x18\x07 \x01(\x0e2:.google.genomics.v1.VariantAnnotation.ClinicalSignificance\x1a}\n\x11ClinicalCondition\x12\r\n\x05names\x18\x01 \x03(\t\x124\n\x0cexternal_ids\x18\x02 \x03(\x0b2\x1e.google.genomics.v1.ExternalId\x12\x12\n\nconcept_id\x18\x03 \x01(\t\x12\x0f\n\x07omim_id\x18\x04 \x01(\t"}\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_OTHER\x10\x01\x12\r\n\tINSERTION\x10\x02\x12\x0c\n\x08DELETION\x10\x03\x12\x10\n\x0cSUBSTITUTION\x10\x04\x12\x07\n\x03SNP\x10\x05\x12\x0e\n\nSTRUCTURAL\x10\x06\x12\x07\n\x03CNV\x10\x07"\xc3\x01\n\x06Effect\x12\x16\n\x12EFFECT_UNSPECIFIED\x10\x00\x12\x10\n\x0cEFFECT_OTHER\x10\x01\x12\x0e\n\nFRAMESHIFT\x10\x02\x12\x1a\n\x16FRAME_PRESERVING_INDEL\x10\x03\x12\x12\n\x0eSYNONYMOUS_SNP\x10\x04\x12\x15\n\x11NONSYNONYMOUS_SNP\x10\x05\x12\r\n\tSTOP_GAIN\x10\x06\x12\r\n\tSTOP_LOSS\x10\x07\x12\x1a\n\x16SPLICE_SITE_DISRUPTION\x10\x08"\xc0\x02\n\x14ClinicalSignificance\x12%\n!CLINICAL_SIGNIFICANCE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bCLINICAL_SIGNIFICANCE_OTHER\x10\x01\x12\r\n\tUNCERTAIN\x10\x02\x12\n\n\x06BENIGN\x10\x03\x12\x11\n\rLIKELY_BENIGN\x10\x04\x12\x15\n\x11LIKELY_PATHOGENIC\x10\x05\x12\x0e\n\nPATHOGENIC\x10\x06\x12\x11\n\rDRUG_RESPONSE\x10\x07\x12\x16\n\x12HISTOCOMPATIBILITY\x10\x08\x12\x17\n\x13CONFERS_SENSITIVITY\x10\t\x12\x0f\n\x0bRISK_FACTOR\x10\n\x12\x0f\n\x0bASSOCIATION\x10\x0b\x12\x0e\n\nPROTECTIVE\x10\x0c\x12\x15\n\x11MULTIPLE_REPORTED\x10\r"\x97\x02\n\nTranscript\x12\x0f\n\x07gene_id\x18\x01 \x01(\t\x122\n\x05exons\x18\x02 \x03(\x0b2#.google.genomics.v1.Transcript.Exon\x12F\n\x0fcoding_sequence\x18\x03 \x01(\x0b2-.google.genomics.v1.Transcript.CodingSequence\x1aN\n\x04Exon\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03end\x18\x02 \x01(\x03\x12*\n\x05frame\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int32Value\x1a,\n\x0eCodingSequence\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03end\x18\x02 \x01(\x03"-\n\nExternalId\x12\x13\n\x0bsource_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t"W\n\x1aCreateAnnotationSetRequest\x129\n\x0eannotation_set\x18\x01 \x01(\x0b2!.google.genomics.v1.AnnotationSet"4\n\x17GetAnnotationSetRequest\x12\x19\n\x11annotation_set_id\x18\x01 \x01(\t"\xa3\x01\n\x1aUpdateAnnotationSetRequest\x12\x19\n\x11annotation_set_id\x18\x01 \x01(\t\x129\n\x0eannotation_set\x18\x02 \x01(\x0b2!.google.genomics.v1.AnnotationSet\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"7\n\x1aDeleteAnnotationSetRequest\x12\x19\n\x11annotation_set_id\x18\x01 \x01(\t"\xb4\x01\n\x1bSearchAnnotationSetsRequest\x12\x13\n\x0bdataset_ids\x18\x01 \x03(\t\x12\x18\n\x10reference_set_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x121\n\x05types\x18\x04 \x03(\x0e2".google.genomics.v1.AnnotationType\x12\x12\n\npage_token\x18\x05 \x01(\t\x12\x11\n\tpage_size\x18\x06 \x01(\x05"s\n\x1cSearchAnnotationSetsResponse\x12:\n\x0fannotation_sets\x18\x01 \x03(\x0b2!.google.genomics.v1.AnnotationSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"M\n\x17CreateAnnotationRequest\x122\n\nannotation\x18\x01 \x01(\x0b2\x1e.google.genomics.v1.Annotation"h\n\x1dBatchCreateAnnotationsRequest\x123\n\x0bannotations\x18\x01 \x03(\x0b2\x1e.google.genomics.v1.Annotation\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\xcc\x01\n\x1eBatchCreateAnnotationsResponse\x12I\n\x07entries\x18\x01 \x03(\x0b28.google.genomics.v1.BatchCreateAnnotationsResponse.Entry\x1a_\n\x05Entry\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x122\n\nannotation\x18\x02 \x01(\x0b2\x1e.google.genomics.v1.Annotation"-\n\x14GetAnnotationRequest\x12\x15\n\rannotation_id\x18\x01 \x01(\t"\x95\x01\n\x17UpdateAnnotationRequest\x12\x15\n\rannotation_id\x18\x01 \x01(\t\x122\n\nannotation\x18\x02 \x01(\x0b2\x1e.google.genomics.v1.Annotation\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"0\n\x17DeleteAnnotationRequest\x12\x15\n\rannotation_id\x18\x01 \x01(\t"\xb8\x01\n\x18SearchAnnotationsRequest\x12\x1a\n\x12annotation_set_ids\x18\x01 \x03(\t\x12\x16\n\x0creference_id\x18\x02 \x01(\tH\x00\x12\x18\n\x0ereference_name\x18\x03 \x01(\tH\x00\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03end\x18\x05 \x01(\x03\x12\x12\n\npage_token\x18\x06 \x01(\t\x12\x11\n\tpage_size\x18\x07 \x01(\x05B\x0b\n\treference"i\n\x19SearchAnnotationsResponse\x123\n\x0bannotations\x18\x01 \x03(\x0b2\x1e.google.genomics.v1.Annotation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*e\n\x0eAnnotationType\x12\x1f\n\x1bANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\x0b\n\x07VARIANT\x10\x02\x12\x08\n\x04GENE\x10\x03\x12\x0e\n\nTRANSCRIPT\x10\x042\x84\r\n\x13AnnotationServiceV1\x12\x94\x01\n\x13CreateAnnotationSet\x12..google.genomics.v1.CreateAnnotationSetRequest\x1a!.google.genomics.v1.AnnotationSet"*\x82\xd3\xe4\x93\x02$"\x12/v1/annotationsets:\x0eannotation_set\x12\x92\x01\n\x10GetAnnotationSet\x12+.google.genomics.v1.GetAnnotationSetRequest\x1a!.google.genomics.v1.AnnotationSet".\x82\xd3\xe4\x93\x02(\x12&/v1/annotationsets/{annotation_set_id}\x12\xa8\x01\n\x13UpdateAnnotationSet\x12..google.genomics.v1.UpdateAnnotationSetRequest\x1a!.google.genomics.v1.AnnotationSet">\x82\xd3\xe4\x93\x028\x1a&/v1/annotationsets/{annotation_set_id}:\x0eannotation_set\x12\x8d\x01\n\x13DeleteAnnotationSet\x12..google.genomics.v1.DeleteAnnotationSetRequest\x1a\x16.google.protobuf.Empty".\x82\xd3\xe4\x93\x02(*&/v1/annotationsets/{annotation_set_id}\x12\x9f\x01\n\x14SearchAnnotationSets\x12/.google.genomics.v1.SearchAnnotationSetsRequest\x1a0.google.genomics.v1.SearchAnnotationSetsResponse"$\x82\xd3\xe4\x93\x02\x1e"\x19/v1/annotationsets/search:\x01*\x12\x84\x01\n\x10CreateAnnotation\x12+.google.genomics.v1.CreateAnnotationRequest\x1a\x1e.google.genomics.v1.Annotation"#\x82\xd3\xe4\x93\x02\x1d"\x0f/v1/annotations:\nannotation\x12\xa7\x01\n\x16BatchCreateAnnotations\x121.google.genomics.v1.BatchCreateAnnotationsRequest\x1a2.google.genomics.v1.BatchCreateAnnotationsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/v1/annotations:batchCreate:\x01*\x12\x82\x01\n\rGetAnnotation\x12(.google.genomics.v1.GetAnnotationRequest\x1a\x1e.google.genomics.v1.Annotation"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/annotations/{annotation_id}\x12\x94\x01\n\x10UpdateAnnotation\x12+.google.genomics.v1.UpdateAnnotationRequest\x1a\x1e.google.genomics.v1.Annotation"3\x82\xd3\xe4\x93\x02-\x1a\x1f/v1/annotations/{annotation_id}:\nannotation\x12\x80\x01\n\x10DeleteAnnotation\x12+.google.genomics.v1.DeleteAnnotationRequest\x1a\x16.google.protobuf.Empty"\'\x82\xd3\xe4\x93\x02!*\x1f/v1/annotations/{annotation_id}\x12\x93\x01\n\x11SearchAnnotations\x12,.google.genomics.v1.SearchAnnotationsRequest\x1a-.google.genomics.v1.SearchAnnotationsResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/v1/annotations/search:\x01*Bk\n\x16com.google.genomics.v1B\x10AnnotationsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.annotations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x10AnnotationsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_ANNOTATIONSET_INFOENTRY']._loaded_options = None
    _globals['_ANNOTATIONSET_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_ANNOTATION_INFOENTRY']._loaded_options = None
    _globals['_ANNOTATION_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['CreateAnnotationSet']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['CreateAnnotationSet']._serialized_options = b'\x82\xd3\xe4\x93\x02$"\x12/v1/annotationsets:\x0eannotation_set'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['GetAnnotationSet']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['GetAnnotationSet']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/v1/annotationsets/{annotation_set_id}'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['UpdateAnnotationSet']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['UpdateAnnotationSet']._serialized_options = b'\x82\xd3\xe4\x93\x028\x1a&/v1/annotationsets/{annotation_set_id}:\x0eannotation_set'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['DeleteAnnotationSet']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['DeleteAnnotationSet']._serialized_options = b'\x82\xd3\xe4\x93\x02(*&/v1/annotationsets/{annotation_set_id}'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['SearchAnnotationSets']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['SearchAnnotationSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x19/v1/annotationsets/search:\x01*'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['CreateAnnotation']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['CreateAnnotation']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x0f/v1/annotations:\nannotation'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['BatchCreateAnnotations']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['BatchCreateAnnotations']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/v1/annotations:batchCreate:\x01*'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['GetAnnotation']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['GetAnnotation']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/annotations/{annotation_id}'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['UpdateAnnotation']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['UpdateAnnotation']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x1a\x1f/v1/annotations/{annotation_id}:\nannotation'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['DeleteAnnotation']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['DeleteAnnotation']._serialized_options = b'\x82\xd3\xe4\x93\x02!*\x1f/v1/annotations/{annotation_id}'
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['SearchAnnotations']._loaded_options = None
    _globals['_ANNOTATIONSERVICEV1'].methods_by_name['SearchAnnotations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/v1/annotations/search:\x01*'
    _globals['_ANNOTATIONTYPE']._serialized_start = 4079
    _globals['_ANNOTATIONTYPE']._serialized_end = 4180
    _globals['_ANNOTATIONSET']._serialized_start = 241
    _globals['_ANNOTATIONSET']._serialized_end = 530
    _globals['_ANNOTATIONSET_INFOENTRY']._serialized_start = 459
    _globals['_ANNOTATIONSET_INFOENTRY']._serialized_end = 530
    _globals['_ANNOTATION']._serialized_start = 533
    _globals['_ANNOTATION']._serialized_end = 996
    _globals['_ANNOTATION_INFOENTRY']._serialized_start = 459
    _globals['_ANNOTATION_INFOENTRY']._serialized_end = 530
    _globals['_VARIANTANNOTATION']._serialized_start = 999
    _globals['_VARIANTANNOTATION']._serialized_end = 2147
    _globals['_VARIANTANNOTATION_CLINICALCONDITION']._serialized_start = 1374
    _globals['_VARIANTANNOTATION_CLINICALCONDITION']._serialized_end = 1499
    _globals['_VARIANTANNOTATION_TYPE']._serialized_start = 1501
    _globals['_VARIANTANNOTATION_TYPE']._serialized_end = 1626
    _globals['_VARIANTANNOTATION_EFFECT']._serialized_start = 1629
    _globals['_VARIANTANNOTATION_EFFECT']._serialized_end = 1824
    _globals['_VARIANTANNOTATION_CLINICALSIGNIFICANCE']._serialized_start = 1827
    _globals['_VARIANTANNOTATION_CLINICALSIGNIFICANCE']._serialized_end = 2147
    _globals['_TRANSCRIPT']._serialized_start = 2150
    _globals['_TRANSCRIPT']._serialized_end = 2429
    _globals['_TRANSCRIPT_EXON']._serialized_start = 2305
    _globals['_TRANSCRIPT_EXON']._serialized_end = 2383
    _globals['_TRANSCRIPT_CODINGSEQUENCE']._serialized_start = 2385
    _globals['_TRANSCRIPT_CODINGSEQUENCE']._serialized_end = 2429
    _globals['_EXTERNALID']._serialized_start = 2431
    _globals['_EXTERNALID']._serialized_end = 2476
    _globals['_CREATEANNOTATIONSETREQUEST']._serialized_start = 2478
    _globals['_CREATEANNOTATIONSETREQUEST']._serialized_end = 2565
    _globals['_GETANNOTATIONSETREQUEST']._serialized_start = 2567
    _globals['_GETANNOTATIONSETREQUEST']._serialized_end = 2619
    _globals['_UPDATEANNOTATIONSETREQUEST']._serialized_start = 2622
    _globals['_UPDATEANNOTATIONSETREQUEST']._serialized_end = 2785
    _globals['_DELETEANNOTATIONSETREQUEST']._serialized_start = 2787
    _globals['_DELETEANNOTATIONSETREQUEST']._serialized_end = 2842
    _globals['_SEARCHANNOTATIONSETSREQUEST']._serialized_start = 2845
    _globals['_SEARCHANNOTATIONSETSREQUEST']._serialized_end = 3025
    _globals['_SEARCHANNOTATIONSETSRESPONSE']._serialized_start = 3027
    _globals['_SEARCHANNOTATIONSETSRESPONSE']._serialized_end = 3142
    _globals['_CREATEANNOTATIONREQUEST']._serialized_start = 3144
    _globals['_CREATEANNOTATIONREQUEST']._serialized_end = 3221
    _globals['_BATCHCREATEANNOTATIONSREQUEST']._serialized_start = 3223
    _globals['_BATCHCREATEANNOTATIONSREQUEST']._serialized_end = 3327
    _globals['_BATCHCREATEANNOTATIONSRESPONSE']._serialized_start = 3330
    _globals['_BATCHCREATEANNOTATIONSRESPONSE']._serialized_end = 3534
    _globals['_BATCHCREATEANNOTATIONSRESPONSE_ENTRY']._serialized_start = 3439
    _globals['_BATCHCREATEANNOTATIONSRESPONSE_ENTRY']._serialized_end = 3534
    _globals['_GETANNOTATIONREQUEST']._serialized_start = 3536
    _globals['_GETANNOTATIONREQUEST']._serialized_end = 3581
    _globals['_UPDATEANNOTATIONREQUEST']._serialized_start = 3584
    _globals['_UPDATEANNOTATIONREQUEST']._serialized_end = 3733
    _globals['_DELETEANNOTATIONREQUEST']._serialized_start = 3735
    _globals['_DELETEANNOTATIONREQUEST']._serialized_end = 3783
    _globals['_SEARCHANNOTATIONSREQUEST']._serialized_start = 3786
    _globals['_SEARCHANNOTATIONSREQUEST']._serialized_end = 3970
    _globals['_SEARCHANNOTATIONSRESPONSE']._serialized_start = 3972
    _globals['_SEARCHANNOTATIONSRESPONSE']._serialized_end = 4077
    _globals['_ANNOTATIONSERVICEV1']._serialized_start = 4183
    _globals['_ANNOTATIONSERVICEV1']._serialized_end = 5851