from google.ads.googleads.v16.enums import sk_ad_network_coarse_conversion_value_pb2 as _sk_ad_network_coarse_conversion_value_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerSkAdNetworkConversionValueSchema(_message.Message):
    __slots__ = ('resource_name', 'schema')

    class SkAdNetworkConversionValueSchema(_message.Message):
        __slots__ = ('app_id', 'measurement_window_hours', 'fine_grained_conversion_value_mappings', 'postback_mappings')

        class FineGrainedConversionValueMappings(_message.Message):
            __slots__ = ('fine_grained_conversion_value', 'conversion_value_mapping')
            FINE_GRAINED_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
            CONVERSION_VALUE_MAPPING_FIELD_NUMBER: _ClassVar[int]
            fine_grained_conversion_value: int
            conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping

            def __init__(self, fine_grained_conversion_value: _Optional[int]=..., conversion_value_mapping: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping, _Mapping]]=...) -> None:
                ...

        class PostbackMapping(_message.Message):
            __slots__ = ('postback_sequence_index', 'coarse_grained_conversion_value_mappings', 'lock_window_coarse_conversion_value', 'lock_window_fine_conversion_value', 'lock_window_event')
            POSTBACK_SEQUENCE_INDEX_FIELD_NUMBER: _ClassVar[int]
            COARSE_GRAINED_CONVERSION_VALUE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
            LOCK_WINDOW_COARSE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
            LOCK_WINDOW_FINE_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
            LOCK_WINDOW_EVENT_FIELD_NUMBER: _ClassVar[int]
            postback_sequence_index: int
            coarse_grained_conversion_value_mappings: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.CoarseGrainedConversionValueMappings
            lock_window_coarse_conversion_value: _sk_ad_network_coarse_conversion_value_pb2.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
            lock_window_fine_conversion_value: int
            lock_window_event: str

            def __init__(self, postback_sequence_index: _Optional[int]=..., coarse_grained_conversion_value_mappings: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.CoarseGrainedConversionValueMappings, _Mapping]]=..., lock_window_coarse_conversion_value: _Optional[_Union[_sk_ad_network_coarse_conversion_value_pb2.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue, str]]=..., lock_window_fine_conversion_value: _Optional[int]=..., lock_window_event: _Optional[str]=...) -> None:
                ...

        class CoarseGrainedConversionValueMappings(_message.Message):
            __slots__ = ('low_conversion_value_mapping', 'medium_conversion_value_mapping', 'high_conversion_value_mapping')
            LOW_CONVERSION_VALUE_MAPPING_FIELD_NUMBER: _ClassVar[int]
            MEDIUM_CONVERSION_VALUE_MAPPING_FIELD_NUMBER: _ClassVar[int]
            HIGH_CONVERSION_VALUE_MAPPING_FIELD_NUMBER: _ClassVar[int]
            low_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            medium_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping
            high_conversion_value_mapping: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping

            def __init__(self, low_conversion_value_mapping: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping, _Mapping]]=..., medium_conversion_value_mapping: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping, _Mapping]]=..., high_conversion_value_mapping: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.ConversionValueMapping, _Mapping]]=...) -> None:
                ...

        class ConversionValueMapping(_message.Message):
            __slots__ = ('min_time_post_install_hours', 'max_time_post_install_hours', 'mapped_events')
            MIN_TIME_POST_INSTALL_HOURS_FIELD_NUMBER: _ClassVar[int]
            MAX_TIME_POST_INSTALL_HOURS_FIELD_NUMBER: _ClassVar[int]
            MAPPED_EVENTS_FIELD_NUMBER: _ClassVar[int]
            min_time_post_install_hours: int
            max_time_post_install_hours: int
            mapped_events: _containers.RepeatedCompositeFieldContainer[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event]

            def __init__(self, min_time_post_install_hours: _Optional[int]=..., max_time_post_install_hours: _Optional[int]=..., mapped_events: _Optional[_Iterable[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event, _Mapping]]]=...) -> None:
                ...

        class Event(_message.Message):
            __slots__ = ('mapped_event_name', 'currency_code', 'event_revenue_range', 'event_revenue_value', 'event_occurrence_range', 'event_counter')

            class RevenueRange(_message.Message):
                __slots__ = ('min_event_revenue', 'max_event_revenue')
                MIN_EVENT_REVENUE_FIELD_NUMBER: _ClassVar[int]
                MAX_EVENT_REVENUE_FIELD_NUMBER: _ClassVar[int]
                min_event_revenue: float
                max_event_revenue: float

                def __init__(self, min_event_revenue: _Optional[float]=..., max_event_revenue: _Optional[float]=...) -> None:
                    ...

            class EventOccurrenceRange(_message.Message):
                __slots__ = ('min_event_count', 'max_event_count')
                MIN_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
                MAX_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
                min_event_count: int
                max_event_count: int

                def __init__(self, min_event_count: _Optional[int]=..., max_event_count: _Optional[int]=...) -> None:
                    ...
            MAPPED_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
            CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
            EVENT_REVENUE_RANGE_FIELD_NUMBER: _ClassVar[int]
            EVENT_REVENUE_VALUE_FIELD_NUMBER: _ClassVar[int]
            EVENT_OCCURRENCE_RANGE_FIELD_NUMBER: _ClassVar[int]
            EVENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
            mapped_event_name: str
            currency_code: str
            event_revenue_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange
            event_revenue_value: float
            event_occurrence_range: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange
            event_counter: int

            def __init__(self, mapped_event_name: _Optional[str]=..., currency_code: _Optional[str]=..., event_revenue_range: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.RevenueRange, _Mapping]]=..., event_revenue_value: _Optional[float]=..., event_occurrence_range: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.Event.EventOccurrenceRange, _Mapping]]=..., event_counter: _Optional[int]=...) -> None:
                ...
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        MEASUREMENT_WINDOW_HOURS_FIELD_NUMBER: _ClassVar[int]
        FINE_GRAINED_CONVERSION_VALUE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
        POSTBACK_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
        app_id: str
        measurement_window_hours: int
        fine_grained_conversion_value_mappings: _containers.RepeatedCompositeFieldContainer[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings]
        postback_mappings: _containers.RepeatedCompositeFieldContainer[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.PostbackMapping]

        def __init__(self, app_id: _Optional[str]=..., measurement_window_hours: _Optional[int]=..., fine_grained_conversion_value_mappings: _Optional[_Iterable[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.FineGrainedConversionValueMappings, _Mapping]]]=..., postback_mappings: _Optional[_Iterable[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema.PostbackMapping, _Mapping]]]=...) -> None:
            ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    schema: CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema

    def __init__(self, resource_name: _Optional[str]=..., schema: _Optional[_Union[CustomerSkAdNetworkConversionValueSchema.SkAdNetworkConversionValueSchema, _Mapping]]=...) -> None:
        ...