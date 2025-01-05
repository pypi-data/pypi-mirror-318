from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v1 import resource_pb2 as _resource_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_VALUE_UNSPECIFIED: _ClassVar[ResourceValue]
    HIGH: _ClassVar[ResourceValue]
    MEDIUM: _ClassVar[ResourceValue]
    LOW: _ClassVar[ResourceValue]
    NONE: _ClassVar[ResourceValue]
RESOURCE_VALUE_UNSPECIFIED: ResourceValue
HIGH: ResourceValue
MEDIUM: ResourceValue
LOW: ResourceValue
NONE: ResourceValue

class ResourceValueConfig(_message.Message):
    __slots__ = ('name', 'resource_value', 'tag_values', 'resource_type', 'scope', 'resource_labels_selector', 'description', 'create_time', 'update_time', 'cloud_provider', 'sensitive_data_protection_mapping')

    class SensitiveDataProtectionMapping(_message.Message):
        __slots__ = ('high_sensitivity_mapping', 'medium_sensitivity_mapping')
        HIGH_SENSITIVITY_MAPPING_FIELD_NUMBER: _ClassVar[int]
        MEDIUM_SENSITIVITY_MAPPING_FIELD_NUMBER: _ClassVar[int]
        high_sensitivity_mapping: ResourceValue
        medium_sensitivity_mapping: ResourceValue

        def __init__(self, high_sensitivity_mapping: _Optional[_Union[ResourceValue, str]]=..., medium_sensitivity_mapping: _Optional[_Union[ResourceValue, str]]=...) -> None:
            ...

    class ResourceLabelsSelectorEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_DATA_PROTECTION_MAPPING_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_value: ResourceValue
    tag_values: _containers.RepeatedScalarFieldContainer[str]
    resource_type: str
    scope: str
    resource_labels_selector: _containers.ScalarMap[str, str]
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    cloud_provider: _resource_pb2_1.CloudProvider
    sensitive_data_protection_mapping: ResourceValueConfig.SensitiveDataProtectionMapping

    def __init__(self, name: _Optional[str]=..., resource_value: _Optional[_Union[ResourceValue, str]]=..., tag_values: _Optional[_Iterable[str]]=..., resource_type: _Optional[str]=..., scope: _Optional[str]=..., resource_labels_selector: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cloud_provider: _Optional[_Union[_resource_pb2_1.CloudProvider, str]]=..., sensitive_data_protection_mapping: _Optional[_Union[ResourceValueConfig.SensitiveDataProtectionMapping, _Mapping]]=...) -> None:
        ...