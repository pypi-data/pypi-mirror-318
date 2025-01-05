from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeployPolicyNotificationEvent(_message.Message):
    __slots__ = ('message', 'deploy_policy', 'deploy_policy_uid', 'type')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    deploy_policy: str
    deploy_policy_uid: str
    type: _log_enums_pb2.Type

    def __init__(self, message: _Optional[str]=..., deploy_policy: _Optional[str]=..., deploy_policy_uid: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=...) -> None:
        ...