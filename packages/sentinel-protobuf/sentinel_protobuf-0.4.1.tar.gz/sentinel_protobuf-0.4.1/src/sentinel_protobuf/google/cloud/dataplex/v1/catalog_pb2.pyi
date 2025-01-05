from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import service_pb2 as _service_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntryView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTRY_VIEW_UNSPECIFIED: _ClassVar[EntryView]
    BASIC: _ClassVar[EntryView]
    FULL: _ClassVar[EntryView]
    CUSTOM: _ClassVar[EntryView]
    ALL: _ClassVar[EntryView]

class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_STATUS_UNSPECIFIED: _ClassVar[TransferStatus]
    TRANSFER_STATUS_MIGRATED: _ClassVar[TransferStatus]
    TRANSFER_STATUS_TRANSFERRED: _ClassVar[TransferStatus]
ENTRY_VIEW_UNSPECIFIED: EntryView
BASIC: EntryView
FULL: EntryView
CUSTOM: EntryView
ALL: EntryView
TRANSFER_STATUS_UNSPECIFIED: TransferStatus
TRANSFER_STATUS_MIGRATED: TransferStatus
TRANSFER_STATUS_TRANSFERRED: TransferStatus

class AspectType(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'etag', 'authorization', 'metadata_template', 'transfer_status')

    class Authorization(_message.Message):
        __slots__ = ('alternate_use_permission',)
        ALTERNATE_USE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        alternate_use_permission: str

        def __init__(self, alternate_use_permission: _Optional[str]=...) -> None:
            ...

    class MetadataTemplate(_message.Message):
        __slots__ = ('index', 'name', 'type', 'record_fields', 'enum_values', 'map_items', 'array_items', 'type_id', 'type_ref', 'constraints', 'annotations')

        class EnumValue(_message.Message):
            __slots__ = ('index', 'name', 'deprecated')
            INDEX_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            DEPRECATED_FIELD_NUMBER: _ClassVar[int]
            index: int
            name: str
            deprecated: str

            def __init__(self, index: _Optional[int]=..., name: _Optional[str]=..., deprecated: _Optional[str]=...) -> None:
                ...

        class Constraints(_message.Message):
            __slots__ = ('required',)
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            required: bool

            def __init__(self, required: bool=...) -> None:
                ...

        class Annotations(_message.Message):
            __slots__ = ('deprecated', 'display_name', 'description', 'display_order', 'string_type', 'string_values')
            DEPRECATED_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
            STRING_TYPE_FIELD_NUMBER: _ClassVar[int]
            STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
            deprecated: str
            display_name: str
            description: str
            display_order: int
            string_type: str
            string_values: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, deprecated: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., display_order: _Optional[int]=..., string_type: _Optional[str]=..., string_values: _Optional[_Iterable[str]]=...) -> None:
                ...
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RECORD_FIELDS_FIELD_NUMBER: _ClassVar[int]
        ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
        MAP_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ARRAY_ITEMS_FIELD_NUMBER: _ClassVar[int]
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_REF_FIELD_NUMBER: _ClassVar[int]
        CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        index: int
        name: str
        type: str
        record_fields: _containers.RepeatedCompositeFieldContainer[AspectType.MetadataTemplate]
        enum_values: _containers.RepeatedCompositeFieldContainer[AspectType.MetadataTemplate.EnumValue]
        map_items: AspectType.MetadataTemplate
        array_items: AspectType.MetadataTemplate
        type_id: str
        type_ref: str
        constraints: AspectType.MetadataTemplate.Constraints
        annotations: AspectType.MetadataTemplate.Annotations

        def __init__(self, index: _Optional[int]=..., name: _Optional[str]=..., type: _Optional[str]=..., record_fields: _Optional[_Iterable[_Union[AspectType.MetadataTemplate, _Mapping]]]=..., enum_values: _Optional[_Iterable[_Union[AspectType.MetadataTemplate.EnumValue, _Mapping]]]=..., map_items: _Optional[_Union[AspectType.MetadataTemplate, _Mapping]]=..., array_items: _Optional[_Union[AspectType.MetadataTemplate, _Mapping]]=..., type_id: _Optional[str]=..., type_ref: _Optional[str]=..., constraints: _Optional[_Union[AspectType.MetadataTemplate.Constraints, _Mapping]]=..., annotations: _Optional[_Union[AspectType.MetadataTemplate.Annotations, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    etag: str
    authorization: AspectType.Authorization
    metadata_template: AspectType.MetadataTemplate
    transfer_status: TransferStatus

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., authorization: _Optional[_Union[AspectType.Authorization, _Mapping]]=..., metadata_template: _Optional[_Union[AspectType.MetadataTemplate, _Mapping]]=..., transfer_status: _Optional[_Union[TransferStatus, str]]=...) -> None:
        ...

class EntryGroup(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'etag', 'transfer_status')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    etag: str
    transfer_status: TransferStatus

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., transfer_status: _Optional[_Union[TransferStatus, str]]=...) -> None:
        ...

class EntryType(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'display_name', 'labels', 'etag', 'type_aliases', 'platform', 'system', 'required_aspects', 'authorization')

    class AspectInfo(_message.Message):
        __slots__ = ('type',)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str

        def __init__(self, type: _Optional[str]=...) -> None:
            ...

    class Authorization(_message.Message):
        __slots__ = ('alternate_use_permission',)
        ALTERNATE_USE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        alternate_use_permission: str

        def __init__(self, alternate_use_permission: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_ALIASES_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ASPECTS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    etag: str
    type_aliases: _containers.RepeatedScalarFieldContainer[str]
    platform: str
    system: str
    required_aspects: _containers.RepeatedCompositeFieldContainer[EntryType.AspectInfo]
    authorization: EntryType.Authorization

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., type_aliases: _Optional[_Iterable[str]]=..., platform: _Optional[str]=..., system: _Optional[str]=..., required_aspects: _Optional[_Iterable[_Union[EntryType.AspectInfo, _Mapping]]]=..., authorization: _Optional[_Union[EntryType.Authorization, _Mapping]]=...) -> None:
        ...

class Aspect(_message.Message):
    __slots__ = ('aspect_type', 'path', 'create_time', 'update_time', 'data', 'aspect_source')
    ASPECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ASPECT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    aspect_type: str
    path: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    data: _struct_pb2.Struct
    aspect_source: AspectSource

    def __init__(self, aspect_type: _Optional[str]=..., path: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., aspect_source: _Optional[_Union[AspectSource, _Mapping]]=...) -> None:
        ...

class AspectSource(_message.Message):
    __slots__ = ('create_time', 'update_time', 'data_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    data_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_version: _Optional[str]=...) -> None:
        ...

class Entry(_message.Message):
    __slots__ = ('name', 'entry_type', 'create_time', 'update_time', 'aspects', 'parent_entry', 'fully_qualified_name', 'entry_source')

    class AspectsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Aspect

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Aspect, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ASPECTS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTRY_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    entry_type: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    aspects: _containers.MessageMap[str, Aspect]
    parent_entry: str
    fully_qualified_name: str
    entry_source: EntrySource

    def __init__(self, name: _Optional[str]=..., entry_type: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., aspects: _Optional[_Mapping[str, Aspect]]=..., parent_entry: _Optional[str]=..., fully_qualified_name: _Optional[str]=..., entry_source: _Optional[_Union[EntrySource, _Mapping]]=...) -> None:
        ...

class EntrySource(_message.Message):
    __slots__ = ('resource', 'system', 'platform', 'display_name', 'description', 'labels', 'ancestors', 'create_time', 'update_time', 'location')

    class Ancestor(_message.Message):
        __slots__ = ('name', 'type')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str

        def __init__(self, name: _Optional[str]=..., type: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    system: str
    platform: str
    display_name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    ancestors: _containers.RepeatedCompositeFieldContainer[EntrySource.Ancestor]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    location: str

    def __init__(self, resource: _Optional[str]=..., system: _Optional[str]=..., platform: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., ancestors: _Optional[_Iterable[_Union[EntrySource.Ancestor, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class CreateEntryGroupRequest(_message.Message):
    __slots__ = ('parent', 'entry_group_id', 'entry_group', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_group_id: str
    entry_group: EntryGroup
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., entry_group_id: _Optional[str]=..., entry_group: _Optional[_Union[EntryGroup, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateEntryGroupRequest(_message.Message):
    __slots__ = ('entry_group', 'update_mask', 'validate_only')
    ENTRY_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    entry_group: EntryGroup
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, entry_group: _Optional[_Union[EntryGroup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteEntryGroupRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListEntryGroupsRequest(_message.Message):
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

class ListEntryGroupsResponse(_message.Message):
    __slots__ = ('entry_groups', 'next_page_token', 'unreachable_locations')
    ENTRY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    entry_groups: _containers.RepeatedCompositeFieldContainer[EntryGroup]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, entry_groups: _Optional[_Iterable[_Union[EntryGroup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEntryGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEntryTypeRequest(_message.Message):
    __slots__ = ('parent', 'entry_type_id', 'entry_type', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_type_id: str
    entry_type: EntryType
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., entry_type_id: _Optional[str]=..., entry_type: _Optional[_Union[EntryType, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateEntryTypeRequest(_message.Message):
    __slots__ = ('entry_type', 'update_mask', 'validate_only')
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    entry_type: EntryType
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, entry_type: _Optional[_Union[EntryType, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteEntryTypeRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListEntryTypesRequest(_message.Message):
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

class ListEntryTypesResponse(_message.Message):
    __slots__ = ('entry_types', 'next_page_token', 'unreachable_locations')
    ENTRY_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    entry_types: _containers.RepeatedCompositeFieldContainer[EntryType]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, entry_types: _Optional[_Iterable[_Union[EntryType, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEntryTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAspectTypeRequest(_message.Message):
    __slots__ = ('parent', 'aspect_type_id', 'aspect_type', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASPECT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ASPECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    aspect_type_id: str
    aspect_type: AspectType
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., aspect_type_id: _Optional[str]=..., aspect_type: _Optional[_Union[AspectType, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateAspectTypeRequest(_message.Message):
    __slots__ = ('aspect_type', 'update_mask', 'validate_only')
    ASPECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    aspect_type: AspectType
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, aspect_type: _Optional[_Union[AspectType, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteAspectTypeRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListAspectTypesRequest(_message.Message):
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

class ListAspectTypesResponse(_message.Message):
    __slots__ = ('aspect_types', 'next_page_token', 'unreachable_locations')
    ASPECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    aspect_types: _containers.RepeatedCompositeFieldContainer[AspectType]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, aspect_types: _Optional[_Iterable[_Union[AspectType, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAspectTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEntryRequest(_message.Message):
    __slots__ = ('parent', 'entry_id', 'entry')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entry_id: str
    entry: Entry

    def __init__(self, parent: _Optional[str]=..., entry_id: _Optional[str]=..., entry: _Optional[_Union[Entry, _Mapping]]=...) -> None:
        ...

class UpdateEntryRequest(_message.Message):
    __slots__ = ('entry', 'update_mask', 'allow_missing', 'delete_missing_aspects', 'aspect_keys')
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    DELETE_MISSING_ASPECTS_FIELD_NUMBER: _ClassVar[int]
    ASPECT_KEYS_FIELD_NUMBER: _ClassVar[int]
    entry: Entry
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    delete_missing_aspects: bool
    aspect_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, entry: _Optional[_Union[Entry, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., allow_missing: bool=..., delete_missing_aspects: bool=..., aspect_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteEntryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEntriesRequest(_message.Message):
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

class ListEntriesResponse(_message.Message):
    __slots__ = ('entries', 'next_page_token')
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Entry]
    next_page_token: str

    def __init__(self, entries: _Optional[_Iterable[_Union[Entry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEntryRequest(_message.Message):
    __slots__ = ('name', 'view', 'aspect_types', 'paths')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ASPECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: EntryView
    aspect_types: _containers.RepeatedScalarFieldContainer[str]
    paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[EntryView, str]]=..., aspect_types: _Optional[_Iterable[str]]=..., paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class LookupEntryRequest(_message.Message):
    __slots__ = ('name', 'view', 'aspect_types', 'paths', 'entry')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ASPECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: EntryView
    aspect_types: _containers.RepeatedScalarFieldContainer[str]
    paths: _containers.RepeatedScalarFieldContainer[str]
    entry: str

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[EntryView, str]]=..., aspect_types: _Optional[_Iterable[str]]=..., paths: _Optional[_Iterable[str]]=..., entry: _Optional[str]=...) -> None:
        ...

class SearchEntriesRequest(_message.Message):
    __slots__ = ('name', 'query', 'page_size', 'page_token', 'order_by', 'scope')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    page_size: int
    page_token: str
    order_by: str
    scope: str

    def __init__(self, name: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., scope: _Optional[str]=...) -> None:
        ...

class SearchEntriesResult(_message.Message):
    __slots__ = ('linked_resource', 'dataplex_entry', 'snippets')

    class Snippets(_message.Message):
        __slots__ = ('dataplex_entry',)
        DATAPLEX_ENTRY_FIELD_NUMBER: _ClassVar[int]
        dataplex_entry: Entry

        def __init__(self, dataplex_entry: _Optional[_Union[Entry, _Mapping]]=...) -> None:
            ...
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_ENTRY_FIELD_NUMBER: _ClassVar[int]
    SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    linked_resource: str
    dataplex_entry: Entry
    snippets: SearchEntriesResult.Snippets

    def __init__(self, linked_resource: _Optional[str]=..., dataplex_entry: _Optional[_Union[Entry, _Mapping]]=..., snippets: _Optional[_Union[SearchEntriesResult.Snippets, _Mapping]]=...) -> None:
        ...

class SearchEntriesResponse(_message.Message):
    __slots__ = ('results', 'total_size', 'next_page_token', 'unreachable')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchEntriesResult]
    total_size: int
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, results: _Optional[_Iterable[_Union[SearchEntriesResult, _Mapping]]]=..., total_size: _Optional[int]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ImportItem(_message.Message):
    __slots__ = ('entry', 'update_mask', 'aspect_keys')
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ASPECT_KEYS_FIELD_NUMBER: _ClassVar[int]
    entry: Entry
    update_mask: _field_mask_pb2.FieldMask
    aspect_keys: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, entry: _Optional[_Union[Entry, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., aspect_keys: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateMetadataJobRequest(_message.Message):
    __slots__ = ('parent', 'metadata_job', 'metadata_job_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_JOB_FIELD_NUMBER: _ClassVar[int]
    METADATA_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metadata_job: MetadataJob
    metadata_job_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., metadata_job: _Optional[_Union[MetadataJob, _Mapping]]=..., metadata_job_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class GetMetadataJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMetadataJobsRequest(_message.Message):
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

class ListMetadataJobsResponse(_message.Message):
    __slots__ = ('metadata_jobs', 'next_page_token', 'unreachable_locations')
    METADATA_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    metadata_jobs: _containers.RepeatedCompositeFieldContainer[MetadataJob]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, metadata_jobs: _Optional[_Iterable[_Union[MetadataJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class CancelMetadataJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class MetadataJob(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'labels', 'type', 'import_spec', 'import_result', 'status')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[MetadataJob.Type]
        IMPORT: _ClassVar[MetadataJob.Type]
    TYPE_UNSPECIFIED: MetadataJob.Type
    IMPORT: MetadataJob.Type

    class ImportJobResult(_message.Message):
        __slots__ = ('deleted_entries', 'updated_entries', 'created_entries', 'unchanged_entries', 'recreated_entries', 'update_time')
        DELETED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        UPDATED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        CREATED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        UNCHANGED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        RECREATED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        deleted_entries: int
        updated_entries: int
        created_entries: int
        unchanged_entries: int
        recreated_entries: int
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, deleted_entries: _Optional[int]=..., updated_entries: _Optional[int]=..., created_entries: _Optional[int]=..., unchanged_entries: _Optional[int]=..., recreated_entries: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class ImportJobSpec(_message.Message):
        __slots__ = ('source_storage_uri', 'source_create_time', 'scope', 'entry_sync_mode', 'aspect_sync_mode', 'log_level')

        class SyncMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SYNC_MODE_UNSPECIFIED: _ClassVar[MetadataJob.ImportJobSpec.SyncMode]
            FULL: _ClassVar[MetadataJob.ImportJobSpec.SyncMode]
            INCREMENTAL: _ClassVar[MetadataJob.ImportJobSpec.SyncMode]
        SYNC_MODE_UNSPECIFIED: MetadataJob.ImportJobSpec.SyncMode
        FULL: MetadataJob.ImportJobSpec.SyncMode
        INCREMENTAL: MetadataJob.ImportJobSpec.SyncMode

        class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOG_LEVEL_UNSPECIFIED: _ClassVar[MetadataJob.ImportJobSpec.LogLevel]
            DEBUG: _ClassVar[MetadataJob.ImportJobSpec.LogLevel]
            INFO: _ClassVar[MetadataJob.ImportJobSpec.LogLevel]
        LOG_LEVEL_UNSPECIFIED: MetadataJob.ImportJobSpec.LogLevel
        DEBUG: MetadataJob.ImportJobSpec.LogLevel
        INFO: MetadataJob.ImportJobSpec.LogLevel

        class ImportJobScope(_message.Message):
            __slots__ = ('entry_groups', 'entry_types', 'aspect_types')
            ENTRY_GROUPS_FIELD_NUMBER: _ClassVar[int]
            ENTRY_TYPES_FIELD_NUMBER: _ClassVar[int]
            ASPECT_TYPES_FIELD_NUMBER: _ClassVar[int]
            entry_groups: _containers.RepeatedScalarFieldContainer[str]
            entry_types: _containers.RepeatedScalarFieldContainer[str]
            aspect_types: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, entry_groups: _Optional[_Iterable[str]]=..., entry_types: _Optional[_Iterable[str]]=..., aspect_types: _Optional[_Iterable[str]]=...) -> None:
                ...
        SOURCE_STORAGE_URI_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        ENTRY_SYNC_MODE_FIELD_NUMBER: _ClassVar[int]
        ASPECT_SYNC_MODE_FIELD_NUMBER: _ClassVar[int]
        LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
        source_storage_uri: str
        source_create_time: _timestamp_pb2.Timestamp
        scope: MetadataJob.ImportJobSpec.ImportJobScope
        entry_sync_mode: MetadataJob.ImportJobSpec.SyncMode
        aspect_sync_mode: MetadataJob.ImportJobSpec.SyncMode
        log_level: MetadataJob.ImportJobSpec.LogLevel

        def __init__(self, source_storage_uri: _Optional[str]=..., source_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., scope: _Optional[_Union[MetadataJob.ImportJobSpec.ImportJobScope, _Mapping]]=..., entry_sync_mode: _Optional[_Union[MetadataJob.ImportJobSpec.SyncMode, str]]=..., aspect_sync_mode: _Optional[_Union[MetadataJob.ImportJobSpec.SyncMode, str]]=..., log_level: _Optional[_Union[MetadataJob.ImportJobSpec.LogLevel, str]]=...) -> None:
            ...

    class Status(_message.Message):
        __slots__ = ('state', 'message', 'completion_percent', 'update_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[MetadataJob.Status.State]
            QUEUED: _ClassVar[MetadataJob.Status.State]
            RUNNING: _ClassVar[MetadataJob.Status.State]
            CANCELING: _ClassVar[MetadataJob.Status.State]
            CANCELED: _ClassVar[MetadataJob.Status.State]
            SUCCEEDED: _ClassVar[MetadataJob.Status.State]
            FAILED: _ClassVar[MetadataJob.Status.State]
            SUCCEEDED_WITH_ERRORS: _ClassVar[MetadataJob.Status.State]
        STATE_UNSPECIFIED: MetadataJob.Status.State
        QUEUED: MetadataJob.Status.State
        RUNNING: MetadataJob.Status.State
        CANCELING: MetadataJob.Status.State
        CANCELED: MetadataJob.Status.State
        SUCCEEDED: MetadataJob.Status.State
        FAILED: MetadataJob.Status.State
        SUCCEEDED_WITH_ERRORS: MetadataJob.Status.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_PERCENT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        state: MetadataJob.Status.State
        message: str
        completion_percent: int
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[MetadataJob.Status.State, str]]=..., message: _Optional[str]=..., completion_percent: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SPEC_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RESULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    type: MetadataJob.Type
    import_spec: MetadataJob.ImportJobSpec
    import_result: MetadataJob.ImportJobResult
    status: MetadataJob.Status

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., type: _Optional[_Union[MetadataJob.Type, str]]=..., import_spec: _Optional[_Union[MetadataJob.ImportJobSpec, _Mapping]]=..., import_result: _Optional[_Union[MetadataJob.ImportJobResult, _Mapping]]=..., status: _Optional[_Union[MetadataJob.Status, _Mapping]]=...) -> None:
        ...