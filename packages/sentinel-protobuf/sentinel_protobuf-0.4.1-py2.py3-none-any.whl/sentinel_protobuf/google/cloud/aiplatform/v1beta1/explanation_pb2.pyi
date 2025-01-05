from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import explanation_metadata_pb2 as _explanation_metadata_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Explanation(_message.Message):
    __slots__ = ("attributions", "neighbors")
    ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    attributions: _containers.RepeatedCompositeFieldContainer[Attribution]
    neighbors: _containers.RepeatedCompositeFieldContainer[Neighbor]
    def __init__(self, attributions: _Optional[_Iterable[_Union[Attribution, _Mapping]]] = ..., neighbors: _Optional[_Iterable[_Union[Neighbor, _Mapping]]] = ...) -> None: ...

class ModelExplanation(_message.Message):
    __slots__ = ("mean_attributions",)
    MEAN_ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    mean_attributions: _containers.RepeatedCompositeFieldContainer[Attribution]
    def __init__(self, mean_attributions: _Optional[_Iterable[_Union[Attribution, _Mapping]]] = ...) -> None: ...

class Attribution(_message.Message):
    __slots__ = ("baseline_output_value", "instance_output_value", "feature_attributions", "output_index", "output_display_name", "approximation_error", "output_name")
    BASELINE_OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NAME_FIELD_NUMBER: _ClassVar[int]
    baseline_output_value: float
    instance_output_value: float
    feature_attributions: _struct_pb2.Value
    output_index: _containers.RepeatedScalarFieldContainer[int]
    output_display_name: str
    approximation_error: float
    output_name: str
    def __init__(self, baseline_output_value: _Optional[float] = ..., instance_output_value: _Optional[float] = ..., feature_attributions: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., output_index: _Optional[_Iterable[int]] = ..., output_display_name: _Optional[str] = ..., approximation_error: _Optional[float] = ..., output_name: _Optional[str] = ...) -> None: ...

class Neighbor(_message.Message):
    __slots__ = ("neighbor_id", "neighbor_distance")
    NEIGHBOR_ID_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    neighbor_id: str
    neighbor_distance: float
    def __init__(self, neighbor_id: _Optional[str] = ..., neighbor_distance: _Optional[float] = ...) -> None: ...

class ExplanationSpec(_message.Message):
    __slots__ = ("parameters", "metadata")
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    parameters: ExplanationParameters
    metadata: _explanation_metadata_pb2.ExplanationMetadata
    def __init__(self, parameters: _Optional[_Union[ExplanationParameters, _Mapping]] = ..., metadata: _Optional[_Union[_explanation_metadata_pb2.ExplanationMetadata, _Mapping]] = ...) -> None: ...

