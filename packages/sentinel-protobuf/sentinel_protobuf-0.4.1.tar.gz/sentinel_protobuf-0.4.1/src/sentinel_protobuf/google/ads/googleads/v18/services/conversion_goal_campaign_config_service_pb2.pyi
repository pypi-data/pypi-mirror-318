from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import conversion_goal_campaign_config_pb2 as _conversion_goal_campaign_config_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateConversionGoalCampaignConfigsRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'validate_only', 'response_content_type')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[ConversionGoalCampaignConfigOperation]
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[ConversionGoalCampaignConfigOperation, _Mapping]]]=..., validate_only: bool=..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]]=...) -> None:
        ...

class ConversionGoalCampaignConfigOperation(_message.Message):
    __slots__ = ('update_mask', 'update')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    update: _conversion_goal_campaign_config_pb2.ConversionGoalCampaignConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., update: _Optional[_Union[_conversion_goal_campaign_config_pb2.ConversionGoalCampaignConfig, _Mapping]]=...) -> None:
        ...

class MutateConversionGoalCampaignConfigsResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateConversionGoalCampaignConfigResult]

    def __init__(self, results: _Optional[_Iterable[_Union[MutateConversionGoalCampaignConfigResult, _Mapping]]]=...) -> None:
        ...

class MutateConversionGoalCampaignConfigResult(_message.Message):
    __slots__ = ('resource_name', 'conversion_goal_campaign_config')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_GOAL_CAMPAIGN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    conversion_goal_campaign_config: _conversion_goal_campaign_config_pb2.ConversionGoalCampaignConfig

    def __init__(self, resource_name: _Optional[str]=..., conversion_goal_campaign_config: _Optional[_Union[_conversion_goal_campaign_config_pb2.ConversionGoalCampaignConfig, _Mapping]]=...) -> None:
        ...