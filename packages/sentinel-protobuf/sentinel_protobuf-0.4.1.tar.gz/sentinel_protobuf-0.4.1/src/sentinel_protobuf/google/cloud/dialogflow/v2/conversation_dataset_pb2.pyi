from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2 import gcs_pb2 as _gcs_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationInfo(_message.Message):
    __slots__ = ("language_code",)
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    def __init__(self, language_code: _Optional[str] = ...) -> None: ...

class InputConfig(_message.Message):
    __slots__ = ("gcs_source",)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _gcs_pb2.GcsSources
    def __init__(self, gcs_source: _Optional[_Union[_gcs_pb2.GcsSources, _Mapping]] = ...) -> None: ...

class ConversationDataset(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "input_config", "conversation_info", "conversation_count", "satisfies_pzi", "satisfies_pzs")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    input_config: InputConfig
    conversation_info: ConversationInfo
    conversation_count: int
    satisfies_pzi: bool
    satisfies_pzs: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., input_config: _Optional[_Union[InputConfig, _Mapping]] = ..., conversation_info: _Optional[_Union[ConversationInfo, _Mapping]] = ..., conversation_count: _Optional[int] = ..., satisfies_pzi: bool = ..., satisfies_pzs: bool = ...) -> None: ...

class CreateConversationDatasetRequest(_message.Message):
    __slots__ = ("parent", "conversation_dataset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation_dataset: ConversationDataset
    def __init__(self, parent: _Optional[str] = ..., conversation_dataset: _Optional[_Union[ConversationDataset, _Mapping]] = ...) -> None: ...

class GetConversationDatasetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConversationDatasetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListConversationDatasetsResponse(_message.Message):
    __slots__ = ("conversation_datasets", "next_page_token")
    CONVERSATION_DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversation_datasets: _containers.RepeatedCompositeFieldContainer[ConversationDataset]
    next_page_token: str
    def __init__(self, conversation_datasets: _Optional[_Iterable[_Union[ConversationDataset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteConversationDatasetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ImportConversationDataRequest(_message.Message):
    __slots__ = ("name", "input_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: InputConfig
    def __init__(self, name: _Optional[str] = ..., input_config: _Optional[_Union[InputConfig, _Mapping]] = ...) -> None: ...

class ImportConversationDataOperationMetadata(_message.Message):
    __slots__ = ("conversation_dataset", "partial_failures", "create_time")
    CONVERSATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_dataset: str
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_dataset: _Optional[str] = ..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ImportConversationDataOperationResponse(_message.Message):
    __slots__ = ("conversation_dataset", "import_count")
    CONVERSATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    IMPORT_COUNT_FIELD_NUMBER: _ClassVar[int]
    conversation_dataset: str
    import_count: int
    def __init__(self, conversation_dataset: _Optional[str] = ..., import_count: _Optional[int] = ...) -> None: ...

class CreateConversationDatasetOperationMetadata(_message.Message):
    __slots__ = ("conversation_dataset",)
    CONVERSATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    conversation_dataset: str
    def __init__(self, conversation_dataset: _Optional[str] = ...) -> None: ...

class DeleteConversationDatasetOperationMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
