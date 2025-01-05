"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/privacy/dlp/v2/storage.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/privacy/dlp/v2/storage.proto\x12\x15google.privacy.dlp.v2\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"m\n\x08InfoType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12B\n\x11sensitivity_score\x18\x03 \x01(\x0b2\'.google.privacy.dlp.v2.SensitivityScore"\xfb\x01\n\x10SensitivityScore\x12L\n\x05score\x18\x01 \x01(\x0e2=.google.privacy.dlp.v2.SensitivityScore.SensitivityScoreLevel"\x98\x01\n\x15SensitivityScoreLevel\x12!\n\x1dSENSITIVITY_SCORE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSENSITIVITY_LOW\x10\n\x12\x17\n\x13SENSITIVITY_UNKNOWN\x10\x0c\x12\x18\n\x14SENSITIVITY_MODERATE\x10\x14\x12\x14\n\x10SENSITIVITY_HIGH\x10\x1e"K\n\nStoredType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8c\x0c\n\x0eCustomInfoType\x122\n\tinfo_type\x18\x01 \x01(\x0b2\x1f.google.privacy.dlp.v2.InfoType\x125\n\nlikelihood\x18\x06 \x01(\x0e2!.google.privacy.dlp.v2.Likelihood\x12F\n\ndictionary\x18\x02 \x01(\x0b20.google.privacy.dlp.v2.CustomInfoType.DictionaryH\x00\x12<\n\x05regex\x18\x03 \x01(\x0b2+.google.privacy.dlp.v2.CustomInfoType.RegexH\x00\x12M\n\x0esurrogate_type\x18\x04 \x01(\x0b23.google.privacy.dlp.v2.CustomInfoType.SurrogateTypeH\x00\x128\n\x0bstored_type\x18\x05 \x01(\x0b2!.google.privacy.dlp.v2.StoredTypeH\x00\x12L\n\x0fdetection_rules\x18\x07 \x03(\x0b23.google.privacy.dlp.v2.CustomInfoType.DetectionRule\x12K\n\x0eexclusion_type\x18\x08 \x01(\x0e23.google.privacy.dlp.v2.CustomInfoType.ExclusionType\x12B\n\x11sensitivity_score\x18\t \x01(\x0b2\'.google.privacy.dlp.v2.SensitivityScore\x1a\xc8\x01\n\nDictionary\x12N\n\tword_list\x18\x01 \x01(\x0b29.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordListH\x00\x12E\n\x12cloud_storage_path\x18\x03 \x01(\x0b2\'.google.privacy.dlp.v2.CloudStoragePathH\x00\x1a\x19\n\x08WordList\x12\r\n\x05words\x18\x01 \x03(\tB\x08\n\x06source\x1a/\n\x05Regex\x12\x0f\n\x07pattern\x18\x01 \x01(\t\x12\x15\n\rgroup_indexes\x18\x02 \x03(\x05\x1a\x0f\n\rSurrogateType\x1a\xbe\x04\n\rDetectionRule\x12W\n\x0chotword_rule\x18\x01 \x01(\x0b2?.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRuleH\x00\x1a8\n\tProximity\x12\x15\n\rwindow_before\x18\x01 \x01(\x05\x12\x14\n\x0cwindow_after\x18\x02 \x01(\x05\x1a\x82\x01\n\x14LikelihoodAdjustment\x12=\n\x10fixed_likelihood\x18\x01 \x01(\x0e2!.google.privacy.dlp.v2.LikelihoodH\x00\x12\x1d\n\x13relative_likelihood\x18\x02 \x01(\x05H\x00B\x0c\n\nadjustment\x1a\x8c\x02\n\x0bHotwordRule\x12B\n\rhotword_regex\x18\x01 \x01(\x0b2+.google.privacy.dlp.v2.CustomInfoType.Regex\x12P\n\tproximity\x18\x02 \x01(\x0b2=.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity\x12g\n\x15likelihood_adjustment\x18\x03 \x01(\x0b2H.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustmentB\x06\n\x04type"K\n\rExclusionType\x12\x1e\n\x1aEXCLUSION_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16EXCLUSION_TYPE_EXCLUDE\x10\x01B\x06\n\x04type"\x17\n\x07FieldId\x12\x0c\n\x04name\x18\x01 \x01(\t"7\n\x0bPartitionId\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t"\x1e\n\x0eKindExpression\x12\x0c\n\x04name\x18\x01 \x01(\t"\x81\x01\n\x10DatastoreOptions\x128\n\x0cpartition_id\x18\x01 \x01(\x0b2".google.privacy.dlp.v2.PartitionId\x123\n\x04kind\x18\x02 \x01(\x0b2%.google.privacy.dlp.v2.KindExpression"]\n\x18CloudStorageRegexFileSet\x12\x13\n\x0bbucket_name\x18\x01 \x01(\t\x12\x15\n\rinclude_regex\x18\x02 \x03(\t\x12\x15\n\rexclude_regex\x18\x03 \x03(\t"\xec\x03\n\x13CloudStorageOptions\x12D\n\x08file_set\x18\x01 \x01(\x0b22.google.privacy.dlp.v2.CloudStorageOptions.FileSet\x12\x1c\n\x14bytes_limit_per_file\x18\x04 \x01(\x03\x12$\n\x1cbytes_limit_per_file_percent\x18\x08 \x01(\x05\x123\n\nfile_types\x18\x05 \x03(\x0e2\x1f.google.privacy.dlp.v2.FileType\x12N\n\rsample_method\x18\x06 \x01(\x0e27.google.privacy.dlp.v2.CloudStorageOptions.SampleMethod\x12\x1b\n\x13files_limit_percent\x18\x07 \x01(\x05\x1a_\n\x07FileSet\x12\x0b\n\x03url\x18\x01 \x01(\t\x12G\n\x0eregex_file_set\x18\x02 \x01(\x0b2/.google.privacy.dlp.v2.CloudStorageRegexFileSet"H\n\x0cSampleMethod\x12\x1d\n\x19SAMPLE_METHOD_UNSPECIFIED\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\x10\n\x0cRANDOM_START\x10\x02""\n\x13CloudStorageFileSet\x12\x0b\n\x03url\x18\x01 \x01(\t" \n\x10CloudStoragePath\x12\x0c\n\x04path\x18\x01 \x01(\t"\xc4\x03\n\x0fBigQueryOptions\x12=\n\x0ftable_reference\x18\x01 \x01(\x0b2$.google.privacy.dlp.v2.BigQueryTable\x12:\n\x12identifying_fields\x18\x02 \x03(\x0b2\x1e.google.privacy.dlp.v2.FieldId\x12\x12\n\nrows_limit\x18\x03 \x01(\x03\x12\x1a\n\x12rows_limit_percent\x18\x06 \x01(\x05\x12J\n\rsample_method\x18\x04 \x01(\x0e23.google.privacy.dlp.v2.BigQueryOptions.SampleMethod\x127\n\x0fexcluded_fields\x18\x05 \x03(\x0b2\x1e.google.privacy.dlp.v2.FieldId\x127\n\x0fincluded_fields\x18\x07 \x03(\x0b2\x1e.google.privacy.dlp.v2.FieldId"H\n\x0cSampleMethod\x12\x1d\n\x19SAMPLE_METHOD_UNSPECIFIED\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\x10\n\x0cRANDOM_START\x10\x02"\xda\x04\n\rStorageConfig\x12D\n\x11datastore_options\x18\x02 \x01(\x0b2\'.google.privacy.dlp.v2.DatastoreOptionsH\x00\x12K\n\x15cloud_storage_options\x18\x03 \x01(\x0b2*.google.privacy.dlp.v2.CloudStorageOptionsH\x00\x12C\n\x11big_query_options\x18\x04 \x01(\x0b2&.google.privacy.dlp.v2.BigQueryOptionsH\x00\x12>\n\x0ehybrid_options\x18\t \x01(\x0b2$.google.privacy.dlp.v2.HybridOptionsH\x00\x12L\n\x0ftimespan_config\x18\x06 \x01(\x0b23.google.privacy.dlp.v2.StorageConfig.TimespanConfig\x1a\xda\x01\n\x0eTimespanConfig\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x0ftimestamp_field\x18\x03 \x01(\x0b2\x1e.google.privacy.dlp.v2.FieldId\x121\n)enable_auto_population_of_timespan_config\x18\x04 \x01(\x08B\x06\n\x04type"\xf6\x01\n\rHybridOptions\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12#\n\x1brequired_finding_label_keys\x18\x02 \x03(\t\x12@\n\x06labels\x18\x03 \x03(\x0b20.google.privacy.dlp.v2.HybridOptions.LabelsEntry\x12:\n\rtable_options\x18\x04 \x01(\x0b2#.google.privacy.dlp.v2.TableOptions\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"`\n\x0bBigQueryKey\x12=\n\x0ftable_reference\x18\x01 \x01(\x0b2$.google.privacy.dlp.v2.BigQueryTable\x12\x12\n\nrow_number\x18\x02 \x01(\x03">\n\x0cDatastoreKey\x12.\n\nentity_key\x18\x01 \x01(\x0b2\x1a.google.privacy.dlp.v2.Key"\xbb\x01\n\x03Key\x128\n\x0cpartition_id\x18\x01 \x01(\x0b2".google.privacy.dlp.v2.PartitionId\x124\n\x04path\x18\x02 \x03(\x0b2&.google.privacy.dlp.v2.Key.PathElement\x1aD\n\x0bPathElement\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x02id\x18\x02 \x01(\x03H\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x00B\t\n\x07id_type"\xa1\x01\n\tRecordKey\x12<\n\rdatastore_key\x18\x02 \x01(\x0b2#.google.privacy.dlp.v2.DatastoreKeyH\x00\x12;\n\rbig_query_key\x18\x03 \x01(\x0b2".google.privacy.dlp.v2.BigQueryKeyH\x00\x12\x11\n\tid_values\x18\x05 \x03(\tB\x06\n\x04type"I\n\rBigQueryTable\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t"6\n\x0eTableReference\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x10\n\x08table_id\x18\x02 \x01(\t"s\n\rBigQueryField\x123\n\x05table\x18\x01 \x01(\x0b2$.google.privacy.dlp.v2.BigQueryTable\x12-\n\x05field\x18\x02 \x01(\x0b2\x1e.google.privacy.dlp.v2.FieldId"9\n\x08EntityId\x12-\n\x05field\x18\x01 \x01(\x0b2\x1e.google.privacy.dlp.v2.FieldId"J\n\x0cTableOptions\x12:\n\x12identifying_fields\x18\x01 \x03(\x0b2\x1e.google.privacy.dlp.v2.FieldId*t\n\nLikelihood\x12\x1a\n\x16LIKELIHOOD_UNSPECIFIED\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x05*\x9a\x01\n\x08FileType\x12\x19\n\x15FILE_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bBINARY_FILE\x10\x01\x12\r\n\tTEXT_FILE\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\x08\n\x04WORD\x10\x05\x12\x07\n\x03PDF\x10\x06\x12\x08\n\x04AVRO\x10\x07\x12\x07\n\x03CSV\x10\x08\x12\x07\n\x03TSV\x10\t\x12\x0e\n\nPOWERPOINT\x10\x0b\x12\t\n\x05EXCEL\x10\x0cB\x99\x01\n\x19com.google.privacy.dlp.v2B\nDlpStorageP\x01Z)cloud.google.com/go/dlp/apiv2/dlppb;dlppb\xaa\x02\x13Google.Cloud.Dlp.V2\xca\x02\x13Google\\Cloud\\Dlp\\V2\xea\x02\x16Google::Cloud::Dlp::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.privacy.dlp.v2.storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.privacy.dlp.v2B\nDlpStorageP\x01Z)cloud.google.com/go/dlp/apiv2/dlppb;dlppb\xaa\x02\x13Google.Cloud.Dlp.V2\xca\x02\x13Google\\Cloud\\Dlp\\V2\xea\x02\x16Google::Cloud::Dlp::V2'
    _globals['_HYBRIDOPTIONS_LABELSENTRY']._loaded_options = None
    _globals['_HYBRIDOPTIONS_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LIKELIHOOD']._serialized_start = 5229
    _globals['_LIKELIHOOD']._serialized_end = 5345
    _globals['_FILETYPE']._serialized_start = 5348
    _globals['_FILETYPE']._serialized_end = 5502
    _globals['_INFOTYPE']._serialized_start = 122
    _globals['_INFOTYPE']._serialized_end = 231
    _globals['_SENSITIVITYSCORE']._serialized_start = 234
    _globals['_SENSITIVITYSCORE']._serialized_end = 485
    _globals['_SENSITIVITYSCORE_SENSITIVITYSCORELEVEL']._serialized_start = 333
    _globals['_SENSITIVITYSCORE_SENSITIVITYSCORELEVEL']._serialized_end = 485
    _globals['_STOREDTYPE']._serialized_start = 487
    _globals['_STOREDTYPE']._serialized_end = 562
    _globals['_CUSTOMINFOTYPE']._serialized_start = 565
    _globals['_CUSTOMINFOTYPE']._serialized_end = 2113
    _globals['_CUSTOMINFOTYPE_DICTIONARY']._serialized_start = 1185
    _globals['_CUSTOMINFOTYPE_DICTIONARY']._serialized_end = 1385
    _globals['_CUSTOMINFOTYPE_DICTIONARY_WORDLIST']._serialized_start = 1350
    _globals['_CUSTOMINFOTYPE_DICTIONARY_WORDLIST']._serialized_end = 1375
    _globals['_CUSTOMINFOTYPE_REGEX']._serialized_start = 1387
    _globals['_CUSTOMINFOTYPE_REGEX']._serialized_end = 1434
    _globals['_CUSTOMINFOTYPE_SURROGATETYPE']._serialized_start = 1436
    _globals['_CUSTOMINFOTYPE_SURROGATETYPE']._serialized_end = 1451
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE']._serialized_start = 1454
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE']._serialized_end = 2028
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_PROXIMITY']._serialized_start = 1560
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_PROXIMITY']._serialized_end = 1616
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_LIKELIHOODADJUSTMENT']._serialized_start = 1619
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_LIKELIHOODADJUSTMENT']._serialized_end = 1749
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_HOTWORDRULE']._serialized_start = 1752
    _globals['_CUSTOMINFOTYPE_DETECTIONRULE_HOTWORDRULE']._serialized_end = 2020
    _globals['_CUSTOMINFOTYPE_EXCLUSIONTYPE']._serialized_start = 2030
    _globals['_CUSTOMINFOTYPE_EXCLUSIONTYPE']._serialized_end = 2105
    _globals['_FIELDID']._serialized_start = 2115
    _globals['_FIELDID']._serialized_end = 2138
    _globals['_PARTITIONID']._serialized_start = 2140
    _globals['_PARTITIONID']._serialized_end = 2195
    _globals['_KINDEXPRESSION']._serialized_start = 2197
    _globals['_KINDEXPRESSION']._serialized_end = 2227
    _globals['_DATASTOREOPTIONS']._serialized_start = 2230
    _globals['_DATASTOREOPTIONS']._serialized_end = 2359
    _globals['_CLOUDSTORAGEREGEXFILESET']._serialized_start = 2361
    _globals['_CLOUDSTORAGEREGEXFILESET']._serialized_end = 2454
    _globals['_CLOUDSTORAGEOPTIONS']._serialized_start = 2457
    _globals['_CLOUDSTORAGEOPTIONS']._serialized_end = 2949
    _globals['_CLOUDSTORAGEOPTIONS_FILESET']._serialized_start = 2780
    _globals['_CLOUDSTORAGEOPTIONS_FILESET']._serialized_end = 2875
    _globals['_CLOUDSTORAGEOPTIONS_SAMPLEMETHOD']._serialized_start = 2877
    _globals['_CLOUDSTORAGEOPTIONS_SAMPLEMETHOD']._serialized_end = 2949
    _globals['_CLOUDSTORAGEFILESET']._serialized_start = 2951
    _globals['_CLOUDSTORAGEFILESET']._serialized_end = 2985
    _globals['_CLOUDSTORAGEPATH']._serialized_start = 2987
    _globals['_CLOUDSTORAGEPATH']._serialized_end = 3019
    _globals['_BIGQUERYOPTIONS']._serialized_start = 3022
    _globals['_BIGQUERYOPTIONS']._serialized_end = 3474
    _globals['_BIGQUERYOPTIONS_SAMPLEMETHOD']._serialized_start = 2877
    _globals['_BIGQUERYOPTIONS_SAMPLEMETHOD']._serialized_end = 2949
    _globals['_STORAGECONFIG']._serialized_start = 3477
    _globals['_STORAGECONFIG']._serialized_end = 4079
    _globals['_STORAGECONFIG_TIMESPANCONFIG']._serialized_start = 3853
    _globals['_STORAGECONFIG_TIMESPANCONFIG']._serialized_end = 4071
    _globals['_HYBRIDOPTIONS']._serialized_start = 4082
    _globals['_HYBRIDOPTIONS']._serialized_end = 4328
    _globals['_HYBRIDOPTIONS_LABELSENTRY']._serialized_start = 4283
    _globals['_HYBRIDOPTIONS_LABELSENTRY']._serialized_end = 4328
    _globals['_BIGQUERYKEY']._serialized_start = 4330
    _globals['_BIGQUERYKEY']._serialized_end = 4426
    _globals['_DATASTOREKEY']._serialized_start = 4428
    _globals['_DATASTOREKEY']._serialized_end = 4490
    _globals['_KEY']._serialized_start = 4493
    _globals['_KEY']._serialized_end = 4680
    _globals['_KEY_PATHELEMENT']._serialized_start = 4612
    _globals['_KEY_PATHELEMENT']._serialized_end = 4680
    _globals['_RECORDKEY']._serialized_start = 4683
    _globals['_RECORDKEY']._serialized_end = 4844
    _globals['_BIGQUERYTABLE']._serialized_start = 4846
    _globals['_BIGQUERYTABLE']._serialized_end = 4919
    _globals['_TABLEREFERENCE']._serialized_start = 4921
    _globals['_TABLEREFERENCE']._serialized_end = 4975
    _globals['_BIGQUERYFIELD']._serialized_start = 4977
    _globals['_BIGQUERYFIELD']._serialized_end = 5092
    _globals['_ENTITYID']._serialized_start = 5094
    _globals['_ENTITYID']._serialized_end = 5151
    _globals['_TABLEOPTIONS']._serialized_start = 5153
    _globals['_TABLEOPTIONS']._serialized_end = 5227