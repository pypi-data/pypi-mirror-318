from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.metastore.v1alpha import metastore_pb2 as _metastore_pb2
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

class Federation(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'version', 'backend_metastores', 'endpoint_uri', 'state', 'state_message', 'uid')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Federation.State]
        CREATING: _ClassVar[Federation.State]
        ACTIVE: _ClassVar[Federation.State]
        UPDATING: _ClassVar[Federation.State]
        DELETING: _ClassVar[Federation.State]
        ERROR: _ClassVar[Federation.State]
    STATE_UNSPECIFIED: Federation.State
    CREATING: Federation.State
    ACTIVE: Federation.State
    UPDATING: Federation.State
    DELETING: Federation.State
    ERROR: Federation.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class BackendMetastoresEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BackendMetastore

        def __init__(self, key: _Optional[int]=..., value: _Optional[_Union[BackendMetastore, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BACKEND_METASTORES_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    version: str
    backend_metastores: _containers.MessageMap[int, BackendMetastore]
    endpoint_uri: str
    state: Federation.State
    state_message: str
    uid: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., version: _Optional[str]=..., backend_metastores: _Optional[_Mapping[int, BackendMetastore]]=..., endpoint_uri: _Optional[str]=..., state: _Optional[_Union[Federation.State, str]]=..., state_message: _Optional[str]=..., uid: _Optional[str]=...) -> None:
        ...

class BackendMetastore(_message.Message):
    __slots__ = ('name', 'metastore_type')

    class MetastoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METASTORE_TYPE_UNSPECIFIED: _ClassVar[BackendMetastore.MetastoreType]
        DATAPLEX: _ClassVar[BackendMetastore.MetastoreType]
        BIGQUERY: _ClassVar[BackendMetastore.MetastoreType]
        DATAPROC_METASTORE: _ClassVar[BackendMetastore.MetastoreType]
    METASTORE_TYPE_UNSPECIFIED: BackendMetastore.MetastoreType
    DATAPLEX: BackendMetastore.MetastoreType
    BIGQUERY: BackendMetastore.MetastoreType
    DATAPROC_METASTORE: BackendMetastore.MetastoreType
    NAME_FIELD_NUMBER: _ClassVar[int]
    METASTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    metastore_type: BackendMetastore.MetastoreType

    def __init__(self, name: _Optional[str]=..., metastore_type: _Optional[_Union[BackendMetastore.MetastoreType, str]]=...) -> None:
        ...

class ListFederationsRequest(_message.Message):
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

class ListFederationsResponse(_message.Message):
    __slots__ = ('federations', 'next_page_token', 'unreachable')
    FEDERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    federations: _containers.RepeatedCompositeFieldContainer[Federation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, federations: _Optional[_Iterable[_Union[Federation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetFederationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateFederationRequest(_message.Message):
    __slots__ = ('parent', 'federation_id', 'federation', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    FEDERATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    federation_id: str
    federation: Federation
    request_id: str

    def __init__(self, parent: _Optional[str]=..., federation_id: _Optional[str]=..., federation: _Optional[_Union[Federation, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateFederationRequest(_message.Message):
    __slots__ = ('update_mask', 'federation', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    FEDERATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    federation: Federation
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., federation: _Optional[_Union[Federation, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteFederationRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...