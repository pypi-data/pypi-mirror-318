from google.ads.googleads.v16.enums import goal_config_level_pb2 as _goal_config_level_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionGoalCampaignConfig(_message.Message):
    __slots__ = ('resource_name', 'campaign', 'goal_config_level', 'custom_conversion_goal')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    GOAL_CONFIG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONVERSION_GOAL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    goal_config_level: _goal_config_level_pb2.GoalConfigLevelEnum.GoalConfigLevel
    custom_conversion_goal: str

    def __init__(self, resource_name: _Optional[str]=..., campaign: _Optional[str]=..., goal_config_level: _Optional[_Union[_goal_config_level_pb2.GoalConfigLevelEnum.GoalConfigLevel, str]]=..., custom_conversion_goal: _Optional[str]=...) -> None:
        ...