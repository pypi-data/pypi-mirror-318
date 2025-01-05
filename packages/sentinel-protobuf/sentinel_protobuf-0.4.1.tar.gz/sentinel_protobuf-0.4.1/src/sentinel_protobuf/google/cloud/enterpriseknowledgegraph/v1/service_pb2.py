"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/enterpriseknowledgegraph/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.enterpriseknowledgegraph.v1 import job_state_pb2 as google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_job__state__pb2
from .....google.cloud.enterpriseknowledgegraph.v1 import operation_metadata_pb2 as google_dot_cloud_dot_enterpriseknowledgegraph_dot_v1_dot_operation__metadata__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/enterpriseknowledgegraph/v1/service.proto\x12(google.cloud.enterpriseknowledgegraph.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/enterpriseknowledgegraph/v1/job_state.proto\x1aAgoogle/cloud/enterpriseknowledgegraph/v1/operation_metadata.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xb6\x03\n\x0bInputConfig\x12]\n\x16bigquery_input_configs\x18\x01 \x03(\x0b2=.google.cloud.enterpriseknowledgegraph.v1.BigQueryInputConfig\x12U\n\x0bentity_type\x18\x02 \x01(\x0e2@.google.cloud.enterpriseknowledgegraph.v1.InputConfig.EntityType\x12M\n\x1eprevious_result_bigquery_table\x18\x03 \x01(\tB%\xe0A\x01\xfaA\x1f\n\x1dbigquery.googleapis.com/Table"\xa1\x01\n\nEntityType\x12\x1b\n\x17ENTITY_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\x06PEOPLE\x10\x01\x1a\x02\x08\x01\x12\x15\n\rESTABLISHMENT\x10\x02\x1a\x02\x08\x01\x12\x10\n\x08PROPERTY\x10\x03\x1a\x02\x08\x01\x12\x0b\n\x07PRODUCT\x10\x04\x12\x10\n\x0cORGANIZATION\x10\x05\x12\x12\n\x0eLOCAL_BUSINESS\x10\x06\x12\n\n\x06PERSON\x10\x07"j\n\x13BigQueryInputConfig\x12=\n\x0ebigquery_table\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\x14\n\x07gcs_uri\x18\x02 \x01(\tB\x03\xe0A\x02"N\n\x0cOutputConfig\x12>\n\x10bigquery_dataset\x18\x01 \x01(\tB$\xfaA!\n\x1fbigquery.googleapis.com/Dataset"\x89\x04\n\x0bReconConfig\x12j\n\x1bconnected_components_config\x18\x01 \x01(\x0b2C.google.cloud.enterpriseknowledgegraph.v1.ConnectedComponentsConfigH\x00\x12h\n\x1aaffinity_clustering_config\x18\x02 \x01(\x0b2B.google.cloud.enterpriseknowledgegraph.v1.AffinityClusteringConfigH\x00\x12N\n\x07options\x18\x03 \x01(\x0b2=.google.cloud.enterpriseknowledgegraph.v1.ReconConfig.Options\x12W\n\x0cmodel_config\x18\x04 \x01(\x0b2A.google.cloud.enterpriseknowledgegraph.v1.ReconConfig.ModelConfig\x1a.\n\x07Options\x12#\n\x1benable_geocoding_separation\x18d \x01(\x08\x1a6\n\x0bModelConfig\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x13\n\x0bversion_tag\x18\x02 \x01(\tB\x13\n\x11clustering_config"5\n\x19ConnectedComponentsConfig\x12\x18\n\x10weight_threshold\x18\x01 \x01(\x02";\n\x18AffinityClusteringConfig\x12\x1f\n\x17compression_round_count\x18\x01 \x01(\x03"u\n\x17DeleteOperationMetadata\x12Z\n\x0fcommon_metadata\x18\x01 \x01(\x0b2A.google.cloud.enterpriseknowledgegraph.v1.CommonOperationMetadata"\xea\x01\n$CreateEntityReconciliationJobRequest\x12W\n\x06parent\x18\x01 \x01(\tBG\xe0A\x02\xfaAA\x12?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob\x12i\n\x19entity_reconciliation_job\x18\x02 \x01(\x0b2A.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJobB\x03\xe0A\x02"z\n!GetEntityReconciliationJobRequest\x12U\n\x04name\x18\x01 \x01(\tBG\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob"\xb5\x01\n#ListEntityReconciliationJobsRequest\x12W\n\x06parent\x18\x01 \x01(\tBG\xe0A\x02\xfaAA\x12?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\xa6\x01\n$ListEntityReconciliationJobsResponse\x12e\n\x1aentity_reconciliation_jobs\x18\x01 \x03(\x0b2A.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"}\n$CancelEntityReconciliationJobRequest\x12U\n\x04name\x18\x01 \x01(\tBG\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob"}\n$DeleteEntityReconciliationJobRequest\x12U\n\x04name\x18\x01 \x01(\tBG\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob"\xd9\x05\n\x17EntityReconciliationJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12P\n\x0cinput_config\x18\x02 \x01(\x0b25.google.cloud.enterpriseknowledgegraph.v1.InputConfigB\x03\xe0A\x02\x12R\n\routput_config\x18\x03 \x01(\x0b26.google.cloud.enterpriseknowledgegraph.v1.OutputConfigB\x03\xe0A\x02\x12F\n\x05state\x18\x04 \x01(\x0e22.google.cloud.enterpriseknowledgegraph.v1.JobStateB\x03\xe0A\x03\x12&\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x0crecon_config\x18\t \x01(\x0b25.google.cloud.enterpriseknowledgegraph.v1.ReconConfigB\x03\xe0A\x01:\xa3\x01\xeaA\x9f\x01\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob\x12\\projects/{project}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}"\x8f\x01\n\rLookupRequest\x12Y\n\x06parent\x18\x01 \x01(\tBI\xe0A\x02\xfaAC\x12Aenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity\x12\x10\n\x03ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x11\n\tlanguages\x18\x03 \x03(\t"\x96\x01\n\x0eLookupResponse\x12\'\n\x07context\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x04type\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x11item_list_element\x18\x03 \x01(\x0b2\x1a.google.protobuf.ListValue"\xcc\x01\n\rSearchRequest\x12Y\n\x06parent\x18\x01 \x01(\tBI\xe0A\x02\xfaAC\x12Aenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tlanguages\x18\x03 \x03(\t\x12\r\n\x05types\x18\x04 \x03(\t\x12*\n\x05limit\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value"\x96\x01\n\x0eSearchResponse\x12\'\n\x07context\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x04type\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x11item_list_element\x18\x03 \x01(\x0b2\x1a.google.protobuf.ListValue"\x98\x01\n\x15LookupPublicKgRequest\x12Z\n\x06parent\x18\x01 \x01(\tBJ\xe0A\x02\xfaAD\x12Benterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity\x12\x10\n\x03ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x11\n\tlanguages\x18\x03 \x03(\t"\x9e\x01\n\x16LookupPublicKgResponse\x12\'\n\x07context\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x04type\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x11item_list_element\x18\x03 \x01(\x0b2\x1a.google.protobuf.ListValue"\xd5\x01\n\x15SearchPublicKgRequest\x12Z\n\x06parent\x18\x01 \x01(\tBJ\xe0A\x02\xfaAD\x12Benterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tlanguages\x18\x03 \x03(\t\x12\r\n\x05types\x18\x04 \x03(\t\x12*\n\x05limit\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int32Value"\x9e\x01\n\x16SearchPublicKgResponse\x12\'\n\x07context\x18\x01 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x04type\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x125\n\x11item_list_element\x18\x03 \x01(\x0b2\x1a.google.protobuf.ListValue2\x9d\x12\n\x1fEnterpriseKnowledgeGraphService\x12\xb7\x02\n\x1dCreateEntityReconciliationJob\x12N.google.cloud.enterpriseknowledgegraph.v1.CreateEntityReconciliationJobRequest\x1aA.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJob"\x82\x01\xdaA parent,entity_reconciliation_job\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/entityReconciliationJobs:\x19entity_reconciliation_job\x12\xf9\x01\n\x1aGetEntityReconciliationJob\x12K.google.cloud.enterpriseknowledgegraph.v1.GetEntityReconciliationJobRequest\x1aA.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJob"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/entityReconciliationJobs/*}\x12\x8c\x02\n\x1cListEntityReconciliationJobs\x12M.google.cloud.enterpriseknowledgegraph.v1.ListEntityReconciliationJobsRequest\x1aN.google.cloud.enterpriseknowledgegraph.v1.ListEntityReconciliationJobsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/entityReconciliationJobs\x12\xde\x01\n\x1dCancelEntityReconciliationJob\x12N.google.cloud.enterpriseknowledgegraph.v1.CancelEntityReconciliationJobRequest\x1a\x16.google.protobuf.Empty"U\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1/{name=projects/*/locations/*/entityReconciliationJobs/*}:cancel:\x01*\x12\xd4\x01\n\x1dDeleteEntityReconciliationJob\x12N.google.cloud.enterpriseknowledgegraph.v1.DeleteEntityReconciliationJobRequest\x1a\x16.google.protobuf.Empty"K\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/entityReconciliationJobs/*}\x12\xd8\x01\n\x06Lookup\x127.google.cloud.enterpriseknowledgegraph.v1.LookupRequest\x1a8.google.cloud.enterpriseknowledgegraph.v1.LookupResponse"[\xdaA\nparent,ids\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*}/cloudKnowledgeGraphEntities:Lookup\x12\xda\x01\n\x06Search\x127.google.cloud.enterpriseknowledgegraph.v1.SearchRequest\x1a8.google.cloud.enterpriseknowledgegraph.v1.SearchResponse"]\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*}/cloudKnowledgeGraphEntities:Search\x12\xf1\x01\n\x0eLookupPublicKg\x12?.google.cloud.enterpriseknowledgegraph.v1.LookupPublicKgRequest\x1a@.google.cloud.enterpriseknowledgegraph.v1.LookupPublicKgResponse"\\\xdaA\nparent,ids\x82\xd3\xe4\x93\x02I\x12G/v1/{parent=projects/*/locations/*}/publicKnowledgeGraphEntities:Lookup\x12\xf3\x01\n\x0eSearchPublicKg\x12?.google.cloud.enterpriseknowledgegraph.v1.SearchPublicKgRequest\x1a@.google.cloud.enterpriseknowledgegraph.v1.SearchPublicKgResponse"^\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02I\x12G/v1/{parent=projects/*/locations/*}/publicKnowledgeGraphEntities:Search\x1a[\xcaA\'enterpriseknowledgegraph.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa8\x06\n,com.google.cloud.enterpriseknowledgegraph.v1B\x0cServiceProtoP\x01Zhcloud.google.com/go/enterpriseknowledgegraph/apiv1/enterpriseknowledgegraphpb;enterpriseknowledgegraphpb\xaa\x02(Google.Cloud.EnterpriseKnowledgeGraph.V1\xca\x02(Google\\Cloud\\EnterpriseKnowledgeGraph\\V1\xea\x02+Google::Cloud::EnterpriseKnowledgeGraph::V1\xeaAH\n\x1fbigquery.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}\xeaA\xa7\x01\nAenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity\x12bprojects/{project}/locations/{location}/cloudKnowledgeGraphEntities/{cloud_knowledge_graph_entity}\xeaA\xaa\x01\nBenterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity\x12dprojects/{project}/locations/{location}/publicKnowledgeGraphEntities/{public_knowledge_graph_entity}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.enterpriseknowledgegraph.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.enterpriseknowledgegraph.v1B\x0cServiceProtoP\x01Zhcloud.google.com/go/enterpriseknowledgegraph/apiv1/enterpriseknowledgegraphpb;enterpriseknowledgegraphpb\xaa\x02(Google.Cloud.EnterpriseKnowledgeGraph.V1\xca\x02(Google\\Cloud\\EnterpriseKnowledgeGraph\\V1\xea\x02+Google::Cloud::EnterpriseKnowledgeGraph::V1\xeaAH\n\x1fbigquery.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}\xeaA\xa7\x01\nAenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity\x12bprojects/{project}/locations/{location}/cloudKnowledgeGraphEntities/{cloud_knowledge_graph_entity}\xeaA\xaa\x01\nBenterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity\x12dprojects/{project}/locations/{location}/publicKnowledgeGraphEntities/{public_knowledge_graph_entity}'
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['PEOPLE']._loaded_options = None
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['PEOPLE']._serialized_options = b'\x08\x01'
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['ESTABLISHMENT']._loaded_options = None
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['ESTABLISHMENT']._serialized_options = b'\x08\x01'
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['PROPERTY']._loaded_options = None
    _globals['_INPUTCONFIG_ENTITYTYPE'].values_by_name['PROPERTY']._serialized_options = b'\x08\x01'
    _globals['_INPUTCONFIG'].fields_by_name['previous_result_bigquery_table']._loaded_options = None
    _globals['_INPUTCONFIG'].fields_by_name['previous_result_bigquery_table']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BIGQUERYINPUTCONFIG'].fields_by_name['bigquery_table']._loaded_options = None
    _globals['_BIGQUERYINPUTCONFIG'].fields_by_name['bigquery_table']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BIGQUERYINPUTCONFIG'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_BIGQUERYINPUTCONFIG'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTCONFIG'].fields_by_name['bigquery_dataset']._loaded_options = None
    _globals['_OUTPUTCONFIG'].fields_by_name['bigquery_dataset']._serialized_options = b'\xfaA!\n\x1fbigquery.googleapis.com/Dataset'
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAA\x12?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob'
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['entity_reconciliation_job']._loaded_options = None
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['entity_reconciliation_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob'
    _globals['_LISTENTITYRECONCILIATIONJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTITYRECONCILIATIONJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAA\x12?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob'
    _globals['_CANCELENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob'
    _globals['_DELETEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTITYRECONCILIATIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaAA\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['name']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['input_config']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['output_config']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['state']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['error']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['recon_config']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB'].fields_by_name['recon_config']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYRECONCILIATIONJOB']._loaded_options = None
    _globals['_ENTITYRECONCILIATIONJOB']._serialized_options = b'\xeaA\x9f\x01\n?enterpriseknowledgegraph.googleapis.com/EntityReconciliationJob\x12\\projects/{project}/locations/{location}/entityReconciliationJobs/{entity_reconciliation_job}'
    _globals['_LOOKUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LOOKUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAC\x12Aenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity'
    _globals['_LOOKUPREQUEST'].fields_by_name['ids']._loaded_options = None
    _globals['_LOOKUPREQUEST'].fields_by_name['ids']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAC\x12Aenterpriseknowledgegraph.googleapis.com/CloudKnowledgeGraphEntity'
    _globals['_SEARCHREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPPUBLICKGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LOOKUPPUBLICKGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAD\x12Benterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity'
    _globals['_LOOKUPPUBLICKGREQUEST'].fields_by_name['ids']._loaded_options = None
    _globals['_LOOKUPPUBLICKGREQUEST'].fields_by_name['ids']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHPUBLICKGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHPUBLICKGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaAD\x12Benterpriseknowledgegraph.googleapis.com/PublicKnowledgeGraphEntity'
    _globals['_SEARCHPUBLICKGREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHPUBLICKGREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE']._serialized_options = b"\xcaA'enterpriseknowledgegraph.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform"
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['CreateEntityReconciliationJob']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['CreateEntityReconciliationJob']._serialized_options = b'\xdaA parent,entity_reconciliation_job\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/entityReconciliationJobs:\x19entity_reconciliation_job'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['GetEntityReconciliationJob']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['GetEntityReconciliationJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/entityReconciliationJobs/*}'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['ListEntityReconciliationJobs']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['ListEntityReconciliationJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/entityReconciliationJobs'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['CancelEntityReconciliationJob']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['CancelEntityReconciliationJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1/{name=projects/*/locations/*/entityReconciliationJobs/*}:cancel:\x01*'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['DeleteEntityReconciliationJob']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['DeleteEntityReconciliationJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/entityReconciliationJobs/*}'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['Lookup']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['Lookup']._serialized_options = b'\xdaA\nparent,ids\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*}/cloudKnowledgeGraphEntities:Lookup'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['Search']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['Search']._serialized_options = b'\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*}/cloudKnowledgeGraphEntities:Search'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['LookupPublicKg']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['LookupPublicKg']._serialized_options = b'\xdaA\nparent,ids\x82\xd3\xe4\x93\x02I\x12G/v1/{parent=projects/*/locations/*}/publicKnowledgeGraphEntities:Lookup'
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['SearchPublicKg']._loaded_options = None
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE'].methods_by_name['SearchPublicKg']._serialized_options = b'\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02I\x12G/v1/{parent=projects/*/locations/*}/publicKnowledgeGraphEntities:Search'
    _globals['_INPUTCONFIG']._serialized_start = 490
    _globals['_INPUTCONFIG']._serialized_end = 928
    _globals['_INPUTCONFIG_ENTITYTYPE']._serialized_start = 767
    _globals['_INPUTCONFIG_ENTITYTYPE']._serialized_end = 928
    _globals['_BIGQUERYINPUTCONFIG']._serialized_start = 930
    _globals['_BIGQUERYINPUTCONFIG']._serialized_end = 1036
    _globals['_OUTPUTCONFIG']._serialized_start = 1038
    _globals['_OUTPUTCONFIG']._serialized_end = 1116
    _globals['_RECONCONFIG']._serialized_start = 1119
    _globals['_RECONCONFIG']._serialized_end = 1640
    _globals['_RECONCONFIG_OPTIONS']._serialized_start = 1517
    _globals['_RECONCONFIG_OPTIONS']._serialized_end = 1563
    _globals['_RECONCONFIG_MODELCONFIG']._serialized_start = 1565
    _globals['_RECONCONFIG_MODELCONFIG']._serialized_end = 1619
    _globals['_CONNECTEDCOMPONENTSCONFIG']._serialized_start = 1642
    _globals['_CONNECTEDCOMPONENTSCONFIG']._serialized_end = 1695
    _globals['_AFFINITYCLUSTERINGCONFIG']._serialized_start = 1697
    _globals['_AFFINITYCLUSTERINGCONFIG']._serialized_end = 1756
    _globals['_DELETEOPERATIONMETADATA']._serialized_start = 1758
    _globals['_DELETEOPERATIONMETADATA']._serialized_end = 1875
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST']._serialized_start = 1878
    _globals['_CREATEENTITYRECONCILIATIONJOBREQUEST']._serialized_end = 2112
    _globals['_GETENTITYRECONCILIATIONJOBREQUEST']._serialized_start = 2114
    _globals['_GETENTITYRECONCILIATIONJOBREQUEST']._serialized_end = 2236
    _globals['_LISTENTITYRECONCILIATIONJOBSREQUEST']._serialized_start = 2239
    _globals['_LISTENTITYRECONCILIATIONJOBSREQUEST']._serialized_end = 2420
    _globals['_LISTENTITYRECONCILIATIONJOBSRESPONSE']._serialized_start = 2423
    _globals['_LISTENTITYRECONCILIATIONJOBSRESPONSE']._serialized_end = 2589
    _globals['_CANCELENTITYRECONCILIATIONJOBREQUEST']._serialized_start = 2591
    _globals['_CANCELENTITYRECONCILIATIONJOBREQUEST']._serialized_end = 2716
    _globals['_DELETEENTITYRECONCILIATIONJOBREQUEST']._serialized_start = 2718
    _globals['_DELETEENTITYRECONCILIATIONJOBREQUEST']._serialized_end = 2843
    _globals['_ENTITYRECONCILIATIONJOB']._serialized_start = 2846
    _globals['_ENTITYRECONCILIATIONJOB']._serialized_end = 3575
    _globals['_LOOKUPREQUEST']._serialized_start = 3578
    _globals['_LOOKUPREQUEST']._serialized_end = 3721
    _globals['_LOOKUPRESPONSE']._serialized_start = 3724
    _globals['_LOOKUPRESPONSE']._serialized_end = 3874
    _globals['_SEARCHREQUEST']._serialized_start = 3877
    _globals['_SEARCHREQUEST']._serialized_end = 4081
    _globals['_SEARCHRESPONSE']._serialized_start = 4084
    _globals['_SEARCHRESPONSE']._serialized_end = 4234
    _globals['_LOOKUPPUBLICKGREQUEST']._serialized_start = 4237
    _globals['_LOOKUPPUBLICKGREQUEST']._serialized_end = 4389
    _globals['_LOOKUPPUBLICKGRESPONSE']._serialized_start = 4392
    _globals['_LOOKUPPUBLICKGRESPONSE']._serialized_end = 4550
    _globals['_SEARCHPUBLICKGREQUEST']._serialized_start = 4553
    _globals['_SEARCHPUBLICKGREQUEST']._serialized_end = 4766
    _globals['_SEARCHPUBLICKGRESPONSE']._serialized_start = 4769
    _globals['_SEARCHPUBLICKGRESPONSE']._serialized_end = 4927
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE']._serialized_start = 4930
    _globals['_ENTERPRISEKNOWLEDGEGRAPHSERVICE']._serialized_end = 7263