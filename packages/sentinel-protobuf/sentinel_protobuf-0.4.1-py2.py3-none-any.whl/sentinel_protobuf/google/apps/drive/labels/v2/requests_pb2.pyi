from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.drive.labels.v2 import common_pb2 as _common_pb2
from google.apps.drive.labels.v2 import field_pb2 as _field_pb2
from google.apps.drive.labels.v2 import label_pb2 as _label_pb2
from google.apps.drive.labels.v2 import label_lock_pb2 as _label_lock_pb2
from google.apps.drive.labels.v2 import label_permission_pb2 as _label_permission_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LabelView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LABEL_VIEW_BASIC: _ClassVar[LabelView]
    LABEL_VIEW_FULL: _ClassVar[LabelView]
LABEL_VIEW_BASIC: LabelView
LABEL_VIEW_FULL: LabelView

class WriteControl(_message.Message):
    __slots__ = ('required_revision_id',)
    REQUIRED_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    required_revision_id: str

    def __init__(self, required_revision_id: _Optional[str]=...) -> None:
        ...

class GetUserCapabilitiesRequest(_message.Message):
    __slots__ = ('name', 'customer')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    name: str
    customer: str

    def __init__(self, name: _Optional[str]=..., customer: _Optional[str]=...) -> None:
        ...

class CreateLabelRequest(_message.Message):
    __slots__ = ('label', 'use_admin_access', 'language_code')
    LABEL_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    label: _label_pb2.Label
    use_admin_access: bool
    language_code: str

    def __init__(self, label: _Optional[_Union[_label_pb2.Label, _Mapping]]=..., use_admin_access: bool=..., language_code: _Optional[str]=...) -> None:
        ...

class GetLabelRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access', 'language_code', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    language_code: str
    view: LabelView

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=..., language_code: _Optional[str]=..., view: _Optional[_Union[LabelView, str]]=...) -> None:
        ...

