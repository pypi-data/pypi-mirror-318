from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PairwiseChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAIRWISE_CHOICE_UNSPECIFIED: _ClassVar[PairwiseChoice]
    BASELINE: _ClassVar[PairwiseChoice]
    CANDIDATE: _ClassVar[PairwiseChoice]
    TIE: _ClassVar[PairwiseChoice]
PAIRWISE_CHOICE_UNSPECIFIED: PairwiseChoice
BASELINE: PairwiseChoice
CANDIDATE: PairwiseChoice
TIE: PairwiseChoice

class EvaluateInstancesRequest(_message.Message):
    __slots__ = ("exact_match_input", "bleu_input", "rouge_input", "fluency_input", "coherence_input", "safety_input", "groundedness_input", "fulfillment_input", "summarization_quality_input", "pairwise_summarization_quality_input", "summarization_helpfulness_input", "summarization_verbosity_input", "question_answering_quality_input", "pairwise_question_answering_quality_input", "question_answering_relevance_input", "question_answering_helpfulness_input", "question_answering_correctness_input", "pointwise_metric_input", "pairwise_metric_input", "tool_call_valid_input", "tool_name_match_input", "tool_parameter_key_match_input", "tool_parameter_kv_match_input", "trajectory_exact_match_input", "trajectory_in_order_match_input", "trajectory_any_order_match_input", "trajectory_precision_input", "trajectory_recall_input", "trajectory_single_tool_use_input", "location")
    EXACT_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    BLEU_INPUT_FIELD_NUMBER: _ClassVar[int]
    ROUGE_INPUT_FIELD_NUMBER: _ClassVar[int]
    FLUENCY_INPUT_FIELD_NUMBER: _ClassVar[int]
    COHERENCE_INPUT_FIELD_NUMBER: _ClassVar[int]
    SAFETY_INPUT_FIELD_NUMBER: _ClassVar[int]
    GROUNDEDNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_SUMMARIZATION_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_HELPFULNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_VERBOSITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_QUESTION_ANSWERING_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_RELEVANCE_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_HELPFULNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_CORRECTNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    POINTWISE_METRIC_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_VALID_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KEY_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KV_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_EXACT_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_IN_ORDER_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_ANY_ORDER_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_PRECISION_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_RECALL_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_SINGLE_TOOL_USE_INPUT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    exact_match_input: ExactMatchInput
    bleu_input: BleuInput
    rouge_input: RougeInput
    fluency_input: FluencyInput
    coherence_input: CoherenceInput
    safety_input: SafetyInput
    groundedness_input: GroundednessInput
    fulfillment_input: FulfillmentInput
    summarization_quality_input: SummarizationQualityInput
    pairwise_summarization_quality_input: PairwiseSummarizationQualityInput
    summarization_helpfulness_input: SummarizationHelpfulnessInput
    summarization_verbosity_input: SummarizationVerbosityInput
    question_answering_quality_input: QuestionAnsweringQualityInput
    pairwise_question_answering_quality_input: PairwiseQuestionAnsweringQualityInput
    question_answering_relevance_input: QuestionAnsweringRelevanceInput
    question_answering_helpfulness_input: QuestionAnsweringHelpfulnessInput
    question_answering_correctness_input: QuestionAnsweringCorrectnessInput
    pointwise_metric_input: PointwiseMetricInput
    pairwise_metric_input: PairwiseMetricInput
    tool_call_valid_input: ToolCallValidInput
    tool_name_match_input: ToolNameMatchInput
    tool_parameter_key_match_input: ToolParameterKeyMatchInput
    tool_parameter_kv_match_input: ToolParameterKVMatchInput
    trajectory_exact_match_input: TrajectoryExactMatchInput
    trajectory_in_order_match_input: TrajectoryInOrderMatchInput
    trajectory_any_order_match_input: TrajectoryAnyOrderMatchInput
    trajectory_precision_input: TrajectoryPrecisionInput
    trajectory_recall_input: TrajectoryRecallInput
    trajectory_single_tool_use_input: TrajectorySingleToolUseInput
    location: str
    def __init__(self, exact_match_input: _Optional[_Union[ExactMatchInput, _Mapping]] = ..., bleu_input: _Optional[_Union[BleuInput, _Mapping]] = ..., rouge_input: _Optional[_Union[RougeInput, _Mapping]] = ..., fluency_input: _Optional[_Union[FluencyInput, _Mapping]] = ..., coherence_input: _Optional[_Union[CoherenceInput, _Mapping]] = ..., safety_input: _Optional[_Union[SafetyInput, _Mapping]] = ..., groundedness_input: _Optional[_Union[GroundednessInput, _Mapping]] = ..., fulfillment_input: _Optional[_Union[FulfillmentInput, _Mapping]] = ..., summarization_quality_input: _Optional[_Union[SummarizationQualityInput, _Mapping]] = ..., pairwise_summarization_quality_input: _Optional[_Union[PairwiseSummarizationQualityInput, _Mapping]] = ..., summarization_helpfulness_input: _Optional[_Union[SummarizationHelpfulnessInput, _Mapping]] = ..., summarization_verbosity_input: _Optional[_Union[SummarizationVerbosityInput, _Mapping]] = ..., question_answering_quality_input: _Optional[_Union[QuestionAnsweringQualityInput, _Mapping]] = ..., pairwise_question_answering_quality_input: _Optional[_Union[PairwiseQuestionAnsweringQualityInput, _Mapping]] = ..., question_answering_relevance_input: _Optional[_Union[QuestionAnsweringRelevanceInput, _Mapping]] = ..., question_answering_helpfulness_input: _Optional[_Union[QuestionAnsweringHelpfulnessInput, _Mapping]] = ..., question_answering_correctness_input: _Optional[_Union[QuestionAnsweringCorrectnessInput, _Mapping]] = ..., pointwise_metric_input: _Optional[_Union[PointwiseMetricInput, _Mapping]] = ..., pairwise_metric_input: _Optional[_Union[PairwiseMetricInput, _Mapping]] = ..., tool_call_valid_input: _Optional[_Union[ToolCallValidInput, _Mapping]] = ..., tool_name_match_input: _Optional[_Union[ToolNameMatchInput, _Mapping]] = ..., tool_parameter_key_match_input: _Optional[_Union[ToolParameterKeyMatchInput, _Mapping]] = ..., tool_parameter_kv_match_input: _Optional[_Union[ToolParameterKVMatchInput, _Mapping]] = ..., trajectory_exact_match_input: _Optional[_Union[TrajectoryExactMatchInput, _Mapping]] = ..., trajectory_in_order_match_input: _Optional[_Union[TrajectoryInOrderMatchInput, _Mapping]] = ..., trajectory_any_order_match_input: _Optional[_Union[TrajectoryAnyOrderMatchInput, _Mapping]] = ..., trajectory_precision_input: _Optional[_Union[TrajectoryPrecisionInput, _Mapping]] = ..., trajectory_recall_input: _Optional[_Union[TrajectoryRecallInput, _Mapping]] = ..., trajectory_single_tool_use_input: _Optional[_Union[TrajectorySingleToolUseInput, _Mapping]] = ..., location: _Optional[str] = ...) -> None: ...

