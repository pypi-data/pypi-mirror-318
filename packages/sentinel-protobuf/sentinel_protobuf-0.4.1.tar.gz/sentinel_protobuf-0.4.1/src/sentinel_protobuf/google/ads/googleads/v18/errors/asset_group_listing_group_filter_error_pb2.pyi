from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupListingGroupFilterErrorEnum(_message.Message):
    __slots__ = ()

    class AssetGroupListingGroupFilterError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        UNKNOWN: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        TREE_TOO_DEEP: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        UNIT_CANNOT_HAVE_CHILDREN: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MULTIPLE_ROOTS: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        INVALID_DIMENSION_VALUE: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MUST_REFINE_HIERARCHICAL_PARENT_TYPE: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        INVALID_PRODUCT_BIDDING_CATEGORY: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        CHANGING_CASE_VALUE_WITH_CHILDREN: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        SUBDIVISION_HAS_CHILDREN: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        DIMENSION_TYPE_NOT_ALLOWED: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        DUPLICATE_WEBPAGE_FILTER_UNDER_ASSET_GROUP: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        LISTING_SOURCE_NOT_ALLOWED: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        FILTER_EXCLUSION_NOT_ALLOWED: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MULTIPLE_LISTING_SOURCES: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MULTIPLE_WEBPAGE_CONDITION_TYPES_NOT_ALLOWED: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MULTIPLE_WEBPAGE_TYPES_PER_ASSET_GROUP: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        PAGE_FEED_FILTER_HAS_PARENT: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        MULTIPLE_OPERATIONS_ON_ONE_NODE: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
        TREE_WAS_INVALID_BEFORE_MUTATION: _ClassVar[AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError]
    UNSPECIFIED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    UNKNOWN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    TREE_TOO_DEEP: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    UNIT_CANNOT_HAVE_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MULTIPLE_ROOTS: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    INVALID_DIMENSION_VALUE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MUST_REFINE_HIERARCHICAL_PARENT_TYPE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    INVALID_PRODUCT_BIDDING_CATEGORY: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    CHANGING_CASE_VALUE_WITH_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    SUBDIVISION_HAS_CHILDREN: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    DIMENSION_TYPE_NOT_ALLOWED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    DUPLICATE_WEBPAGE_FILTER_UNDER_ASSET_GROUP: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    LISTING_SOURCE_NOT_ALLOWED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    FILTER_EXCLUSION_NOT_ALLOWED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MULTIPLE_LISTING_SOURCES: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MULTIPLE_WEBPAGE_CONDITION_TYPES_NOT_ALLOWED: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MULTIPLE_WEBPAGE_TYPES_PER_ASSET_GROUP: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    PAGE_FEED_FILTER_HAS_PARENT: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    MULTIPLE_OPERATIONS_ON_ONE_NODE: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    TREE_WAS_INVALID_BEFORE_MUTATION: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError

    def __init__(self) -> None:
        ...