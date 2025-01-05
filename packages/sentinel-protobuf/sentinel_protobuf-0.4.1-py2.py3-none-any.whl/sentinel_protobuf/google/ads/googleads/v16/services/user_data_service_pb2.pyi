from google.ads.googleads.v16.common import offline_user_data_pb2 as _offline_user_data_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadUserDataRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "customer_match_user_list_metadata")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MATCH_USER_LIST_METADATA_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[UserDataOperation]
    customer_match_user_list_metadata: _offline_user_data_pb2.CustomerMatchUserListMetadata
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[UserDataOperation, _Mapping]]] = ..., customer_match_user_list_metadata: _Optional[_Union[_offline_user_data_pb2.CustomerMatchUserListMetadata, _Mapping]] = ...) -> None: ...

class UserDataOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _offline_user_data_pb2.UserData
    remove: _offline_user_data_pb2.UserData
    def __init__(self, create: _Optional[_Union[_offline_user_data_pb2.UserData, _Mapping]] = ..., remove: _Optional[_Union[_offline_user_data_pb2.UserData, _Mapping]] = ...) -> None: ...

class UploadUserDataResponse(_message.Message):
    __slots__ = ("upload_date_time", "received_operations_count")
    UPLOAD_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_OPERATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    upload_date_time: str
    received_operations_count: int
    def __init__(self, upload_date_time: _Optional[str] = ..., received_operations_count: _Optional[int] = ...) -> None: ...
