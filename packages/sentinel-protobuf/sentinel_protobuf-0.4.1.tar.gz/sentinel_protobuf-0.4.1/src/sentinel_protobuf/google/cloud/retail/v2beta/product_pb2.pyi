from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2beta import common_pb2 as _common_pb2
from google.cloud.retail.v2beta import promotion_pb2 as _promotion_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("expire_time", "ttl", "name", "id", "type", "primary_product_id", "collection_member_ids", "gtin", "categories", "title", "brands", "description", "language_code", "attributes", "tags", "price_info", "rating", "available_time", "availability", "available_quantity", "fulfillment_info", "uri", "images", "audience", "color_info", "sizes", "materials", "patterns", "conditions", "promotions", "publish_time", "retrievable_fields", "variants", "local_inventories")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Product.Type]
        PRIMARY: _ClassVar[Product.Type]
        VARIANT: _ClassVar[Product.Type]
        COLLECTION: _ClassVar[Product.Type]
    TYPE_UNSPECIFIED: Product.Type
    PRIMARY: Product.Type
    VARIANT: Product.Type
    COLLECTION: Product.Type
    class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AVAILABILITY_UNSPECIFIED: _ClassVar[Product.Availability]
        IN_STOCK: _ClassVar[Product.Availability]
        OUT_OF_STOCK: _ClassVar[Product.Availability]
        PREORDER: _ClassVar[Product.Availability]
        BACKORDER: _ClassVar[Product.Availability]
    AVAILABILITY_UNSPECIFIED: Product.Availability
    IN_STOCK: Product.Availability
    OUT_OF_STOCK: Product.Availability
    PREORDER: Product.Availability
    BACKORDER: Product.Availability
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.CustomAttribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.CustomAttribute, _Mapping]] = ...) -> None: ...
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    GTIN_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PRICE_INFO_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    COLOR_INFO_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    PATTERNS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONS_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    RETRIEVABLE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    name: str
    id: str
    type: Product.Type
    primary_product_id: str
    collection_member_ids: _containers.RepeatedScalarFieldContainer[str]
    gtin: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    title: str
    brands: _containers.RepeatedScalarFieldContainer[str]
    description: str
    language_code: str
    attributes: _containers.MessageMap[str, _common_pb2.CustomAttribute]
    tags: _containers.RepeatedScalarFieldContainer[str]
    price_info: _common_pb2.PriceInfo
    rating: _common_pb2.Rating
    available_time: _timestamp_pb2.Timestamp
    availability: Product.Availability
    available_quantity: _wrappers_pb2.Int32Value
    fulfillment_info: _containers.RepeatedCompositeFieldContainer[_common_pb2.FulfillmentInfo]
    uri: str
    images: _containers.RepeatedCompositeFieldContainer[_common_pb2.Image]
    audience: _common_pb2.Audience
    color_info: _common_pb2.ColorInfo
    sizes: _containers.RepeatedScalarFieldContainer[str]
    materials: _containers.RepeatedScalarFieldContainer[str]
    patterns: _containers.RepeatedScalarFieldContainer[str]
    conditions: _containers.RepeatedScalarFieldContainer[str]
    promotions: _containers.RepeatedCompositeFieldContainer[_promotion_pb2.Promotion]
    publish_time: _timestamp_pb2.Timestamp
    retrievable_fields: _field_mask_pb2.FieldMask
    variants: _containers.RepeatedCompositeFieldContainer[Product]
    local_inventories: _containers.RepeatedCompositeFieldContainer[_common_pb2.LocalInventory]
    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ..., type: _Optional[_Union[Product.Type, str]] = ..., primary_product_id: _Optional[str] = ..., collection_member_ids: _Optional[_Iterable[str]] = ..., gtin: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ..., title: _Optional[str] = ..., brands: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., language_code: _Optional[str] = ..., attributes: _Optional[_Mapping[str, _common_pb2.CustomAttribute]] = ..., tags: _Optional[_Iterable[str]] = ..., price_info: _Optional[_Union[_common_pb2.PriceInfo, _Mapping]] = ..., rating: _Optional[_Union[_common_pb2.Rating, _Mapping]] = ..., available_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., availability: _Optional[_Union[Product.Availability, str]] = ..., available_quantity: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., fulfillment_info: _Optional[_Iterable[_Union[_common_pb2.FulfillmentInfo, _Mapping]]] = ..., uri: _Optional[str] = ..., images: _Optional[_Iterable[_Union[_common_pb2.Image, _Mapping]]] = ..., audience: _Optional[_Union[_common_pb2.Audience, _Mapping]] = ..., color_info: _Optional[_Union[_common_pb2.ColorInfo, _Mapping]] = ..., sizes: _Optional[_Iterable[str]] = ..., materials: _Optional[_Iterable[str]] = ..., patterns: _Optional[_Iterable[str]] = ..., conditions: _Optional[_Iterable[str]] = ..., promotions: _Optional[_Iterable[_Union[_promotion_pb2.Promotion, _Mapping]]] = ..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., retrievable_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., variants: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., local_inventories: _Optional[_Iterable[_Union[_common_pb2.LocalInventory, _Mapping]]] = ...) -> None: ...
