from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_FORM_UNSPECIFIED: _ClassVar[DeviceForm]
    VIRTUAL: _ClassVar[DeviceForm]
    PHYSICAL: _ClassVar[DeviceForm]
    EMULATOR: _ClassVar[DeviceForm]

class DeviceFormFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_FORM_FACTOR_UNSPECIFIED: _ClassVar[DeviceFormFactor]
    PHONE: _ClassVar[DeviceFormFactor]
    TABLET: _ClassVar[DeviceFormFactor]
    WEARABLE: _ClassVar[DeviceFormFactor]

class DeviceCapacity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_CAPACITY_UNSPECIFIED: _ClassVar[DeviceCapacity]
    DEVICE_CAPACITY_HIGH: _ClassVar[DeviceCapacity]
    DEVICE_CAPACITY_MEDIUM: _ClassVar[DeviceCapacity]
    DEVICE_CAPACITY_LOW: _ClassVar[DeviceCapacity]
    DEVICE_CAPACITY_NONE: _ClassVar[DeviceCapacity]
DEVICE_FORM_UNSPECIFIED: DeviceForm
VIRTUAL: DeviceForm
PHYSICAL: DeviceForm
EMULATOR: DeviceForm
DEVICE_FORM_FACTOR_UNSPECIFIED: DeviceFormFactor
PHONE: DeviceFormFactor
TABLET: DeviceFormFactor
WEARABLE: DeviceFormFactor
DEVICE_CAPACITY_UNSPECIFIED: DeviceCapacity
DEVICE_CAPACITY_HIGH: DeviceCapacity
DEVICE_CAPACITY_MEDIUM: DeviceCapacity
DEVICE_CAPACITY_LOW: DeviceCapacity
DEVICE_CAPACITY_NONE: DeviceCapacity

