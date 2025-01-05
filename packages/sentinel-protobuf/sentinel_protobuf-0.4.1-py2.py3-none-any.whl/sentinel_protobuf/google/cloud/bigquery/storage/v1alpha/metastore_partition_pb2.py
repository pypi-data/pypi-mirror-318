"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1alpha/metastore_partition.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1alpha import partition_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1alpha_dot_partition__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/bigquery/storage/v1alpha/metastore_partition.proto\x12%google.cloud.bigquery.storage.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/bigquery/storage/v1alpha/partition.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb5\x01\n\x1fCreateMetastorePartitionRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12[\n\x13metastore_partition\x18\x02 \x01(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartitionB\x03\xe0A\x02"\xe4\x01\n%BatchCreateMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12]\n\x08requests\x18\x02 \x03(\x0b2F.google.cloud.bigquery.storage.v1alpha.CreateMetastorePartitionRequestB\x03\xe0A\x02\x12%\n\x18skip_existing_partitions\x18\x03 \x01(\x08B\x03\xe0A\x01"w\n&BatchCreateMetastorePartitionsResponse\x12M\n\npartitions\x18\x01 \x03(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartition"\xbe\x01\n%BatchDeleteMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12^\n\x10partition_values\x18\x02 \x03(\x0b2?.google.cloud.bigquery.storage.v1alpha.MetastorePartitionValuesB\x03\xe0A\x02"\xb4\x01\n\x1fUpdateMetastorePartitionRequest\x12[\n\x13metastore_partition\x18\x01 \x01(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartitionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xbd\x01\n%BatchUpdateMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12]\n\x08requests\x18\x02 \x03(\x0b2F.google.cloud.bigquery.storage.v1alpha.UpdateMetastorePartitionRequestB\x03\xe0A\x02"w\n&BatchUpdateMetastorePartitionsResponse\x12M\n\npartitions\x18\x01 \x03(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartition"l\n\x1eListMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01"\xc8\x01\n\x1fListMetastorePartitionsResponse\x12S\n\npartitions\x18\x01 \x01(\x0b2=.google.cloud.bigquery.storage.v1alpha.MetastorePartitionListH\x00\x12D\n\x07streams\x18\x02 \x01(\x0b21.google.cloud.bigquery.storage.v1alpha.StreamListH\x00B\n\n\x08response"\xde\x01\n StreamMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\\\n\x14metastore_partitions\x18\x02 \x03(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartitionB\x03\xe0A\x01\x12%\n\x18skip_existing_partitions\x18\x03 \x01(\x08B\x03\xe0A\x01"u\n!StreamMetastorePartitionsResponse\x12\'\n\x1ftotal_partitions_streamed_count\x18\x02 \x01(\x03\x12\'\n\x1ftotal_partitions_inserted_count\x18\x03 \x01(\x03"L\n\x16BatchSizeTooLargeError\x12\x16\n\x0emax_batch_size\x18\x01 \x01(\x03\x12\x1a\n\rerror_message\x18\x02 \x01(\tB\x03\xe0A\x012\x82\x0b\n\x19MetastorePartitionService\x12\x9d\x02\n\x1eBatchCreateMetastorePartitions\x12L.google.cloud.bigquery.storage.v1alpha.BatchCreateMetastorePartitionsRequest\x1aM.google.cloud.bigquery.storage.v1alpha.BatchCreateMetastorePartitionsResponse"^\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchCreate:\x01*\x12\xe6\x01\n\x1eBatchDeleteMetastorePartitions\x12L.google.cloud.bigquery.storage.v1alpha.BatchDeleteMetastorePartitionsRequest\x1a\x16.google.protobuf.Empty"^\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchDelete:\x01*\x12\x9d\x02\n\x1eBatchUpdateMetastorePartitions\x12L.google.cloud.bigquery.storage.v1alpha.BatchUpdateMetastorePartitionsRequest\x1aM.google.cloud.bigquery.storage.v1alpha.BatchUpdateMetastorePartitionsResponse"^\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchUpdate:\x01*\x12\x87\x02\n\x17ListMetastorePartitions\x12E.google.cloud.bigquery.storage.v1alpha.ListMetastorePartitionsRequest\x1aF.google.cloud.bigquery.storage.v1alpha.ListMetastorePartitionsResponse"]\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:list\x12\xb4\x01\n\x19StreamMetastorePartitions\x12G.google.cloud.bigquery.storage.v1alpha.StreamMetastorePartitionsRequest\x1aH.google.cloud.bigquery.storage.v1alpha.StreamMetastorePartitionsResponse"\x00(\x010\x01\x1a{\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xba\x02\n)com.google.cloud.bigquery.storage.v1alphaB\x1eMetastorePartitionServiceProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1alpha/storagepb;storagepb\xaa\x02%Google.Cloud.BigQuery.Storage.V1Alpha\xca\x02%Google\\Cloud\\BigQuery\\Storage\\V1alpha\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1alpha.metastore_partition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1alphaB\x1eMetastorePartitionServiceProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1alpha/storagepb;storagepb\xaa\x02%Google.Cloud.BigQuery.Storage.V1Alpha\xca\x02%Google\\Cloud\\BigQuery\\Storage\\V1alpha\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}'
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._loaded_options = None
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['partition_values']._loaded_options = None
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['partition_values']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._loaded_options = None
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['metastore_partitions']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['metastore_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHSIZETOOLARGEERROR'].fields_by_name['error_message']._loaded_options = None
    _globals['_BATCHSIZETOOLARGEERROR'].fields_by_name['error_message']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITIONSERVICE']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchCreateMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchCreateMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchCreate:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchDeleteMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchDeleteMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchDelete:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchUpdateMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchUpdateMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:batchUpdate:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['ListMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['ListMetastorePartitions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1alpha/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:list'
    _globals['_CREATEMETASTOREPARTITIONREQUEST']._serialized_start = 340
    _globals['_CREATEMETASTOREPARTITIONREQUEST']._serialized_end = 521
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST']._serialized_start = 524
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST']._serialized_end = 752
    _globals['_BATCHCREATEMETASTOREPARTITIONSRESPONSE']._serialized_start = 754
    _globals['_BATCHCREATEMETASTOREPARTITIONSRESPONSE']._serialized_end = 873
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST']._serialized_start = 876
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST']._serialized_end = 1066
    _globals['_UPDATEMETASTOREPARTITIONREQUEST']._serialized_start = 1069
    _globals['_UPDATEMETASTOREPARTITIONREQUEST']._serialized_end = 1249
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST']._serialized_start = 1252
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST']._serialized_end = 1441
    _globals['_BATCHUPDATEMETASTOREPARTITIONSRESPONSE']._serialized_start = 1443
    _globals['_BATCHUPDATEMETASTOREPARTITIONSRESPONSE']._serialized_end = 1562
    _globals['_LISTMETASTOREPARTITIONSREQUEST']._serialized_start = 1564
    _globals['_LISTMETASTOREPARTITIONSREQUEST']._serialized_end = 1672
    _globals['_LISTMETASTOREPARTITIONSRESPONSE']._serialized_start = 1675
    _globals['_LISTMETASTOREPARTITIONSRESPONSE']._serialized_end = 1875
    _globals['_STREAMMETASTOREPARTITIONSREQUEST']._serialized_start = 1878
    _globals['_STREAMMETASTOREPARTITIONSREQUEST']._serialized_end = 2100
    _globals['_STREAMMETASTOREPARTITIONSRESPONSE']._serialized_start = 2102
    _globals['_STREAMMETASTOREPARTITIONSRESPONSE']._serialized_end = 2219
    _globals['_BATCHSIZETOOLARGEERROR']._serialized_start = 2221
    _globals['_BATCHSIZETOOLARGEERROR']._serialized_end = 2297
    _globals['_METASTOREPARTITIONSERVICE']._serialized_start = 2300
    _globals['_METASTOREPARTITIONSERVICE']._serialized_end = 3710