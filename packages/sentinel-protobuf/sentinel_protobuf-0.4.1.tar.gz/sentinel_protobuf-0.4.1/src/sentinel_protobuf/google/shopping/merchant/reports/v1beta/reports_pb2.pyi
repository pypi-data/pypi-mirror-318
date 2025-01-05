from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchRequest(_message.Message):
    __slots__ = ("parent", "query", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., query: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("results", "next_page_token")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ReportRow]
    next_page_token: str
    def __init__(self, results: _Optional[_Iterable[_Union[ReportRow, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportRow(_message.Message):
    __slots__ = ("product_performance_view", "non_product_performance_view", "product_view", "price_competitiveness_product_view", "price_insights_product_view", "best_sellers_product_cluster_view", "best_sellers_brand_view", "competitive_visibility_competitor_view", "competitive_visibility_top_merchant_view", "competitive_visibility_benchmark_view")
    PRODUCT_PERFORMANCE_VIEW_FIELD_NUMBER: _ClassVar[int]
    NON_PRODUCT_PERFORMANCE_VIEW_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_VIEW_FIELD_NUMBER: _ClassVar[int]
    PRICE_COMPETITIVENESS_PRODUCT_VIEW_FIELD_NUMBER: _ClassVar[int]
    PRICE_INSIGHTS_PRODUCT_VIEW_FIELD_NUMBER: _ClassVar[int]
    BEST_SELLERS_PRODUCT_CLUSTER_VIEW_FIELD_NUMBER: _ClassVar[int]
    BEST_SELLERS_BRAND_VIEW_FIELD_NUMBER: _ClassVar[int]
    COMPETITIVE_VISIBILITY_COMPETITOR_VIEW_FIELD_NUMBER: _ClassVar[int]
    COMPETITIVE_VISIBILITY_TOP_MERCHANT_VIEW_FIELD_NUMBER: _ClassVar[int]
    COMPETITIVE_VISIBILITY_BENCHMARK_VIEW_FIELD_NUMBER: _ClassVar[int]
    product_performance_view: ProductPerformanceView
    non_product_performance_view: NonProductPerformanceView
    product_view: ProductView
    price_competitiveness_product_view: PriceCompetitivenessProductView
    price_insights_product_view: PriceInsightsProductView
    best_sellers_product_cluster_view: BestSellersProductClusterView
    best_sellers_brand_view: BestSellersBrandView
    competitive_visibility_competitor_view: CompetitiveVisibilityCompetitorView
    competitive_visibility_top_merchant_view: CompetitiveVisibilityTopMerchantView
    competitive_visibility_benchmark_view: CompetitiveVisibilityBenchmarkView
    def __init__(self, product_performance_view: _Optional[_Union[ProductPerformanceView, _Mapping]] = ..., non_product_performance_view: _Optional[_Union[NonProductPerformanceView, _Mapping]] = ..., product_view: _Optional[_Union[ProductView, _Mapping]] = ..., price_competitiveness_product_view: _Optional[_Union[PriceCompetitivenessProductView, _Mapping]] = ..., price_insights_product_view: _Optional[_Union[PriceInsightsProductView, _Mapping]] = ..., best_sellers_product_cluster_view: _Optional[_Union[BestSellersProductClusterView, _Mapping]] = ..., best_sellers_brand_view: _Optional[_Union[BestSellersBrandView, _Mapping]] = ..., competitive_visibility_competitor_view: _Optional[_Union[CompetitiveVisibilityCompetitorView, _Mapping]] = ..., competitive_visibility_top_merchant_view: _Optional[_Union[CompetitiveVisibilityTopMerchantView, _Mapping]] = ..., competitive_visibility_benchmark_view: _Optional[_Union[CompetitiveVisibilityBenchmarkView, _Mapping]] = ...) -> None: ...

class ProductPerformanceView(_message.Message):
    __slots__ = ("marketing_method", "date", "week", "customer_country_code", "offer_id", "title", "brand", "category_l1", "category_l2", "category_l3", "category_l4", "category_l5", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "custom_label0", "custom_label1", "custom_label2", "custom_label3", "custom_label4", "clicks", "impressions", "click_through_rate", "conversions", "conversion_value", "conversion_rate")
    MARKETING_METHOD_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL0_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL1_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL2_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL3_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL4_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_RATE_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
    marketing_method: MarketingMethod.MarketingMethodEnum
    date: _date_pb2.Date
    week: _date_pb2.Date
    customer_country_code: str
    offer_id: str
    title: str
    brand: str
    category_l1: str
    category_l2: str
    category_l3: str
    category_l4: str
    category_l5: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    custom_label0: str
    custom_label1: str
    custom_label2: str
    custom_label3: str
    custom_label4: str
    clicks: int
    impressions: int
    click_through_rate: float
    conversions: float
    conversion_value: _types_pb2.Price
    conversion_rate: float
    def __init__(self, marketing_method: _Optional[_Union[MarketingMethod.MarketingMethodEnum, str]] = ..., date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., week: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., customer_country_code: _Optional[str] = ..., offer_id: _Optional[str] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., category_l1: _Optional[str] = ..., category_l2: _Optional[str] = ..., category_l3: _Optional[str] = ..., category_l4: _Optional[str] = ..., category_l5: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., custom_label0: _Optional[str] = ..., custom_label1: _Optional[str] = ..., custom_label2: _Optional[str] = ..., custom_label3: _Optional[str] = ..., custom_label4: _Optional[str] = ..., clicks: _Optional[int] = ..., impressions: _Optional[int] = ..., click_through_rate: _Optional[float] = ..., conversions: _Optional[float] = ..., conversion_value: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., conversion_rate: _Optional[float] = ...) -> None: ...

class ProductView(_message.Message):
    __slots__ = ("id", "channel", "language_code", "feed_label", "offer_id", "title", "brand", "category_l1", "category_l2", "category_l3", "category_l4", "category_l5", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "price", "condition", "availability", "shipping_label", "gtin", "item_group_id", "thumbnail_link", "creation_time", "expiration_date", "aggregated_reporting_context_status", "item_issues", "click_potential", "click_potential_rank")
    class AggregatedReportingContextStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATED_REPORTING_CONTEXT_STATUS_UNSPECIFIED: _ClassVar[ProductView.AggregatedReportingContextStatus]
        NOT_ELIGIBLE_OR_DISAPPROVED: _ClassVar[ProductView.AggregatedReportingContextStatus]
        PENDING: _ClassVar[ProductView.AggregatedReportingContextStatus]
        ELIGIBLE_LIMITED: _ClassVar[ProductView.AggregatedReportingContextStatus]
        ELIGIBLE: _ClassVar[ProductView.AggregatedReportingContextStatus]
    AGGREGATED_REPORTING_CONTEXT_STATUS_UNSPECIFIED: ProductView.AggregatedReportingContextStatus
    NOT_ELIGIBLE_OR_DISAPPROVED: ProductView.AggregatedReportingContextStatus
    PENDING: ProductView.AggregatedReportingContextStatus
    ELIGIBLE_LIMITED: ProductView.AggregatedReportingContextStatus
    ELIGIBLE: ProductView.AggregatedReportingContextStatus
    class ClickPotential(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLICK_POTENTIAL_UNSPECIFIED: _ClassVar[ProductView.ClickPotential]
        LOW: _ClassVar[ProductView.ClickPotential]
        MEDIUM: _ClassVar[ProductView.ClickPotential]
        HIGH: _ClassVar[ProductView.ClickPotential]
    CLICK_POTENTIAL_UNSPECIFIED: ProductView.ClickPotential
    LOW: ProductView.ClickPotential
    MEDIUM: ProductView.ClickPotential
    HIGH: ProductView.ClickPotential
    class ItemIssue(_message.Message):
        __slots__ = ("type", "severity", "resolution")
        class ItemIssueResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ITEM_ISSUE_RESOLUTION_UNSPECIFIED: _ClassVar[ProductView.ItemIssue.ItemIssueResolution]
            MERCHANT_ACTION: _ClassVar[ProductView.ItemIssue.ItemIssueResolution]
            PENDING_PROCESSING: _ClassVar[ProductView.ItemIssue.ItemIssueResolution]
        ITEM_ISSUE_RESOLUTION_UNSPECIFIED: ProductView.ItemIssue.ItemIssueResolution
        MERCHANT_ACTION: ProductView.ItemIssue.ItemIssueResolution
        PENDING_PROCESSING: ProductView.ItemIssue.ItemIssueResolution
        class ItemIssueType(_message.Message):
            __slots__ = ("code", "canonical_attribute")
            CODE_FIELD_NUMBER: _ClassVar[int]
            CANONICAL_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
            code: str
            canonical_attribute: str
            def __init__(self, code: _Optional[str] = ..., canonical_attribute: _Optional[str] = ...) -> None: ...
        class ItemIssueSeverity(_message.Message):
            __slots__ = ("severity_per_reporting_context", "aggregated_severity")
            class AggregatedIssueSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED: _ClassVar[ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity]
                DISAPPROVED: _ClassVar[ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity]
                DEMOTED: _ClassVar[ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity]
                PENDING: _ClassVar[ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity]
            AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED: ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity
            DISAPPROVED: ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity
            DEMOTED: ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity
            PENDING: ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity
            class IssueSeverityPerReportingContext(_message.Message):
                __slots__ = ("reporting_context", "disapproved_countries", "demoted_countries")
                REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
                DISAPPROVED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
                DEMOTED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
                reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
                disapproved_countries: _containers.RepeatedScalarFieldContainer[str]
                demoted_countries: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., disapproved_countries: _Optional[_Iterable[str]] = ..., demoted_countries: _Optional[_Iterable[str]] = ...) -> None: ...
            SEVERITY_PER_REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
            AGGREGATED_SEVERITY_FIELD_NUMBER: _ClassVar[int]
            severity_per_reporting_context: _containers.RepeatedCompositeFieldContainer[ProductView.ItemIssue.ItemIssueSeverity.IssueSeverityPerReportingContext]
            aggregated_severity: ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity
            def __init__(self, severity_per_reporting_context: _Optional[_Iterable[_Union[ProductView.ItemIssue.ItemIssueSeverity.IssueSeverityPerReportingContext, _Mapping]]] = ..., aggregated_severity: _Optional[_Union[ProductView.ItemIssue.ItemIssueSeverity.AggregatedIssueSeverity, str]] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        type: ProductView.ItemIssue.ItemIssueType
        severity: ProductView.ItemIssue.ItemIssueSeverity
        resolution: ProductView.ItemIssue.ItemIssueResolution
        def __init__(self, type: _Optional[_Union[ProductView.ItemIssue.ItemIssueType, _Mapping]] = ..., severity: _Optional[_Union[ProductView.ItemIssue.ItemIssueSeverity, _Mapping]] = ..., resolution: _Optional[_Union[ProductView.ItemIssue.ItemIssueResolution, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_LABEL_FIELD_NUMBER: _ClassVar[int]
    GTIN_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_REPORTING_CONTEXT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEM_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CLICK_POTENTIAL_FIELD_NUMBER: _ClassVar[int]
    CLICK_POTENTIAL_RANK_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel: _types_pb2.Channel.ChannelEnum
    language_code: str
    feed_label: str
    offer_id: str
    title: str
    brand: str
    category_l1: str
    category_l2: str
    category_l3: str
    category_l4: str
    category_l5: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    price: _types_pb2.Price
    condition: str
    availability: str
    shipping_label: str
    gtin: _containers.RepeatedScalarFieldContainer[str]
    item_group_id: str
    thumbnail_link: str
    creation_time: _timestamp_pb2.Timestamp
    expiration_date: _date_pb2.Date
    aggregated_reporting_context_status: ProductView.AggregatedReportingContextStatus
    item_issues: _containers.RepeatedCompositeFieldContainer[ProductView.ItemIssue]
    click_potential: ProductView.ClickPotential
    click_potential_rank: int
    def __init__(self, id: _Optional[str] = ..., channel: _Optional[_Union[_types_pb2.Channel.ChannelEnum, str]] = ..., language_code: _Optional[str] = ..., feed_label: _Optional[str] = ..., offer_id: _Optional[str] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., category_l1: _Optional[str] = ..., category_l2: _Optional[str] = ..., category_l3: _Optional[str] = ..., category_l4: _Optional[str] = ..., category_l5: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., condition: _Optional[str] = ..., availability: _Optional[str] = ..., shipping_label: _Optional[str] = ..., gtin: _Optional[_Iterable[str]] = ..., item_group_id: _Optional[str] = ..., thumbnail_link: _Optional[str] = ..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., aggregated_reporting_context_status: _Optional[_Union[ProductView.AggregatedReportingContextStatus, str]] = ..., item_issues: _Optional[_Iterable[_Union[ProductView.ItemIssue, _Mapping]]] = ..., click_potential: _Optional[_Union[ProductView.ClickPotential, str]] = ..., click_potential_rank: _Optional[int] = ...) -> None: ...

class PriceCompetitivenessProductView(_message.Message):
    __slots__ = ("report_country_code", "id", "offer_id", "title", "brand", "category_l1", "category_l2", "category_l3", "category_l4", "category_l5", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "price", "benchmark_price")
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    BENCHMARK_PRICE_FIELD_NUMBER: _ClassVar[int]
    report_country_code: str
    id: str
    offer_id: str
    title: str
    brand: str
    category_l1: str
    category_l2: str
    category_l3: str
    category_l4: str
    category_l5: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    price: _types_pb2.Price
    benchmark_price: _types_pb2.Price
    def __init__(self, report_country_code: _Optional[str] = ..., id: _Optional[str] = ..., offer_id: _Optional[str] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., category_l1: _Optional[str] = ..., category_l2: _Optional[str] = ..., category_l3: _Optional[str] = ..., category_l4: _Optional[str] = ..., category_l5: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., benchmark_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ...) -> None: ...

class PriceInsightsProductView(_message.Message):
    __slots__ = ("id", "offer_id", "title", "brand", "category_l1", "category_l2", "category_l3", "category_l4", "category_l5", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "price", "suggested_price", "predicted_impressions_change_fraction", "predicted_clicks_change_fraction", "predicted_conversions_change_fraction", "effectiveness")
    class Effectiveness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECTIVENESS_UNSPECIFIED: _ClassVar[PriceInsightsProductView.Effectiveness]
        LOW: _ClassVar[PriceInsightsProductView.Effectiveness]
        MEDIUM: _ClassVar[PriceInsightsProductView.Effectiveness]
        HIGH: _ClassVar[PriceInsightsProductView.Effectiveness]
    EFFECTIVENESS_UNSPECIFIED: PriceInsightsProductView.Effectiveness
    LOW: PriceInsightsProductView.Effectiveness
    MEDIUM: PriceInsightsProductView.Effectiveness
    HIGH: PriceInsightsProductView.Effectiveness
    ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_PRICE_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_IMPRESSIONS_CHANGE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_CLICKS_CHANGE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    PREDICTED_CONVERSIONS_CHANGE_FRACTION_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVENESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    offer_id: str
    title: str
    brand: str
    category_l1: str
    category_l2: str
    category_l3: str
    category_l4: str
    category_l5: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    price: _types_pb2.Price
    suggested_price: _types_pb2.Price
    predicted_impressions_change_fraction: float
    predicted_clicks_change_fraction: float
    predicted_conversions_change_fraction: float
    effectiveness: PriceInsightsProductView.Effectiveness
    def __init__(self, id: _Optional[str] = ..., offer_id: _Optional[str] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., category_l1: _Optional[str] = ..., category_l2: _Optional[str] = ..., category_l3: _Optional[str] = ..., category_l4: _Optional[str] = ..., category_l5: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., suggested_price: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., predicted_impressions_change_fraction: _Optional[float] = ..., predicted_clicks_change_fraction: _Optional[float] = ..., predicted_conversions_change_fraction: _Optional[float] = ..., effectiveness: _Optional[_Union[PriceInsightsProductView.Effectiveness, str]] = ...) -> None: ...

class BestSellersProductClusterView(_message.Message):
    __slots__ = ("report_date", "report_granularity", "report_country_code", "report_category_id", "title", "brand", "category_l1", "category_l2", "category_l3", "category_l4", "category_l5", "variant_gtins", "inventory_status", "brand_inventory_status", "rank", "previous_rank", "relative_demand", "previous_relative_demand", "relative_demand_change")
    class InventoryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVENTORY_STATUS_UNSPECIFIED: _ClassVar[BestSellersProductClusterView.InventoryStatus]
        IN_STOCK: _ClassVar[BestSellersProductClusterView.InventoryStatus]
        OUT_OF_STOCK: _ClassVar[BestSellersProductClusterView.InventoryStatus]
        NOT_IN_INVENTORY: _ClassVar[BestSellersProductClusterView.InventoryStatus]
    INVENTORY_STATUS_UNSPECIFIED: BestSellersProductClusterView.InventoryStatus
    IN_STOCK: BestSellersProductClusterView.InventoryStatus
    OUT_OF_STOCK: BestSellersProductClusterView.InventoryStatus
    NOT_IN_INVENTORY: BestSellersProductClusterView.InventoryStatus
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    REPORT_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_L5_FIELD_NUMBER: _ClassVar[int]
    VARIANT_GTINS_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_STATUS_FIELD_NUMBER: _ClassVar[int]
    BRAND_INVENTORY_STATUS_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RANK_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DEMAND_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RELATIVE_DEMAND_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DEMAND_CHANGE_FIELD_NUMBER: _ClassVar[int]
    report_date: _date_pb2.Date
    report_granularity: ReportGranularity.ReportGranularityEnum
    report_country_code: str
    report_category_id: int
    title: str
    brand: str
    category_l1: str
    category_l2: str
    category_l3: str
    category_l4: str
    category_l5: str
    variant_gtins: _containers.RepeatedScalarFieldContainer[str]
    inventory_status: BestSellersProductClusterView.InventoryStatus
    brand_inventory_status: BestSellersProductClusterView.InventoryStatus
    rank: int
    previous_rank: int
    relative_demand: RelativeDemand.RelativeDemandEnum
    previous_relative_demand: RelativeDemand.RelativeDemandEnum
    relative_demand_change: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    def __init__(self, report_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., report_granularity: _Optional[_Union[ReportGranularity.ReportGranularityEnum, str]] = ..., report_country_code: _Optional[str] = ..., report_category_id: _Optional[int] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., category_l1: _Optional[str] = ..., category_l2: _Optional[str] = ..., category_l3: _Optional[str] = ..., category_l4: _Optional[str] = ..., category_l5: _Optional[str] = ..., variant_gtins: _Optional[_Iterable[str]] = ..., inventory_status: _Optional[_Union[BestSellersProductClusterView.InventoryStatus, str]] = ..., brand_inventory_status: _Optional[_Union[BestSellersProductClusterView.InventoryStatus, str]] = ..., rank: _Optional[int] = ..., previous_rank: _Optional[int] = ..., relative_demand: _Optional[_Union[RelativeDemand.RelativeDemandEnum, str]] = ..., previous_relative_demand: _Optional[_Union[RelativeDemand.RelativeDemandEnum, str]] = ..., relative_demand_change: _Optional[_Union[RelativeDemandChangeType.RelativeDemandChangeTypeEnum, str]] = ...) -> None: ...

class BestSellersBrandView(_message.Message):
    __slots__ = ("report_date", "report_granularity", "report_country_code", "report_category_id", "brand", "rank", "previous_rank", "relative_demand", "previous_relative_demand", "relative_demand_change")
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    REPORT_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RANK_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DEMAND_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RELATIVE_DEMAND_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DEMAND_CHANGE_FIELD_NUMBER: _ClassVar[int]
    report_date: _date_pb2.Date
    report_granularity: ReportGranularity.ReportGranularityEnum
    report_country_code: str
    report_category_id: int
    brand: str
    rank: int
    previous_rank: int
    relative_demand: RelativeDemand.RelativeDemandEnum
    previous_relative_demand: RelativeDemand.RelativeDemandEnum
    relative_demand_change: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    def __init__(self, report_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., report_granularity: _Optional[_Union[ReportGranularity.ReportGranularityEnum, str]] = ..., report_country_code: _Optional[str] = ..., report_category_id: _Optional[int] = ..., brand: _Optional[str] = ..., rank: _Optional[int] = ..., previous_rank: _Optional[int] = ..., relative_demand: _Optional[_Union[RelativeDemand.RelativeDemandEnum, str]] = ..., previous_relative_demand: _Optional[_Union[RelativeDemand.RelativeDemandEnum, str]] = ..., relative_demand_change: _Optional[_Union[RelativeDemandChangeType.RelativeDemandChangeTypeEnum, str]] = ...) -> None: ...

class NonProductPerformanceView(_message.Message):
    __slots__ = ("date", "week", "clicks", "impressions", "click_through_rate")
    DATE_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_RATE_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    week: _date_pb2.Date
    clicks: int
    impressions: int
    click_through_rate: float
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., week: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., clicks: _Optional[int] = ..., impressions: _Optional[int] = ..., click_through_rate: _Optional[float] = ...) -> None: ...

class CompetitiveVisibilityCompetitorView(_message.Message):
    __slots__ = ("date", "domain", "is_your_domain", "report_country_code", "report_category_id", "traffic_source", "rank", "ads_organic_ratio", "page_overlap_rate", "higher_position_rate", "relative_visibility")
    DATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IS_YOUR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    ADS_ORGANIC_RATIO_FIELD_NUMBER: _ClassVar[int]
    PAGE_OVERLAP_RATE_FIELD_NUMBER: _ClassVar[int]
    HIGHER_POSITION_RATE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    domain: str
    is_your_domain: bool
    report_country_code: str
    report_category_id: int
    traffic_source: TrafficSource.TrafficSourceEnum
    rank: int
    ads_organic_ratio: float
    page_overlap_rate: float
    higher_position_rate: float
    relative_visibility: float
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., domain: _Optional[str] = ..., is_your_domain: bool = ..., report_country_code: _Optional[str] = ..., report_category_id: _Optional[int] = ..., traffic_source: _Optional[_Union[TrafficSource.TrafficSourceEnum, str]] = ..., rank: _Optional[int] = ..., ads_organic_ratio: _Optional[float] = ..., page_overlap_rate: _Optional[float] = ..., higher_position_rate: _Optional[float] = ..., relative_visibility: _Optional[float] = ...) -> None: ...

class CompetitiveVisibilityTopMerchantView(_message.Message):
    __slots__ = ("date", "domain", "is_your_domain", "report_country_code", "report_category_id", "traffic_source", "rank", "ads_organic_ratio", "page_overlap_rate", "higher_position_rate")
    DATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IS_YOUR_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    ADS_ORGANIC_RATIO_FIELD_NUMBER: _ClassVar[int]
    PAGE_OVERLAP_RATE_FIELD_NUMBER: _ClassVar[int]
    HIGHER_POSITION_RATE_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    domain: str
    is_your_domain: bool
    report_country_code: str
    report_category_id: int
    traffic_source: TrafficSource.TrafficSourceEnum
    rank: int
    ads_organic_ratio: float
    page_overlap_rate: float
    higher_position_rate: float
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., domain: _Optional[str] = ..., is_your_domain: bool = ..., report_country_code: _Optional[str] = ..., report_category_id: _Optional[int] = ..., traffic_source: _Optional[_Union[TrafficSource.TrafficSourceEnum, str]] = ..., rank: _Optional[int] = ..., ads_organic_ratio: _Optional[float] = ..., page_overlap_rate: _Optional[float] = ..., higher_position_rate: _Optional[float] = ...) -> None: ...

class CompetitiveVisibilityBenchmarkView(_message.Message):
    __slots__ = ("date", "report_country_code", "report_category_id", "traffic_source", "your_domain_visibility_trend", "category_benchmark_visibility_trend")
    DATE_FIELD_NUMBER: _ClassVar[int]
    REPORT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REPORT_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SOURCE_FIELD_NUMBER: _ClassVar[int]
    YOUR_DOMAIN_VISIBILITY_TREND_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_BENCHMARK_VISIBILITY_TREND_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    report_country_code: str
    report_category_id: int
    traffic_source: TrafficSource.TrafficSourceEnum
    your_domain_visibility_trend: float
    category_benchmark_visibility_trend: float
    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., report_country_code: _Optional[str] = ..., report_category_id: _Optional[int] = ..., traffic_source: _Optional[_Union[TrafficSource.TrafficSourceEnum, str]] = ..., your_domain_visibility_trend: _Optional[float] = ..., category_benchmark_visibility_trend: _Optional[float] = ...) -> None: ...

class MarketingMethod(_message.Message):
    __slots__ = ()
    class MarketingMethodEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MARKETING_METHOD_ENUM_UNSPECIFIED: _ClassVar[MarketingMethod.MarketingMethodEnum]
        ORGANIC: _ClassVar[MarketingMethod.MarketingMethodEnum]
        ADS: _ClassVar[MarketingMethod.MarketingMethodEnum]
    MARKETING_METHOD_ENUM_UNSPECIFIED: MarketingMethod.MarketingMethodEnum
    ORGANIC: MarketingMethod.MarketingMethodEnum
    ADS: MarketingMethod.MarketingMethodEnum
    def __init__(self) -> None: ...

class ReportGranularity(_message.Message):
    __slots__ = ()
    class ReportGranularityEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORT_GRANULARITY_ENUM_UNSPECIFIED: _ClassVar[ReportGranularity.ReportGranularityEnum]
        WEEKLY: _ClassVar[ReportGranularity.ReportGranularityEnum]
        MONTHLY: _ClassVar[ReportGranularity.ReportGranularityEnum]
    REPORT_GRANULARITY_ENUM_UNSPECIFIED: ReportGranularity.ReportGranularityEnum
    WEEKLY: ReportGranularity.ReportGranularityEnum
    MONTHLY: ReportGranularity.ReportGranularityEnum
    def __init__(self) -> None: ...

class RelativeDemand(_message.Message):
    __slots__ = ()
    class RelativeDemandEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELATIVE_DEMAND_ENUM_UNSPECIFIED: _ClassVar[RelativeDemand.RelativeDemandEnum]
        VERY_LOW: _ClassVar[RelativeDemand.RelativeDemandEnum]
        LOW: _ClassVar[RelativeDemand.RelativeDemandEnum]
        MEDIUM: _ClassVar[RelativeDemand.RelativeDemandEnum]
        HIGH: _ClassVar[RelativeDemand.RelativeDemandEnum]
        VERY_HIGH: _ClassVar[RelativeDemand.RelativeDemandEnum]
    RELATIVE_DEMAND_ENUM_UNSPECIFIED: RelativeDemand.RelativeDemandEnum
    VERY_LOW: RelativeDemand.RelativeDemandEnum
    LOW: RelativeDemand.RelativeDemandEnum
    MEDIUM: RelativeDemand.RelativeDemandEnum
    HIGH: RelativeDemand.RelativeDemandEnum
    VERY_HIGH: RelativeDemand.RelativeDemandEnum
    def __init__(self) -> None: ...

class RelativeDemandChangeType(_message.Message):
    __slots__ = ()
    class RelativeDemandChangeTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED: _ClassVar[RelativeDemandChangeType.RelativeDemandChangeTypeEnum]
        SINKER: _ClassVar[RelativeDemandChangeType.RelativeDemandChangeTypeEnum]
        FLAT: _ClassVar[RelativeDemandChangeType.RelativeDemandChangeTypeEnum]
        RISER: _ClassVar[RelativeDemandChangeType.RelativeDemandChangeTypeEnum]
    RELATIVE_DEMAND_CHANGE_TYPE_ENUM_UNSPECIFIED: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    SINKER: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    FLAT: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    RISER: RelativeDemandChangeType.RelativeDemandChangeTypeEnum
    def __init__(self) -> None: ...

class TrafficSource(_message.Message):
    __slots__ = ()
    class TrafficSourceEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAFFIC_SOURCE_ENUM_UNSPECIFIED: _ClassVar[TrafficSource.TrafficSourceEnum]
        ORGANIC: _ClassVar[TrafficSource.TrafficSourceEnum]
        ADS: _ClassVar[TrafficSource.TrafficSourceEnum]
        ALL: _ClassVar[TrafficSource.TrafficSourceEnum]
    TRAFFIC_SOURCE_ENUM_UNSPECIFIED: TrafficSource.TrafficSourceEnum
    ORGANIC: TrafficSource.TrafficSourceEnum
    ADS: TrafficSource.TrafficSourceEnum
    ALL: TrafficSource.TrafficSourceEnum
    def __init__(self) -> None: ...
