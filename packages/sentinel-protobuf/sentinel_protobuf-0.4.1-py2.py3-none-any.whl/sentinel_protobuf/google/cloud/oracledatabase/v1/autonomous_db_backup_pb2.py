"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/oracledatabase/v1/autonomous_db_backup.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/oracledatabase/v1/autonomous_db_backup.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xda\x04\n\x18AutonomousDatabaseBackup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12U\n\x13autonomous_database\x18\x02 \x01(\tB8\xe0A\x02\xfaA2\n0oracledatabase.googleapis.com/AutonomousDatabase\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12[\n\nproperties\x18\x04 \x01(\x0b2B.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupPropertiesB\x03\xe0A\x01\x12Y\n\x06labels\x18\x05 \x03(\x0b2D.google.cloud.oracledatabase.v1.AutonomousDatabaseBackup.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xd1\x01\xeaA\xcd\x01\n6oracledatabase.googleapis.com/AutonomousDatabaseBackup\x12^projects/{project}/locations/{location}/autonomousDatabaseBackups/{autonomous_database_backup}*\x19autonomousDatabaseBackups2\x18autonomousDatabaseBackup"\xf2\x07\n"AutonomousDatabaseBackupProperties\x12\x11\n\x04ocid\x18\x01 \x01(\tB\x03\xe0A\x03\x12"\n\x15retention_period_days\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0ecompartment_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10database_size_tb\x18\x04 \x01(\x02B\x03\xe0A\x03\x12\x17\n\ndb_version\x18\x05 \x01(\tB\x03\xe0A\x03\x12 \n\x13is_long_term_backup\x18\x06 \x01(\x08B\x03\xe0A\x03\x12 \n\x13is_automatic_backup\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\ris_restorable\x18\x08 \x01(\x08B\x03\xe0A\x03\x12\x19\n\x0ckey_store_id\x18\t \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10key_store_wallet\x18\n \x01(\tB\x03\xe0A\x01\x12\x17\n\nkms_key_id\x18\x0b \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12kms_key_version_id\x18\x0c \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11lifecycle_details\x18\r \x01(\tB\x03\xe0A\x03\x12f\n\x0flifecycle_state\x18\x0e \x01(\x0e2H.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.StateB\x03\xe0A\x03\x12\x14\n\x07size_tb\x18\x0f \x01(\x02B\x03\xe0A\x03\x12<\n\x13available_till_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Z\n\x04type\x18\x13 \x01(\x0e2G.google.cloud.oracledatabase.v1.AutonomousDatabaseBackupProperties.TypeB\x03\xe0A\x03\x12\x15\n\x08vault_id\x18\x14 \x01(\tB\x03\xe0A\x01"m\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0b\n\x07DELETED\x10\x04\x12\n\n\x06FAILED\x10\x06\x12\x0c\n\x08UPDATING\x10\x07"F\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02\x12\r\n\tLONG_TERM\x10\x03B\xf1\x01\n"com.google.cloud.oracledatabase.v1B\x17AutonomousDbBackupProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.autonomous_db_backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x17AutonomousDbBackupProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_AUTONOMOUSDATABASEBACKUP_LABELSENTRY']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['name']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['autonomous_database']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['autonomous_database']._serialized_options = b'\xe0A\x02\xfaA2\n0oracledatabase.googleapis.com/AutonomousDatabase'
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['display_name']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['properties']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['labels']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUP']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUP']._serialized_options = b'\xeaA\xcd\x01\n6oracledatabase.googleapis.com/AutonomousDatabaseBackup\x12^projects/{project}/locations/{location}/autonomousDatabaseBackups/{autonomous_database_backup}*\x19autonomousDatabaseBackups2\x18autonomousDatabaseBackup'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['ocid']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['ocid']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['retention_period_days']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['retention_period_days']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['compartment_id']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['compartment_id']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['database_size_tb']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['database_size_tb']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['db_version']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['db_version']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_long_term_backup']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_long_term_backup']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_automatic_backup']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_automatic_backup']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_restorable']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['is_restorable']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['key_store_id']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['key_store_id']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['key_store_wallet']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['key_store_wallet']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['kms_key_id']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['kms_key_id']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['kms_key_version_id']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['kms_key_version_id']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['lifecycle_details']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['lifecycle_details']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['lifecycle_state']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['lifecycle_state']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['size_tb']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['size_tb']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['available_till_time']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['available_till_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['end_time']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['start_time']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['type']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['vault_id']._loaded_options = None
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES'].fields_by_name['vault_id']._serialized_options = b'\xe0A\x01'
    _globals['_AUTONOMOUSDATABASEBACKUP']._serialized_start = 187
    _globals['_AUTONOMOUSDATABASEBACKUP']._serialized_end = 789
    _globals['_AUTONOMOUSDATABASEBACKUP_LABELSENTRY']._serialized_start = 532
    _globals['_AUTONOMOUSDATABASEBACKUP_LABELSENTRY']._serialized_end = 577
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES']._serialized_start = 792
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES']._serialized_end = 1802
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES_STATE']._serialized_start = 1621
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES_STATE']._serialized_end = 1730
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES_TYPE']._serialized_start = 1732
    _globals['_AUTONOMOUSDATABASEBACKUPPROPERTIES_TYPE']._serialized_end = 1802