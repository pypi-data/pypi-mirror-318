from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Rule(_message.Message):
    __slots__ = ('name', 'rule_description', 'api_type', 'transaction_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    rule_description: str
    api_type: _common_fields_pb2.ApiType
    transaction_type: _common_fields_pb2.TransactionType

    def __init__(self, name: _Optional[str]=..., rule_description: _Optional[str]=..., api_type: _Optional[_Union[_common_fields_pb2.ApiType, str]]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=...) -> None:
        ...

class RuleMetadata(_message.Message):
    __slots__ = ('name', 'description', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[RuleMetadata.Type]
        LIST: _ClassVar[RuleMetadata.Type]
    TYPE_UNSPECIFIED: RuleMetadata.Type
    LIST: RuleMetadata.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: RuleMetadata.Type

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[RuleMetadata.Type, str]]=...) -> None:
        ...

class RuleMetadataValue(_message.Message):
    __slots__ = ('name', 'id', 'account_reference')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    account_reference: _common_fields_pb2.AccountReference

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., account_reference: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=...) -> None:
        ...

class ListRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRulesResponse(_message.Message):
    __slots__ = ('rules', 'next_page_token', 'total_size')
    RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    next_page_token: str
    total_size: int

    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListRuleMetadataRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRuleMetadataResponse(_message.Message):
    __slots__ = ('rule_metadata', 'next_page_token', 'total_size')
    RULE_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    rule_metadata: _containers.RepeatedCompositeFieldContainer[RuleMetadata]
    next_page_token: str
    total_size: int

    def __init__(self, rule_metadata: _Optional[_Iterable[_Union[RuleMetadata, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class ListRuleMetadataValuesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListRuleMetadataValuesResponse(_message.Message):
    __slots__ = ('rule_metadata_values', 'next_page_token')
    RULE_METADATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rule_metadata_values: _containers.RepeatedCompositeFieldContainer[RuleMetadataValue]
    next_page_token: str

    def __init__(self, rule_metadata_values: _Optional[_Iterable[_Union[RuleMetadataValue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchCreateRuleMetadataValuesRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateRuleMetadataValueRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateRuleMetadataValueRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateRuleMetadataValuesResponse(_message.Message):
    __slots__ = ('rule_metadata_value',)
    RULE_METADATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    rule_metadata_value: _containers.RepeatedCompositeFieldContainer[RuleMetadataValue]

    def __init__(self, rule_metadata_value: _Optional[_Iterable[_Union[RuleMetadataValue, _Mapping]]]=...) -> None:
        ...

class CreateRuleMetadataValueRequest(_message.Message):
    __slots__ = ('parent', 'rule_metadata_value')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RULE_METADATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rule_metadata_value: RuleMetadataValue

    def __init__(self, parent: _Optional[str]=..., rule_metadata_value: _Optional[_Union[RuleMetadataValue, _Mapping]]=...) -> None:
        ...

class BatchDeleteRuleMetadataValuesRequest(_message.Message):
    __slots__ = ('parent', 'names')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=...) -> None:
        ...