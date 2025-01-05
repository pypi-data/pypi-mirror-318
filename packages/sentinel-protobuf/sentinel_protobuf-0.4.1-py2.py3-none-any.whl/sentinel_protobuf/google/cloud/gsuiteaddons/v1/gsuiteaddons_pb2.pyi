from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.apps.script.type.calendar import calendar_addon_manifest_pb2 as _calendar_addon_manifest_pb2
from google.apps.script.type.docs import docs_addon_manifest_pb2 as _docs_addon_manifest_pb2
from google.apps.script.type.drive import drive_addon_manifest_pb2 as _drive_addon_manifest_pb2
from google.apps.script.type.gmail import gmail_addon_manifest_pb2 as _gmail_addon_manifest_pb2
from google.apps.script.type import script_manifest_pb2 as _script_manifest_pb2
from google.apps.script.type.sheets import sheets_addon_manifest_pb2 as _sheets_addon_manifest_pb2
from google.apps.script.type.slides import slides_addon_manifest_pb2 as _slides_addon_manifest_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetAuthorizationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Authorization(_message.Message):
    __slots__ = ('name', 'service_account_email', 'oauth_client_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_account_email: str
    oauth_client_id: str

    def __init__(self, name: _Optional[str]=..., service_account_email: _Optional[str]=..., oauth_client_id: _Optional[str]=...) -> None:
        ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'deployment_id', 'deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_id: str
    deployment: Deployment

    def __init__(self, parent: _Optional[str]=..., deployment_id: _Optional[str]=..., deployment: _Optional[_Union[Deployment, _Mapping]]=...) -> None:
        ...

class ReplaceDeploymentRequest(_message.Message):
    __slots__ = ('deployment',)
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    deployment: Deployment

    def __init__(self, deployment: _Optional[_Union[Deployment, _Mapping]]=...) -> None:
        ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteDeploymentRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class InstallDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UninstallDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetInstallStatusRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class InstallStatus(_message.Message):
    __slots__ = ('name', 'installed')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    installed: _wrappers_pb2.BoolValue

    def __init__(self, name: _Optional[str]=..., installed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ('name', 'oauth_scopes', 'add_ons', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    ADD_ONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    oauth_scopes: _containers.RepeatedScalarFieldContainer[str]
    add_ons: AddOns
    etag: str

    def __init__(self, name: _Optional[str]=..., oauth_scopes: _Optional[_Iterable[str]]=..., add_ons: _Optional[_Union[AddOns, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class AddOns(_message.Message):
    __slots__ = ('common', 'gmail', 'drive', 'calendar', 'docs', 'sheets', 'slides', 'http_options')
    COMMON_FIELD_NUMBER: _ClassVar[int]
    GMAIL_FIELD_NUMBER: _ClassVar[int]
    DRIVE_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    DOCS_FIELD_NUMBER: _ClassVar[int]
    SHEETS_FIELD_NUMBER: _ClassVar[int]
    SLIDES_FIELD_NUMBER: _ClassVar[int]
    HTTP_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    common: _script_manifest_pb2.CommonAddOnManifest
    gmail: _gmail_addon_manifest_pb2.GmailAddOnManifest
    drive: _drive_addon_manifest_pb2.DriveAddOnManifest
    calendar: _calendar_addon_manifest_pb2.CalendarAddOnManifest
    docs: _docs_addon_manifest_pb2.DocsAddOnManifest
    sheets: _sheets_addon_manifest_pb2.SheetsAddOnManifest
    slides: _slides_addon_manifest_pb2.SlidesAddOnManifest
    http_options: _script_manifest_pb2.HttpOptions

    def __init__(self, common: _Optional[_Union[_script_manifest_pb2.CommonAddOnManifest, _Mapping]]=..., gmail: _Optional[_Union[_gmail_addon_manifest_pb2.GmailAddOnManifest, _Mapping]]=..., drive: _Optional[_Union[_drive_addon_manifest_pb2.DriveAddOnManifest, _Mapping]]=..., calendar: _Optional[_Union[_calendar_addon_manifest_pb2.CalendarAddOnManifest, _Mapping]]=..., docs: _Optional[_Union[_docs_addon_manifest_pb2.DocsAddOnManifest, _Mapping]]=..., sheets: _Optional[_Union[_sheets_addon_manifest_pb2.SheetsAddOnManifest, _Mapping]]=..., slides: _Optional[_Union[_slides_addon_manifest_pb2.SlidesAddOnManifest, _Mapping]]=..., http_options: _Optional[_Union[_script_manifest_pb2.HttpOptions, _Mapping]]=...) -> None:
        ...