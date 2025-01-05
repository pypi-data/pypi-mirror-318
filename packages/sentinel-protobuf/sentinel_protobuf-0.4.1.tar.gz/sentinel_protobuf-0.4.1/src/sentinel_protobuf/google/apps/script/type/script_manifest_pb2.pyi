from google.apps.script.type import addon_widget_set_pb2 as _addon_widget_set_pb2
from google.apps.script.type import extension_point_pb2 as _extension_point_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HttpAuthorizationHeader(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_AUTHORIZATION_HEADER_UNSPECIFIED: _ClassVar[HttpAuthorizationHeader]
    SYSTEM_ID_TOKEN: _ClassVar[HttpAuthorizationHeader]
    USER_ID_TOKEN: _ClassVar[HttpAuthorizationHeader]
    NONE: _ClassVar[HttpAuthorizationHeader]
HTTP_AUTHORIZATION_HEADER_UNSPECIFIED: HttpAuthorizationHeader
SYSTEM_ID_TOKEN: HttpAuthorizationHeader
USER_ID_TOKEN: HttpAuthorizationHeader
NONE: HttpAuthorizationHeader

class CommonAddOnManifest(_message.Message):
    __slots__ = ('name', 'logo_url', 'layout_properties', 'add_on_widget_set', 'use_locale_from_app', 'homepage_trigger', 'universal_actions', 'open_link_url_prefixes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ADD_ON_WIDGET_SET_FIELD_NUMBER: _ClassVar[int]
    USE_LOCALE_FROM_APP_FIELD_NUMBER: _ClassVar[int]
    HOMEPAGE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    OPEN_LINK_URL_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    name: str
    logo_url: str
    layout_properties: LayoutProperties
    add_on_widget_set: _addon_widget_set_pb2.AddOnWidgetSet
    use_locale_from_app: bool
    homepage_trigger: _extension_point_pb2.HomepageExtensionPoint
    universal_actions: _containers.RepeatedCompositeFieldContainer[_extension_point_pb2.UniversalActionExtensionPoint]
    open_link_url_prefixes: _struct_pb2.ListValue

    def __init__(self, name: _Optional[str]=..., logo_url: _Optional[str]=..., layout_properties: _Optional[_Union[LayoutProperties, _Mapping]]=..., add_on_widget_set: _Optional[_Union[_addon_widget_set_pb2.AddOnWidgetSet, _Mapping]]=..., use_locale_from_app: bool=..., homepage_trigger: _Optional[_Union[_extension_point_pb2.HomepageExtensionPoint, _Mapping]]=..., universal_actions: _Optional[_Iterable[_Union[_extension_point_pb2.UniversalActionExtensionPoint, _Mapping]]]=..., open_link_url_prefixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...

class LayoutProperties(_message.Message):
    __slots__ = ('primary_color', 'secondary_color')
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    primary_color: str
    secondary_color: str

    def __init__(self, primary_color: _Optional[str]=..., secondary_color: _Optional[str]=...) -> None:
        ...

class HttpOptions(_message.Message):
    __slots__ = ('authorization_header',)
    AUTHORIZATION_HEADER_FIELD_NUMBER: _ClassVar[int]
    authorization_header: HttpAuthorizationHeader

    def __init__(self, authorization_header: _Optional[_Union[HttpAuthorizationHeader, str]]=...) -> None:
        ...