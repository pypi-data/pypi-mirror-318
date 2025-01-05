from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudDlpDataProfile(_message.Message):
    __slots__ = ('data_profile', 'parent_type')

    class ParentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARENT_TYPE_UNSPECIFIED: _ClassVar[CloudDlpDataProfile.ParentType]
        ORGANIZATION: _ClassVar[CloudDlpDataProfile.ParentType]
        PROJECT: _ClassVar[CloudDlpDataProfile.ParentType]
    PARENT_TYPE_UNSPECIFIED: CloudDlpDataProfile.ParentType
    ORGANIZATION: CloudDlpDataProfile.ParentType
    PROJECT: CloudDlpDataProfile.ParentType
    DATA_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    data_profile: str
    parent_type: CloudDlpDataProfile.ParentType

    def __init__(self, data_profile: _Optional[str]=..., parent_type: _Optional[_Union[CloudDlpDataProfile.ParentType, str]]=...) -> None:
        ...