class EvaluateInstancesResponse(_message.Message):
    __slots__ = ("exact_match_results", "bleu_results", "rouge_results", "fluency_result", "coherence_result", "safety_result", "groundedness_result", "fulfillment_result", "summarization_quality_result", "pairwise_summarization_quality_result", "summarization_helpfulness_result", "summarization_verbosity_result", "question_answering_quality_result", "pairwise_question_answering_quality_result", "question_answering_relevance_result", "question_answering_helpfulness_result", "question_answering_correctness_result", "pointwise_metric_result", "pairwise_metric_result", "tool_call_valid_results", "tool_name_match_results", "tool_parameter_key_match_results", "tool_parameter_kv_match_results", "trajectory_exact_match_results", "trajectory_in_order_match_results", "trajectory_any_order_match_results", "trajectory_precision_results", "trajectory_recall_results", "trajectory_single_tool_use_results")
    EXACT_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    BLEU_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ROUGE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    FLUENCY_RESULT_FIELD_NUMBER: _ClassVar[int]
    COHERENCE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RESULT_FIELD_NUMBER: _ClassVar[int]
    GROUNDEDNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_SUMMARIZATION_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_HELPFULNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_VERBOSITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_QUESTION_ANSWERING_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_RELEVANCE_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_HELPFULNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_CORRECTNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    POINTWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_VALID_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KEY_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KV_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_EXACT_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_IN_ORDER_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_ANY_ORDER_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_PRECISION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_RECALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_SINGLE_TOOL_USE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    exact_match_results: ExactMatchResults
    bleu_results: BleuResults
    rouge_results: RougeResults
    fluency_result: FluencyResult
    coherence_result: CoherenceResult
    safety_result: SafetyResult
    groundedness_result: GroundednessResult
    fulfillment_result: FulfillmentResult
    summarization_quality_result: SummarizationQualityResult
    pairwise_summarization_quality_result: PairwiseSummarizationQualityResult
    summarization_helpfulness_result: SummarizationHelpfulnessResult
    summarization_verbosity_result: SummarizationVerbosityResult
    question_answering_quality_result: QuestionAnsweringQualityResult
    pairwise_question_answering_quality_result: PairwiseQuestionAnsweringQualityResult
    question_answering_relevance_result: QuestionAnsweringRelevanceResult
    question_answering_helpfulness_result: QuestionAnsweringHelpfulnessResult
    question_answering_correctness_result: QuestionAnsweringCorrectnessResult
    pointwise_metric_result: PointwiseMetricResult
    pairwise_metric_result: PairwiseMetricResult
    tool_call_valid_results: ToolCallValidResults
    tool_name_match_results: ToolNameMatchResults
    tool_parameter_key_match_results: ToolParameterKeyMatchResults
    tool_parameter_kv_match_results: ToolParameterKVMatchResults
    trajectory_exact_match_results: TrajectoryExactMatchResults
    trajectory_in_order_match_results: TrajectoryInOrderMatchResults
    trajectory_any_order_match_results: TrajectoryAnyOrderMatchResults
    trajectory_precision_results: TrajectoryPrecisionResults
    trajectory_recall_results: TrajectoryRecallResults
    trajectory_single_tool_use_results: TrajectorySingleToolUseResults
    def __init__(self, exact_match_results: _Optional[_Union[ExactMatchResults, _Mapping]] = ..., bleu_results: _Optional[_Union[BleuResults, _Mapping]] = ..., rouge_results: _Optional[_Union[RougeResults, _Mapping]] = ..., fluency_result: _Optional[_Union[FluencyResult, _Mapping]] = ..., coherence_result: _Optional[_Union[CoherenceResult, _Mapping]] = ..., safety_result: _Optional[_Union[SafetyResult, _Mapping]] = ..., groundedness_result: _Optional[_Union[GroundednessResult, _Mapping]] = ..., fulfillment_result: _Optional[_Union[FulfillmentResult, _Mapping]] = ..., summarization_quality_result: _Optional[_Union[SummarizationQualityResult, _Mapping]] = ..., pairwise_summarization_quality_result: _Optional[_Union[PairwiseSummarizationQualityResult, _Mapping]] = ..., summarization_helpfulness_result: _Optional[_Union[SummarizationHelpfulnessResult, _Mapping]] = ..., summarization_verbosity_result: _Optional[_Union[SummarizationVerbosityResult, _Mapping]] = ..., question_answering_quality_result: _Optional[_Union[QuestionAnsweringQualityResult, _Mapping]] = ..., pairwise_question_answering_quality_result: _Optional[_Union[PairwiseQuestionAnsweringQualityResult, _Mapping]] = ..., question_answering_relevance_result: _Optional[_Union[QuestionAnsweringRelevanceResult, _Mapping]] = ..., question_answering_helpfulness_result: _Optional[_Union[QuestionAnsweringHelpfulnessResult, _Mapping]] = ..., question_answering_correctness_result: _Optional[_Union[QuestionAnsweringCorrectnessResult, _Mapping]] = ..., pointwise_metric_result: _Optional[_Union[PointwiseMetricResult, _Mapping]] = ..., pairwise_metric_result: _Optional[_Union[PairwiseMetricResult, _Mapping]] = ..., tool_call_valid_results: _Optional[_Union[ToolCallValidResults, _Mapping]] = ..., tool_name_match_results: _Optional[_Union[ToolNameMatchResults, _Mapping]] = ..., tool_parameter_key_match_results: _Optional[_Union[ToolParameterKeyMatchResults, _Mapping]] = ..., tool_parameter_kv_match_results: _Optional[_Union[ToolParameterKVMatchResults, _Mapping]] = ..., trajectory_exact_match_results: _Optional[_Union[TrajectoryExactMatchResults, _Mapping]] = ..., trajectory_in_order_match_results: _Optional[_Union[TrajectoryInOrderMatchResults, _Mapping]] = ..., trajectory_any_order_match_results: _Optional[_Union[TrajectoryAnyOrderMatchResults, _Mapping]] = ..., trajectory_precision_results: _Optional[_Union[TrajectoryPrecisionResults, _Mapping]] = ..., trajectory_recall_results: _Optional[_Union[TrajectoryRecallResults, _Mapping]] = ..., trajectory_single_tool_use_results: _Optional[_Union[TrajectorySingleToolUseResults, _Mapping]] = ...) -> None: ...

class ExactMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ExactMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ExactMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[ExactMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[ExactMatchInstance, _Mapping]]] = ...) -> None: ...

class ExactMatchInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ExactMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExactMatchResults(_message.Message):
    __slots__ = ("exact_match_metric_values",)
    EXACT_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    exact_match_metric_values: _containers.RepeatedCompositeFieldContainer[ExactMatchMetricValue]
    def __init__(self, exact_match_metric_values: _Optional[_Iterable[_Union[ExactMatchMetricValue, _Mapping]]] = ...) -> None: ...

class ExactMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class BleuInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: BleuSpec
    instances: _containers.RepeatedCompositeFieldContainer[BleuInstance]
    def __init__(self, metric_spec: _Optional[_Union[BleuSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[BleuInstance, _Mapping]]] = ...) -> None: ...

class BleuInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class BleuSpec(_message.Message):
    __slots__ = ("use_effective_order",)
    USE_EFFECTIVE_ORDER_FIELD_NUMBER: _ClassVar[int]
    use_effective_order: bool
    def __init__(self, use_effective_order: bool = ...) -> None: ...

class BleuResults(_message.Message):
    __slots__ = ("bleu_metric_values",)
    BLEU_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    bleu_metric_values: _containers.RepeatedCompositeFieldContainer[BleuMetricValue]
    def __init__(self, bleu_metric_values: _Optional[_Iterable[_Union[BleuMetricValue, _Mapping]]] = ...) -> None: ...

class BleuMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class RougeInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: RougeSpec
    instances: _containers.RepeatedCompositeFieldContainer[RougeInstance]
    def __init__(self, metric_spec: _Optional[_Union[RougeSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[RougeInstance, _Mapping]]] = ...) -> None: ...

class RougeInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class RougeSpec(_message.Message):
    __slots__ = ("rouge_type", "use_stemmer", "split_summaries")
    ROUGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_STEMMER_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    rouge_type: str
    use_stemmer: bool
    split_summaries: bool
    def __init__(self, rouge_type: _Optional[str] = ..., use_stemmer: bool = ..., split_summaries: bool = ...) -> None: ...

class RougeResults(_message.Message):
    __slots__ = ("rouge_metric_values",)
    ROUGE_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    rouge_metric_values: _containers.RepeatedCompositeFieldContainer[RougeMetricValue]
    def __init__(self, rouge_metric_values: _Optional[_Iterable[_Union[RougeMetricValue, _Mapping]]] = ...) -> None: ...

class RougeMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class CoherenceInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: CoherenceSpec
    instance: CoherenceInstance
    def __init__(self, metric_spec: _Optional[_Union[CoherenceSpec, _Mapping]] = ..., instance: _Optional[_Union[CoherenceInstance, _Mapping]] = ...) -> None: ...

class CoherenceInstance(_message.Message):
    __slots__ = ("prediction",)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    def __init__(self, prediction: _Optional[str] = ...) -> None: ...

