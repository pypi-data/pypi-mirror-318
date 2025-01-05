from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PatchConfig(_message.Message):
    __slots__ = ('reboot_config', 'retry_strategy', 'apt', 'yum', 'goo', 'zypper', 'windows_update', 'pre_step', 'post_step', 'mig_instances_allowed')

    class RebootConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REBOOT_CONFIG_UNSPECIFIED: _ClassVar[PatchConfig.RebootConfig]
        DEFAULT: _ClassVar[PatchConfig.RebootConfig]
        ALWAYS: _ClassVar[PatchConfig.RebootConfig]
        NEVER: _ClassVar[PatchConfig.RebootConfig]
    REBOOT_CONFIG_UNSPECIFIED: PatchConfig.RebootConfig
    DEFAULT: PatchConfig.RebootConfig
    ALWAYS: PatchConfig.RebootConfig
    NEVER: PatchConfig.RebootConfig
    REBOOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETRY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    APT_FIELD_NUMBER: _ClassVar[int]
    YUM_FIELD_NUMBER: _ClassVar[int]
    GOO_FIELD_NUMBER: _ClassVar[int]
    ZYPPER_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PRE_STEP_FIELD_NUMBER: _ClassVar[int]
    POST_STEP_FIELD_NUMBER: _ClassVar[int]
    MIG_INSTANCES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    reboot_config: PatchConfig.RebootConfig
    retry_strategy: RetryStrategy
    apt: AptSettings
    yum: YumSettings
    goo: GooSettings
    zypper: ZypperSettings
    windows_update: WindowsUpdateSettings
    pre_step: ExecStep
    post_step: ExecStep
    mig_instances_allowed: bool

    def __init__(self, reboot_config: _Optional[_Union[PatchConfig.RebootConfig, str]]=..., retry_strategy: _Optional[_Union[RetryStrategy, _Mapping]]=..., apt: _Optional[_Union[AptSettings, _Mapping]]=..., yum: _Optional[_Union[YumSettings, _Mapping]]=..., goo: _Optional[_Union[GooSettings, _Mapping]]=..., zypper: _Optional[_Union[ZypperSettings, _Mapping]]=..., windows_update: _Optional[_Union[WindowsUpdateSettings, _Mapping]]=..., pre_step: _Optional[_Union[ExecStep, _Mapping]]=..., post_step: _Optional[_Union[ExecStep, _Mapping]]=..., mig_instances_allowed: bool=...) -> None:
        ...

class AptSettings(_message.Message):
    __slots__ = ('type', 'excludes', 'exclusive_packages')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AptSettings.Type]
        DIST: _ClassVar[AptSettings.Type]
        UPGRADE: _ClassVar[AptSettings.Type]
    TYPE_UNSPECIFIED: AptSettings.Type
    DIST: AptSettings.Type
    UPGRADE: AptSettings.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    type: AptSettings.Type
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_packages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[AptSettings.Type, str]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_packages: _Optional[_Iterable[str]]=...) -> None:
        ...

class YumSettings(_message.Message):
    __slots__ = ('security', 'minimal', 'excludes', 'exclusive_packages')
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    security: bool
    minimal: bool
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_packages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, security: bool=..., minimal: bool=..., excludes: _Optional[_Iterable[str]]=..., exclusive_packages: _Optional[_Iterable[str]]=...) -> None:
        ...

