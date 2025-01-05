"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta2/storage.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1beta2 import arrow_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_arrow__pb2
from ......google.cloud.bigquery.storage.v1beta2 import avro_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_avro__pb2
from ......google.cloud.bigquery.storage.v1beta2 import protobuf_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_protobuf__pb2
from ......google.cloud.bigquery.storage.v1beta2 import stream_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_stream__pb2
from ......google.cloud.bigquery.storage.v1beta2 import table_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_table__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/bigquery/storage/v1beta2/storage.proto\x12%google.cloud.bigquery.storage.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/bigquery/storage/v1beta2/arrow.proto\x1a0google/cloud/bigquery/storage/v1beta2/avro.proto\x1a4google/cloud/bigquery/storage/v1beta2/protobuf.proto\x1a2google/cloud/bigquery/storage/v1beta2/stream.proto\x1a1google/cloud/bigquery/storage/v1beta2/table.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xc8\x01\n\x18CreateReadSessionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12M\n\x0cread_session\x18\x02 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.ReadSessionB\x03\xe0A\x02\x12\x18\n\x10max_stream_count\x18\x03 \x01(\x05"i\n\x0fReadRowsRequest\x12F\n\x0bread_stream\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream\x12\x0e\n\x06offset\x18\x02 \x01(\x03")\n\rThrottleState\x12\x18\n\x10throttle_percent\x18\x01 \x01(\x05"\x9c\x01\n\x0bStreamStats\x12M\n\x08progress\x18\x02 \x01(\x0b2;.google.cloud.bigquery.storage.v1beta2.StreamStats.Progress\x1a>\n\x08Progress\x12\x19\n\x11at_response_start\x18\x01 \x01(\x01\x12\x17\n\x0fat_response_end\x18\x02 \x01(\x01"\x85\x04\n\x10ReadRowsResponse\x12D\n\tavro_rows\x18\x03 \x01(\x0b2/.google.cloud.bigquery.storage.v1beta2.AvroRowsH\x00\x12U\n\x12arrow_record_batch\x18\x04 \x01(\x0b27.google.cloud.bigquery.storage.v1beta2.ArrowRecordBatchH\x00\x12\x11\n\trow_count\x18\x06 \x01(\x03\x12A\n\x05stats\x18\x02 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.StreamStats\x12L\n\x0ethrottle_state\x18\x05 \x01(\x0b24.google.cloud.bigquery.storage.v1beta2.ThrottleState\x12M\n\x0bavro_schema\x18\x07 \x01(\x0b21.google.cloud.bigquery.storage.v1beta2.AvroSchemaB\x03\xe0A\x03H\x01\x12O\n\x0carrow_schema\x18\x08 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.ArrowSchemaB\x03\xe0A\x03H\x01B\x06\n\x04rowsB\x08\n\x06schema"k\n\x16SplitReadStreamRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream\x12\x10\n\x08fraction\x18\x02 \x01(\x01"\xb1\x01\n\x17SplitReadStreamResponse\x12I\n\x0eprimary_stream\x18\x01 \x01(\x0b21.google.cloud.bigquery.storage.v1beta2.ReadStream\x12K\n\x10remainder_stream\x18\x02 \x01(\x0b21.google.cloud.bigquery.storage.v1beta2.ReadStream"\xa0\x01\n\x18CreateWriteStreamRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12M\n\x0cwrite_stream\x18\x02 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.WriteStreamB\x03\xe0A\x02"\x97\x03\n\x11AppendRowsRequest\x12H\n\x0cwrite_stream\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream\x12+\n\x06offset\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12X\n\nproto_rows\x18\x04 \x01(\x0b2B.google.cloud.bigquery.storage.v1beta2.AppendRowsRequest.ProtoDataH\x00\x12\x10\n\x08trace_id\x18\x06 \x01(\t\x1a\x96\x01\n\tProtoData\x12I\n\rwriter_schema\x18\x01 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.ProtoSchema\x12>\n\x04rows\x18\x02 \x01(\x0b20.google.cloud.bigquery.storage.v1beta2.ProtoRowsB\x06\n\x04rows"\xaf\x02\n\x12AppendRowsResponse\x12_\n\rappend_result\x18\x01 \x01(\x0b2F.google.cloud.bigquery.storage.v1beta2.AppendRowsResponse.AppendResultH\x00\x12#\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00\x12J\n\x0eupdated_schema\x18\x03 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.TableSchema\x1a;\n\x0cAppendResult\x12+\n\x06offset\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\n\n\x08response"Y\n\x15GetWriteStreamRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream"Q\n\x1eBatchCommitWriteStreamsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rwrite_streams\x18\x02 \x03(\tB\x03\xe0A\x02"\x9e\x01\n\x1fBatchCommitWriteStreamsResponse\x12/\n\x0bcommit_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12J\n\rstream_errors\x18\x02 \x03(\x0b23.google.cloud.bigquery.storage.v1beta2.StorageError"^\n\x1aFinalizeWriteStreamRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream"0\n\x1bFinalizeWriteStreamResponse\x12\x11\n\trow_count\x18\x01 \x01(\x03"\x89\x01\n\x10FlushRowsRequest\x12H\n\x0cwrite_stream\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream\x12+\n\x06offset\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64Value"#\n\x11FlushRowsResponse\x12\x0e\n\x06offset\x18\x01 \x01(\x03"\xd4\x02\n\x0cStorageError\x12R\n\x04code\x18\x01 \x01(\x0e2D.google.cloud.bigquery.storage.v1beta2.StorageError.StorageErrorCode\x12\x0e\n\x06entity\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t"\xc8\x01\n\x10StorageErrorCode\x12"\n\x1eSTORAGE_ERROR_CODE_UNSPECIFIED\x10\x00\x12\x13\n\x0fTABLE_NOT_FOUND\x10\x01\x12\x1c\n\x18STREAM_ALREADY_COMMITTED\x10\x02\x12\x14\n\x10STREAM_NOT_FOUND\x10\x03\x12\x17\n\x13INVALID_STREAM_TYPE\x10\x04\x12\x18\n\x14INVALID_STREAM_STATE\x10\x05\x12\x14\n\x10STREAM_FINALIZED\x10\x062\xbf\x06\n\x0cBigQueryRead\x12\xf8\x01\n\x11CreateReadSession\x12?.google.cloud.bigquery.storage.v1beta2.CreateReadSessionRequest\x1a2.google.cloud.bigquery.storage.v1beta2.ReadSession"n\xdaA$parent,read_session,max_stream_count\x82\xd3\xe4\x93\x02A"</v1beta2/{read_session.table=projects/*/datasets/*/tables/*}:\x01*\x12\xde\x01\n\x08ReadRows\x126.google.cloud.bigquery.storage.v1beta2.ReadRowsRequest\x1a7.google.cloud.bigquery.storage.v1beta2.ReadRowsResponse"_\xdaA\x12read_stream,offset\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{read_stream=projects/*/locations/*/sessions/*/streams/*}0\x01\x12\xd5\x01\n\x0fSplitReadStream\x12=.google.cloud.bigquery.storage.v1beta2.SplitReadStreamRequest\x1a>.google.cloud.bigquery.storage.v1beta2.SplitReadStreamResponse"C\x82\xd3\xe4\x93\x02=\x12;/v1beta2/{name=projects/*/locations/*/sessions/*/streams/*}\x1a{\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform2\xab\x0c\n\rBigQueryWrite\x12\xe9\x01\n\x11CreateWriteStream\x12?.google.cloud.bigquery.storage.v1beta2.CreateWriteStreamRequest\x1a2.google.cloud.bigquery.storage.v1beta2.WriteStream"_\x88\x02\x01\xdaA\x13parent,write_stream\x82\xd3\xe4\x93\x02@"0/v1beta2/{parent=projects/*/datasets/*/tables/*}:\x0cwrite_stream\x12\xe4\x01\n\nAppendRows\x128.google.cloud.bigquery.storage.v1beta2.AppendRowsRequest\x1a9.google.cloud.bigquery.storage.v1beta2.AppendRowsResponse"]\x88\x02\x01\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02E"@/v1beta2/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*(\x010\x01\x12\xd1\x01\n\x0eGetWriteStream\x12<.google.cloud.bigquery.storage.v1beta2.GetWriteStreamRequest\x1a2.google.cloud.bigquery.storage.v1beta2.WriteStream"M\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta2/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*\x12\xeb\x01\n\x13FinalizeWriteStream\x12A.google.cloud.bigquery.storage.v1beta2.FinalizeWriteStreamRequest\x1aB.google.cloud.bigquery.storage.v1beta2.FinalizeWriteStreamResponse"M\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta2/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*\x12\xee\x01\n\x17BatchCommitWriteStreams\x12E.google.cloud.bigquery.storage.v1beta2.BatchCommitWriteStreamsRequest\x1aF.google.cloud.bigquery.storage.v1beta2.BatchCommitWriteStreamsResponse"D\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta2/{parent=projects/*/datasets/*/tables/*}\x12\xdd\x01\n\tFlushRows\x127.google.cloud.bigquery.storage.v1beta2.FlushRowsRequest\x1a8.google.cloud.bigquery.storage.v1beta2.FlushRowsResponse"]\x88\x02\x01\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02E"@/v1beta2/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*\x1a\xb3\x01\x88\x02\x01\xcaA\x1ebigquerystorage.googleapis.com\xd2A\x8b\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/bigquery.insertdata,https://www.googleapis.com/auth/cloud-platformB\x80\x01\n)com.google.cloud.bigquery.storage.v1beta2B\x0cStorageProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta2.storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta2B\x0cStorageProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepb'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['read_session']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['read_session']._serialized_options = b'\xe0A\x02'
    _globals['_READROWSREQUEST'].fields_by_name['read_stream']._loaded_options = None
    _globals['_READROWSREQUEST'].fields_by_name['read_stream']._serialized_options = b'\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream'
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._serialized_options = b'\xe0A\x03'
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream'
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDROWSREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_APPENDROWSREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_GETWRITESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWRITESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['write_streams']._loaded_options = None
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['write_streams']._serialized_options = b'\xe0A\x02'
    _globals['_FINALIZEWRITESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FINALIZEWRITESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_FLUSHROWSREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_FLUSHROWSREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_BIGQUERYREAD']._loaded_options = None
    _globals['_BIGQUERYREAD']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BIGQUERYREAD'].methods_by_name['CreateReadSession']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['CreateReadSession']._serialized_options = b'\xdaA$parent,read_session,max_stream_count\x82\xd3\xe4\x93\x02A"</v1beta2/{read_session.table=projects/*/datasets/*/tables/*}:\x01*'
    _globals['_BIGQUERYREAD'].methods_by_name['ReadRows']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['ReadRows']._serialized_options = b'\xdaA\x12read_stream,offset\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{read_stream=projects/*/locations/*/sessions/*/streams/*}'
    _globals['_BIGQUERYREAD'].methods_by_name['SplitReadStream']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['SplitReadStream']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/v1beta2/{name=projects/*/locations/*/sessions/*/streams/*}'
    _globals['_BIGQUERYWRITE']._loaded_options = None
    _globals['_BIGQUERYWRITE']._serialized_options = b'\x88\x02\x01\xcaA\x1ebigquerystorage.googleapis.com\xd2A\x8b\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/bigquery.insertdata,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BIGQUERYWRITE'].methods_by_name['CreateWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['CreateWriteStream']._serialized_options = b'\x88\x02\x01\xdaA\x13parent,write_stream\x82\xd3\xe4\x93\x02@"0/v1beta2/{parent=projects/*/datasets/*/tables/*}:\x0cwrite_stream'
    _globals['_BIGQUERYWRITE'].methods_by_name['AppendRows']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['AppendRows']._serialized_options = b'\x88\x02\x01\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02E"@/v1beta2/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['GetWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['GetWriteStream']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta2/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['FinalizeWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['FinalizeWriteStream']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta2/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['BatchCommitWriteStreams']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['BatchCommitWriteStreams']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta2/{parent=projects/*/datasets/*/tables/*}'
    _globals['_BIGQUERYWRITE'].methods_by_name['FlushRows']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['FlushRows']._serialized_options = b'\x88\x02\x01\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02E"@/v1beta2/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_CREATEREADSESSIONREQUEST']._serialized_start = 558
    _globals['_CREATEREADSESSIONREQUEST']._serialized_end = 758
    _globals['_READROWSREQUEST']._serialized_start = 760
    _globals['_READROWSREQUEST']._serialized_end = 865
    _globals['_THROTTLESTATE']._serialized_start = 867
    _globals['_THROTTLESTATE']._serialized_end = 908
    _globals['_STREAMSTATS']._serialized_start = 911
    _globals['_STREAMSTATS']._serialized_end = 1067
    _globals['_STREAMSTATS_PROGRESS']._serialized_start = 1005
    _globals['_STREAMSTATS_PROGRESS']._serialized_end = 1067
    _globals['_READROWSRESPONSE']._serialized_start = 1070
    _globals['_READROWSRESPONSE']._serialized_end = 1587
    _globals['_SPLITREADSTREAMREQUEST']._serialized_start = 1589
    _globals['_SPLITREADSTREAMREQUEST']._serialized_end = 1696
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_start = 1699
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_end = 1876
    _globals['_CREATEWRITESTREAMREQUEST']._serialized_start = 1879
    _globals['_CREATEWRITESTREAMREQUEST']._serialized_end = 2039
    _globals['_APPENDROWSREQUEST']._serialized_start = 2042
    _globals['_APPENDROWSREQUEST']._serialized_end = 2449
    _globals['_APPENDROWSREQUEST_PROTODATA']._serialized_start = 2291
    _globals['_APPENDROWSREQUEST_PROTODATA']._serialized_end = 2441
    _globals['_APPENDROWSRESPONSE']._serialized_start = 2452
    _globals['_APPENDROWSRESPONSE']._serialized_end = 2755
    _globals['_APPENDROWSRESPONSE_APPENDRESULT']._serialized_start = 2684
    _globals['_APPENDROWSRESPONSE_APPENDRESULT']._serialized_end = 2743
    _globals['_GETWRITESTREAMREQUEST']._serialized_start = 2757
    _globals['_GETWRITESTREAMREQUEST']._serialized_end = 2846
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST']._serialized_start = 2848
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST']._serialized_end = 2929
    _globals['_BATCHCOMMITWRITESTREAMSRESPONSE']._serialized_start = 2932
    _globals['_BATCHCOMMITWRITESTREAMSRESPONSE']._serialized_end = 3090
    _globals['_FINALIZEWRITESTREAMREQUEST']._serialized_start = 3092
    _globals['_FINALIZEWRITESTREAMREQUEST']._serialized_end = 3186
    _globals['_FINALIZEWRITESTREAMRESPONSE']._serialized_start = 3188
    _globals['_FINALIZEWRITESTREAMRESPONSE']._serialized_end = 3236
    _globals['_FLUSHROWSREQUEST']._serialized_start = 3239
    _globals['_FLUSHROWSREQUEST']._serialized_end = 3376
    _globals['_FLUSHROWSRESPONSE']._serialized_start = 3378
    _globals['_FLUSHROWSRESPONSE']._serialized_end = 3413
    _globals['_STORAGEERROR']._serialized_start = 3416
    _globals['_STORAGEERROR']._serialized_end = 3756
    _globals['_STORAGEERROR_STORAGEERRORCODE']._serialized_start = 3556
    _globals['_STORAGEERROR_STORAGEERRORCODE']._serialized_end = 3756
    _globals['_BIGQUERYREAD']._serialized_start = 3759
    _globals['_BIGQUERYREAD']._serialized_end = 4590
    _globals['_BIGQUERYWRITE']._serialized_start = 4593
    _globals['_BIGQUERYWRITE']._serialized_end = 6172