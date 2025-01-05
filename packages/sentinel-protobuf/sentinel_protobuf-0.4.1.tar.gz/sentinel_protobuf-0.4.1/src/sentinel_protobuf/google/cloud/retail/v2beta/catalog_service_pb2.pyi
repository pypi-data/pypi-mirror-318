from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2beta import catalog_pb2 as _catalog_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCatalogsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCatalogsResponse(_message.Message):
    __slots__ = ("catalogs", "next_page_token")
    CATALOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    catalogs: _containers.RepeatedCompositeFieldContainer[_catalog_pb2.Catalog]
    next_page_token: str
    def __init__(self, catalogs: _Optional[_Iterable[_Union[_catalog_pb2.Catalog, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateCatalogRequest(_message.Message):
    __slots__ = ("catalog", "update_mask")
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    catalog: _catalog_pb2.Catalog
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, catalog: _Optional[_Union[_catalog_pb2.Catalog, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetDefaultBranchRequest(_message.Message):
    __slots__ = ("catalog", "branch_id", "note", "force")
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    branch_id: str
    note: str
    force: bool
    def __init__(self, catalog: _Optional[str] = ..., branch_id: _Optional[str] = ..., note: _Optional[str] = ..., force: bool = ...) -> None: ...

class GetDefaultBranchRequest(_message.Message):
    __slots__ = ("catalog",)
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    def __init__(self, catalog: _Optional[str] = ...) -> None: ...

class GetDefaultBranchResponse(_message.Message):
    __slots__ = ("branch", "set_time", "note")
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    SET_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    branch: str
    set_time: _timestamp_pb2.Timestamp
    note: str
    def __init__(self, branch: _Optional[str] = ..., set_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., note: _Optional[str] = ...) -> None: ...

class GetCompletionConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateCompletionConfigRequest(_message.Message):
    __slots__ = ("completion_config", "update_mask")
    COMPLETION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    completion_config: _catalog_pb2.CompletionConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, completion_config: _Optional[_Union[_catalog_pb2.CompletionConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAttributesConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAttributesConfigRequest(_message.Message):
    __slots__ = ("attributes_config", "update_mask")
    ATTRIBUTES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    attributes_config: _catalog_pb2.AttributesConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, attributes_config: _Optional[_Union[_catalog_pb2.AttributesConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AddCatalogAttributeRequest(_message.Message):
    __slots__ = ("attributes_config", "catalog_attribute")
    ATTRIBUTES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attributes_config: str
    catalog_attribute: _catalog_pb2.CatalogAttribute
    def __init__(self, attributes_config: _Optional[str] = ..., catalog_attribute: _Optional[_Union[_catalog_pb2.CatalogAttribute, _Mapping]] = ...) -> None: ...

class RemoveCatalogAttributeRequest(_message.Message):
    __slots__ = ("attributes_config", "key")
    ATTRIBUTES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    attributes_config: str
    key: str
    def __init__(self, attributes_config: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class BatchRemoveCatalogAttributesRequest(_message.Message):
    __slots__ = ("attributes_config", "attribute_keys")
    ATTRIBUTES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEYS_FIELD_NUMBER: _ClassVar[int]
    attributes_config: str
    attribute_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, attributes_config: _Optional[str] = ..., attribute_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchRemoveCatalogAttributesResponse(_message.Message):
    __slots__ = ("deleted_catalog_attributes", "reset_catalog_attributes")
    DELETED_CATALOG_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RESET_CATALOG_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    deleted_catalog_attributes: _containers.RepeatedScalarFieldContainer[str]
    reset_catalog_attributes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deleted_catalog_attributes: _Optional[_Iterable[str]] = ..., reset_catalog_attributes: _Optional[_Iterable[str]] = ...) -> None: ...

class ReplaceCatalogAttributeRequest(_message.Message):
    __slots__ = ("attributes_config", "catalog_attribute", "update_mask")
    ATTRIBUTES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    attributes_config: str
    catalog_attribute: _catalog_pb2.CatalogAttribute
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, attributes_config: _Optional[str] = ..., catalog_attribute: _Optional[_Union[_catalog_pb2.CatalogAttribute, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