class DeviceIpBlock(_message.Message):
    __slots__ = ('block', 'form', 'added_date')
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    ADDED_DATE_FIELD_NUMBER: _ClassVar[int]
    block: str
    form: DeviceForm
    added_date: _date_pb2.Date

    def __init__(self, block: _Optional[str]=..., form: _Optional[_Union[DeviceForm, str]]=..., added_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class GetTestEnvironmentCatalogRequest(_message.Message):
    __slots__ = ('environment_type', 'project_id')

    class EnvironmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENVIRONMENT_TYPE_UNSPECIFIED: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
        ANDROID: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
        IOS: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
        NETWORK_CONFIGURATION: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
        PROVIDED_SOFTWARE: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
        DEVICE_IP_BLOCKS: _ClassVar[GetTestEnvironmentCatalogRequest.EnvironmentType]
    ENVIRONMENT_TYPE_UNSPECIFIED: GetTestEnvironmentCatalogRequest.EnvironmentType
    ANDROID: GetTestEnvironmentCatalogRequest.EnvironmentType
    IOS: GetTestEnvironmentCatalogRequest.EnvironmentType
    NETWORK_CONFIGURATION: GetTestEnvironmentCatalogRequest.EnvironmentType
    PROVIDED_SOFTWARE: GetTestEnvironmentCatalogRequest.EnvironmentType
    DEVICE_IP_BLOCKS: GetTestEnvironmentCatalogRequest.EnvironmentType
    ENVIRONMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    environment_type: GetTestEnvironmentCatalogRequest.EnvironmentType
    project_id: str

    def __init__(self, environment_type: _Optional[_Union[GetTestEnvironmentCatalogRequest.EnvironmentType, str]]=..., project_id: _Optional[str]=...) -> None:
        ...

class TestEnvironmentCatalog(_message.Message):
    __slots__ = ('android_device_catalog', 'ios_device_catalog', 'network_configuration_catalog', 'software_catalog', 'device_ip_block_catalog')
    ANDROID_DEVICE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    IOS_DEVICE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIGURATION_CATALOG_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IP_BLOCK_CATALOG_FIELD_NUMBER: _ClassVar[int]
    android_device_catalog: AndroidDeviceCatalog
    ios_device_catalog: IosDeviceCatalog
    network_configuration_catalog: NetworkConfigurationCatalog
    software_catalog: ProvidedSoftwareCatalog
    device_ip_block_catalog: DeviceIpBlockCatalog

    def __init__(self, android_device_catalog: _Optional[_Union[AndroidDeviceCatalog, _Mapping]]=..., ios_device_catalog: _Optional[_Union[IosDeviceCatalog, _Mapping]]=..., network_configuration_catalog: _Optional[_Union[NetworkConfigurationCatalog, _Mapping]]=..., software_catalog: _Optional[_Union[ProvidedSoftwareCatalog, _Mapping]]=..., device_ip_block_catalog: _Optional[_Union[DeviceIpBlockCatalog, _Mapping]]=...) -> None:
        ...

class DeviceIpBlockCatalog(_message.Message):
    __slots__ = ('ip_blocks',)
    IP_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    ip_blocks: _containers.RepeatedCompositeFieldContainer[DeviceIpBlock]

    def __init__(self, ip_blocks: _Optional[_Iterable[_Union[DeviceIpBlock, _Mapping]]]=...) -> None:
        ...

class AndroidDeviceCatalog(_message.Message):
    __slots__ = ('models', 'versions', 'runtime_configuration')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[AndroidModel]
    versions: _containers.RepeatedCompositeFieldContainer[AndroidVersion]
    runtime_configuration: AndroidRuntimeConfiguration

    def __init__(self, models: _Optional[_Iterable[_Union[AndroidModel, _Mapping]]]=..., versions: _Optional[_Iterable[_Union[AndroidVersion, _Mapping]]]=..., runtime_configuration: _Optional[_Union[AndroidRuntimeConfiguration, _Mapping]]=...) -> None:
        ...

class AndroidRuntimeConfiguration(_message.Message):
    __slots__ = ('locales', 'orientations')
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    ORIENTATIONS_FIELD_NUMBER: _ClassVar[int]
    locales: _containers.RepeatedCompositeFieldContainer[Locale]
    orientations: _containers.RepeatedCompositeFieldContainer[Orientation]

    def __init__(self, locales: _Optional[_Iterable[_Union[Locale, _Mapping]]]=..., orientations: _Optional[_Iterable[_Union[Orientation, _Mapping]]]=...) -> None:
        ...

class AndroidModel(_message.Message):
    __slots__ = ('id', 'name', 'manufacturer', 'brand', 'codename', 'form', 'form_factor', 'per_version_info', 'screen_x', 'screen_y', 'screen_density', 'low_fps_video_recording', 'supported_version_ids', 'supported_abis', 'tags', 'thumbnail_url', 'lab_info')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CODENAME_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    PER_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SCREEN_X_FIELD_NUMBER: _ClassVar[int]
    SCREEN_Y_FIELD_NUMBER: _ClassVar[int]
    SCREEN_DENSITY_FIELD_NUMBER: _ClassVar[int]
    LOW_FPS_VIDEO_RECORDING_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ABIS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    LAB_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    manufacturer: str
    brand: str
    codename: str
    form: DeviceForm
    form_factor: DeviceFormFactor
    per_version_info: _containers.RepeatedCompositeFieldContainer[PerAndroidVersionInfo]
    screen_x: int
    screen_y: int
    screen_density: int
    low_fps_video_recording: bool
    supported_version_ids: _containers.RepeatedScalarFieldContainer[str]
    supported_abis: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    thumbnail_url: str
    lab_info: LabInfo

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., manufacturer: _Optional[str]=..., brand: _Optional[str]=..., codename: _Optional[str]=..., form: _Optional[_Union[DeviceForm, str]]=..., form_factor: _Optional[_Union[DeviceFormFactor, str]]=..., per_version_info: _Optional[_Iterable[_Union[PerAndroidVersionInfo, _Mapping]]]=..., screen_x: _Optional[int]=..., screen_y: _Optional[int]=..., screen_density: _Optional[int]=..., low_fps_video_recording: bool=..., supported_version_ids: _Optional[_Iterable[str]]=..., supported_abis: _Optional[_Iterable[str]]=..., tags: _Optional[_Iterable[str]]=..., thumbnail_url: _Optional[str]=..., lab_info: _Optional[_Union[LabInfo, _Mapping]]=...) -> None:
        ...

