from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Lun(_message.Message):
    __slots__ = ('name', 'id', 'state', 'size_gb', 'multiprotocol_type', 'storage_volume', 'shareable', 'boot_lun', 'storage_type', 'wwid', 'expire_time', 'instances')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Lun.State]
        CREATING: _ClassVar[Lun.State]
        UPDATING: _ClassVar[Lun.State]
        READY: _ClassVar[Lun.State]
        DELETING: _ClassVar[Lun.State]
        COOL_OFF: _ClassVar[Lun.State]
    STATE_UNSPECIFIED: Lun.State
    CREATING: Lun.State
    UPDATING: Lun.State
    READY: Lun.State
    DELETING: Lun.State
    COOL_OFF: Lun.State

    class MultiprotocolType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MULTIPROTOCOL_TYPE_UNSPECIFIED: _ClassVar[Lun.MultiprotocolType]
        LINUX: _ClassVar[Lun.MultiprotocolType]
    MULTIPROTOCOL_TYPE_UNSPECIFIED: Lun.MultiprotocolType
    LINUX: Lun.MultiprotocolType

    class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_TYPE_UNSPECIFIED: _ClassVar[Lun.StorageType]
        SSD: _ClassVar[Lun.StorageType]
        HDD: _ClassVar[Lun.StorageType]
    STORAGE_TYPE_UNSPECIFIED: Lun.StorageType
    SSD: Lun.StorageType
    HDD: Lun.StorageType
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MULTIPROTOCOL_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_FIELD_NUMBER: _ClassVar[int]
    BOOT_LUN_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    WWID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    state: Lun.State
    size_gb: int
    multiprotocol_type: Lun.MultiprotocolType
    storage_volume: str
    shareable: bool
    boot_lun: bool
    storage_type: Lun.StorageType
    wwid: str
    expire_time: _timestamp_pb2.Timestamp
    instances: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., state: _Optional[_Union[Lun.State, str]]=..., size_gb: _Optional[int]=..., multiprotocol_type: _Optional[_Union[Lun.MultiprotocolType, str]]=..., storage_volume: _Optional[str]=..., shareable: bool=..., boot_lun: bool=..., storage_type: _Optional[_Union[Lun.StorageType, str]]=..., wwid: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., instances: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetLunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLunsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLunsResponse(_message.Message):
    __slots__ = ('luns', 'next_page_token', 'unreachable')
    LUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    luns: _containers.RepeatedCompositeFieldContainer[Lun]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, luns: _Optional[_Iterable[_Union[Lun, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class EvictLunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...