class DeltaUpdateLabelRequest(_message.Message):
    __slots__ = ('name', 'write_control', 'requests', 'use_admin_access', 'view', 'language_code')

    class Request(_message.Message):
        __slots__ = ('update_label', 'create_field', 'update_field', 'update_field_type', 'enable_field', 'disable_field', 'delete_field', 'create_selection_choice', 'update_selection_choice_properties', 'enable_selection_choice', 'disable_selection_choice', 'delete_selection_choice')
        UPDATE_LABEL_FIELD_NUMBER: _ClassVar[int]
        CREATE_FIELD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_FIELD_NUMBER: _ClassVar[int]
        DISABLE_FIELD_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_FIELD_NUMBER: _ClassVar[int]
        CREATE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_SELECTION_CHOICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        DISABLE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        DELETE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        update_label: DeltaUpdateLabelRequest.UpdateLabelPropertiesRequest
        create_field: DeltaUpdateLabelRequest.CreateFieldRequest
        update_field: DeltaUpdateLabelRequest.UpdateFieldPropertiesRequest
        update_field_type: DeltaUpdateLabelRequest.UpdateFieldTypeRequest
        enable_field: DeltaUpdateLabelRequest.EnableFieldRequest
        disable_field: DeltaUpdateLabelRequest.DisableFieldRequest
        delete_field: DeltaUpdateLabelRequest.DeleteFieldRequest
        create_selection_choice: DeltaUpdateLabelRequest.CreateSelectionChoiceRequest
        update_selection_choice_properties: DeltaUpdateLabelRequest.UpdateSelectionChoicePropertiesRequest
        enable_selection_choice: DeltaUpdateLabelRequest.EnableSelectionChoiceRequest
        disable_selection_choice: DeltaUpdateLabelRequest.DisableSelectionChoiceRequest
        delete_selection_choice: DeltaUpdateLabelRequest.DeleteSelectionChoiceRequest

        def __init__(self, update_label: _Optional[_Union[DeltaUpdateLabelRequest.UpdateLabelPropertiesRequest, _Mapping]]=..., create_field: _Optional[_Union[DeltaUpdateLabelRequest.CreateFieldRequest, _Mapping]]=..., update_field: _Optional[_Union[DeltaUpdateLabelRequest.UpdateFieldPropertiesRequest, _Mapping]]=..., update_field_type: _Optional[_Union[DeltaUpdateLabelRequest.UpdateFieldTypeRequest, _Mapping]]=..., enable_field: _Optional[_Union[DeltaUpdateLabelRequest.EnableFieldRequest, _Mapping]]=..., disable_field: _Optional[_Union[DeltaUpdateLabelRequest.DisableFieldRequest, _Mapping]]=..., delete_field: _Optional[_Union[DeltaUpdateLabelRequest.DeleteFieldRequest, _Mapping]]=..., create_selection_choice: _Optional[_Union[DeltaUpdateLabelRequest.CreateSelectionChoiceRequest, _Mapping]]=..., update_selection_choice_properties: _Optional[_Union[DeltaUpdateLabelRequest.UpdateSelectionChoicePropertiesRequest, _Mapping]]=..., enable_selection_choice: _Optional[_Union[DeltaUpdateLabelRequest.EnableSelectionChoiceRequest, _Mapping]]=..., disable_selection_choice: _Optional[_Union[DeltaUpdateLabelRequest.DisableSelectionChoiceRequest, _Mapping]]=..., delete_selection_choice: _Optional[_Union[DeltaUpdateLabelRequest.DeleteSelectionChoiceRequest, _Mapping]]=...) -> None:
            ...

    class UpdateLabelPropertiesRequest(_message.Message):
        __slots__ = ('update_mask', 'properties')
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        properties: _label_pb2.Label.Properties

        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., properties: _Optional[_Union[_label_pb2.Label.Properties, _Mapping]]=...) -> None:
            ...

    class DisableFieldRequest(_message.Message):
        __slots__ = ('update_mask', 'id', 'disabled_policy')
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        DISABLED_POLICY_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        id: str
        disabled_policy: _common_pb2.Lifecycle.DisabledPolicy

        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., id: _Optional[str]=..., disabled_policy: _Optional[_Union[_common_pb2.Lifecycle.DisabledPolicy, _Mapping]]=...) -> None:
            ...

    class EnableFieldRequest(_message.Message):
        __slots__ = ('id',)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str

        def __init__(self, id: _Optional[str]=...) -> None:
            ...

    class DeleteFieldRequest(_message.Message):
        __slots__ = ('id',)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str

        def __init__(self, id: _Optional[str]=...) -> None:
            ...

    class CreateFieldRequest(_message.Message):
        __slots__ = ('field',)
        FIELD_FIELD_NUMBER: _ClassVar[int]
        field: _field_pb2.Field

        def __init__(self, field: _Optional[_Union[_field_pb2.Field, _Mapping]]=...) -> None:
            ...

    class UpdateFieldPropertiesRequest(_message.Message):
        __slots__ = ('update_mask', 'id', 'properties')
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        id: str
        properties: _field_pb2.Field.Properties

        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., id: _Optional[str]=..., properties: _Optional[_Union[_field_pb2.Field.Properties, _Mapping]]=...) -> None:
            ...

    class UpdateFieldTypeRequest(_message.Message):
        __slots__ = ('text_options', 'integer_options', 'date_options', 'selection_options', 'user_options', 'update_mask', 'id')
        TEXT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        INTEGER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        DATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SELECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        USER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        text_options: _field_pb2.Field.TextOptions
        integer_options: _field_pb2.Field.IntegerOptions
        date_options: _field_pb2.Field.DateOptions
        selection_options: _field_pb2.Field.SelectionOptions
        user_options: _field_pb2.Field.UserOptions
        update_mask: _field_mask_pb2.FieldMask
        id: str

        def __init__(self, text_options: _Optional[_Union[_field_pb2.Field.TextOptions, _Mapping]]=..., integer_options: _Optional[_Union[_field_pb2.Field.IntegerOptions, _Mapping]]=..., date_options: _Optional[_Union[_field_pb2.Field.DateOptions, _Mapping]]=..., selection_options: _Optional[_Union[_field_pb2.Field.SelectionOptions, _Mapping]]=..., user_options: _Optional[_Union[_field_pb2.Field.UserOptions, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., id: _Optional[str]=...) -> None:
            ...

    class CreateSelectionChoiceRequest(_message.Message):
        __slots__ = ('field_id', 'choice')
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        field_id: str
        choice: _field_pb2.Field.SelectionOptions.Choice

        def __init__(self, field_id: _Optional[str]=..., choice: _Optional[_Union[_field_pb2.Field.SelectionOptions.Choice, _Mapping]]=...) -> None:
            ...

    class UpdateSelectionChoicePropertiesRequest(_message.Message):
        __slots__ = ('update_mask', 'field_id', 'id', 'properties')
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        field_id: str
        id: str
        properties: _field_pb2.Field.SelectionOptions.Choice.Properties

        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., field_id: _Optional[str]=..., id: _Optional[str]=..., properties: _Optional[_Union[_field_pb2.Field.SelectionOptions.Choice.Properties, _Mapping]]=...) -> None:
            ...

    class DeleteSelectionChoiceRequest(_message.Message):
        __slots__ = ('field_id', 'id')
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        field_id: str
        id: str

        def __init__(self, field_id: _Optional[str]=..., id: _Optional[str]=...) -> None:
            ...

    class DisableSelectionChoiceRequest(_message.Message):
        __slots__ = ('update_mask', 'field_id', 'id', 'disabled_policy')
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        DISABLED_POLICY_FIELD_NUMBER: _ClassVar[int]
        update_mask: _field_mask_pb2.FieldMask
        field_id: str
        id: str
        disabled_policy: _common_pb2.Lifecycle.DisabledPolicy

        def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., field_id: _Optional[str]=..., id: _Optional[str]=..., disabled_policy: _Optional[_Union[_common_pb2.Lifecycle.DisabledPolicy, _Mapping]]=...) -> None:
            ...

    class EnableSelectionChoiceRequest(_message.Message):
        __slots__ = ('field_id', 'id')
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        field_id: str
        id: str

        def __init__(self, field_id: _Optional[str]=..., id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    write_control: WriteControl
    requests: _containers.RepeatedCompositeFieldContainer[DeltaUpdateLabelRequest.Request]
    use_admin_access: bool
    view: LabelView
    language_code: str

    def __init__(self, name: _Optional[str]=..., write_control: _Optional[_Union[WriteControl, _Mapping]]=..., requests: _Optional[_Iterable[_Union[DeltaUpdateLabelRequest.Request, _Mapping]]]=..., use_admin_access: bool=..., view: _Optional[_Union[LabelView, str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class DeltaUpdateLabelResponse(_message.Message):
    __slots__ = ('responses', 'updated_label')

    class Response(_message.Message):
        __slots__ = ('update_label', 'create_field', 'update_field', 'update_field_type', 'enable_field', 'disable_field', 'delete_field', 'create_selection_choice', 'update_selection_choice_properties', 'enable_selection_choice', 'disable_selection_choice', 'delete_selection_choice')
        UPDATE_LABEL_FIELD_NUMBER: _ClassVar[int]
        CREATE_FIELD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_FIELD_NUMBER: _ClassVar[int]
        DISABLE_FIELD_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_FIELD_NUMBER: _ClassVar[int]
        CREATE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_SELECTION_CHOICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        DISABLE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        DELETE_SELECTION_CHOICE_FIELD_NUMBER: _ClassVar[int]
        update_label: DeltaUpdateLabelResponse.UpdateLabelPropertiesResponse
        create_field: DeltaUpdateLabelResponse.CreateFieldResponse
        update_field: DeltaUpdateLabelResponse.UpdateFieldPropertiesResponse
        update_field_type: DeltaUpdateLabelResponse.UpdateFieldTypeResponse
        enable_field: DeltaUpdateLabelResponse.EnableFieldResponse
        disable_field: DeltaUpdateLabelResponse.DisableFieldResponse
        delete_field: DeltaUpdateLabelResponse.DeleteFieldResponse
        create_selection_choice: DeltaUpdateLabelResponse.CreateSelectionChoiceResponse
        update_selection_choice_properties: DeltaUpdateLabelResponse.UpdateSelectionChoicePropertiesResponse
        enable_selection_choice: DeltaUpdateLabelResponse.EnableSelectionChoiceResponse
        disable_selection_choice: DeltaUpdateLabelResponse.DisableSelectionChoiceResponse
        delete_selection_choice: DeltaUpdateLabelResponse.DeleteSelectionChoiceResponse

        def __init__(self, update_label: _Optional[_Union[DeltaUpdateLabelResponse.UpdateLabelPropertiesResponse, _Mapping]]=..., create_field: _Optional[_Union[DeltaUpdateLabelResponse.CreateFieldResponse, _Mapping]]=..., update_field: _Optional[_Union[DeltaUpdateLabelResponse.UpdateFieldPropertiesResponse, _Mapping]]=..., update_field_type: _Optional[_Union[DeltaUpdateLabelResponse.UpdateFieldTypeResponse, _Mapping]]=..., enable_field: _Optional[_Union[DeltaUpdateLabelResponse.EnableFieldResponse, _Mapping]]=..., disable_field: _Optional[_Union[DeltaUpdateLabelResponse.DisableFieldResponse, _Mapping]]=..., delete_field: _Optional[_Union[DeltaUpdateLabelResponse.DeleteFieldResponse, _Mapping]]=..., create_selection_choice: _Optional[_Union[DeltaUpdateLabelResponse.CreateSelectionChoiceResponse, _Mapping]]=..., update_selection_choice_properties: _Optional[_Union[DeltaUpdateLabelResponse.UpdateSelectionChoicePropertiesResponse, _Mapping]]=..., enable_selection_choice: _Optional[_Union[DeltaUpdateLabelResponse.EnableSelectionChoiceResponse, _Mapping]]=..., disable_selection_choice: _Optional[_Union[DeltaUpdateLabelResponse.DisableSelectionChoiceResponse, _Mapping]]=..., delete_selection_choice: _Optional[_Union[DeltaUpdateLabelResponse.DeleteSelectionChoiceResponse, _Mapping]]=...) -> None:
            ...

    class UpdateLabelPropertiesResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class CreateFieldResponse(_message.Message):
        __slots__ = ('id', 'priority')
        ID_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        priority: int

        def __init__(self, id: _Optional[str]=..., priority: _Optional[int]=...) -> None:
            ...

    class UpdateFieldPropertiesResponse(_message.Message):
        __slots__ = ('priority',)
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        priority: int

        def __init__(self, priority: _Optional[int]=...) -> None:
            ...

    class UpdateFieldTypeResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class EnableFieldResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DisableFieldResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DeleteFieldResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class CreateSelectionChoiceResponse(_message.Message):
        __slots__ = ('field_id', 'id')
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        field_id: str
        id: str

        def __init__(self, field_id: _Optional[str]=..., id: _Optional[str]=...) -> None:
            ...

    class UpdateSelectionChoicePropertiesResponse(_message.Message):
        __slots__ = ('priority',)
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        priority: int

        def __init__(self, priority: _Optional[int]=...) -> None:
            ...

    class EnableSelectionChoiceResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DisableSelectionChoiceResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DeleteSelectionChoiceResponse(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_LABEL_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[DeltaUpdateLabelResponse.Response]
    updated_label: _label_pb2.Label

    def __init__(self, responses: _Optional[_Iterable[_Union[DeltaUpdateLabelResponse.Response, _Mapping]]]=..., updated_label: _Optional[_Union[_label_pb2.Label, _Mapping]]=...) -> None:
        ...

class UpdateLabelCopyModeRequest(_message.Message):
    __slots__ = ('name', 'copy_mode', 'use_admin_access', 'language_code', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    copy_mode: _label_pb2.Label.AppliedLabelPolicy.CopyMode
    use_admin_access: bool
    language_code: str
    view: LabelView

    def __init__(self, name: _Optional[str]=..., copy_mode: _Optional[_Union[_label_pb2.Label.AppliedLabelPolicy.CopyMode, str]]=..., use_admin_access: bool=..., language_code: _Optional[str]=..., view: _Optional[_Union[LabelView, str]]=...) -> None:
        ...

class GetLabelLimitsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLabelsRequest(_message.Message):
    __slots__ = ('use_admin_access', 'minimum_role', 'published_only', 'customer', 'language_code', 'page_size', 'page_token', 'view')
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ROLE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_ONLY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    use_admin_access: bool
    minimum_role: _label_permission_pb2.LabelPermission.LabelRole
    published_only: bool
    customer: str
    language_code: str
    page_size: int
    page_token: str
    view: LabelView

    def __init__(self, use_admin_access: bool=..., minimum_role: _Optional[_Union[_label_permission_pb2.LabelPermission.LabelRole, str]]=..., published_only: bool=..., customer: _Optional[str]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[LabelView, str]]=...) -> None:
        ...

class ListLabelsResponse(_message.Message):
    __slots__ = ('labels', 'next_page_token')
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[_label_pb2.Label]
    next_page_token: str

    def __init__(self, labels: _Optional[_Iterable[_Union[_label_pb2.Label, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateLabelPermissionRequest(_message.Message):
    __slots__ = ('parent', 'label_permission', 'use_admin_access')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    label_permission: _label_permission_pb2.LabelPermission
    use_admin_access: bool

    def __init__(self, parent: _Optional[str]=..., label_permission: _Optional[_Union[_label_permission_pb2.LabelPermission, _Mapping]]=..., use_admin_access: bool=...) -> None:
        ...

class ListLabelPermissionsRequest(_message.Message):
    __slots__ = ('parent', 'use_admin_access', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    use_admin_access: bool
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., use_admin_access: bool=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLabelPermissionsResponse(_message.Message):
    __slots__ = ('label_permissions', 'next_page_token')
    LABEL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    label_permissions: _containers.RepeatedCompositeFieldContainer[_label_permission_pb2.LabelPermission]
    next_page_token: str

    def __init__(self, label_permissions: _Optional[_Iterable[_Union[_label_permission_pb2.LabelPermission, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateLabelPermissionRequest(_message.Message):
    __slots__ = ('parent', 'label_permission', 'use_admin_access')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    label_permission: _label_permission_pb2.LabelPermission
    use_admin_access: bool

    def __init__(self, parent: _Optional[str]=..., label_permission: _Optional[_Union[_label_permission_pb2.LabelPermission, _Mapping]]=..., use_admin_access: bool=...) -> None:
        ...

class DeleteLabelPermissionRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=...) -> None:
        ...

class BatchUpdateLabelPermissionsRequest(_message.Message):
    __slots__ = ('parent', 'requests', 'use_admin_access')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateLabelPermissionRequest]
    use_admin_access: bool

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateLabelPermissionRequest, _Mapping]]]=..., use_admin_access: bool=...) -> None:
        ...

class BatchUpdateLabelPermissionsResponse(_message.Message):
    __slots__ = ('permissions',)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_label_permission_pb2.LabelPermission]

    def __init__(self, permissions: _Optional[_Iterable[_Union[_label_permission_pb2.LabelPermission, _Mapping]]]=...) -> None:
        ...

class BatchDeleteLabelPermissionsRequest(_message.Message):
    __slots__ = ('requests', 'use_admin_access', 'parent')
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[DeleteLabelPermissionRequest]
    use_admin_access: bool
    parent: str

    def __init__(self, requests: _Optional[_Iterable[_Union[DeleteLabelPermissionRequest, _Mapping]]]=..., use_admin_access: bool=..., parent: _Optional[str]=...) -> None:
        ...

class DisableLabelRequest(_message.Message):
    __slots__ = ('update_mask', 'name', 'use_admin_access', 'write_control', 'disabled_policy', 'language_code')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_POLICY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    name: str
    use_admin_access: bool
    write_control: WriteControl
    disabled_policy: _common_pb2.Lifecycle.DisabledPolicy
    language_code: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., name: _Optional[str]=..., use_admin_access: bool=..., write_control: _Optional[_Union[WriteControl, _Mapping]]=..., disabled_policy: _Optional[_Union[_common_pb2.Lifecycle.DisabledPolicy, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class PublishLabelRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access', 'write_control', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    write_control: WriteControl
    language_code: str

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=..., write_control: _Optional[_Union[WriteControl, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class EnableLabelRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access', 'write_control', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    write_control: WriteControl
    language_code: str

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=..., write_control: _Optional[_Union[WriteControl, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class DeleteLabelRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access', 'write_control')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool
    write_control: WriteControl

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=..., write_control: _Optional[_Union[WriteControl, _Mapping]]=...) -> None:
        ...

class ListLabelLocksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLabelLocksResponse(_message.Message):
    __slots__ = ('label_locks', 'next_page_token')
    LABEL_LOCKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    label_locks: _containers.RepeatedCompositeFieldContainer[_label_lock_pb2.LabelLock]
    next_page_token: str

    def __init__(self, label_locks: _Optional[_Iterable[_Union[_label_lock_pb2.LabelLock, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...