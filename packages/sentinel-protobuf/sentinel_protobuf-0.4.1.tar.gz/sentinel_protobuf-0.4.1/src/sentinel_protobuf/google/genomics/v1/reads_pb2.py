"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/reads.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.genomics.v1 import range_pb2 as google_dot_genomics_dot_v1_dot_range__pb2
from ....google.genomics.v1 import readalignment_pb2 as google_dot_genomics_dot_v1_dot_readalignment__pb2
from ....google.genomics.v1 import readgroupset_pb2 as google_dot_genomics_dot_v1_dot_readgroupset__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/genomics/v1/reads.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/genomics/v1/range.proto\x1a&google/genomics/v1/readalignment.proto\x1a%google/genomics/v1/readgroupset.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"f\n\x1aSearchReadGroupSetsRequest\x12\x13\n\x0bdataset_ids\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"q\n\x1bSearchReadGroupSetsResponse\x129\n\x0fread_group_sets\x18\x01 \x03(\x0b2 .google.genomics.v1.ReadGroupSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9e\x02\n\x1aImportReadGroupSetsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x18\n\x10reference_set_id\x18\x04 \x01(\t\x12\x13\n\x0bsource_uris\x18\x02 \x03(\t\x12\\\n\x12partition_strategy\x18\x05 \x01(\x0e2@.google.genomics.v1.ImportReadGroupSetsRequest.PartitionStrategy"_\n\x11PartitionStrategy\x12"\n\x1ePARTITION_STRATEGY_UNSPECIFIED\x10\x00\x12\x17\n\x13PER_FILE_PER_SAMPLE\x10\x01\x12\r\n\tMERGE_ALL\x10\x02"9\n\x1bImportReadGroupSetsResponse\x12\x1a\n\x12read_group_set_ids\x18\x01 \x03(\t"w\n\x19ExportReadGroupSetRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\nexport_uri\x18\x02 \x01(\t\x12\x19\n\x11read_group_set_id\x18\x03 \x01(\t\x12\x17\n\x0freference_names\x18\x04 \x03(\t"\xa1\x01\n\x19UpdateReadGroupSetRequest\x12\x19\n\x11read_group_set_id\x18\x01 \x01(\t\x128\n\x0eread_group_set\x18\x02 \x01(\x0b2 .google.genomics.v1.ReadGroupSet\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"6\n\x19DeleteReadGroupSetRequest\x12\x19\n\x11read_group_set_id\x18\x01 \x01(\t"3\n\x16GetReadGroupSetRequest\x12\x19\n\x11read_group_set_id\x18\x01 \x01(\t"\xaf\x01\n\x1aListCoverageBucketsRequest\x12\x19\n\x11read_group_set_id\x18\x01 \x01(\t\x12\x16\n\x0ereference_name\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03end\x18\x05 \x01(\x03\x12\x1b\n\x13target_bucket_width\x18\x06 \x01(\x03\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x11\n\tpage_size\x18\x08 \x01(\x05"Q\n\x0eCoverageBucket\x12(\n\x05range\x18\x01 \x01(\x0b2\x19.google.genomics.v1.Range\x12\x15\n\rmean_coverage\x18\x02 \x01(\x02"\x8a\x01\n\x1bListCoverageBucketsResponse\x12\x14\n\x0cbucket_width\x18\x01 \x01(\x03\x12<\n\x10coverage_buckets\x18\x02 \x03(\x0b2".google.genomics.v1.CoverageBucket\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\xa3\x01\n\x12SearchReadsRequest\x12\x1a\n\x12read_group_set_ids\x18\x01 \x03(\t\x12\x16\n\x0eread_group_ids\x18\x05 \x03(\t\x12\x16\n\x0ereference_name\x18\x07 \x01(\t\x12\r\n\x05start\x18\x08 \x01(\x03\x12\x0b\n\x03end\x18\t \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"\\\n\x13SearchReadsResponse\x12,\n\nalignments\x18\x01 \x03(\x0b2\x18.google.genomics.v1.Read\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9c\x01\n\x12StreamReadsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x19\n\x11read_group_set_id\x18\x02 \x01(\t\x12\x16\n\x0ereference_name\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03end\x18\x05 \x01(\x03\x12\r\n\x05shard\x18\x06 \x01(\x05\x12\x14\n\x0ctotal_shards\x18\x07 \x01(\x05"C\n\x13StreamReadsResponse\x12,\n\nalignments\x18\x01 \x03(\x0b2\x18.google.genomics.v1.Read2\x95\x01\n\x14StreamingReadService\x12}\n\x0bStreamReads\x12&.google.genomics.v1.StreamReadsRequest\x1a\'.google.genomics.v1.StreamReadsResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/v1/reads:stream:\x01*0\x012\xd1\t\n\rReadServiceV1\x12\x89\x01\n\x13ImportReadGroupSets\x12..google.genomics.v1.ImportReadGroupSetsRequest\x1a\x1d.google.longrunning.Operation"#\x82\xd3\xe4\x93\x02\x1d"\x18/v1/readgroupsets:import:\x01*\x12\x9b\x01\n\x12ExportReadGroupSet\x12-.google.genomics.v1.ExportReadGroupSetRequest\x1a\x1d.google.longrunning.Operation"7\x82\xd3\xe4\x93\x021",/v1/readgroupsets/{read_group_set_id}:export:\x01*\x12\x9b\x01\n\x13SearchReadGroupSets\x12..google.genomics.v1.SearchReadGroupSetsRequest\x1a/.google.genomics.v1.SearchReadGroupSetsResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/v1/readgroupsets/search:\x01*\x12\xa4\x01\n\x12UpdateReadGroupSet\x12-.google.genomics.v1.UpdateReadGroupSetRequest\x1a .google.genomics.v1.ReadGroupSet"=\x82\xd3\xe4\x93\x0272%/v1/readgroupsets/{read_group_set_id}:\x0eread_group_set\x12\x8a\x01\n\x12DeleteReadGroupSet\x12-.google.genomics.v1.DeleteReadGroupSetRequest\x1a\x16.google.protobuf.Empty"-\x82\xd3\xe4\x93\x02\'*%/v1/readgroupsets/{read_group_set_id}\x12\x8e\x01\n\x0fGetReadGroupSet\x12*.google.genomics.v1.GetReadGroupSetRequest\x1a .google.genomics.v1.ReadGroupSet"-\x82\xd3\xe4\x93\x02\'\x12%/v1/readgroupsets/{read_group_set_id}\x12\xb5\x01\n\x13ListCoverageBuckets\x12..google.genomics.v1.ListCoverageBucketsRequest\x1a/.google.genomics.v1.ListCoverageBucketsResponse"=\x82\xd3\xe4\x93\x027\x125/v1/readgroupsets/{read_group_set_id}/coveragebuckets\x12{\n\x0bSearchReads\x12&.google.genomics.v1.SearchReadsRequest\x1a\'.google.genomics.v1.SearchReadsResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/v1/reads/search:\x01*Be\n\x16com.google.genomics.v1B\nReadsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.reads_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\nReadsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_STREAMINGREADSERVICE'].methods_by_name['StreamReads']._loaded_options = None
    _globals['_STREAMINGREADSERVICE'].methods_by_name['StreamReads']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/v1/reads:stream:\x01*'
    _globals['_READSERVICEV1'].methods_by_name['ImportReadGroupSets']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['ImportReadGroupSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/v1/readgroupsets:import:\x01*'
    _globals['_READSERVICEV1'].methods_by_name['ExportReadGroupSet']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['ExportReadGroupSet']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1/readgroupsets/{read_group_set_id}:export:\x01*'
    _globals['_READSERVICEV1'].methods_by_name['SearchReadGroupSets']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['SearchReadGroupSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/v1/readgroupsets/search:\x01*'
    _globals['_READSERVICEV1'].methods_by_name['UpdateReadGroupSet']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['UpdateReadGroupSet']._serialized_options = b'\x82\xd3\xe4\x93\x0272%/v1/readgroupsets/{read_group_set_id}:\x0eread_group_set'
    _globals['_READSERVICEV1'].methods_by_name['DeleteReadGroupSet']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['DeleteReadGroupSet']._serialized_options = b"\x82\xd3\xe4\x93\x02'*%/v1/readgroupsets/{read_group_set_id}"
    _globals['_READSERVICEV1'].methods_by_name['GetReadGroupSet']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['GetReadGroupSet']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1/readgroupsets/{read_group_set_id}"
    _globals['_READSERVICEV1'].methods_by_name['ListCoverageBuckets']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['ListCoverageBuckets']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1/readgroupsets/{read_group_set_id}/coveragebuckets'
    _globals['_READSERVICEV1'].methods_by_name['SearchReads']._loaded_options = None
    _globals['_READSERVICEV1'].methods_by_name['SearchReads']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15"\x10/v1/reads/search:\x01*'
    _globals['_SEARCHREADGROUPSETSREQUEST']._serialized_start = 295
    _globals['_SEARCHREADGROUPSETSREQUEST']._serialized_end = 397
    _globals['_SEARCHREADGROUPSETSRESPONSE']._serialized_start = 399
    _globals['_SEARCHREADGROUPSETSRESPONSE']._serialized_end = 512
    _globals['_IMPORTREADGROUPSETSREQUEST']._serialized_start = 515
    _globals['_IMPORTREADGROUPSETSREQUEST']._serialized_end = 801
    _globals['_IMPORTREADGROUPSETSREQUEST_PARTITIONSTRATEGY']._serialized_start = 706
    _globals['_IMPORTREADGROUPSETSREQUEST_PARTITIONSTRATEGY']._serialized_end = 801
    _globals['_IMPORTREADGROUPSETSRESPONSE']._serialized_start = 803
    _globals['_IMPORTREADGROUPSETSRESPONSE']._serialized_end = 860
    _globals['_EXPORTREADGROUPSETREQUEST']._serialized_start = 862
    _globals['_EXPORTREADGROUPSETREQUEST']._serialized_end = 981
    _globals['_UPDATEREADGROUPSETREQUEST']._serialized_start = 984
    _globals['_UPDATEREADGROUPSETREQUEST']._serialized_end = 1145
    _globals['_DELETEREADGROUPSETREQUEST']._serialized_start = 1147
    _globals['_DELETEREADGROUPSETREQUEST']._serialized_end = 1201
    _globals['_GETREADGROUPSETREQUEST']._serialized_start = 1203
    _globals['_GETREADGROUPSETREQUEST']._serialized_end = 1254
    _globals['_LISTCOVERAGEBUCKETSREQUEST']._serialized_start = 1257
    _globals['_LISTCOVERAGEBUCKETSREQUEST']._serialized_end = 1432
    _globals['_COVERAGEBUCKET']._serialized_start = 1434
    _globals['_COVERAGEBUCKET']._serialized_end = 1515
    _globals['_LISTCOVERAGEBUCKETSRESPONSE']._serialized_start = 1518
    _globals['_LISTCOVERAGEBUCKETSRESPONSE']._serialized_end = 1656
    _globals['_SEARCHREADSREQUEST']._serialized_start = 1659
    _globals['_SEARCHREADSREQUEST']._serialized_end = 1822
    _globals['_SEARCHREADSRESPONSE']._serialized_start = 1824
    _globals['_SEARCHREADSRESPONSE']._serialized_end = 1916
    _globals['_STREAMREADSREQUEST']._serialized_start = 1919
    _globals['_STREAMREADSREQUEST']._serialized_end = 2075
    _globals['_STREAMREADSRESPONSE']._serialized_start = 2077
    _globals['_STREAMREADSRESPONSE']._serialized_end = 2144
    _globals['_STREAMINGREADSERVICE']._serialized_start = 2147
    _globals['_STREAMINGREADSERVICE']._serialized_end = 2296
    _globals['_READSERVICEV1']._serialized_start = 2299
    _globals['_READSERVICEV1']._serialized_end = 3532