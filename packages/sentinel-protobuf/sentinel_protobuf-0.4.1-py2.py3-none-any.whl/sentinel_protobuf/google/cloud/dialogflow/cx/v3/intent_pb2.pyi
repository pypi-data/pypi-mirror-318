from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import inline_pb2 as _inline_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IntentView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTENT_VIEW_UNSPECIFIED: _ClassVar[IntentView]
    INTENT_VIEW_PARTIAL: _ClassVar[IntentView]
    INTENT_VIEW_FULL: _ClassVar[IntentView]
INTENT_VIEW_UNSPECIFIED: IntentView
INTENT_VIEW_PARTIAL: IntentView
INTENT_VIEW_FULL: IntentView

class Intent(_message.Message):
    __slots__ = ('name', 'display_name', 'training_phrases', 'parameters', 'priority', 'is_fallback', 'labels', 'description')

    class TrainingPhrase(_message.Message):
        __slots__ = ('id', 'parts', 'repeat_count')

        class Part(_message.Message):
            __slots__ = ('text', 'parameter_id')
            TEXT_FIELD_NUMBER: _ClassVar[int]
            PARAMETER_ID_FIELD_NUMBER: _ClassVar[int]
            text: str
            parameter_id: str

            def __init__(self, text: _Optional[str]=..., parameter_id: _Optional[str]=...) -> None:
                ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PARTS_FIELD_NUMBER: _ClassVar[int]
        REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        parts: _containers.RepeatedCompositeFieldContainer[Intent.TrainingPhrase.Part]
        repeat_count: int

        def __init__(self, id: _Optional[str]=..., parts: _Optional[_Iterable[_Union[Intent.TrainingPhrase.Part, _Mapping]]]=..., repeat_count: _Optional[int]=...) -> None:
            ...

    class Parameter(_message.Message):
        __slots__ = ('id', 'entity_type', 'is_list', 'redact')
        ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_LIST_FIELD_NUMBER: _ClassVar[int]
        REDACT_FIELD_NUMBER: _ClassVar[int]
        id: str
        entity_type: str
        is_list: bool
        redact: bool

        def __init__(self, id: _Optional[str]=..., entity_type: _Optional[str]=..., is_list: bool=..., redact: bool=...) -> None:
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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PHRASES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IS_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    training_phrases: _containers.RepeatedCompositeFieldContainer[Intent.TrainingPhrase]
    parameters: _containers.RepeatedCompositeFieldContainer[Intent.Parameter]
    priority: int
    is_fallback: bool
    labels: _containers.ScalarMap[str, str]
    description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., training_phrases: _Optional[_Iterable[_Union[Intent.TrainingPhrase, _Mapping]]]=..., parameters: _Optional[_Iterable[_Union[Intent.Parameter, _Mapping]]]=..., priority: _Optional[int]=..., is_fallback: bool=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
        ...

