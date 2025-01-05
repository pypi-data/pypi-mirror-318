from google.cloud.securitycenter.v1 import access_pb2 as _access_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SensitiveAction(_message.Message):
    __slots__ = ('action_type', 'action_time', 'affected_resources', 'source_log_ids', 'learn_more_uri', 'access')

    class SourceLogId(_message.Message):
        __slots__ = ('resource_container', 'log_time', 'insert_id', 'query_uri')
        RESOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        LOG_TIME_FIELD_NUMBER: _ClassVar[int]
        INSERT_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_URI_FIELD_NUMBER: _ClassVar[int]
        resource_container: str
        log_time: _timestamp_pb2.Timestamp
        insert_id: str
        query_uri: str

        def __init__(self, resource_container: _Optional[str]=..., log_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., insert_id: _Optional[str]=..., query_uri: _Optional[str]=...) -> None:
            ...
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOG_IDS_FIELD_NUMBER: _ClassVar[int]
    LEARN_MORE_URI_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    action_time: _timestamp_pb2.Timestamp
    affected_resources: _containers.RepeatedScalarFieldContainer[str]
    source_log_ids: _containers.RepeatedCompositeFieldContainer[SensitiveAction.SourceLogId]
    learn_more_uri: str
    access: _access_pb2.Access

    def __init__(self, action_type: _Optional[str]=..., action_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., affected_resources: _Optional[_Iterable[str]]=..., source_log_ids: _Optional[_Iterable[_Union[SensitiveAction.SourceLogId, _Mapping]]]=..., learn_more_uri: _Optional[str]=..., access: _Optional[_Union[_access_pb2.Access, _Mapping]]=...) -> None:
        ...