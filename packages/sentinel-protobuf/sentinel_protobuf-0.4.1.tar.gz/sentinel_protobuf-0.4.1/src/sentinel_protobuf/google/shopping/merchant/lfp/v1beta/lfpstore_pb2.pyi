from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LfpStore(_message.Message):
    __slots__ = ("name", "target_account", "store_code", "store_address", "store_name", "phone_number", "website_uri", "gcid_category", "place_id", "matching_state", "matching_state_hint")
    class StoreMatchingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORE_MATCHING_STATE_UNSPECIFIED: _ClassVar[LfpStore.StoreMatchingState]
        STORE_MATCHING_STATE_MATCHED: _ClassVar[LfpStore.StoreMatchingState]
        STORE_MATCHING_STATE_FAILED: _ClassVar[LfpStore.StoreMatchingState]
    STORE_MATCHING_STATE_UNSPECIFIED: LfpStore.StoreMatchingState
    STORE_MATCHING_STATE_MATCHED: LfpStore.StoreMatchingState
    STORE_MATCHING_STATE_FAILED: LfpStore.StoreMatchingState
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    STORE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STORE_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URI_FIELD_NUMBER: _ClassVar[int]
    GCID_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHING_STATE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_STATE_HINT_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_account: int
    store_code: str
    store_address: str
    store_name: str
    phone_number: str
    website_uri: str
    gcid_category: _containers.RepeatedScalarFieldContainer[str]
    place_id: str
    matching_state: LfpStore.StoreMatchingState
    matching_state_hint: str
    def __init__(self, name: _Optional[str] = ..., target_account: _Optional[int] = ..., store_code: _Optional[str] = ..., store_address: _Optional[str] = ..., store_name: _Optional[str] = ..., phone_number: _Optional[str] = ..., website_uri: _Optional[str] = ..., gcid_category: _Optional[_Iterable[str]] = ..., place_id: _Optional[str] = ..., matching_state: _Optional[_Union[LfpStore.StoreMatchingState, str]] = ..., matching_state_hint: _Optional[str] = ...) -> None: ...

class GetLfpStoreRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class InsertLfpStoreRequest(_message.Message):
    __slots__ = ("parent", "lfp_store")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LFP_STORE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lfp_store: LfpStore
    def __init__(self, parent: _Optional[str] = ..., lfp_store: _Optional[_Union[LfpStore, _Mapping]] = ...) -> None: ...

class DeleteLfpStoreRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListLfpStoresRequest(_message.Message):
    __slots__ = ("parent", "target_account", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    target_account: int
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., target_account: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListLfpStoresResponse(_message.Message):
    __slots__ = ("lfp_stores", "next_page_token")
    LFP_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    lfp_stores: _containers.RepeatedCompositeFieldContainer[LfpStore]
    next_page_token: str
    def __init__(self, lfp_stores: _Optional[_Iterable[_Union[LfpStore, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
