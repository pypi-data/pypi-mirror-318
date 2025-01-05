from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SettingView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETTING_VIEW_UNSPECIFIED: _ClassVar[SettingView]
    SETTING_VIEW_BASIC: _ClassVar[SettingView]
    SETTING_VIEW_EFFECTIVE_VALUE: _ClassVar[SettingView]
    SETTING_VIEW_LOCAL_VALUE: _ClassVar[SettingView]
SETTING_VIEW_UNSPECIFIED: SettingView
SETTING_VIEW_BASIC: SettingView
SETTING_VIEW_EFFECTIVE_VALUE: SettingView
SETTING_VIEW_LOCAL_VALUE: SettingView

class Setting(_message.Message):
    __slots__ = ('name', 'metadata', 'local_value', 'effective_value', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    metadata: SettingMetadata
    local_value: Value
    effective_value: Value
    etag: str

    def __init__(self, name: _Optional[str]=..., metadata: _Optional[_Union[SettingMetadata, _Mapping]]=..., local_value: _Optional[_Union[Value, _Mapping]]=..., effective_value: _Optional[_Union[Value, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class SettingMetadata(_message.Message):
    __slots__ = ('display_name', 'description', 'read_only', 'data_type', 'default_value')

    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[SettingMetadata.DataType]
        BOOLEAN: _ClassVar[SettingMetadata.DataType]
        STRING: _ClassVar[SettingMetadata.DataType]
        STRING_SET: _ClassVar[SettingMetadata.DataType]
        ENUM_VALUE: _ClassVar[SettingMetadata.DataType]
    DATA_TYPE_UNSPECIFIED: SettingMetadata.DataType
    BOOLEAN: SettingMetadata.DataType
    STRING: SettingMetadata.DataType
    STRING_SET: SettingMetadata.DataType
    ENUM_VALUE: SettingMetadata.DataType
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    read_only: bool
    data_type: SettingMetadata.DataType
    default_value: Value

    def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., read_only: bool=..., data_type: _Optional[_Union[SettingMetadata.DataType, str]]=..., default_value: _Optional[_Union[Value, _Mapping]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('boolean_value', 'string_value', 'string_set_value', 'enum_value')

    class StringSet(_message.Message):
        __slots__ = ('values',)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
            ...

    class EnumValue(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_SET_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    boolean_value: bool
    string_value: str
    string_set_value: Value.StringSet
    enum_value: Value.EnumValue

    def __init__(self, boolean_value: bool=..., string_value: _Optional[str]=..., string_set_value: _Optional[_Union[Value.StringSet, _Mapping]]=..., enum_value: _Optional[_Union[Value.EnumValue, _Mapping]]=...) -> None:
        ...

class ListSettingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: SettingView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[SettingView, str]]=...) -> None:
        ...

class ListSettingsResponse(_message.Message):
    __slots__ = ('settings', 'next_page_token')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[Setting]
    next_page_token: str

    def __init__(self, settings: _Optional[_Iterable[_Union[Setting, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSettingRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: SettingView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[SettingView, str]]=...) -> None:
        ...

class UpdateSettingRequest(_message.Message):
    __slots__ = ('setting',)
    SETTING_FIELD_NUMBER: _ClassVar[int]
    setting: Setting

    def __init__(self, setting: _Optional[_Union[Setting, _Mapping]]=...) -> None:
        ...