from google.actions.sdk.v2 import account_linking_secret_pb2 as _account_linking_secret_pb2
from google.actions.sdk.v2 import files_pb2 as _files_pb2
from google.actions.sdk.v2 import release_channel_pb2 as _release_channel_pb2
from google.actions.sdk.v2 import validation_results_pb2 as _validation_results_pb2
from google.actions.sdk.v2 import version_pb2 as _version_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WriteDraftRequest(_message.Message):
    __slots__ = ('parent', 'files')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    files: _files_pb2.Files

    def __init__(self, parent: _Optional[str]=..., files: _Optional[_Union[_files_pb2.Files, _Mapping]]=...) -> None:
        ...

class Draft(_message.Message):
    __slots__ = ('name', 'validation_results')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    validation_results: _validation_results_pb2.ValidationResults

    def __init__(self, name: _Optional[str]=..., validation_results: _Optional[_Union[_validation_results_pb2.ValidationResults, _Mapping]]=...) -> None:
        ...

class WritePreviewRequest(_message.Message):
    __slots__ = ('parent', 'files', 'draft', 'submitted_version', 'preview_settings')

    class ContentFromDraft(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class ContentFromSubmittedVersion(_message.Message):
        __slots__ = ('version',)
        VERSION_FIELD_NUMBER: _ClassVar[int]
        version: str

        def __init__(self, version: _Optional[str]=...) -> None:
            ...

    class PreviewSettings(_message.Message):
        __slots__ = ('sandbox',)
        SANDBOX_FIELD_NUMBER: _ClassVar[int]
        sandbox: _wrappers_pb2.BoolValue

        def __init__(self, sandbox: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    files: _files_pb2.Files
    draft: WritePreviewRequest.ContentFromDraft
    submitted_version: WritePreviewRequest.ContentFromSubmittedVersion
    preview_settings: WritePreviewRequest.PreviewSettings

    def __init__(self, parent: _Optional[str]=..., files: _Optional[_Union[_files_pb2.Files, _Mapping]]=..., draft: _Optional[_Union[WritePreviewRequest.ContentFromDraft, _Mapping]]=..., submitted_version: _Optional[_Union[WritePreviewRequest.ContentFromSubmittedVersion, _Mapping]]=..., preview_settings: _Optional[_Union[WritePreviewRequest.PreviewSettings, _Mapping]]=...) -> None:
        ...

class Preview(_message.Message):
    __slots__ = ('name', 'validation_results', 'simulator_url')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    validation_results: _validation_results_pb2.ValidationResults
    simulator_url: str

    def __init__(self, name: _Optional[str]=..., validation_results: _Optional[_Union[_validation_results_pb2.ValidationResults, _Mapping]]=..., simulator_url: _Optional[str]=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'files', 'release_channel')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    files: _files_pb2.Files
    release_channel: str

    def __init__(self, parent: _Optional[str]=..., files: _Optional[_Union[_files_pb2.Files, _Mapping]]=..., release_channel: _Optional[str]=...) -> None:
        ...

class ReadDraftRequest(_message.Message):
    __slots__ = ('name', 'client_secret_encryption_key_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_ENCRYPTION_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    client_secret_encryption_key_version: str

    def __init__(self, name: _Optional[str]=..., client_secret_encryption_key_version: _Optional[str]=...) -> None:
        ...

class ReadDraftResponse(_message.Message):
    __slots__ = ('files',)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _files_pb2.Files

    def __init__(self, files: _Optional[_Union[_files_pb2.Files, _Mapping]]=...) -> None:
        ...

class ReadVersionRequest(_message.Message):
    __slots__ = ('name', 'client_secret_encryption_key_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_ENCRYPTION_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    client_secret_encryption_key_version: str

    def __init__(self, name: _Optional[str]=..., client_secret_encryption_key_version: _Optional[str]=...) -> None:
        ...

class ReadVersionResponse(_message.Message):
    __slots__ = ('files',)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _files_pb2.Files

    def __init__(self, files: _Optional[_Union[_files_pb2.Files, _Mapping]]=...) -> None:
        ...

class EncryptSecretRequest(_message.Message):
    __slots__ = ('client_secret',)
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_secret: str

    def __init__(self, client_secret: _Optional[str]=...) -> None:
        ...

class EncryptSecretResponse(_message.Message):
    __slots__ = ('account_linking_secret',)
    ACCOUNT_LINKING_SECRET_FIELD_NUMBER: _ClassVar[int]
    account_linking_secret: _account_linking_secret_pb2.AccountLinkingSecret

    def __init__(self, account_linking_secret: _Optional[_Union[_account_linking_secret_pb2.AccountLinkingSecret, _Mapping]]=...) -> None:
        ...

class DecryptSecretRequest(_message.Message):
    __slots__ = ('encrypted_client_secret',)
    ENCRYPTED_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    encrypted_client_secret: bytes

    def __init__(self, encrypted_client_secret: _Optional[bytes]=...) -> None:
        ...

class DecryptSecretResponse(_message.Message):
    __slots__ = ('client_secret',)
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    client_secret: str

    def __init__(self, client_secret: _Optional[str]=...) -> None:
        ...

class ListSampleProjectsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSampleProjectsResponse(_message.Message):
    __slots__ = ('sample_projects', 'next_page_token')
    SAMPLE_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sample_projects: _containers.RepeatedCompositeFieldContainer[SampleProject]
    next_page_token: str

    def __init__(self, sample_projects: _Optional[_Iterable[_Union[SampleProject, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SampleProject(_message.Message):
    __slots__ = ('name', 'hosted_url', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTED_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    hosted_url: str
    description: str

    def __init__(self, name: _Optional[str]=..., hosted_url: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ListReleaseChannelsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReleaseChannelsResponse(_message.Message):
    __slots__ = ('release_channels', 'next_page_token')
    RELEASE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    release_channels: _containers.RepeatedCompositeFieldContainer[_release_channel_pb2.ReleaseChannel]
    next_page_token: str

    def __init__(self, release_channels: _Optional[_Iterable[_Union[_release_channel_pb2.ReleaseChannel, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[_version_pb2.Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[_version_pb2.Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...