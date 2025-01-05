from google.ads.googleads.v16.enums import product_category_level_pb2 as _product_category_level_pb2
from google.ads.googleads.v16.enums import product_category_state_pb2 as _product_category_state_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductCategoryConstant(_message.Message):
    __slots__ = ("resource_name", "category_id", "product_category_constant_parent", "level", "state", "localizations")
    class ProductCategoryLocalization(_message.Message):
        __slots__ = ("region_code", "language_code", "value")
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        region_code: str
        language_code: str
        value: str
        def __init__(self, region_code: _Optional[str] = ..., language_code: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_CONSTANT_PARENT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    category_id: int
    product_category_constant_parent: str
    level: _product_category_level_pb2.ProductCategoryLevelEnum.ProductCategoryLevel
    state: _product_category_state_pb2.ProductCategoryStateEnum.ProductCategoryState
    localizations: _containers.RepeatedCompositeFieldContainer[ProductCategoryConstant.ProductCategoryLocalization]
    def __init__(self, resource_name: _Optional[str] = ..., category_id: _Optional[int] = ..., product_category_constant_parent: _Optional[str] = ..., level: _Optional[_Union[_product_category_level_pb2.ProductCategoryLevelEnum.ProductCategoryLevel, str]] = ..., state: _Optional[_Union[_product_category_state_pb2.ProductCategoryStateEnum.ProductCategoryState, str]] = ..., localizations: _Optional[_Iterable[_Union[ProductCategoryConstant.ProductCategoryLocalization, _Mapping]]] = ...) -> None: ...
