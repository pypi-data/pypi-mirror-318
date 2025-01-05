from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GuestOsScan(_message.Message):
    __slots__ = ('core_source',)
    CORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    core_source: str

    def __init__(self, core_source: _Optional[str]=...) -> None:
        ...

class VSphereScan(_message.Message):
    __slots__ = ('core_source',)
    CORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    core_source: str

    def __init__(self, core_source: _Optional[str]=...) -> None:
        ...

class Collector(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'description', 'service_account', 'bucket', 'expected_asset_count', 'state', 'client_version', 'guest_os_scan', 'vsphere_scan', 'collection_days', 'eula_uri')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Collector.State]
        STATE_INITIALIZING: _ClassVar[Collector.State]
        STATE_READY_TO_USE: _ClassVar[Collector.State]
        STATE_REGISTERED: _ClassVar[Collector.State]
        STATE_ACTIVE: _ClassVar[Collector.State]
        STATE_PAUSED: _ClassVar[Collector.State]
        STATE_DELETING: _ClassVar[Collector.State]
        STATE_DECOMMISSIONED: _ClassVar[Collector.State]
        STATE_ERROR: _ClassVar[Collector.State]
    STATE_UNSPECIFIED: Collector.State
    STATE_INITIALIZING: Collector.State
    STATE_READY_TO_USE: Collector.State
    STATE_REGISTERED: Collector.State
    STATE_ACTIVE: Collector.State
    STATE_PAUSED: Collector.State
    STATE_DELETING: Collector.State
    STATE_DECOMMISSIONED: Collector.State
    STATE_ERROR: Collector.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_SCAN_FIELD_NUMBER: _ClassVar[int]
    VSPHERE_SCAN_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    EULA_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str
    service_account: str
    bucket: str
    expected_asset_count: int
    state: Collector.State
    client_version: str
    guest_os_scan: GuestOsScan
    vsphere_scan: VSphereScan
    collection_days: int
    eula_uri: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., service_account: _Optional[str]=..., bucket: _Optional[str]=..., expected_asset_count: _Optional[int]=..., state: _Optional[_Union[Collector.State, str]]=..., client_version: _Optional[str]=..., guest_os_scan: _Optional[_Union[GuestOsScan, _Mapping]]=..., vsphere_scan: _Optional[_Union[VSphereScan, _Mapping]]=..., collection_days: _Optional[int]=..., eula_uri: _Optional[str]=...) -> None:
        ...

class Annotation(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Annotation.Type]
        TYPE_LEGACY_EXPORT_CONSENT: _ClassVar[Annotation.Type]
        TYPE_QWIKLAB: _ClassVar[Annotation.Type]
    TYPE_UNSPECIFIED: Annotation.Type
    TYPE_LEGACY_EXPORT_CONSENT: Annotation.Type
    TYPE_QWIKLAB: Annotation.Type

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    type: Annotation.Type

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., type: _Optional[_Union[Annotation.Type, str]]=...) -> None:
        ...