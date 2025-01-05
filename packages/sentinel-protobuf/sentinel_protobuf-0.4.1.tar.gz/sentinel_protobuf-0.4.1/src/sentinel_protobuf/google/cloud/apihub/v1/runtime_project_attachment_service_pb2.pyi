from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateRuntimeProjectAttachmentRequest(_message.Message):
    __slots__ = ('parent', 'runtime_project_attachment_id', 'runtime_project_attachment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_PROJECT_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_PROJECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    runtime_project_attachment_id: str
    runtime_project_attachment: RuntimeProjectAttachment

    def __init__(self, parent: _Optional[str]=..., runtime_project_attachment_id: _Optional[str]=..., runtime_project_attachment: _Optional[_Union[RuntimeProjectAttachment, _Mapping]]=...) -> None:
        ...

class GetRuntimeProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListRuntimeProjectAttachmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListRuntimeProjectAttachmentsResponse(_message.Message):
    __slots__ = ('runtime_project_attachments', 'next_page_token')
    RUNTIME_PROJECT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runtime_project_attachments: _containers.RepeatedCompositeFieldContainer[RuntimeProjectAttachment]
    next_page_token: str

    def __init__(self, runtime_project_attachments: _Optional[_Iterable[_Union[RuntimeProjectAttachment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteRuntimeProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupRuntimeProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupRuntimeProjectAttachmentResponse(_message.Message):
    __slots__ = ('runtime_project_attachment',)
    RUNTIME_PROJECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    runtime_project_attachment: RuntimeProjectAttachment

    def __init__(self, runtime_project_attachment: _Optional[_Union[RuntimeProjectAttachment, _Mapping]]=...) -> None:
        ...

class RuntimeProjectAttachment(_message.Message):
    __slots__ = ('name', 'runtime_project', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    runtime_project: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., runtime_project: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...