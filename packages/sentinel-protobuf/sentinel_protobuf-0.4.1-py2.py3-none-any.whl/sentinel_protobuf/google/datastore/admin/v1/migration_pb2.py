"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/admin/v1/migration.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/datastore/admin/v1/migration.proto\x12\x19google.datastore.admin.v1"O\n\x13MigrationStateEvent\x128\n\x05state\x18\x01 \x01(\x0e2).google.datastore.admin.v1.MigrationState"\xa1\x05\n\x16MigrationProgressEvent\x126\n\x04step\x18\x01 \x01(\x0e2(.google.datastore.admin.v1.MigrationStep\x12d\n\x14prepare_step_details\x18\x02 \x01(\x0b2D.google.datastore.admin.v1.MigrationProgressEvent.PrepareStepDetailsH\x00\x12s\n\x1credirect_writes_step_details\x18\x03 \x01(\x0b2K.google.datastore.admin.v1.MigrationProgressEvent.RedirectWritesStepDetailsH\x00\x1aq\n\x12PrepareStepDetails\x12[\n\x10concurrency_mode\x18\x01 \x01(\x0e2A.google.datastore.admin.v1.MigrationProgressEvent.ConcurrencyMode\x1ax\n\x19RedirectWritesStepDetails\x12[\n\x10concurrency_mode\x18\x01 \x01(\x0e2A.google.datastore.admin.v1.MigrationProgressEvent.ConcurrencyMode"w\n\x0fConcurrencyMode\x12 \n\x1cCONCURRENCY_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPESSIMISTIC\x10\x01\x12\x0e\n\nOPTIMISTIC\x10\x02\x12!\n\x1dOPTIMISTIC_WITH_ENTITY_GROUPS\x10\x03B\x0e\n\x0cstep_details*X\n\x0eMigrationState\x12\x1f\n\x1bMIGRATION_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08COMPLETE\x10\x03*\xe3\x01\n\rMigrationStep\x12\x1e\n\x1aMIGRATION_STEP_UNSPECIFIED\x10\x00\x12\x0b\n\x07PREPARE\x10\x06\x12\t\n\x05START\x10\x01\x12\x1e\n\x1aAPPLY_WRITES_SYNCHRONOUSLY\x10\x07\x12\x13\n\x0fCOPY_AND_VERIFY\x10\x02\x12(\n$REDIRECT_EVENTUALLY_CONSISTENT_READS\x10\x03\x12&\n"REDIRECT_STRONGLY_CONSISTENT_READS\x10\x04\x12\x13\n\x0fREDIRECT_WRITES\x10\x05B\xd6\x01\n\x1dcom.google.datastore.admin.v1B\x0eMigrationProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.admin.v1.migration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.datastore.admin.v1B\x0eMigrationProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1'
    _globals['_MIGRATIONSTATE']._serialized_start = 829
    _globals['_MIGRATIONSTATE']._serialized_end = 917
    _globals['_MIGRATIONSTEP']._serialized_start = 920
    _globals['_MIGRATIONSTEP']._serialized_end = 1147
    _globals['_MIGRATIONSTATEEVENT']._serialized_start = 72
    _globals['_MIGRATIONSTATEEVENT']._serialized_end = 151
    _globals['_MIGRATIONPROGRESSEVENT']._serialized_start = 154
    _globals['_MIGRATIONPROGRESSEVENT']._serialized_end = 827
    _globals['_MIGRATIONPROGRESSEVENT_PREPARESTEPDETAILS']._serialized_start = 455
    _globals['_MIGRATIONPROGRESSEVENT_PREPARESTEPDETAILS']._serialized_end = 568
    _globals['_MIGRATIONPROGRESSEVENT_REDIRECTWRITESSTEPDETAILS']._serialized_start = 570
    _globals['_MIGRATIONPROGRESSEVENT_REDIRECTWRITESSTEPDETAILS']._serialized_end = 690
    _globals['_MIGRATIONPROGRESSEVENT_CONCURRENCYMODE']._serialized_start = 692
    _globals['_MIGRATIONPROGRESSEVENT_CONCURRENCYMODE']._serialized_end = 811