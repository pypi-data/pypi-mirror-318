"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/data_profile.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.dataplex.v1 import processing_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_processing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/dataplex/v1/data_profile.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/cloud/dataplex/v1/processing.proto"\xa8\x04\n\x0fDataProfileSpec\x12\x1d\n\x10sampling_percent\x18\x02 \x01(\x02B\x03\xe0A\x01\x12\x17\n\nrow_filter\x18\x03 \x01(\tB\x03\xe0A\x01\x12Y\n\x11post_scan_actions\x18\x04 \x01(\x0b29.google.cloud.dataplex.v1.DataProfileSpec.PostScanActionsB\x03\xe0A\x01\x12U\n\x0einclude_fields\x18\x05 \x01(\x0b28.google.cloud.dataplex.v1.DataProfileSpec.SelectedFieldsB\x03\xe0A\x01\x12U\n\x0eexclude_fields\x18\x06 \x01(\x0b28.google.cloud.dataplex.v1.DataProfileSpec.SelectedFieldsB\x03\xe0A\x01\x1a\xa7\x01\n\x0fPostScanActions\x12f\n\x0fbigquery_export\x18\x01 \x01(\x0b2H.google.cloud.dataplex.v1.DataProfileSpec.PostScanActions.BigQueryExportB\x03\xe0A\x01\x1a,\n\x0eBigQueryExport\x12\x1a\n\rresults_table\x18\x01 \x01(\tB\x03\xe0A\x01\x1a*\n\x0eSelectedFields\x12\x18\n\x0bfield_names\x18\x01 \x03(\tB\x03\xe0A\x01"\xe4\r\n\x11DataProfileResult\x12\x11\n\trow_count\x18\x03 \x01(\x03\x12D\n\x07profile\x18\x04 \x01(\x0b23.google.cloud.dataplex.v1.DataProfileResult.Profile\x12;\n\x0cscanned_data\x18\x05 \x01(\x0b2%.google.cloud.dataplex.v1.ScannedData\x12h\n\x18post_scan_actions_result\x18\x06 \x01(\x0b2A.google.cloud.dataplex.v1.DataProfileResult.PostScanActionsResultB\x03\xe0A\x03\x1a\xce\x08\n\x07Profile\x12I\n\x06fields\x18\x02 \x03(\x0b29.google.cloud.dataplex.v1.DataProfileResult.Profile.Field\x1a\xf7\x07\n\x05Field\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04mode\x18\x03 \x01(\t\x12V\n\x07profile\x18\x04 \x01(\x0b2E.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo\x1a\xeb\x06\n\x0bProfileInfo\x12\x12\n\nnull_ratio\x18\x02 \x01(\x01\x12\x16\n\x0edistinct_ratio\x18\x03 \x01(\x01\x12e\n\x0ctop_n_values\x18\x04 \x03(\x0b2O.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.TopNValue\x12o\n\x0estring_profile\x18e \x01(\x0b2U.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfoH\x00\x12q\n\x0finteger_profile\x18f \x01(\x0b2V.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfoH\x00\x12o\n\x0edouble_profile\x18g \x01(\x0b2U.google.cloud.dataplex.v1.DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfoH\x00\x1aQ\n\x0fStringFieldInfo\x12\x12\n\nmin_length\x18\x01 \x01(\x03\x12\x12\n\nmax_length\x18\x02 \x01(\x03\x12\x16\n\x0eaverage_length\x18\x03 \x01(\x01\x1al\n\x10IntegerFieldInfo\x12\x0f\n\x07average\x18\x01 \x01(\x01\x12\x1a\n\x12standard_deviation\x18\x03 \x01(\x01\x12\x0b\n\x03min\x18\x04 \x01(\x03\x12\x11\n\tquartiles\x18\x06 \x03(\x03\x12\x0b\n\x03max\x18\x05 \x01(\x03\x1ak\n\x0fDoubleFieldInfo\x12\x0f\n\x07average\x18\x01 \x01(\x01\x12\x1a\n\x12standard_deviation\x18\x03 \x01(\x01\x12\x0b\n\x03min\x18\x04 \x01(\x01\x12\x11\n\tquartiles\x18\x06 \x03(\x01\x12\x0b\n\x03max\x18\x05 \x01(\x01\x1a8\n\tTopNValue\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03\x12\r\n\x05ratio\x18\x03 \x01(\x01B\x0c\n\nfield_info\x1a\xfd\x02\n\x15PostScanActionsResult\x12{\n\x16bigquery_export_result\x18\x01 \x01(\x0b2V.google.cloud.dataplex.v1.DataProfileResult.PostScanActionsResult.BigQueryExportResultB\x03\xe0A\x03\x1a\xe6\x01\n\x14BigQueryExportResult\x12p\n\x05state\x18\x01 \x01(\x0e2\\.google.cloud.dataplex.v1.DataProfileResult.PostScanActionsResult.BigQueryExportResult.StateB\x03\xe0A\x03\x12\x14\n\x07message\x18\x02 \x01(\tB\x03\xe0A\x03"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\x0b\n\x07SKIPPED\x10\x03Bl\n\x1ccom.google.cloud.dataplex.v1B\x10DataProfileProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.data_profile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x10DataProfileProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS_BIGQUERYEXPORT'].fields_by_name['results_table']._loaded_options = None
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS_BIGQUERYEXPORT'].fields_by_name['results_table']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS'].fields_by_name['bigquery_export']._loaded_options = None
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS'].fields_by_name['bigquery_export']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC_SELECTEDFIELDS'].fields_by_name['field_names']._loaded_options = None
    _globals['_DATAPROFILESPEC_SELECTEDFIELDS'].fields_by_name['field_names']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC'].fields_by_name['sampling_percent']._loaded_options = None
    _globals['_DATAPROFILESPEC'].fields_by_name['sampling_percent']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC'].fields_by_name['row_filter']._loaded_options = None
    _globals['_DATAPROFILESPEC'].fields_by_name['row_filter']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC'].fields_by_name['post_scan_actions']._loaded_options = None
    _globals['_DATAPROFILESPEC'].fields_by_name['post_scan_actions']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC'].fields_by_name['include_fields']._loaded_options = None
    _globals['_DATAPROFILESPEC'].fields_by_name['include_fields']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILESPEC'].fields_by_name['exclude_fields']._loaded_options = None
    _globals['_DATAPROFILESPEC'].fields_by_name['exclude_fields']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT'].fields_by_name['state']._loaded_options = None
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT'].fields_by_name['message']._loaded_options = None
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT'].fields_by_name['message']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT'].fields_by_name['bigquery_export_result']._loaded_options = None
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT'].fields_by_name['bigquery_export_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPROFILERESULT'].fields_by_name['post_scan_actions_result']._loaded_options = None
    _globals['_DATAPROFILERESULT'].fields_by_name['post_scan_actions_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPROFILESPEC']._serialized_start = 150
    _globals['_DATAPROFILESPEC']._serialized_end = 702
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS']._serialized_start = 491
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS']._serialized_end = 658
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS_BIGQUERYEXPORT']._serialized_start = 614
    _globals['_DATAPROFILESPEC_POSTSCANACTIONS_BIGQUERYEXPORT']._serialized_end = 658
    _globals['_DATAPROFILESPEC_SELECTEDFIELDS']._serialized_start = 660
    _globals['_DATAPROFILESPEC_SELECTEDFIELDS']._serialized_end = 702
    _globals['_DATAPROFILERESULT']._serialized_start = 705
    _globals['_DATAPROFILERESULT']._serialized_end = 2469
    _globals['_DATAPROFILERESULT_PROFILE']._serialized_start = 983
    _globals['_DATAPROFILERESULT_PROFILE']._serialized_end = 2085
    _globals['_DATAPROFILERESULT_PROFILE_FIELD']._serialized_start = 1070
    _globals['_DATAPROFILERESULT_PROFILE_FIELD']._serialized_end = 2085
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO']._serialized_start = 1210
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO']._serialized_end = 2085
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_STRINGFIELDINFO']._serialized_start = 1713
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_STRINGFIELDINFO']._serialized_end = 1794
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_INTEGERFIELDINFO']._serialized_start = 1796
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_INTEGERFIELDINFO']._serialized_end = 1904
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_DOUBLEFIELDINFO']._serialized_start = 1906
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_DOUBLEFIELDINFO']._serialized_end = 2013
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_TOPNVALUE']._serialized_start = 2015
    _globals['_DATAPROFILERESULT_PROFILE_FIELD_PROFILEINFO_TOPNVALUE']._serialized_end = 2071
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT']._serialized_start = 2088
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT']._serialized_end = 2469
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT']._serialized_start = 2239
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT']._serialized_end = 2469
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT_STATE']._serialized_start = 2399
    _globals['_DATAPROFILERESULT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT_STATE']._serialized_end = 2469