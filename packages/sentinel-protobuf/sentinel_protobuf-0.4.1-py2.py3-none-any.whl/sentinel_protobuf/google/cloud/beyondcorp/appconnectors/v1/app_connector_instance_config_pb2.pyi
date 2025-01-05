from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AppConnectorInstanceConfig(_message.Message):
    __slots__ = ('sequence_number', 'instance_config', 'notification_config', 'image_config')
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    sequence_number: int
    instance_config: _any_pb2.Any
    notification_config: NotificationConfig
    image_config: ImageConfig

    def __init__(self, sequence_number: _Optional[int]=..., instance_config: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., image_config: _Optional[_Union[ImageConfig, _Mapping]]=...) -> None:
        ...

class NotificationConfig(_message.Message):
    __slots__ = ('pubsub_notification',)

    class CloudPubSubNotificationConfig(_message.Message):
        __slots__ = ('pubsub_subscription',)
        PUBSUB_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
        pubsub_subscription: str

        def __init__(self, pubsub_subscription: _Optional[str]=...) -> None:
            ...
    PUBSUB_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    pubsub_notification: NotificationConfig.CloudPubSubNotificationConfig

    def __init__(self, pubsub_notification: _Optional[_Union[NotificationConfig.CloudPubSubNotificationConfig, _Mapping]]=...) -> None:
        ...

class ImageConfig(_message.Message):
    __slots__ = ('target_image', 'stable_image')
    TARGET_IMAGE_FIELD_NUMBER: _ClassVar[int]
    STABLE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    target_image: str
    stable_image: str

    def __init__(self, target_image: _Optional[str]=..., stable_image: _Optional[str]=...) -> None:
        ...