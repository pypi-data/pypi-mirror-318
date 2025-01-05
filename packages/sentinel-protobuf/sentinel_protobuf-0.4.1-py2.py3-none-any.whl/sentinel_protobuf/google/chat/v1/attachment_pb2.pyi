from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Attachment(_message.Message):
    __slots__ = ('name', 'content_name', 'content_type', 'attachment_data_ref', 'drive_data_ref', 'thumbnail_uri', 'download_uri', 'source')

    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_UNSPECIFIED: _ClassVar[Attachment.Source]
        DRIVE_FILE: _ClassVar[Attachment.Source]
        UPLOADED_CONTENT: _ClassVar[Attachment.Source]
    SOURCE_UNSPECIFIED: Attachment.Source
    DRIVE_FILE: Attachment.Source
    UPLOADED_CONTENT: Attachment.Source
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_DATA_REF_FIELD_NUMBER: _ClassVar[int]
    DRIVE_DATA_REF_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URI_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    content_name: str
    content_type: str
    attachment_data_ref: AttachmentDataRef
    drive_data_ref: DriveDataRef
    thumbnail_uri: str
    download_uri: str
    source: Attachment.Source

    def __init__(self, name: _Optional[str]=..., content_name: _Optional[str]=..., content_type: _Optional[str]=..., attachment_data_ref: _Optional[_Union[AttachmentDataRef, _Mapping]]=..., drive_data_ref: _Optional[_Union[DriveDataRef, _Mapping]]=..., thumbnail_uri: _Optional[str]=..., download_uri: _Optional[str]=..., source: _Optional[_Union[Attachment.Source, str]]=...) -> None:
        ...

class DriveDataRef(_message.Message):
    __slots__ = ('drive_file_id',)
    DRIVE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    drive_file_id: str

    def __init__(self, drive_file_id: _Optional[str]=...) -> None:
        ...

class AttachmentDataRef(_message.Message):
    __slots__ = ('resource_name', 'attachment_upload_token')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    attachment_upload_token: str

    def __init__(self, resource_name: _Optional[str]=..., attachment_upload_token: _Optional[str]=...) -> None:
        ...

class GetAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UploadAttachmentRequest(_message.Message):
    __slots__ = ('parent', 'filename')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filename: str

    def __init__(self, parent: _Optional[str]=..., filename: _Optional[str]=...) -> None:
        ...

class UploadAttachmentResponse(_message.Message):
    __slots__ = ('attachment_data_ref',)
    ATTACHMENT_DATA_REF_FIELD_NUMBER: _ClassVar[int]
    attachment_data_ref: AttachmentDataRef

    def __init__(self, attachment_data_ref: _Optional[_Union[AttachmentDataRef, _Mapping]]=...) -> None:
        ...