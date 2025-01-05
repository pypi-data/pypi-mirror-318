"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/integrations/v1alpha/task_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.integrations.v1alpha import coordinate_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_coordinate__pb2
from .....google.cloud.integrations.v1alpha import event_parameter_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_event__parameter__pb2
from .....google.cloud.integrations.v1alpha import json_validation_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_json__validation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/integrations/v1alpha/task_config.proto\x12!google.cloud.integrations.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/cloud/integrations/v1alpha/coordinate.proto\x1a7google/cloud/integrations/v1alpha/event_parameter.proto\x1a7google/cloud/integrations/v1alpha/json_validation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd7\x0c\n\nTaskConfig\x12\x11\n\x04task\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07task_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12V\n\nparameters\x18\x03 \x03(\x0b2=.google.cloud.integrations.v1alpha.TaskConfig.ParametersEntryB\x03\xe0A\x01\x12M\n\x0efailure_policy\x18\x04 \x01(\x0b20.google.cloud.integrations.v1alpha.FailurePolicyB\x03\xe0A\x01\x12^\n\x1fsynchronous_call_failure_policy\x18\x05 \x01(\x0b20.google.cloud.integrations.v1alpha.FailurePolicyB\x03\xe0A\x01\x12h\n\x1cconditional_failure_policies\x18\x12 \x01(\x0b2=.google.cloud.integrations.v1alpha.ConditionalFailurePoliciesB\x03\xe0A\x01\x12D\n\nnext_tasks\x18\x06 \x03(\x0b2+.google.cloud.integrations.v1alpha.NextTaskB\x03\xe0A\x01\x12p\n\x1bnext_tasks_execution_policy\x18\x07 \x01(\x0e2F.google.cloud.integrations.v1alpha.TaskConfig.NextTasksExecutionPolicyB\x03\xe0A\x01\x12i\n\x17task_execution_strategy\x18\x08 \x01(\x0e2C.google.cloud.integrations.v1alpha.TaskConfig.TaskExecutionStrategyB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\t \x01(\tB\x03\xe0A\x01\x12M\n\x0esuccess_policy\x18\n \x01(\x0b20.google.cloud.integrations.v1alpha.SuccessPolicyB\x03\xe0A\x01\x12\\\n\x16json_validation_option\x18\x0b \x01(\x0e27.google.cloud.integrations.v1alpha.JsonValidationOptionB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x0c \x01(\tB\x03\xe0A\x01\x12\x1a\n\rtask_template\x18\r \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10error_catcher_id\x18\x11 \x01(\tB\x03\xe0A\x01\x12_\n\x12external_task_type\x18\x0f \x01(\x0e2>.google.cloud.integrations.v1alpha.TaskConfig.ExternalTaskTypeB\x03\xe0A\x01\x12D\n\x08position\x18\x10 \x01(\x0b2-.google.cloud.integrations.v1alpha.CoordinateB\x03\xe0A\x01\x1ad\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.integrations.v1alpha.EventParameter:\x028\x01"o\n\x18NextTasksExecutionPolicy\x12+\n\'NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED\x10\x00\x12\x11\n\rRUN_ALL_MATCH\x10\x01\x12\x13\n\x0fRUN_FIRST_MATCH\x10\x02"\x97\x01\n\x15TaskExecutionStrategy\x12\'\n#TASK_EXECUTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x14\n\x10WHEN_ALL_SUCCEED\x10\x01\x12\x14\n\x10WHEN_ANY_SUCCEED\x10\x02\x12)\n%WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED\x10\x03"W\n\x10ExternalTaskType\x12"\n\x1eEXTERNAL_TASK_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNORMAL_TASK\x10\x01\x12\x0e\n\nERROR_TASK\x10\x02"\xaa\x01\n\rSuccessPolicy\x12P\n\x0bfinal_state\x18\x01 \x01(\x0e2;.google.cloud.integrations.v1alpha.SuccessPolicy.FinalState"G\n\nFinalState\x12\x1b\n\x17FINAL_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\r\n\tSUSPENDED\x10\x02"\xfc\x02\n\rFailurePolicy\x12V\n\x0eretry_strategy\x18\x01 \x01(\x0e2>.google.cloud.integrations.v1alpha.FailurePolicy.RetryStrategy\x12\x13\n\x0bmax_retries\x18\x02 \x01(\x05\x121\n\rinterval_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x11\n\tcondition\x18\x04 \x01(\t"\xb7\x01\n\rRetryStrategy\x12\x1e\n\x1aRETRY_STRATEGY_UNSPECIFIED\x10\x00\x12\n\n\x06IGNORE\x10\x01\x12\x08\n\x04NONE\x10\x02\x12\t\n\x05FATAL\x10\x03\x12\x12\n\x0eFIXED_INTERVAL\x10\x04\x12\x12\n\x0eLINEAR_BACKOFF\x10\x05\x12\x17\n\x13EXPONENTIAL_BACKOFF\x10\x06\x12$\n RESTART_INTEGRATION_WITH_BACKOFF\x10\x07"q\n\x08NextTask\x12\x16\n\x0etask_config_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x11\n\tcondition\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"\xba\x01\n\x1aConditionalFailurePolicies\x12J\n\x10failure_policies\x18\x01 \x03(\x0b20.google.cloud.integrations.v1alpha.FailurePolicy\x12P\n\x16default_failure_policy\x18\x02 \x01(\x0b20.google.cloud.integrations.v1alpha.FailurePolicyB\xa9\x01\n%com.google.cloud.integrations.v1alphaB\x0fTaskConfigProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.integrations.v1alpha.task_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\x0fTaskConfigProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alpha'
    _globals['_TASKCONFIG_PARAMETERSENTRY']._loaded_options = None
    _globals['_TASKCONFIG_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_TASKCONFIG'].fields_by_name['task']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['task']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['task_id']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['task_id']._serialized_options = b'\xe0A\x02'
    _globals['_TASKCONFIG'].fields_by_name['parameters']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['failure_policy']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['failure_policy']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['synchronous_call_failure_policy']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['synchronous_call_failure_policy']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['conditional_failure_policies']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['conditional_failure_policies']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['next_tasks']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['next_tasks']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['next_tasks_execution_policy']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['next_tasks_execution_policy']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['task_execution_strategy']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['task_execution_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['display_name']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['success_policy']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['success_policy']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['json_validation_option']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['json_validation_option']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['description']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['task_template']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['task_template']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['error_catcher_id']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['error_catcher_id']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['external_task_type']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['external_task_type']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG'].fields_by_name['position']._loaded_options = None
    _globals['_TASKCONFIG'].fields_by_name['position']._serialized_options = b'\xe0A\x01'
    _globals['_TASKCONFIG']._serialized_start = 323
    _globals['_TASKCONFIG']._serialized_end = 1946
    _globals['_TASKCONFIG_PARAMETERSENTRY']._serialized_start = 1490
    _globals['_TASKCONFIG_PARAMETERSENTRY']._serialized_end = 1590
    _globals['_TASKCONFIG_NEXTTASKSEXECUTIONPOLICY']._serialized_start = 1592
    _globals['_TASKCONFIG_NEXTTASKSEXECUTIONPOLICY']._serialized_end = 1703
    _globals['_TASKCONFIG_TASKEXECUTIONSTRATEGY']._serialized_start = 1706
    _globals['_TASKCONFIG_TASKEXECUTIONSTRATEGY']._serialized_end = 1857
    _globals['_TASKCONFIG_EXTERNALTASKTYPE']._serialized_start = 1859
    _globals['_TASKCONFIG_EXTERNALTASKTYPE']._serialized_end = 1946
    _globals['_SUCCESSPOLICY']._serialized_start = 1949
    _globals['_SUCCESSPOLICY']._serialized_end = 2119
    _globals['_SUCCESSPOLICY_FINALSTATE']._serialized_start = 2048
    _globals['_SUCCESSPOLICY_FINALSTATE']._serialized_end = 2119
    _globals['_FAILUREPOLICY']._serialized_start = 2122
    _globals['_FAILUREPOLICY']._serialized_end = 2502
    _globals['_FAILUREPOLICY_RETRYSTRATEGY']._serialized_start = 2319
    _globals['_FAILUREPOLICY_RETRYSTRATEGY']._serialized_end = 2502
    _globals['_NEXTTASK']._serialized_start = 2504
    _globals['_NEXTTASK']._serialized_end = 2617
    _globals['_CONDITIONALFAILUREPOLICIES']._serialized_start = 2620
    _globals['_CONDITIONALFAILUREPOLICIES']._serialized_end = 2806