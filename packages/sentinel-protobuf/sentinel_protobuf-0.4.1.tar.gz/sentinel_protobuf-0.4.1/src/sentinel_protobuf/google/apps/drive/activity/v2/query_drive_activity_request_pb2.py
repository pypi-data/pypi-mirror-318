"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/activity/v2/query_drive_activity_request.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/apps/drive/activity/v2/query_drive_activity_request.proto\x12\x1dgoogle.apps.drive.activity.v2"\xdd\x01\n\x19QueryDriveActivityRequest\x12\x13\n\titem_name\x18\x01 \x01(\tH\x00\x12\x17\n\rancestor_name\x18\x02 \x01(\tH\x00\x12T\n\x16consolidation_strategy\x18\x05 \x01(\x0b24.google.apps.drive.activity.v2.ConsolidationStrategy\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x0e\n\x06filter\x18\x08 \x01(\tB\x05\n\x03key"\xe5\x01\n\x15ConsolidationStrategy\x12T\n\x04none\x18\x01 \x01(\x0b2D.google.apps.drive.activity.v2.ConsolidationStrategy.NoConsolidationH\x00\x12M\n\x06legacy\x18\x02 \x01(\x0b2;.google.apps.drive.activity.v2.ConsolidationStrategy.LegacyH\x00\x1a\x11\n\x0fNoConsolidation\x1a\x08\n\x06LegacyB\n\n\x08strategyB\xd3\x01\n!com.google.apps.drive.activity.v2B\x1eQueryDriveActivityRequestProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.query_drive_activity_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x1eQueryDriveActivityRequestProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_QUERYDRIVEACTIVITYREQUEST']._serialized_start = 100
    _globals['_QUERYDRIVEACTIVITYREQUEST']._serialized_end = 321
    _globals['_CONSOLIDATIONSTRATEGY']._serialized_start = 324
    _globals['_CONSOLIDATIONSTRATEGY']._serialized_end = 553
    _globals['_CONSOLIDATIONSTRATEGY_NOCONSOLIDATION']._serialized_start = 514
    _globals['_CONSOLIDATIONSTRATEGY_NOCONSOLIDATION']._serialized_end = 531
    _globals['_CONSOLIDATIONSTRATEGY_LEGACY']._serialized_start = 533
    _globals['_CONSOLIDATIONSTRATEGY_LEGACY']._serialized_end = 541