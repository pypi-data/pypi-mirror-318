from google.ads.googleads.v17.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.googleads.v17.enums import conversion_value_rule_set_status_pb2 as _conversion_value_rule_set_status_pb2
from google.ads.googleads.v17.enums import value_rule_set_attachment_type_pb2 as _value_rule_set_attachment_type_pb2
from google.ads.googleads.v17.enums import value_rule_set_dimension_pb2 as _value_rule_set_dimension_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRuleSet(_message.Message):
    __slots__ = ('resource_name', 'id', 'conversion_value_rules', 'dimensions', 'owner_customer', 'attachment_type', 'campaign', 'status', 'conversion_action_categories')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_RULES_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    conversion_value_rules: _containers.RepeatedScalarFieldContainer[str]
    dimensions: _containers.RepeatedScalarFieldContainer[_value_rule_set_dimension_pb2.ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    owner_customer: str
    attachment_type: _value_rule_set_attachment_type_pb2.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    campaign: str
    status: _conversion_value_rule_set_status_pb2.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    conversion_action_categories: _containers.RepeatedScalarFieldContainer[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory]

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., conversion_value_rules: _Optional[_Iterable[str]]=..., dimensions: _Optional[_Iterable[_Union[_value_rule_set_dimension_pb2.ValueRuleSetDimensionEnum.ValueRuleSetDimension, str]]]=..., owner_customer: _Optional[str]=..., attachment_type: _Optional[_Union[_value_rule_set_attachment_type_pb2.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType, str]]=..., campaign: _Optional[str]=..., status: _Optional[_Union[_conversion_value_rule_set_status_pb2.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus, str]]=..., conversion_action_categories: _Optional[_Iterable[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]]]=...) -> None:
        ...