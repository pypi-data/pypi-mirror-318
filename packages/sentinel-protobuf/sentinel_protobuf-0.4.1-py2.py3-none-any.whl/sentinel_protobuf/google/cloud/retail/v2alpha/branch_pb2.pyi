from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import product_pb2 as _product_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BranchView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BRANCH_VIEW_UNSPECIFIED: _ClassVar[BranchView]
    BRANCH_VIEW_BASIC: _ClassVar[BranchView]
    BRANCH_VIEW_FULL: _ClassVar[BranchView]
BRANCH_VIEW_UNSPECIFIED: BranchView
BRANCH_VIEW_BASIC: BranchView
BRANCH_VIEW_FULL: BranchView

class Branch(_message.Message):
    __slots__ = ("name", "display_name", "is_default", "last_product_import_time", "product_count_stats", "quality_metrics")
    class ProductCountStatistic(_message.Message):
        __slots__ = ("scope", "counts")
        class ProductCountScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRODUCT_COUNT_SCOPE_UNSPECIFIED: _ClassVar[Branch.ProductCountStatistic.ProductCountScope]
            ALL_PRODUCTS: _ClassVar[Branch.ProductCountStatistic.ProductCountScope]
            LAST_24_HOUR_UPDATE: _ClassVar[Branch.ProductCountStatistic.ProductCountScope]
        PRODUCT_COUNT_SCOPE_UNSPECIFIED: Branch.ProductCountStatistic.ProductCountScope
        ALL_PRODUCTS: Branch.ProductCountStatistic.ProductCountScope
        LAST_24_HOUR_UPDATE: Branch.ProductCountStatistic.ProductCountScope
        class CountsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        COUNTS_FIELD_NUMBER: _ClassVar[int]
        scope: Branch.ProductCountStatistic.ProductCountScope
        counts: _containers.ScalarMap[str, int]
        def __init__(self, scope: _Optional[_Union[Branch.ProductCountStatistic.ProductCountScope, str]] = ..., counts: _Optional[_Mapping[str, int]] = ...) -> None: ...
    class QualityMetric(_message.Message):
        __slots__ = ("requirement_key", "qualified_product_count", "unqualified_product_count", "suggested_quality_percent_threshold", "unqualified_sample_products")
        REQUIREMENT_KEY_FIELD_NUMBER: _ClassVar[int]
        QUALIFIED_PRODUCT_COUNT_FIELD_NUMBER: _ClassVar[int]
        UNQUALIFIED_PRODUCT_COUNT_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_QUALITY_PERCENT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        UNQUALIFIED_SAMPLE_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        requirement_key: str
        qualified_product_count: int
        unqualified_product_count: int
        suggested_quality_percent_threshold: float
        unqualified_sample_products: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
        def __init__(self, requirement_key: _Optional[str] = ..., qualified_product_count: _Optional[int] = ..., unqualified_product_count: _Optional[int] = ..., suggested_quality_percent_threshold: _Optional[float] = ..., unqualified_sample_products: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LAST_PRODUCT_IMPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COUNT_STATS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    is_default: bool
    last_product_import_time: _timestamp_pb2.Timestamp
    product_count_stats: _containers.RepeatedCompositeFieldContainer[Branch.ProductCountStatistic]
    quality_metrics: _containers.RepeatedCompositeFieldContainer[Branch.QualityMetric]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., is_default: bool = ..., last_product_import_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., product_count_stats: _Optional[_Iterable[_Union[Branch.ProductCountStatistic, _Mapping]]] = ..., quality_metrics: _Optional[_Iterable[_Union[Branch.QualityMetric, _Mapping]]] = ...) -> None: ...
