from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExplanationMetadata(_message.Message):
    __slots__ = ('inputs', 'outputs', 'feature_attributions_schema_uri', 'latent_space_source')

    class InputMetadata(_message.Message):
        __slots__ = ('input_baselines', 'input_tensor_name', 'encoding', 'modality', 'feature_value_domain', 'indices_tensor_name', 'dense_shape_tensor_name', 'index_feature_mapping', 'encoded_tensor_name', 'encoded_baselines', 'visualization', 'group_name')

        class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENCODING_UNSPECIFIED: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            IDENTITY: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            BAG_OF_FEATURES: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            BAG_OF_FEATURES_SPARSE: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            INDICATOR: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            COMBINED_EMBEDDING: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
            CONCAT_EMBEDDING: _ClassVar[ExplanationMetadata.InputMetadata.Encoding]
        ENCODING_UNSPECIFIED: ExplanationMetadata.InputMetadata.Encoding
        IDENTITY: ExplanationMetadata.InputMetadata.Encoding
        BAG_OF_FEATURES: ExplanationMetadata.InputMetadata.Encoding
        BAG_OF_FEATURES_SPARSE: ExplanationMetadata.InputMetadata.Encoding
        INDICATOR: ExplanationMetadata.InputMetadata.Encoding
        COMBINED_EMBEDDING: ExplanationMetadata.InputMetadata.Encoding
        CONCAT_EMBEDDING: ExplanationMetadata.InputMetadata.Encoding

        class FeatureValueDomain(_message.Message):
            __slots__ = ('min_value', 'max_value', 'original_mean', 'original_stddev')
            MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
            MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
            ORIGINAL_MEAN_FIELD_NUMBER: _ClassVar[int]
            ORIGINAL_STDDEV_FIELD_NUMBER: _ClassVar[int]
            min_value: float
            max_value: float
            original_mean: float
            original_stddev: float

            def __init__(self, min_value: _Optional[float]=..., max_value: _Optional[float]=..., original_mean: _Optional[float]=..., original_stddev: _Optional[float]=...) -> None:
                ...

        class Visualization(_message.Message):
            __slots__ = ('type', 'polarity', 'color_map', 'clip_percent_upperbound', 'clip_percent_lowerbound', 'overlay_type')

            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNSPECIFIED: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Type]
                PIXELS: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Type]
                OUTLINES: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Type]
            TYPE_UNSPECIFIED: ExplanationMetadata.InputMetadata.Visualization.Type
            PIXELS: ExplanationMetadata.InputMetadata.Visualization.Type
            OUTLINES: ExplanationMetadata.InputMetadata.Visualization.Type

            class Polarity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                POLARITY_UNSPECIFIED: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Polarity]
                POSITIVE: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Polarity]
                NEGATIVE: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Polarity]
                BOTH: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.Polarity]
            POLARITY_UNSPECIFIED: ExplanationMetadata.InputMetadata.Visualization.Polarity
            POSITIVE: ExplanationMetadata.InputMetadata.Visualization.Polarity
            NEGATIVE: ExplanationMetadata.InputMetadata.Visualization.Polarity
            BOTH: ExplanationMetadata.InputMetadata.Visualization.Polarity

            class ColorMap(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COLOR_MAP_UNSPECIFIED: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                PINK_GREEN: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                VIRIDIS: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                RED: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                GREEN: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                RED_GREEN: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
                PINK_WHITE_GREEN: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.ColorMap]
            COLOR_MAP_UNSPECIFIED: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            PINK_GREEN: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            VIRIDIS: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            RED: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            GREEN: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            RED_GREEN: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            PINK_WHITE_GREEN: ExplanationMetadata.InputMetadata.Visualization.ColorMap

            class OverlayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OVERLAY_TYPE_UNSPECIFIED: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.OverlayType]
                NONE: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.OverlayType]
                ORIGINAL: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.OverlayType]
                GRAYSCALE: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.OverlayType]
                MASK_BLACK: _ClassVar[ExplanationMetadata.InputMetadata.Visualization.OverlayType]
            OVERLAY_TYPE_UNSPECIFIED: ExplanationMetadata.InputMetadata.Visualization.OverlayType
            NONE: ExplanationMetadata.InputMetadata.Visualization.OverlayType
            ORIGINAL: ExplanationMetadata.InputMetadata.Visualization.OverlayType
            GRAYSCALE: ExplanationMetadata.InputMetadata.Visualization.OverlayType
            MASK_BLACK: ExplanationMetadata.InputMetadata.Visualization.OverlayType
            TYPE_FIELD_NUMBER: _ClassVar[int]
            POLARITY_FIELD_NUMBER: _ClassVar[int]
            COLOR_MAP_FIELD_NUMBER: _ClassVar[int]
            CLIP_PERCENT_UPPERBOUND_FIELD_NUMBER: _ClassVar[int]
            CLIP_PERCENT_LOWERBOUND_FIELD_NUMBER: _ClassVar[int]
            OVERLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
            type: ExplanationMetadata.InputMetadata.Visualization.Type
            polarity: ExplanationMetadata.InputMetadata.Visualization.Polarity
            color_map: ExplanationMetadata.InputMetadata.Visualization.ColorMap
            clip_percent_upperbound: float
            clip_percent_lowerbound: float
            overlay_type: ExplanationMetadata.InputMetadata.Visualization.OverlayType

            def __init__(self, type: _Optional[_Union[ExplanationMetadata.InputMetadata.Visualization.Type, str]]=..., polarity: _Optional[_Union[ExplanationMetadata.InputMetadata.Visualization.Polarity, str]]=..., color_map: _Optional[_Union[ExplanationMetadata.InputMetadata.Visualization.ColorMap, str]]=..., clip_percent_upperbound: _Optional[float]=..., clip_percent_lowerbound: _Optional[float]=..., overlay_type: _Optional[_Union[ExplanationMetadata.InputMetadata.Visualization.OverlayType, str]]=...) -> None:
                ...
        INPUT_BASELINES_FIELD_NUMBER: _ClassVar[int]
        INPUT_TENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        MODALITY_FIELD_NUMBER: _ClassVar[int]
        FEATURE_VALUE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        INDICES_TENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        DENSE_SHAPE_TENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FEATURE_MAPPING_FIELD_NUMBER: _ClassVar[int]
        ENCODED_TENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCODED_BASELINES_FIELD_NUMBER: _ClassVar[int]
        VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        input_baselines: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
        input_tensor_name: str
        encoding: ExplanationMetadata.InputMetadata.Encoding
        modality: str
        feature_value_domain: ExplanationMetadata.InputMetadata.FeatureValueDomain
        indices_tensor_name: str
        dense_shape_tensor_name: str
        index_feature_mapping: _containers.RepeatedScalarFieldContainer[str]
        encoded_tensor_name: str
        encoded_baselines: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
        visualization: ExplanationMetadata.InputMetadata.Visualization
        group_name: str

        def __init__(self, input_baselines: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., input_tensor_name: _Optional[str]=..., encoding: _Optional[_Union[ExplanationMetadata.InputMetadata.Encoding, str]]=..., modality: _Optional[str]=..., feature_value_domain: _Optional[_Union[ExplanationMetadata.InputMetadata.FeatureValueDomain, _Mapping]]=..., indices_tensor_name: _Optional[str]=..., dense_shape_tensor_name: _Optional[str]=..., index_feature_mapping: _Optional[_Iterable[str]]=..., encoded_tensor_name: _Optional[str]=..., encoded_baselines: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., visualization: _Optional[_Union[ExplanationMetadata.InputMetadata.Visualization, _Mapping]]=..., group_name: _Optional[str]=...) -> None:
            ...

    class OutputMetadata(_message.Message):
        __slots__ = ('index_display_name_mapping', 'display_name_mapping_key', 'output_tensor_name')
        INDEX_DISPLAY_NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_MAPPING_KEY_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_TENSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        index_display_name_mapping: _struct_pb2.Value
        display_name_mapping_key: str
        output_tensor_name: str

        def __init__(self, index_display_name_mapping: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., display_name_mapping_key: _Optional[str]=..., output_tensor_name: _Optional[str]=...) -> None:
            ...

    class InputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExplanationMetadata.InputMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ExplanationMetadata.InputMetadata, _Mapping]]=...) -> None:
            ...

    class OutputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExplanationMetadata.OutputMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ExplanationMetadata.OutputMetadata, _Mapping]]=...) -> None:
            ...
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ATTRIBUTIONS_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    LATENT_SPACE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.MessageMap[str, ExplanationMetadata.InputMetadata]
    outputs: _containers.MessageMap[str, ExplanationMetadata.OutputMetadata]
    feature_attributions_schema_uri: str
    latent_space_source: str

    def __init__(self, inputs: _Optional[_Mapping[str, ExplanationMetadata.InputMetadata]]=..., outputs: _Optional[_Mapping[str, ExplanationMetadata.OutputMetadata]]=..., feature_attributions_schema_uri: _Optional[str]=..., latent_space_source: _Optional[str]=...) -> None:
        ...