from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import merchant_center_account_link_pb2 as _merchant_center_account_link_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListMerchantCenterAccountLinksRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListMerchantCenterAccountLinksResponse(_message.Message):
    __slots__ = ('merchant_center_account_links',)
    MERCHANT_CENTER_ACCOUNT_LINKS_FIELD_NUMBER: _ClassVar[int]
    merchant_center_account_links: _containers.RepeatedCompositeFieldContainer[_merchant_center_account_link_pb2.MerchantCenterAccountLink]

    def __init__(self, merchant_center_account_links: _Optional[_Iterable[_Union[_merchant_center_account_link_pb2.MerchantCenterAccountLink, _Mapping]]]=...) -> None:
        ...

class CreateMerchantCenterAccountLinkRequest(_message.Message):
    __slots__ = ('parent', 'merchant_center_account_link')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_ACCOUNT_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    merchant_center_account_link: _merchant_center_account_link_pb2.MerchantCenterAccountLink

    def __init__(self, parent: _Optional[str]=..., merchant_center_account_link: _Optional[_Union[_merchant_center_account_link_pb2.MerchantCenterAccountLink, _Mapping]]=...) -> None:
        ...

class DeleteMerchantCenterAccountLinkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...