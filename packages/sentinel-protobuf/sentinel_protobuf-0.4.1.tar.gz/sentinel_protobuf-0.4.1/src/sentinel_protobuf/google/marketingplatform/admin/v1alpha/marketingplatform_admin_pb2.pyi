from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.marketingplatform.admin.v1alpha import resources_pb2 as _resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnalyticsServiceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANALYTICS_SERVICE_LEVEL_UNSPECIFIED: _ClassVar[AnalyticsServiceLevel]
    ANALYTICS_SERVICE_LEVEL_STANDARD: _ClassVar[AnalyticsServiceLevel]
    ANALYTICS_SERVICE_LEVEL_360: _ClassVar[AnalyticsServiceLevel]
ANALYTICS_SERVICE_LEVEL_UNSPECIFIED: AnalyticsServiceLevel
ANALYTICS_SERVICE_LEVEL_STANDARD: AnalyticsServiceLevel
ANALYTICS_SERVICE_LEVEL_360: AnalyticsServiceLevel

class GetOrganizationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAnalyticsAccountLinksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAnalyticsAccountLinksResponse(_message.Message):
    __slots__ = ('analytics_account_links', 'next_page_token')
    ANALYTICS_ACCOUNT_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    analytics_account_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AnalyticsAccountLink]
    next_page_token: str

    def __init__(self, analytics_account_links: _Optional[_Iterable[_Union[_resources_pb2.AnalyticsAccountLink, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateAnalyticsAccountLinkRequest(_message.Message):
    __slots__ = ('parent', 'analytics_account_link')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_ACCOUNT_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    analytics_account_link: _resources_pb2.AnalyticsAccountLink

    def __init__(self, parent: _Optional[str]=..., analytics_account_link: _Optional[_Union[_resources_pb2.AnalyticsAccountLink, _Mapping]]=...) -> None:
        ...

class DeleteAnalyticsAccountLinkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SetPropertyServiceLevelRequest(_message.Message):
    __slots__ = ('analytics_account_link', 'analytics_property', 'service_level')
    ANALYTICS_ACCOUNT_LINK_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    analytics_account_link: str
    analytics_property: str
    service_level: AnalyticsServiceLevel

    def __init__(self, analytics_account_link: _Optional[str]=..., analytics_property: _Optional[str]=..., service_level: _Optional[_Union[AnalyticsServiceLevel, str]]=...) -> None:
        ...

class SetPropertyServiceLevelResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...