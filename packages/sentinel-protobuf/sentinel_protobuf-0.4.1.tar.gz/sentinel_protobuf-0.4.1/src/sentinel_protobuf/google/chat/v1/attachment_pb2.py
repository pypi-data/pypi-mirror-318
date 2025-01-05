"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/attachment.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/chat/v1/attachment.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfd\x03\n\nAttachment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0ccontent_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0ccontent_type\x18\x03 \x01(\tB\x03\xe0A\x03\x12E\n\x13attachment_data_ref\x18\x04 \x01(\x0b2!.google.chat.v1.AttachmentDataRefB\x03\xe0A\x01H\x00\x12;\n\x0edrive_data_ref\x18\x07 \x01(\x0b2\x1c.google.chat.v1.DriveDataRefB\x03\xe0A\x03H\x00\x12\x1a\n\rthumbnail_uri\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdownload_uri\x18\x06 \x01(\tB\x03\xe0A\x03\x126\n\x06source\x18\t \x01(\x0e2!.google.chat.v1.Attachment.SourceB\x03\xe0A\x03"F\n\x06Source\x12\x16\n\x12SOURCE_UNSPECIFIED\x10\x00\x12\x0e\n\nDRIVE_FILE\x10\x01\x12\x14\n\x10UPLOADED_CONTENT\x10\x02:_\xeaA\\\n\x1echat.googleapis.com/Attachment\x12:spaces/{space}/messages/{message}/attachments/{attachment}B\n\n\x08data_ref"%\n\x0cDriveDataRef\x12\x15\n\rdrive_file_id\x18\x02 \x01(\t"U\n\x11AttachmentDataRef\x12\x1a\n\rresource_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12$\n\x17attachment_upload_token\x18\x02 \x01(\tB\x03\xe0A\x01"L\n\x14GetAttachmentRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1echat.googleapis.com/Attachment"e\n\x17UploadAttachmentRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message\x12\x15\n\x08filename\x18\x04 \x01(\tB\x03\xe0A\x02"Z\n\x18UploadAttachmentResponse\x12>\n\x13attachment_data_ref\x18\x01 \x01(\x0b2!.google.chat.v1.AttachmentDataRefB\xa8\x01\n\x12com.google.chat.v1B\x0fAttachmentProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.attachment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0fAttachmentProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_ATTACHMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHMENT'].fields_by_name['content_name']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['content_name']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['content_type']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['content_type']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['attachment_data_ref']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['attachment_data_ref']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHMENT'].fields_by_name['drive_data_ref']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['drive_data_ref']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['thumbnail_uri']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['thumbnail_uri']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['download_uri']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['download_uri']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['source']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['source']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT']._loaded_options = None
    _globals['_ATTACHMENT']._serialized_options = b'\xeaA\\\n\x1echat.googleapis.com/Attachment\x12:spaces/{space}/messages/{message}/attachments/{attachment}'
    _globals['_ATTACHMENTDATAREF'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ATTACHMENTDATAREF'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHMENTDATAREF'].fields_by_name['attachment_upload_token']._loaded_options = None
    _globals['_ATTACHMENTDATAREF'].fields_by_name['attachment_upload_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1echat.googleapis.com/Attachment'
    _globals['_UPLOADATTACHMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPLOADATTACHMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message'
    _globals['_UPLOADATTACHMENTREQUEST'].fields_by_name['filename']._loaded_options = None
    _globals['_UPLOADATTACHMENTREQUEST'].fields_by_name['filename']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHMENT']._serialized_start = 112
    _globals['_ATTACHMENT']._serialized_end = 621
    _globals['_ATTACHMENT_SOURCE']._serialized_start = 442
    _globals['_ATTACHMENT_SOURCE']._serialized_end = 512
    _globals['_DRIVEDATAREF']._serialized_start = 623
    _globals['_DRIVEDATAREF']._serialized_end = 660
    _globals['_ATTACHMENTDATAREF']._serialized_start = 662
    _globals['_ATTACHMENTDATAREF']._serialized_end = 747
    _globals['_GETATTACHMENTREQUEST']._serialized_start = 749
    _globals['_GETATTACHMENTREQUEST']._serialized_end = 825
    _globals['_UPLOADATTACHMENTREQUEST']._serialized_start = 827
    _globals['_UPLOADATTACHMENTREQUEST']._serialized_end = 928
    _globals['_UPLOADATTACHMENTRESPONSE']._serialized_start = 930
    _globals['_UPLOADATTACHMENTRESPONSE']._serialized_end = 1020