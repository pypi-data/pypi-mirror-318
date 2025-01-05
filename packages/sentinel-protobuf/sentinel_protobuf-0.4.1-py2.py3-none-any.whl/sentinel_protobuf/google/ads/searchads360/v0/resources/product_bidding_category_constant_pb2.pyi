from google.ads.searchads360.v0.enums import product_bidding_category_level_pb2 as _product_bidding_category_level_pb2
from google.ads.searchads360.v0.enums import product_bidding_category_status_pb2 as _product_bidding_category_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductBiddingCategoryConstant(_message.Message):
    __slots__ = ("resource_name", "id", "country_code", "product_bidding_category_constant_parent", "level", "status", "language_code", "localized_name")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_CONSTANT_PARENT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    country_code: str
    product_bidding_category_constant_parent: str
    level: _product_bidding_category_level_pb2.ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    status: _product_bidding_category_status_pb2.ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    language_code: str
    localized_name: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., country_code: _Optional[str] = ..., product_bidding_category_constant_parent: _Optional[str] = ..., level: _Optional[_Union[_product_bidding_category_level_pb2.ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel, str]] = ..., status: _Optional[_Union[_product_bidding_category_status_pb2.ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus, str]] = ..., language_code: _Optional[str] = ..., localized_name: _Optional[str] = ...) -> None: ...
