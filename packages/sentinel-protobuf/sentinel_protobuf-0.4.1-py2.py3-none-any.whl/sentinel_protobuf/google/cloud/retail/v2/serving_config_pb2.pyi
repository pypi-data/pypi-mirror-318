from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import common_pb2 as _common_pb2
from google.cloud.retail.v2 import search_service_pb2 as _search_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServingConfig(_message.Message):
    __slots__ = ("name", "display_name", "model_id", "price_reranking_level", "facet_control_ids", "dynamic_facet_spec", "boost_control_ids", "filter_control_ids", "redirect_control_ids", "twoway_synonyms_control_ids", "oneway_synonyms_control_ids", "do_not_associate_control_ids", "replacement_control_ids", "ignore_control_ids", "diversity_level", "diversity_type", "enable_category_filter_level", "ignore_recs_denylist", "personalization_spec", "solution_types")
    class DiversityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIVERSITY_TYPE_UNSPECIFIED: _ClassVar[ServingConfig.DiversityType]
        RULE_BASED_DIVERSITY: _ClassVar[ServingConfig.DiversityType]
        DATA_DRIVEN_DIVERSITY: _ClassVar[ServingConfig.DiversityType]
    DIVERSITY_TYPE_UNSPECIFIED: ServingConfig.DiversityType
    RULE_BASED_DIVERSITY: ServingConfig.DiversityType
    DATA_DRIVEN_DIVERSITY: ServingConfig.DiversityType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_RERANKING_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FACET_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FACET_SPEC_FIELD_NUMBER: _ClassVar[int]
    BOOST_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    TWOWAY_SYNONYMS_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    ONEWAY_SYNONYMS_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_ASSOCIATE_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    DIVERSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DIVERSITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CATEGORY_FILTER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_RECS_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    model_id: str
    price_reranking_level: str
    facet_control_ids: _containers.RepeatedScalarFieldContainer[str]
    dynamic_facet_spec: _search_service_pb2.SearchRequest.DynamicFacetSpec
    boost_control_ids: _containers.RepeatedScalarFieldContainer[str]
    filter_control_ids: _containers.RepeatedScalarFieldContainer[str]
    redirect_control_ids: _containers.RepeatedScalarFieldContainer[str]
    twoway_synonyms_control_ids: _containers.RepeatedScalarFieldContainer[str]
    oneway_synonyms_control_ids: _containers.RepeatedScalarFieldContainer[str]
    do_not_associate_control_ids: _containers.RepeatedScalarFieldContainer[str]
    replacement_control_ids: _containers.RepeatedScalarFieldContainer[str]
    ignore_control_ids: _containers.RepeatedScalarFieldContainer[str]
    diversity_level: str
    diversity_type: ServingConfig.DiversityType
    enable_category_filter_level: str
    ignore_recs_denylist: bool
    personalization_spec: _search_service_pb2.SearchRequest.PersonalizationSpec
    solution_types: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., model_id: _Optional[str] = ..., price_reranking_level: _Optional[str] = ..., facet_control_ids: _Optional[_Iterable[str]] = ..., dynamic_facet_spec: _Optional[_Union[_search_service_pb2.SearchRequest.DynamicFacetSpec, _Mapping]] = ..., boost_control_ids: _Optional[_Iterable[str]] = ..., filter_control_ids: _Optional[_Iterable[str]] = ..., redirect_control_ids: _Optional[_Iterable[str]] = ..., twoway_synonyms_control_ids: _Optional[_Iterable[str]] = ..., oneway_synonyms_control_ids: _Optional[_Iterable[str]] = ..., do_not_associate_control_ids: _Optional[_Iterable[str]] = ..., replacement_control_ids: _Optional[_Iterable[str]] = ..., ignore_control_ids: _Optional[_Iterable[str]] = ..., diversity_level: _Optional[str] = ..., diversity_type: _Optional[_Union[ServingConfig.DiversityType, str]] = ..., enable_category_filter_level: _Optional[str] = ..., ignore_recs_denylist: bool = ..., personalization_spec: _Optional[_Union[_search_service_pb2.SearchRequest.PersonalizationSpec, _Mapping]] = ..., solution_types: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]] = ...) -> None: ...
