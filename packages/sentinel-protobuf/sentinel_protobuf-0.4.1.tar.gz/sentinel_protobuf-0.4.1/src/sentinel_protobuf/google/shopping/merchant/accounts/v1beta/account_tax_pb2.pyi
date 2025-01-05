from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.merchant.accounts.v1beta import tax_rule_pb2 as _tax_rule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccountTax(_message.Message):
    __slots__ = ('name', 'account', 'tax_rules')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: int
    tax_rules: _containers.RepeatedCompositeFieldContainer[_tax_rule_pb2.TaxRule]

    def __init__(self, name: _Optional[str]=..., account: _Optional[int]=..., tax_rules: _Optional[_Iterable[_Union[_tax_rule_pb2.TaxRule, _Mapping]]]=...) -> None:
        ...

class GetAccountTaxRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAccountTaxRequest(_message.Message):
    __slots__ = ('account_tax', 'update_mask')
    ACCOUNT_TAX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    account_tax: AccountTax
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, account_tax: _Optional[_Union[AccountTax, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListAccountTaxRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAccountTaxResponse(_message.Message):
    __slots__ = ('account_taxes', 'next_page_token')
    ACCOUNT_TAXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_taxes: _containers.RepeatedCompositeFieldContainer[AccountTax]
    next_page_token: str

    def __init__(self, account_taxes: _Optional[_Iterable[_Union[AccountTax, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...