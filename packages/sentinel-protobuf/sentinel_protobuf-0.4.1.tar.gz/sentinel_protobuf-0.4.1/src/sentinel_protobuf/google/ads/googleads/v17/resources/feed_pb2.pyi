from google.ads.googleads.v17.enums import affiliate_location_feed_relationship_type_pb2 as _affiliate_location_feed_relationship_type_pb2
from google.ads.googleads.v17.enums import feed_attribute_type_pb2 as _feed_attribute_type_pb2
from google.ads.googleads.v17.enums import feed_origin_pb2 as _feed_origin_pb2
from google.ads.googleads.v17.enums import feed_status_pb2 as _feed_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Feed(_message.Message):
    __slots__ = ("resource_name", "id", "name", "attributes", "attribute_operations", "origin", "status", "places_location_feed_data", "affiliate_location_feed_data")
    class PlacesLocationFeedData(_message.Message):
        __slots__ = ("oauth_info", "email_address", "business_account_id", "business_name_filter", "category_filters", "label_filters")
        class OAuthInfo(_message.Message):
            __slots__ = ("http_method", "http_request_url", "http_authorization_header")
            HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
            HTTP_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
            HTTP_AUTHORIZATION_HEADER_FIELD_NUMBER: _ClassVar[int]
            http_method: str
            http_request_url: str
            http_authorization_header: str
            def __init__(self, http_method: _Optional[str] = ..., http_request_url: _Optional[str] = ..., http_authorization_header: _Optional[str] = ...) -> None: ...
        OAUTH_INFO_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        BUSINESS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        BUSINESS_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FILTERS_FIELD_NUMBER: _ClassVar[int]
        LABEL_FILTERS_FIELD_NUMBER: _ClassVar[int]
        oauth_info: Feed.PlacesLocationFeedData.OAuthInfo
        email_address: str
        business_account_id: str
        business_name_filter: str
        category_filters: _containers.RepeatedScalarFieldContainer[str]
        label_filters: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, oauth_info: _Optional[_Union[Feed.PlacesLocationFeedData.OAuthInfo, _Mapping]] = ..., email_address: _Optional[str] = ..., business_account_id: _Optional[str] = ..., business_name_filter: _Optional[str] = ..., category_filters: _Optional[_Iterable[str]] = ..., label_filters: _Optional[_Iterable[str]] = ...) -> None: ...
    class AffiliateLocationFeedData(_message.Message):
        __slots__ = ("chain_ids", "relationship_type")
        CHAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
        chain_ids: _containers.RepeatedScalarFieldContainer[int]
        relationship_type: _affiliate_location_feed_relationship_type_pb2.AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
        def __init__(self, chain_ids: _Optional[_Iterable[int]] = ..., relationship_type: _Optional[_Union[_affiliate_location_feed_relationship_type_pb2.AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType, str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PLACES_LOCATION_FEED_DATA_FIELD_NUMBER: _ClassVar[int]
    AFFILIATE_LOCATION_FEED_DATA_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    attributes: _containers.RepeatedCompositeFieldContainer[FeedAttribute]
    attribute_operations: _containers.RepeatedCompositeFieldContainer[FeedAttributeOperation]
    origin: _feed_origin_pb2.FeedOriginEnum.FeedOrigin
    status: _feed_status_pb2.FeedStatusEnum.FeedStatus
    places_location_feed_data: Feed.PlacesLocationFeedData
    affiliate_location_feed_data: Feed.AffiliateLocationFeedData
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[FeedAttribute, _Mapping]]] = ..., attribute_operations: _Optional[_Iterable[_Union[FeedAttributeOperation, _Mapping]]] = ..., origin: _Optional[_Union[_feed_origin_pb2.FeedOriginEnum.FeedOrigin, str]] = ..., status: _Optional[_Union[_feed_status_pb2.FeedStatusEnum.FeedStatus, str]] = ..., places_location_feed_data: _Optional[_Union[Feed.PlacesLocationFeedData, _Mapping]] = ..., affiliate_location_feed_data: _Optional[_Union[Feed.AffiliateLocationFeedData, _Mapping]] = ...) -> None: ...

class FeedAttribute(_message.Message):
    __slots__ = ("id", "name", "type", "is_part_of_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PART_OF_KEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: _feed_attribute_type_pb2.FeedAttributeTypeEnum.FeedAttributeType
    is_part_of_key: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_feed_attribute_type_pb2.FeedAttributeTypeEnum.FeedAttributeType, str]] = ..., is_part_of_key: bool = ...) -> None: ...

class FeedAttributeOperation(_message.Message):
    __slots__ = ("operator", "value")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedAttributeOperation.Operator]
        UNKNOWN: _ClassVar[FeedAttributeOperation.Operator]
        ADD: _ClassVar[FeedAttributeOperation.Operator]
    UNSPECIFIED: FeedAttributeOperation.Operator
    UNKNOWN: FeedAttributeOperation.Operator
    ADD: FeedAttributeOperation.Operator
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operator: FeedAttributeOperation.Operator
    value: FeedAttribute
    def __init__(self, operator: _Optional[_Union[FeedAttributeOperation.Operator, str]] = ..., value: _Optional[_Union[FeedAttribute, _Mapping]] = ...) -> None: ...
