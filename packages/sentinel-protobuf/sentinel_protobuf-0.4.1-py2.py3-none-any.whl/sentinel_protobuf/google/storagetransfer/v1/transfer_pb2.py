"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/storagetransfer/v1/transfer.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ....google.storagetransfer.v1 import transfer_types_pb2 as google_dot_storagetransfer_dot_v1_dot_transfer__types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/storagetransfer/v1/transfer.proto\x12\x19google.storagetransfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a.google/storagetransfer/v1/transfer_types.proto"9\n\x1eGetGoogleServiceAccountRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02"]\n\x18CreateTransferJobRequest\x12A\n\x0ctransfer_job\x18\x01 \x01(\x0b2&.google.storagetransfer.v1.TransferJobB\x03\xe0A\x02"\xd1\x01\n\x18UpdateTransferJobRequest\x12\x15\n\x08job_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x0ctransfer_job\x18\x03 \x01(\x0b2&.google.storagetransfer.v1.TransferJobB\x03\xe0A\x02\x12B\n\x1eupdate_transfer_job_field_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask"G\n\x15GetTransferJobRequest\x12\x15\n\x08job_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x02"J\n\x18DeleteTransferJobRequest\x12\x15\n\x08job_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x02"U\n\x17ListTransferJobsRequest\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"r\n\x18ListTransferJobsResponse\x12=\n\rtransfer_jobs\x18\x01 \x03(\x0b2&.google.storagetransfer.v1.TransferJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"2\n\x1dPauseTransferOperationRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"3\n\x1eResumeTransferOperationRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"G\n\x15RunTransferJobRequest\x12\x15\n\x08job_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproject_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x8c\x01\n\x16CreateAgentPoolRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12=\n\nagent_pool\x18\x02 \x01(\x0b2$.google.storagetransfer.v1.AgentPoolB\x03\xe0A\x02\x12\x1a\n\ragent_pool_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x88\x01\n\x16UpdateAgentPoolRequest\x12=\n\nagent_pool\x18\x01 \x01(\x0b2$.google.storagetransfer.v1.AgentPoolB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"(\n\x13GetAgentPoolRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"+\n\x16DeleteAgentPoolRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"g\n\x15ListAgentPoolsRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"l\n\x16ListAgentPoolsResponse\x129\n\x0bagent_pools\x18\x01 \x03(\x0b2$.google.storagetransfer.v1.AgentPool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x91\x13\n\x16StorageTransferService\x12\xb5\x01\n\x17GetGoogleServiceAccount\x129.google.storagetransfer.v1.GetGoogleServiceAccountRequest\x1a/.google.storagetransfer.v1.GoogleServiceAccount".\x82\xd3\xe4\x93\x02(\x12&/v1/googleServiceAccounts/{project_id}\x12\x98\x01\n\x11CreateTransferJob\x123.google.storagetransfer.v1.CreateTransferJobRequest\x1a&.google.storagetransfer.v1.TransferJob"&\x82\xd3\xe4\x93\x02 "\x10/v1/transferJobs:\x0ctransfer_job\x12\x9b\x01\n\x11UpdateTransferJob\x123.google.storagetransfer.v1.UpdateTransferJobRequest\x1a&.google.storagetransfer.v1.TransferJob")\x82\xd3\xe4\x93\x02#2\x1e/v1/{job_name=transferJobs/**}:\x01*\x12\x92\x01\n\x0eGetTransferJob\x120.google.storagetransfer.v1.GetTransferJobRequest\x1a&.google.storagetransfer.v1.TransferJob"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{job_name=transferJobs/**}\x12\x95\x01\n\x10ListTransferJobs\x122.google.storagetransfer.v1.ListTransferJobsRequest\x1a3.google.storagetransfer.v1.ListTransferJobsResponse"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/transferJobs\x12\x9d\x01\n\x16PauseTransferOperation\x128.google.storagetransfer.v1.PauseTransferOperationRequest\x1a\x16.google.protobuf.Empty"1\x82\xd3\xe4\x93\x02+"&/v1/{name=transferOperations/**}:pause:\x01*\x12\xa0\x01\n\x17ResumeTransferOperation\x129.google.storagetransfer.v1.ResumeTransferOperationRequest\x1a\x16.google.protobuf.Empty"2\x82\xd3\xe4\x93\x02,"\'/v1/{name=transferOperations/**}:resume:\x01*\x12\xbd\x01\n\x0eRunTransferJob\x120.google.storagetransfer.v1.RunTransferJobRequest\x1a\x1d.google.longrunning.Operation"Z\xcaA*\n\x15google.protobuf.Empty\x12\x11TransferOperation\x82\xd3\xe4\x93\x02\'""/v1/{job_name=transferJobs/**}:run:\x01*\x12\x88\x01\n\x11DeleteTransferJob\x123.google.storagetransfer.v1.DeleteTransferJobRequest\x1a\x16.google.protobuf.Empty"&\x82\xd3\xe4\x93\x02 *\x1e/v1/{job_name=transferJobs/**}\x12\xcc\x01\n\x0fCreateAgentPool\x121.google.storagetransfer.v1.CreateAgentPoolRequest\x1a$.google.storagetransfer.v1.AgentPool"`\xdaA#project_id,agent_pool,agent_pool_id\x82\xd3\xe4\x93\x024"&/v1/projects/{project_id=*}/agentPools:\nagent_pool\x12\xc6\x01\n\x0fUpdateAgentPool\x121.google.storagetransfer.v1.UpdateAgentPoolRequest\x1a$.google.storagetransfer.v1.AgentPool"Z\xdaA\x16agent_pool,update_mask\x82\xd3\xe4\x93\x02;2-/v1/{agent_pool.name=projects/*/agentPools/*}:\nagent_pool\x12\x97\x01\n\x0cGetAgentPool\x12..google.storagetransfer.v1.GetAgentPoolRequest\x1a$.google.storagetransfer.v1.AgentPool"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=projects/*/agentPools/*}\x12\xb2\x01\n\x0eListAgentPools\x120.google.storagetransfer.v1.ListAgentPoolsRequest\x1a1.google.storagetransfer.v1.ListAgentPoolsResponse";\xdaA\nproject_id\x82\xd3\xe4\x93\x02(\x12&/v1/projects/{project_id=*}/agentPools\x12\x8f\x01\n\x0fDeleteAgentPool\x121.google.storagetransfer.v1.DeleteAgentPoolRequest\x1a\x16.google.protobuf.Empty"1\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=projects/*/agentPools/*}\x1aR\xcaA\x1estoragetransfer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xec\x01\n#com.google.storagetransfer.v1.protoB\rTransferProtoZMcloud.google.com/go/storagetransfer/apiv1/storagetransferpb;storagetransferpb\xaa\x02\x1fGoogle.Cloud.StorageTransfer.V1\xca\x02\x1fGoogle\\Cloud\\StorageTransfer\\V1\xea\x02"Google::Cloud::StorageTransfer::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.storagetransfer.v1.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.storagetransfer.v1.protoB\rTransferProtoZMcloud.google.com/go/storagetransfer/apiv1/storagetransferpb;storagetransferpb\xaa\x02\x1fGoogle.Cloud.StorageTransfer.V1\xca\x02\x1fGoogle\\Cloud\\StorageTransfer\\V1\xea\x02"Google::Cloud::StorageTransfer::V1'
    _globals['_GETGOOGLESERVICEACCOUNTREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETGOOGLESERVICEACCOUNTREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETRANSFERJOBREQUEST'].fields_by_name['transfer_job']._loaded_options = None
    _globals['_CREATETRANSFERJOBREQUEST'].fields_by_name['transfer_job']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['job_name']._loaded_options = None
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['job_name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['transfer_job']._loaded_options = None
    _globals['_UPDATETRANSFERJOBREQUEST'].fields_by_name['transfer_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRANSFERJOBREQUEST'].fields_by_name['job_name']._loaded_options = None
    _globals['_GETTRANSFERJOBREQUEST'].fields_by_name['job_name']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRANSFERJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETTRANSFERJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETRANSFERJOBREQUEST'].fields_by_name['job_name']._loaded_options = None
    _globals['_DELETETRANSFERJOBREQUEST'].fields_by_name['job_name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETRANSFERJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETETRANSFERJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTRANSFERJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTRANSFERJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PAUSETRANSFEROPERATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSETRANSFEROPERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RESUMETRANSFEROPERATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMETRANSFEROPERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RUNTRANSFERJOBREQUEST'].fields_by_name['job_name']._loaded_options = None
    _globals['_RUNTRANSFERJOBREQUEST'].fields_by_name['job_name']._serialized_options = b'\xe0A\x02'
    _globals['_RUNTRANSFERJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_RUNTRANSFERJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['agent_pool']._loaded_options = None
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['agent_pool']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['agent_pool_id']._loaded_options = None
    _globals['_CREATEAGENTPOOLREQUEST'].fields_by_name['agent_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAGENTPOOLREQUEST'].fields_by_name['agent_pool']._loaded_options = None
    _globals['_UPDATEAGENTPOOLREQUEST'].fields_by_name['agent_pool']._serialized_options = b'\xe0A\x02'
    _globals['_GETAGENTPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAGENTPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAGENTPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAGENTPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAGENTPOOLSREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTAGENTPOOLSREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGETRANSFERSERVICE']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE']._serialized_options = b'\xcaA\x1estoragetransfer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetGoogleServiceAccount']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetGoogleServiceAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/v1/googleServiceAccounts/{project_id}'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['CreateTransferJob']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['CreateTransferJob']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x10/v1/transferJobs:\x0ctransfer_job'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['UpdateTransferJob']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['UpdateTransferJob']._serialized_options = b'\x82\xd3\xe4\x93\x02#2\x1e/v1/{job_name=transferJobs/**}:\x01*'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetTransferJob']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetTransferJob']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{job_name=transferJobs/**}'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ListTransferJobs']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ListTransferJobs']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/transferJobs'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['PauseTransferOperation']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['PauseTransferOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02+"&/v1/{name=transferOperations/**}:pause:\x01*'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ResumeTransferOperation']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ResumeTransferOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v1/{name=transferOperations/**}:resume:\x01*'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['RunTransferJob']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['RunTransferJob']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11TransferOperation\x82\xd3\xe4\x93\x02\'""/v1/{job_name=transferJobs/**}:run:\x01*'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['DeleteTransferJob']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['DeleteTransferJob']._serialized_options = b'\x82\xd3\xe4\x93\x02 *\x1e/v1/{job_name=transferJobs/**}'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['CreateAgentPool']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['CreateAgentPool']._serialized_options = b'\xdaA#project_id,agent_pool,agent_pool_id\x82\xd3\xe4\x93\x024"&/v1/projects/{project_id=*}/agentPools:\nagent_pool'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['UpdateAgentPool']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['UpdateAgentPool']._serialized_options = b'\xdaA\x16agent_pool,update_mask\x82\xd3\xe4\x93\x02;2-/v1/{agent_pool.name=projects/*/agentPools/*}:\nagent_pool'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetAgentPool']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['GetAgentPool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=projects/*/agentPools/*}'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ListAgentPools']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['ListAgentPools']._serialized_options = b'\xdaA\nproject_id\x82\xd3\xe4\x93\x02(\x12&/v1/projects/{project_id=*}/agentPools'
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['DeleteAgentPool']._loaded_options = None
    _globals['_STORAGETRANSFERSERVICE'].methods_by_name['DeleteAgentPool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/v1/{name=projects/*/agentPools/*}'
    _globals['_GETGOOGLESERVICEACCOUNTREQUEST']._serialized_start = 307
    _globals['_GETGOOGLESERVICEACCOUNTREQUEST']._serialized_end = 364
    _globals['_CREATETRANSFERJOBREQUEST']._serialized_start = 366
    _globals['_CREATETRANSFERJOBREQUEST']._serialized_end = 459
    _globals['_UPDATETRANSFERJOBREQUEST']._serialized_start = 462
    _globals['_UPDATETRANSFERJOBREQUEST']._serialized_end = 671
    _globals['_GETTRANSFERJOBREQUEST']._serialized_start = 673
    _globals['_GETTRANSFERJOBREQUEST']._serialized_end = 744
    _globals['_DELETETRANSFERJOBREQUEST']._serialized_start = 746
    _globals['_DELETETRANSFERJOBREQUEST']._serialized_end = 820
    _globals['_LISTTRANSFERJOBSREQUEST']._serialized_start = 822
    _globals['_LISTTRANSFERJOBSREQUEST']._serialized_end = 907
    _globals['_LISTTRANSFERJOBSRESPONSE']._serialized_start = 909
    _globals['_LISTTRANSFERJOBSRESPONSE']._serialized_end = 1023
    _globals['_PAUSETRANSFEROPERATIONREQUEST']._serialized_start = 1025
    _globals['_PAUSETRANSFEROPERATIONREQUEST']._serialized_end = 1075
    _globals['_RESUMETRANSFEROPERATIONREQUEST']._serialized_start = 1077
    _globals['_RESUMETRANSFEROPERATIONREQUEST']._serialized_end = 1128
    _globals['_RUNTRANSFERJOBREQUEST']._serialized_start = 1130
    _globals['_RUNTRANSFERJOBREQUEST']._serialized_end = 1201
    _globals['_CREATEAGENTPOOLREQUEST']._serialized_start = 1204
    _globals['_CREATEAGENTPOOLREQUEST']._serialized_end = 1344
    _globals['_UPDATEAGENTPOOLREQUEST']._serialized_start = 1347
    _globals['_UPDATEAGENTPOOLREQUEST']._serialized_end = 1483
    _globals['_GETAGENTPOOLREQUEST']._serialized_start = 1485
    _globals['_GETAGENTPOOLREQUEST']._serialized_end = 1525
    _globals['_DELETEAGENTPOOLREQUEST']._serialized_start = 1527
    _globals['_DELETEAGENTPOOLREQUEST']._serialized_end = 1570
    _globals['_LISTAGENTPOOLSREQUEST']._serialized_start = 1572
    _globals['_LISTAGENTPOOLSREQUEST']._serialized_end = 1675
    _globals['_LISTAGENTPOOLSRESPONSE']._serialized_start = 1677
    _globals['_LISTAGENTPOOLSRESPONSE']._serialized_end = 1785
    _globals['_STORAGETRANSFERSERVICE']._serialized_start = 1788
    _globals['_STORAGETRANSFERSERVICE']._serialized_end = 4237