class ExplanationParameters(_message.Message):
    __slots__ = ("sampled_shapley_attribution", "integrated_gradients_attribution", "xrai_attribution", "examples", "top_k", "output_indices")
    SAMPLED_SHAPLEY_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    INTEGRATED_GRADIENTS_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    XRAI_ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INDICES_FIELD_NUMBER: _ClassVar[int]
    sampled_shapley_attribution: SampledShapleyAttribution
    integrated_gradients_attribution: IntegratedGradientsAttribution
    xrai_attribution: XraiAttribution
    examples: Examples
    top_k: int
    output_indices: _struct_pb2.ListValue
    def __init__(self, sampled_shapley_attribution: _Optional[_Union[SampledShapleyAttribution, _Mapping]] = ..., integrated_gradients_attribution: _Optional[_Union[IntegratedGradientsAttribution, _Mapping]] = ..., xrai_attribution: _Optional[_Union[XraiAttribution, _Mapping]] = ..., examples: _Optional[_Union[Examples, _Mapping]] = ..., top_k: _Optional[int] = ..., output_indices: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class SampledShapleyAttribution(_message.Message):
    __slots__ = ("path_count",)
    PATH_COUNT_FIELD_NUMBER: _ClassVar[int]
    path_count: int
    def __init__(self, path_count: _Optional[int] = ...) -> None: ...

class IntegratedGradientsAttribution(_message.Message):
    __slots__ = ("step_count", "smooth_grad_config", "blur_baseline_config")
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    SMOOTH_GRAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BLUR_BASELINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    step_count: int
    smooth_grad_config: SmoothGradConfig
    blur_baseline_config: BlurBaselineConfig
    def __init__(self, step_count: _Optional[int] = ..., smooth_grad_config: _Optional[_Union[SmoothGradConfig, _Mapping]] = ..., blur_baseline_config: _Optional[_Union[BlurBaselineConfig, _Mapping]] = ...) -> None: ...

class XraiAttribution(_message.Message):
    __slots__ = ("step_count", "smooth_grad_config", "blur_baseline_config")
    STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    SMOOTH_GRAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BLUR_BASELINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    step_count: int
    smooth_grad_config: SmoothGradConfig
    blur_baseline_config: BlurBaselineConfig
    def __init__(self, step_count: _Optional[int] = ..., smooth_grad_config: _Optional[_Union[SmoothGradConfig, _Mapping]] = ..., blur_baseline_config: _Optional[_Union[BlurBaselineConfig, _Mapping]] = ...) -> None: ...

class SmoothGradConfig(_message.Message):
    __slots__ = ("noise_sigma", "feature_noise_sigma", "noisy_sample_count")
    NOISE_SIGMA_FIELD_NUMBER: _ClassVar[int]
    FEATURE_NOISE_SIGMA_FIELD_NUMBER: _ClassVar[int]
    NOISY_SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    noise_sigma: float
    feature_noise_sigma: FeatureNoiseSigma
    noisy_sample_count: int
    def __init__(self, noise_sigma: _Optional[float] = ..., feature_noise_sigma: _Optional[_Union[FeatureNoiseSigma, _Mapping]] = ..., noisy_sample_count: _Optional[int] = ...) -> None: ...

class FeatureNoiseSigma(_message.Message):
    __slots__ = ("noise_sigma",)
    class NoiseSigmaForFeature(_message.Message):
        __slots__ = ("name", "sigma")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIGMA_FIELD_NUMBER: _ClassVar[int]
        name: str
        sigma: float
        def __init__(self, name: _Optional[str] = ..., sigma: _Optional[float] = ...) -> None: ...
    NOISE_SIGMA_FIELD_NUMBER: _ClassVar[int]
    noise_sigma: _containers.RepeatedCompositeFieldContainer[FeatureNoiseSigma.NoiseSigmaForFeature]
    def __init__(self, noise_sigma: _Optional[_Iterable[_Union[FeatureNoiseSigma.NoiseSigmaForFeature, _Mapping]]] = ...) -> None: ...

class BlurBaselineConfig(_message.Message):
    __slots__ = ("max_blur_sigma",)
    MAX_BLUR_SIGMA_FIELD_NUMBER: _ClassVar[int]
    max_blur_sigma: float
    def __init__(self, max_blur_sigma: _Optional[float] = ...) -> None: ...

class Examples(_message.Message):
    __slots__ = ("example_gcs_source", "nearest_neighbor_search_config", "presets", "gcs_source", "neighbor_count")
    class ExampleGcsSource(_message.Message):
        __slots__ = ("data_format", "gcs_source")
        class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DATA_FORMAT_UNSPECIFIED: _ClassVar[Examples.ExampleGcsSource.DataFormat]
            JSONL: _ClassVar[Examples.ExampleGcsSource.DataFormat]
        DATA_FORMAT_UNSPECIFIED: Examples.ExampleGcsSource.DataFormat
        JSONL: Examples.ExampleGcsSource.DataFormat
        DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        data_format: Examples.ExampleGcsSource.DataFormat
        gcs_source: _io_pb2.GcsSource
        def __init__(self, data_format: _Optional[_Union[Examples.ExampleGcsSource.DataFormat, str]] = ..., gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]] = ...) -> None: ...
    EXAMPLE_GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NEAREST_NEIGHBOR_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    example_gcs_source: Examples.ExampleGcsSource
    nearest_neighbor_search_config: _struct_pb2.Value
    presets: Presets
    gcs_source: _io_pb2.GcsSource
    neighbor_count: int
    def __init__(self, example_gcs_source: _Optional[_Union[Examples.ExampleGcsSource, _Mapping]] = ..., nearest_neighbor_search_config: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., presets: _Optional[_Union[Presets, _Mapping]] = ..., gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]] = ..., neighbor_count: _Optional[int] = ...) -> None: ...

