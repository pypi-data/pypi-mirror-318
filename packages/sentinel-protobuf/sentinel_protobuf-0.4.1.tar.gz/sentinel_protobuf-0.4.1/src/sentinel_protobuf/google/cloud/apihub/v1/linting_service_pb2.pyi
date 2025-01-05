from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetStyleGuideRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateStyleGuideRequest(_message.Message):
    __slots__ = ('style_guide', 'update_mask')
    STYLE_GUIDE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    style_guide: StyleGuide
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, style_guide: _Optional[_Union[StyleGuide, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetStyleGuideContentsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LintSpecRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StyleGuideContents(_message.Message):
    __slots__ = ('contents', 'mime_type')
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    mime_type: str

    def __init__(self, contents: _Optional[bytes]=..., mime_type: _Optional[str]=...) -> None:
        ...

class StyleGuide(_message.Message):
    __slots__ = ('name', 'linter', 'contents')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINTER_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    linter: _common_fields_pb2.Linter
    contents: StyleGuideContents

    def __init__(self, name: _Optional[str]=..., linter: _Optional[_Union[_common_fields_pb2.Linter, str]]=..., contents: _Optional[_Union[StyleGuideContents, _Mapping]]=...) -> None:
        ...