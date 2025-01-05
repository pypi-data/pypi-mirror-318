"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/activity/v2/actor.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/apps/drive/activity/v2/actor.proto\x12\x1dgoogle.apps.drive.activity.v2"\xd3\x02\n\x05Actor\x123\n\x04user\x18\x01 \x01(\x0b2#.google.apps.drive.activity.v2.UserH\x00\x12A\n\tanonymous\x18\x02 \x01(\x0b2,.google.apps.drive.activity.v2.AnonymousUserH\x00\x12E\n\rimpersonation\x18\x03 \x01(\x0b2,.google.apps.drive.activity.v2.ImpersonationH\x00\x12<\n\x06system\x18\x04 \x01(\x0b2*.google.apps.drive.activity.v2.SystemEventH\x00\x12E\n\radministrator\x18\x05 \x01(\x0b2,.google.apps.drive.activity.v2.AdministratorH\x00B\x06\n\x04type"\xbe\x02\n\x04User\x12C\n\nknown_user\x18\x02 \x01(\x0b2-.google.apps.drive.activity.v2.User.KnownUserH\x00\x12G\n\x0cdeleted_user\x18\x03 \x01(\x0b2/.google.apps.drive.activity.v2.User.DeletedUserH\x00\x12G\n\x0cunknown_user\x18\x04 \x01(\x0b2/.google.apps.drive.activity.v2.User.UnknownUserH\x00\x1a9\n\tKnownUser\x12\x13\n\x0bperson_name\x18\x01 \x01(\t\x12\x17\n\x0fis_current_user\x18\x02 \x01(\x08\x1a\r\n\x0bDeletedUser\x1a\r\n\x0bUnknownUserB\x06\n\x04type"\x0f\n\rAnonymousUser"O\n\rImpersonation\x12>\n\x11impersonated_user\x18\x01 \x01(\x0b2#.google.apps.drive.activity.v2.User"\x93\x01\n\x0bSystemEvent\x12=\n\x04type\x18\x01 \x01(\x0e2/.google.apps.drive.activity.v2.SystemEvent.Type"E\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rUSER_DELETION\x10\x01\x12\x14\n\x10TRASH_AUTO_PURGE\x10\x02"\x0f\n\rAdministratorB\xbf\x01\n!com.google.apps.drive.activity.v2B\nActorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.actor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\nActorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_ACTOR']._serialized_start = 77
    _globals['_ACTOR']._serialized_end = 416
    _globals['_USER']._serialized_start = 419
    _globals['_USER']._serialized_end = 737
    _globals['_USER_KNOWNUSER']._serialized_start = 642
    _globals['_USER_KNOWNUSER']._serialized_end = 699
    _globals['_USER_DELETEDUSER']._serialized_start = 701
    _globals['_USER_DELETEDUSER']._serialized_end = 714
    _globals['_USER_UNKNOWNUSER']._serialized_start = 716
    _globals['_USER_UNKNOWNUSER']._serialized_end = 729
    _globals['_ANONYMOUSUSER']._serialized_start = 739
    _globals['_ANONYMOUSUSER']._serialized_end = 754
    _globals['_IMPERSONATION']._serialized_start = 756
    _globals['_IMPERSONATION']._serialized_end = 835
    _globals['_SYSTEMEVENT']._serialized_start = 838
    _globals['_SYSTEMEVENT']._serialized_end = 985
    _globals['_SYSTEMEVENT_TYPE']._serialized_start = 916
    _globals['_SYSTEMEVENT_TYPE']._serialized_end = 985
    _globals['_ADMINISTRATOR']._serialized_start = 987
    _globals['_ADMINISTRATOR']._serialized_end = 1002