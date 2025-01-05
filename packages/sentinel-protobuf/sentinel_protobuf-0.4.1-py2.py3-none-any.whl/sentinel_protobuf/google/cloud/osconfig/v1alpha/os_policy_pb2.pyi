from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OSPolicy(_message.Message):
    __slots__ = ('id', 'description', 'mode', 'resource_groups', 'allow_no_resource_group_match')

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[OSPolicy.Mode]
        VALIDATION: _ClassVar[OSPolicy.Mode]
        ENFORCEMENT: _ClassVar[OSPolicy.Mode]
    MODE_UNSPECIFIED: OSPolicy.Mode
    VALIDATION: OSPolicy.Mode
    ENFORCEMENT: OSPolicy.Mode

    class OSFilter(_message.Message):
        __slots__ = ('os_short_name', 'os_version')
        OS_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        os_short_name: str
        os_version: str

        def __init__(self, os_short_name: _Optional[str]=..., os_version: _Optional[str]=...) -> None:
            ...

    class InventoryFilter(_message.Message):
        __slots__ = ('os_short_name', 'os_version')
        OS_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        os_short_name: str
        os_version: str

        def __init__(self, os_short_name: _Optional[str]=..., os_version: _Optional[str]=...) -> None:
            ...

    class Resource(_message.Message):
        __slots__ = ('id', 'pkg', 'repository', 'exec', 'file')

        class File(_message.Message):
            __slots__ = ('remote', 'gcs', 'local_path', 'allow_insecure')

            class Remote(_message.Message):
                __slots__ = ('uri', 'sha256_checksum')
                URI_FIELD_NUMBER: _ClassVar[int]
                SHA256_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
                uri: str
                sha256_checksum: str

                def __init__(self, uri: _Optional[str]=..., sha256_checksum: _Optional[str]=...) -> None:
                    ...

            class Gcs(_message.Message):
                __slots__ = ('bucket', 'object', 'generation')
                BUCKET_FIELD_NUMBER: _ClassVar[int]
                OBJECT_FIELD_NUMBER: _ClassVar[int]
                GENERATION_FIELD_NUMBER: _ClassVar[int]
                bucket: str
                object: str
                generation: int

                def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=...) -> None:
                    ...
            REMOTE_FIELD_NUMBER: _ClassVar[int]
            GCS_FIELD_NUMBER: _ClassVar[int]
            LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
            ALLOW_INSECURE_FIELD_NUMBER: _ClassVar[int]
            remote: OSPolicy.Resource.File.Remote
            gcs: OSPolicy.Resource.File.Gcs
            local_path: str
            allow_insecure: bool

            def __init__(self, remote: _Optional[_Union[OSPolicy.Resource.File.Remote, _Mapping]]=..., gcs: _Optional[_Union[OSPolicy.Resource.File.Gcs, _Mapping]]=..., local_path: _Optional[str]=..., allow_insecure: bool=...) -> None:
                ...

        class PackageResource(_message.Message):
            __slots__ = ('desired_state', 'apt', 'deb', 'yum', 'zypper', 'rpm', 'googet', 'msi')

            class DesiredState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                DESIRED_STATE_UNSPECIFIED: _ClassVar[OSPolicy.Resource.PackageResource.DesiredState]
                INSTALLED: _ClassVar[OSPolicy.Resource.PackageResource.DesiredState]
                REMOVED: _ClassVar[OSPolicy.Resource.PackageResource.DesiredState]
            DESIRED_STATE_UNSPECIFIED: OSPolicy.Resource.PackageResource.DesiredState
            INSTALLED: OSPolicy.Resource.PackageResource.DesiredState
            REMOVED: OSPolicy.Resource.PackageResource.DesiredState

            class Deb(_message.Message):
                __slots__ = ('source', 'pull_deps')
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                PULL_DEPS_FIELD_NUMBER: _ClassVar[int]
                source: OSPolicy.Resource.File
                pull_deps: bool

                def __init__(self, source: _Optional[_Union[OSPolicy.Resource.File, _Mapping]]=..., pull_deps: bool=...) -> None:
                    ...

            class APT(_message.Message):
                __slots__ = ('name',)
                NAME_FIELD_NUMBER: _ClassVar[int]
                name: str

                def __init__(self, name: _Optional[str]=...) -> None:
                    ...

            class RPM(_message.Message):
                __slots__ = ('source', 'pull_deps')
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                PULL_DEPS_FIELD_NUMBER: _ClassVar[int]
                source: OSPolicy.Resource.File
                pull_deps: bool

                def __init__(self, source: _Optional[_Union[OSPolicy.Resource.File, _Mapping]]=..., pull_deps: bool=...) -> None:
                    ...

            class YUM(_message.Message):
                __slots__ = ('name',)
                NAME_FIELD_NUMBER: _ClassVar[int]
                name: str

                def __init__(self, name: _Optional[str]=...) -> None:
                    ...

            class Zypper(_message.Message):
                __slots__ = ('name',)
                NAME_FIELD_NUMBER: _ClassVar[int]
                name: str

                def __init__(self, name: _Optional[str]=...) -> None:
                    ...

            class GooGet(_message.Message):
                __slots__ = ('name',)
                NAME_FIELD_NUMBER: _ClassVar[int]
                name: str

                def __init__(self, name: _Optional[str]=...) -> None:
                    ...

            class MSI(_message.Message):
                __slots__ = ('source', 'properties')
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                source: OSPolicy.Resource.File
                properties: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, source: _Optional[_Union[OSPolicy.Resource.File, _Mapping]]=..., properties: _Optional[_Iterable[str]]=...) -> None:
                    ...
            DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
            APT_FIELD_NUMBER: _ClassVar[int]
            DEB_FIELD_NUMBER: _ClassVar[int]
            YUM_FIELD_NUMBER: _ClassVar[int]
            ZYPPER_FIELD_NUMBER: _ClassVar[int]
            RPM_FIELD_NUMBER: _ClassVar[int]
            GOOGET_FIELD_NUMBER: _ClassVar[int]
            MSI_FIELD_NUMBER: _ClassVar[int]
            desired_state: OSPolicy.Resource.PackageResource.DesiredState
            apt: OSPolicy.Resource.PackageResource.APT
            deb: OSPolicy.Resource.PackageResource.Deb
            yum: OSPolicy.Resource.PackageResource.YUM
            zypper: OSPolicy.Resource.PackageResource.Zypper
            rpm: OSPolicy.Resource.PackageResource.RPM
            googet: OSPolicy.Resource.PackageResource.GooGet
            msi: OSPolicy.Resource.PackageResource.MSI

            def __init__(self, desired_state: _Optional[_Union[OSPolicy.Resource.PackageResource.DesiredState, str]]=..., apt: _Optional[_Union[OSPolicy.Resource.PackageResource.APT, _Mapping]]=..., deb: _Optional[_Union[OSPolicy.Resource.PackageResource.Deb, _Mapping]]=..., yum: _Optional[_Union[OSPolicy.Resource.PackageResource.YUM, _Mapping]]=..., zypper: _Optional[_Union[OSPolicy.Resource.PackageResource.Zypper, _Mapping]]=..., rpm: _Optional[_Union[OSPolicy.Resource.PackageResource.RPM, _Mapping]]=..., googet: _Optional[_Union[OSPolicy.Resource.PackageResource.GooGet, _Mapping]]=..., msi: _Optional[_Union[OSPolicy.Resource.PackageResource.MSI, _Mapping]]=...) -> None:
                ...

        class RepositoryResource(_message.Message):
            __slots__ = ('apt', 'yum', 'zypper', 'goo')

            class AptRepository(_message.Message):
                __slots__ = ('archive_type', 'uri', 'distribution', 'components', 'gpg_key')

                class ArchiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ARCHIVE_TYPE_UNSPECIFIED: _ClassVar[OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType]
                    DEB: _ClassVar[OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType]
                    DEB_SRC: _ClassVar[OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType]
                ARCHIVE_TYPE_UNSPECIFIED: OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType
                DEB: OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType
                DEB_SRC: OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType
                ARCHIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
                URI_FIELD_NUMBER: _ClassVar[int]
                DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
                COMPONENTS_FIELD_NUMBER: _ClassVar[int]
                GPG_KEY_FIELD_NUMBER: _ClassVar[int]
                archive_type: OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType
                uri: str
                distribution: str
                components: _containers.RepeatedScalarFieldContainer[str]
                gpg_key: str

                def __init__(self, archive_type: _Optional[_Union[OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType, str]]=..., uri: _Optional[str]=..., distribution: _Optional[str]=..., components: _Optional[_Iterable[str]]=..., gpg_key: _Optional[str]=...) -> None:
                    ...

            class YumRepository(_message.Message):
                __slots__ = ('id', 'display_name', 'base_url', 'gpg_keys')
                ID_FIELD_NUMBER: _ClassVar[int]
                DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
                BASE_URL_FIELD_NUMBER: _ClassVar[int]
                GPG_KEYS_FIELD_NUMBER: _ClassVar[int]
                id: str
                display_name: str
                base_url: str
                gpg_keys: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., base_url: _Optional[str]=..., gpg_keys: _Optional[_Iterable[str]]=...) -> None:
                    ...

            class ZypperRepository(_message.Message):
                __slots__ = ('id', 'display_name', 'base_url', 'gpg_keys')
                ID_FIELD_NUMBER: _ClassVar[int]
                DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
                BASE_URL_FIELD_NUMBER: _ClassVar[int]
                GPG_KEYS_FIELD_NUMBER: _ClassVar[int]
                id: str
                display_name: str
                base_url: str
                gpg_keys: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., base_url: _Optional[str]=..., gpg_keys: _Optional[_Iterable[str]]=...) -> None:
                    ...

            class GooRepository(_message.Message):
                __slots__ = ('name', 'url')
                NAME_FIELD_NUMBER: _ClassVar[int]
                URL_FIELD_NUMBER: _ClassVar[int]
                name: str
                url: str

                def __init__(self, name: _Optional[str]=..., url: _Optional[str]=...) -> None:
                    ...
            APT_FIELD_NUMBER: _ClassVar[int]
            YUM_FIELD_NUMBER: _ClassVar[int]
            ZYPPER_FIELD_NUMBER: _ClassVar[int]
            GOO_FIELD_NUMBER: _ClassVar[int]
            apt: OSPolicy.Resource.RepositoryResource.AptRepository
            yum: OSPolicy.Resource.RepositoryResource.YumRepository
            zypper: OSPolicy.Resource.RepositoryResource.ZypperRepository
            goo: OSPolicy.Resource.RepositoryResource.GooRepository

            def __init__(self, apt: _Optional[_Union[OSPolicy.Resource.RepositoryResource.AptRepository, _Mapping]]=..., yum: _Optional[_Union[OSPolicy.Resource.RepositoryResource.YumRepository, _Mapping]]=..., zypper: _Optional[_Union[OSPolicy.Resource.RepositoryResource.ZypperRepository, _Mapping]]=..., goo: _Optional[_Union[OSPolicy.Resource.RepositoryResource.GooRepository, _Mapping]]=...) -> None:
                ...

        class ExecResource(_message.Message):
            __slots__ = ('validate', 'enforce')

            class Exec(_message.Message):
                __slots__ = ('file', 'script', 'args', 'interpreter', 'output_file_path')

                class Interpreter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    INTERPRETER_UNSPECIFIED: _ClassVar[OSPolicy.Resource.ExecResource.Exec.Interpreter]
                    NONE: _ClassVar[OSPolicy.Resource.ExecResource.Exec.Interpreter]
                    SHELL: _ClassVar[OSPolicy.Resource.ExecResource.Exec.Interpreter]
                    POWERSHELL: _ClassVar[OSPolicy.Resource.ExecResource.Exec.Interpreter]
                INTERPRETER_UNSPECIFIED: OSPolicy.Resource.ExecResource.Exec.Interpreter
                NONE: OSPolicy.Resource.ExecResource.Exec.Interpreter
                SHELL: OSPolicy.Resource.ExecResource.Exec.Interpreter
                POWERSHELL: OSPolicy.Resource.ExecResource.Exec.Interpreter
                FILE_FIELD_NUMBER: _ClassVar[int]
                SCRIPT_FIELD_NUMBER: _ClassVar[int]
                ARGS_FIELD_NUMBER: _ClassVar[int]
                INTERPRETER_FIELD_NUMBER: _ClassVar[int]
                OUTPUT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
                file: OSPolicy.Resource.File
                script: str
                args: _containers.RepeatedScalarFieldContainer[str]
                interpreter: OSPolicy.Resource.ExecResource.Exec.Interpreter
                output_file_path: str

                def __init__(self, file: _Optional[_Union[OSPolicy.Resource.File, _Mapping]]=..., script: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., interpreter: _Optional[_Union[OSPolicy.Resource.ExecResource.Exec.Interpreter, str]]=..., output_file_path: _Optional[str]=...) -> None:
                    ...
            VALIDATE_FIELD_NUMBER: _ClassVar[int]
            ENFORCE_FIELD_NUMBER: _ClassVar[int]
            validate: OSPolicy.Resource.ExecResource.Exec
            enforce: OSPolicy.Resource.ExecResource.Exec

            def __init__(self, validate: _Optional[_Union[OSPolicy.Resource.ExecResource.Exec, _Mapping]]=..., enforce: _Optional[_Union[OSPolicy.Resource.ExecResource.Exec, _Mapping]]=...) -> None:
                ...

        class FileResource(_message.Message):
            __slots__ = ('file', 'content', 'path', 'state', 'permissions')

            class DesiredState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                DESIRED_STATE_UNSPECIFIED: _ClassVar[OSPolicy.Resource.FileResource.DesiredState]
                PRESENT: _ClassVar[OSPolicy.Resource.FileResource.DesiredState]
                ABSENT: _ClassVar[OSPolicy.Resource.FileResource.DesiredState]
                CONTENTS_MATCH: _ClassVar[OSPolicy.Resource.FileResource.DesiredState]
            DESIRED_STATE_UNSPECIFIED: OSPolicy.Resource.FileResource.DesiredState
            PRESENT: OSPolicy.Resource.FileResource.DesiredState
            ABSENT: OSPolicy.Resource.FileResource.DesiredState
            CONTENTS_MATCH: OSPolicy.Resource.FileResource.DesiredState
            FILE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            PATH_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            file: OSPolicy.Resource.File
            content: str
            path: str
            state: OSPolicy.Resource.FileResource.DesiredState
            permissions: str

            def __init__(self, file: _Optional[_Union[OSPolicy.Resource.File, _Mapping]]=..., content: _Optional[str]=..., path: _Optional[str]=..., state: _Optional[_Union[OSPolicy.Resource.FileResource.DesiredState, str]]=..., permissions: _Optional[str]=...) -> None:
                ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PKG_FIELD_NUMBER: _ClassVar[int]
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        EXEC_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        id: str
        pkg: OSPolicy.Resource.PackageResource
        repository: OSPolicy.Resource.RepositoryResource
        exec: OSPolicy.Resource.ExecResource
        file: OSPolicy.Resource.FileResource

        def __init__(self, id: _Optional[str]=..., pkg: _Optional[_Union[OSPolicy.Resource.PackageResource, _Mapping]]=..., repository: _Optional[_Union[OSPolicy.Resource.RepositoryResource, _Mapping]]=..., exec: _Optional[_Union[OSPolicy.Resource.ExecResource, _Mapping]]=..., file: _Optional[_Union[OSPolicy.Resource.FileResource, _Mapping]]=...) -> None:
            ...

    class ResourceGroup(_message.Message):
        __slots__ = ('os_filter', 'inventory_filters', 'resources')
        OS_FILTER_FIELD_NUMBER: _ClassVar[int]
        INVENTORY_FILTERS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        os_filter: OSPolicy.OSFilter
        inventory_filters: _containers.RepeatedCompositeFieldContainer[OSPolicy.InventoryFilter]
        resources: _containers.RepeatedCompositeFieldContainer[OSPolicy.Resource]

        def __init__(self, os_filter: _Optional[_Union[OSPolicy.OSFilter, _Mapping]]=..., inventory_filters: _Optional[_Iterable[_Union[OSPolicy.InventoryFilter, _Mapping]]]=..., resources: _Optional[_Iterable[_Union[OSPolicy.Resource, _Mapping]]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NO_RESOURCE_GROUP_MATCH_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    mode: OSPolicy.Mode
    resource_groups: _containers.RepeatedCompositeFieldContainer[OSPolicy.ResourceGroup]
    allow_no_resource_group_match: bool

    def __init__(self, id: _Optional[str]=..., description: _Optional[str]=..., mode: _Optional[_Union[OSPolicy.Mode, str]]=..., resource_groups: _Optional[_Iterable[_Union[OSPolicy.ResourceGroup, _Mapping]]]=..., allow_no_resource_group_match: bool=...) -> None:
        ...