class GooSettings(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ZypperSettings(_message.Message):
    __slots__ = ('with_optional', 'with_update', 'categories', 'severities', 'excludes', 'exclusive_patches')
    WITH_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    WITH_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SEVERITIES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    with_optional: bool
    with_update: bool
    categories: _containers.RepeatedScalarFieldContainer[str]
    severities: _containers.RepeatedScalarFieldContainer[str]
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_patches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, with_optional: bool=..., with_update: bool=..., categories: _Optional[_Iterable[str]]=..., severities: _Optional[_Iterable[str]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_patches: _Optional[_Iterable[str]]=...) -> None:
        ...

class WindowsUpdateSettings(_message.Message):
    __slots__ = ('classifications', 'excludes', 'exclusive_patches')

    class Classification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASSIFICATION_UNSPECIFIED: _ClassVar[WindowsUpdateSettings.Classification]
        CRITICAL: _ClassVar[WindowsUpdateSettings.Classification]
        SECURITY: _ClassVar[WindowsUpdateSettings.Classification]
        DEFINITION: _ClassVar[WindowsUpdateSettings.Classification]
        DRIVER: _ClassVar[WindowsUpdateSettings.Classification]
        FEATURE_PACK: _ClassVar[WindowsUpdateSettings.Classification]
        SERVICE_PACK: _ClassVar[WindowsUpdateSettings.Classification]
        TOOL: _ClassVar[WindowsUpdateSettings.Classification]
        UPDATE_ROLLUP: _ClassVar[WindowsUpdateSettings.Classification]
        UPDATE: _ClassVar[WindowsUpdateSettings.Classification]
    CLASSIFICATION_UNSPECIFIED: WindowsUpdateSettings.Classification
    CRITICAL: WindowsUpdateSettings.Classification
    SECURITY: WindowsUpdateSettings.Classification
    DEFINITION: WindowsUpdateSettings.Classification
    DRIVER: WindowsUpdateSettings.Classification
    FEATURE_PACK: WindowsUpdateSettings.Classification
    SERVICE_PACK: WindowsUpdateSettings.Classification
    TOOL: WindowsUpdateSettings.Classification
    UPDATE_ROLLUP: WindowsUpdateSettings.Classification
    UPDATE: WindowsUpdateSettings.Classification
    CLASSIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    classifications: _containers.RepeatedScalarFieldContainer[WindowsUpdateSettings.Classification]
    excludes: _containers.RepeatedScalarFieldContainer[str]
    exclusive_patches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, classifications: _Optional[_Iterable[_Union[WindowsUpdateSettings.Classification, str]]]=..., excludes: _Optional[_Iterable[str]]=..., exclusive_patches: _Optional[_Iterable[str]]=...) -> None:
        ...

class RetryStrategy(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class ExecStep(_message.Message):
    __slots__ = ('linux_exec_step_config', 'windows_exec_step_config')
    LINUX_EXEC_STEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_EXEC_STEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    linux_exec_step_config: ExecStepConfig
    windows_exec_step_config: ExecStepConfig

    def __init__(self, linux_exec_step_config: _Optional[_Union[ExecStepConfig, _Mapping]]=..., windows_exec_step_config: _Optional[_Union[ExecStepConfig, _Mapping]]=...) -> None:
        ...

class ExecStepConfig(_message.Message):
    __slots__ = ('local_path', 'gcs_object', 'allowed_success_codes', 'interpreter')

    class Interpreter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERPRETER_UNSPECIFIED: _ClassVar[ExecStepConfig.Interpreter]
        NONE: _ClassVar[ExecStepConfig.Interpreter]
        SHELL: _ClassVar[ExecStepConfig.Interpreter]
        POWERSHELL: _ClassVar[ExecStepConfig.Interpreter]
    INTERPRETER_UNSPECIFIED: ExecStepConfig.Interpreter
    NONE: ExecStepConfig.Interpreter
    SHELL: ExecStepConfig.Interpreter
    POWERSHELL: ExecStepConfig.Interpreter
    LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SUCCESS_CODES_FIELD_NUMBER: _ClassVar[int]
    INTERPRETER_FIELD_NUMBER: _ClassVar[int]
    local_path: str
    gcs_object: GcsObject
    allowed_success_codes: _containers.RepeatedScalarFieldContainer[int]
    interpreter: ExecStepConfig.Interpreter

    def __init__(self, local_path: _Optional[str]=..., gcs_object: _Optional[_Union[GcsObject, _Mapping]]=..., allowed_success_codes: _Optional[_Iterable[int]]=..., interpreter: _Optional[_Union[ExecStepConfig.Interpreter, str]]=...) -> None:
        ...

class GcsObject(_message.Message):
    __slots__ = ('bucket', 'object', 'generation_number')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation_number: int

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation_number: _Optional[int]=...) -> None:
        ...