class AndroidVersion(_message.Message):
    __slots__ = ('id', 'version_string', 'api_level', 'code_name', 'release_date', 'distribution', 'tags')
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    API_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CODE_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version_string: str
    api_level: int
    code_name: str
    release_date: _date_pb2.Date
    distribution: Distribution
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., version_string: _Optional[str]=..., api_level: _Optional[int]=..., code_name: _Optional[str]=..., release_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., distribution: _Optional[_Union[Distribution, _Mapping]]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class PerAndroidVersionInfo(_message.Message):
    __slots__ = ('version_id', 'device_capacity', 'interactive_device_availability_estimate', 'direct_access_version_info')
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_DEVICE_AVAILABILITY_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ACCESS_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    device_capacity: DeviceCapacity
    interactive_device_availability_estimate: _duration_pb2.Duration
    direct_access_version_info: DirectAccessVersionInfo

    def __init__(self, version_id: _Optional[str]=..., device_capacity: _Optional[_Union[DeviceCapacity, str]]=..., interactive_device_availability_estimate: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., direct_access_version_info: _Optional[_Union[DirectAccessVersionInfo, _Mapping]]=...) -> None:
        ...

class DirectAccessVersionInfo(_message.Message):
    __slots__ = ('direct_access_supported', 'minimum_android_studio_version')
    DIRECT_ACCESS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ANDROID_STUDIO_VERSION_FIELD_NUMBER: _ClassVar[int]
    direct_access_supported: bool
    minimum_android_studio_version: str

    def __init__(self, direct_access_supported: bool=..., minimum_android_studio_version: _Optional[str]=...) -> None:
        ...

class Distribution(_message.Message):
    __slots__ = ('measurement_time', 'market_share')
    MEASUREMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    MARKET_SHARE_FIELD_NUMBER: _ClassVar[int]
    measurement_time: _timestamp_pb2.Timestamp
    market_share: float

    def __init__(self, measurement_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., market_share: _Optional[float]=...) -> None:
        ...

class LabInfo(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class IosDeviceCatalog(_message.Message):
    __slots__ = ('models', 'versions', 'xcode_versions', 'runtime_configuration')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    XCODE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[IosModel]
    versions: _containers.RepeatedCompositeFieldContainer[IosVersion]
    xcode_versions: _containers.RepeatedCompositeFieldContainer[XcodeVersion]
    runtime_configuration: IosRuntimeConfiguration

    def __init__(self, models: _Optional[_Iterable[_Union[IosModel, _Mapping]]]=..., versions: _Optional[_Iterable[_Union[IosVersion, _Mapping]]]=..., xcode_versions: _Optional[_Iterable[_Union[XcodeVersion, _Mapping]]]=..., runtime_configuration: _Optional[_Union[IosRuntimeConfiguration, _Mapping]]=...) -> None:
        ...

class IosRuntimeConfiguration(_message.Message):
    __slots__ = ('locales', 'orientations')
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    ORIENTATIONS_FIELD_NUMBER: _ClassVar[int]
    locales: _containers.RepeatedCompositeFieldContainer[Locale]
    orientations: _containers.RepeatedCompositeFieldContainer[Orientation]

    def __init__(self, locales: _Optional[_Iterable[_Union[Locale, _Mapping]]]=..., orientations: _Optional[_Iterable[_Union[Orientation, _Mapping]]]=...) -> None:
        ...

class IosModel(_message.Message):
    __slots__ = ('id', 'name', 'supported_version_ids', 'tags', 'device_capabilities', 'screen_x', 'screen_y', 'screen_density', 'form_factor', 'per_version_info')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SCREEN_X_FIELD_NUMBER: _ClassVar[int]
    SCREEN_Y_FIELD_NUMBER: _ClassVar[int]
    SCREEN_DENSITY_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    PER_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    supported_version_ids: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    device_capabilities: _containers.RepeatedScalarFieldContainer[str]
    screen_x: int
    screen_y: int
    screen_density: int
    form_factor: DeviceFormFactor
    per_version_info: _containers.RepeatedCompositeFieldContainer[PerIosVersionInfo]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., supported_version_ids: _Optional[_Iterable[str]]=..., tags: _Optional[_Iterable[str]]=..., device_capabilities: _Optional[_Iterable[str]]=..., screen_x: _Optional[int]=..., screen_y: _Optional[int]=..., screen_density: _Optional[int]=..., form_factor: _Optional[_Union[DeviceFormFactor, str]]=..., per_version_info: _Optional[_Iterable[_Union[PerIosVersionInfo, _Mapping]]]=...) -> None:
        ...

