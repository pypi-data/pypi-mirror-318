"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/v1/batches.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataproc.v1 import shared_pb2 as google_dot_cloud_dot_dataproc_dot_v1_dot_shared__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/dataproc/v1/batches.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/dataproc/v1/shared.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb0\x01\n\x12CreateBatchRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1ddataproc.googleapis.com/Batch\x123\n\x05batch\x18\x02 \x01(\x0b2\x1f.google.cloud.dataproc.v1.BatchB\x03\xe0A\x02\x12\x15\n\x08batch_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"F\n\x0fGetBatchRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1ddataproc.googleapis.com/Batch"\xa8\x01\n\x12ListBatchesRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1ddataproc.googleapis.com/Batch\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"z\n\x13ListBatchesResponse\x120\n\x07batches\x18\x01 \x03(\x0b2\x1f.google.cloud.dataproc.v1.Batch\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x03"I\n\x12DeleteBatchRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1ddataproc.googleapis.com/Batch"\xc8\n\n\x05Batch\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04uuid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\rpyspark_batch\x18\x04 \x01(\x0b2&.google.cloud.dataproc.v1.PySparkBatchB\x03\xe0A\x01H\x00\x12@\n\x0bspark_batch\x18\x05 \x01(\x0b2$.google.cloud.dataproc.v1.SparkBatchB\x03\xe0A\x01H\x00\x12C\n\rspark_r_batch\x18\x06 \x01(\x0b2%.google.cloud.dataproc.v1.SparkRBatchB\x03\xe0A\x01H\x00\x12G\n\x0fspark_sql_batch\x18\x07 \x01(\x0b2\'.google.cloud.dataproc.v1.SparkSqlBatchB\x03\xe0A\x01H\x00\x12@\n\x0cruntime_info\x18\x08 \x01(\x0b2%.google.cloud.dataproc.v1.RuntimeInfoB\x03\xe0A\x03\x129\n\x05state\x18\t \x01(\x0e2%.google.cloud.dataproc.v1.Batch.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\n \x01(\tB\x03\xe0A\x03\x123\n\nstate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x07creator\x18\x0c \x01(\tB\x03\xe0A\x03\x12@\n\x06labels\x18\r \x03(\x0b2+.google.cloud.dataproc.v1.Batch.LabelsEntryB\x03\xe0A\x01\x12D\n\x0eruntime_config\x18\x0e \x01(\x0b2\'.google.cloud.dataproc.v1.RuntimeConfigB\x03\xe0A\x01\x12L\n\x12environment_config\x18\x0f \x01(\x0b2+.google.cloud.dataproc.v1.EnvironmentConfigB\x03\xe0A\x01\x12\x16\n\toperation\x18\x10 \x01(\tB\x03\xe0A\x03\x12H\n\rstate_history\x18\x11 \x03(\x0b2,.google.cloud.dataproc.v1.Batch.StateHistoryB\x03\xe0A\x03\x1a\xa0\x01\n\x0cStateHistory\x129\n\x05state\x18\x01 \x01(\x0e2%.google.cloud.dataproc.v1.Batch.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x02 \x01(\tB\x03\xe0A\x03\x129\n\x10state_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"r\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\r\n\tSUCCEEDED\x10\x05\x12\n\n\x06FAILED\x10\x06:[\xeaAX\n\x1ddataproc.googleapis.com/Batch\x127projects/{project}/locations/{location}/batches/{batch}B\x0e\n\x0cbatch_config"\xb2\x01\n\x0cPySparkBatch\x12!\n\x14main_python_file_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04args\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1d\n\x10python_file_uris\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x1a\n\rjar_file_uris\x18\x04 \x03(\tB\x03\xe0A\x01\x12\x16\n\tfile_uris\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0carchive_uris\x18\x06 \x03(\tB\x03\xe0A\x01"\xb5\x01\n\nSparkBatch\x12 \n\x11main_jar_file_uri\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x12\x19\n\nmain_class\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x12\x11\n\x04args\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x1a\n\rjar_file_uris\x18\x04 \x03(\tB\x03\xe0A\x01\x12\x16\n\tfile_uris\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0carchive_uris\x18\x06 \x03(\tB\x03\xe0A\x01B\x08\n\x06driver"q\n\x0bSparkRBatch\x12\x1c\n\x0fmain_r_file_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04args\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x16\n\tfile_uris\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0carchive_uris\x18\x04 \x03(\tB\x03\xe0A\x01"\xda\x01\n\rSparkSqlBatch\x12\x1b\n\x0equery_file_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\x0fquery_variables\x18\x02 \x03(\x0b2;.google.cloud.dataproc.v1.SparkSqlBatch.QueryVariablesEntryB\x03\xe0A\x01\x12\x1a\n\rjar_file_uris\x18\x03 \x03(\tB\x03\xe0A\x01\x1a5\n\x13QueryVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\x9d\x06\n\x0fBatchController\x12\xea\x01\n\x0bCreateBatch\x12,.google.cloud.dataproc.v1.CreateBatchRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA8\n\x05Batch\x12/google.cloud.dataproc.v1.BatchOperationMetadata\xdaA\x15parent,batch,batch_id\x82\xd3\xe4\x93\x024"+/v1/{parent=projects/*/locations/*}/batches:\x05batch\x12\x92\x01\n\x08GetBatch\x12).google.cloud.dataproc.v1.GetBatchRequest\x1a\x1f.google.cloud.dataproc.v1.Batch":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/batches/*}\x12\xa8\x01\n\x0bListBatches\x12,.google.cloud.dataproc.v1.ListBatchesRequest\x1a-.google.cloud.dataproc.v1.ListBatchesResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/batches\x12\x8f\x01\n\x0bDeleteBatch\x12,.google.cloud.dataproc.v1.DeleteBatchRequest\x1a\x16.google.protobuf.Empty":\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/batches/*}\x1aK\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBk\n\x1ccom.google.cloud.dataproc.v1B\x0cBatchesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.batches_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\x0cBatchesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb'
    _globals['_CREATEBATCHREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBATCHREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\x12\x1ddataproc.googleapis.com/Batch'
    _globals['_CREATEBATCHREQUEST'].fields_by_name['batch']._loaded_options = None
    _globals['_CREATEBATCHREQUEST'].fields_by_name['batch']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBATCHREQUEST'].fields_by_name['batch_id']._loaded_options = None
    _globals['_CREATEBATCHREQUEST'].fields_by_name['batch_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEBATCHREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEBATCHREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETBATCHREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBATCHREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1ddataproc.googleapis.com/Batch'
    _globals['_LISTBATCHESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBATCHESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\x12\x1ddataproc.googleapis.com/Batch'
    _globals['_LISTBATCHESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBATCHESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBATCHESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBATCHESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBATCHESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTBATCHESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBATCHESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTBATCHESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBATCHESRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTBATCHESRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x03'
    _globals['_DELETEBATCHREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBATCHREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1ddataproc.googleapis.com/Batch'
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state']._loaded_options = None
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state_message']._loaded_options = None
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state_start_time']._loaded_options = None
    _globals['_BATCH_STATEHISTORY'].fields_by_name['state_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH_LABELSENTRY']._loaded_options = None
    _globals['_BATCH_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCH'].fields_by_name['name']._loaded_options = None
    _globals['_BATCH'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['uuid']._loaded_options = None
    _globals['_BATCH'].fields_by_name['uuid']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['create_time']._loaded_options = None
    _globals['_BATCH'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['pyspark_batch']._loaded_options = None
    _globals['_BATCH'].fields_by_name['pyspark_batch']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['spark_batch']._loaded_options = None
    _globals['_BATCH'].fields_by_name['spark_batch']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['spark_r_batch']._loaded_options = None
    _globals['_BATCH'].fields_by_name['spark_r_batch']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['spark_sql_batch']._loaded_options = None
    _globals['_BATCH'].fields_by_name['spark_sql_batch']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['runtime_info']._loaded_options = None
    _globals['_BATCH'].fields_by_name['runtime_info']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['state']._loaded_options = None
    _globals['_BATCH'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['state_message']._loaded_options = None
    _globals['_BATCH'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['state_time']._loaded_options = None
    _globals['_BATCH'].fields_by_name['state_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['creator']._loaded_options = None
    _globals['_BATCH'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['labels']._loaded_options = None
    _globals['_BATCH'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['runtime_config']._loaded_options = None
    _globals['_BATCH'].fields_by_name['runtime_config']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['environment_config']._loaded_options = None
    _globals['_BATCH'].fields_by_name['environment_config']._serialized_options = b'\xe0A\x01'
    _globals['_BATCH'].fields_by_name['operation']._loaded_options = None
    _globals['_BATCH'].fields_by_name['operation']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH'].fields_by_name['state_history']._loaded_options = None
    _globals['_BATCH'].fields_by_name['state_history']._serialized_options = b'\xe0A\x03'
    _globals['_BATCH']._loaded_options = None
    _globals['_BATCH']._serialized_options = b'\xeaAX\n\x1ddataproc.googleapis.com/Batch\x127projects/{project}/locations/{location}/batches/{batch}'
    _globals['_PYSPARKBATCH'].fields_by_name['main_python_file_uri']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['main_python_file_uri']._serialized_options = b'\xe0A\x02'
    _globals['_PYSPARKBATCH'].fields_by_name['args']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['args']._serialized_options = b'\xe0A\x01'
    _globals['_PYSPARKBATCH'].fields_by_name['python_file_uris']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['python_file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_PYSPARKBATCH'].fields_by_name['jar_file_uris']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['jar_file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_PYSPARKBATCH'].fields_by_name['file_uris']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_PYSPARKBATCH'].fields_by_name['archive_uris']._loaded_options = None
    _globals['_PYSPARKBATCH'].fields_by_name['archive_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['main_jar_file_uri']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['main_jar_file_uri']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['main_class']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['main_class']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['args']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['args']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['jar_file_uris']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['jar_file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['file_uris']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKBATCH'].fields_by_name['archive_uris']._loaded_options = None
    _globals['_SPARKBATCH'].fields_by_name['archive_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKRBATCH'].fields_by_name['main_r_file_uri']._loaded_options = None
    _globals['_SPARKRBATCH'].fields_by_name['main_r_file_uri']._serialized_options = b'\xe0A\x02'
    _globals['_SPARKRBATCH'].fields_by_name['args']._loaded_options = None
    _globals['_SPARKRBATCH'].fields_by_name['args']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKRBATCH'].fields_by_name['file_uris']._loaded_options = None
    _globals['_SPARKRBATCH'].fields_by_name['file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKRBATCH'].fields_by_name['archive_uris']._loaded_options = None
    _globals['_SPARKRBATCH'].fields_by_name['archive_uris']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKSQLBATCH_QUERYVARIABLESENTRY']._loaded_options = None
    _globals['_SPARKSQLBATCH_QUERYVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_SPARKSQLBATCH'].fields_by_name['query_file_uri']._loaded_options = None
    _globals['_SPARKSQLBATCH'].fields_by_name['query_file_uri']._serialized_options = b'\xe0A\x02'
    _globals['_SPARKSQLBATCH'].fields_by_name['query_variables']._loaded_options = None
    _globals['_SPARKSQLBATCH'].fields_by_name['query_variables']._serialized_options = b'\xe0A\x01'
    _globals['_SPARKSQLBATCH'].fields_by_name['jar_file_uris']._loaded_options = None
    _globals['_SPARKSQLBATCH'].fields_by_name['jar_file_uris']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHCONTROLLER']._loaded_options = None
    _globals['_BATCHCONTROLLER']._serialized_options = b'\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BATCHCONTROLLER'].methods_by_name['CreateBatch']._loaded_options = None
    _globals['_BATCHCONTROLLER'].methods_by_name['CreateBatch']._serialized_options = b'\xcaA8\n\x05Batch\x12/google.cloud.dataproc.v1.BatchOperationMetadata\xdaA\x15parent,batch,batch_id\x82\xd3\xe4\x93\x024"+/v1/{parent=projects/*/locations/*}/batches:\x05batch'
    _globals['_BATCHCONTROLLER'].methods_by_name['GetBatch']._loaded_options = None
    _globals['_BATCHCONTROLLER'].methods_by_name['GetBatch']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/batches/*}'
    _globals['_BATCHCONTROLLER'].methods_by_name['ListBatches']._loaded_options = None
    _globals['_BATCHCONTROLLER'].methods_by_name['ListBatches']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/batches'
    _globals['_BATCHCONTROLLER'].methods_by_name['DeleteBatch']._loaded_options = None
    _globals['_BATCHCONTROLLER'].methods_by_name['DeleteBatch']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/batches/*}'
    _globals['_CREATEBATCHREQUEST']._serialized_start = 322
    _globals['_CREATEBATCHREQUEST']._serialized_end = 498
    _globals['_GETBATCHREQUEST']._serialized_start = 500
    _globals['_GETBATCHREQUEST']._serialized_end = 570
    _globals['_LISTBATCHESREQUEST']._serialized_start = 573
    _globals['_LISTBATCHESREQUEST']._serialized_end = 741
    _globals['_LISTBATCHESRESPONSE']._serialized_start = 743
    _globals['_LISTBATCHESRESPONSE']._serialized_end = 865
    _globals['_DELETEBATCHREQUEST']._serialized_start = 867
    _globals['_DELETEBATCHREQUEST']._serialized_end = 940
    _globals['_BATCH']._serialized_start = 943
    _globals['_BATCH']._serialized_end = 2295
    _globals['_BATCH_STATEHISTORY']._serialized_start = 1863
    _globals['_BATCH_STATEHISTORY']._serialized_end = 2023
    _globals['_BATCH_LABELSENTRY']._serialized_start = 2025
    _globals['_BATCH_LABELSENTRY']._serialized_end = 2070
    _globals['_BATCH_STATE']._serialized_start = 2072
    _globals['_BATCH_STATE']._serialized_end = 2186
    _globals['_PYSPARKBATCH']._serialized_start = 2298
    _globals['_PYSPARKBATCH']._serialized_end = 2476
    _globals['_SPARKBATCH']._serialized_start = 2479
    _globals['_SPARKBATCH']._serialized_end = 2660
    _globals['_SPARKRBATCH']._serialized_start = 2662
    _globals['_SPARKRBATCH']._serialized_end = 2775
    _globals['_SPARKSQLBATCH']._serialized_start = 2778
    _globals['_SPARKSQLBATCH']._serialized_end = 2996
    _globals['_SPARKSQLBATCH_QUERYVARIABLESENTRY']._serialized_start = 2943
    _globals['_SPARKSQLBATCH_QUERYVARIABLESENTRY']._serialized_end = 2996
    _globals['_BATCHCONTROLLER']._serialized_start = 2999
    _globals['_BATCHCONTROLLER']._serialized_end = 3796