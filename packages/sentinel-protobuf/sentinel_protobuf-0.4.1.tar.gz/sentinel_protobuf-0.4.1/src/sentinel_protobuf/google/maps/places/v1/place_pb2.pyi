from google.api import resource_pb2 as _resource_pb2
from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.places.v1 import content_block_pb2 as _content_block_pb2
from google.maps.places.v1 import ev_charging_pb2 as _ev_charging_pb2
from google.maps.places.v1 import fuel_options_pb2 as _fuel_options_pb2
from google.maps.places.v1 import photo_pb2 as _photo_pb2
from google.maps.places.v1 import price_range_pb2 as _price_range_pb2
from google.maps.places.v1 import reference_pb2 as _reference_pb2
from google.maps.places.v1 import review_pb2 as _review_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PriceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRICE_LEVEL_UNSPECIFIED: _ClassVar[PriceLevel]
    PRICE_LEVEL_FREE: _ClassVar[PriceLevel]
    PRICE_LEVEL_INEXPENSIVE: _ClassVar[PriceLevel]
    PRICE_LEVEL_MODERATE: _ClassVar[PriceLevel]
    PRICE_LEVEL_EXPENSIVE: _ClassVar[PriceLevel]
    PRICE_LEVEL_VERY_EXPENSIVE: _ClassVar[PriceLevel]
PRICE_LEVEL_UNSPECIFIED: PriceLevel
PRICE_LEVEL_FREE: PriceLevel
PRICE_LEVEL_INEXPENSIVE: PriceLevel
PRICE_LEVEL_MODERATE: PriceLevel
PRICE_LEVEL_EXPENSIVE: PriceLevel
PRICE_LEVEL_VERY_EXPENSIVE: PriceLevel