class CoherenceSpec(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class CoherenceResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class FluencyInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: FluencySpec
    instance: FluencyInstance
    def __init__(self, metric_spec: _Optional[_Union[FluencySpec, _Mapping]] = ..., instance: _Optional[_Union[FluencyInstance, _Mapping]] = ...) -> None: ...

class FluencyInstance(_message.Message):
    __slots__ = ("prediction",)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    def __init__(self, prediction: _Optional[str] = ...) -> None: ...

class FluencySpec(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class FluencyResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class SafetyInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SafetySpec
    instance: SafetyInstance
    def __init__(self, metric_spec: _Optional[_Union[SafetySpec, _Mapping]] = ..., instance: _Optional[_Union[SafetyInstance, _Mapping]] = ...) -> None: ...

class SafetyInstance(_message.Message):
    __slots__ = ("prediction",)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    def __init__(self, prediction: _Optional[str] = ...) -> None: ...

class SafetySpec(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class SafetyResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class GroundednessInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: GroundednessSpec
    instance: GroundednessInstance
    def __init__(self, metric_spec: _Optional[_Union[GroundednessSpec, _Mapping]] = ..., instance: _Optional[_Union[GroundednessInstance, _Mapping]] = ...) -> None: ...

class GroundednessInstance(_message.Message):
    __slots__ = ("prediction", "context")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    context: str
    def __init__(self, prediction: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class GroundednessSpec(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class GroundednessResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class FulfillmentInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: FulfillmentSpec
    instance: FulfillmentInstance
    def __init__(self, metric_spec: _Optional[_Union[FulfillmentSpec, _Mapping]] = ..., instance: _Optional[_Union[FulfillmentInstance, _Mapping]] = ...) -> None: ...

class FulfillmentInstance(_message.Message):
    __slots__ = ("prediction", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class FulfillmentSpec(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class FulfillmentResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class SummarizationQualityInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationQualitySpec
    instance: SummarizationQualityInstance
    def __init__(self, metric_spec: _Optional[_Union[SummarizationQualitySpec, _Mapping]] = ..., instance: _Optional[_Union[SummarizationQualityInstance, _Mapping]] = ...) -> None: ...

class SummarizationQualityInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class SummarizationQualitySpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class SummarizationQualityResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class PairwiseSummarizationQualityInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseSummarizationQualitySpec
    instance: PairwiseSummarizationQualityInstance
    def __init__(self, metric_spec: _Optional[_Union[PairwiseSummarizationQualitySpec, _Mapping]] = ..., instance: _Optional[_Union[PairwiseSummarizationQualityInstance, _Mapping]] = ...) -> None: ...

class PairwiseSummarizationQualityInstance(_message.Message):
    __slots__ = ("prediction", "baseline_prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    BASELINE_PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    baseline_prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., baseline_prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class PairwiseSummarizationQualitySpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class PairwiseSummarizationQualityResult(_message.Message):
    __slots__ = ("pairwise_choice", "explanation", "confidence")
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    confidence: float
    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class SummarizationHelpfulnessInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationHelpfulnessSpec
    instance: SummarizationHelpfulnessInstance
    def __init__(self, metric_spec: _Optional[_Union[SummarizationHelpfulnessSpec, _Mapping]] = ..., instance: _Optional[_Union[SummarizationHelpfulnessInstance, _Mapping]] = ...) -> None: ...

class SummarizationHelpfulnessInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class SummarizationHelpfulnessSpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class SummarizationHelpfulnessResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class SummarizationVerbosityInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationVerbositySpec
    instance: SummarizationVerbosityInstance
    def __init__(self, metric_spec: _Optional[_Union[SummarizationVerbositySpec, _Mapping]] = ..., instance: _Optional[_Union[SummarizationVerbosityInstance, _Mapping]] = ...) -> None: ...

class SummarizationVerbosityInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class SummarizationVerbositySpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class SummarizationVerbosityResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class QuestionAnsweringQualityInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringQualitySpec
    instance: QuestionAnsweringQualityInstance
    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringQualitySpec, _Mapping]] = ..., instance: _Optional[_Union[QuestionAnsweringQualityInstance, _Mapping]] = ...) -> None: ...

class QuestionAnsweringQualityInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class QuestionAnsweringQualitySpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class QuestionAnsweringQualityResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class PairwiseQuestionAnsweringQualityInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseQuestionAnsweringQualitySpec
    instance: PairwiseQuestionAnsweringQualityInstance
    def __init__(self, metric_spec: _Optional[_Union[PairwiseQuestionAnsweringQualitySpec, _Mapping]] = ..., instance: _Optional[_Union[PairwiseQuestionAnsweringQualityInstance, _Mapping]] = ...) -> None: ...

class PairwiseQuestionAnsweringQualityInstance(_message.Message):
    __slots__ = ("prediction", "baseline_prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    BASELINE_PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    baseline_prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., baseline_prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class PairwiseQuestionAnsweringQualitySpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class PairwiseQuestionAnsweringQualityResult(_message.Message):
    __slots__ = ("pairwise_choice", "explanation", "confidence")
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    confidence: float
    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class QuestionAnsweringRelevanceInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringRelevanceSpec
    instance: QuestionAnsweringRelevanceInstance
    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringRelevanceSpec, _Mapping]] = ..., instance: _Optional[_Union[QuestionAnsweringRelevanceInstance, _Mapping]] = ...) -> None: ...

class QuestionAnsweringRelevanceInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class QuestionAnsweringRelevanceSpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class QuestionAnsweringRelevanceResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class QuestionAnsweringHelpfulnessInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringHelpfulnessSpec
    instance: QuestionAnsweringHelpfulnessInstance
    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringHelpfulnessSpec, _Mapping]] = ..., instance: _Optional[_Union[QuestionAnsweringHelpfulnessInstance, _Mapping]] = ...) -> None: ...

class QuestionAnsweringHelpfulnessInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class QuestionAnsweringHelpfulnessSpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class QuestionAnsweringHelpfulnessResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class QuestionAnsweringCorrectnessInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringCorrectnessSpec
    instance: QuestionAnsweringCorrectnessInstance
    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringCorrectnessSpec, _Mapping]] = ..., instance: _Optional[_Union[QuestionAnsweringCorrectnessInstance, _Mapping]] = ...) -> None: ...

class QuestionAnsweringCorrectnessInstance(_message.Message):
    __slots__ = ("prediction", "reference", "context", "instruction")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ..., context: _Optional[str] = ..., instruction: _Optional[str] = ...) -> None: ...

class QuestionAnsweringCorrectnessSpec(_message.Message):
    __slots__ = ("use_reference", "version")
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int
    def __init__(self, use_reference: bool = ..., version: _Optional[int] = ...) -> None: ...

class QuestionAnsweringCorrectnessResult(_message.Message):
    __slots__ = ("score", "explanation", "confidence")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class PointwiseMetricInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PointwiseMetricSpec
    instance: PointwiseMetricInstance
    def __init__(self, metric_spec: _Optional[_Union[PointwiseMetricSpec, _Mapping]] = ..., instance: _Optional[_Union[PointwiseMetricInstance, _Mapping]] = ...) -> None: ...

class PointwiseMetricInstance(_message.Message):
    __slots__ = ("json_instance",)
    JSON_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    json_instance: str
    def __init__(self, json_instance: _Optional[str] = ...) -> None: ...

class PointwiseMetricSpec(_message.Message):
    __slots__ = ("metric_prompt_template",)
    METRIC_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    metric_prompt_template: str
    def __init__(self, metric_prompt_template: _Optional[str] = ...) -> None: ...

class PointwiseMetricResult(_message.Message):
    __slots__ = ("score", "explanation")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    def __init__(self, score: _Optional[float] = ..., explanation: _Optional[str] = ...) -> None: ...

class PairwiseMetricInput(_message.Message):
    __slots__ = ("metric_spec", "instance")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseMetricSpec
    instance: PairwiseMetricInstance
    def __init__(self, metric_spec: _Optional[_Union[PairwiseMetricSpec, _Mapping]] = ..., instance: _Optional[_Union[PairwiseMetricInstance, _Mapping]] = ...) -> None: ...

class PairwiseMetricInstance(_message.Message):
    __slots__ = ("json_instance",)
    JSON_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    json_instance: str
    def __init__(self, json_instance: _Optional[str] = ...) -> None: ...

