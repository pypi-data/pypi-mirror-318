from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Attachment(_message.Message):
    __slots__ = ('name', 'target', 'type', 'attachment_namespace', 'annotations', 'create_time', 'update_time', 'files', 'oci_version_name')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    OCI_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    target: str
    type: str
    attachment_namespace: str
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    files: _containers.RepeatedScalarFieldContainer[str]
    oci_version_name: str

    def __init__(self, name: _Optional[str]=..., target: _Optional[str]=..., type: _Optional[str]=..., attachment_namespace: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., files: _Optional[_Iterable[str]]=..., oci_version_name: _Optional[str]=...) -> None:
        ...

class ListAttachmentsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAttachmentsResponse(_message.Message):
    __slots__ = ('attachments', 'next_page_token')
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    next_page_token: str

    def __init__(self, attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAttachmentRequest(_message.Message):
    __slots__ = ('parent', 'attachment_id', 'attachment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    attachment_id: str
    attachment: Attachment

    def __init__(self, parent: _Optional[str]=..., attachment_id: _Optional[str]=..., attachment: _Optional[_Union[Attachment, _Mapping]]=...) -> None:
        ...

class DeleteAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...