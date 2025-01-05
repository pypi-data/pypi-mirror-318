from google.ads.googleads.v18.common import user_lists_pb2 as _user_lists_pb2
from google.ads.googleads.v18.enums import access_reason_pb2 as _access_reason_pb2
from google.ads.googleads.v18.enums import user_list_access_status_pb2 as _user_list_access_status_pb2
from google.ads.googleads.v18.enums import user_list_closing_reason_pb2 as _user_list_closing_reason_pb2
from google.ads.googleads.v18.enums import user_list_membership_status_pb2 as _user_list_membership_status_pb2
from google.ads.googleads.v18.enums import user_list_size_range_pb2 as _user_list_size_range_pb2
from google.ads.googleads.v18.enums import user_list_type_pb2 as _user_list_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserList(_message.Message):
    __slots__ = ("resource_name", "id", "read_only", "name", "description", "membership_status", "integration_code", "membership_life_span", "size_for_display", "size_range_for_display", "size_for_search", "size_range_for_search", "type", "closing_reason", "access_reason", "account_user_list_status", "eligible_for_search", "eligible_for_display", "match_rate_percentage", "crm_based_user_list", "similar_user_list", "rule_based_user_list", "logical_user_list", "basic_user_list", "lookalike_user_list")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_STATUS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_CODE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_LIFE_SPAN_FIELD_NUMBER: _ClassVar[int]
    SIZE_FOR_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    SIZE_RANGE_FOR_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FOR_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SIZE_RANGE_FOR_SEARCH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOSING_REASON_FIELD_NUMBER: _ClassVar[int]
    ACCESS_REASON_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_USER_LIST_STATUS_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FOR_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_FOR_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    MATCH_RATE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CRM_BASED_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    RULE_BASED_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    BASIC_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    LOOKALIKE_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    read_only: bool
    name: str
    description: str
    membership_status: _user_list_membership_status_pb2.UserListMembershipStatusEnum.UserListMembershipStatus
    integration_code: str
    membership_life_span: int
    size_for_display: int
    size_range_for_display: _user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange
    size_for_search: int
    size_range_for_search: _user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange
    type: _user_list_type_pb2.UserListTypeEnum.UserListType
    closing_reason: _user_list_closing_reason_pb2.UserListClosingReasonEnum.UserListClosingReason
    access_reason: _access_reason_pb2.AccessReasonEnum.AccessReason
    account_user_list_status: _user_list_access_status_pb2.UserListAccessStatusEnum.UserListAccessStatus
    eligible_for_search: bool
    eligible_for_display: bool
    match_rate_percentage: int
    crm_based_user_list: _user_lists_pb2.CrmBasedUserListInfo
    similar_user_list: _user_lists_pb2.SimilarUserListInfo
    rule_based_user_list: _user_lists_pb2.RuleBasedUserListInfo
    logical_user_list: _user_lists_pb2.LogicalUserListInfo
    basic_user_list: _user_lists_pb2.BasicUserListInfo
    lookalike_user_list: _user_lists_pb2.LookalikeUserListInfo
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., read_only: bool = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., membership_status: _Optional[_Union[_user_list_membership_status_pb2.UserListMembershipStatusEnum.UserListMembershipStatus, str]] = ..., integration_code: _Optional[str] = ..., membership_life_span: _Optional[int] = ..., size_for_display: _Optional[int] = ..., size_range_for_display: _Optional[_Union[_user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange, str]] = ..., size_for_search: _Optional[int] = ..., size_range_for_search: _Optional[_Union[_user_list_size_range_pb2.UserListSizeRangeEnum.UserListSizeRange, str]] = ..., type: _Optional[_Union[_user_list_type_pb2.UserListTypeEnum.UserListType, str]] = ..., closing_reason: _Optional[_Union[_user_list_closing_reason_pb2.UserListClosingReasonEnum.UserListClosingReason, str]] = ..., access_reason: _Optional[_Union[_access_reason_pb2.AccessReasonEnum.AccessReason, str]] = ..., account_user_list_status: _Optional[_Union[_user_list_access_status_pb2.UserListAccessStatusEnum.UserListAccessStatus, str]] = ..., eligible_for_search: bool = ..., eligible_for_display: bool = ..., match_rate_percentage: _Optional[int] = ..., crm_based_user_list: _Optional[_Union[_user_lists_pb2.CrmBasedUserListInfo, _Mapping]] = ..., similar_user_list: _Optional[_Union[_user_lists_pb2.SimilarUserListInfo, _Mapping]] = ..., rule_based_user_list: _Optional[_Union[_user_lists_pb2.RuleBasedUserListInfo, _Mapping]] = ..., logical_user_list: _Optional[_Union[_user_lists_pb2.LogicalUserListInfo, _Mapping]] = ..., basic_user_list: _Optional[_Union[_user_lists_pb2.BasicUserListInfo, _Mapping]] = ..., lookalike_user_list: _Optional[_Union[_user_lists_pb2.LookalikeUserListInfo, _Mapping]] = ...) -> None: ...
