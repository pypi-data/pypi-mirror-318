"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/vertex_rag_data.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import api_auth_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_api__auth__pb2
from .....google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/aiplatform/v1/vertex_rag_data.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/aiplatform/v1/api_auth.proto\x1a#google/cloud/aiplatform/v1/io.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x02\n\x17RagEmbeddingModelConfig\x12r\n\x1avertex_prediction_endpoint\x18\x01 \x01(\x0b2L.google.cloud.aiplatform.v1.RagEmbeddingModelConfig.VertexPredictionEndpointH\x00\x1a\xaf\x01\n\x18VertexPredictionEndpoint\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x126\n\x05model\x18\x02 \x01(\tB\'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x03 \x01(\tB\x03\xe0A\x03B\x0e\n\x0cmodel_config"\xa9\x04\n\x11RagVectorDbConfig\x12T\n\x0erag_managed_db\x18\x01 \x01(\x0b2:.google.cloud.aiplatform.v1.RagVectorDbConfig.RagManagedDbH\x00\x12J\n\x08pinecone\x18\x03 \x01(\x0b26.google.cloud.aiplatform.v1.RagVectorDbConfig.PineconeH\x00\x12`\n\x14vertex_vector_search\x18\x06 \x01(\x0b2@.google.cloud.aiplatform.v1.RagVectorDbConfig.VertexVectorSearchH\x00\x125\n\x08api_auth\x18\x05 \x01(\x0b2#.google.cloud.aiplatform.v1.ApiAuth\x12_\n\x1arag_embedding_model_config\x18\x07 \x01(\x0b23.google.cloud.aiplatform.v1.RagEmbeddingModelConfigB\x06\xe0A\x01\xe0A\x05\x1a\x0e\n\x0cRagManagedDb\x1a\x1e\n\x08Pinecone\x12\x12\n\nindex_name\x18\x01 \x01(\t\x1a;\n\x12VertexVectorSearch\x12\x16\n\x0eindex_endpoint\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\tB\x0b\n\tvector_db"\xa0\x01\n\nFileStatus\x12@\n\x05state\x18\x01 \x01(\x0e2,.google.cloud.aiplatform.v1.FileStatus.StateB\x03\xe0A\x03\x12\x19\n\x0cerror_status\x18\x02 \x01(\tB\x03\xe0A\x03"5\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\t\n\x05ERROR\x10\x02"\xab\x01\n\x0cCorpusStatus\x12B\n\x05state\x18\x01 \x01(\x0e2..google.cloud.aiplatform.v1.CorpusStatus.StateB\x03\xe0A\x03\x12\x19\n\x0cerror_status\x18\x02 \x01(\tB\x03\xe0A\x03"<\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bINITIALIZED\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\t\n\x05ERROR\x10\x03"\xed\x03\n\tRagCorpus\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\rcorpus_status\x18\x08 \x01(\x0b2(.google.cloud.aiplatform.v1.CorpusStatusB\x03\xe0A\x03\x12Q\n\x10vector_db_config\x18\t \x01(\x0b2-.google.cloud.aiplatform.v1.RagVectorDbConfigB\x06\xe0A\x01\xe0A\x05H\x00:\x80\x01\xeaA}\n#aiplatform.googleapis.com/RagCorpus\x12?projects/{project}/locations/{location}/ragCorpora/{rag_corpus}*\nragCorpora2\tragCorpusB\x10\n\x0ebackend_config"\xdc\x06\n\x07RagFile\x12@\n\ngcs_source\x18\x08 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSourceB\x03\xe0A\x03H\x00\x12Q\n\x13google_drive_source\x18\t \x01(\x0b2-.google.cloud.aiplatform.v1.GoogleDriveSourceB\x03\xe0A\x03H\x00\x12S\n\x14direct_upload_source\x18\n \x01(\x0b2..google.cloud.aiplatform.v1.DirectUploadSourceB\x03\xe0A\x03H\x00\x12?\n\x0cslack_source\x18\x0b \x01(\x0b2\'.google.cloud.aiplatform.v1.SlackSourceH\x00\x12=\n\x0bjira_source\x18\x0c \x01(\x0b2&.google.cloud.aiplatform.v1.JiraSourceH\x00\x12L\n\x13share_point_sources\x18\x0e \x01(\x0b2-.google.cloud.aiplatform.v1.SharePointSourcesH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x0bfile_status\x18\r \x01(\x0b2&.google.cloud.aiplatform.v1.FileStatusB\x03\xe0A\x03:\x8f\x01\xeaA\x8b\x01\n!aiplatform.googleapis.com/RagFile\x12Sprojects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}*\x08ragFiles2\x07ragFileB\x11\n\x0frag_file_source"\xd4\x01\n\x15RagFileChunkingConfig\x12f\n\x15fixed_length_chunking\x18\x03 \x01(\x0b2E.google.cloud.aiplatform.v1.RagFileChunkingConfig.FixedLengthChunkingH\x00\x1a@\n\x13FixedLengthChunking\x12\x12\n\nchunk_size\x18\x01 \x01(\x05\x12\x15\n\rchunk_overlap\x18\x02 \x01(\x05B\x11\n\x0fchunking_config"r\n\x1bRagFileTransformationConfig\x12S\n\x18rag_file_chunking_config\x18\x01 \x01(\x0b21.google.cloud.aiplatform.v1.RagFileChunkingConfig"v\n\x13UploadRagFileConfig\x12_\n\x1erag_file_transformation_config\x18\x03 \x01(\x0b27.google.cloud.aiplatform.v1.RagFileTransformationConfig"\xd8\x05\n\x14ImportRagFilesConfig\x12;\n\ngcs_source\x18\x02 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSourceH\x00\x12L\n\x13google_drive_source\x18\x03 \x01(\x0b2-.google.cloud.aiplatform.v1.GoogleDriveSourceH\x00\x12?\n\x0cslack_source\x18\x06 \x01(\x0b2\'.google.cloud.aiplatform.v1.SlackSourceH\x00\x12=\n\x0bjira_source\x18\x07 \x01(\x0b2&.google.cloud.aiplatform.v1.JiraSourceH\x00\x12L\n\x13share_point_sources\x18\r \x01(\x0b2-.google.cloud.aiplatform.v1.SharePointSourcesH\x00\x12R\n\x18partial_failure_gcs_sink\x18\x0b \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestinationB\x02\x18\x01H\x01\x12\\\n\x1dpartial_failure_bigquery_sink\x18\x0c \x01(\x0b2/.google.cloud.aiplatform.v1.BigQueryDestinationB\x02\x18\x01H\x01\x12_\n\x1erag_file_transformation_config\x18\x10 \x01(\x0b27.google.cloud.aiplatform.v1.RagFileTransformationConfig\x12+\n\x1emax_embedding_requests_per_min\x18\x05 \x01(\x05B\x03\xe0A\x01B\x0f\n\rimport_sourceB\x16\n\x14partial_failure_sinkB\xd0\x01\n\x1ecom.google.cloud.aiplatform.v1B\x12VertexRagDataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.vertex_rag_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x12VertexRagDataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['endpoint']._loaded_options = None
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['model']._loaded_options = None
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['model']._serialized_options = b'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_RAGVECTORDBCONFIG'].fields_by_name['rag_embedding_model_config']._loaded_options = None
    _globals['_RAGVECTORDBCONFIG'].fields_by_name['rag_embedding_model_config']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_FILESTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_FILESTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FILESTATUS'].fields_by_name['error_status']._loaded_options = None
    _globals['_FILESTATUS'].fields_by_name['error_status']._serialized_options = b'\xe0A\x03'
    _globals['_CORPUSSTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_CORPUSSTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CORPUSSTATUS'].fields_by_name['error_status']._loaded_options = None
    _globals['_CORPUSSTATUS'].fields_by_name['error_status']._serialized_options = b'\xe0A\x03'
    _globals['_RAGCORPUS'].fields_by_name['name']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_RAGCORPUS'].fields_by_name['display_name']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_RAGCORPUS'].fields_by_name['description']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_RAGCORPUS'].fields_by_name['create_time']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RAGCORPUS'].fields_by_name['update_time']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_RAGCORPUS'].fields_by_name['corpus_status']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['corpus_status']._serialized_options = b'\xe0A\x03'
    _globals['_RAGCORPUS'].fields_by_name['vector_db_config']._loaded_options = None
    _globals['_RAGCORPUS'].fields_by_name['vector_db_config']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_RAGCORPUS']._loaded_options = None
    _globals['_RAGCORPUS']._serialized_options = b'\xeaA}\n#aiplatform.googleapis.com/RagCorpus\x12?projects/{project}/locations/{location}/ragCorpora/{rag_corpus}*\nragCorpora2\tragCorpus'
    _globals['_RAGFILE'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['google_drive_source']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['google_drive_source']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['direct_upload_source']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['direct_upload_source']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['name']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['display_name']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_RAGFILE'].fields_by_name['description']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_RAGFILE'].fields_by_name['create_time']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['update_time']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE'].fields_by_name['file_status']._loaded_options = None
    _globals['_RAGFILE'].fields_by_name['file_status']._serialized_options = b'\xe0A\x03'
    _globals['_RAGFILE']._loaded_options = None
    _globals['_RAGFILE']._serialized_options = b'\xeaA\x8b\x01\n!aiplatform.googleapis.com/RagFile\x12Sprojects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragFiles/{rag_file}*\x08ragFiles2\x07ragFile'
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['partial_failure_gcs_sink']._loaded_options = None
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['partial_failure_gcs_sink']._serialized_options = b'\x18\x01'
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['partial_failure_bigquery_sink']._loaded_options = None
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['partial_failure_bigquery_sink']._serialized_options = b'\x18\x01'
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['max_embedding_requests_per_min']._loaded_options = None
    _globals['_IMPORTRAGFILESCONFIG'].fields_by_name['max_embedding_requests_per_min']._serialized_options = b'\xe0A\x01'
    _globals['_RAGEMBEDDINGMODELCONFIG']._serialized_start = 254
    _globals['_RAGEMBEDDINGMODELCONFIG']._serialized_end = 589
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT']._serialized_start = 398
    _globals['_RAGEMBEDDINGMODELCONFIG_VERTEXPREDICTIONENDPOINT']._serialized_end = 573
    _globals['_RAGVECTORDBCONFIG']._serialized_start = 592
    _globals['_RAGVECTORDBCONFIG']._serialized_end = 1145
    _globals['_RAGVECTORDBCONFIG_RAGMANAGEDDB']._serialized_start = 1025
    _globals['_RAGVECTORDBCONFIG_RAGMANAGEDDB']._serialized_end = 1039
    _globals['_RAGVECTORDBCONFIG_PINECONE']._serialized_start = 1041
    _globals['_RAGVECTORDBCONFIG_PINECONE']._serialized_end = 1071
    _globals['_RAGVECTORDBCONFIG_VERTEXVECTORSEARCH']._serialized_start = 1073
    _globals['_RAGVECTORDBCONFIG_VERTEXVECTORSEARCH']._serialized_end = 1132
    _globals['_FILESTATUS']._serialized_start = 1148
    _globals['_FILESTATUS']._serialized_end = 1308
    _globals['_FILESTATUS_STATE']._serialized_start = 1255
    _globals['_FILESTATUS_STATE']._serialized_end = 1308
    _globals['_CORPUSSTATUS']._serialized_start = 1311
    _globals['_CORPUSSTATUS']._serialized_end = 1482
    _globals['_CORPUSSTATUS_STATE']._serialized_start = 1422
    _globals['_CORPUSSTATUS_STATE']._serialized_end = 1482
    _globals['_RAGCORPUS']._serialized_start = 1485
    _globals['_RAGCORPUS']._serialized_end = 1978
    _globals['_RAGFILE']._serialized_start = 1981
    _globals['_RAGFILE']._serialized_end = 2841
    _globals['_RAGFILECHUNKINGCONFIG']._serialized_start = 2844
    _globals['_RAGFILECHUNKINGCONFIG']._serialized_end = 3056
    _globals['_RAGFILECHUNKINGCONFIG_FIXEDLENGTHCHUNKING']._serialized_start = 2973
    _globals['_RAGFILECHUNKINGCONFIG_FIXEDLENGTHCHUNKING']._serialized_end = 3037
    _globals['_RAGFILETRANSFORMATIONCONFIG']._serialized_start = 3058
    _globals['_RAGFILETRANSFORMATIONCONFIG']._serialized_end = 3172
    _globals['_UPLOADRAGFILECONFIG']._serialized_start = 3174
    _globals['_UPLOADRAGFILECONFIG']._serialized_end = 3292
    _globals['_IMPORTRAGFILESCONFIG']._serialized_start = 3295
    _globals['_IMPORTRAGFILESCONFIG']._serialized_end = 4023