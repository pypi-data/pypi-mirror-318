"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/membership.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.chat.v1 import group_pb2 as google_dot_chat_dot_v1_dot_group__pb2
from ....google.chat.v1 import user_pb2 as google_dot_chat_dot_v1_dot_user__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/chat/v1/membership.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1agoogle/chat/v1/group.proto\x1a\x19google/chat/v1/user.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfa\x04\n\nMembership\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12>\n\x05state\x18\x02 \x01(\x0e2*.google.chat.v1.Membership.MembershipStateB\x03\xe0A\x03\x12<\n\x04role\x18\x07 \x01(\x0e2).google.chat.v1.Membership.MembershipRoleB\x03\xe0A\x01\x12+\n\x06member\x18\x03 \x01(\x0b2\x14.google.chat.v1.UserB\x03\xe0A\x01H\x00\x122\n\x0cgroup_member\x18\x05 \x01(\x0b2\x15.google.chat.v1.GroupB\x03\xe0A\x01H\x00\x127\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x05\xe0A\x01\x127\n\x0bdelete_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x05\xe0A\x01"^\n\x0fMembershipState\x12 \n\x1cMEMBERSHIP_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06JOINED\x10\x01\x12\x0b\n\x07INVITED\x10\x02\x12\x10\n\x0cNOT_A_MEMBER\x10\x03"T\n\x0eMembershipRole\x12\x1f\n\x1bMEMBERSHIP_ROLE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bROLE_MEMBER\x10\x01\x12\x10\n\x0cROLE_MANAGER\x10\x02:D\xeaAA\n\x1echat.googleapis.com/Membership\x12\x1fspaces/{space}/members/{member}B\x0c\n\nmemberType"\xa5\x01\n\x17CreateMembershipRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1echat.googleapis.com/Membership\x123\n\nmembership\x18\x02 \x01(\x0b2\x1a.google.chat.v1.MembershipB\x03\xe0A\x02\x12\x1d\n\x10use_admin_access\x18\x05 \x01(\x08B\x03\xe0A\x01"\xa3\x01\n\x17UpdateMembershipRequest\x123\n\nmembership\x18\x01 \x01(\x0b2\x1a.google.chat.v1.MembershipB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x1d\n\x10use_admin_access\x18\x03 \x01(\x08B\x03\xe0A\x01"\xea\x01\n\x16ListMembershipsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1echat.googleapis.com/Membership\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bshow_groups\x18\x06 \x01(\x08B\x03\xe0A\x01\x12\x19\n\x0cshow_invited\x18\x07 \x01(\x08B\x03\xe0A\x01\x12\x1d\n\x10use_admin_access\x18\x08 \x01(\x08B\x03\xe0A\x01"h\n\x17ListMembershipsResponse\x124\n\x0bmemberships\x18\x01 \x03(\x0b2\x1a.google.chat.v1.MembershipB\x03\xe0A\x06\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"k\n\x14GetMembershipRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1echat.googleapis.com/Membership\x12\x1d\n\x10use_admin_access\x18\x03 \x01(\x08B\x03\xe0A\x01"n\n\x17DeleteMembershipRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1echat.googleapis.com/Membership\x12\x1d\n\x10use_admin_access\x18\x02 \x01(\x08B\x03\xe0A\x01B\xa8\x01\n\x12com.google.chat.v1B\x0fMembershipProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.membership_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0fMembershipProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_MEMBERSHIP'].fields_by_name['name']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MEMBERSHIP'].fields_by_name['state']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['role']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['role']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['member']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['member']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['group_member']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['group_member']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['create_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['delete_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_MEMBERSHIP']._loaded_options = None
    _globals['_MEMBERSHIP']._serialized_options = b'\xeaAA\n\x1echat.googleapis.com/Membership\x12\x1fspaces/{space}/members/{member}'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1echat.googleapis.com/Membership'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['membership']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['membership']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['membership']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['membership']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1echat.googleapis.com/Membership'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['show_groups']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['show_groups']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['show_invited']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['show_invited']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['use_admin_access']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['use_admin_access']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSRESPONSE'].fields_by_name['memberships']._loaded_options = None
    _globals['_LISTMEMBERSHIPSRESPONSE'].fields_by_name['memberships']._serialized_options = b'\xe0A\x06'
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1echat.googleapis.com/Membership'
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._loaded_options = None
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1echat.googleapis.com/Membership'
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._loaded_options = None
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['use_admin_access']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP']._serialized_start = 234
    _globals['_MEMBERSHIP']._serialized_end = 868
    _globals['_MEMBERSHIP_MEMBERSHIPSTATE']._serialized_start = 604
    _globals['_MEMBERSHIP_MEMBERSHIPSTATE']._serialized_end = 698
    _globals['_MEMBERSHIP_MEMBERSHIPROLE']._serialized_start = 700
    _globals['_MEMBERSHIP_MEMBERSHIPROLE']._serialized_end = 784
    _globals['_CREATEMEMBERSHIPREQUEST']._serialized_start = 871
    _globals['_CREATEMEMBERSHIPREQUEST']._serialized_end = 1036
    _globals['_UPDATEMEMBERSHIPREQUEST']._serialized_start = 1039
    _globals['_UPDATEMEMBERSHIPREQUEST']._serialized_end = 1202
    _globals['_LISTMEMBERSHIPSREQUEST']._serialized_start = 1205
    _globals['_LISTMEMBERSHIPSREQUEST']._serialized_end = 1439
    _globals['_LISTMEMBERSHIPSRESPONSE']._serialized_start = 1441
    _globals['_LISTMEMBERSHIPSRESPONSE']._serialized_end = 1545
    _globals['_GETMEMBERSHIPREQUEST']._serialized_start = 1547
    _globals['_GETMEMBERSHIPREQUEST']._serialized_end = 1654
    _globals['_DELETEMEMBERSHIPREQUEST']._serialized_start = 1656
    _globals['_DELETEMEMBERSHIPREQUEST']._serialized_end = 1766