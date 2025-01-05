"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/rule_engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/contentwarehouse/v1/rule_engine.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1agoogle/iam/v1/policy.proto"\xde\x01\n\x07RuleSet\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x125\n\x05rules\x18\x03 \x03(\x0b2&.google.cloud.contentwarehouse.v1.Rule:i\xeaAf\n\'contentwarehouse.googleapis.com/RuleSet\x12;projects/{project}/locations/{location}/ruleSets/{rule_set}"\xa6\x02\n\x04Rule\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x0f\n\x07rule_id\x18\x02 \x01(\t\x12H\n\x0ctrigger_type\x18\x03 \x01(\x0e22.google.cloud.contentwarehouse.v1.Rule.TriggerType\x12\x11\n\tcondition\x18\x04 \x01(\t\x129\n\x07actions\x18\x05 \x03(\x0b2(.google.cloud.contentwarehouse.v1.Action"`\n\x0bTriggerType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tON_CREATE\x10\x01\x12\r\n\tON_UPDATE\x10\x04\x12\x12\n\x0eON_CREATE_LINK\x10\x07\x12\x12\n\x0eON_DELETE_LINK\x10\x08"\xea\x04\n\x06Action\x12\x11\n\taction_id\x18\x01 \x01(\t\x12O\n\x0eaccess_control\x18\x02 \x01(\x0b25.google.cloud.contentwarehouse.v1.AccessControlActionH\x00\x12Q\n\x0fdata_validation\x18\x03 \x01(\x0b26.google.cloud.contentwarehouse.v1.DataValidationActionH\x00\x12I\n\x0bdata_update\x18\x04 \x01(\x0b22.google.cloud.contentwarehouse.v1.DataUpdateActionH\x00\x12L\n\radd_to_folder\x18\x05 \x01(\x0b23.google.cloud.contentwarehouse.v1.AddToFolderActionH\x00\x12M\n\x12publish_to_pub_sub\x18\x06 \x01(\x0b2/.google.cloud.contentwarehouse.v1.PublishActionH\x00\x12]\n\x19remove_from_folder_action\x18\t \x01(\x0b28.google.cloud.contentwarehouse.v1.RemoveFromFolderActionH\x00\x12X\n\x16delete_document_action\x18\n \x01(\x0b26.google.cloud.contentwarehouse.v1.DeleteDocumentActionH\x00B\x08\n\x06action"\x86\x02\n\x13AccessControlAction\x12[\n\x0eoperation_type\x18\x01 \x01(\x0e2C.google.cloud.contentwarehouse.v1.AccessControlAction.OperationType\x12%\n\x06policy\x18\x02 \x01(\x0b2\x15.google.iam.v1.Policy"k\n\rOperationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\x12ADD_POLICY_BINDING\x10\x01\x12\x19\n\x15REMOVE_POLICY_BINDING\x10\x02\x12\x1a\n\x16REPLACE_POLICY_BINDING\x10\x03"\xa5\x01\n\x14DataValidationAction\x12Z\n\nconditions\x18\x01 \x03(\x0b2F.google.cloud.contentwarehouse.v1.DataValidationAction.ConditionsEntry\x1a1\n\x0fConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x94\x01\n\x10DataUpdateAction\x12P\n\x07entries\x18\x01 \x03(\x0b2?.google.cloud.contentwarehouse.v1.DataUpdateAction.EntriesEntry\x1a.\n\x0cEntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"S\n\x11AddToFolderAction\x12>\n\x07folders\x18\x01 \x03(\tB-\xfaA*\n(contentwarehouse.googleapis.com/Document"j\n\x16RemoveFromFolderAction\x12\x11\n\tcondition\x18\x01 \x01(\t\x12=\n\x06folder\x18\x02 \x01(\tB-\xfaA*\n(contentwarehouse.googleapis.com/Document"3\n\rPublishAction\x12\x10\n\x08topic_id\x18\x01 \x01(\t\x12\x10\n\x08messages\x18\x02 \x03(\t"2\n\x14DeleteDocumentAction\x12\x1a\n\x12enable_hard_delete\x18\x01 \x01(\x08"\xd7\x01\n\x10RuleEngineOutput\x12\x15\n\rdocument_name\x18\x03 \x01(\t\x12T\n\x15rule_evaluator_output\x18\x01 \x01(\x0b25.google.cloud.contentwarehouse.v1.RuleEvaluatorOutput\x12V\n\x16action_executor_output\x18\x02 \x01(\x0b26.google.cloud.contentwarehouse.v1.ActionExecutorOutput"\xdb\x01\n\x13RuleEvaluatorOutput\x12?\n\x0ftriggered_rules\x18\x01 \x03(\x0b2&.google.cloud.contentwarehouse.v1.Rule\x12=\n\rmatched_rules\x18\x02 \x03(\x0b2&.google.cloud.contentwarehouse.v1.Rule\x12D\n\rinvalid_rules\x18\x03 \x03(\x0b2-.google.cloud.contentwarehouse.v1.InvalidRule"R\n\x0bInvalidRule\x124\n\x04rule\x18\x01 \x01(\x0b2&.google.cloud.contentwarehouse.v1.Rule\x12\r\n\x05error\x18\x02 \x01(\t"e\n\x14ActionExecutorOutput\x12M\n\x12rule_actions_pairs\x18\x01 \x03(\x0b21.google.cloud.contentwarehouse.v1.RuleActionsPair"\x8f\x01\n\x0fRuleActionsPair\x124\n\x04rule\x18\x01 \x01(\x0b2&.google.cloud.contentwarehouse.v1.Rule\x12F\n\x0eaction_outputs\x18\x02 \x03(\x0b2..google.cloud.contentwarehouse.v1.ActionOutput"\xee\x01\n\x0cActionOutput\x12\x11\n\taction_id\x18\x01 \x01(\t\x12J\n\x0caction_state\x18\x02 \x01(\x0e24.google.cloud.contentwarehouse.v1.ActionOutput.State\x12\x16\n\x0eoutput_message\x18\x03 \x01(\t"g\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10ACTION_SUCCEEDED\x10\x01\x12\x11\n\rACTION_FAILED\x10\x02\x12\x14\n\x10ACTION_TIMED_OUT\x10\x03\x12\x12\n\x0eACTION_PENDING\x10\x04B\xf7\x01\n$com.google.cloud.contentwarehouse.v1B\x0fRuleEngineProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.rule_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x0fRuleEngineProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_RULESET']._loaded_options = None
    _globals['_RULESET']._serialized_options = b"\xeaAf\n'contentwarehouse.googleapis.com/RuleSet\x12;projects/{project}/locations/{location}/ruleSets/{rule_set}"
    _globals['_DATAVALIDATIONACTION_CONDITIONSENTRY']._loaded_options = None
    _globals['_DATAVALIDATIONACTION_CONDITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_DATAUPDATEACTION_ENTRIESENTRY']._loaded_options = None
    _globals['_DATAUPDATEACTION_ENTRIESENTRY']._serialized_options = b'8\x01'
    _globals['_ADDTOFOLDERACTION'].fields_by_name['folders']._loaded_options = None
    _globals['_ADDTOFOLDERACTION'].fields_by_name['folders']._serialized_options = b'\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_REMOVEFROMFOLDERACTION'].fields_by_name['folder']._loaded_options = None
    _globals['_REMOVEFROMFOLDERACTION'].fields_by_name['folder']._serialized_options = b'\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_RULESET']._serialized_start = 177
    _globals['_RULESET']._serialized_end = 399
    _globals['_RULE']._serialized_start = 402
    _globals['_RULE']._serialized_end = 696
    _globals['_RULE_TRIGGERTYPE']._serialized_start = 600
    _globals['_RULE_TRIGGERTYPE']._serialized_end = 696
    _globals['_ACTION']._serialized_start = 699
    _globals['_ACTION']._serialized_end = 1317
    _globals['_ACCESSCONTROLACTION']._serialized_start = 1320
    _globals['_ACCESSCONTROLACTION']._serialized_end = 1582
    _globals['_ACCESSCONTROLACTION_OPERATIONTYPE']._serialized_start = 1475
    _globals['_ACCESSCONTROLACTION_OPERATIONTYPE']._serialized_end = 1582
    _globals['_DATAVALIDATIONACTION']._serialized_start = 1585
    _globals['_DATAVALIDATIONACTION']._serialized_end = 1750
    _globals['_DATAVALIDATIONACTION_CONDITIONSENTRY']._serialized_start = 1701
    _globals['_DATAVALIDATIONACTION_CONDITIONSENTRY']._serialized_end = 1750
    _globals['_DATAUPDATEACTION']._serialized_start = 1753
    _globals['_DATAUPDATEACTION']._serialized_end = 1901
    _globals['_DATAUPDATEACTION_ENTRIESENTRY']._serialized_start = 1855
    _globals['_DATAUPDATEACTION_ENTRIESENTRY']._serialized_end = 1901
    _globals['_ADDTOFOLDERACTION']._serialized_start = 1903
    _globals['_ADDTOFOLDERACTION']._serialized_end = 1986
    _globals['_REMOVEFROMFOLDERACTION']._serialized_start = 1988
    _globals['_REMOVEFROMFOLDERACTION']._serialized_end = 2094
    _globals['_PUBLISHACTION']._serialized_start = 2096
    _globals['_PUBLISHACTION']._serialized_end = 2147
    _globals['_DELETEDOCUMENTACTION']._serialized_start = 2149
    _globals['_DELETEDOCUMENTACTION']._serialized_end = 2199
    _globals['_RULEENGINEOUTPUT']._serialized_start = 2202
    _globals['_RULEENGINEOUTPUT']._serialized_end = 2417
    _globals['_RULEEVALUATOROUTPUT']._serialized_start = 2420
    _globals['_RULEEVALUATOROUTPUT']._serialized_end = 2639
    _globals['_INVALIDRULE']._serialized_start = 2641
    _globals['_INVALIDRULE']._serialized_end = 2723
    _globals['_ACTIONEXECUTOROUTPUT']._serialized_start = 2725
    _globals['_ACTIONEXECUTOROUTPUT']._serialized_end = 2826
    _globals['_RULEACTIONSPAIR']._serialized_start = 2829
    _globals['_RULEACTIONSPAIR']._serialized_end = 2972
    _globals['_ACTIONOUTPUT']._serialized_start = 2975
    _globals['_ACTIONOUTPUT']._serialized_end = 3213
    _globals['_ACTIONOUTPUT_STATE']._serialized_start = 3110
    _globals['_ACTIONOUTPUT_STATE']._serialized_end = 3213