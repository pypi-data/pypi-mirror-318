from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.settings.v1beta1 import component_settings_pb2 as _component_settings_pb2
from google.cloud.securitycenter.settings.v1beta1 import detector_pb2 as _detector_pb2
from google.cloud.securitycenter.settings.v1beta1 import settings_pb2 as _settings_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetServiceAccountRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('name', 'service_account')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_account: str

    def __init__(self, name: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class GetSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ('settings', 'update_mask')
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    settings: _settings_pb2.Settings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, settings: _Optional[_Union[_settings_pb2.Settings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ResetSettingsRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class BatchGetSettingsRequest(_message.Message):
    __slots__ = ('parent', 'names')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchGetSettingsResponse(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[_settings_pb2.Settings]

    def __init__(self, settings: _Optional[_Iterable[_Union[_settings_pb2.Settings, _Mapping]]]=...) -> None:
        ...

class CalculateEffectiveSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchCalculateEffectiveSettingsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CalculateEffectiveSettingsRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CalculateEffectiveSettingsRequest, _Mapping]]]=...) -> None:
        ...

class BatchCalculateEffectiveSettingsResponse(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[_settings_pb2.Settings]

    def __init__(self, settings: _Optional[_Iterable[_Union[_settings_pb2.Settings, _Mapping]]]=...) -> None:
        ...

class GetComponentSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateComponentSettingsRequest(_message.Message):
    __slots__ = ('component_settings', 'update_mask')
    COMPONENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    component_settings: _component_settings_pb2.ComponentSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, component_settings: _Optional[_Union[_component_settings_pb2.ComponentSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ResetComponentSettingsRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CalculateEffectiveComponentSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDetectorsRequest(_message.Message):
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

class ListDetectorsResponse(_message.Message):
    __slots__ = ('detectors', 'next_page_token')
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    detectors: _containers.RepeatedCompositeFieldContainer[_detector_pb2.Detector]
    next_page_token: str

    def __init__(self, detectors: _Optional[_Iterable[_Union[_detector_pb2.Detector, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListComponentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListComponentsResponse(_message.Message):
    __slots__ = ('components', 'next_page_token')
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    components: _containers.RepeatedScalarFieldContainer[str]
    next_page_token: str

    def __init__(self, components: _Optional[_Iterable[str]]=..., next_page_token: _Optional[str]=...) -> None:
        ...