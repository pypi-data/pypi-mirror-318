"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/run/v2/condition.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/run/v2/condition.proto\x12\x13google.cloud.run.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xac\x0c\n\tCondition\x12\x0c\n\x04type\x18\x01 \x01(\t\x123\n\x05state\x18\x02 \x01(\x0e2$.google.cloud.run.v2.Condition.State\x12\x0f\n\x07message\x18\x03 \x01(\t\x128\n\x14last_transition_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x129\n\x08severity\x18\x05 \x01(\x0e2\'.google.cloud.run.v2.Condition.Severity\x12B\n\x06reason\x18\x06 \x01(\x0e2+.google.cloud.run.v2.Condition.CommonReasonB\x03\xe0A\x03H\x00\x12M\n\x0frevision_reason\x18\t \x01(\x0e2-.google.cloud.run.v2.Condition.RevisionReasonB\x03\xe0A\x03H\x00\x12O\n\x10execution_reason\x18\x0b \x01(\x0e2..google.cloud.run.v2.Condition.ExecutionReasonB\x03\xe0A\x03H\x00"\x7f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11CONDITION_PENDING\x10\x01\x12\x19\n\x15CONDITION_RECONCILING\x10\x02\x12\x14\n\x10CONDITION_FAILED\x10\x03\x12\x17\n\x13CONDITION_SUCCEEDED\x10\x04"F\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x08\n\x04INFO\x10\x03"\xb2\x03\n\x0cCommonReason\x12\x1b\n\x17COMMON_REASON_UNDEFINED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fREVISION_FAILED\x10\x03\x12\x1e\n\x1aPROGRESS_DEADLINE_EXCEEDED\x10\x04\x12\x15\n\x11CONTAINER_MISSING\x10\x06\x12\x1f\n\x1bCONTAINER_PERMISSION_DENIED\x10\x07\x12 \n\x1cCONTAINER_IMAGE_UNAUTHORIZED\x10\x08\x12.\n*CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED\x10\t\x12$\n ENCRYPTION_KEY_PERMISSION_DENIED\x10\n\x12\x1f\n\x1bENCRYPTION_KEY_CHECK_FAILED\x10\x0b\x12\x1f\n\x1bSECRETS_ACCESS_CHECK_FAILED\x10\x0c\x12\x19\n\x15WAITING_FOR_OPERATION\x10\r\x12\x13\n\x0fIMMEDIATE_RETRY\x10\x0e\x12\x13\n\x0fPOSTPONED_RETRY\x10\x0f\x12\x0c\n\x08INTERNAL\x10\x10"\xca\x02\n\x0eRevisionReason\x12\x1d\n\x19REVISION_REASON_UNDEFINED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RESERVE\x10\x02\x12\x0b\n\x07RETIRED\x10\x03\x12\x0c\n\x08RETIRING\x10\x04\x12\x0e\n\nRECREATING\x10\x05\x12 \n\x1cHEALTH_CHECK_CONTAINER_ERROR\x10\x06\x12$\n CUSTOMIZED_PATH_RESPONSE_PENDING\x10\x07\x12!\n\x1dMIN_INSTANCES_NOT_PROVISIONED\x10\x08\x12!\n\x1dACTIVE_REVISION_LIMIT_REACHED\x10\t\x12\x11\n\rNO_DEPLOYMENT\x10\n\x12\x18\n\x14HEALTH_CHECK_SKIPPED\x10\x0b\x12\x19\n\x15MIN_INSTANCES_WARMING\x10\x0c"\x9b\x01\n\x0fExecutionReason\x12\x1e\n\x1aEXECUTION_REASON_UNDEFINED\x10\x00\x12$\n JOB_STATUS_SERVICE_POLLING_ERROR\x10\x01\x12\x16\n\x12NON_ZERO_EXIT_CODE\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0e\n\nCANCELLING\x10\x04\x12\x0b\n\x07DELETED\x10\x05B\t\n\x07reasonsBV\n\x17com.google.cloud.run.v2B\x0eConditionProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.run.v2.condition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.run.v2B\x0eConditionProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb'
    _globals['_CONDITION'].fields_by_name['reason']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['reason']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITION'].fields_by_name['revision_reason']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['revision_reason']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITION'].fields_by_name['execution_reason']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['execution_reason']._serialized_options = b'\xe0A\x03'
    _globals['_CONDITION']._serialized_start = 127
    _globals['_CONDITION']._serialized_end = 1707
    _globals['_CONDITION_STATE']._serialized_start = 569
    _globals['_CONDITION_STATE']._serialized_end = 696
    _globals['_CONDITION_SEVERITY']._serialized_start = 698
    _globals['_CONDITION_SEVERITY']._serialized_end = 768
    _globals['_CONDITION_COMMONREASON']._serialized_start = 771
    _globals['_CONDITION_COMMONREASON']._serialized_end = 1205
    _globals['_CONDITION_REVISIONREASON']._serialized_start = 1208
    _globals['_CONDITION_REVISIONREASON']._serialized_end = 1538
    _globals['_CONDITION_EXECUTIONREASON']._serialized_start = 1541
    _globals['_CONDITION_EXECUTIONREASON']._serialized_end = 1696