from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Inventory(_message.Message):
    __slots__ = ('os_info', 'installed_packages', 'available_packages')

    class OsInfo(_message.Message):
        __slots__ = ('hostname', 'long_name', 'short_name', 'version', 'architecture', 'kernel_version', 'kernel_release', 'osconfig_agent_version')
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        LONG_NAME_FIELD_NUMBER: _ClassVar[int]
        SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
        KERNEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        KERNEL_RELEASE_FIELD_NUMBER: _ClassVar[int]
        OSCONFIG_AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        hostname: str
        long_name: str
        short_name: str
        version: str
        architecture: str
        kernel_version: str
        kernel_release: str
        osconfig_agent_version: str

        def __init__(self, hostname: _Optional[str]=..., long_name: _Optional[str]=..., short_name: _Optional[str]=..., version: _Optional[str]=..., architecture: _Optional[str]=..., kernel_version: _Optional[str]=..., kernel_release: _Optional[str]=..., osconfig_agent_version: _Optional[str]=...) -> None:
            ...

    class SoftwarePackage(_message.Message):
        __slots__ = ('yum_package', 'apt_package', 'zypper_package', 'googet_package', 'zypper_patch', 'wua_package', 'qfe_package', 'cos_package', 'windows_application')
        YUM_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        APT_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        ZYPPER_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        GOOGET_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        ZYPPER_PATCH_FIELD_NUMBER: _ClassVar[int]
        WUA_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        QFE_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        COS_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        WINDOWS_APPLICATION_FIELD_NUMBER: _ClassVar[int]
        yum_package: Inventory.VersionedPackage
        apt_package: Inventory.VersionedPackage
        zypper_package: Inventory.VersionedPackage
        googet_package: Inventory.VersionedPackage
        zypper_patch: Inventory.ZypperPatch
        wua_package: Inventory.WindowsUpdatePackage
        qfe_package: Inventory.WindowsQuickFixEngineeringPackage
        cos_package: Inventory.VersionedPackage
        windows_application: Inventory.WindowsApplication

        def __init__(self, yum_package: _Optional[_Union[Inventory.VersionedPackage, _Mapping]]=..., apt_package: _Optional[_Union[Inventory.VersionedPackage, _Mapping]]=..., zypper_package: _Optional[_Union[Inventory.VersionedPackage, _Mapping]]=..., googet_package: _Optional[_Union[Inventory.VersionedPackage, _Mapping]]=..., zypper_patch: _Optional[_Union[Inventory.ZypperPatch, _Mapping]]=..., wua_package: _Optional[_Union[Inventory.WindowsUpdatePackage, _Mapping]]=..., qfe_package: _Optional[_Union[Inventory.WindowsQuickFixEngineeringPackage, _Mapping]]=..., cos_package: _Optional[_Union[Inventory.VersionedPackage, _Mapping]]=..., windows_application: _Optional[_Union[Inventory.WindowsApplication, _Mapping]]=...) -> None:
            ...

    class VersionedPackage(_message.Message):
        __slots__ = ('package_name', 'architecture', 'version', 'source')

        class Source(_message.Message):
            __slots__ = ('name', 'version')
            NAME_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            name: str
            version: str

            def __init__(self, name: _Optional[str]=..., version: _Optional[str]=...) -> None:
                ...
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        package_name: str
        architecture: str
        version: str
        source: Inventory.VersionedPackage.Source

        def __init__(self, package_name: _Optional[str]=..., architecture: _Optional[str]=..., version: _Optional[str]=..., source: _Optional[_Union[Inventory.VersionedPackage.Source, _Mapping]]=...) -> None:
            ...

    class ZypperPatch(_message.Message):
        __slots__ = ('patch_name', 'category', 'severity', 'summary')
        PATCH_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        patch_name: str
        category: str
        severity: str
        summary: str

        def __init__(self, patch_name: _Optional[str]=..., category: _Optional[str]=..., severity: _Optional[str]=..., summary: _Optional[str]=...) -> None:
            ...

    class WindowsUpdatePackage(_message.Message):
        __slots__ = ('title', 'description', 'categories', 'kb_article_ids', 'support_url', 'more_info_urls', 'update_id', 'revision_number', 'last_deployment_change_time')

        class WindowsUpdateCategory(_message.Message):
            __slots__ = ('id', 'name')
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str

            def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
                ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        KB_ARTICLE_IDS_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_URL_FIELD_NUMBER: _ClassVar[int]
        MORE_INFO_URLS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
        REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LAST_DEPLOYMENT_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        categories: _containers.RepeatedCompositeFieldContainer[Inventory.WindowsUpdatePackage.WindowsUpdateCategory]
        kb_article_ids: _containers.RepeatedScalarFieldContainer[str]
        support_url: str
        more_info_urls: _containers.RepeatedScalarFieldContainer[str]
        update_id: str
        revision_number: int
        last_deployment_change_time: _timestamp_pb2.Timestamp

        def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., categories: _Optional[_Iterable[_Union[Inventory.WindowsUpdatePackage.WindowsUpdateCategory, _Mapping]]]=..., kb_article_ids: _Optional[_Iterable[str]]=..., support_url: _Optional[str]=..., more_info_urls: _Optional[_Iterable[str]]=..., update_id: _Optional[str]=..., revision_number: _Optional[int]=..., last_deployment_change_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class WindowsQuickFixEngineeringPackage(_message.Message):
        __slots__ = ('caption', 'description', 'hot_fix_id', 'install_time')
        CAPTION_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        HOT_FIX_ID_FIELD_NUMBER: _ClassVar[int]
        INSTALL_TIME_FIELD_NUMBER: _ClassVar[int]
        caption: str
        description: str
        hot_fix_id: str
        install_time: _timestamp_pb2.Timestamp

        def __init__(self, caption: _Optional[str]=..., description: _Optional[str]=..., hot_fix_id: _Optional[str]=..., install_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class WindowsApplication(_message.Message):
        __slots__ = ('display_name', 'display_version', 'publisher', 'install_date', 'help_link')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_VERSION_FIELD_NUMBER: _ClassVar[int]
        PUBLISHER_FIELD_NUMBER: _ClassVar[int]
        INSTALL_DATE_FIELD_NUMBER: _ClassVar[int]
        HELP_LINK_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        display_version: str
        publisher: str
        install_date: _date_pb2.Date
        help_link: str

        def __init__(self, display_name: _Optional[str]=..., display_version: _Optional[str]=..., publisher: _Optional[str]=..., install_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., help_link: _Optional[str]=...) -> None:
            ...
    OS_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    os_info: Inventory.OsInfo
    installed_packages: _containers.RepeatedCompositeFieldContainer[Inventory.SoftwarePackage]
    available_packages: _containers.RepeatedCompositeFieldContainer[Inventory.SoftwarePackage]

    def __init__(self, os_info: _Optional[_Union[Inventory.OsInfo, _Mapping]]=..., installed_packages: _Optional[_Iterable[_Union[Inventory.SoftwarePackage, _Mapping]]]=..., available_packages: _Optional[_Iterable[_Union[Inventory.SoftwarePackage, _Mapping]]]=...) -> None:
        ...