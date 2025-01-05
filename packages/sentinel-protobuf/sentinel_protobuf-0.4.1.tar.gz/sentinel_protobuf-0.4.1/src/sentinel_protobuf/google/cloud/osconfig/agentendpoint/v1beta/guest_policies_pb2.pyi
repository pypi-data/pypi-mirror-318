from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DesiredState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DESIRED_STATE_UNSPECIFIED: _ClassVar[DesiredState]
    INSTALLED: _ClassVar[DesiredState]
    UPDATED: _ClassVar[DesiredState]
    REMOVED: _ClassVar[DesiredState]
DESIRED_STATE_UNSPECIFIED: DesiredState
INSTALLED: DesiredState
UPDATED: DesiredState
REMOVED: DesiredState

class Package(_message.Message):
    __slots__ = ('name', 'desired_state', 'manager')

    class Manager(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANAGER_UNSPECIFIED: _ClassVar[Package.Manager]
        ANY: _ClassVar[Package.Manager]
        APT: _ClassVar[Package.Manager]
        YUM: _ClassVar[Package.Manager]
        ZYPPER: _ClassVar[Package.Manager]
        GOO: _ClassVar[Package.Manager]
    MANAGER_UNSPECIFIED: Package.Manager
    ANY: Package.Manager
    APT: Package.Manager
    YUM: Package.Manager
    ZYPPER: Package.Manager
    GOO: Package.Manager
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    name: str
    desired_state: DesiredState
    manager: Package.Manager

    def __init__(self, name: _Optional[str]=..., desired_state: _Optional[_Union[DesiredState, str]]=..., manager: _Optional[_Union[Package.Manager, str]]=...) -> None:
        ...

class AptRepository(_message.Message):
    __slots__ = ('archive_type', 'uri', 'distribution', 'components', 'gpg_key')

    class ArchiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARCHIVE_TYPE_UNSPECIFIED: _ClassVar[AptRepository.ArchiveType]
        DEB: _ClassVar[AptRepository.ArchiveType]
        DEB_SRC: _ClassVar[AptRepository.ArchiveType]
    ARCHIVE_TYPE_UNSPECIFIED: AptRepository.ArchiveType
    DEB: AptRepository.ArchiveType
    DEB_SRC: AptRepository.ArchiveType
    ARCHIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    GPG_KEY_FIELD_NUMBER: _ClassVar[int]
    archive_type: AptRepository.ArchiveType
    uri: str
    distribution: str
    components: _containers.RepeatedScalarFieldContainer[str]
    gpg_key: str

    def __init__(self, archive_type: _Optional[_Union[AptRepository.ArchiveType, str]]=..., uri: _Optional[str]=..., distribution: _Optional[str]=..., components: _Optional[_Iterable[str]]=..., gpg_key: _Optional[str]=...) -> None:
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

class PackageRepository(_message.Message):
    __slots__ = ('apt', 'yum', 'zypper', 'goo')
    APT_FIELD_NUMBER: _ClassVar[int]
    YUM_FIELD_NUMBER: _ClassVar[int]
    ZYPPER_FIELD_NUMBER: _ClassVar[int]
    GOO_FIELD_NUMBER: _ClassVar[int]
    apt: AptRepository
    yum: YumRepository
    zypper: ZypperRepository
    goo: GooRepository

    def __init__(self, apt: _Optional[_Union[AptRepository, _Mapping]]=..., yum: _Optional[_Union[YumRepository, _Mapping]]=..., zypper: _Optional[_Union[ZypperRepository, _Mapping]]=..., goo: _Optional[_Union[GooRepository, _Mapping]]=...) -> None:
        ...

class SoftwareRecipe(_message.Message):
    __slots__ = ('name', 'version', 'artifacts', 'install_steps', 'update_steps', 'desired_state')

    class Artifact(_message.Message):
        __slots__ = ('id', 'remote', 'gcs', 'allow_insecure')

        class Remote(_message.Message):
            __slots__ = ('uri', 'checksum')
            URI_FIELD_NUMBER: _ClassVar[int]
            CHECKSUM_FIELD_NUMBER: _ClassVar[int]
            uri: str
            checksum: str

            def __init__(self, uri: _Optional[str]=..., checksum: _Optional[str]=...) -> None:
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
        ID_FIELD_NUMBER: _ClassVar[int]
        REMOTE_FIELD_NUMBER: _ClassVar[int]
        GCS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_INSECURE_FIELD_NUMBER: _ClassVar[int]
        id: str
        remote: SoftwareRecipe.Artifact.Remote
        gcs: SoftwareRecipe.Artifact.Gcs
        allow_insecure: bool

        def __init__(self, id: _Optional[str]=..., remote: _Optional[_Union[SoftwareRecipe.Artifact.Remote, _Mapping]]=..., gcs: _Optional[_Union[SoftwareRecipe.Artifact.Gcs, _Mapping]]=..., allow_insecure: bool=...) -> None:
            ...

    class Step(_message.Message):
        __slots__ = ('file_copy', 'archive_extraction', 'msi_installation', 'dpkg_installation', 'rpm_installation', 'file_exec', 'script_run')

        class CopyFile(_message.Message):
            __slots__ = ('artifact_id', 'destination', 'overwrite', 'permissions')
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            DESTINATION_FIELD_NUMBER: _ClassVar[int]
            OVERWRITE_FIELD_NUMBER: _ClassVar[int]
            PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str
            destination: str
            overwrite: bool
            permissions: str

            def __init__(self, artifact_id: _Optional[str]=..., destination: _Optional[str]=..., overwrite: bool=..., permissions: _Optional[str]=...) -> None:
                ...

        class ExtractArchive(_message.Message):
            __slots__ = ('artifact_id', 'destination', 'type')

            class ArchiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ARCHIVE_TYPE_UNSPECIFIED: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                TAR: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                TAR_GZIP: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                TAR_BZIP: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                TAR_LZMA: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                TAR_XZ: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
                ZIP: _ClassVar[SoftwareRecipe.Step.ExtractArchive.ArchiveType]
            ARCHIVE_TYPE_UNSPECIFIED: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            TAR: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            TAR_GZIP: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            TAR_BZIP: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            TAR_LZMA: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            TAR_XZ: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            ZIP: SoftwareRecipe.Step.ExtractArchive.ArchiveType
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            DESTINATION_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str
            destination: str
            type: SoftwareRecipe.Step.ExtractArchive.ArchiveType

            def __init__(self, artifact_id: _Optional[str]=..., destination: _Optional[str]=..., type: _Optional[_Union[SoftwareRecipe.Step.ExtractArchive.ArchiveType, str]]=...) -> None:
                ...

        class InstallMsi(_message.Message):
            __slots__ = ('artifact_id', 'flags', 'allowed_exit_codes')
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            FLAGS_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str
            flags: _containers.RepeatedScalarFieldContainer[str]
            allowed_exit_codes: _containers.RepeatedScalarFieldContainer[int]

            def __init__(self, artifact_id: _Optional[str]=..., flags: _Optional[_Iterable[str]]=..., allowed_exit_codes: _Optional[_Iterable[int]]=...) -> None:
                ...

        class InstallDpkg(_message.Message):
            __slots__ = ('artifact_id',)
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str

            def __init__(self, artifact_id: _Optional[str]=...) -> None:
                ...

        class InstallRpm(_message.Message):
            __slots__ = ('artifact_id',)
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str

            def __init__(self, artifact_id: _Optional[str]=...) -> None:
                ...

        class ExecFile(_message.Message):
            __slots__ = ('artifact_id', 'local_path', 'args', 'allowed_exit_codes')
            ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
            LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
            ARGS_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
            artifact_id: str
            local_path: str
            args: _containers.RepeatedScalarFieldContainer[str]
            allowed_exit_codes: _containers.RepeatedScalarFieldContainer[int]

            def __init__(self, artifact_id: _Optional[str]=..., local_path: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., allowed_exit_codes: _Optional[_Iterable[int]]=...) -> None:
                ...

        class RunScript(_message.Message):
            __slots__ = ('script', 'allowed_exit_codes', 'interpreter')

            class Interpreter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                INTERPRETER_UNSPECIFIED: _ClassVar[SoftwareRecipe.Step.RunScript.Interpreter]
                SHELL: _ClassVar[SoftwareRecipe.Step.RunScript.Interpreter]
                POWERSHELL: _ClassVar[SoftwareRecipe.Step.RunScript.Interpreter]
            INTERPRETER_UNSPECIFIED: SoftwareRecipe.Step.RunScript.Interpreter
            SHELL: SoftwareRecipe.Step.RunScript.Interpreter
            POWERSHELL: SoftwareRecipe.Step.RunScript.Interpreter
            SCRIPT_FIELD_NUMBER: _ClassVar[int]
            ALLOWED_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
            INTERPRETER_FIELD_NUMBER: _ClassVar[int]
            script: str
            allowed_exit_codes: _containers.RepeatedScalarFieldContainer[int]
            interpreter: SoftwareRecipe.Step.RunScript.Interpreter

            def __init__(self, script: _Optional[str]=..., allowed_exit_codes: _Optional[_Iterable[int]]=..., interpreter: _Optional[_Union[SoftwareRecipe.Step.RunScript.Interpreter, str]]=...) -> None:
                ...
        FILE_COPY_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
        MSI_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        DPKG_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        RPM_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        FILE_EXEC_FIELD_NUMBER: _ClassVar[int]
        SCRIPT_RUN_FIELD_NUMBER: _ClassVar[int]
        file_copy: SoftwareRecipe.Step.CopyFile
        archive_extraction: SoftwareRecipe.Step.ExtractArchive
        msi_installation: SoftwareRecipe.Step.InstallMsi
        dpkg_installation: SoftwareRecipe.Step.InstallDpkg
        rpm_installation: SoftwareRecipe.Step.InstallRpm
        file_exec: SoftwareRecipe.Step.ExecFile
        script_run: SoftwareRecipe.Step.RunScript

        def __init__(self, file_copy: _Optional[_Union[SoftwareRecipe.Step.CopyFile, _Mapping]]=..., archive_extraction: _Optional[_Union[SoftwareRecipe.Step.ExtractArchive, _Mapping]]=..., msi_installation: _Optional[_Union[SoftwareRecipe.Step.InstallMsi, _Mapping]]=..., dpkg_installation: _Optional[_Union[SoftwareRecipe.Step.InstallDpkg, _Mapping]]=..., rpm_installation: _Optional[_Union[SoftwareRecipe.Step.InstallRpm, _Mapping]]=..., file_exec: _Optional[_Union[SoftwareRecipe.Step.ExecFile, _Mapping]]=..., script_run: _Optional[_Union[SoftwareRecipe.Step.RunScript, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    INSTALL_STEPS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STEPS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    artifacts: _containers.RepeatedCompositeFieldContainer[SoftwareRecipe.Artifact]
    install_steps: _containers.RepeatedCompositeFieldContainer[SoftwareRecipe.Step]
    update_steps: _containers.RepeatedCompositeFieldContainer[SoftwareRecipe.Step]
    desired_state: DesiredState

    def __init__(self, name: _Optional[str]=..., version: _Optional[str]=..., artifacts: _Optional[_Iterable[_Union[SoftwareRecipe.Artifact, _Mapping]]]=..., install_steps: _Optional[_Iterable[_Union[SoftwareRecipe.Step, _Mapping]]]=..., update_steps: _Optional[_Iterable[_Union[SoftwareRecipe.Step, _Mapping]]]=..., desired_state: _Optional[_Union[DesiredState, str]]=...) -> None:
        ...

class LookupEffectiveGuestPolicyRequest(_message.Message):
    __slots__ = ('instance_id_token', 'os_short_name', 'os_version', 'os_architecture')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OS_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    os_short_name: str
    os_version: str
    os_architecture: str

    def __init__(self, instance_id_token: _Optional[str]=..., os_short_name: _Optional[str]=..., os_version: _Optional[str]=..., os_architecture: _Optional[str]=...) -> None:
        ...

class EffectiveGuestPolicy(_message.Message):
    __slots__ = ('packages', 'package_repositories', 'software_recipes')

    class SourcedPackage(_message.Message):
        __slots__ = ('source', 'package')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_FIELD_NUMBER: _ClassVar[int]
        source: str
        package: Package

        def __init__(self, source: _Optional[str]=..., package: _Optional[_Union[Package, _Mapping]]=...) -> None:
            ...

    class SourcedPackageRepository(_message.Message):
        __slots__ = ('source', 'package_repository')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        source: str
        package_repository: PackageRepository

        def __init__(self, source: _Optional[str]=..., package_repository: _Optional[_Union[PackageRepository, _Mapping]]=...) -> None:
            ...

    class SourcedSoftwareRecipe(_message.Message):
        __slots__ = ('source', 'software_recipe')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_RECIPE_FIELD_NUMBER: _ClassVar[int]
        source: str
        software_recipe: SoftwareRecipe

        def __init__(self, source: _Optional[str]=..., software_recipe: _Optional[_Union[SoftwareRecipe, _Mapping]]=...) -> None:
            ...
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_RECIPES_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedCompositeFieldContainer[EffectiveGuestPolicy.SourcedPackage]
    package_repositories: _containers.RepeatedCompositeFieldContainer[EffectiveGuestPolicy.SourcedPackageRepository]
    software_recipes: _containers.RepeatedCompositeFieldContainer[EffectiveGuestPolicy.SourcedSoftwareRecipe]

    def __init__(self, packages: _Optional[_Iterable[_Union[EffectiveGuestPolicy.SourcedPackage, _Mapping]]]=..., package_repositories: _Optional[_Iterable[_Union[EffectiveGuestPolicy.SourcedPackageRepository, _Mapping]]]=..., software_recipes: _Optional[_Iterable[_Union[EffectiveGuestPolicy.SourcedSoftwareRecipe, _Mapping]]]=...) -> None:
        ...