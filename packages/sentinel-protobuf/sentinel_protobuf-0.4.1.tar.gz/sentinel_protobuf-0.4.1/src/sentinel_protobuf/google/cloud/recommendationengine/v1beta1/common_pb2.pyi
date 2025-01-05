from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureMap(_message.Message):
    __slots__ = ('categorical_features', 'numerical_features')

    class StringList(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, value: _Optional[_Iterable[str]]=...) -> None:
            ...

    class FloatList(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]

        def __init__(self, value: _Optional[_Iterable[float]]=...) -> None:
            ...

    class CategoricalFeaturesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FeatureMap.StringList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FeatureMap.StringList, _Mapping]]=...) -> None:
            ...

    class NumericalFeaturesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FeatureMap.FloatList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FeatureMap.FloatList, _Mapping]]=...) -> None:
            ...
    CATEGORICAL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    NUMERICAL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    categorical_features: _containers.MessageMap[str, FeatureMap.StringList]
    numerical_features: _containers.MessageMap[str, FeatureMap.FloatList]

    def __init__(self, categorical_features: _Optional[_Mapping[str, FeatureMap.StringList]]=..., numerical_features: _Optional[_Mapping[str, FeatureMap.FloatList]]=...) -> None:
        ...