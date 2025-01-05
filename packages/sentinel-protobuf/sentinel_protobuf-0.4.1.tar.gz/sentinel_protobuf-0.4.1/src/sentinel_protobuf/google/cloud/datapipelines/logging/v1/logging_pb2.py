"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datapipelines/logging/v1/logging.proto')
_sym_db = _symbol_database.Default()
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/datapipelines/logging/v1/logging.proto\x12%google.cloud.datapipelines.logging.v1\x1a\x17google/rpc/status.proto"\xb8\t\n\x0fRequestLogEntry\x12X\n\x0crequest_type\x18\x01 \x01(\x0e2B.google.cloud.datapipelines.logging.v1.RequestLogEntry.RequestType\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12V\n\x0berror_cause\x18\x03 \x01(\x0e2A.google.cloud.datapipelines.logging.v1.RequestLogEntry.ErrorCause"\xc4\x01\n\x0bRequestType\x12\x1c\n\x18REQUEST_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCREATE_PIPELINE\x10\x01\x12\x13\n\x0fUPDATE_PIPELINE\x10\x02\x12\x13\n\x0fDELETE_PIPELINE\x10\x03\x12\x12\n\x0eLIST_PIPELINES\x10\x04\x12\x10\n\x0cGET_PIPELINE\x10\x05\x12\x11\n\rSTOP_PIPELINE\x10\x06\x12\x10\n\x0cRUN_PIPELINE\x10\x07\x12\r\n\tLIST_JOBS\x10\x08"\x87\x06\n\nErrorCause\x12\x1b\n\x17ERROR_CAUSE_UNSPECIFIED\x10\x00\x12\x13\n\x0fINVALID_REQUEST\x10\x01\x12\x1c\n\x18PROJECT_NUMBER_NOT_FOUND\x10\x02\x12\x1e\n\x1aPIPELINE_ID_ALREADY_EXISTS\x10\x03\x12$\n PIPELINE_QUOTA_ALLOCATION_FAILED\x10\x04\x12\x16\n\x12PIPELINE_NOT_FOUND\x10\x05\x12\x1d\n\x19INVALID_PIPELINE_WORKLOAD\x10\x06\x125\n1DATAFLOW_WORKER_SERVICE_ACCOUNT_PERMISSION_DENIED\x10\x07\x125\n1CLOUD_SCHEDULER_SERVICE_ACCOUNT_PERMISSION_DENIED\x10\x08\x121\n-INTERNAL_DATA_PIPELINES_SERVICE_ACCOUNT_ISSUE\x10\t\x12$\n CLOUD_SCHEDULER_INVALID_ARGUMENT\x10\n\x12&\n"CLOUD_SCHEDULER_RESOURCE_EXHAUSTED\x10\x0b\x12!\n\x1dCLOUD_SCHEDULER_JOB_NOT_FOUND\x10\x0c\x12\x1f\n\x1bOTHER_CLOUD_SCHEDULER_ISSUE\x10\r\x12\x1f\n\x1bDATAFLOW_JOB_ALREADY_EXISTS\x10\x0e\x12\x1d\n\x19DATAFLOW_INVALID_ARGUMENT\x10\x0f\x12\x1f\n\x1bDATAFLOW_RESOURCE_EXHAUSTED\x10\x10\x12\x1a\n\x16DATAFLOW_JOB_NOT_FOUND\x10\x11\x12\x18\n\x14OTHER_DATAFLOW_ISSUE\x10\x12\x12\x12\n\x0eDATABASE_ERROR\x10\x13\x12\x17\n\x13WRONG_PIPELINE_TYPE\x10\x14\x12\x12\n\x0eINTERNAL_ERROR\x10\x15\x12!\n\x1dPIPELINE_OR_PROJECT_NOT_FOUND\x10\x16B\x80\x01\n)com.google.cloud.datapipelines.logging.v1B\x0cLoggingProtoP\x01ZCcloud.google.com/go/datapipelines/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datapipelines.logging.v1.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.datapipelines.logging.v1B\x0cLoggingProtoP\x01ZCcloud.google.com/go/datapipelines/logging/apiv1/loggingpb;loggingpb'
    _globals['_REQUESTLOGENTRY']._serialized_start = 120
    _globals['_REQUESTLOGENTRY']._serialized_end = 1328
    _globals['_REQUESTLOGENTRY_REQUESTTYPE']._serialized_start = 354
    _globals['_REQUESTLOGENTRY_REQUESTTYPE']._serialized_end = 550
    _globals['_REQUESTLOGENTRY_ERRORCAUSE']._serialized_start = 553
    _globals['_REQUESTLOGENTRY_ERRORCAUSE']._serialized_end = 1328