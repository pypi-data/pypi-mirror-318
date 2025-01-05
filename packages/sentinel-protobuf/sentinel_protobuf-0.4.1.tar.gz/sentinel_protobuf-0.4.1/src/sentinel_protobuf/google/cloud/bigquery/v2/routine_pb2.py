"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/routine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import routine_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_routine__reference__pb2
from .....google.cloud.bigquery.v2 import standard_sql_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_standard__sql__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/bigquery/v2/routine.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a0google/cloud/bigquery/v2/routine_reference.proto\x1a+google/cloud/bigquery/v2/standard_sql.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbc\x11\n\x07Routine\x12\x11\n\x04etag\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x11routine_reference\x18\x02 \x01(\x0b2*.google.cloud.bigquery.v2.RoutineReferenceB\x03\xe0A\x02\x12H\n\x0croutine_type\x18\x03 \x01(\x0e2-.google.cloud.bigquery.v2.Routine.RoutineTypeB\x03\xe0A\x02\x12\x1a\n\rcreation_time\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18\x05 \x01(\x03B\x03\xe0A\x03\x12A\n\x08language\x18\x06 \x01(\x0e2*.google.cloud.bigquery.v2.Routine.LanguageB\x03\xe0A\x01\x12=\n\targuments\x18\x07 \x03(\x0b2*.google.cloud.bigquery.v2.Routine.Argument\x12B\n\x0breturn_type\x18\n \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataType\x12N\n\x11return_table_type\x18\r \x01(\x0b2..google.cloud.bigquery.v2.StandardSqlTableTypeB\x03\xe0A\x01\x12\x1a\n\x12imported_libraries\x18\x08 \x03(\t\x12\x17\n\x0fdefinition_body\x18\t \x01(\t\x12\x18\n\x0bdescription\x18\x0b \x01(\tB\x03\xe0A\x01\x12R\n\x11determinism_level\x18\x0c \x01(\x0e22.google.cloud.bigquery.v2.Routine.DeterminismLevelB\x03\xe0A\x01\x12J\n\rsecurity_mode\x18\x12 \x01(\x0e2..google.cloud.bigquery.v2.Routine.SecurityModeB\x03\xe0A\x01\x124\n\x0bstrict_mode\x18\x0e \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12]\n\x17remote_function_options\x18\x0f \x01(\x0b27.google.cloud.bigquery.v2.Routine.RemoteFunctionOptionsB\x03\xe0A\x01\x12B\n\rspark_options\x18\x10 \x01(\x0b2&.google.cloud.bigquery.v2.SparkOptionsB\x03\xe0A\x01\x12W\n\x14data_governance_type\x18\x11 \x01(\x0e24.google.cloud.bigquery.v2.Routine.DataGovernanceTypeB\x03\xe0A\x01\x1a\xb1\x03\n\x08Argument\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12S\n\rargument_kind\x18\x02 \x01(\x0e27.google.cloud.bigquery.v2.Routine.Argument.ArgumentKindB\x03\xe0A\x01\x12=\n\x04mode\x18\x03 \x01(\x0e2/.google.cloud.bigquery.v2.Routine.Argument.Mode\x12@\n\tdata_type\x18\x04 \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataType\x125\n\x0cis_aggregate\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"K\n\x0cArgumentKind\x12\x1d\n\x19ARGUMENT_KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nFIXED_TYPE\x10\x01\x12\x0c\n\x08ANY_TYPE\x10\x02"8\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x06\n\x02IN\x10\x01\x12\x07\n\x03OUT\x10\x02\x12\t\n\x05INOUT\x10\x03\x1a\x82\x02\n\x15RemoteFunctionOptions\x12\x10\n\x08endpoint\x18\x01 \x01(\t\x12\x12\n\nconnection\x18\x02 \x01(\t\x12m\n\x14user_defined_context\x18\x03 \x03(\x0b2O.google.cloud.bigquery.v2.Routine.RemoteFunctionOptions.UserDefinedContextEntry\x12\x19\n\x11max_batching_rows\x18\x04 \x01(\x03\x1a9\n\x17UserDefinedContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x82\x01\n\x0bRoutineType\x12\x1c\n\x18ROUTINE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCALAR_FUNCTION\x10\x01\x12\r\n\tPROCEDURE\x10\x02\x12\x19\n\x15TABLE_VALUED_FUNCTION\x10\x03\x12\x16\n\x12AGGREGATE_FUNCTION\x10\x04"^\n\x08Language\x12\x18\n\x14LANGUAGE_UNSPECIFIED\x10\x00\x12\x07\n\x03SQL\x10\x01\x12\x0e\n\nJAVASCRIPT\x10\x02\x12\n\n\x06PYTHON\x10\x03\x12\x08\n\x04JAVA\x10\x04\x12\t\n\x05SCALA\x10\x05"_\n\x10DeterminismLevel\x12!\n\x1dDETERMINISM_LEVEL_UNSPECIFIED\x10\x00\x12\x11\n\rDETERMINISTIC\x10\x01\x12\x15\n\x11NOT_DETERMINISTIC\x10\x02"G\n\x0cSecurityMode\x12\x1d\n\x19SECURITY_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFINER\x10\x01\x12\x0b\n\x07INVOKER\x10\x02"L\n\x12DataGovernanceType\x12$\n DATA_GOVERNANCE_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cDATA_MASKING\x10\x01"\xcf\x02\n\x0cSparkOptions\x12\x12\n\nconnection\x18\x01 \x01(\t\x12\x17\n\x0fruntime_version\x18\x02 \x01(\t\x12\x17\n\x0fcontainer_image\x18\x03 \x01(\t\x12J\n\nproperties\x18\x04 \x03(\x0b26.google.cloud.bigquery.v2.SparkOptions.PropertiesEntry\x12\x15\n\rmain_file_uri\x18\x05 \x01(\t\x12\x14\n\x0cpy_file_uris\x18\x06 \x03(\t\x12\x10\n\x08jar_uris\x18\x07 \x03(\t\x12\x11\n\tfile_uris\x18\x08 \x03(\t\x12\x14\n\x0carchive_uris\x18\t \x03(\t\x12\x12\n\nmain_class\x18\n \x01(\t\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x11GetRoutineRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nroutine_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x81\x01\n\x14InsertRoutineRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x07routine\x18\x03 \x01(\x0b2!.google.cloud.bigquery.v2.RoutineB\x03\xe0A\x02"\x9a\x01\n\x14UpdateRoutineRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nroutine_id\x18\x03 \x01(\tB\x03\xe0A\x02\x127\n\x07routine\x18\x04 \x01(\x0b2!.google.cloud.bigquery.v2.RoutineB\x03\xe0A\x02"\xc9\x01\n\x13PatchRoutineRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nroutine_id\x18\x03 \x01(\tB\x03\xe0A\x02\x127\n\x07routine\x18\x04 \x01(\x0b2!.google.cloud.bigquery.v2.RoutineB\x03\xe0A\x02\x12.\n\nfield_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"a\n\x14DeleteRoutineRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nroutine_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x9e\x01\n\x13ListRoutinesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x121\n\x0bmax_results\x18\x03 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x06 \x01(\t"d\n\x14ListRoutinesResponse\x123\n\x08routines\x18\x01 \x03(\x0b2!.google.cloud.bigquery.v2.Routine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe2\t\n\x0eRoutineService\x12\xba\x01\n\nGetRoutine\x12+.google.cloud.bigquery.v2.GetRoutineRequest\x1a!.google.cloud.bigquery.v2.Routine"\\\x82\xd3\xe4\x93\x02V\x12T/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}\x12\xba\x01\n\rInsertRoutine\x12..google.cloud.bigquery.v2.InsertRoutineRequest\x1a!.google.cloud.bigquery.v2.Routine"V\x82\xd3\xe4\x93\x02P"E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines:\x07routine\x12\xc9\x01\n\rUpdateRoutine\x12..google.cloud.bigquery.v2.UpdateRoutineRequest\x1a!.google.cloud.bigquery.v2.Routine"e\x82\xd3\xe4\x93\x02_\x1aT/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}:\x07routine\x12b\n\x0cPatchRoutine\x12-.google.cloud.bigquery.v2.PatchRoutineRequest\x1a!.google.cloud.bigquery.v2.Routine"\x00\x12\xb5\x01\n\rDeleteRoutine\x12..google.cloud.bigquery.v2.DeleteRoutineRequest\x1a\x16.google.protobuf.Empty"\\\x82\xd3\xe4\x93\x02V*T/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}\x12\xbc\x01\n\x0cListRoutines\x12-.google.cloud.bigquery.v2.ListRoutinesRequest\x1a..google.cloud.bigquery.v2.ListRoutinesResponse"M\x82\xd3\xe4\x93\x02G\x12E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBf\n\x1ccom.google.cloud.bigquery.v2B\x0cRoutineProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.routine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x0cRoutineProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['argument_kind']._loaded_options = None
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['argument_kind']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['is_aggregate']._loaded_options = None
    _globals['_ROUTINE_ARGUMENT'].fields_by_name['is_aggregate']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS_USERDEFINEDCONTEXTENTRY']._loaded_options = None
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS_USERDEFINEDCONTEXTENTRY']._serialized_options = b'8\x01'
    _globals['_ROUTINE'].fields_by_name['etag']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ROUTINE'].fields_by_name['routine_reference']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['routine_reference']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTINE'].fields_by_name['routine_type']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['routine_type']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTINE'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROUTINE'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROUTINE'].fields_by_name['language']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['language']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['return_table_type']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['return_table_type']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['description']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['determinism_level']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['determinism_level']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['security_mode']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['security_mode']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['strict_mode']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['strict_mode']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['remote_function_options']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['remote_function_options']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['spark_options']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['spark_options']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINE'].fields_by_name['data_governance_type']._loaded_options = None
    _globals['_ROUTINE'].fields_by_name['data_governance_type']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKOPTIONS_PROPERTIESENTRY']._loaded_options = None
    _globals['_SPARKOPTIONS_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_GETROUTINEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETROUTINEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROUTINEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_GETROUTINEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROUTINEREQUEST'].fields_by_name['routine_id']._loaded_options = None
    _globals['_GETROUTINEREQUEST'].fields_by_name['routine_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['routine']._loaded_options = None
    _globals['_INSERTROUTINEREQUEST'].fields_by_name['routine']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['routine_id']._loaded_options = None
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['routine_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['routine']._loaded_options = None
    _globals['_UPDATEROUTINEREQUEST'].fields_by_name['routine']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['routine_id']._loaded_options = None
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['routine_id']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['routine']._loaded_options = None
    _globals['_PATCHROUTINEREQUEST'].fields_by_name['routine']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['routine_id']._loaded_options = None
    _globals['_DELETEROUTINEREQUEST'].fields_by_name['routine_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROUTINESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTROUTINESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROUTINESREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_LISTROUTINESREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTINESERVICE']._loaded_options = None
    _globals['_ROUTINESERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_ROUTINESERVICE'].methods_by_name['GetRoutine']._loaded_options = None
    _globals['_ROUTINESERVICE'].methods_by_name['GetRoutine']._serialized_options = b'\x82\xd3\xe4\x93\x02V\x12T/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}'
    _globals['_ROUTINESERVICE'].methods_by_name['InsertRoutine']._loaded_options = None
    _globals['_ROUTINESERVICE'].methods_by_name['InsertRoutine']._serialized_options = b'\x82\xd3\xe4\x93\x02P"E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines:\x07routine'
    _globals['_ROUTINESERVICE'].methods_by_name['UpdateRoutine']._loaded_options = None
    _globals['_ROUTINESERVICE'].methods_by_name['UpdateRoutine']._serialized_options = b'\x82\xd3\xe4\x93\x02_\x1aT/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}:\x07routine'
    _globals['_ROUTINESERVICE'].methods_by_name['DeleteRoutine']._loaded_options = None
    _globals['_ROUTINESERVICE'].methods_by_name['DeleteRoutine']._serialized_options = b'\x82\xd3\xe4\x93\x02V*T/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines/{routine_id=*}'
    _globals['_ROUTINESERVICE'].methods_by_name['ListRoutines']._loaded_options = None
    _globals['_ROUTINESERVICE'].methods_by_name['ListRoutines']._serialized_options = b'\x82\xd3\xe4\x93\x02G\x12E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/routines'
    _globals['_ROUTINE']._serialized_start = 347
    _globals['_ROUTINE']._serialized_end = 2583
    _globals['_ROUTINE_ARGUMENT']._serialized_start = 1412
    _globals['_ROUTINE_ARGUMENT']._serialized_end = 1845
    _globals['_ROUTINE_ARGUMENT_ARGUMENTKIND']._serialized_start = 1712
    _globals['_ROUTINE_ARGUMENT_ARGUMENTKIND']._serialized_end = 1787
    _globals['_ROUTINE_ARGUMENT_MODE']._serialized_start = 1789
    _globals['_ROUTINE_ARGUMENT_MODE']._serialized_end = 1845
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS']._serialized_start = 1848
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS']._serialized_end = 2106
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS_USERDEFINEDCONTEXTENTRY']._serialized_start = 2049
    _globals['_ROUTINE_REMOTEFUNCTIONOPTIONS_USERDEFINEDCONTEXTENTRY']._serialized_end = 2106
    _globals['_ROUTINE_ROUTINETYPE']._serialized_start = 2109
    _globals['_ROUTINE_ROUTINETYPE']._serialized_end = 2239
    _globals['_ROUTINE_LANGUAGE']._serialized_start = 2241
    _globals['_ROUTINE_LANGUAGE']._serialized_end = 2335
    _globals['_ROUTINE_DETERMINISMLEVEL']._serialized_start = 2337
    _globals['_ROUTINE_DETERMINISMLEVEL']._serialized_end = 2432
    _globals['_ROUTINE_SECURITYMODE']._serialized_start = 2434
    _globals['_ROUTINE_SECURITYMODE']._serialized_end = 2505
    _globals['_ROUTINE_DATAGOVERNANCETYPE']._serialized_start = 2507
    _globals['_ROUTINE_DATAGOVERNANCETYPE']._serialized_end = 2583
    _globals['_SPARKOPTIONS']._serialized_start = 2586
    _globals['_SPARKOPTIONS']._serialized_end = 2921
    _globals['_SPARKOPTIONS_PROPERTIESENTRY']._serialized_start = 2872
    _globals['_SPARKOPTIONS_PROPERTIESENTRY']._serialized_end = 2921
    _globals['_GETROUTINEREQUEST']._serialized_start = 2923
    _globals['_GETROUTINEREQUEST']._serialized_end = 3017
    _globals['_INSERTROUTINEREQUEST']._serialized_start = 3020
    _globals['_INSERTROUTINEREQUEST']._serialized_end = 3149
    _globals['_UPDATEROUTINEREQUEST']._serialized_start = 3152
    _globals['_UPDATEROUTINEREQUEST']._serialized_end = 3306
    _globals['_PATCHROUTINEREQUEST']._serialized_start = 3309
    _globals['_PATCHROUTINEREQUEST']._serialized_end = 3510
    _globals['_DELETEROUTINEREQUEST']._serialized_start = 3512
    _globals['_DELETEROUTINEREQUEST']._serialized_end = 3609
    _globals['_LISTROUTINESREQUEST']._serialized_start = 3612
    _globals['_LISTROUTINESREQUEST']._serialized_end = 3770
    _globals['_LISTROUTINESRESPONSE']._serialized_start = 3772
    _globals['_LISTROUTINESRESPONSE']._serialized_end = 3872
    _globals['_ROUTINESERVICE']._serialized_start = 3875
    _globals['_ROUTINESERVICE']._serialized_end = 5125