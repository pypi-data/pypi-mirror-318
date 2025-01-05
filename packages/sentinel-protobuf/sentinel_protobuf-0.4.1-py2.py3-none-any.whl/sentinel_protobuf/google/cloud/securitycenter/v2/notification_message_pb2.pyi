from google.cloud.securitycenter.v2 import finding_pb2 as _finding_pb2
from google.cloud.securitycenter.v2 import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationMessage(_message.Message):
    __slots__ = ('notification_config_name', 'finding', 'resource')
    NOTIFICATION_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    notification_config_name: str
    finding: _finding_pb2.Finding
    resource: _resource_pb2.Resource

    def __init__(self, notification_config_name: _Optional[str]=..., finding: _Optional[_Union[_finding_pb2.Finding, _Mapping]]=..., resource: _Optional[_Union[_resource_pb2.Resource, _Mapping]]=...) -> None:
        ...