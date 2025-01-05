from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelFeature(_message.Message):
    __slots__ = ('feature', 'release_state')
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_STATE_FIELD_NUMBER: _ClassVar[int]
    feature: str
    release_state: str

    def __init__(self, feature: _Optional[str]=..., release_state: _Optional[str]=...) -> None:
        ...

class ModelFeatures(_message.Message):
    __slots__ = ('model_feature',)
    MODEL_FEATURE_FIELD_NUMBER: _ClassVar[int]
    model_feature: _containers.RepeatedCompositeFieldContainer[ModelFeature]

    def __init__(self, model_feature: _Optional[_Iterable[_Union[ModelFeature, _Mapping]]]=...) -> None:
        ...

class ModelMetadata(_message.Message):
    __slots__ = ('model_features',)

    class ModelFeaturesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelFeatures

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ModelFeatures, _Mapping]]=...) -> None:
            ...
    MODEL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    model_features: _containers.MessageMap[str, ModelFeatures]

    def __init__(self, model_features: _Optional[_Mapping[str, ModelFeatures]]=...) -> None:
        ...

class LanguageMetadata(_message.Message):
    __slots__ = ('models',)

    class ModelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ModelMetadata, _Mapping]]=...) -> None:
            ...
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.MessageMap[str, ModelMetadata]

    def __init__(self, models: _Optional[_Mapping[str, ModelMetadata]]=...) -> None:
        ...

class AccessMetadata(_message.Message):
    __slots__ = ('constraint_type',)

    class ConstraintType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSTRAINT_TYPE_UNSPECIFIED: _ClassVar[AccessMetadata.ConstraintType]
        RESOURCE_LOCATIONS_ORG_POLICY_CREATE_CONSTRAINT: _ClassVar[AccessMetadata.ConstraintType]
    CONSTRAINT_TYPE_UNSPECIFIED: AccessMetadata.ConstraintType
    RESOURCE_LOCATIONS_ORG_POLICY_CREATE_CONSTRAINT: AccessMetadata.ConstraintType
    CONSTRAINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    constraint_type: AccessMetadata.ConstraintType

    def __init__(self, constraint_type: _Optional[_Union[AccessMetadata.ConstraintType, str]]=...) -> None:
        ...

class LocationsMetadata(_message.Message):
    __slots__ = ('languages', 'access_metadata')
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_METADATA_FIELD_NUMBER: _ClassVar[int]
    languages: LanguageMetadata
    access_metadata: AccessMetadata

    def __init__(self, languages: _Optional[_Union[LanguageMetadata, _Mapping]]=..., access_metadata: _Optional[_Union[AccessMetadata, _Mapping]]=...) -> None:
        ...