class Presets(_message.Message):
    __slots__ = ("query", "modality")
    class Query(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRECISE: _ClassVar[Presets.Query]
        FAST: _ClassVar[Presets.Query]
    PRECISE: Presets.Query
    FAST: Presets.Query
    class Modality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODALITY_UNSPECIFIED: _ClassVar[Presets.Modality]
        IMAGE: _ClassVar[Presets.Modality]
        TEXT: _ClassVar[Presets.Modality]
        TABULAR: _ClassVar[Presets.Modality]
    MODALITY_UNSPECIFIED: Presets.Modality
    IMAGE: Presets.Modality
    TEXT: Presets.Modality
    TABULAR: Presets.Modality
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MODALITY_FIELD_NUMBER: _ClassVar[int]
    query: Presets.Query
    modality: Presets.Modality
    def __init__(self, query: _Optional[_Union[Presets.Query, str]] = ..., modality: _Optional[_Union[Presets.Modality, str]] = ...) -> None: ...

class ExplanationSpecOverride(_message.Message):
    __slots__ = ("parameters", "metadata", "examples_override")
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    parameters: ExplanationParameters
    metadata: ExplanationMetadataOverride
    examples_override: ExamplesOverride
    def __init__(self, parameters: _Optional[_Union[ExplanationParameters, _Mapping]] = ..., metadata: _Optional[_Union[ExplanationMetadataOverride, _Mapping]] = ..., examples_override: _Optional[_Union[ExamplesOverride, _Mapping]] = ...) -> None: ...

class ExplanationMetadataOverride(_message.Message):
    __slots__ = ("inputs",)
    class InputMetadataOverride(_message.Message):
        __slots__ = ("input_baselines",)
        INPUT_BASELINES_FIELD_NUMBER: _ClassVar[int]
        input_baselines: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
        def __init__(self, input_baselines: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...
    class InputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExplanationMetadataOverride.InputMetadataOverride
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExplanationMetadataOverride.InputMetadataOverride, _Mapping]] = ...) -> None: ...
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.MessageMap[str, ExplanationMetadataOverride.InputMetadataOverride]
    def __init__(self, inputs: _Optional[_Mapping[str, ExplanationMetadataOverride.InputMetadataOverride]] = ...) -> None: ...

class ExamplesOverride(_message.Message):
    __slots__ = ("neighbor_count", "crowding_count", "restrictions", "return_embeddings", "data_format")
    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExamplesOverride.DataFormat]
        INSTANCES: _ClassVar[ExamplesOverride.DataFormat]
        EMBEDDINGS: _ClassVar[ExamplesOverride.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExamplesOverride.DataFormat
    INSTANCES: ExamplesOverride.DataFormat
    EMBEDDINGS: ExamplesOverride.DataFormat
    NEIGHBOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    CROWDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    RETURN_EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    neighbor_count: int
    crowding_count: int
    restrictions: _containers.RepeatedCompositeFieldContainer[ExamplesRestrictionsNamespace]
    return_embeddings: bool
    data_format: ExamplesOverride.DataFormat
    def __init__(self, neighbor_count: _Optional[int] = ..., crowding_count: _Optional[int] = ..., restrictions: _Optional[_Iterable[_Union[ExamplesRestrictionsNamespace, _Mapping]]] = ..., return_embeddings: bool = ..., data_format: _Optional[_Union[ExamplesOverride.DataFormat, str]] = ...) -> None: ...

class ExamplesRestrictionsNamespace(_message.Message):
    __slots__ = ("namespace_name", "allow", "deny")
    NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    DENY_FIELD_NUMBER: _ClassVar[int]
    namespace_name: str
    allow: _containers.RepeatedScalarFieldContainer[str]
    deny: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace_name: _Optional[str] = ..., allow: _Optional[_Iterable[str]] = ..., deny: _Optional[_Iterable[str]] = ...) -> None: ...
