"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/customer_manager_link_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v16/errors/customer_manager_link_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\xd0\x03\n\x1cCustomerManagerLinkErrorEnum"\xaf\x03\n\x18CustomerManagerLinkError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11NO_PENDING_INVITE\x10\x02\x12\'\n#SAME_CLIENT_MORE_THAN_ONCE_PER_CALL\x10\x03\x12-\n)MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS\x10\x04\x12-\n)CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER\x10\x05\x12+\n\'CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER\x10\x06\x12+\n\'CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER\x10\x07\x122\n.CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT\x10\x08\x12\x19\n\x15DUPLICATE_CHILD_FOUND\x10\t\x12.\n*TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS\x10\nB\xfd\x01\n#com.google.ads.googleads.v16.errorsB\x1dCustomerManagerLinkErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.customer_manager_link_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x1dCustomerManagerLinkErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_CUSTOMERMANAGERLINKERRORENUM']._serialized_start = 103
    _globals['_CUSTOMERMANAGERLINKERRORENUM']._serialized_end = 567
    _globals['_CUSTOMERMANAGERLINKERRORENUM_CUSTOMERMANAGERLINKERROR']._serialized_start = 136
    _globals['_CUSTOMERMANAGERLINKERRORENUM_CUSTOMERMANAGERLINKERROR']._serialized_end = 567