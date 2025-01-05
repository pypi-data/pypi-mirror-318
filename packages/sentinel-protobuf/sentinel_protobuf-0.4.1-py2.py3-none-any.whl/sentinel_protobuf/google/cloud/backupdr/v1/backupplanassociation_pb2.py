"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/backupdr/v1/backupplanassociation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/backupdr/v1/backupplanassociation.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xd4\x05\n\x15BackupPlanAssociation\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x03\x12\x1a\n\rresource_type\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x08resource\x18\x03 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12?\n\x0bbackup_plan\x18\x04 \x01(\tB*\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x05state\x18\x07 \x01(\x0e25.google.cloud.backupdr.v1.BackupPlanAssociation.StateB\x03\xe0A\x03\x12H\n\x11rules_config_info\x18\x08 \x03(\x0b2(.google.cloud.backupdr.v1.RuleConfigInfoB\x03\xe0A\x03\x12\x18\n\x0bdata_source\x18\t \x01(\tB\x03\xe0A\x03"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08INACTIVE\x10\x04:\xbc\x01\xeaA\xb8\x01\n-backupdr.googleapis.com/BackupPlanAssociation\x12Xprojects/{project}/locations/{location}/backupPlanAssociations/{backup_plan_association}*\x16backupPlanAssociations2\x15backupPlanAssociation"\x89\x03\n\x0eRuleConfigInfo\x12\x14\n\x07rule_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12X\n\x11last_backup_state\x18\x03 \x01(\x0e28.google.cloud.backupdr.v1.RuleConfigInfo.LastBackupStateB\x03\xe0A\x03\x122\n\x11last_backup_error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12P\n\'last_successful_backup_consistency_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x80\x01\n\x0fLastBackupState\x12!\n\x1dLAST_BACKUP_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14FIRST_BACKUP_PENDING\x10\x01\x12\x15\n\x11PERMISSION_DENIED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04"\x8c\x02\n"CreateBackupPlanAssociationRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-backupdr.googleapis.com/BackupPlanAssociation\x12\'\n\x1abackup_plan_association_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12U\n\x17backup_plan_association\x18\x03 \x01(\x0b2/.google.cloud.backupdr.v1.BackupPlanAssociationB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xb0\x01\n!ListBackupPlanAssociationsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-backupdr.googleapis.com/BackupPlanAssociation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\xa5\x01\n"ListBackupPlanAssociationsResponse\x12Q\n\x18backup_plan_associations\x18\x01 \x03(\x0b2/.google.cloud.backupdr.v1.BackupPlanAssociation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"f\n\x1fGetBackupPlanAssociationRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation"\x8a\x01\n"DeleteBackupPlanAssociationRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x92\x01\n\x14TriggerBackupRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation\x12\x14\n\x07rule_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01B\xca\x01\n\x1ccom.google.cloud.backupdr.v1B\x1aBackupPlanAssociationProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupplanassociation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\x1aBackupPlanAssociationProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['resource_type']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['resource']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['resource']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['backup_plan']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['backup_plan']._serialized_options = b'\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['rules_config_info']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['rules_config_info']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['data_source']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANASSOCIATION']._loaded_options = None
    _globals['_BACKUPPLANASSOCIATION']._serialized_options = b'\xeaA\xb8\x01\n-backupdr.googleapis.com/BackupPlanAssociation\x12Xprojects/{project}/locations/{location}/backupPlanAssociations/{backup_plan_association}*\x16backupPlanAssociations2\x15backupPlanAssociation'
    _globals['_RULECONFIGINFO'].fields_by_name['rule_id']._loaded_options = None
    _globals['_RULECONFIGINFO'].fields_by_name['rule_id']._serialized_options = b'\xe0A\x03'
    _globals['_RULECONFIGINFO'].fields_by_name['last_backup_state']._loaded_options = None
    _globals['_RULECONFIGINFO'].fields_by_name['last_backup_state']._serialized_options = b'\xe0A\x03'
    _globals['_RULECONFIGINFO'].fields_by_name['last_backup_error']._loaded_options = None
    _globals['_RULECONFIGINFO'].fields_by_name['last_backup_error']._serialized_options = b'\xe0A\x03'
    _globals['_RULECONFIGINFO'].fields_by_name['last_successful_backup_consistency_time']._loaded_options = None
    _globals['_RULECONFIGINFO'].fields_by_name['last_successful_backup_consistency_time']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-backupdr.googleapis.com/BackupPlanAssociation'
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['backup_plan_association_id']._loaded_options = None
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['backup_plan_association_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['backup_plan_association']._loaded_options = None
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['backup_plan_association']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-backupdr.googleapis.com/BackupPlanAssociation'
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation'
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation'
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-backupdr.googleapis.com/BackupPlanAssociation'
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['rule_id']._loaded_options = None
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['rule_id']._serialized_options = b'\xe0A\x02'
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_TRIGGERBACKUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_BACKUPPLANASSOCIATION']._serialized_start = 230
    _globals['_BACKUPPLANASSOCIATION']._serialized_end = 954
    _globals['_BACKUPPLANASSOCIATION_STATE']._serialized_start = 679
    _globals['_BACKUPPLANASSOCIATION_STATE']._serialized_end = 763
    _globals['_RULECONFIGINFO']._serialized_start = 957
    _globals['_RULECONFIGINFO']._serialized_end = 1350
    _globals['_RULECONFIGINFO_LASTBACKUPSTATE']._serialized_start = 1222
    _globals['_RULECONFIGINFO_LASTBACKUPSTATE']._serialized_end = 1350
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST']._serialized_start = 1353
    _globals['_CREATEBACKUPPLANASSOCIATIONREQUEST']._serialized_end = 1621
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST']._serialized_start = 1624
    _globals['_LISTBACKUPPLANASSOCIATIONSREQUEST']._serialized_end = 1800
    _globals['_LISTBACKUPPLANASSOCIATIONSRESPONSE']._serialized_start = 1803
    _globals['_LISTBACKUPPLANASSOCIATIONSRESPONSE']._serialized_end = 1968
    _globals['_GETBACKUPPLANASSOCIATIONREQUEST']._serialized_start = 1970
    _globals['_GETBACKUPPLANASSOCIATIONREQUEST']._serialized_end = 2072
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST']._serialized_start = 2075
    _globals['_DELETEBACKUPPLANASSOCIATIONREQUEST']._serialized_end = 2213
    _globals['_TRIGGERBACKUPREQUEST']._serialized_start = 2216
    _globals['_TRIGGERBACKUPREQUEST']._serialized_end = 2362