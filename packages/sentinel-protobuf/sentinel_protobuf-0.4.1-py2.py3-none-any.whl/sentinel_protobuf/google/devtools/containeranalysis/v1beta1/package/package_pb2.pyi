from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Architecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARCHITECTURE_UNSPECIFIED: _ClassVar[Architecture]
    X86: _ClassVar[Architecture]
    X64: _ClassVar[Architecture]
ARCHITECTURE_UNSPECIFIED: Architecture
X86: Architecture
X64: Architecture

class Distribution(_message.Message):
    __slots__ = ('cpe_uri', 'architecture', 'latest_version', 'maintainer', 'url', 'description')
    CPE_URI_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAINTAINER_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    cpe_uri: str
    architecture: Architecture
    latest_version: Version
    maintainer: str
    url: str
    description: str

    def __init__(self, cpe_uri: _Optional[str]=..., architecture: _Optional[_Union[Architecture, str]]=..., latest_version: _Optional[_Union[Version, _Mapping]]=..., maintainer: _Optional[str]=..., url: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class Location(_message.Message):
    __slots__ = ('cpe_uri', 'version', 'path')
    CPE_URI_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    cpe_uri: str
    version: Version
    path: str

    def __init__(self, cpe_uri: _Optional[str]=..., version: _Optional[_Union[Version, _Mapping]]=..., path: _Optional[str]=...) -> None:
        ...

class Package(_message.Message):
    __slots__ = ('name', 'distribution')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    distribution: _containers.RepeatedCompositeFieldContainer[Distribution]

    def __init__(self, name: _Optional[str]=..., distribution: _Optional[_Iterable[_Union[Distribution, _Mapping]]]=...) -> None:
        ...

class Details(_message.Message):
    __slots__ = ('installation',)
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    installation: Installation

    def __init__(self, installation: _Optional[_Union[Installation, _Mapping]]=...) -> None:
        ...

class Installation(_message.Message):
    __slots__ = ('name', 'location')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: _containers.RepeatedCompositeFieldContainer[Location]

    def __init__(self, name: _Optional[str]=..., location: _Optional[_Iterable[_Union[Location, _Mapping]]]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('epoch', 'name', 'revision', 'kind')

    class VersionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_KIND_UNSPECIFIED: _ClassVar[Version.VersionKind]
        NORMAL: _ClassVar[Version.VersionKind]
        MINIMUM: _ClassVar[Version.VersionKind]
        MAXIMUM: _ClassVar[Version.VersionKind]
    VERSION_KIND_UNSPECIFIED: Version.VersionKind
    NORMAL: Version.VersionKind
    MINIMUM: Version.VersionKind
    MAXIMUM: Version.VersionKind
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    name: str
    revision: str
    kind: Version.VersionKind

    def __init__(self, epoch: _Optional[int]=..., name: _Optional[str]=..., revision: _Optional[str]=..., kind: _Optional[_Union[Version.VersionKind, str]]=...) -> None:
        ...