from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.drive.labels.v2beta import common_pb2 as _common_pb2
from google.apps.drive.labels.v2beta import field_pb2 as _field_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Label(_message.Message):
    __slots__ = ('name', 'id', 'revision_id', 'label_type', 'creator', 'create_time', 'revision_creator', 'revision_create_time', 'publisher', 'publish_time', 'disabler', 'disable_time', 'customer', 'properties', 'lifecycle', 'display_hints', 'applied_capabilities', 'schema_capabilities', 'applied_label_policy', 'fields', 'learn_more_uri', 'lock_status')

    class LabelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LABEL_TYPE_UNSPECIFIED: _ClassVar[Label.LabelType]
        SHARED: _ClassVar[Label.LabelType]
        ADMIN: _ClassVar[Label.LabelType]
        GOOGLE_APP: _ClassVar[Label.LabelType]
    LABEL_TYPE_UNSPECIFIED: Label.LabelType
    SHARED: Label.LabelType
    ADMIN: Label.LabelType
    GOOGLE_APP: Label.LabelType

    class Properties(_message.Message):
        __slots__ = ('title', 'description')
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str

        def __init__(self, title: _Optional[str]=..., description: _Optional[str]=...) -> None:
            ...

    class DisplayHints(_message.Message):
        __slots__ = ('disabled', 'hidden_in_search', 'shown_in_apply', 'priority')
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        SHOWN_IN_APPLY_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        disabled: bool
        hidden_in_search: bool
        shown_in_apply: bool
        priority: int

        def __init__(self, disabled: bool=..., hidden_in_search: bool=..., shown_in_apply: bool=..., priority: _Optional[int]=...) -> None:
            ...

    class AppliedCapabilities(_message.Message):
        __slots__ = ('can_read', 'can_apply', 'can_remove')
        CAN_READ_FIELD_NUMBER: _ClassVar[int]
        CAN_APPLY_FIELD_NUMBER: _ClassVar[int]
        CAN_REMOVE_FIELD_NUMBER: _ClassVar[int]
        can_read: bool
        can_apply: bool
        can_remove: bool

        def __init__(self, can_read: bool=..., can_apply: bool=..., can_remove: bool=...) -> None:
            ...

    class SchemaCapabilities(_message.Message):
        __slots__ = ('can_update', 'can_delete', 'can_disable', 'can_enable')
        CAN_UPDATE_FIELD_NUMBER: _ClassVar[int]
        CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
        CAN_DISABLE_FIELD_NUMBER: _ClassVar[int]
        CAN_ENABLE_FIELD_NUMBER: _ClassVar[int]
        can_update: bool
        can_delete: bool
        can_disable: bool
        can_enable: bool

        def __init__(self, can_update: bool=..., can_delete: bool=..., can_disable: bool=..., can_enable: bool=...) -> None:
            ...

    class AppliedLabelPolicy(_message.Message):
        __slots__ = ('copy_mode',)

        class CopyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COPY_MODE_UNSPECIFIED: _ClassVar[Label.AppliedLabelPolicy.CopyMode]
            DO_NOT_COPY: _ClassVar[Label.AppliedLabelPolicy.CopyMode]
            ALWAYS_COPY: _ClassVar[Label.AppliedLabelPolicy.CopyMode]
            COPY_APPLIABLE: _ClassVar[Label.AppliedLabelPolicy.CopyMode]
        COPY_MODE_UNSPECIFIED: Label.AppliedLabelPolicy.CopyMode
        DO_NOT_COPY: Label.AppliedLabelPolicy.CopyMode
        ALWAYS_COPY: Label.AppliedLabelPolicy.CopyMode
        COPY_APPLIABLE: Label.AppliedLabelPolicy.CopyMode
        COPY_MODE_FIELD_NUMBER: _ClassVar[int]
        copy_mode: Label.AppliedLabelPolicy.CopyMode

        def __init__(self, copy_mode: _Optional[_Union[Label.AppliedLabelPolicy.CopyMode, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATOR_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    DISABLER_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TIME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_HINTS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABEL_POLICY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    LEARN_MORE_URI_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    revision_id: str
    label_type: Label.LabelType
    creator: _common_pb2.UserInfo
    create_time: _timestamp_pb2.Timestamp
    revision_creator: _common_pb2.UserInfo
    revision_create_time: _timestamp_pb2.Timestamp
    publisher: _common_pb2.UserInfo
    publish_time: _timestamp_pb2.Timestamp
    disabler: _common_pb2.UserInfo
    disable_time: _timestamp_pb2.Timestamp
    customer: str
    properties: Label.Properties
    lifecycle: _common_pb2.Lifecycle
    display_hints: Label.DisplayHints
    applied_capabilities: Label.AppliedCapabilities
    schema_capabilities: Label.SchemaCapabilities
    applied_label_policy: Label.AppliedLabelPolicy
    fields: _containers.RepeatedCompositeFieldContainer[_field_pb2.Field]
    learn_more_uri: str
    lock_status: _common_pb2.LockStatus

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., revision_id: _Optional[str]=..., label_type: _Optional[_Union[Label.LabelType, str]]=..., creator: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., revision_creator: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., publisher: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disabler: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., disable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., customer: _Optional[str]=..., properties: _Optional[_Union[Label.Properties, _Mapping]]=..., lifecycle: _Optional[_Union[_common_pb2.Lifecycle, _Mapping]]=..., display_hints: _Optional[_Union[Label.DisplayHints, _Mapping]]=..., applied_capabilities: _Optional[_Union[Label.AppliedCapabilities, _Mapping]]=..., schema_capabilities: _Optional[_Union[Label.SchemaCapabilities, _Mapping]]=..., applied_label_policy: _Optional[_Union[Label.AppliedLabelPolicy, _Mapping]]=..., fields: _Optional[_Iterable[_Union[_field_pb2.Field, _Mapping]]]=..., learn_more_uri: _Optional[str]=..., lock_status: _Optional[_Union[_common_pb2.LockStatus, _Mapping]]=...) -> None:
        ...