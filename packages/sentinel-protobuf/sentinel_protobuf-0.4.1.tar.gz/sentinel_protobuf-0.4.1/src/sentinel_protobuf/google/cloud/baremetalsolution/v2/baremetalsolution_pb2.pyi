from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.baremetalsolution.v2 import instance_pb2 as _instance_pb2
from google.cloud.baremetalsolution.v2 import lun_pb2 as _lun_pb2
from google.cloud.baremetalsolution.v2 import network_pb2 as _network_pb2
from google.cloud.baremetalsolution.v2 import nfs_share_pb2 as _nfs_share_pb2
from google.cloud.baremetalsolution.v2 import osimage_pb2 as _osimage_pb2
from google.cloud.baremetalsolution.v2 import provisioning_pb2 as _provisioning_pb2
from google.cloud.baremetalsolution.v2 import ssh_key_pb2 as _ssh_key_pb2
from google.cloud.baremetalsolution.v2 import volume_pb2 as _volume_pb2
from google.cloud.baremetalsolution.v2 import volume_snapshot_pb2 as _volume_snapshot_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class ResetInstanceResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...