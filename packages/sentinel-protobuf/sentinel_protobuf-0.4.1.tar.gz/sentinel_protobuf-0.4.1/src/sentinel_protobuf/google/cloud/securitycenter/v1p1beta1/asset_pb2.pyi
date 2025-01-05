from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1p1beta1 import folder_pb2 as _folder_pb2
from google.cloud.securitycenter.v1p1beta1 import security_marks_pb2 as _security_marks_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ('name', 'security_center_properties', 'resource_properties', 'security_marks', 'create_time', 'update_time', 'iam_policy', 'canonical_name')

    class SecurityCenterProperties(_message.Message):
        __slots__ = ('resource_name', 'resource_type', 'resource_parent', 'resource_project', 'resource_owners', 'resource_display_name', 'resource_parent_display_name', 'resource_project_display_name', 'folders')
        RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_PARENT_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_PROJECT_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_OWNERS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        FOLDERS_FIELD_NUMBER: _ClassVar[int]
        resource_name: str
        resource_type: str
        resource_parent: str
        resource_project: str
        resource_owners: _containers.RepeatedScalarFieldContainer[str]
        resource_display_name: str
        resource_parent_display_name: str
        resource_project_display_name: str
        folders: _containers.RepeatedCompositeFieldContainer[_folder_pb2.Folder]

        def __init__(self, resource_name: _Optional[str]=..., resource_type: _Optional[str]=..., resource_parent: _Optional[str]=..., resource_project: _Optional[str]=..., resource_owners: _Optional[_Iterable[str]]=..., resource_display_name: _Optional[str]=..., resource_parent_display_name: _Optional[str]=..., resource_project_display_name: _Optional[str]=..., folders: _Optional[_Iterable[_Union[_folder_pb2.Folder, _Mapping]]]=...) -> None:
            ...

    class IamPolicy(_message.Message):
        __slots__ = ('policy_blob',)
        POLICY_BLOB_FIELD_NUMBER: _ClassVar[int]
        policy_blob: str

        def __init__(self, policy_blob: _Optional[str]=...) -> None:
            ...

    class ResourcePropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CENTER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    IAM_POLICY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    security_center_properties: Asset.SecurityCenterProperties
    resource_properties: _containers.MessageMap[str, _struct_pb2.Value]
    security_marks: _security_marks_pb2.SecurityMarks
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    iam_policy: Asset.IamPolicy
    canonical_name: str

    def __init__(self, name: _Optional[str]=..., security_center_properties: _Optional[_Union[Asset.SecurityCenterProperties, _Mapping]]=..., resource_properties: _Optional[_Mapping[str, _struct_pb2.Value]]=..., security_marks: _Optional[_Union[_security_marks_pb2.SecurityMarks, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., iam_policy: _Optional[_Union[Asset.IamPolicy, _Mapping]]=..., canonical_name: _Optional[str]=...) -> None:
        ...