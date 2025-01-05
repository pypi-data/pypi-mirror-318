from google.ads.googleads.v16.enums import conversion_value_rule_status_pb2 as _conversion_value_rule_status_pb2
from google.ads.googleads.v16.enums import value_rule_device_type_pb2 as _value_rule_device_type_pb2
from google.ads.googleads.v16.enums import value_rule_geo_location_match_type_pb2 as _value_rule_geo_location_match_type_pb2
from google.ads.googleads.v16.enums import value_rule_operation_pb2 as _value_rule_operation_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRule(_message.Message):
    __slots__ = ('resource_name', 'id', 'action', 'geo_location_condition', 'device_condition', 'audience_condition', 'owner_customer', 'status')

    class ValueRuleAction(_message.Message):
        __slots__ = ('operation', 'value')
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operation: _value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation
        value: float

        def __init__(self, operation: _Optional[_Union[_value_rule_operation_pb2.ValueRuleOperationEnum.ValueRuleOperation, str]]=..., value: _Optional[float]=...) -> None:
            ...

    class ValueRuleGeoLocationCondition(_message.Message):
        __slots__ = ('excluded_geo_target_constants', 'excluded_geo_match_type', 'geo_target_constants', 'geo_match_type')
        EXCLUDED_GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_GEO_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        GEO_MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        excluded_geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
        excluded_geo_match_type: _value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
        geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
        geo_match_type: _value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType

        def __init__(self, excluded_geo_target_constants: _Optional[_Iterable[str]]=..., excluded_geo_match_type: _Optional[_Union[_value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType, str]]=..., geo_target_constants: _Optional[_Iterable[str]]=..., geo_match_type: _Optional[_Union[_value_rule_geo_location_match_type_pb2.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType, str]]=...) -> None:
            ...

    class ValueRuleDeviceCondition(_message.Message):
        __slots__ = ('device_types',)
        DEVICE_TYPES_FIELD_NUMBER: _ClassVar[int]
        device_types: _containers.RepeatedScalarFieldContainer[_value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]

        def __init__(self, device_types: _Optional[_Iterable[_Union[_value_rule_device_type_pb2.ValueRuleDeviceTypeEnum.ValueRuleDeviceType, str]]]=...) -> None:
            ...

    class ValueRuleAudienceCondition(_message.Message):
        __slots__ = ('user_lists', 'user_interests')
        USER_LISTS_FIELD_NUMBER: _ClassVar[int]
        USER_INTERESTS_FIELD_NUMBER: _ClassVar[int]
        user_lists: _containers.RepeatedScalarFieldContainer[str]
        user_interests: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, user_lists: _Optional[_Iterable[str]]=..., user_interests: _Optional[_Iterable[str]]=...) -> None:
            ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    action: ConversionValueRule.ValueRuleAction
    geo_location_condition: ConversionValueRule.ValueRuleGeoLocationCondition
    device_condition: ConversionValueRule.ValueRuleDeviceCondition
    audience_condition: ConversionValueRule.ValueRuleAudienceCondition
    owner_customer: str
    status: _conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., action: _Optional[_Union[ConversionValueRule.ValueRuleAction, _Mapping]]=..., geo_location_condition: _Optional[_Union[ConversionValueRule.ValueRuleGeoLocationCondition, _Mapping]]=..., device_condition: _Optional[_Union[ConversionValueRule.ValueRuleDeviceCondition, _Mapping]]=..., audience_condition: _Optional[_Union[ConversionValueRule.ValueRuleAudienceCondition, _Mapping]]=..., owner_customer: _Optional[str]=..., status: _Optional[_Union[_conversion_value_rule_status_pb2.ConversionValueRuleStatusEnum.ConversionValueRuleStatus, str]]=...) -> None:
        ...