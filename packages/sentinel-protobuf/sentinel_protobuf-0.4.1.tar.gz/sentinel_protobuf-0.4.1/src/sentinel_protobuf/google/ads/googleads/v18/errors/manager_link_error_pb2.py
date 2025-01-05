"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/manager_link_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v18/errors/manager_link_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\x8d\x05\n\x14ManagerLinkErrorEnum"\xf4\x04\n\x10ManagerLinkError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING\x10\x02\x12\x15\n\x11TOO_MANY_MANAGERS\x10\x03\x12\x14\n\x10TOO_MANY_INVITES\x10\x04\x12#\n\x1fALREADY_INVITED_BY_THIS_MANAGER\x10\x05\x12#\n\x1fALREADY_MANAGED_BY_THIS_MANAGER\x10\x06\x12 \n\x1cALREADY_MANAGED_IN_HIERARCHY\x10\x07\x12\x19\n\x15DUPLICATE_CHILD_FOUND\x10\x08\x12\x1c\n\x18CLIENT_HAS_NO_ADMIN_USER\x10\t\x12\x16\n\x12MAX_DEPTH_EXCEEDED\x10\n\x12\x15\n\x11CYCLE_NOT_ALLOWED\x10\x0b\x12\x15\n\x11TOO_MANY_ACCOUNTS\x10\x0c\x12 \n\x1cTOO_MANY_ACCOUNTS_AT_MANAGER\x10\r\x12%\n!NON_OWNER_USER_CANNOT_MODIFY_LINK\x10\x0e\x12(\n$SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS\x10\x0f\x12\x17\n\x13CLIENT_OUTSIDE_TREE\x10\x10\x12\x19\n\x15INVALID_STATUS_CHANGE\x10\x11\x12\x12\n\x0eINVALID_CHANGE\x10\x12\x12\x1f\n\x1bCUSTOMER_CANNOT_MANAGE_SELF\x10\x13\x12%\n!CREATING_ENABLED_LINK_NOT_ALLOWED\x10\x14B\xf5\x01\n#com.google.ads.googleads.v18.errorsB\x15ManagerLinkErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.manager_link_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x15ManagerLinkErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_MANAGERLINKERRORENUM']._serialized_start = 94
    _globals['_MANAGERLINKERRORENUM']._serialized_end = 747
    _globals['_MANAGERLINKERRORENUM_MANAGERLINKERROR']._serialized_start = 119
    _globals['_MANAGERLINKERRORENUM_MANAGERLINKERROR']._serialized_end = 747