from google.ads.googleads.v16.enums import distance_bucket_pb2 as _distance_bucket_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DistanceView(_message.Message):
    __slots__ = ("resource_name", "distance_bucket", "metric_system")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    METRIC_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    distance_bucket: _distance_bucket_pb2.DistanceBucketEnum.DistanceBucket
    metric_system: bool
    def __init__(self, resource_name: _Optional[str] = ..., distance_bucket: _Optional[_Union[_distance_bucket_pb2.DistanceBucketEnum.DistanceBucket, str]] = ..., metric_system: bool = ...) -> None: ...
