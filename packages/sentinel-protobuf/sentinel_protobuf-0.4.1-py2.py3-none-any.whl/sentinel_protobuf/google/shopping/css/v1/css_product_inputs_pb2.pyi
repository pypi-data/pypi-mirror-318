from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.css.v1 import css_product_common_pb2 as _css_product_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CssProductInput(_message.Message):
    __slots__ = ("name", "final_name", "raw_provided_id", "content_language", "feed_label", "freshness_time", "attributes", "custom_attributes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINAL_NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_PROVIDED_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    final_name: str
    raw_provided_id: str
    content_language: str
    feed_label: str
    freshness_time: _timestamp_pb2.Timestamp
    attributes: _css_product_common_pb2.Attributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    def __init__(self, name: _Optional[str] = ..., final_name: _Optional[str] = ..., raw_provided_id: _Optional[str] = ..., content_language: _Optional[str] = ..., feed_label: _Optional[str] = ..., freshness_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Union[_css_product_common_pb2.Attributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class InsertCssProductInputRequest(_message.Message):
    __slots__ = ("parent", "css_product_input", "feed_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CSS_PRODUCT_INPUT_FIELD_NUMBER: _ClassVar[int]
    FEED_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    css_product_input: CssProductInput
    feed_id: int
    def __init__(self, parent: _Optional[str] = ..., css_product_input: _Optional[_Union[CssProductInput, _Mapping]] = ..., feed_id: _Optional[int] = ...) -> None: ...

class UpdateCssProductInputRequest(_message.Message):
    __slots__ = ("css_product_input", "update_mask")
    CSS_PRODUCT_INPUT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    css_product_input: CssProductInput
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, css_product_input: _Optional[_Union[CssProductInput, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteCssProductInputRequest(_message.Message):
    __slots__ = ("name", "supplemental_feed_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_FEED_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    supplemental_feed_id: int
    def __init__(self, name: _Optional[str] = ..., supplemental_feed_id: _Optional[int] = ...) -> None: ...