class PairwiseMetricSpec(_message.Message):
    __slots__ = ("metric_prompt_template",)
    METRIC_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    metric_prompt_template: str
    def __init__(self, metric_prompt_template: _Optional[str] = ...) -> None: ...

class PairwiseMetricResult(_message.Message):
    __slots__ = ("pairwise_choice", "explanation")
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]] = ..., explanation: _Optional[str] = ...) -> None: ...

class ToolCallValidInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolCallValidSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolCallValidInstance]
    def __init__(self, metric_spec: _Optional[_Union[ToolCallValidSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[ToolCallValidInstance, _Mapping]]] = ...) -> None: ...

class ToolCallValidSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolCallValidInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ToolCallValidResults(_message.Message):
    __slots__ = ("tool_call_valid_metric_values",)
    TOOL_CALL_VALID_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_call_valid_metric_values: _containers.RepeatedCompositeFieldContainer[ToolCallValidMetricValue]
    def __init__(self, tool_call_valid_metric_values: _Optional[_Iterable[_Union[ToolCallValidMetricValue, _Mapping]]] = ...) -> None: ...

class ToolCallValidMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class ToolNameMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolNameMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolNameMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[ToolNameMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[ToolNameMatchInstance, _Mapping]]] = ...) -> None: ...

class ToolNameMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolNameMatchInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ToolNameMatchResults(_message.Message):
    __slots__ = ("tool_name_match_metric_values",)
    TOOL_NAME_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_name_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolNameMatchMetricValue]
    def __init__(self, tool_name_match_metric_values: _Optional[_Iterable[_Union[ToolNameMatchMetricValue, _Mapping]]] = ...) -> None: ...

class ToolNameMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class ToolParameterKeyMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolParameterKeyMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolParameterKeyMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[ToolParameterKeyMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[ToolParameterKeyMatchInstance, _Mapping]]] = ...) -> None: ...

class ToolParameterKeyMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ToolParameterKeyMatchInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ToolParameterKeyMatchResults(_message.Message):
    __slots__ = ("tool_parameter_key_match_metric_values",)
    TOOL_PARAMETER_KEY_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_parameter_key_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolParameterKeyMatchMetricValue]
    def __init__(self, tool_parameter_key_match_metric_values: _Optional[_Iterable[_Union[ToolParameterKeyMatchMetricValue, _Mapping]]] = ...) -> None: ...

class ToolParameterKeyMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class ToolParameterKVMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolParameterKVMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolParameterKVMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[ToolParameterKVMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[ToolParameterKVMatchInstance, _Mapping]]] = ...) -> None: ...

class ToolParameterKVMatchSpec(_message.Message):
    __slots__ = ("use_strict_string_match",)
    USE_STRICT_STRING_MATCH_FIELD_NUMBER: _ClassVar[int]
    use_strict_string_match: bool
    def __init__(self, use_strict_string_match: bool = ...) -> None: ...

class ToolParameterKVMatchInstance(_message.Message):
    __slots__ = ("prediction", "reference")
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    def __init__(self, prediction: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ToolParameterKVMatchResults(_message.Message):
    __slots__ = ("tool_parameter_kv_match_metric_values",)
    TOOL_PARAMETER_KV_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_parameter_kv_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolParameterKVMatchMetricValue]
    def __init__(self, tool_parameter_kv_match_metric_values: _Optional[_Iterable[_Union[ToolParameterKVMatchMetricValue, _Mapping]]] = ...) -> None: ...

class ToolParameterKVMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectoryExactMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryExactMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryExactMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectoryExactMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectoryExactMatchInstance, _Mapping]]] = ...) -> None: ...

class TrajectoryExactMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TrajectoryExactMatchInstance(_message.Message):
    __slots__ = ("predicted_trajectory", "reference_trajectory")
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectoryExactMatchResults(_message.Message):
    __slots__ = ("trajectory_exact_match_metric_values",)
    TRAJECTORY_EXACT_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_exact_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryExactMatchMetricValue]
    def __init__(self, trajectory_exact_match_metric_values: _Optional[_Iterable[_Union[TrajectoryExactMatchMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectoryExactMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectoryInOrderMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryInOrderMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryInOrderMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectoryInOrderMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectoryInOrderMatchInstance, _Mapping]]] = ...) -> None: ...

class TrajectoryInOrderMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TrajectoryInOrderMatchInstance(_message.Message):
    __slots__ = ("predicted_trajectory", "reference_trajectory")
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectoryInOrderMatchResults(_message.Message):
    __slots__ = ("trajectory_in_order_match_metric_values",)
    TRAJECTORY_IN_ORDER_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_in_order_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryInOrderMatchMetricValue]
    def __init__(self, trajectory_in_order_match_metric_values: _Optional[_Iterable[_Union[TrajectoryInOrderMatchMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectoryInOrderMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectoryAnyOrderMatchInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryAnyOrderMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryAnyOrderMatchInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectoryAnyOrderMatchSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectoryAnyOrderMatchInstance, _Mapping]]] = ...) -> None: ...

class TrajectoryAnyOrderMatchSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TrajectoryAnyOrderMatchInstance(_message.Message):
    __slots__ = ("predicted_trajectory", "reference_trajectory")
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectoryAnyOrderMatchResults(_message.Message):
    __slots__ = ("trajectory_any_order_match_metric_values",)
    TRAJECTORY_ANY_ORDER_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_any_order_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryAnyOrderMatchMetricValue]
    def __init__(self, trajectory_any_order_match_metric_values: _Optional[_Iterable[_Union[TrajectoryAnyOrderMatchMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectoryAnyOrderMatchMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectoryPrecisionInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryPrecisionSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryPrecisionInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectoryPrecisionSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectoryPrecisionInstance, _Mapping]]] = ...) -> None: ...

class TrajectoryPrecisionSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TrajectoryPrecisionInstance(_message.Message):
    __slots__ = ("predicted_trajectory", "reference_trajectory")
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectoryPrecisionResults(_message.Message):
    __slots__ = ("trajectory_precision_metric_values",)
    TRAJECTORY_PRECISION_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_precision_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryPrecisionMetricValue]
    def __init__(self, trajectory_precision_metric_values: _Optional[_Iterable[_Union[TrajectoryPrecisionMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectoryPrecisionMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectoryRecallInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryRecallSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryRecallInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectoryRecallSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectoryRecallInstance, _Mapping]]] = ...) -> None: ...

class TrajectoryRecallSpec(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TrajectoryRecallInstance(_message.Message):
    __slots__ = ("predicted_trajectory", "reference_trajectory")
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectoryRecallResults(_message.Message):
    __slots__ = ("trajectory_recall_metric_values",)
    TRAJECTORY_RECALL_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_recall_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryRecallMetricValue]
    def __init__(self, trajectory_recall_metric_values: _Optional[_Iterable[_Union[TrajectoryRecallMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectoryRecallMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class TrajectorySingleToolUseInput(_message.Message):
    __slots__ = ("metric_spec", "instances")
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectorySingleToolUseSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectorySingleToolUseInstance]
    def __init__(self, metric_spec: _Optional[_Union[TrajectorySingleToolUseSpec, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[TrajectorySingleToolUseInstance, _Mapping]]] = ...) -> None: ...

class TrajectorySingleToolUseSpec(_message.Message):
    __slots__ = ("tool_name",)
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    def __init__(self, tool_name: _Optional[str] = ...) -> None: ...

class TrajectorySingleToolUseInstance(_message.Message):
    __slots__ = ("predicted_trajectory",)
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]] = ...) -> None: ...

class TrajectorySingleToolUseResults(_message.Message):
    __slots__ = ("trajectory_single_tool_use_metric_values",)
    TRAJECTORY_SINGLE_TOOL_USE_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_single_tool_use_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectorySingleToolUseMetricValue]
    def __init__(self, trajectory_single_tool_use_metric_values: _Optional[_Iterable[_Union[TrajectorySingleToolUseMetricValue, _Mapping]]] = ...) -> None: ...

class TrajectorySingleToolUseMetricValue(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...

class Trajectory(_message.Message):
    __slots__ = ("tool_calls",)
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    def __init__(self, tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("tool_name", "tool_input")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_input: str
    def __init__(self, tool_name: _Optional[str] = ..., tool_input: _Optional[str] = ...) -> None: ...
