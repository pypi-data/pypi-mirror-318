from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import resource_policy_member_pb2 as _resource_policy_member_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParameterFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARAMETER_FORMAT_UNSPECIFIED: _ClassVar[ParameterFormat]
    UNFORMATTED: _ClassVar[ParameterFormat]
    YAML: _ClassVar[ParameterFormat]
    JSON: _ClassVar[ParameterFormat]

class View(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEW_UNSPECIFIED: _ClassVar[View]
    BASIC: _ClassVar[View]
    FULL: _ClassVar[View]
PARAMETER_FORMAT_UNSPECIFIED: ParameterFormat
UNFORMATTED: ParameterFormat
YAML: ParameterFormat
JSON: ParameterFormat
VIEW_UNSPECIFIED: View
BASIC: View
FULL: View

class Parameter(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'format', 'policy_member')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    POLICY_MEMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    format: ParameterFormat
    policy_member: _resource_policy_member_pb2.ResourcePolicyMember

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., format: _Optional[_Union[ParameterFormat, str]]=..., policy_member: _Optional[_Union[_resource_policy_member_pb2.ResourcePolicyMember, _Mapping]]=...) -> None:
        ...

class ListParametersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListParametersResponse(_message.Message):
    __slots__ = ('parameters', 'next_page_token', 'unreachable')
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[Parameter]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parameters: _Optional[_Iterable[_Union[Parameter, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetParameterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateParameterRequest(_message.Message):
    __slots__ = ('parent', 'parameter_id', 'parameter', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    parameter_id: str
    parameter: Parameter
    request_id: str

    def __init__(self, parent: _Optional[str]=..., parameter_id: _Optional[str]=..., parameter: _Optional[_Union[Parameter, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateParameterRequest(_message.Message):
    __slots__ = ('update_mask', 'parameter', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    parameter: Parameter
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., parameter: _Optional[_Union[Parameter, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteParameterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ParameterVersion(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'disabled', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    disabled: bool
    payload: ParameterVersionPayload

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disabled: bool=..., payload: _Optional[_Union[ParameterVersionPayload, _Mapping]]=...) -> None:
        ...

class ParameterVersionPayload(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes

    def __init__(self, data: _Optional[bytes]=...) -> None:
        ...

class ListParameterVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListParameterVersionsResponse(_message.Message):
    __slots__ = ('parameter_versions', 'next_page_token', 'unreachable')
    PARAMETER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    parameter_versions: _containers.RepeatedCompositeFieldContainer[ParameterVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parameter_versions: _Optional[_Iterable[_Union[ParameterVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetParameterVersionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: View

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[View, str]]=...) -> None:
        ...

class RenderParameterVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RenderParameterVersionResponse(_message.Message):
    __slots__ = ('parameter_version', 'payload', 'rendered_payload')
    PARAMETER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RENDERED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    parameter_version: str
    payload: ParameterVersionPayload
    rendered_payload: bytes

    def __init__(self, parameter_version: _Optional[str]=..., payload: _Optional[_Union[ParameterVersionPayload, _Mapping]]=..., rendered_payload: _Optional[bytes]=...) -> None:
        ...

class CreateParameterVersionRequest(_message.Message):
    __slots__ = ('parent', 'parameter_version_id', 'parameter_version', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    parameter_version_id: str
    parameter_version: ParameterVersion
    request_id: str

    def __init__(self, parent: _Optional[str]=..., parameter_version_id: _Optional[str]=..., parameter_version: _Optional[_Union[ParameterVersion, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateParameterVersionRequest(_message.Message):
    __slots__ = ('update_mask', 'parameter_version', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    parameter_version: ParameterVersion
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., parameter_version: _Optional[_Union[ParameterVersion, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteParameterVersionRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...