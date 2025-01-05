"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/document_io.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/documentai/v1beta3/document_io.proto\x12\x1fgoogle.cloud.documentai.v1beta3\x1a google/protobuf/field_mask.proto"G\n\x0bRawDocument\x12\x0f\n\x07content\x18\x01 \x01(\x0c\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t"1\n\x0bGcsDocument\x12\x0f\n\x07gcs_uri\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t"O\n\x0cGcsDocuments\x12?\n\tdocuments\x18\x01 \x03(\x0b2,.google.cloud.documentai.v1beta3.GcsDocument"#\n\tGcsPrefix\x12\x16\n\x0egcs_uri_prefix\x18\x01 \x01(\t"\xaf\x01\n\x19BatchDocumentsInputConfig\x12@\n\ngcs_prefix\x18\x01 \x01(\x0b2*.google.cloud.documentai.v1beta3.GcsPrefixH\x00\x12F\n\rgcs_documents\x18\x02 \x01(\x0b2-.google.cloud.documentai.v1beta3.GcsDocumentsH\x00B\x08\n\x06source"\x8f\x03\n\x14DocumentOutputConfig\x12b\n\x11gcs_output_config\x18\x01 \x01(\x0b2E.google.cloud.documentai.v1beta3.DocumentOutputConfig.GcsOutputConfigH\x00\x1a\x83\x02\n\x0fGcsOutputConfig\x12\x0f\n\x07gcs_uri\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12m\n\x0fsharding_config\x18\x03 \x01(\x0b2T.google.cloud.documentai.v1beta3.DocumentOutputConfig.GcsOutputConfig.ShardingConfig\x1a@\n\x0eShardingConfig\x12\x17\n\x0fpages_per_shard\x18\x01 \x01(\x05\x12\x15\n\rpages_overlap\x18\x02 \x01(\x05B\r\n\x0bdestination"\xfc\x03\n\tOcrConfig\x12?\n\x05hints\x18\x02 \x01(\x0b20.google.cloud.documentai.v1beta3.OcrConfig.Hints\x12!\n\x19enable_native_pdf_parsing\x18\x03 \x01(\x08\x12#\n\x1benable_image_quality_scores\x18\x04 \x01(\x08\x12\x1c\n\x14advanced_ocr_options\x18\x05 \x03(\t\x12\x15\n\renable_symbol\x18\x06 \x01(\x08\x12\x1e\n\x12compute_style_info\x18\x08 \x01(\x08B\x02\x18\x01\x12)\n!disable_character_boxes_detection\x18\n \x01(\x08\x12T\n\x10premium_features\x18\x0b \x01(\x0b2:.google.cloud.documentai.v1beta3.OcrConfig.PremiumFeatures\x1a\x1f\n\x05Hints\x12\x16\n\x0elanguage_hints\x18\x01 \x03(\t\x1ao\n\x0fPremiumFeatures\x12\'\n\x1fenable_selection_mark_detection\x18\x03 \x01(\x08\x12\x1a\n\x12compute_style_info\x18\x04 \x01(\x08\x12\x17\n\x0fenable_math_ocr\x18\x05 \x01(\x08B\xe6\x01\n#com.google.cloud.documentai.v1beta3B\x0fDocumentIoProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.document_io_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x0fDocumentIoProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
    _globals['_OCRCONFIG'].fields_by_name['compute_style_info']._loaded_options = None
    _globals['_OCRCONFIG'].fields_by_name['compute_style_info']._serialized_options = b'\x18\x01'
    _globals['_RAWDOCUMENT']._serialized_start = 120
    _globals['_RAWDOCUMENT']._serialized_end = 191
    _globals['_GCSDOCUMENT']._serialized_start = 193
    _globals['_GCSDOCUMENT']._serialized_end = 242
    _globals['_GCSDOCUMENTS']._serialized_start = 244
    _globals['_GCSDOCUMENTS']._serialized_end = 323
    _globals['_GCSPREFIX']._serialized_start = 325
    _globals['_GCSPREFIX']._serialized_end = 360
    _globals['_BATCHDOCUMENTSINPUTCONFIG']._serialized_start = 363
    _globals['_BATCHDOCUMENTSINPUTCONFIG']._serialized_end = 538
    _globals['_DOCUMENTOUTPUTCONFIG']._serialized_start = 541
    _globals['_DOCUMENTOUTPUTCONFIG']._serialized_end = 940
    _globals['_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG']._serialized_start = 666
    _globals['_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG']._serialized_end = 925
    _globals['_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG_SHARDINGCONFIG']._serialized_start = 861
    _globals['_DOCUMENTOUTPUTCONFIG_GCSOUTPUTCONFIG_SHARDINGCONFIG']._serialized_end = 925
    _globals['_OCRCONFIG']._serialized_start = 943
    _globals['_OCRCONFIG']._serialized_end = 1451
    _globals['_OCRCONFIG_HINTS']._serialized_start = 1307
    _globals['_OCRCONFIG_HINTS']._serialized_end = 1338
    _globals['_OCRCONFIG_PREMIUMFEATURES']._serialized_start = 1340
    _globals['_OCRCONFIG_PREMIUMFEATURES']._serialized_end = 1451