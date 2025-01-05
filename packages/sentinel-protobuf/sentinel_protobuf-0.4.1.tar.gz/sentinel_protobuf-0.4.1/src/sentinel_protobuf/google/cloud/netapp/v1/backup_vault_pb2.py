"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/netapp/v1/backup_vault.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/netapp/v1/backup_vault.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x84\x04\n\x0bBackupVault\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12=\n\x05state\x18\x02 \x01(\x0e2).google.cloud.netapp.v1.BackupVault.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12?\n\x06labels\x18\x05 \x03(\x0b2/.google.cloud.netapp.v1.BackupVault.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05ERROR\x10\x04\x12\x0c\n\x08UPDATING\x10\x05:\x87\x01\xeaA\x83\x01\n!netapp.googleapis.com/BackupVault\x12Cprojects/{project}/locations/{location}/backupVaults/{backup_vault}*\x0cbackupVaults2\x0bbackupVault"P\n\x15GetBackupVaultRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault"\x9d\x01\n\x17ListBackupVaultsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"\x84\x01\n\x18ListBackupVaultsResponse\x12:\n\rbackup_vaults\x18\x01 \x03(\x0b2#.google.cloud.netapp.v1.BackupVault\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xb3\x01\n\x18CreateBackupVaultRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault\x12\x1c\n\x0fbackup_vault_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x0cbackup_vault\x18\x03 \x01(\x0b2#.google.cloud.netapp.v1.BackupVaultB\x03\xe0A\x02"S\n\x18DeleteBackupVaultRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault"\x90\x01\n\x18UpdateBackupVaultRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x0cbackup_vault\x18\x02 \x01(\x0b2#.google.cloud.netapp.v1.BackupVaultB\x03\xe0A\x02B\xb2\x01\n\x1acom.google.cloud.netapp.v1B\x10BackupVaultProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.backup_vault_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x10BackupVaultProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_BACKUPVAULT_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPVAULT'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPVAULT'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPVAULT'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPVAULT']._loaded_options = None
    _globals['_BACKUPVAULT']._serialized_options = b'\xeaA\x83\x01\n!netapp.googleapis.com/BackupVault\x12Cprojects/{project}/locations/{location}/backupVaults/{backup_vault}*\x0cbackupVaults2\x0bbackupVault'
    _globals['_GETBACKUPVAULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPVAULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_LISTBACKUPVAULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPVAULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault_id']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBACKUPVAULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPVAULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._loaded_options = None
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPVAULT']._serialized_start = 197
    _globals['_BACKUPVAULT']._serialized_end = 713
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_start = 434
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_end = 479
    _globals['_BACKUPVAULT_STATE']._serialized_start = 481
    _globals['_BACKUPVAULT_STATE']._serialized_end = 575
    _globals['_GETBACKUPVAULTREQUEST']._serialized_start = 715
    _globals['_GETBACKUPVAULTREQUEST']._serialized_end = 795
    _globals['_LISTBACKUPVAULTSREQUEST']._serialized_start = 798
    _globals['_LISTBACKUPVAULTSREQUEST']._serialized_end = 955
    _globals['_LISTBACKUPVAULTSRESPONSE']._serialized_start = 958
    _globals['_LISTBACKUPVAULTSRESPONSE']._serialized_end = 1090
    _globals['_CREATEBACKUPVAULTREQUEST']._serialized_start = 1093
    _globals['_CREATEBACKUPVAULTREQUEST']._serialized_end = 1272
    _globals['_DELETEBACKUPVAULTREQUEST']._serialized_start = 1274
    _globals['_DELETEBACKUPVAULTREQUEST']._serialized_end = 1357
    _globals['_UPDATEBACKUPVAULTREQUEST']._serialized_start = 1360
    _globals['_UPDATEBACKUPVAULTREQUEST']._serialized_end = 1504