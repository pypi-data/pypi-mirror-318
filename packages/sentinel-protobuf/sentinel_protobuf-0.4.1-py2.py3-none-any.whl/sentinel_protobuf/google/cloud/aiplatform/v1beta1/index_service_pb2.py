"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/index_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import index_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_index__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/index_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/aiplatform/v1beta1/index.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x8b\x01\n\x12CreateIndexRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12:\n\x05index\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.IndexB\x03\xe0A\x02"\xf0\x01\n\x1cCreateIndexOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12{\n*nearest_neighbor_search_operation_metadata\x18\x02 \x01(\x0b2G.google.cloud.aiplatform.v1beta1.NearestNeighborSearchOperationMetadata"H\n\x0fGetIndexRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index"\xb5\x01\n\x12ListIndexesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"g\n\x13ListIndexesResponse\x127\n\x07indexes\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Index\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x81\x01\n\x12UpdateIndexRequest\x12:\n\x05index\x18\x01 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.IndexB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xf0\x01\n\x1cUpdateIndexOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12{\n*nearest_neighbor_search_operation_metadata\x18\x02 \x01(\x0b2G.google.cloud.aiplatform.v1beta1.NearestNeighborSearchOperationMetadata"K\n\x12DeleteIndexRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index"\xcc\x01\n\x17UpsertDatapointsRequest\x126\n\x05index\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index\x12C\n\ndatapoints\x18\x02 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.IndexDatapoint\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x1a\n\x18UpsertDatapointsResponse"h\n\x17RemoveDatapointsRequest\x126\n\x05index\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index\x12\x15\n\rdatapoint_ids\x18\x02 \x03(\t"\x1a\n\x18RemoveDatapointsResponse"\x95\t\n&NearestNeighborSearchOperationMetadata\x12\x80\x01\n\x18content_validation_stats\x18\x01 \x03(\x0b2^.google.cloud.aiplatform.v1beta1.NearestNeighborSearchOperationMetadata.ContentValidationStats\x12\x18\n\x10data_bytes_count\x18\x02 \x01(\x03\x1a\xab\x05\n\x0bRecordError\x12w\n\nerror_type\x18\x01 \x01(\x0e2c.google.cloud.aiplatform.v1beta1.NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x16\n\x0esource_gcs_uri\x18\x03 \x01(\t\x12\x14\n\x0cembedding_id\x18\x04 \x01(\t\x12\x12\n\nraw_record\x18\x05 \x01(\t"\xc9\x03\n\x0fRecordErrorType\x12\x1a\n\x16ERROR_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nEMPTY_LINE\x10\x01\x12\x17\n\x13INVALID_JSON_SYNTAX\x10\x02\x12\x16\n\x12INVALID_CSV_SYNTAX\x10\x03\x12\x17\n\x13INVALID_AVRO_SYNTAX\x10\x04\x12\x18\n\x14INVALID_EMBEDDING_ID\x10\x05\x12\x1b\n\x17EMBEDDING_SIZE_MISMATCH\x10\x06\x12\x15\n\x11NAMESPACE_MISSING\x10\x07\x12\x11\n\rPARSING_ERROR\x10\x08\x12\x17\n\x13DUPLICATE_NAMESPACE\x10\t\x12\x13\n\x0fOP_IN_DATAPOINT\x10\n\x12\x13\n\x0fMULTIPLE_VALUES\x10\x0b\x12\x19\n\x15INVALID_NUMERIC_VALUE\x10\x0c\x12\x14\n\x10INVALID_ENCODING\x10\r\x12\x1d\n\x19INVALID_SPARSE_DIMENSIONS\x10\x0e\x12\x17\n\x13INVALID_TOKEN_VALUE\x10\x0f\x12\x1c\n\x18INVALID_SPARSE_EMBEDDING\x10\x10\x12\x15\n\x11INVALID_EMBEDDING\x10\x11\x1a\x9f\x02\n\x16ContentValidationStats\x12\x16\n\x0esource_gcs_uri\x18\x01 \x01(\t\x12\x1a\n\x12valid_record_count\x18\x02 \x01(\x03\x12\x1c\n\x14invalid_record_count\x18\x03 \x01(\x03\x12k\n\x0epartial_errors\x18\x04 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.NearestNeighborSearchOperationMetadata.RecordError\x12!\n\x19valid_sparse_record_count\x18\x05 \x01(\x03\x12#\n\x1binvalid_sparse_record_count\x18\x06 \x01(\x032\x91\x0c\n\x0cIndexService\x12\xd9\x01\n\x0bCreateIndex\x123.google.cloud.aiplatform.v1beta1.CreateIndexRequest\x1a\x1d.google.longrunning.Operation"v\xcaA%\n\x05Index\x12\x1cCreateIndexOperationMetadata\xdaA\x0cparent,index\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/locations/*}/indexes:\x05index\x12\xa5\x01\n\x08GetIndex\x120.google.cloud.aiplatform.v1beta1.GetIndexRequest\x1a&.google.cloud.aiplatform.v1beta1.Index"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/locations/*/indexes/*}\x12\xbb\x01\n\x0bListIndexes\x123.google.cloud.aiplatform.v1beta1.ListIndexesRequest\x1a4.google.cloud.aiplatform.v1beta1.ListIndexesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/locations/*}/indexes\x12\xe5\x01\n\x0bUpdateIndex\x123.google.cloud.aiplatform.v1beta1.UpdateIndexRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA%\n\x05Index\x12\x1cUpdateIndexOperationMetadata\xdaA\x11index,update_mask\x82\xd3\xe4\x93\x02?26/v1beta1/{index.name=projects/*/locations/*/indexes/*}:\x05index\x12\xd5\x01\n\x0bDeleteIndex\x123.google.cloud.aiplatform.v1beta1.DeleteIndexRequest\x1a\x1d.google.longrunning.Operation"r\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/locations/*/indexes/*}\x12\xd6\x01\n\x10UpsertDatapoints\x128.google.cloud.aiplatform.v1beta1.UpsertDatapointsRequest\x1a9.google.cloud.aiplatform.v1beta1.UpsertDatapointsResponse"M\x82\xd3\xe4\x93\x02G"B/v1beta1/{index=projects/*/locations/*/indexes/*}:upsertDatapoints:\x01*\x12\xd6\x01\n\x10RemoveDatapoints\x128.google.cloud.aiplatform.v1beta1.RemoveDatapointsRequest\x1a9.google.cloud.aiplatform.v1beta1.RemoveDatapointsResponse"M\x82\xd3\xe4\x93\x02G"B/v1beta1/{index=projects/*/locations/*/indexes/*}:removeDatapoints:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11IndexServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.index_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11IndexServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEINDEXREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINDEXREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINDEXREQUEST'].fields_by_name['index']._loaded_options = None
    _globals['_CREATEINDEXREQUEST'].fields_by_name['index']._serialized_options = b'\xe0A\x02'
    _globals['_GETINDEXREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINDEXREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index'
    _globals['_LISTINDEXESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINDEXESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATEINDEXREQUEST'].fields_by_name['index']._loaded_options = None
    _globals['_UPDATEINDEXREQUEST'].fields_by_name['index']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINDEXREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINDEXREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index'
    _globals['_UPSERTDATAPOINTSREQUEST'].fields_by_name['index']._loaded_options = None
    _globals['_UPSERTDATAPOINTSREQUEST'].fields_by_name['index']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index'
    _globals['_UPSERTDATAPOINTSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPSERTDATAPOINTSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEDATAPOINTSREQUEST'].fields_by_name['index']._loaded_options = None
    _globals['_REMOVEDATAPOINTSREQUEST'].fields_by_name['index']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index'
    _globals['_INDEXSERVICE']._loaded_options = None
    _globals['_INDEXSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INDEXSERVICE'].methods_by_name['CreateIndex']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['CreateIndex']._serialized_options = b'\xcaA%\n\x05Index\x12\x1cCreateIndexOperationMetadata\xdaA\x0cparent,index\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/locations/*}/indexes:\x05index'
    _globals['_INDEXSERVICE'].methods_by_name['GetIndex']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['GetIndex']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/locations/*/indexes/*}'
    _globals['_INDEXSERVICE'].methods_by_name['ListIndexes']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['ListIndexes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/locations/*}/indexes'
    _globals['_INDEXSERVICE'].methods_by_name['UpdateIndex']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['UpdateIndex']._serialized_options = b'\xcaA%\n\x05Index\x12\x1cUpdateIndexOperationMetadata\xdaA\x11index,update_mask\x82\xd3\xe4\x93\x02?26/v1beta1/{index.name=projects/*/locations/*/indexes/*}:\x05index'
    _globals['_INDEXSERVICE'].methods_by_name['DeleteIndex']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['DeleteIndex']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/locations/*/indexes/*}'
    _globals['_INDEXSERVICE'].methods_by_name['UpsertDatapoints']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['UpsertDatapoints']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/v1beta1/{index=projects/*/locations/*/indexes/*}:upsertDatapoints:\x01*'
    _globals['_INDEXSERVICE'].methods_by_name['RemoveDatapoints']._loaded_options = None
    _globals['_INDEXSERVICE'].methods_by_name['RemoveDatapoints']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/v1beta1/{index=projects/*/locations/*/indexes/*}:removeDatapoints:\x01*'
    _globals['_CREATEINDEXREQUEST']._serialized_start = 398
    _globals['_CREATEINDEXREQUEST']._serialized_end = 537
    _globals['_CREATEINDEXOPERATIONMETADATA']._serialized_start = 540
    _globals['_CREATEINDEXOPERATIONMETADATA']._serialized_end = 780
    _globals['_GETINDEXREQUEST']._serialized_start = 782
    _globals['_GETINDEXREQUEST']._serialized_end = 854
    _globals['_LISTINDEXESREQUEST']._serialized_start = 857
    _globals['_LISTINDEXESREQUEST']._serialized_end = 1038
    _globals['_LISTINDEXESRESPONSE']._serialized_start = 1040
    _globals['_LISTINDEXESRESPONSE']._serialized_end = 1143
    _globals['_UPDATEINDEXREQUEST']._serialized_start = 1146
    _globals['_UPDATEINDEXREQUEST']._serialized_end = 1275
    _globals['_UPDATEINDEXOPERATIONMETADATA']._serialized_start = 1278
    _globals['_UPDATEINDEXOPERATIONMETADATA']._serialized_end = 1518
    _globals['_DELETEINDEXREQUEST']._serialized_start = 1520
    _globals['_DELETEINDEXREQUEST']._serialized_end = 1595
    _globals['_UPSERTDATAPOINTSREQUEST']._serialized_start = 1598
    _globals['_UPSERTDATAPOINTSREQUEST']._serialized_end = 1802
    _globals['_UPSERTDATAPOINTSRESPONSE']._serialized_start = 1804
    _globals['_UPSERTDATAPOINTSRESPONSE']._serialized_end = 1830
    _globals['_REMOVEDATAPOINTSREQUEST']._serialized_start = 1832
    _globals['_REMOVEDATAPOINTSREQUEST']._serialized_end = 1936
    _globals['_REMOVEDATAPOINTSRESPONSE']._serialized_start = 1938
    _globals['_REMOVEDATAPOINTSRESPONSE']._serialized_end = 1964
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA']._serialized_start = 1967
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA']._serialized_end = 3140
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_RECORDERROR']._serialized_start = 2167
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_RECORDERROR']._serialized_end = 2850
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_RECORDERROR_RECORDERRORTYPE']._serialized_start = 2393
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_RECORDERROR_RECORDERRORTYPE']._serialized_end = 2850
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_CONTENTVALIDATIONSTATS']._serialized_start = 2853
    _globals['_NEARESTNEIGHBORSEARCHOPERATIONMETADATA_CONTENTVALIDATIONSTATS']._serialized_end = 3140
    _globals['_INDEXSERVICE']._serialized_start = 3143
    _globals['_INDEXSERVICE']._serialized_end = 4696