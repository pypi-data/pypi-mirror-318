"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/activity/v2/target.proto')
_sym_db = _symbol_database.Default()
from ......google.apps.drive.activity.v2 import actor_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_actor__pb2
from ......google.apps.drive.activity.v2 import common_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/apps/drive/activity/v2/target.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a)google/apps/drive/activity/v2/actor.proto\x1a*google/apps/drive/activity/v2/common.proto"\x8f\x02\n\x06Target\x12>\n\ndrive_item\x18\x01 \x01(\x0b2(.google.apps.drive.activity.v2.DriveItemH\x00\x125\n\x05drive\x18\x05 \x01(\x0b2$.google.apps.drive.activity.v2.DriveH\x00\x12B\n\x0cfile_comment\x18\x03 \x01(\x0b2*.google.apps.drive.activity.v2.FileCommentH\x00\x12@\n\nteam_drive\x18\x02 \x01(\x0b2(.google.apps.drive.activity.v2.TeamDriveB\x02\x18\x01B\x08\n\x06object"\xef\x01\n\x0fTargetReference\x12G\n\ndrive_item\x18\x01 \x01(\x0b21.google.apps.drive.activity.v2.DriveItemReferenceH\x00\x12>\n\x05drive\x18\x03 \x01(\x0b2-.google.apps.drive.activity.v2.DriveReferenceH\x00\x12I\n\nteam_drive\x18\x02 \x01(\x0b21.google.apps.drive.activity.v2.TeamDriveReferenceB\x02\x18\x01B\x08\n\x06object"\x9c\x01\n\x0bFileComment\x12\x19\n\x11legacy_comment_id\x18\x01 \x01(\t\x12\x1c\n\x14legacy_discussion_id\x18\x02 \x01(\t\x12\x1a\n\x12link_to_discussion\x18\x03 \x01(\t\x128\n\x06parent\x18\x04 \x01(\x0b2(.google.apps.drive.activity.v2.DriveItem"\x9c\x06\n\tDriveItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12?\n\x04file\x18\x03 \x01(\x0b2-.google.apps.drive.activity.v2.DriveItem.FileB\x02\x18\x01\x12C\n\x06folder\x18\x04 \x01(\x0b2/.google.apps.drive.activity.v2.DriveItem.FolderB\x02\x18\x01\x12H\n\ndrive_file\x18\x08 \x01(\x0b22.google.apps.drive.activity.v2.DriveItem.DriveFileH\x00\x12L\n\x0cdrive_folder\x18\t \x01(\x0b24.google.apps.drive.activity.v2.DriveItem.DriveFolderH\x00\x12\x11\n\tmime_type\x18\x06 \x01(\t\x123\n\x05owner\x18\x07 \x01(\x0b2$.google.apps.drive.activity.v2.Owner\x1a\n\n\x04File:\x02\x18\x01\x1a\xaf\x01\n\x06Folder\x12B\n\x04type\x18\x06 \x01(\x0e24.google.apps.drive.activity.v2.DriveItem.Folder.Type"]\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMY_DRIVE_ROOT\x10\x01\x12\x13\n\x0fTEAM_DRIVE_ROOT\x10\x02\x12\x13\n\x0fSTANDARD_FOLDER\x10\x03\x1a\x02\x18\x01:\x02\x18\x01\x1a\x0b\n\tDriveFile\x1a\xb3\x01\n\x0bDriveFolder\x12G\n\x04type\x18\x06 \x01(\x0e29.google.apps.drive.activity.v2.DriveItem.DriveFolder.Type"[\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMY_DRIVE_ROOT\x10\x01\x12\x15\n\x11SHARED_DRIVE_ROOT\x10\x02\x12\x13\n\x0fSTANDARD_FOLDER\x10\x03B\x0b\n\titem_type"\x87\x02\n\x05Owner\x123\n\x04user\x18\x01 \x01(\x0b2#.google.apps.drive.activity.v2.UserH\x00\x12>\n\x05drive\x18\x04 \x01(\x0b2-.google.apps.drive.activity.v2.DriveReferenceH\x00\x12I\n\nteam_drive\x18\x02 \x01(\x0b21.google.apps.drive.activity.v2.TeamDriveReferenceB\x02\x18\x01\x125\n\x06domain\x18\x03 \x01(\x0b2%.google.apps.drive.activity.v2.DomainB\x07\n\x05owner"d\n\tTeamDrive\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x126\n\x04root\x18\x03 \x01(\x0b2(.google.apps.drive.activity.v2.DriveItem:\x02\x18\x01"\\\n\x05Drive\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x126\n\x04root\x18\x03 \x01(\x0b2(.google.apps.drive.activity.v2.DriveItem"\xdc\x02\n\x12DriveItemReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12?\n\x04file\x18\x03 \x01(\x0b2-.google.apps.drive.activity.v2.DriveItem.FileB\x02\x18\x01\x12C\n\x06folder\x18\x04 \x01(\x0b2/.google.apps.drive.activity.v2.DriveItem.FolderB\x02\x18\x01\x12H\n\ndrive_file\x18\x08 \x01(\x0b22.google.apps.drive.activity.v2.DriveItem.DriveFileH\x00\x12L\n\x0cdrive_folder\x18\t \x01(\x0b24.google.apps.drive.activity.v2.DriveItem.DriveFolderH\x00B\x0b\n\titem_type"5\n\x12TeamDriveReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t:\x02\x18\x01"-\n\x0eDriveReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\tB\xc0\x01\n!com.google.apps.drive.activity.v2B\x0bTargetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x0bTargetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_TARGET'].fields_by_name['team_drive']._loaded_options = None
    _globals['_TARGET'].fields_by_name['team_drive']._serialized_options = b'\x18\x01'
    _globals['_TARGETREFERENCE'].fields_by_name['team_drive']._loaded_options = None
    _globals['_TARGETREFERENCE'].fields_by_name['team_drive']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEM_FILE']._loaded_options = None
    _globals['_DRIVEITEM_FILE']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEM_FOLDER_TYPE']._loaded_options = None
    _globals['_DRIVEITEM_FOLDER_TYPE']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEM_FOLDER']._loaded_options = None
    _globals['_DRIVEITEM_FOLDER']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEM'].fields_by_name['file']._loaded_options = None
    _globals['_DRIVEITEM'].fields_by_name['file']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEM'].fields_by_name['folder']._loaded_options = None
    _globals['_DRIVEITEM'].fields_by_name['folder']._serialized_options = b'\x18\x01'
    _globals['_OWNER'].fields_by_name['team_drive']._loaded_options = None
    _globals['_OWNER'].fields_by_name['team_drive']._serialized_options = b'\x18\x01'
    _globals['_TEAMDRIVE']._loaded_options = None
    _globals['_TEAMDRIVE']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEMREFERENCE'].fields_by_name['file']._loaded_options = None
    _globals['_DRIVEITEMREFERENCE'].fields_by_name['file']._serialized_options = b'\x18\x01'
    _globals['_DRIVEITEMREFERENCE'].fields_by_name['folder']._loaded_options = None
    _globals['_DRIVEITEMREFERENCE'].fields_by_name['folder']._serialized_options = b'\x18\x01'
    _globals['_TEAMDRIVEREFERENCE']._loaded_options = None
    _globals['_TEAMDRIVEREFERENCE']._serialized_options = b'\x18\x01'
    _globals['_TARGET']._serialized_start = 165
    _globals['_TARGET']._serialized_end = 436
    _globals['_TARGETREFERENCE']._serialized_start = 439
    _globals['_TARGETREFERENCE']._serialized_end = 678
    _globals['_FILECOMMENT']._serialized_start = 681
    _globals['_FILECOMMENT']._serialized_end = 837
    _globals['_DRIVEITEM']._serialized_start = 840
    _globals['_DRIVEITEM']._serialized_end = 1636
    _globals['_DRIVEITEM_FILE']._serialized_start = 1240
    _globals['_DRIVEITEM_FILE']._serialized_end = 1250
    _globals['_DRIVEITEM_FOLDER']._serialized_start = 1253
    _globals['_DRIVEITEM_FOLDER']._serialized_end = 1428
    _globals['_DRIVEITEM_FOLDER_TYPE']._serialized_start = 1331
    _globals['_DRIVEITEM_FOLDER_TYPE']._serialized_end = 1424
    _globals['_DRIVEITEM_DRIVEFILE']._serialized_start = 1430
    _globals['_DRIVEITEM_DRIVEFILE']._serialized_end = 1441
    _globals['_DRIVEITEM_DRIVEFOLDER']._serialized_start = 1444
    _globals['_DRIVEITEM_DRIVEFOLDER']._serialized_end = 1623
    _globals['_DRIVEITEM_DRIVEFOLDER_TYPE']._serialized_start = 1532
    _globals['_DRIVEITEM_DRIVEFOLDER_TYPE']._serialized_end = 1623
    _globals['_OWNER']._serialized_start = 1639
    _globals['_OWNER']._serialized_end = 1902
    _globals['_TEAMDRIVE']._serialized_start = 1904
    _globals['_TEAMDRIVE']._serialized_end = 2004
    _globals['_DRIVE']._serialized_start = 2006
    _globals['_DRIVE']._serialized_end = 2098
    _globals['_DRIVEITEMREFERENCE']._serialized_start = 2101
    _globals['_DRIVEITEMREFERENCE']._serialized_end = 2449
    _globals['_TEAMDRIVEREFERENCE']._serialized_start = 2451
    _globals['_TEAMDRIVEREFERENCE']._serialized_end = 2504
    _globals['_DRIVEREFERENCE']._serialized_start = 2506
    _globals['_DRIVEREFERENCE']._serialized_end = 2551