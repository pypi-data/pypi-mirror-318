from google.ads.googleads.v17.enums import extension_setting_device_pb2 as _extension_setting_device_pb2
from google.ads.googleads.v17.enums import extension_type_pb2 as _extension_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupExtensionSetting(_message.Message):
    __slots__ = ("resource_name", "extension_type", "ad_group", "extension_feed_items", "device")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FEED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    extension_type: _extension_type_pb2.ExtensionTypeEnum.ExtensionType
    ad_group: str
    extension_feed_items: _containers.RepeatedScalarFieldContainer[str]
    device: _extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice
    def __init__(self, resource_name: _Optional[str] = ..., extension_type: _Optional[_Union[_extension_type_pb2.ExtensionTypeEnum.ExtensionType, str]] = ..., ad_group: _Optional[str] = ..., extension_feed_items: _Optional[_Iterable[str]] = ..., device: _Optional[_Union[_extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice, str]] = ...) -> None: ...
