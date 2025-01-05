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

class AccountLabel(_message.Message):
    __slots__ = ("name", "label_id", "account_id", "display_name", "description", "label_type")
    class LabelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LABEL_TYPE_UNSPECIFIED: _ClassVar[AccountLabel.LabelType]
        MANUAL: _ClassVar[AccountLabel.LabelType]
        AUTOMATIC: _ClassVar[AccountLabel.LabelType]
    LABEL_TYPE_UNSPECIFIED: AccountLabel.LabelType
    MANUAL: AccountLabel.LabelType
    AUTOMATIC: AccountLabel.LabelType
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    label_id: int
    account_id: int
    display_name: str
    description: str
    label_type: AccountLabel.LabelType
    def __init__(self, name: _Optional[str] = ..., label_id: _Optional[int] = ..., account_id: _Optional[int] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., label_type: _Optional[_Union[AccountLabel.LabelType, str]] = ...) -> None: ...

class ListAccountLabelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAccountLabelsResponse(_message.Message):
    __slots__ = ("account_labels", "next_page_token")
    ACCOUNT_LABELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_labels: _containers.RepeatedCompositeFieldContainer[AccountLabel]
    next_page_token: str
    def __init__(self, account_labels: _Optional[_Iterable[_Union[AccountLabel, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAccountLabelRequest(_message.Message):
    __slots__ = ("parent", "account_label")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account_label: AccountLabel
    def __init__(self, parent: _Optional[str] = ..., account_label: _Optional[_Union[AccountLabel, _Mapping]] = ...) -> None: ...

class UpdateAccountLabelRequest(_message.Message):
    __slots__ = ("account_label",)
    ACCOUNT_LABEL_FIELD_NUMBER: _ClassVar[int]
    account_label: AccountLabel
    def __init__(self, account_label: _Optional[_Union[AccountLabel, _Mapping]] = ...) -> None: ...

class DeleteAccountLabelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
