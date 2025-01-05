from google.cloud.deploy.v1 import cloud_deploy_pb2 as _cloud_deploy_pb2
from google.cloud.deploy.v1 import log_enums_pb2 as _log_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReleaseRenderEvent(_message.Message):
    __slots__ = ('message', 'pipeline_uid', 'release', 'type', 'release_render_state')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_UID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_RENDER_STATE_FIELD_NUMBER: _ClassVar[int]
    message: str
    pipeline_uid: str
    release: str
    type: _log_enums_pb2.Type
    release_render_state: _cloud_deploy_pb2.Release.RenderState

    def __init__(self, message: _Optional[str]=..., pipeline_uid: _Optional[str]=..., release: _Optional[str]=..., type: _Optional[_Union[_log_enums_pb2.Type, str]]=..., release_render_state: _Optional[_Union[_cloud_deploy_pb2.Release.RenderState, str]]=...) -> None:
        ...