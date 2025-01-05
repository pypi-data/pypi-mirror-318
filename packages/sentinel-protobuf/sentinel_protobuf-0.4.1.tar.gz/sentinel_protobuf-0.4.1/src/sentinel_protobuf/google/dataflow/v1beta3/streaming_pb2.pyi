from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TopologyConfig(_message.Message):
    __slots__ = ('computations', 'data_disk_assignments', 'user_stage_to_computation_name_map', 'forwarding_key_bits', 'persistent_state_version')

    class UserStageToComputationNameMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COMPUTATIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    USER_STAGE_TO_COMPUTATION_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_KEY_BITS_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_STATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    computations: _containers.RepeatedCompositeFieldContainer[ComputationTopology]
    data_disk_assignments: _containers.RepeatedCompositeFieldContainer[DataDiskAssignment]
    user_stage_to_computation_name_map: _containers.ScalarMap[str, str]
    forwarding_key_bits: int
    persistent_state_version: int

    def __init__(self, computations: _Optional[_Iterable[_Union[ComputationTopology, _Mapping]]]=..., data_disk_assignments: _Optional[_Iterable[_Union[DataDiskAssignment, _Mapping]]]=..., user_stage_to_computation_name_map: _Optional[_Mapping[str, str]]=..., forwarding_key_bits: _Optional[int]=..., persistent_state_version: _Optional[int]=...) -> None:
        ...

class PubsubLocation(_message.Message):
    __slots__ = ('topic', 'subscription', 'timestamp_label', 'id_label', 'drop_late_data', 'tracking_subscription', 'with_attributes')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_LABEL_FIELD_NUMBER: _ClassVar[int]
    ID_LABEL_FIELD_NUMBER: _ClassVar[int]
    DROP_LATE_DATA_FIELD_NUMBER: _ClassVar[int]
    TRACKING_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WITH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    topic: str
    subscription: str
    timestamp_label: str
    id_label: str
    drop_late_data: bool
    tracking_subscription: str
    with_attributes: bool

    def __init__(self, topic: _Optional[str]=..., subscription: _Optional[str]=..., timestamp_label: _Optional[str]=..., id_label: _Optional[str]=..., drop_late_data: bool=..., tracking_subscription: _Optional[str]=..., with_attributes: bool=...) -> None:
        ...

class StreamingStageLocation(_message.Message):
    __slots__ = ('stream_id',)
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    stream_id: str

    def __init__(self, stream_id: _Optional[str]=...) -> None:
        ...

class StreamingSideInputLocation(_message.Message):
    __slots__ = ('tag', 'state_family')
    TAG_FIELD_NUMBER: _ClassVar[int]
    STATE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    tag: str
    state_family: str

    def __init__(self, tag: _Optional[str]=..., state_family: _Optional[str]=...) -> None:
        ...

class CustomSourceLocation(_message.Message):
    __slots__ = ('stateful',)
    STATEFUL_FIELD_NUMBER: _ClassVar[int]
    stateful: bool

    def __init__(self, stateful: bool=...) -> None:
        ...

class StreamLocation(_message.Message):
    __slots__ = ('streaming_stage_location', 'pubsub_location', 'side_input_location', 'custom_source_location')
    STREAMING_STAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SIDE_INPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    streaming_stage_location: StreamingStageLocation
    pubsub_location: PubsubLocation
    side_input_location: StreamingSideInputLocation
    custom_source_location: CustomSourceLocation

    def __init__(self, streaming_stage_location: _Optional[_Union[StreamingStageLocation, _Mapping]]=..., pubsub_location: _Optional[_Union[PubsubLocation, _Mapping]]=..., side_input_location: _Optional[_Union[StreamingSideInputLocation, _Mapping]]=..., custom_source_location: _Optional[_Union[CustomSourceLocation, _Mapping]]=...) -> None:
        ...

class StateFamilyConfig(_message.Message):
    __slots__ = ('state_family', 'is_read')
    STATE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    state_family: str
    is_read: bool

    def __init__(self, state_family: _Optional[str]=..., is_read: bool=...) -> None:
        ...

class ComputationTopology(_message.Message):
    __slots__ = ('system_stage_name', 'computation_id', 'key_ranges', 'inputs', 'outputs', 'state_families')
    SYSTEM_STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_RANGES_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    system_stage_name: str
    computation_id: str
    key_ranges: _containers.RepeatedCompositeFieldContainer[KeyRangeLocation]
    inputs: _containers.RepeatedCompositeFieldContainer[StreamLocation]
    outputs: _containers.RepeatedCompositeFieldContainer[StreamLocation]
    state_families: _containers.RepeatedCompositeFieldContainer[StateFamilyConfig]

    def __init__(self, system_stage_name: _Optional[str]=..., computation_id: _Optional[str]=..., key_ranges: _Optional[_Iterable[_Union[KeyRangeLocation, _Mapping]]]=..., inputs: _Optional[_Iterable[_Union[StreamLocation, _Mapping]]]=..., outputs: _Optional[_Iterable[_Union[StreamLocation, _Mapping]]]=..., state_families: _Optional[_Iterable[_Union[StateFamilyConfig, _Mapping]]]=...) -> None:
        ...

class KeyRangeLocation(_message.Message):
    __slots__ = ('start', 'end', 'delivery_endpoint', 'data_disk', 'deprecated_persistent_directory')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PERSISTENT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    start: str
    end: str
    delivery_endpoint: str
    data_disk: str
    deprecated_persistent_directory: str

    def __init__(self, start: _Optional[str]=..., end: _Optional[str]=..., delivery_endpoint: _Optional[str]=..., data_disk: _Optional[str]=..., deprecated_persistent_directory: _Optional[str]=...) -> None:
        ...

class MountedDataDisk(_message.Message):
    __slots__ = ('data_disk',)
    DATA_DISK_FIELD_NUMBER: _ClassVar[int]
    data_disk: str

    def __init__(self, data_disk: _Optional[str]=...) -> None:
        ...

class DataDiskAssignment(_message.Message):
    __slots__ = ('vm_instance', 'data_disks')
    VM_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
    vm_instance: str
    data_disks: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vm_instance: _Optional[str]=..., data_disks: _Optional[_Iterable[str]]=...) -> None:
        ...

class KeyRangeDataDiskAssignment(_message.Message):
    __slots__ = ('start', 'end', 'data_disk')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_FIELD_NUMBER: _ClassVar[int]
    start: str
    end: str
    data_disk: str

    def __init__(self, start: _Optional[str]=..., end: _Optional[str]=..., data_disk: _Optional[str]=...) -> None:
        ...

class StreamingComputationRanges(_message.Message):
    __slots__ = ('computation_id', 'range_assignments')
    COMPUTATION_ID_FIELD_NUMBER: _ClassVar[int]
    RANGE_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    computation_id: str
    range_assignments: _containers.RepeatedCompositeFieldContainer[KeyRangeDataDiskAssignment]

    def __init__(self, computation_id: _Optional[str]=..., range_assignments: _Optional[_Iterable[_Union[KeyRangeDataDiskAssignment, _Mapping]]]=...) -> None:
        ...

class StreamingApplianceSnapshotConfig(_message.Message):
    __slots__ = ('snapshot_id', 'import_state_endpoint')
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_STATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: str
    import_state_endpoint: str

    def __init__(self, snapshot_id: _Optional[str]=..., import_state_endpoint: _Optional[str]=...) -> None:
        ...