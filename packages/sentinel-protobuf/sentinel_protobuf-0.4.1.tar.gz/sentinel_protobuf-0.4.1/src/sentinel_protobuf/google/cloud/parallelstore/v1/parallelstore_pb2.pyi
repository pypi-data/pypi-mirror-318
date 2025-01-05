from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_TYPE_UNSPECIFIED: _ClassVar[TransferType]
    IMPORT: _ClassVar[TransferType]
    EXPORT: _ClassVar[TransferType]

class FileStripeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_STRIPE_LEVEL_UNSPECIFIED: _ClassVar[FileStripeLevel]
    FILE_STRIPE_LEVEL_MIN: _ClassVar[FileStripeLevel]
    FILE_STRIPE_LEVEL_BALANCED: _ClassVar[FileStripeLevel]
    FILE_STRIPE_LEVEL_MAX: _ClassVar[FileStripeLevel]

class DirectoryStripeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIRECTORY_STRIPE_LEVEL_UNSPECIFIED: _ClassVar[DirectoryStripeLevel]
    DIRECTORY_STRIPE_LEVEL_MIN: _ClassVar[DirectoryStripeLevel]
    DIRECTORY_STRIPE_LEVEL_BALANCED: _ClassVar[DirectoryStripeLevel]
    DIRECTORY_STRIPE_LEVEL_MAX: _ClassVar[DirectoryStripeLevel]
TRANSFER_TYPE_UNSPECIFIED: TransferType
IMPORT: TransferType
EXPORT: TransferType
FILE_STRIPE_LEVEL_UNSPECIFIED: FileStripeLevel
FILE_STRIPE_LEVEL_MIN: FileStripeLevel
FILE_STRIPE_LEVEL_BALANCED: FileStripeLevel
FILE_STRIPE_LEVEL_MAX: FileStripeLevel
DIRECTORY_STRIPE_LEVEL_UNSPECIFIED: DirectoryStripeLevel
DIRECTORY_STRIPE_LEVEL_MIN: DirectoryStripeLevel
DIRECTORY_STRIPE_LEVEL_BALANCED: DirectoryStripeLevel
DIRECTORY_STRIPE_LEVEL_MAX: DirectoryStripeLevel

class Instance(_message.Message):
    __slots__ = ('name', 'description', 'state', 'create_time', 'update_time', 'labels', 'capacity_gib', 'daos_version', 'access_points', 'network', 'reserved_ip_range', 'effective_reserved_ip_range', 'file_stripe_level', 'directory_stripe_level')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        FAILED: _ClassVar[Instance.State]
        UPGRADING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    DELETING: Instance.State
    FAILED: Instance.State
    UPGRADING: Instance.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GIB_FIELD_NUMBER: _ClassVar[int]
    DAOS_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    FILE_STRIPE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_STRIPE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: Instance.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    capacity_gib: int
    daos_version: str
    access_points: _containers.RepeatedScalarFieldContainer[str]
    network: str
    reserved_ip_range: str
    effective_reserved_ip_range: str
    file_stripe_level: FileStripeLevel
    directory_stripe_level: DirectoryStripeLevel

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Instance.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., capacity_gib: _Optional[int]=..., daos_version: _Optional[str]=..., access_points: _Optional[_Iterable[str]]=..., network: _Optional[str]=..., reserved_ip_range: _Optional[str]=..., effective_reserved_ip_range: _Optional[str]=..., file_stripe_level: _Optional[_Union[FileStripeLevel, str]]=..., directory_stripe_level: _Optional[_Union[DirectoryStripeLevel, str]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    request_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('update_mask', 'instance', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: Instance
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class SourceGcsBucket(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class DestinationGcsBucket(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class SourceParallelstore(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class DestinationParallelstore(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class ImportDataRequest(_message.Message):
    __slots__ = ('source_gcs_bucket', 'destination_parallelstore', 'name', 'request_id', 'service_account')
    SOURCE_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARALLELSTORE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    source_gcs_bucket: SourceGcsBucket
    destination_parallelstore: DestinationParallelstore
    name: str
    request_id: str
    service_account: str

    def __init__(self, source_gcs_bucket: _Optional[_Union[SourceGcsBucket, _Mapping]]=..., destination_parallelstore: _Optional[_Union[DestinationParallelstore, _Mapping]]=..., name: _Optional[str]=..., request_id: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('source_parallelstore', 'destination_gcs_bucket', 'name', 'request_id', 'service_account')
    SOURCE_PARALLELSTORE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    source_parallelstore: SourceParallelstore
    destination_gcs_bucket: DestinationGcsBucket
    name: str
    request_id: str
    service_account: str

    def __init__(self, source_parallelstore: _Optional[_Union[SourceParallelstore, _Mapping]]=..., destination_gcs_bucket: _Optional[_Union[DestinationGcsBucket, _Mapping]]=..., name: _Optional[str]=..., request_id: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class ImportDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportDataMetadata(_message.Message):
    __slots__ = ('operation_metadata', 'create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: TransferOperationMetadata
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, operation_metadata: _Optional[_Union[TransferOperationMetadata, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class ExportDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExportDataMetadata(_message.Message):
    __slots__ = ('operation_metadata', 'create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: TransferOperationMetadata
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, operation_metadata: _Optional[_Union[TransferOperationMetadata, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class TransferOperationMetadata(_message.Message):
    __slots__ = ('source_parallelstore', 'source_gcs_bucket', 'destination_gcs_bucket', 'destination_parallelstore', 'counters', 'transfer_type')
    SOURCE_PARALLELSTORE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARALLELSTORE_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    source_parallelstore: SourceParallelstore
    source_gcs_bucket: SourceGcsBucket
    destination_gcs_bucket: DestinationGcsBucket
    destination_parallelstore: DestinationParallelstore
    counters: TransferCounters
    transfer_type: TransferType

    def __init__(self, source_parallelstore: _Optional[_Union[SourceParallelstore, _Mapping]]=..., source_gcs_bucket: _Optional[_Union[SourceGcsBucket, _Mapping]]=..., destination_gcs_bucket: _Optional[_Union[DestinationGcsBucket, _Mapping]]=..., destination_parallelstore: _Optional[_Union[DestinationParallelstore, _Mapping]]=..., counters: _Optional[_Union[TransferCounters, _Mapping]]=..., transfer_type: _Optional[_Union[TransferType, str]]=...) -> None:
        ...

class TransferCounters(_message.Message):
    __slots__ = ('objects_found', 'bytes_found', 'objects_skipped', 'bytes_skipped', 'objects_copied', 'bytes_copied')
    OBJECTS_FOUND_FIELD_NUMBER: _ClassVar[int]
    BYTES_FOUND_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    BYTES_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_COPIED_FIELD_NUMBER: _ClassVar[int]
    BYTES_COPIED_FIELD_NUMBER: _ClassVar[int]
    objects_found: int
    bytes_found: int
    objects_skipped: int
    bytes_skipped: int
    objects_copied: int
    bytes_copied: int

    def __init__(self, objects_found: _Optional[int]=..., bytes_found: _Optional[int]=..., objects_skipped: _Optional[int]=..., bytes_skipped: _Optional[int]=..., objects_copied: _Optional[int]=..., bytes_copied: _Optional[int]=...) -> None:
        ...