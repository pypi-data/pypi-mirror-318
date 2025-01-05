from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1beta1 import annotation_payload_pb2 as _annotation_payload_pb2
from google.cloud.automl.v1beta1 import data_items_pb2 as _data_items_pb2
from google.cloud.automl.v1beta1 import io_pb2 as _io_pb2
from google.cloud.automl.v1beta1 import operations_pb2 as _operations_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ('name', 'payload', 'params')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    payload: _data_items_pb2.ExamplePayload
    params: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., payload: _Optional[_Union[_data_items_pb2.ExamplePayload, _Mapping]]=..., params: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class PredictResponse(_message.Message):
    __slots__ = ('payload', 'preprocessed_input', 'metadata')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSED_INPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    payload: _containers.RepeatedCompositeFieldContainer[_annotation_payload_pb2.AnnotationPayload]
    preprocessed_input: _data_items_pb2.ExamplePayload
    metadata: _containers.ScalarMap[str, str]

    def __init__(self, payload: _Optional[_Iterable[_Union[_annotation_payload_pb2.AnnotationPayload, _Mapping]]]=..., preprocessed_input: _Optional[_Union[_data_items_pb2.ExamplePayload, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BatchPredictRequest(_message.Message):
    __slots__ = ('name', 'input_config', 'output_config', 'params')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: _io_pb2.BatchPredictInputConfig
    output_config: _io_pb2.BatchPredictOutputConfig
    params: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., input_config: _Optional[_Union[_io_pb2.BatchPredictInputConfig, _Mapping]]=..., output_config: _Optional[_Union[_io_pb2.BatchPredictOutputConfig, _Mapping]]=..., params: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BatchPredictResult(_message.Message):
    __slots__ = ('metadata',)

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.ScalarMap[str, str]

    def __init__(self, metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...