class Place(_message.Message):
    __slots__ = ("name", "id", "display_name", "types", "primary_type", "primary_type_display_name", "national_phone_number", "international_phone_number", "formatted_address", "short_formatted_address", "address_components", "plus_code", "location", "viewport", "rating", "google_maps_uri", "website_uri", "reviews", "regular_opening_hours", "utc_offset_minutes", "photos", "adr_format_address", "business_status", "price_level", "attributions", "user_rating_count", "icon_mask_base_uri", "icon_background_color", "takeout", "delivery", "dine_in", "curbside_pickup", "reservable", "serves_breakfast", "serves_lunch", "serves_dinner", "serves_beer", "serves_wine", "serves_brunch", "serves_vegetarian_food", "current_opening_hours", "current_secondary_opening_hours", "regular_secondary_opening_hours", "editorial_summary", "outdoor_seating", "live_music", "menu_for_children", "serves_cocktails", "serves_dessert", "serves_coffee", "good_for_children", "allows_dogs", "restroom", "good_for_groups", "good_for_watching_sports", "payment_options", "parking_options", "sub_destinations", "accessibility_options", "fuel_options", "ev_charge_options", "generative_summary", "area_summary", "containing_places", "pure_service_area_business", "price_range")
    class BusinessStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUSINESS_STATUS_UNSPECIFIED: _ClassVar[Place.BusinessStatus]
        OPERATIONAL: _ClassVar[Place.BusinessStatus]
        CLOSED_TEMPORARILY: _ClassVar[Place.BusinessStatus]
        CLOSED_PERMANENTLY: _ClassVar[Place.BusinessStatus]
    BUSINESS_STATUS_UNSPECIFIED: Place.BusinessStatus
    OPERATIONAL: Place.BusinessStatus
    CLOSED_TEMPORARILY: Place.BusinessStatus
    CLOSED_PERMANENTLY: Place.BusinessStatus
    class AddressComponent(_message.Message):
        __slots__ = ("long_text", "short_text", "types", "language_code")
        LONG_TEXT_FIELD_NUMBER: _ClassVar[int]
        SHORT_TEXT_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        long_text: str
        short_text: str
        types: _containers.RepeatedScalarFieldContainer[str]
        language_code: str
        def __init__(self, long_text: _Optional[str] = ..., short_text: _Optional[str] = ..., types: _Optional[_Iterable[str]] = ..., language_code: _Optional[str] = ...) -> None: ...
    class PlusCode(_message.Message):
        __slots__ = ("global_code", "compound_code")
        GLOBAL_CODE_FIELD_NUMBER: _ClassVar[int]
        COMPOUND_CODE_FIELD_NUMBER: _ClassVar[int]
        global_code: str
        compound_code: str
        def __init__(self, global_code: _Optional[str] = ..., compound_code: _Optional[str] = ...) -> None: ...
    class OpeningHours(_message.Message):
        __slots__ = ("open_now", "periods", "weekday_descriptions", "secondary_hours_type", "special_days", "next_open_time", "next_close_time")
        class SecondaryHoursType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SECONDARY_HOURS_TYPE_UNSPECIFIED: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            DRIVE_THROUGH: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            HAPPY_HOUR: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            DELIVERY: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            TAKEOUT: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            KITCHEN: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            BREAKFAST: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            LUNCH: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            DINNER: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            BRUNCH: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            PICKUP: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            ACCESS: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            SENIOR_HOURS: _ClassVar[Place.OpeningHours.SecondaryHoursType]
            ONLINE_SERVICE_HOURS: _ClassVar[Place.OpeningHours.SecondaryHoursType]
        SECONDARY_HOURS_TYPE_UNSPECIFIED: Place.OpeningHours.SecondaryHoursType
        DRIVE_THROUGH: Place.OpeningHours.SecondaryHoursType
        HAPPY_HOUR: Place.OpeningHours.SecondaryHoursType
        DELIVERY: Place.OpeningHours.SecondaryHoursType
        TAKEOUT: Place.OpeningHours.SecondaryHoursType
        KITCHEN: Place.OpeningHours.SecondaryHoursType
        BREAKFAST: Place.OpeningHours.SecondaryHoursType
        LUNCH: Place.OpeningHours.SecondaryHoursType
        DINNER: Place.OpeningHours.SecondaryHoursType
        BRUNCH: Place.OpeningHours.SecondaryHoursType
        PICKUP: Place.OpeningHours.SecondaryHoursType
        ACCESS: Place.OpeningHours.SecondaryHoursType
        SENIOR_HOURS: Place.OpeningHours.SecondaryHoursType
        ONLINE_SERVICE_HOURS: Place.OpeningHours.SecondaryHoursType
        class Period(_message.Message):
            __slots__ = ("open", "close")
            class Point(_message.Message):
                __slots__ = ("day", "hour", "minute", "date", "truncated")
                DAY_FIELD_NUMBER: _ClassVar[int]
                HOUR_FIELD_NUMBER: _ClassVar[int]
                MINUTE_FIELD_NUMBER: _ClassVar[int]
                DATE_FIELD_NUMBER: _ClassVar[int]
                TRUNCATED_FIELD_NUMBER: _ClassVar[int]
                day: int
                hour: int
                minute: int
                date: _date_pb2.Date
                truncated: bool
                def __init__(self, day: _Optional[int] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., truncated: bool = ...) -> None: ...
            OPEN_FIELD_NUMBER: _ClassVar[int]
            CLOSE_FIELD_NUMBER: _ClassVar[int]
            open: Place.OpeningHours.Period.Point
            close: Place.OpeningHours.Period.Point
            def __init__(self, open: _Optional[_Union[Place.OpeningHours.Period.Point, _Mapping]] = ..., close: _Optional[_Union[Place.OpeningHours.Period.Point, _Mapping]] = ...) -> None: ...
        class SpecialDay(_message.Message):
            __slots__ = ("date",)
            DATE_FIELD_NUMBER: _ClassVar[int]
            date: _date_pb2.Date
            def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...
        OPEN_NOW_FIELD_NUMBER: _ClassVar[int]
        PERIODS_FIELD_NUMBER: _ClassVar[int]
        WEEKDAY_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_HOURS_TYPE_FIELD_NUMBER: _ClassVar[int]
        SPECIAL_DAYS_FIELD_NUMBER: _ClassVar[int]
        NEXT_OPEN_TIME_FIELD_NUMBER: _ClassVar[int]
        NEXT_CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
        open_now: bool
        periods: _containers.RepeatedCompositeFieldContainer[Place.OpeningHours.Period]
        weekday_descriptions: _containers.RepeatedScalarFieldContainer[str]
        secondary_hours_type: Place.OpeningHours.SecondaryHoursType
        special_days: _containers.RepeatedCompositeFieldContainer[Place.OpeningHours.SpecialDay]
        next_open_time: _timestamp_pb2.Timestamp
        next_close_time: _timestamp_pb2.Timestamp
        def __init__(self, open_now: bool = ..., periods: _Optional[_Iterable[_Union[Place.OpeningHours.Period, _Mapping]]] = ..., weekday_descriptions: _Optional[_Iterable[str]] = ..., secondary_hours_type: _Optional[_Union[Place.OpeningHours.SecondaryHoursType, str]] = ..., special_days: _Optional[_Iterable[_Union[Place.OpeningHours.SpecialDay, _Mapping]]] = ..., next_open_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Attribution(_message.Message):
        __slots__ = ("provider", "provider_uri")
        PROVIDER_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_URI_FIELD_NUMBER: _ClassVar[int]
        provider: str
        provider_uri: str
        def __init__(self, provider: _Optional[str] = ..., provider_uri: _Optional[str] = ...) -> None: ...
    class PaymentOptions(_message.Message):
        __slots__ = ("accepts_credit_cards", "accepts_debit_cards", "accepts_cash_only", "accepts_nfc")
        ACCEPTS_CREDIT_CARDS_FIELD_NUMBER: _ClassVar[int]
        ACCEPTS_DEBIT_CARDS_FIELD_NUMBER: _ClassVar[int]
        ACCEPTS_CASH_ONLY_FIELD_NUMBER: _ClassVar[int]
        ACCEPTS_NFC_FIELD_NUMBER: _ClassVar[int]
        accepts_credit_cards: bool
        accepts_debit_cards: bool
        accepts_cash_only: bool
        accepts_nfc: bool
        def __init__(self, accepts_credit_cards: bool = ..., accepts_debit_cards: bool = ..., accepts_cash_only: bool = ..., accepts_nfc: bool = ...) -> None: ...
    class ParkingOptions(_message.Message):
        __slots__ = ("free_parking_lot", "paid_parking_lot", "free_street_parking", "paid_street_parking", "valet_parking", "free_garage_parking", "paid_garage_parking")
        FREE_PARKING_LOT_FIELD_NUMBER: _ClassVar[int]
        PAID_PARKING_LOT_FIELD_NUMBER: _ClassVar[int]
        FREE_STREET_PARKING_FIELD_NUMBER: _ClassVar[int]
        PAID_STREET_PARKING_FIELD_NUMBER: _ClassVar[int]
        VALET_PARKING_FIELD_NUMBER: _ClassVar[int]
        FREE_GARAGE_PARKING_FIELD_NUMBER: _ClassVar[int]
        PAID_GARAGE_PARKING_FIELD_NUMBER: _ClassVar[int]
        free_parking_lot: bool
        paid_parking_lot: bool
        free_street_parking: bool
        paid_street_parking: bool
        valet_parking: bool
        free_garage_parking: bool
        paid_garage_parking: bool
        def __init__(self, free_parking_lot: bool = ..., paid_parking_lot: bool = ..., free_street_parking: bool = ..., paid_street_parking: bool = ..., valet_parking: bool = ..., free_garage_parking: bool = ..., paid_garage_parking: bool = ...) -> None: ...
    class SubDestination(_message.Message):
        __slots__ = ("name", "id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: str
        def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class AccessibilityOptions(_message.Message):
        __slots__ = ("wheelchair_accessible_parking", "wheelchair_accessible_entrance", "wheelchair_accessible_restroom", "wheelchair_accessible_seating")
        WHEELCHAIR_ACCESSIBLE_PARKING_FIELD_NUMBER: _ClassVar[int]
        WHEELCHAIR_ACCESSIBLE_ENTRANCE_FIELD_NUMBER: _ClassVar[int]
        WHEELCHAIR_ACCESSIBLE_RESTROOM_FIELD_NUMBER: _ClassVar[int]
        WHEELCHAIR_ACCESSIBLE_SEATING_FIELD_NUMBER: _ClassVar[int]
        wheelchair_accessible_parking: bool
        wheelchair_accessible_entrance: bool
        wheelchair_accessible_restroom: bool
        wheelchair_accessible_seating: bool
        def __init__(self, wheelchair_accessible_parking: bool = ..., wheelchair_accessible_entrance: bool = ..., wheelchair_accessible_restroom: bool = ..., wheelchair_accessible_seating: bool = ...) -> None: ...
    class GenerativeSummary(_message.Message):
        __slots__ = ("overview", "description", "references")
        OVERVIEW_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        REFERENCES_FIELD_NUMBER: _ClassVar[int]
        overview: _localized_text_pb2.LocalizedText
        description: _localized_text_pb2.LocalizedText
        references: _reference_pb2.References
        def __init__(self, overview: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., description: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., references: _Optional[_Union[_reference_pb2.References, _Mapping]] = ...) -> None: ...
    class AreaSummary(_message.Message):
        __slots__ = ("content_blocks",)
        CONTENT_BLOCKS_FIELD_NUMBER: _ClassVar[int]
        content_blocks: _containers.RepeatedCompositeFieldContainer[_content_block_pb2.ContentBlock]
        def __init__(self, content_blocks: _Optional[_Iterable[_Union[_content_block_pb2.ContentBlock, _Mapping]]] = ...) -> None: ...
    class ContainingPlace(_message.Message):
        __slots__ = ("name", "id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: str
        def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_TYPE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INTERNATIONAL_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHORT_FORMATTED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    PLUS_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_MAPS_URI_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URI_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    REGULAR_OPENING_HOURS_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_MINUTES_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    ADR_FORMAT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    USER_RATING_COUNT_FIELD_NUMBER: _ClassVar[int]
    ICON_MASK_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    ICON_BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    TAKEOUT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DINE_IN_FIELD_NUMBER: _ClassVar[int]
    CURBSIDE_PICKUP_FIELD_NUMBER: _ClassVar[int]
    RESERVABLE_FIELD_NUMBER: _ClassVar[int]
    SERVES_BREAKFAST_FIELD_NUMBER: _ClassVar[int]
    SERVES_LUNCH_FIELD_NUMBER: _ClassVar[int]
    SERVES_DINNER_FIELD_NUMBER: _ClassVar[int]
    SERVES_BEER_FIELD_NUMBER: _ClassVar[int]
    SERVES_WINE_FIELD_NUMBER: _ClassVar[int]
    SERVES_BRUNCH_FIELD_NUMBER: _ClassVar[int]
    SERVES_VEGETARIAN_FOOD_FIELD_NUMBER: _ClassVar[int]
    CURRENT_OPENING_HOURS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SECONDARY_OPENING_HOURS_FIELD_NUMBER: _ClassVar[int]
    REGULAR_SECONDARY_OPENING_HOURS_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    OUTDOOR_SEATING_FIELD_NUMBER: _ClassVar[int]
    LIVE_MUSIC_FIELD_NUMBER: _ClassVar[int]
    MENU_FOR_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    SERVES_COCKTAILS_FIELD_NUMBER: _ClassVar[int]
    SERVES_DESSERT_FIELD_NUMBER: _ClassVar[int]
    SERVES_COFFEE_FIELD_NUMBER: _ClassVar[int]
    GOOD_FOR_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_DOGS_FIELD_NUMBER: _ClassVar[int]
    RESTROOM_FIELD_NUMBER: _ClassVar[int]
    GOOD_FOR_GROUPS_FIELD_NUMBER: _ClassVar[int]
    GOOD_FOR_WATCHING_SPORTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARKING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SUB_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FUEL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EV_CHARGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GENERATIVE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AREA_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CONTAINING_PLACES_FIELD_NUMBER: _ClassVar[int]
    PURE_SERVICE_AREA_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    display_name: _localized_text_pb2.LocalizedText
    types: _containers.RepeatedScalarFieldContainer[str]
    primary_type: str
    primary_type_display_name: _localized_text_pb2.LocalizedText
    national_phone_number: str
    international_phone_number: str
    formatted_address: str
    short_formatted_address: str
    address_components: _containers.RepeatedCompositeFieldContainer[Place.AddressComponent]
    plus_code: Place.PlusCode
    location: _latlng_pb2.LatLng
    viewport: _viewport_pb2.Viewport
    rating: float
    google_maps_uri: str
    website_uri: str
    reviews: _containers.RepeatedCompositeFieldContainer[_review_pb2.Review]
    regular_opening_hours: Place.OpeningHours
    utc_offset_minutes: int
    photos: _containers.RepeatedCompositeFieldContainer[_photo_pb2.Photo]
    adr_format_address: str
    business_status: Place.BusinessStatus
    price_level: PriceLevel
    attributions: _containers.RepeatedCompositeFieldContainer[Place.Attribution]
    user_rating_count: int
    icon_mask_base_uri: str
    icon_background_color: str
    takeout: bool
    delivery: bool
    dine_in: bool
    curbside_pickup: bool
    reservable: bool
    serves_breakfast: bool
    serves_lunch: bool
    serves_dinner: bool
    serves_beer: bool
    serves_wine: bool
    serves_brunch: bool
    serves_vegetarian_food: bool
    current_opening_hours: Place.OpeningHours
    current_secondary_opening_hours: _containers.RepeatedCompositeFieldContainer[Place.OpeningHours]
    regular_secondary_opening_hours: _containers.RepeatedCompositeFieldContainer[Place.OpeningHours]
    editorial_summary: _localized_text_pb2.LocalizedText
    outdoor_seating: bool
    live_music: bool
    menu_for_children: bool
    serves_cocktails: bool
    serves_dessert: bool
    serves_coffee: bool
    good_for_children: bool
    allows_dogs: bool
    restroom: bool
    good_for_groups: bool
    good_for_watching_sports: bool
    payment_options: Place.PaymentOptions
    parking_options: Place.ParkingOptions
    sub_destinations: _containers.RepeatedCompositeFieldContainer[Place.SubDestination]
    accessibility_options: Place.AccessibilityOptions
    fuel_options: _fuel_options_pb2.FuelOptions
    ev_charge_options: _ev_charging_pb2.EVChargeOptions
    generative_summary: Place.GenerativeSummary
    area_summary: Place.AreaSummary
    containing_places: _containers.RepeatedCompositeFieldContainer[Place.ContainingPlace]
    pure_service_area_business: bool
    price_range: _price_range_pb2.PriceRange
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., display_name: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., types: _Optional[_Iterable[str]] = ..., primary_type: _Optional[str] = ..., primary_type_display_name: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., national_phone_number: _Optional[str] = ..., international_phone_number: _Optional[str] = ..., formatted_address: _Optional[str] = ..., short_formatted_address: _Optional[str] = ..., address_components: _Optional[_Iterable[_Union[Place.AddressComponent, _Mapping]]] = ..., plus_code: _Optional[_Union[Place.PlusCode, _Mapping]] = ..., location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., viewport: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ..., rating: _Optional[float] = ..., google_maps_uri: _Optional[str] = ..., website_uri: _Optional[str] = ..., reviews: _Optional[_Iterable[_Union[_review_pb2.Review, _Mapping]]] = ..., regular_opening_hours: _Optional[_Union[Place.OpeningHours, _Mapping]] = ..., utc_offset_minutes: _Optional[int] = ..., photos: _Optional[_Iterable[_Union[_photo_pb2.Photo, _Mapping]]] = ..., adr_format_address: _Optional[str] = ..., business_status: _Optional[_Union[Place.BusinessStatus, str]] = ..., price_level: _Optional[_Union[PriceLevel, str]] = ..., attributions: _Optional[_Iterable[_Union[Place.Attribution, _Mapping]]] = ..., user_rating_count: _Optional[int] = ..., icon_mask_base_uri: _Optional[str] = ..., icon_background_color: _Optional[str] = ..., takeout: bool = ..., delivery: bool = ..., dine_in: bool = ..., curbside_pickup: bool = ..., reservable: bool = ..., serves_breakfast: bool = ..., serves_lunch: bool = ..., serves_dinner: bool = ..., serves_beer: bool = ..., serves_wine: bool = ..., serves_brunch: bool = ..., serves_vegetarian_food: bool = ..., current_opening_hours: _Optional[_Union[Place.OpeningHours, _Mapping]] = ..., current_secondary_opening_hours: _Optional[_Iterable[_Union[Place.OpeningHours, _Mapping]]] = ..., regular_secondary_opening_hours: _Optional[_Iterable[_Union[Place.OpeningHours, _Mapping]]] = ..., editorial_summary: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., outdoor_seating: bool = ..., live_music: bool = ..., menu_for_children: bool = ..., serves_cocktails: bool = ..., serves_dessert: bool = ..., serves_coffee: bool = ..., good_for_children: bool = ..., allows_dogs: bool = ..., restroom: bool = ..., good_for_groups: bool = ..., good_for_watching_sports: bool = ..., payment_options: _Optional[_Union[Place.PaymentOptions, _Mapping]] = ..., parking_options: _Optional[_Union[Place.ParkingOptions, _Mapping]] = ..., sub_destinations: _Optional[_Iterable[_Union[Place.SubDestination, _Mapping]]] = ..., accessibility_options: _Optional[_Union[Place.AccessibilityOptions, _Mapping]] = ..., fuel_options: _Optional[_Union[_fuel_options_pb2.FuelOptions, _Mapping]] = ..., ev_charge_options: _Optional[_Union[_ev_charging_pb2.EVChargeOptions, _Mapping]] = ..., generative_summary: _Optional[_Union[Place.GenerativeSummary, _Mapping]] = ..., area_summary: _Optional[_Union[Place.AreaSummary, _Mapping]] = ..., containing_places: _Optional[_Iterable[_Union[Place.ContainingPlace, _Mapping]]] = ..., pure_service_area_business: bool = ..., price_range: _Optional[_Union[_price_range_pb2.PriceRange, _Mapping]] = ...) -> None: ...
