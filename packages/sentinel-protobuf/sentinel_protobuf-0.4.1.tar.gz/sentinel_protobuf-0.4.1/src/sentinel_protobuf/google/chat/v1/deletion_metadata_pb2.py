"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/deletion_metadata.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/chat/v1/deletion_metadata.proto\x12\x0egoogle.chat.v1"\xf7\x01\n\x10DeletionMetadata\x12D\n\rdeletion_type\x18\x01 \x01(\x0e2-.google.chat.v1.DeletionMetadata.DeletionType"\x9c\x01\n\x0cDeletionType\x12\x1d\n\x19DELETION_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATOR\x10\x01\x12\x0f\n\x0bSPACE_OWNER\x10\x02\x12\t\n\x05ADMIN\x10\x03\x12\x16\n\x12APP_MESSAGE_EXPIRY\x10\x04\x12\x13\n\x0fCREATOR_VIA_APP\x10\x05\x12\x17\n\x13SPACE_OWNER_VIA_APP\x10\x06B\xae\x01\n\x12com.google.chat.v1B\x15DeletionMetadataProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.deletion_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x15DeletionMetadataProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_DELETIONMETADATA']._serialized_start = 59
    _globals['_DELETIONMETADATA']._serialized_end = 306
    _globals['_DELETIONMETADATA_DELETIONTYPE']._serialized_start = 150
    _globals['_DELETIONMETADATA_DELETIONTYPE']._serialized_end = 306