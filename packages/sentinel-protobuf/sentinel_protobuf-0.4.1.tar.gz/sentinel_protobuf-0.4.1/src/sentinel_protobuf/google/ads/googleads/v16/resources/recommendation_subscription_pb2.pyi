from google.ads.googleads.v16.enums import recommendation_subscription_status_pb2 as _recommendation_subscription_status_pb2
from google.ads.googleads.v16.enums import recommendation_type_pb2 as _recommendation_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecommendationSubscription(_message.Message):
    __slots__ = ("resource_name", "type", "create_date_time", "modify_date_time", "status")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    type: _recommendation_type_pb2.RecommendationTypeEnum.RecommendationType
    create_date_time: str
    modify_date_time: str
    status: _recommendation_subscription_status_pb2.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    def __init__(self, resource_name: _Optional[str] = ..., type: _Optional[_Union[_recommendation_type_pb2.RecommendationTypeEnum.RecommendationType, str]] = ..., create_date_time: _Optional[str] = ..., modify_date_time: _Optional[str] = ..., status: _Optional[_Union[_recommendation_subscription_status_pb2.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus, str]] = ...) -> None: ...
