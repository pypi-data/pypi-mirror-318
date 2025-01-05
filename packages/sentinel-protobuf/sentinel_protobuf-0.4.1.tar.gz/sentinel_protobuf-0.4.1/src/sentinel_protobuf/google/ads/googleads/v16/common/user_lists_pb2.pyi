from google.ads.googleads.v16.enums import customer_match_upload_key_type_pb2 as _customer_match_upload_key_type_pb2
from google.ads.googleads.v16.enums import lookalike_expansion_level_pb2 as _lookalike_expansion_level_pb2
from google.ads.googleads.v16.enums import user_list_crm_data_source_type_pb2 as _user_list_crm_data_source_type_pb2
from google.ads.googleads.v16.enums import user_list_date_rule_item_operator_pb2 as _user_list_date_rule_item_operator_pb2
from google.ads.googleads.v16.enums import user_list_flexible_rule_operator_pb2 as _user_list_flexible_rule_operator_pb2
from google.ads.googleads.v16.enums import user_list_logical_rule_operator_pb2 as _user_list_logical_rule_operator_pb2
from google.ads.googleads.v16.enums import user_list_number_rule_item_operator_pb2 as _user_list_number_rule_item_operator_pb2
from google.ads.googleads.v16.enums import user_list_prepopulation_status_pb2 as _user_list_prepopulation_status_pb2
from google.ads.googleads.v16.enums import user_list_rule_type_pb2 as _user_list_rule_type_pb2
from google.ads.googleads.v16.enums import user_list_string_rule_item_operator_pb2 as _user_list_string_rule_item_operator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookalikeUserListInfo(_message.Message):
    __slots__ = ("seed_user_list_ids", "expansion_level", "country_codes")
    SEED_USER_LIST_IDS_FIELD_NUMBER: _ClassVar[int]
    EXPANSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODES_FIELD_NUMBER: _ClassVar[int]
    seed_user_list_ids: _containers.RepeatedScalarFieldContainer[int]
    expansion_level: _lookalike_expansion_level_pb2.LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    country_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, seed_user_list_ids: _Optional[_Iterable[int]] = ..., expansion_level: _Optional[_Union[_lookalike_expansion_level_pb2.LookalikeExpansionLevelEnum.LookalikeExpansionLevel, str]] = ..., country_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class SimilarUserListInfo(_message.Message):
    __slots__ = ("seed_user_list",)
    SEED_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    seed_user_list: str
    def __init__(self, seed_user_list: _Optional[str] = ...) -> None: ...

class CrmBasedUserListInfo(_message.Message):
    __slots__ = ("app_id", "upload_key_type", "data_source_type")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    upload_key_type: _customer_match_upload_key_type_pb2.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    data_source_type: _user_list_crm_data_source_type_pb2.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    def __init__(self, app_id: _Optional[str] = ..., upload_key_type: _Optional[_Union[_customer_match_upload_key_type_pb2.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType, str]] = ..., data_source_type: _Optional[_Union[_user_list_crm_data_source_type_pb2.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType, str]] = ...) -> None: ...

class UserListRuleInfo(_message.Message):
    __slots__ = ("rule_type", "rule_item_groups")
    RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_ITEM_GROUPS_FIELD_NUMBER: _ClassVar[int]
    rule_type: _user_list_rule_type_pb2.UserListRuleTypeEnum.UserListRuleType
    rule_item_groups: _containers.RepeatedCompositeFieldContainer[UserListRuleItemGroupInfo]
    def __init__(self, rule_type: _Optional[_Union[_user_list_rule_type_pb2.UserListRuleTypeEnum.UserListRuleType, str]] = ..., rule_item_groups: _Optional[_Iterable[_Union[UserListRuleItemGroupInfo, _Mapping]]] = ...) -> None: ...

class UserListRuleItemGroupInfo(_message.Message):
    __slots__ = ("rule_items",)
    RULE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    rule_items: _containers.RepeatedCompositeFieldContainer[UserListRuleItemInfo]
    def __init__(self, rule_items: _Optional[_Iterable[_Union[UserListRuleItemInfo, _Mapping]]] = ...) -> None: ...

class UserListRuleItemInfo(_message.Message):
    __slots__ = ("name", "number_rule_item", "string_rule_item", "date_rule_item")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_RULE_ITEM_FIELD_NUMBER: _ClassVar[int]
    STRING_RULE_ITEM_FIELD_NUMBER: _ClassVar[int]
    DATE_RULE_ITEM_FIELD_NUMBER: _ClassVar[int]
    name: str
    number_rule_item: UserListNumberRuleItemInfo
    string_rule_item: UserListStringRuleItemInfo
    date_rule_item: UserListDateRuleItemInfo
    def __init__(self, name: _Optional[str] = ..., number_rule_item: _Optional[_Union[UserListNumberRuleItemInfo, _Mapping]] = ..., string_rule_item: _Optional[_Union[UserListStringRuleItemInfo, _Mapping]] = ..., date_rule_item: _Optional[_Union[UserListDateRuleItemInfo, _Mapping]] = ...) -> None: ...

