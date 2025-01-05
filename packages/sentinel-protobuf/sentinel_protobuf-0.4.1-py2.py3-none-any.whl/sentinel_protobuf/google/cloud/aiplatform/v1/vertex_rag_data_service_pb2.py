"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/vertex_rag_data_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.cloud.aiplatform.v1 import vertex_rag_data_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_vertex__rag__data__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1/vertex_rag_data_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a0google/cloud/aiplatform/v1/vertex_rag_data.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto"\x93\x01\n\x16CreateRagCorpusRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12>\n\nrag_corpus\x18\x02 \x01(\x0b2%.google.cloud.aiplatform.v1.RagCorpusB\x03\xe0A\x02"P\n\x13GetRagCorpusRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus"\x83\x01\n\x15ListRagCorporaRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x16ListRagCorporaResponse\x12:\n\x0brag_corpora\x18\x01 \x03(\x0b2%.google.cloud.aiplatform.v1.RagCorpus\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"g\n\x16DeleteRagCorpusRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\xe5\x01\n\x14UploadRagFileRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12:\n\x08rag_file\x18\x02 \x01(\x0b2#.google.cloud.aiplatform.v1.RagFileB\x03\xe0A\x02\x12T\n\x16upload_rag_file_config\x18\x05 \x01(\x0b2/.google.cloud.aiplatform.v1.UploadRagFileConfigB\x03\xe0A\x02"\x7f\n\x15UploadRagFileResponse\x127\n\x08rag_file\x18\x01 \x01(\x0b2#.google.cloud.aiplatform.v1.RagFileH\x00\x12#\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusH\x00B\x08\n\x06result"\xac\x01\n\x15ImportRagFilesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12V\n\x17import_rag_files_config\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1.ImportRagFilesConfigB\x03\xe0A\x02"\xe3\x01\n\x16ImportRagFilesResponse\x12#\n\x19partial_failures_gcs_path\x18\x04 \x01(\tH\x00\x12)\n\x1fpartial_failures_bigquery_table\x18\x05 \x01(\tH\x00\x12 \n\x18imported_rag_files_count\x18\x01 \x01(\x03\x12\x1e\n\x16failed_rag_files_count\x18\x02 \x01(\x03\x12\x1f\n\x17skipped_rag_files_count\x18\x03 \x01(\x03B\x16\n\x14partial_failure_sink"L\n\x11GetRagFileRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile"\x83\x01\n\x13ListRagFilesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"g\n\x14ListRagFilesResponse\x126\n\trag_files\x18\x01 \x03(\x0b2#.google.cloud.aiplatform.v1.RagFile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x14DeleteRagFileRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile"r\n CreateRagCorpusOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"X\n\x16UpdateRagCorpusRequest\x12>\n\nrag_corpus\x18\x01 \x01(\x0b2%.google.cloud.aiplatform.v1.RagCorpusB\x03\xe0A\x02"r\n UpdateRagCorpusOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\xfd\x01\n\x1fImportRagFilesOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12\x15\n\rrag_corpus_id\x18\x02 \x01(\x03\x12V\n\x17import_rag_files_config\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1.ImportRagFilesConfigB\x03\xe0A\x03\x12\x1b\n\x13progress_percentage\x18\x04 \x01(\x052\xcf\x11\n\x14VertexRagDataService\x12\xed\x01\n\x0fCreateRagCorpus\x122.google.cloud.aiplatform.v1.CreateRagCorpusRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA-\n\tRagCorpus\x12 CreateRagCorpusOperationMetadata\xdaA\x11parent,rag_corpus\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/ragCorpora:\nrag_corpus\x12\xf1\x01\n\x0fUpdateRagCorpus\x122.google.cloud.aiplatform.v1.UpdateRagCorpusRequest\x1a\x1d.google.longrunning.Operation"\x8a\x01\xcaA-\n\tRagCorpus\x12 UpdateRagCorpusOperationMetadata\xdaA\nrag_corpus\x82\xd3\xe4\x93\x02G29/v1/{rag_corpus.name=projects/*/locations/*/ragCorpora/*}:\nrag_corpus\x12\xa5\x01\n\x0cGetRagCorpus\x12/.google.cloud.aiplatform.v1.GetRagCorpusRequest\x1a%.google.cloud.aiplatform.v1.RagCorpus"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/ragCorpora/*}\x12\xb8\x01\n\x0eListRagCorpora\x121.google.cloud.aiplatform.v1.ListRagCorporaRequest\x1a2.google.cloud.aiplatform.v1.ListRagCorporaResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/ragCorpora\x12\xd6\x01\n\x0fDeleteRagCorpus\x122.google.cloud.aiplatform.v1.DeleteRagCorpusRequest\x1a\x1d.google.longrunning.Operation"p\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/ragCorpora/*}\x12\xea\x01\n\rUploadRagFile\x120.google.cloud.aiplatform.v1.UploadRagFileRequest\x1a1.google.cloud.aiplatform.v1.UploadRagFileResponse"t\xdaA&parent,rag_file,upload_rag_file_config\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:upload:\x01*\x12\x8d\x02\n\x0eImportRagFiles\x121.google.cloud.aiplatform.v1.ImportRagFilesRequest\x1a\x1d.google.longrunning.Operation"\xa8\x01\xcaA9\n\x16ImportRagFilesResponse\x12\x1fImportRagFilesOperationMetadata\xdaA\x1eparent,import_rag_files_config\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:import:\x01*\x12\xaa\x01\n\nGetRagFile\x12-.google.cloud.aiplatform.v1.GetRagFileRequest\x1a#.google.cloud.aiplatform.v1.RagFile"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}\x12\xbd\x01\n\x0cListRagFiles\x12/.google.cloud.aiplatform.v1.ListRagFilesRequest\x1a0.google.cloud.aiplatform.v1.ListRagFilesResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles\x12\xdd\x01\n\rDeleteRagFile\x120.google.cloud.aiplatform.v1.DeleteRagFileRequest\x1a\x1d.google.longrunning.Operation"{\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1ecom.google.cloud.aiplatform.v1B\x19VertexRagDataServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.vertex_rag_data_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x19VertexRagDataServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._loaded_options = None
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._serialized_options = b'\xe0A\x02'
    _globals['_GETRAGCORPUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRAGCORPUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['rag_file']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['rag_file']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['upload_rag_file_config']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['upload_rag_file_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['import_rag_files_config']._loaded_options = None
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['import_rag_files_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETRAGFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRAGFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile'
    _globals['_UPDATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._loaded_options = None
    _globals['_UPDATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTRAGFILESOPERATIONMETADATA'].fields_by_name['import_rag_files_config']._loaded_options = None
    _globals['_IMPORTRAGFILESOPERATIONMETADATA'].fields_by_name['import_rag_files_config']._serialized_options = b'\xe0A\x03'
    _globals['_VERTEXRAGDATASERVICE']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['CreateRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['CreateRagCorpus']._serialized_options = b'\xcaA-\n\tRagCorpus\x12 CreateRagCorpusOperationMetadata\xdaA\x11parent,rag_corpus\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/ragCorpora:\nrag_corpus'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagCorpus']._serialized_options = b'\xcaA-\n\tRagCorpus\x12 UpdateRagCorpusOperationMetadata\xdaA\nrag_corpus\x82\xd3\xe4\x93\x02G29/v1/{rag_corpus.name=projects/*/locations/*/ragCorpora/*}:\nrag_corpus'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagCorpus']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/ragCorpora/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagCorpora']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagCorpora']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/ragCorpora'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagCorpus']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/ragCorpora/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UploadRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UploadRagFile']._serialized_options = b'\xdaA&parent,rag_file,upload_rag_file_config\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:upload:\x01*'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ImportRagFiles']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ImportRagFiles']._serialized_options = b'\xcaA9\n\x16ImportRagFilesResponse\x12\x1fImportRagFilesOperationMetadata\xdaA\x1eparent,import_rag_files_config\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:import:\x01*'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagFile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagFiles']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagFiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagFile']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}'
    _globals['_CREATERAGCORPUSREQUEST']._serialized_start = 389
    _globals['_CREATERAGCORPUSREQUEST']._serialized_end = 536
    _globals['_GETRAGCORPUSREQUEST']._serialized_start = 538
    _globals['_GETRAGCORPUSREQUEST']._serialized_end = 618
    _globals['_LISTRAGCORPORAREQUEST']._serialized_start = 621
    _globals['_LISTRAGCORPORAREQUEST']._serialized_end = 752
    _globals['_LISTRAGCORPORARESPONSE']._serialized_start = 754
    _globals['_LISTRAGCORPORARESPONSE']._serialized_end = 863
    _globals['_DELETERAGCORPUSREQUEST']._serialized_start = 865
    _globals['_DELETERAGCORPUSREQUEST']._serialized_end = 968
    _globals['_UPLOADRAGFILEREQUEST']._serialized_start = 971
    _globals['_UPLOADRAGFILEREQUEST']._serialized_end = 1200
    _globals['_UPLOADRAGFILERESPONSE']._serialized_start = 1202
    _globals['_UPLOADRAGFILERESPONSE']._serialized_end = 1329
    _globals['_IMPORTRAGFILESREQUEST']._serialized_start = 1332
    _globals['_IMPORTRAGFILESREQUEST']._serialized_end = 1504
    _globals['_IMPORTRAGFILESRESPONSE']._serialized_start = 1507
    _globals['_IMPORTRAGFILESRESPONSE']._serialized_end = 1734
    _globals['_GETRAGFILEREQUEST']._serialized_start = 1736
    _globals['_GETRAGFILEREQUEST']._serialized_end = 1812
    _globals['_LISTRAGFILESREQUEST']._serialized_start = 1815
    _globals['_LISTRAGFILESREQUEST']._serialized_end = 1946
    _globals['_LISTRAGFILESRESPONSE']._serialized_start = 1948
    _globals['_LISTRAGFILESRESPONSE']._serialized_end = 2051
    _globals['_DELETERAGFILEREQUEST']._serialized_start = 2053
    _globals['_DELETERAGFILEREQUEST']._serialized_end = 2132
    _globals['_CREATERAGCORPUSOPERATIONMETADATA']._serialized_start = 2134
    _globals['_CREATERAGCORPUSOPERATIONMETADATA']._serialized_end = 2248
    _globals['_UPDATERAGCORPUSREQUEST']._serialized_start = 2250
    _globals['_UPDATERAGCORPUSREQUEST']._serialized_end = 2338
    _globals['_UPDATERAGCORPUSOPERATIONMETADATA']._serialized_start = 2340
    _globals['_UPDATERAGCORPUSOPERATIONMETADATA']._serialized_end = 2454
    _globals['_IMPORTRAGFILESOPERATIONMETADATA']._serialized_start = 2457
    _globals['_IMPORTRAGFILESOPERATIONMETADATA']._serialized_end = 2710
    _globals['_VERTEXRAGDATASERVICE']._serialized_start = 2713
    _globals['_VERTEXRAGDATASERVICE']._serialized_end = 4968