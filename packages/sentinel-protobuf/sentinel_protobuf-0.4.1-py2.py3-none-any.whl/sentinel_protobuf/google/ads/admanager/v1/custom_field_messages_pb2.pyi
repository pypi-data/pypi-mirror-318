from google.ads.admanager.v1 import custom_field_enums_pb2 as _custom_field_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomField(_message.Message):
    __slots__ = ('name', 'custom_field_id', 'display_name', 'description', 'status', 'entity_type', 'data_type', 'visibility', 'options')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_field_id: int
    display_name: str
    description: str
    status: _custom_field_enums_pb2.CustomFieldStatusEnum.CustomFieldStatus
    entity_type: _custom_field_enums_pb2.CustomFieldEntityTypeEnum.CustomFieldEntityType
    data_type: _custom_field_enums_pb2.CustomFieldDataTypeEnum.CustomFieldDataType
    visibility: _custom_field_enums_pb2.CustomFieldVisibilityEnum.CustomFieldVisibility
    options: _containers.RepeatedCompositeFieldContainer[CustomFieldOption]

    def __init__(self, name: _Optional[str]=..., custom_field_id: _Optional[int]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., status: _Optional[_Union[_custom_field_enums_pb2.CustomFieldStatusEnum.CustomFieldStatus, str]]=..., entity_type: _Optional[_Union[_custom_field_enums_pb2.CustomFieldEntityTypeEnum.CustomFieldEntityType, str]]=..., data_type: _Optional[_Union[_custom_field_enums_pb2.CustomFieldDataTypeEnum.CustomFieldDataType, str]]=..., visibility: _Optional[_Union[_custom_field_enums_pb2.CustomFieldVisibilityEnum.CustomFieldVisibility, str]]=..., options: _Optional[_Iterable[_Union[CustomFieldOption, _Mapping]]]=...) -> None:
        ...

class CustomFieldOption(_message.Message):
    __slots__ = ('custom_field_option_id', 'display_name')
    CUSTOM_FIELD_OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    custom_field_option_id: int
    display_name: str

    def __init__(self, custom_field_option_id: _Optional[int]=..., display_name: _Optional[str]=...) -> None:
        ...