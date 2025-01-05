"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta1/storage.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1beta1 import arrow_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta1_dot_arrow__pb2
from ......google.cloud.bigquery.storage.v1beta1 import avro_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta1_dot_avro__pb2
from ......google.cloud.bigquery.storage.v1beta1 import read_options_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta1_dot_read__options__pb2
from ......google.cloud.bigquery.storage.v1beta1 import table_reference_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta1_dot_table__reference__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/bigquery/storage/v1beta1/storage.proto\x12%google.cloud.bigquery.storage.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/bigquery/storage/v1beta1/arrow.proto\x1a0google/cloud/bigquery/storage/v1beta1/avro.proto\x1a8google/cloud/bigquery/storage/v1beta1/read_options.proto\x1a;google/cloud/bigquery/storage/v1beta1/table_reference.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"|\n\x06Stream\x12\x0c\n\x04name\x18\x01 \x01(\t:d\xeaAa\n%bigquerystorage.googleapis.com/Stream\x128projects/{project}/locations/{location}/streams/{stream}"_\n\x0eStreamPosition\x12=\n\x06stream\x18\x01 \x01(\x0b2-.google.cloud.bigquery.storage.v1beta1.Stream\x12\x0e\n\x06offset\x18\x02 \x01(\x03"\x8d\x05\n\x0bReadSession\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12H\n\x0bavro_schema\x18\x05 \x01(\x0b21.google.cloud.bigquery.storage.v1beta1.AvroSchemaH\x00\x12J\n\x0carrow_schema\x18\x06 \x01(\x0b22.google.cloud.bigquery.storage.v1beta1.ArrowSchemaH\x00\x12>\n\x07streams\x18\x04 \x03(\x0b2-.google.cloud.bigquery.storage.v1beta1.Stream\x12N\n\x0ftable_reference\x18\x07 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.TableReference\x12N\n\x0ftable_modifiers\x18\x08 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.TableModifiers\x12R\n\x11sharding_strategy\x18\t \x01(\x0e27.google.cloud.bigquery.storage.v1beta1.ShardingStrategy:k\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}B\x08\n\x06schema"\x85\x04\n\x18CreateReadSessionRequest\x12S\n\x0ftable_reference\x18\x01 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.TableReferenceB\x03\xe0A\x02\x12C\n\x06parent\x18\x06 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12N\n\x0ftable_modifiers\x18\x02 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.TableModifiers\x12\x19\n\x11requested_streams\x18\x03 \x01(\x05\x12M\n\x0cread_options\x18\x04 \x01(\x0b27.google.cloud.bigquery.storage.v1beta1.TableReadOptions\x12A\n\x06format\x18\x05 \x01(\x0e21.google.cloud.bigquery.storage.v1beta1.DataFormat\x12R\n\x11sharding_strategy\x18\x07 \x01(\x0e27.google.cloud.bigquery.storage.v1beta1.ShardingStrategy"d\n\x0fReadRowsRequest\x12Q\n\rread_position\x18\x01 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.StreamPositionB\x03\xe0A\x02"\xa0\x01\n\x0cStreamStatus\x12\x1b\n\x13estimated_row_count\x18\x01 \x01(\x03\x12\x19\n\x11fraction_consumed\x18\x02 \x01(\x02\x12A\n\x08progress\x18\x04 \x01(\x0b2/.google.cloud.bigquery.storage.v1beta1.Progress\x12\x15\n\ris_splittable\x18\x03 \x01(\x08">\n\x08Progress\x12\x19\n\x11at_response_start\x18\x01 \x01(\x02\x12\x17\n\x0fat_response_end\x18\x02 \x01(\x02"*\n\x0eThrottleStatus\x12\x18\n\x10throttle_percent\x18\x01 \x01(\x05"\x89\x04\n\x10ReadRowsResponse\x12D\n\tavro_rows\x18\x03 \x01(\x0b2/.google.cloud.bigquery.storage.v1beta1.AvroRowsH\x00\x12U\n\x12arrow_record_batch\x18\x04 \x01(\x0b27.google.cloud.bigquery.storage.v1beta1.ArrowRecordBatchH\x00\x12\x11\n\trow_count\x18\x06 \x01(\x03\x12C\n\x06status\x18\x02 \x01(\x0b23.google.cloud.bigquery.storage.v1beta1.StreamStatus\x12N\n\x0fthrottle_status\x18\x05 \x01(\x0b25.google.cloud.bigquery.storage.v1beta1.ThrottleStatus\x12M\n\x0bavro_schema\x18\x07 \x01(\x0b21.google.cloud.bigquery.storage.v1beta1.AvroSchemaB\x03\xe0A\x03H\x01\x12O\n\x0carrow_schema\x18\x08 \x01(\x0b22.google.cloud.bigquery.storage.v1beta1.ArrowSchemaB\x03\xe0A\x03H\x01B\x06\n\x04rowsB\x08\n\x06schema"\x90\x01\n$BatchCreateReadSessionStreamsRequest\x12H\n\x07session\x18\x01 \x01(\x0b22.google.cloud.bigquery.storage.v1beta1.ReadSessionB\x03\xe0A\x02\x12\x1e\n\x11requested_streams\x18\x02 \x01(\x05B\x03\xe0A\x02"g\n%BatchCreateReadSessionStreamsResponse\x12>\n\x07streams\x18\x01 \x03(\x0b2-.google.cloud.bigquery.storage.v1beta1.Stream"[\n\x15FinalizeStreamRequest\x12B\n\x06stream\x18\x02 \x01(\x0b2-.google.cloud.bigquery.storage.v1beta1.StreamB\x03\xe0A\x02"w\n\x16SplitReadStreamRequest\x12K\n\x0foriginal_stream\x18\x01 \x01(\x0b2-.google.cloud.bigquery.storage.v1beta1.StreamB\x03\xe0A\x02\x12\x10\n\x08fraction\x18\x02 \x01(\x02"\xa9\x01\n\x17SplitReadStreamResponse\x12E\n\x0eprimary_stream\x18\x01 \x01(\x0b2-.google.cloud.bigquery.storage.v1beta1.Stream\x12G\n\x10remainder_stream\x18\x02 \x01(\x0b2-.google.cloud.bigquery.storage.v1beta1.Stream*>\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04AVRO\x10\x01\x12\t\n\x05ARROW\x10\x03*O\n\x10ShardingStrategy\x12!\n\x1dSHARDING_STRATEGY_UNSPECIFIED\x10\x00\x12\n\n\x06LIQUID\x10\x01\x12\x0c\n\x08BALANCED\x10\x022\xb7\n\n\x0fBigQueryStorage\x12\xb3\x02\n\x11CreateReadSession\x12?.google.cloud.bigquery.storage.v1beta1.CreateReadSessionRequest\x1a2.google.cloud.bigquery.storage.v1beta1.ReadSession"\xa8\x01\xdaA(table_reference,parent,requested_streams\x82\xd3\xe4\x93\x02w"0/v1beta1/{table_reference.project_id=projects/*}:\x01*Z@";/v1beta1/{table_reference.dataset_id=projects/*/datasets/*}:\x01*\x12\xd0\x01\n\x08ReadRows\x126.google.cloud.bigquery.storage.v1beta1.ReadRowsRequest\x1a7.google.cloud.bigquery.storage.v1beta1.ReadRowsResponse"Q\xdaA\rread_position\x82\xd3\xe4\x93\x02;\x129/v1beta1/{read_position.stream.name=projects/*/streams/*}0\x01\x12\x90\x02\n\x1dBatchCreateReadSessionStreams\x12K.google.cloud.bigquery.storage.v1beta1.BatchCreateReadSessionStreamsRequest\x1aL.google.cloud.bigquery.storage.v1beta1.BatchCreateReadSessionStreamsResponse"T\xdaA\x19session,requested_streams\x82\xd3\xe4\x93\x022"-/v1beta1/{session.name=projects/*/sessions/*}:\x01*\x12\xa7\x01\n\x0eFinalizeStream\x12<.google.cloud.bigquery.storage.v1beta1.FinalizeStreamRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x06stream\x82\xd3\xe4\x93\x020"+/v1beta1/{stream.name=projects/*/streams/*}:\x01*\x12\xe0\x01\n\x0fSplitReadStream\x12=.google.cloud.bigquery.storage.v1beta1.SplitReadStreamRequest\x1a>.google.cloud.bigquery.storage.v1beta1.SplitReadStreamResponse"N\xdaA\x0foriginal_stream\x82\xd3\xe4\x93\x026\x124/v1beta1/{original_stream.name=projects/*/streams/*}\x1a{\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformBp\n)com.google.cloud.bigquery.storage.v1beta1ZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta1.storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta1ZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepb'
    _globals['_STREAM']._loaded_options = None
    _globals['_STREAM']._serialized_options = b'\xeaAa\n%bigquerystorage.googleapis.com/Stream\x128projects/{project}/locations/{location}/streams/{stream}'
    _globals['_READSESSION']._loaded_options = None
    _globals['_READSESSION']._serialized_options = b'\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['table_reference']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['table_reference']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_READROWSREQUEST'].fields_by_name['read_position']._loaded_options = None
    _globals['_READROWSREQUEST'].fields_by_name['read_position']._serialized_options = b'\xe0A\x02'
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST'].fields_by_name['requested_streams']._loaded_options = None
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST'].fields_by_name['requested_streams']._serialized_options = b'\xe0A\x02'
    _globals['_FINALIZESTREAMREQUEST'].fields_by_name['stream']._loaded_options = None
    _globals['_FINALIZESTREAMREQUEST'].fields_by_name['stream']._serialized_options = b'\xe0A\x02'
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['original_stream']._loaded_options = None
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['original_stream']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSTORAGE']._loaded_options = None
    _globals['_BIGQUERYSTORAGE']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BIGQUERYSTORAGE'].methods_by_name['CreateReadSession']._loaded_options = None
    _globals['_BIGQUERYSTORAGE'].methods_by_name['CreateReadSession']._serialized_options = b'\xdaA(table_reference,parent,requested_streams\x82\xd3\xe4\x93\x02w"0/v1beta1/{table_reference.project_id=projects/*}:\x01*Z@";/v1beta1/{table_reference.dataset_id=projects/*/datasets/*}:\x01*'
    _globals['_BIGQUERYSTORAGE'].methods_by_name['ReadRows']._loaded_options = None
    _globals['_BIGQUERYSTORAGE'].methods_by_name['ReadRows']._serialized_options = b'\xdaA\rread_position\x82\xd3\xe4\x93\x02;\x129/v1beta1/{read_position.stream.name=projects/*/streams/*}'
    _globals['_BIGQUERYSTORAGE'].methods_by_name['BatchCreateReadSessionStreams']._loaded_options = None
    _globals['_BIGQUERYSTORAGE'].methods_by_name['BatchCreateReadSessionStreams']._serialized_options = b'\xdaA\x19session,requested_streams\x82\xd3\xe4\x93\x022"-/v1beta1/{session.name=projects/*/sessions/*}:\x01*'
    _globals['_BIGQUERYSTORAGE'].methods_by_name['FinalizeStream']._loaded_options = None
    _globals['_BIGQUERYSTORAGE'].methods_by_name['FinalizeStream']._serialized_options = b'\xdaA\x06stream\x82\xd3\xe4\x93\x020"+/v1beta1/{stream.name=projects/*/streams/*}:\x01*'
    _globals['_BIGQUERYSTORAGE'].methods_by_name['SplitReadStream']._loaded_options = None
    _globals['_BIGQUERYSTORAGE'].methods_by_name['SplitReadStream']._serialized_options = b'\xdaA\x0foriginal_stream\x82\xd3\xe4\x93\x026\x124/v1beta1/{original_stream.name=projects/*/streams/*}'
    _globals['_DATAFORMAT']._serialized_start = 3425
    _globals['_DATAFORMAT']._serialized_end = 3487
    _globals['_SHARDINGSTRATEGY']._serialized_start = 3489
    _globals['_SHARDINGSTRATEGY']._serialized_end = 3568
    _globals['_STREAM']._serialized_start = 491
    _globals['_STREAM']._serialized_end = 615
    _globals['_STREAMPOSITION']._serialized_start = 617
    _globals['_STREAMPOSITION']._serialized_end = 712
    _globals['_READSESSION']._serialized_start = 715
    _globals['_READSESSION']._serialized_end = 1368
    _globals['_CREATEREADSESSIONREQUEST']._serialized_start = 1371
    _globals['_CREATEREADSESSIONREQUEST']._serialized_end = 1888
    _globals['_READROWSREQUEST']._serialized_start = 1890
    _globals['_READROWSREQUEST']._serialized_end = 1990
    _globals['_STREAMSTATUS']._serialized_start = 1993
    _globals['_STREAMSTATUS']._serialized_end = 2153
    _globals['_PROGRESS']._serialized_start = 2155
    _globals['_PROGRESS']._serialized_end = 2217
    _globals['_THROTTLESTATUS']._serialized_start = 2219
    _globals['_THROTTLESTATUS']._serialized_end = 2261
    _globals['_READROWSRESPONSE']._serialized_start = 2264
    _globals['_READROWSRESPONSE']._serialized_end = 2785
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST']._serialized_start = 2788
    _globals['_BATCHCREATEREADSESSIONSTREAMSREQUEST']._serialized_end = 2932
    _globals['_BATCHCREATEREADSESSIONSTREAMSRESPONSE']._serialized_start = 2934
    _globals['_BATCHCREATEREADSESSIONSTREAMSRESPONSE']._serialized_end = 3037
    _globals['_FINALIZESTREAMREQUEST']._serialized_start = 3039
    _globals['_FINALIZESTREAMREQUEST']._serialized_end = 3130
    _globals['_SPLITREADSTREAMREQUEST']._serialized_start = 3132
    _globals['_SPLITREADSTREAMREQUEST']._serialized_end = 3251
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_start = 3254
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_end = 3423
    _globals['_BIGQUERYSTORAGE']._serialized_start = 3571
    _globals['_BIGQUERYSTORAGE']._serialized_end = 4906