class ListIntentsRequest(_message.Message):
    __slots__ = ('parent', 'language_code', 'intent_view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str
    intent_view: IntentView
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., language_code: _Optional[str]=..., intent_view: _Optional[_Union[IntentView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIntentsResponse(_message.Message):
    __slots__ = ('intents', 'next_page_token')
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[Intent]
    next_page_token: str

    def __init__(self, intents: _Optional[_Iterable[_Union[Intent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetIntentRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class CreateIntentRequest(_message.Message):
    __slots__ = ('parent', 'intent', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intent: Intent
    language_code: str

    def __init__(self, parent: _Optional[str]=..., intent: _Optional[_Union[Intent, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class UpdateIntentRequest(_message.Message):
    __slots__ = ('intent', 'language_code', 'update_mask')
    INTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    intent: Intent
    language_code: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, intent: _Optional[_Union[Intent, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteIntentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportIntentsRequest(_message.Message):
    __slots__ = ('parent', 'intents_uri', 'intents_content', 'merge_option')

    class MergeOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MERGE_OPTION_UNSPECIFIED: _ClassVar[ImportIntentsRequest.MergeOption]
        REJECT: _ClassVar[ImportIntentsRequest.MergeOption]
        REPLACE: _ClassVar[ImportIntentsRequest.MergeOption]
        MERGE: _ClassVar[ImportIntentsRequest.MergeOption]
        RENAME: _ClassVar[ImportIntentsRequest.MergeOption]
        REPORT_CONFLICT: _ClassVar[ImportIntentsRequest.MergeOption]
        KEEP: _ClassVar[ImportIntentsRequest.MergeOption]
    MERGE_OPTION_UNSPECIFIED: ImportIntentsRequest.MergeOption
    REJECT: ImportIntentsRequest.MergeOption
    REPLACE: ImportIntentsRequest.MergeOption
    MERGE: ImportIntentsRequest.MergeOption
    RENAME: ImportIntentsRequest.MergeOption
    REPORT_CONFLICT: ImportIntentsRequest.MergeOption
    KEEP: ImportIntentsRequest.MergeOption
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENTS_URI_FIELD_NUMBER: _ClassVar[int]
    INTENTS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    MERGE_OPTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intents_uri: str
    intents_content: _inline_pb2.InlineSource
    merge_option: ImportIntentsRequest.MergeOption

    def __init__(self, parent: _Optional[str]=..., intents_uri: _Optional[str]=..., intents_content: _Optional[_Union[_inline_pb2.InlineSource, _Mapping]]=..., merge_option: _Optional[_Union[ImportIntentsRequest.MergeOption, str]]=...) -> None:
        ...

class ImportIntentsResponse(_message.Message):
    __slots__ = ('intents', 'conflicting_resources')

    class ConflictingResources(_message.Message):
        __slots__ = ('intent_display_names', 'entity_display_names')
        INTENT_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
        ENTITY_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
        intent_display_names: _containers.RepeatedScalarFieldContainer[str]
        entity_display_names: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, intent_display_names: _Optional[_Iterable[str]]=..., entity_display_names: _Optional[_Iterable[str]]=...) -> None:
            ...
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    CONFLICTING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedScalarFieldContainer[str]
    conflicting_resources: ImportIntentsResponse.ConflictingResources

    def __init__(self, intents: _Optional[_Iterable[str]]=..., conflicting_resources: _Optional[_Union[ImportIntentsResponse.ConflictingResources, _Mapping]]=...) -> None:
        ...

class ImportIntentsMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExportIntentsRequest(_message.Message):
    __slots__ = ('parent', 'intents', 'intents_uri', 'intents_content_inline', 'data_format')

    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExportIntentsRequest.DataFormat]
        BLOB: _ClassVar[ExportIntentsRequest.DataFormat]
        JSON: _ClassVar[ExportIntentsRequest.DataFormat]
        CSV: _ClassVar[ExportIntentsRequest.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExportIntentsRequest.DataFormat
    BLOB: ExportIntentsRequest.DataFormat
    JSON: ExportIntentsRequest.DataFormat
    CSV: ExportIntentsRequest.DataFormat
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    INTENTS_URI_FIELD_NUMBER: _ClassVar[int]
    INTENTS_CONTENT_INLINE_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intents: _containers.RepeatedScalarFieldContainer[str]
    intents_uri: str
    intents_content_inline: bool
    data_format: ExportIntentsRequest.DataFormat

    def __init__(self, parent: _Optional[str]=..., intents: _Optional[_Iterable[str]]=..., intents_uri: _Optional[str]=..., intents_content_inline: bool=..., data_format: _Optional[_Union[ExportIntentsRequest.DataFormat, str]]=...) -> None:
        ...

class ExportIntentsResponse(_message.Message):
    __slots__ = ('intents_uri', 'intents_content')
    INTENTS_URI_FIELD_NUMBER: _ClassVar[int]
    INTENTS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    intents_uri: str
    intents_content: _inline_pb2.InlineDestination

    def __init__(self, intents_uri: _Optional[str]=..., intents_content: _Optional[_Union[_inline_pb2.InlineDestination, _Mapping]]=...) -> None:
        ...

class ExportIntentsMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...