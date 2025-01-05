from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import feature_selector_pb2 as _feature_selector_pb2
from google.cloud.aiplatform.v1 import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WriteFeatureValuesRequest(_message.Message):
    __slots__ = ('entity_type', 'payloads')
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    entity_type: str
    payloads: _containers.RepeatedCompositeFieldContainer[WriteFeatureValuesPayload]

    def __init__(self, entity_type: _Optional[str]=..., payloads: _Optional[_Iterable[_Union[WriteFeatureValuesPayload, _Mapping]]]=...) -> None:
        ...

class WriteFeatureValuesPayload(_message.Message):
    __slots__ = ('entity_id', 'feature_values')

    class FeatureValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FeatureValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FeatureValue, _Mapping]]=...) -> None:
            ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VALUES_FIELD_NUMBER: _ClassVar[int]
    entity_id: str
    feature_values: _containers.MessageMap[str, FeatureValue]

    def __init__(self, entity_id: _Optional[str]=..., feature_values: _Optional[_Mapping[str, FeatureValue]]=...) -> None:
        ...

class WriteFeatureValuesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReadFeatureValuesRequest(_message.Message):
    __slots__ = ('entity_type', 'entity_id', 'feature_selector')
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    entity_type: str
    entity_id: str
    feature_selector: _feature_selector_pb2.FeatureSelector

    def __init__(self, entity_type: _Optional[str]=..., entity_id: _Optional[str]=..., feature_selector: _Optional[_Union[_feature_selector_pb2.FeatureSelector, _Mapping]]=...) -> None:
        ...

class ReadFeatureValuesResponse(_message.Message):
    __slots__ = ('header', 'entity_view')

    class FeatureDescriptor(_message.Message):
        __slots__ = ('id',)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str

        def __init__(self, id: _Optional[str]=...) -> None:
            ...

    class Header(_message.Message):
        __slots__ = ('entity_type', 'feature_descriptors')
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        FEATURE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
        entity_type: str
        feature_descriptors: _containers.RepeatedCompositeFieldContainer[ReadFeatureValuesResponse.FeatureDescriptor]

        def __init__(self, entity_type: _Optional[str]=..., feature_descriptors: _Optional[_Iterable[_Union[ReadFeatureValuesResponse.FeatureDescriptor, _Mapping]]]=...) -> None:
            ...

    class EntityView(_message.Message):
        __slots__ = ('entity_id', 'data')

        class Data(_message.Message):
            __slots__ = ('value', 'values')
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            value: FeatureValue
            values: FeatureValueList

            def __init__(self, value: _Optional[_Union[FeatureValue, _Mapping]]=..., values: _Optional[_Union[FeatureValueList, _Mapping]]=...) -> None:
                ...
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        data: _containers.RepeatedCompositeFieldContainer[ReadFeatureValuesResponse.EntityView.Data]

        def __init__(self, entity_id: _Optional[str]=..., data: _Optional[_Iterable[_Union[ReadFeatureValuesResponse.EntityView.Data, _Mapping]]]=...) -> None:
            ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VIEW_FIELD_NUMBER: _ClassVar[int]
    header: ReadFeatureValuesResponse.Header
    entity_view: ReadFeatureValuesResponse.EntityView

    def __init__(self, header: _Optional[_Union[ReadFeatureValuesResponse.Header, _Mapping]]=..., entity_view: _Optional[_Union[ReadFeatureValuesResponse.EntityView, _Mapping]]=...) -> None:
        ...

class StreamingReadFeatureValuesRequest(_message.Message):
    __slots__ = ('entity_type', 'entity_ids', 'feature_selector')
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    entity_type: str
    entity_ids: _containers.RepeatedScalarFieldContainer[str]
    feature_selector: _feature_selector_pb2.FeatureSelector

    def __init__(self, entity_type: _Optional[str]=..., entity_ids: _Optional[_Iterable[str]]=..., feature_selector: _Optional[_Union[_feature_selector_pb2.FeatureSelector, _Mapping]]=...) -> None:
        ...

class FeatureValue(_message.Message):
    __slots__ = ('bool_value', 'double_value', 'int64_value', 'string_value', 'bool_array_value', 'double_array_value', 'int64_array_value', 'string_array_value', 'bytes_value', 'struct_value', 'metadata')

    class Metadata(_message.Message):
        __slots__ = ('generate_time',)
        GENERATE_TIME_FIELD_NUMBER: _ClassVar[int]
        generate_time: _timestamp_pb2.Timestamp

        def __init__(self, generate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    double_value: float
    int64_value: int
    string_value: str
    bool_array_value: _types_pb2.BoolArray
    double_array_value: _types_pb2.DoubleArray
    int64_array_value: _types_pb2.Int64Array
    string_array_value: _types_pb2.StringArray
    bytes_value: bytes
    struct_value: StructValue
    metadata: FeatureValue.Metadata

    def __init__(self, bool_value: bool=..., double_value: _Optional[float]=..., int64_value: _Optional[int]=..., string_value: _Optional[str]=..., bool_array_value: _Optional[_Union[_types_pb2.BoolArray, _Mapping]]=..., double_array_value: _Optional[_Union[_types_pb2.DoubleArray, _Mapping]]=..., int64_array_value: _Optional[_Union[_types_pb2.Int64Array, _Mapping]]=..., string_array_value: _Optional[_Union[_types_pb2.StringArray, _Mapping]]=..., bytes_value: _Optional[bytes]=..., struct_value: _Optional[_Union[StructValue, _Mapping]]=..., metadata: _Optional[_Union[FeatureValue.Metadata, _Mapping]]=...) -> None:
        ...

class StructValue(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[StructFieldValue]

    def __init__(self, values: _Optional[_Iterable[_Union[StructFieldValue, _Mapping]]]=...) -> None:
        ...

class StructFieldValue(_message.Message):
    __slots__ = ('name', 'value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: FeatureValue

    def __init__(self, name: _Optional[str]=..., value: _Optional[_Union[FeatureValue, _Mapping]]=...) -> None:
        ...

class FeatureValueList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[FeatureValue]

    def __init__(self, values: _Optional[_Iterable[_Union[FeatureValue, _Mapping]]]=...) -> None:
        ...