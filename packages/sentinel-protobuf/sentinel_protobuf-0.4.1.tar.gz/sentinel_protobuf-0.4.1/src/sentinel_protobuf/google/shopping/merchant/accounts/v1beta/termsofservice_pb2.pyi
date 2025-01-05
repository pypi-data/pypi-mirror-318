from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.merchant.accounts.v1beta import termsofservicekind_pb2 as _termsofservicekind_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TermsOfService(_message.Message):
    __slots__ = ("name", "region_code", "kind", "file_uri", "external")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FILE_URI_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    region_code: str
    kind: _termsofservicekind_pb2.TermsOfServiceKind
    file_uri: str
    external: bool
    def __init__(self, name: _Optional[str] = ..., region_code: _Optional[str] = ..., kind: _Optional[_Union[_termsofservicekind_pb2.TermsOfServiceKind, str]] = ..., file_uri: _Optional[str] = ..., external: bool = ...) -> None: ...

class GetTermsOfServiceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RetrieveLatestTermsOfServiceRequest(_message.Message):
    __slots__ = ("region_code", "kind")
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    region_code: str
    kind: _termsofservicekind_pb2.TermsOfServiceKind
    def __init__(self, region_code: _Optional[str] = ..., kind: _Optional[_Union[_termsofservicekind_pb2.TermsOfServiceKind, str]] = ...) -> None: ...

class AcceptTermsOfServiceRequest(_message.Message):
    __slots__ = ("name", "account", "region_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: str
    region_code: str
    def __init__(self, name: _Optional[str] = ..., account: _Optional[str] = ..., region_code: _Optional[str] = ...) -> None: ...
