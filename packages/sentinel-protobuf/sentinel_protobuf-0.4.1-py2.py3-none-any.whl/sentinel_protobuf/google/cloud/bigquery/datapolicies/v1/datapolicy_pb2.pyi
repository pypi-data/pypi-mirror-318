from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDataPolicyRequest(_message.Message):
    __slots__ = ('parent', 'data_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_policy: DataPolicy

    def __init__(self, parent: _Optional[str]=..., data_policy: _Optional[_Union[DataPolicy, _Mapping]]=...) -> None:
        ...

class UpdateDataPolicyRequest(_message.Message):
    __slots__ = ('data_policy', 'update_mask')
    DATA_POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_policy: DataPolicy
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, data_policy: _Optional[_Union[DataPolicy, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameDataPolicyRequest(_message.Message):
    __slots__ = ('name', 'new_data_policy_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_DATA_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_data_policy_id: str

    def __init__(self, name: _Optional[str]=..., new_data_policy_id: _Optional[str]=...) -> None:
        ...

class DeleteDataPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetDataPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListDataPoliciesResponse(_message.Message):
    __slots__ = ('data_policies', 'next_page_token')
    DATA_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_policies: _containers.RepeatedCompositeFieldContainer[DataPolicy]
    next_page_token: str

    def __init__(self, data_policies: _Optional[_Iterable[_Union[DataPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DataPolicy(_message.Message):
    __slots__ = ('policy_tag', 'data_masking_policy', 'name', 'data_policy_type', 'data_policy_id')

    class DataPolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_POLICY_TYPE_UNSPECIFIED: _ClassVar[DataPolicy.DataPolicyType]
        COLUMN_LEVEL_SECURITY_POLICY: _ClassVar[DataPolicy.DataPolicyType]
        DATA_MASKING_POLICY: _ClassVar[DataPolicy.DataPolicyType]
    DATA_POLICY_TYPE_UNSPECIFIED: DataPolicy.DataPolicyType
    COLUMN_LEVEL_SECURITY_POLICY: DataPolicy.DataPolicyType
    DATA_MASKING_POLICY: DataPolicy.DataPolicyType
    POLICY_TAG_FIELD_NUMBER: _ClassVar[int]
    DATA_MASKING_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    policy_tag: str
    data_masking_policy: DataMaskingPolicy
    name: str
    data_policy_type: DataPolicy.DataPolicyType
    data_policy_id: str

    def __init__(self, policy_tag: _Optional[str]=..., data_masking_policy: _Optional[_Union[DataMaskingPolicy, _Mapping]]=..., name: _Optional[str]=..., data_policy_type: _Optional[_Union[DataPolicy.DataPolicyType, str]]=..., data_policy_id: _Optional[str]=...) -> None:
        ...

class DataMaskingPolicy(_message.Message):
    __slots__ = ('predefined_expression', 'routine')

    class PredefinedExpression(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREDEFINED_EXPRESSION_UNSPECIFIED: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        SHA256: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        ALWAYS_NULL: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        DEFAULT_MASKING_VALUE: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        LAST_FOUR_CHARACTERS: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        FIRST_FOUR_CHARACTERS: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        EMAIL_MASK: _ClassVar[DataMaskingPolicy.PredefinedExpression]
        DATE_YEAR_MASK: _ClassVar[DataMaskingPolicy.PredefinedExpression]
    PREDEFINED_EXPRESSION_UNSPECIFIED: DataMaskingPolicy.PredefinedExpression
    SHA256: DataMaskingPolicy.PredefinedExpression
    ALWAYS_NULL: DataMaskingPolicy.PredefinedExpression
    DEFAULT_MASKING_VALUE: DataMaskingPolicy.PredefinedExpression
    LAST_FOUR_CHARACTERS: DataMaskingPolicy.PredefinedExpression
    FIRST_FOUR_CHARACTERS: DataMaskingPolicy.PredefinedExpression
    EMAIL_MASK: DataMaskingPolicy.PredefinedExpression
    DATE_YEAR_MASK: DataMaskingPolicy.PredefinedExpression
    PREDEFINED_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    predefined_expression: DataMaskingPolicy.PredefinedExpression
    routine: str

    def __init__(self, predefined_expression: _Optional[_Union[DataMaskingPolicy.PredefinedExpression, str]]=..., routine: _Optional[str]=...) -> None:
        ...