class IosVersion(_message.Message):
    __slots__ = ('id', 'major_version', 'minor_version', 'tags', 'supported_xcode_version_ids')
    ID_FIELD_NUMBER: _ClassVar[int]
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_XCODE_VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    major_version: int
    minor_version: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    supported_xcode_version_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., major_version: _Optional[int]=..., minor_version: _Optional[int]=..., tags: _Optional[_Iterable[str]]=..., supported_xcode_version_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class PerIosVersionInfo(_message.Message):
    __slots__ = ('version_id', 'device_capacity')
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    device_capacity: DeviceCapacity

    def __init__(self, version_id: _Optional[str]=..., device_capacity: _Optional[_Union[DeviceCapacity, str]]=...) -> None:
        ...

class Locale(_message.Message):
    __slots__ = ('id', 'name', 'region', 'tags')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    region: str
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., region: _Optional[str]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class Orientation(_message.Message):
    __slots__ = ('id', 'name', 'tags')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class XcodeVersion(_message.Message):
    __slots__ = ('version', 'tags')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    version: str
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, version: _Optional[str]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class NetworkConfigurationCatalog(_message.Message):
    __slots__ = ('configurations',)
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    configurations: _containers.RepeatedCompositeFieldContainer[NetworkConfiguration]

    def __init__(self, configurations: _Optional[_Iterable[_Union[NetworkConfiguration, _Mapping]]]=...) -> None:
        ...

class NetworkConfiguration(_message.Message):
    __slots__ = ('id', 'up_rule', 'down_rule')
    ID_FIELD_NUMBER: _ClassVar[int]
    UP_RULE_FIELD_NUMBER: _ClassVar[int]
    DOWN_RULE_FIELD_NUMBER: _ClassVar[int]
    id: str
    up_rule: TrafficRule
    down_rule: TrafficRule

    def __init__(self, id: _Optional[str]=..., up_rule: _Optional[_Union[TrafficRule, _Mapping]]=..., down_rule: _Optional[_Union[TrafficRule, _Mapping]]=...) -> None:
        ...

class TrafficRule(_message.Message):
    __slots__ = ('delay', 'packet_loss_ratio', 'packet_duplication_ratio', 'bandwidth', 'burst')
    DELAY_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_RATIO_FIELD_NUMBER: _ClassVar[int]
    PACKET_DUPLICATION_RATIO_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    BURST_FIELD_NUMBER: _ClassVar[int]
    delay: _duration_pb2.Duration
    packet_loss_ratio: float
    packet_duplication_ratio: float
    bandwidth: float
    burst: float

    def __init__(self, delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., packet_loss_ratio: _Optional[float]=..., packet_duplication_ratio: _Optional[float]=..., bandwidth: _Optional[float]=..., burst: _Optional[float]=...) -> None:
        ...

class ProvidedSoftwareCatalog(_message.Message):
    __slots__ = ('orchestrator_version', 'androidx_orchestrator_version')
    ORCHESTRATOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    ANDROIDX_ORCHESTRATOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    orchestrator_version: str
    androidx_orchestrator_version: str

    def __init__(self, orchestrator_version: _Optional[str]=..., androidx_orchestrator_version: _Optional[str]=...) -> None:
        ...