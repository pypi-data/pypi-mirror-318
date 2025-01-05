from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListTrustConfigsRequest(_message.Message):
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

class ListTrustConfigsResponse(_message.Message):
    __slots__ = ('trust_configs', 'next_page_token', 'unreachable')
    TRUST_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    trust_configs: _containers.RepeatedCompositeFieldContainer[TrustConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, trust_configs: _Optional[_Iterable[_Union[TrustConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetTrustConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTrustConfigRequest(_message.Message):
    __slots__ = ('parent', 'trust_config_id', 'trust_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRUST_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    TRUST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    trust_config_id: str
    trust_config: TrustConfig

    def __init__(self, parent: _Optional[str]=..., trust_config_id: _Optional[str]=..., trust_config: _Optional[_Union[TrustConfig, _Mapping]]=...) -> None:
        ...

class UpdateTrustConfigRequest(_message.Message):
    __slots__ = ('trust_config', 'update_mask')
    TRUST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    trust_config: TrustConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, trust_config: _Optional[_Union[TrustConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTrustConfigRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class TrustConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'etag', 'trust_stores')

    class TrustAnchor(_message.Message):
        __slots__ = ('pem_certificate',)
        PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        pem_certificate: str

        def __init__(self, pem_certificate: _Optional[str]=...) -> None:
            ...

    class IntermediateCA(_message.Message):
        __slots__ = ('pem_certificate',)
        PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        pem_certificate: str

        def __init__(self, pem_certificate: _Optional[str]=...) -> None:
            ...

    class TrustStore(_message.Message):
        __slots__ = ('trust_anchors', 'intermediate_cas')
        TRUST_ANCHORS_FIELD_NUMBER: _ClassVar[int]
        INTERMEDIATE_CAS_FIELD_NUMBER: _ClassVar[int]
        trust_anchors: _containers.RepeatedCompositeFieldContainer[TrustConfig.TrustAnchor]
        intermediate_cas: _containers.RepeatedCompositeFieldContainer[TrustConfig.IntermediateCA]

        def __init__(self, trust_anchors: _Optional[_Iterable[_Union[TrustConfig.TrustAnchor, _Mapping]]]=..., intermediate_cas: _Optional[_Iterable[_Union[TrustConfig.IntermediateCA, _Mapping]]]=...) -> None:
            ...

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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TRUST_STORES_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    etag: str
    trust_stores: _containers.RepeatedCompositeFieldContainer[TrustConfig.TrustStore]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., etag: _Optional[str]=..., trust_stores: _Optional[_Iterable[_Union[TrustConfig.TrustStore, _Mapping]]]=...) -> None:
        ...