from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShippingSettings(_message.Message):
    __slots__ = ("name", "services", "warehouses", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    services: _containers.RepeatedCompositeFieldContainer[Service]
    warehouses: _containers.RepeatedCompositeFieldContainer[Warehouse]
    etag: str
    def __init__(self, name: _Optional[str] = ..., services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., warehouses: _Optional[_Iterable[_Union[Warehouse, _Mapping]]] = ..., etag: _Optional[str] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("service_name", "active", "delivery_countries", "currency_code", "delivery_time", "rate_groups", "shipment_type", "minimum_order_value", "minimum_order_value_table", "store_config", "loyalty_programs")
    class ShipmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHIPMENT_TYPE_UNSPECIFIED: _ClassVar[Service.ShipmentType]
        DELIVERY: _ClassVar[Service.ShipmentType]
        LOCAL_DELIVERY: _ClassVar[Service.ShipmentType]
        COLLECTION_POINT: _ClassVar[Service.ShipmentType]
    SHIPMENT_TYPE_UNSPECIFIED: Service.ShipmentType
    DELIVERY: Service.ShipmentType
    LOCAL_DELIVERY: Service.ShipmentType
    COLLECTION_POINT: Service.ShipmentType
    class StoreConfig(_message.Message):
        __slots__ = ("store_service_type", "store_codes", "cutoff_config", "service_radius")
        class StoreServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORE_SERVICE_TYPE_UNSPECIFIED: _ClassVar[Service.StoreConfig.StoreServiceType]
            ALL_STORES: _ClassVar[Service.StoreConfig.StoreServiceType]
            SELECTED_STORES: _ClassVar[Service.StoreConfig.StoreServiceType]
        STORE_SERVICE_TYPE_UNSPECIFIED: Service.StoreConfig.StoreServiceType
        ALL_STORES: Service.StoreConfig.StoreServiceType
        SELECTED_STORES: Service.StoreConfig.StoreServiceType
        class CutoffConfig(_message.Message):
            __slots__ = ("local_cutoff_time", "store_close_offset_hours", "no_delivery_post_cutoff")
            class LocalCutoffTime(_message.Message):
                __slots__ = ("hour", "minute")
                HOUR_FIELD_NUMBER: _ClassVar[int]
                MINUTE_FIELD_NUMBER: _ClassVar[int]
                hour: int
                minute: int
                def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...
            LOCAL_CUTOFF_TIME_FIELD_NUMBER: _ClassVar[int]
            STORE_CLOSE_OFFSET_HOURS_FIELD_NUMBER: _ClassVar[int]
            NO_DELIVERY_POST_CUTOFF_FIELD_NUMBER: _ClassVar[int]
            local_cutoff_time: Service.StoreConfig.CutoffConfig.LocalCutoffTime
            store_close_offset_hours: int
            no_delivery_post_cutoff: bool
            def __init__(self, local_cutoff_time: _Optional[_Union[Service.StoreConfig.CutoffConfig.LocalCutoffTime, _Mapping]] = ..., store_close_offset_hours: _Optional[int] = ..., no_delivery_post_cutoff: bool = ...) -> None: ...
        STORE_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STORE_CODES_FIELD_NUMBER: _ClassVar[int]
        CUTOFF_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_RADIUS_FIELD_NUMBER: _ClassVar[int]
        store_service_type: Service.StoreConfig.StoreServiceType
        store_codes: _containers.RepeatedScalarFieldContainer[str]
        cutoff_config: Service.StoreConfig.CutoffConfig
        service_radius: Distance
        def __init__(self, store_service_type: _Optional[_Union[Service.StoreConfig.StoreServiceType, str]] = ..., store_codes: _Optional[_Iterable[str]] = ..., cutoff_config: _Optional[_Union[Service.StoreConfig.CutoffConfig, _Mapping]] = ..., service_radius: _Optional[_Union[Distance, _Mapping]] = ...) -> None: ...
    class LoyaltyProgram(_message.Message):
        __slots__ = ("program_label", "loyalty_program_tiers")
        class LoyaltyProgramTiers(_message.Message):
            __slots__ = ("tier_label",)
            TIER_LABEL_FIELD_NUMBER: _ClassVar[int]
            tier_label: str
            def __init__(self, tier_label: _Optional[str] = ...) -> None: ...
        PROGRAM_LABEL_FIELD_NUMBER: _ClassVar[int]
        LOYALTY_PROGRAM_TIERS_FIELD_NUMBER: _ClassVar[int]
        program_label: str
        loyalty_program_tiers: _containers.RepeatedCompositeFieldContainer[Service.LoyaltyProgram.LoyaltyProgramTiers]
        def __init__(self, program_label: _Optional[str] = ..., loyalty_program_tiers: _Optional[_Iterable[_Union[Service.LoyaltyProgram.LoyaltyProgramTiers, _Mapping]]] = ...) -> None: ...
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    RATE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ORDER_VALUE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ORDER_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    STORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOYALTY_PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    active: bool
    delivery_countries: _containers.RepeatedScalarFieldContainer[str]
    currency_code: str
    delivery_time: DeliveryTime
    rate_groups: _containers.RepeatedCompositeFieldContainer[RateGroup]
    shipment_type: Service.ShipmentType
    minimum_order_value: _types_pb2.Price
    minimum_order_value_table: MinimumOrderValueTable
    store_config: Service.StoreConfig
    loyalty_programs: _containers.RepeatedCompositeFieldContainer[Service.LoyaltyProgram]
    def __init__(self, service_name: _Optional[str] = ..., active: bool = ..., delivery_countries: _Optional[_Iterable[str]] = ..., currency_code: _Optional[str] = ..., delivery_time: _Optional[_Union[DeliveryTime, _Mapping]] = ..., rate_groups: _Optional[_Iterable[_Union[RateGroup, _Mapping]]] = ..., shipment_type: _Optional[_Union[Service.ShipmentType, str]] = ..., minimum_order_value: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., minimum_order_value_table: _Optional[_Union[MinimumOrderValueTable, _Mapping]] = ..., store_config: _Optional[_Union[Service.StoreConfig, _Mapping]] = ..., loyalty_programs: _Optional[_Iterable[_Union[Service.LoyaltyProgram, _Mapping]]] = ...) -> None: ...

class Distance(_message.Message):
    __slots__ = ("value", "unit")
    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_UNSPECIFIED: _ClassVar[Distance.Unit]
        MILES: _ClassVar[Distance.Unit]
        KILOMETERS: _ClassVar[Distance.Unit]
    UNIT_UNSPECIFIED: Distance.Unit
    MILES: Distance.Unit
    KILOMETERS: Distance.Unit
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: int
    unit: Distance.Unit
    def __init__(self, value: _Optional[int] = ..., unit: _Optional[_Union[Distance.Unit, str]] = ...) -> None: ...

class Warehouse(_message.Message):
    __slots__ = ("name", "shipping_address", "cutoff_time", "handling_days", "business_day_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CUTOFF_TIME_FIELD_NUMBER: _ClassVar[int]
    HANDLING_DAYS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_DAY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    shipping_address: Address
    cutoff_time: WarehouseCutoffTime
    handling_days: int
    business_day_config: BusinessDayConfig
    def __init__(self, name: _Optional[str] = ..., shipping_address: _Optional[_Union[Address, _Mapping]] = ..., cutoff_time: _Optional[_Union[WarehouseCutoffTime, _Mapping]] = ..., handling_days: _Optional[int] = ..., business_day_config: _Optional[_Union[BusinessDayConfig, _Mapping]] = ...) -> None: ...

class WarehouseCutoffTime(_message.Message):
    __slots__ = ("hour", "minute")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("street_address", "city", "administrative_area", "postal_code", "region_code")
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_AREA_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    street_address: str
    city: str
    administrative_area: str
    postal_code: str
    region_code: str
    def __init__(self, street_address: _Optional[str] = ..., city: _Optional[str] = ..., administrative_area: _Optional[str] = ..., postal_code: _Optional[str] = ..., region_code: _Optional[str] = ...) -> None: ...

class DeliveryTime(_message.Message):
    __slots__ = ("min_transit_days", "max_transit_days", "cutoff_time", "min_handling_days", "max_handling_days", "transit_time_table", "handling_business_day_config", "transit_business_day_config", "warehouse_based_delivery_times")
    MIN_TRANSIT_DAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSIT_DAYS_FIELD_NUMBER: _ClassVar[int]
    CUTOFF_TIME_FIELD_NUMBER: _ClassVar[int]
    MIN_HANDLING_DAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_HANDLING_DAYS_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_TIME_TABLE_FIELD_NUMBER: _ClassVar[int]
    HANDLING_BUSINESS_DAY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_BUSINESS_DAY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_BASED_DELIVERY_TIMES_FIELD_NUMBER: _ClassVar[int]
    min_transit_days: int
    max_transit_days: int
    cutoff_time: CutoffTime
    min_handling_days: int
    max_handling_days: int
    transit_time_table: TransitTable
    handling_business_day_config: BusinessDayConfig
    transit_business_day_config: BusinessDayConfig
    warehouse_based_delivery_times: _containers.RepeatedCompositeFieldContainer[WarehouseBasedDeliveryTime]
    def __init__(self, min_transit_days: _Optional[int] = ..., max_transit_days: _Optional[int] = ..., cutoff_time: _Optional[_Union[CutoffTime, _Mapping]] = ..., min_handling_days: _Optional[int] = ..., max_handling_days: _Optional[int] = ..., transit_time_table: _Optional[_Union[TransitTable, _Mapping]] = ..., handling_business_day_config: _Optional[_Union[BusinessDayConfig, _Mapping]] = ..., transit_business_day_config: _Optional[_Union[BusinessDayConfig, _Mapping]] = ..., warehouse_based_delivery_times: _Optional[_Iterable[_Union[WarehouseBasedDeliveryTime, _Mapping]]] = ...) -> None: ...

class CutoffTime(_message.Message):
    __slots__ = ("hour", "minute", "time_zone")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    time_zone: str
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ..., time_zone: _Optional[str] = ...) -> None: ...

class BusinessDayConfig(_message.Message):
    __slots__ = ("business_days",)
    class Weekday(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEEKDAY_UNSPECIFIED: _ClassVar[BusinessDayConfig.Weekday]
        MONDAY: _ClassVar[BusinessDayConfig.Weekday]
        TUESDAY: _ClassVar[BusinessDayConfig.Weekday]
        WEDNESDAY: _ClassVar[BusinessDayConfig.Weekday]
        THURSDAY: _ClassVar[BusinessDayConfig.Weekday]
        FRIDAY: _ClassVar[BusinessDayConfig.Weekday]
        SATURDAY: _ClassVar[BusinessDayConfig.Weekday]
        SUNDAY: _ClassVar[BusinessDayConfig.Weekday]
    WEEKDAY_UNSPECIFIED: BusinessDayConfig.Weekday
    MONDAY: BusinessDayConfig.Weekday
    TUESDAY: BusinessDayConfig.Weekday
    WEDNESDAY: BusinessDayConfig.Weekday
    THURSDAY: BusinessDayConfig.Weekday
    FRIDAY: BusinessDayConfig.Weekday
    SATURDAY: BusinessDayConfig.Weekday
    SUNDAY: BusinessDayConfig.Weekday
    BUSINESS_DAYS_FIELD_NUMBER: _ClassVar[int]
    business_days: _containers.RepeatedScalarFieldContainer[BusinessDayConfig.Weekday]
    def __init__(self, business_days: _Optional[_Iterable[_Union[BusinessDayConfig.Weekday, str]]] = ...) -> None: ...

class WarehouseBasedDeliveryTime(_message.Message):
    __slots__ = ("carrier", "carrier_service", "warehouse")
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    CARRIER_SERVICE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    carrier: str
    carrier_service: str
    warehouse: str
    def __init__(self, carrier: _Optional[str] = ..., carrier_service: _Optional[str] = ..., warehouse: _Optional[str] = ...) -> None: ...

class RateGroup(_message.Message):
    __slots__ = ("applicable_shipping_labels", "single_value", "main_table", "subtables", "carrier_rates", "name")
    APPLICABLE_SHIPPING_LABELS_FIELD_NUMBER: _ClassVar[int]
    SINGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAIN_TABLE_FIELD_NUMBER: _ClassVar[int]
    SUBTABLES_FIELD_NUMBER: _ClassVar[int]
    CARRIER_RATES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    applicable_shipping_labels: _containers.RepeatedScalarFieldContainer[str]
    single_value: Value
    main_table: Table
    subtables: _containers.RepeatedCompositeFieldContainer[Table]
    carrier_rates: _containers.RepeatedCompositeFieldContainer[CarrierRate]
    name: str
    def __init__(self, applicable_shipping_labels: _Optional[_Iterable[str]] = ..., single_value: _Optional[_Union[Value, _Mapping]] = ..., main_table: _Optional[_Union[Table, _Mapping]] = ..., subtables: _Optional[_Iterable[_Union[Table, _Mapping]]] = ..., carrier_rates: _Optional[_Iterable[_Union[CarrierRate, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ("name", "row_headers", "column_headers", "rows")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_HEADERS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    name: str
    row_headers: Headers
    column_headers: Headers
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, name: _Optional[str] = ..., row_headers: _Optional[_Union[Headers, _Mapping]] = ..., column_headers: _Optional[_Union[Headers, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...

class TransitTable(_message.Message):
    __slots__ = ("postal_code_group_names", "transit_time_labels", "rows")
    class TransitTimeRow(_message.Message):
        __slots__ = ("values",)
        class TransitTimeValue(_message.Message):
            __slots__ = ("min_transit_days", "max_transit_days")
            MIN_TRANSIT_DAYS_FIELD_NUMBER: _ClassVar[int]
            MAX_TRANSIT_DAYS_FIELD_NUMBER: _ClassVar[int]
            min_transit_days: int
            max_transit_days: int
            def __init__(self, min_transit_days: _Optional[int] = ..., max_transit_days: _Optional[int] = ...) -> None: ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[TransitTable.TransitTimeRow.TransitTimeValue]
        def __init__(self, values: _Optional[_Iterable[_Union[TransitTable.TransitTimeRow.TransitTimeValue, _Mapping]]] = ...) -> None: ...
    POSTAL_CODE_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_TIME_LABELS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    postal_code_group_names: _containers.RepeatedScalarFieldContainer[str]
    transit_time_labels: _containers.RepeatedScalarFieldContainer[str]
    rows: _containers.RepeatedCompositeFieldContainer[TransitTable.TransitTimeRow]
    def __init__(self, postal_code_group_names: _Optional[_Iterable[str]] = ..., transit_time_labels: _Optional[_Iterable[str]] = ..., rows: _Optional[_Iterable[_Union[TransitTable.TransitTimeRow, _Mapping]]] = ...) -> None: ...

class MinimumOrderValueTable(_message.Message):
    __slots__ = ("store_code_set_with_movs",)
    class StoreCodeSetWithMov(_message.Message):
        __slots__ = ("store_codes", "value")
        STORE_CODES_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        store_codes: _containers.RepeatedScalarFieldContainer[str]
        value: _types_pb2.Price
        def __init__(self, store_codes: _Optional[_Iterable[str]] = ..., value: _Optional[_Union[_types_pb2.Price, _Mapping]] = ...) -> None: ...
    STORE_CODE_SET_WITH_MOVS_FIELD_NUMBER: _ClassVar[int]
    store_code_set_with_movs: _containers.RepeatedCompositeFieldContainer[MinimumOrderValueTable.StoreCodeSetWithMov]
    def __init__(self, store_code_set_with_movs: _Optional[_Iterable[_Union[MinimumOrderValueTable.StoreCodeSetWithMov, _Mapping]]] = ...) -> None: ...

class Headers(_message.Message):
    __slots__ = ("prices", "weights", "number_of_items", "postal_code_group_names", "locations")
    PRICES_FIELD_NUMBER: _ClassVar[int]
    WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_ITEMS_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    prices: _containers.RepeatedCompositeFieldContainer[_types_pb2.Price]
    weights: _containers.RepeatedCompositeFieldContainer[_types_pb2.Weight]
    number_of_items: _containers.RepeatedScalarFieldContainer[str]
    postal_code_group_names: _containers.RepeatedScalarFieldContainer[str]
    locations: _containers.RepeatedCompositeFieldContainer[LocationIdSet]
    def __init__(self, prices: _Optional[_Iterable[_Union[_types_pb2.Price, _Mapping]]] = ..., weights: _Optional[_Iterable[_Union[_types_pb2.Weight, _Mapping]]] = ..., number_of_items: _Optional[_Iterable[str]] = ..., postal_code_group_names: _Optional[_Iterable[str]] = ..., locations: _Optional[_Iterable[_Union[LocationIdSet, _Mapping]]] = ...) -> None: ...

class LocationIdSet(_message.Message):
    __slots__ = ("location_ids",)
    LOCATION_IDS_FIELD_NUMBER: _ClassVar[int]
    location_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, location_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("cells",)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, cells: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("no_shipping", "flat_rate", "price_percentage", "carrier_rate", "subtable")
    NO_SHIPPING_FIELD_NUMBER: _ClassVar[int]
    FLAT_RATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CARRIER_RATE_FIELD_NUMBER: _ClassVar[int]
    SUBTABLE_FIELD_NUMBER: _ClassVar[int]
    no_shipping: bool
    flat_rate: _types_pb2.Price
    price_percentage: str
    carrier_rate: str
    subtable: str
    def __init__(self, no_shipping: bool = ..., flat_rate: _Optional[_Union[_types_pb2.Price, _Mapping]] = ..., price_percentage: _Optional[str] = ..., carrier_rate: _Optional[str] = ..., subtable: _Optional[str] = ...) -> None: ...

class CarrierRate(_message.Message):
    __slots__ = ("name", "carrier", "carrier_service", "origin_postal_code", "percentage_adjustment", "flat_adjustment")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    CARRIER_SERVICE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    FLAT_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    carrier: str
    carrier_service: str
    origin_postal_code: str
    percentage_adjustment: str
    flat_adjustment: _types_pb2.Price
    def __init__(self, name: _Optional[str] = ..., carrier: _Optional[str] = ..., carrier_service: _Optional[str] = ..., origin_postal_code: _Optional[str] = ..., percentage_adjustment: _Optional[str] = ..., flat_adjustment: _Optional[_Union[_types_pb2.Price, _Mapping]] = ...) -> None: ...

class GetShippingSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InsertShippingSettingsRequest(_message.Message):
    __slots__ = ("parent", "shipping_setting")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_SETTING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    shipping_setting: ShippingSettings
    def __init__(self, parent: _Optional[str] = ..., shipping_setting: _Optional[_Union[ShippingSettings, _Mapping]] = ...) -> None: ...
