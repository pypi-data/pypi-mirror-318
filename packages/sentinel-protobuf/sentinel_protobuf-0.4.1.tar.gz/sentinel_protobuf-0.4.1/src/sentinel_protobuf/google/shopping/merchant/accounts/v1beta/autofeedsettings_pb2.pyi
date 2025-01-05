from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutofeedSettings(_message.Message):
    __slots__ = ('name', 'enable_products', 'eligible')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    enable_products: bool
    eligible: bool

    def __init__(self, name: _Optional[str]=..., enable_products: bool=..., eligible: bool=...) -> None:
        ...

class GetAutofeedSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAutofeedSettingsRequest(_message.Message):
    __slots__ = ('autofeed_settings', 'update_mask')
    AUTOFEED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    autofeed_settings: AutofeedSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, autofeed_settings: _Optional[_Union[AutofeedSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...