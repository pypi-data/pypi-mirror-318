"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/language/v2/language_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/language/v2/language_service.proto\x12\x18google.cloud.language.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xcd\x01\n\x08Document\x125\n\x04type\x18\x01 \x01(\x0e2\'.google.cloud.language.v2.Document.Type\x12\x11\n\x07content\x18\x02 \x01(\tH\x00\x12\x19\n\x0fgcs_content_uri\x18\x03 \x01(\tH\x00\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nPLAIN_TEXT\x10\x01\x12\x08\n\x04HTML\x10\x02B\x08\n\x06source"t\n\x08Sentence\x120\n\x04text\x18\x01 \x01(\x0b2".google.cloud.language.v2.TextSpan\x126\n\tsentiment\x18\x02 \x01(\x0b2#.google.cloud.language.v2.Sentiment"\xed\x03\n\x06Entity\x12\x0c\n\x04name\x18\x01 \x01(\t\x123\n\x04type\x18\x02 \x01(\x0e2%.google.cloud.language.v2.Entity.Type\x12@\n\x08metadata\x18\x03 \x03(\x0b2..google.cloud.language.v2.Entity.MetadataEntry\x129\n\x08mentions\x18\x05 \x03(\x0b2\'.google.cloud.language.v2.EntityMention\x126\n\tsentiment\x18\x06 \x01(\x0b2#.google.cloud.language.v2.Sentiment\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xb9\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06PERSON\x10\x01\x12\x0c\n\x08LOCATION\x10\x02\x12\x10\n\x0cORGANIZATION\x10\x03\x12\t\n\x05EVENT\x10\x04\x12\x0f\n\x0bWORK_OF_ART\x10\x05\x12\x11\n\rCONSUMER_GOOD\x10\x06\x12\t\n\x05OTHER\x10\x07\x12\x10\n\x0cPHONE_NUMBER\x10\t\x12\x0b\n\x07ADDRESS\x10\n\x12\x08\n\x04DATE\x10\x0b\x12\n\n\x06NUMBER\x10\x0c\x12\t\n\x05PRICE\x10\r"-\n\tSentiment\x12\x11\n\tmagnitude\x18\x01 \x01(\x02\x12\r\n\x05score\x18\x02 \x01(\x02"\xfc\x01\n\rEntityMention\x120\n\x04text\x18\x01 \x01(\x0b2".google.cloud.language.v2.TextSpan\x12:\n\x04type\x18\x02 \x01(\x0e2,.google.cloud.language.v2.EntityMention.Type\x126\n\tsentiment\x18\x03 \x01(\x0b2#.google.cloud.language.v2.Sentiment\x12\x13\n\x0bprobability\x18\x04 \x01(\x02"0\n\x04Type\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\n\n\x06PROPER\x10\x01\x12\n\n\x06COMMON\x10\x02"1\n\x08TextSpan\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x14\n\x0cbegin_offset\x18\x02 \x01(\x05"Q\n\x16ClassificationCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x15\n\x08severity\x18\x03 \x01(\x02B\x03\xe0A\x01"\x93\x01\n\x17AnalyzeSentimentRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.cloud.language.v2.DocumentB\x03\xe0A\x02\x12=\n\rencoding_type\x18\x02 \x01(\x0e2&.google.cloud.language.v2.EncodingType"\xc5\x01\n\x18AnalyzeSentimentResponse\x12?\n\x12document_sentiment\x18\x01 \x01(\x0b2#.google.cloud.language.v2.Sentiment\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x125\n\tsentences\x18\x03 \x03(\x0b2".google.cloud.language.v2.Sentence\x12\x1a\n\x12language_supported\x18\x04 \x01(\x08"\x92\x01\n\x16AnalyzeEntitiesRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.cloud.language.v2.DocumentB\x03\xe0A\x02\x12=\n\rencoding_type\x18\x02 \x01(\x0e2&.google.cloud.language.v2.EncodingType"\x80\x01\n\x17AnalyzeEntitiesResponse\x122\n\x08entities\x18\x01 \x03(\x0b2 .google.cloud.language.v2.Entity\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x1a\n\x12language_supported\x18\x03 \x01(\x08"P\n\x13ClassifyTextRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.cloud.language.v2.DocumentB\x03\xe0A\x02"\x8f\x01\n\x14ClassifyTextResponse\x12D\n\ncategories\x18\x01 \x03(\x0b20.google.cloud.language.v2.ClassificationCategory\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x1a\n\x12language_supported\x18\x03 \x01(\x08"\x81\x02\n\x13ModerateTextRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.cloud.language.v2.DocumentB\x03\xe0A\x02\x12V\n\rmodel_version\x18\x02 \x01(\x0e2:.google.cloud.language.v2.ModerateTextRequest.ModelVersionB\x03\xe0A\x01"W\n\x0cModelVersion\x12\x1d\n\x19MODEL_VERSION_UNSPECIFIED\x10\x00\x12\x13\n\x0fMODEL_VERSION_1\x10\x01\x12\x13\n\x0fMODEL_VERSION_2\x10\x02"\x9a\x01\n\x14ModerateTextResponse\x12O\n\x15moderation_categories\x18\x01 \x03(\x0b20.google.cloud.language.v2.ClassificationCategory\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x1a\n\x12language_supported\x18\x03 \x01(\x08"\xeb\x02\n\x13AnnotateTextRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.cloud.language.v2.DocumentB\x03\xe0A\x02\x12M\n\x08features\x18\x02 \x01(\x0b26.google.cloud.language.v2.AnnotateTextRequest.FeaturesB\x03\xe0A\x02\x12=\n\rencoding_type\x18\x03 \x01(\x0e2&.google.cloud.language.v2.EncodingType\x1a\x8a\x01\n\x08Features\x12\x1d\n\x10extract_entities\x18\x01 \x01(\x08B\x03\xe0A\x01\x12\'\n\x1aextract_document_sentiment\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rclassify_text\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rmoderate_text\x18\x05 \x01(\x08B\x03\xe0A\x01"\x8c\x03\n\x14AnnotateTextResponse\x125\n\tsentences\x18\x01 \x03(\x0b2".google.cloud.language.v2.Sentence\x122\n\x08entities\x18\x02 \x03(\x0b2 .google.cloud.language.v2.Entity\x12?\n\x12document_sentiment\x18\x03 \x01(\x0b2#.google.cloud.language.v2.Sentiment\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12D\n\ncategories\x18\x05 \x03(\x0b20.google.cloud.language.v2.ClassificationCategory\x12O\n\x15moderation_categories\x18\x06 \x03(\x0b20.google.cloud.language.v2.ClassificationCategory\x12\x1a\n\x12language_supported\x18\x07 \x01(\x08*8\n\x0cEncodingType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04UTF8\x10\x01\x12\t\n\x05UTF16\x10\x02\x12\t\n\x05UTF32\x10\x032\xb0\x08\n\x0fLanguageService\x12\xc8\x01\n\x10AnalyzeSentiment\x121.google.cloud.language.v2.AnalyzeSentimentRequest\x1a2.google.cloud.language.v2.AnalyzeSentimentResponse"M\xdaA\x16document,encoding_type\xdaA\x08document\x82\xd3\xe4\x93\x02#"\x1e/v2/documents:analyzeSentiment:\x01*\x12\xc4\x01\n\x0fAnalyzeEntities\x120.google.cloud.language.v2.AnalyzeEntitiesRequest\x1a1.google.cloud.language.v2.AnalyzeEntitiesResponse"L\xdaA\x16document,encoding_type\xdaA\x08document\x82\xd3\xe4\x93\x02""\x1d/v2/documents:analyzeEntities:\x01*\x12\x9f\x01\n\x0cClassifyText\x12-.google.cloud.language.v2.ClassifyTextRequest\x1a..google.cloud.language.v2.ClassifyTextResponse"0\xdaA\x08document\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:classifyText:\x01*\x12\x9f\x01\n\x0cModerateText\x12-.google.cloud.language.v2.ModerateTextRequest\x1a..google.cloud.language.v2.ModerateTextResponse"0\xdaA\x08document\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:moderateText:\x01*\x12\xca\x01\n\x0cAnnotateText\x12-.google.cloud.language.v2.AnnotateTextRequest\x1a..google.cloud.language.v2.AnnotateTextResponse"[\xdaA\x1fdocument,features,encoding_type\xdaA\x11document,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:annotateText:\x01*\x1az\xcaA\x17language.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-language,https://www.googleapis.com/auth/cloud-platformBp\n\x1ccom.google.cloud.language.v2B\x14LanguageServiceProtoP\x01Z8cloud.google.com/go/language/apiv2/languagepb;languagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.language.v2.language_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.language.v2B\x14LanguageServiceProtoP\x01Z8cloud.google.com/go/language/apiv2/languagepb;languagepb'
    _globals['_DOCUMENT'].fields_by_name['language_code']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITY_METADATAENTRY']._loaded_options = None
    _globals['_ENTITY_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_CLASSIFICATIONCATEGORY'].fields_by_name['severity']._loaded_options = None
    _globals['_CLASSIFICATIONCATEGORY'].fields_by_name['severity']._serialized_options = b'\xe0A\x01'
    _globals['_ANALYZESENTIMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_ANALYZESENTIMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_ANALYZEENTITIESREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_ANALYZEENTITIESREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_CLASSIFYTEXTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_CLASSIFYTEXTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_MODERATETEXTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_MODERATETEXTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_MODERATETEXTREQUEST'].fields_by_name['model_version']._loaded_options = None
    _globals['_MODERATETEXTREQUEST'].fields_by_name['model_version']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['extract_entities']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['extract_entities']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['extract_document_sentiment']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['extract_document_sentiment']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['classify_text']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['classify_text']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['moderate_text']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST_FEATURES'].fields_by_name['moderate_text']._serialized_options = b'\xe0A\x01'
    _globals['_ANNOTATETEXTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_ANNOTATETEXTREQUEST'].fields_by_name['features']._loaded_options = None
    _globals['_ANNOTATETEXTREQUEST'].fields_by_name['features']._serialized_options = b'\xe0A\x02'
    _globals['_LANGUAGESERVICE']._loaded_options = None
    _globals['_LANGUAGESERVICE']._serialized_options = b'\xcaA\x17language.googleapis.com\xd2A]https://www.googleapis.com/auth/cloud-language,https://www.googleapis.com/auth/cloud-platform'
    _globals['_LANGUAGESERVICE'].methods_by_name['AnalyzeSentiment']._loaded_options = None
    _globals['_LANGUAGESERVICE'].methods_by_name['AnalyzeSentiment']._serialized_options = b'\xdaA\x16document,encoding_type\xdaA\x08document\x82\xd3\xe4\x93\x02#"\x1e/v2/documents:analyzeSentiment:\x01*'
    _globals['_LANGUAGESERVICE'].methods_by_name['AnalyzeEntities']._loaded_options = None
    _globals['_LANGUAGESERVICE'].methods_by_name['AnalyzeEntities']._serialized_options = b'\xdaA\x16document,encoding_type\xdaA\x08document\x82\xd3\xe4\x93\x02""\x1d/v2/documents:analyzeEntities:\x01*'
    _globals['_LANGUAGESERVICE'].methods_by_name['ClassifyText']._loaded_options = None
    _globals['_LANGUAGESERVICE'].methods_by_name['ClassifyText']._serialized_options = b'\xdaA\x08document\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:classifyText:\x01*'
    _globals['_LANGUAGESERVICE'].methods_by_name['ModerateText']._loaded_options = None
    _globals['_LANGUAGESERVICE'].methods_by_name['ModerateText']._serialized_options = b'\xdaA\x08document\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:moderateText:\x01*'
    _globals['_LANGUAGESERVICE'].methods_by_name['AnnotateText']._loaded_options = None
    _globals['_LANGUAGESERVICE'].methods_by_name['AnnotateText']._serialized_options = b'\xdaA\x1fdocument,features,encoding_type\xdaA\x11document,features\x82\xd3\xe4\x93\x02\x1f"\x1a/v2/documents:annotateText:\x01*'
    _globals['_ENCODINGTYPE']._serialized_start = 3463
    _globals['_ENCODINGTYPE']._serialized_end = 3519
    _globals['_DOCUMENT']._serialized_start = 166
    _globals['_DOCUMENT']._serialized_end = 371
    _globals['_DOCUMENT_TYPE']._serialized_start = 307
    _globals['_DOCUMENT_TYPE']._serialized_end = 361
    _globals['_SENTENCE']._serialized_start = 373
    _globals['_SENTENCE']._serialized_end = 489
    _globals['_ENTITY']._serialized_start = 492
    _globals['_ENTITY']._serialized_end = 985
    _globals['_ENTITY_METADATAENTRY']._serialized_start = 750
    _globals['_ENTITY_METADATAENTRY']._serialized_end = 797
    _globals['_ENTITY_TYPE']._serialized_start = 800
    _globals['_ENTITY_TYPE']._serialized_end = 985
    _globals['_SENTIMENT']._serialized_start = 987
    _globals['_SENTIMENT']._serialized_end = 1032
    _globals['_ENTITYMENTION']._serialized_start = 1035
    _globals['_ENTITYMENTION']._serialized_end = 1287
    _globals['_ENTITYMENTION_TYPE']._serialized_start = 1239
    _globals['_ENTITYMENTION_TYPE']._serialized_end = 1287
    _globals['_TEXTSPAN']._serialized_start = 1289
    _globals['_TEXTSPAN']._serialized_end = 1338
    _globals['_CLASSIFICATIONCATEGORY']._serialized_start = 1340
    _globals['_CLASSIFICATIONCATEGORY']._serialized_end = 1421
    _globals['_ANALYZESENTIMENTREQUEST']._serialized_start = 1424
    _globals['_ANALYZESENTIMENTREQUEST']._serialized_end = 1571
    _globals['_ANALYZESENTIMENTRESPONSE']._serialized_start = 1574
    _globals['_ANALYZESENTIMENTRESPONSE']._serialized_end = 1771
    _globals['_ANALYZEENTITIESREQUEST']._serialized_start = 1774
    _globals['_ANALYZEENTITIESREQUEST']._serialized_end = 1920
    _globals['_ANALYZEENTITIESRESPONSE']._serialized_start = 1923
    _globals['_ANALYZEENTITIESRESPONSE']._serialized_end = 2051
    _globals['_CLASSIFYTEXTREQUEST']._serialized_start = 2053
    _globals['_CLASSIFYTEXTREQUEST']._serialized_end = 2133
    _globals['_CLASSIFYTEXTRESPONSE']._serialized_start = 2136
    _globals['_CLASSIFYTEXTRESPONSE']._serialized_end = 2279
    _globals['_MODERATETEXTREQUEST']._serialized_start = 2282
    _globals['_MODERATETEXTREQUEST']._serialized_end = 2539
    _globals['_MODERATETEXTREQUEST_MODELVERSION']._serialized_start = 2452
    _globals['_MODERATETEXTREQUEST_MODELVERSION']._serialized_end = 2539
    _globals['_MODERATETEXTRESPONSE']._serialized_start = 2542
    _globals['_MODERATETEXTRESPONSE']._serialized_end = 2696
    _globals['_ANNOTATETEXTREQUEST']._serialized_start = 2699
    _globals['_ANNOTATETEXTREQUEST']._serialized_end = 3062
    _globals['_ANNOTATETEXTREQUEST_FEATURES']._serialized_start = 2924
    _globals['_ANNOTATETEXTREQUEST_FEATURES']._serialized_end = 3062
    _globals['_ANNOTATETEXTRESPONSE']._serialized_start = 3065
    _globals['_ANNOTATETEXTRESPONSE']._serialized_end = 3461
    _globals['_LANGUAGESERVICE']._serialized_start = 3522
    _globals['_LANGUAGESERVICE']._serialized_end = 4594