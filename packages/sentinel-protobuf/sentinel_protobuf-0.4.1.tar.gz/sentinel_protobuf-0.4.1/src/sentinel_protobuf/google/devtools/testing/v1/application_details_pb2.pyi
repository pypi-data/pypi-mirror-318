from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.devtools.testing.v1 import test_execution_pb2 as _test_execution_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ApkDetail(_message.Message):
    __slots__ = ('apk_manifest',)
    APK_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    apk_manifest: ApkManifest

    def __init__(self, apk_manifest: _Optional[_Union[ApkManifest, _Mapping]]=...) -> None:
        ...

class ApkManifest(_message.Message):
    __slots__ = ('package_name', 'min_sdk_version', 'max_sdk_version', 'target_sdk_version', 'application_label', 'intent_filters', 'uses_permission_tags', 'uses_permission', 'version_code', 'version_name', 'metadata', 'uses_feature', 'services')
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_LABEL_FIELD_NUMBER: _ClassVar[int]
    INTENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    USES_PERMISSION_TAGS_FIELD_NUMBER: _ClassVar[int]
    USES_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USES_FEATURE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    package_name: str
    min_sdk_version: int
    max_sdk_version: int
    target_sdk_version: int
    application_label: str
    intent_filters: _containers.RepeatedCompositeFieldContainer[IntentFilter]
    uses_permission_tags: _containers.RepeatedCompositeFieldContainer[UsesPermissionTag]
    uses_permission: _containers.RepeatedScalarFieldContainer[str]
    version_code: int
    version_name: str
    metadata: _containers.RepeatedCompositeFieldContainer[Metadata]
    uses_feature: _containers.RepeatedCompositeFieldContainer[UsesFeature]
    services: _containers.RepeatedCompositeFieldContainer[Service]

    def __init__(self, package_name: _Optional[str]=..., min_sdk_version: _Optional[int]=..., max_sdk_version: _Optional[int]=..., target_sdk_version: _Optional[int]=..., application_label: _Optional[str]=..., intent_filters: _Optional[_Iterable[_Union[IntentFilter, _Mapping]]]=..., uses_permission_tags: _Optional[_Iterable[_Union[UsesPermissionTag, _Mapping]]]=..., uses_permission: _Optional[_Iterable[str]]=..., version_code: _Optional[int]=..., version_name: _Optional[str]=..., metadata: _Optional[_Iterable[_Union[Metadata, _Mapping]]]=..., uses_feature: _Optional[_Iterable[_Union[UsesFeature, _Mapping]]]=..., services: _Optional[_Iterable[_Union[Service, _Mapping]]]=...) -> None:
        ...

class UsesPermissionTag(_message.Message):
    __slots__ = ('name', 'max_sdk_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    max_sdk_version: int

    def __init__(self, name: _Optional[str]=..., max_sdk_version: _Optional[int]=...) -> None:
        ...

class Service(_message.Message):
    __slots__ = ('name', 'intent_filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    intent_filter: _containers.RepeatedCompositeFieldContainer[IntentFilter]

    def __init__(self, name: _Optional[str]=..., intent_filter: _Optional[_Iterable[_Union[IntentFilter, _Mapping]]]=...) -> None:
        ...

class IntentFilter(_message.Message):
    __slots__ = ('action_names', 'category_names', 'mime_type')
    ACTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAMES_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    action_names: _containers.RepeatedScalarFieldContainer[str]
    category_names: _containers.RepeatedScalarFieldContainer[str]
    mime_type: str

    def __init__(self, action_names: _Optional[_Iterable[str]]=..., category_names: _Optional[_Iterable[str]]=..., mime_type: _Optional[str]=...) -> None:
        ...

class Metadata(_message.Message):
    __slots__ = ('name', 'value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str

    def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class UsesFeature(_message.Message):
    __slots__ = ('name', 'is_required')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_required: bool

    def __init__(self, name: _Optional[str]=..., is_required: bool=...) -> None:
        ...

class GetApkDetailsRequest(_message.Message):
    __slots__ = ('location', 'bundle_location')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _test_execution_pb2.FileReference
    bundle_location: _test_execution_pb2.FileReference

    def __init__(self, location: _Optional[_Union[_test_execution_pb2.FileReference, _Mapping]]=..., bundle_location: _Optional[_Union[_test_execution_pb2.FileReference, _Mapping]]=...) -> None:
        ...

class GetApkDetailsResponse(_message.Message):
    __slots__ = ('apk_detail',)
    APK_DETAIL_FIELD_NUMBER: _ClassVar[int]
    apk_detail: ApkDetail

    def __init__(self, apk_detail: _Optional[_Union[ApkDetail, _Mapping]]=...) -> None:
        ...