class UserListDateRuleItemInfo(_message.Message):
    __slots__ = ("operator", "value", "offset_in_days")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    operator: _user_list_date_rule_item_operator_pb2.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    value: str
    offset_in_days: int
    def __init__(self, operator: _Optional[_Union[_user_list_date_rule_item_operator_pb2.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator, str]] = ..., value: _Optional[str] = ..., offset_in_days: _Optional[int] = ...) -> None: ...

class UserListNumberRuleItemInfo(_message.Message):
    __slots__ = ("operator", "value")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operator: _user_list_number_rule_item_operator_pb2.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    value: float
    def __init__(self, operator: _Optional[_Union[_user_list_number_rule_item_operator_pb2.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator, str]] = ..., value: _Optional[float] = ...) -> None: ...

class UserListStringRuleItemInfo(_message.Message):
    __slots__ = ("operator", "value")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operator: _user_list_string_rule_item_operator_pb2.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    value: str
    def __init__(self, operator: _Optional[_Union[_user_list_string_rule_item_operator_pb2.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator, str]] = ..., value: _Optional[str] = ...) -> None: ...

class FlexibleRuleOperandInfo(_message.Message):
    __slots__ = ("rule", "lookback_window_days")
    RULE_FIELD_NUMBER: _ClassVar[int]
    LOOKBACK_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    rule: UserListRuleInfo
    lookback_window_days: int
    def __init__(self, rule: _Optional[_Union[UserListRuleInfo, _Mapping]] = ..., lookback_window_days: _Optional[int] = ...) -> None: ...

class FlexibleRuleUserListInfo(_message.Message):
    __slots__ = ("inclusive_rule_operator", "inclusive_operands", "exclusive_operands")
    INCLUSIVE_RULE_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    inclusive_rule_operator: _user_list_flexible_rule_operator_pb2.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    inclusive_operands: _containers.RepeatedCompositeFieldContainer[FlexibleRuleOperandInfo]
    exclusive_operands: _containers.RepeatedCompositeFieldContainer[FlexibleRuleOperandInfo]
    def __init__(self, inclusive_rule_operator: _Optional[_Union[_user_list_flexible_rule_operator_pb2.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator, str]] = ..., inclusive_operands: _Optional[_Iterable[_Union[FlexibleRuleOperandInfo, _Mapping]]] = ..., exclusive_operands: _Optional[_Iterable[_Union[FlexibleRuleOperandInfo, _Mapping]]] = ...) -> None: ...

class RuleBasedUserListInfo(_message.Message):
    __slots__ = ("prepopulation_status", "flexible_rule_user_list")
    PREPOPULATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    FLEXIBLE_RULE_USER_LIST_FIELD_NUMBER: _ClassVar[int]
    prepopulation_status: _user_list_prepopulation_status_pb2.UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    flexible_rule_user_list: FlexibleRuleUserListInfo
    def __init__(self, prepopulation_status: _Optional[_Union[_user_list_prepopulation_status_pb2.UserListPrepopulationStatusEnum.UserListPrepopulationStatus, str]] = ..., flexible_rule_user_list: _Optional[_Union[FlexibleRuleUserListInfo, _Mapping]] = ...) -> None: ...

class LogicalUserListInfo(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[UserListLogicalRuleInfo]
    def __init__(self, rules: _Optional[_Iterable[_Union[UserListLogicalRuleInfo, _Mapping]]] = ...) -> None: ...

class UserListLogicalRuleInfo(_message.Message):
    __slots__ = ("operator", "rule_operands")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    RULE_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    operator: _user_list_logical_rule_operator_pb2.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    rule_operands: _containers.RepeatedCompositeFieldContainer[LogicalUserListOperandInfo]
    def __init__(self, operator: _Optional[_Union[_user_list_logical_rule_operator_pb2.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator, str]] = ..., rule_operands: _Optional[_Iterable[_Union[LogicalUserListOperandInfo, _Mapping]]] = ...) -> None: ...

class LogicalUserListOperandInfo(_message.Message):
    __slots__ = ("user_list",)
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: str
    def __init__(self, user_list: _Optional[str] = ...) -> None: ...

class BasicUserListInfo(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[UserListActionInfo]
    def __init__(self, actions: _Optional[_Iterable[_Union[UserListActionInfo, _Mapping]]] = ...) -> None: ...

class UserListActionInfo(_message.Message):
    __slots__ = ("conversion_action", "remarketing_action")
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    REMARKETING_ACTION_FIELD_NUMBER: _ClassVar[int]
    conversion_action: str
    remarketing_action: str
    def __init__(self, conversion_action: _Optional[str] = ..., remarketing_action: _Optional[str] = ...) -> None: ...
