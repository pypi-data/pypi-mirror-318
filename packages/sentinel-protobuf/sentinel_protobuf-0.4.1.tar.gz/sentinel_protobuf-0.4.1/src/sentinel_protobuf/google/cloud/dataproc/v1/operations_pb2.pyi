from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BatchOperationMetadata(_message.Message):
    __slots__ = ('batch', 'batch_uuid', 'create_time', 'done_time', 'operation_type', 'description', 'labels', 'warnings')

    class BatchOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BATCH_OPERATION_TYPE_UNSPECIFIED: _ClassVar[BatchOperationMetadata.BatchOperationType]
        BATCH: _ClassVar[BatchOperationMetadata.BatchOperationType]
    BATCH_OPERATION_TYPE_UNSPECIFIED: BatchOperationMetadata.BatchOperationType
    BATCH: BatchOperationMetadata.BatchOperationType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BATCH_FIELD_NUMBER: _ClassVar[int]
    BATCH_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DONE_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    batch: str
    batch_uuid: str
    create_time: _timestamp_pb2.Timestamp
    done_time: _timestamp_pb2.Timestamp
    operation_type: BatchOperationMetadata.BatchOperationType
    description: str
    labels: _containers.ScalarMap[str, str]
    warnings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, batch: _Optional[str]=..., batch_uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., done_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation_type: _Optional[_Union[BatchOperationMetadata.BatchOperationType, str]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
        ...

class SessionOperationMetadata(_message.Message):
    __slots__ = ('session', 'session_uuid', 'create_time', 'done_time', 'operation_type', 'description', 'labels', 'warnings')

    class SessionOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SESSION_OPERATION_TYPE_UNSPECIFIED: _ClassVar[SessionOperationMetadata.SessionOperationType]
        CREATE: _ClassVar[SessionOperationMetadata.SessionOperationType]
        TERMINATE: _ClassVar[SessionOperationMetadata.SessionOperationType]
        DELETE: _ClassVar[SessionOperationMetadata.SessionOperationType]
    SESSION_OPERATION_TYPE_UNSPECIFIED: SessionOperationMetadata.SessionOperationType
    CREATE: SessionOperationMetadata.SessionOperationType
    TERMINATE: SessionOperationMetadata.SessionOperationType
    DELETE: SessionOperationMetadata.SessionOperationType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DONE_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    session: str
    session_uuid: str
    create_time: _timestamp_pb2.Timestamp
    done_time: _timestamp_pb2.Timestamp
    operation_type: SessionOperationMetadata.SessionOperationType
    description: str
    labels: _containers.ScalarMap[str, str]
    warnings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, session: _Optional[str]=..., session_uuid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., done_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operation_type: _Optional[_Union[SessionOperationMetadata.SessionOperationType, str]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
        ...

class ClusterOperationStatus(_message.Message):
    __slots__ = ('state', 'inner_state', 'details', 'state_start_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ClusterOperationStatus.State]
        PENDING: _ClassVar[ClusterOperationStatus.State]
        RUNNING: _ClassVar[ClusterOperationStatus.State]
        DONE: _ClassVar[ClusterOperationStatus.State]
    UNKNOWN: ClusterOperationStatus.State
    PENDING: ClusterOperationStatus.State
    RUNNING: ClusterOperationStatus.State
    DONE: ClusterOperationStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    INNER_STATE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    state: ClusterOperationStatus.State
    inner_state: str
    details: str
    state_start_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[ClusterOperationStatus.State, str]]=..., inner_state: _Optional[str]=..., details: _Optional[str]=..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ClusterOperationMetadata(_message.Message):
    __slots__ = ('cluster_name', 'cluster_uuid', 'status', 'status_history', 'operation_type', 'description', 'labels', 'warnings', 'child_operation_ids')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    CHILD_OPERATION_IDS_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    cluster_uuid: str
    status: ClusterOperationStatus
    status_history: _containers.RepeatedCompositeFieldContainer[ClusterOperationStatus]
    operation_type: str
    description: str
    labels: _containers.ScalarMap[str, str]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    child_operation_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cluster_name: _Optional[str]=..., cluster_uuid: _Optional[str]=..., status: _Optional[_Union[ClusterOperationStatus, _Mapping]]=..., status_history: _Optional[_Iterable[_Union[ClusterOperationStatus, _Mapping]]]=..., operation_type: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., warnings: _Optional[_Iterable[str]]=..., child_operation_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class NodeGroupOperationMetadata(_message.Message):
    __slots__ = ('node_group_id', 'cluster_uuid', 'status', 'status_history', 'operation_type', 'description', 'labels', 'warnings')

    class NodeGroupOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_GROUP_OPERATION_TYPE_UNSPECIFIED: _ClassVar[NodeGroupOperationMetadata.NodeGroupOperationType]
        CREATE: _ClassVar[NodeGroupOperationMetadata.NodeGroupOperationType]
        UPDATE: _ClassVar[NodeGroupOperationMetadata.NodeGroupOperationType]
        DELETE: _ClassVar[NodeGroupOperationMetadata.NodeGroupOperationType]
        RESIZE: _ClassVar[NodeGroupOperationMetadata.NodeGroupOperationType]
    NODE_GROUP_OPERATION_TYPE_UNSPECIFIED: NodeGroupOperationMetadata.NodeGroupOperationType
    CREATE: NodeGroupOperationMetadata.NodeGroupOperationType
    UPDATE: NodeGroupOperationMetadata.NodeGroupOperationType
    DELETE: NodeGroupOperationMetadata.NodeGroupOperationType
    RESIZE: NodeGroupOperationMetadata.NodeGroupOperationType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NODE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    node_group_id: str
    cluster_uuid: str
    status: ClusterOperationStatus
    status_history: _containers.RepeatedCompositeFieldContainer[ClusterOperationStatus]
    operation_type: NodeGroupOperationMetadata.NodeGroupOperationType
    description: str
    labels: _containers.ScalarMap[str, str]
    warnings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, node_group_id: _Optional[str]=..., cluster_uuid: _Optional[str]=..., status: _Optional[_Union[ClusterOperationStatus, _Mapping]]=..., status_history: _Optional[_Iterable[_Union[ClusterOperationStatus, _Mapping]]]=..., operation_type: _Optional[_Union[NodeGroupOperationMetadata.NodeGroupOperationType, str]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., warnings: _Optional[_Iterable[str]]=...) -> None:
        ...