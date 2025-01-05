from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import project_pb2 as _project_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ProvisionProjectRequest(_message.Message):
    __slots__ = ('name', 'accept_data_use_terms', 'data_use_terms_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_DATA_USE_TERMS_FIELD_NUMBER: _ClassVar[int]
    DATA_USE_TERMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    accept_data_use_terms: bool
    data_use_terms_version: str

    def __init__(self, name: _Optional[str]=..., accept_data_use_terms: bool=..., data_use_terms_version: _Optional[str]=...) -> None:
        ...

class ProvisionProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReportConsentChangeRequest(_message.Message):
    __slots__ = ('consent_change_action', 'project', 'service_term_id', 'service_term_version')

    class ConsentChangeAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSENT_CHANGE_ACTION_UNSPECIFIED: _ClassVar[ReportConsentChangeRequest.ConsentChangeAction]
        ACCEPT: _ClassVar[ReportConsentChangeRequest.ConsentChangeAction]
    CONSENT_CHANGE_ACTION_UNSPECIFIED: ReportConsentChangeRequest.ConsentChangeAction
    ACCEPT: ReportConsentChangeRequest.ConsentChangeAction
    CONSENT_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TERM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TERM_VERSION_FIELD_NUMBER: _ClassVar[int]
    consent_change_action: ReportConsentChangeRequest.ConsentChangeAction
    project: str
    service_term_id: str
    service_term_version: str

    def __init__(self, consent_change_action: _Optional[_Union[ReportConsentChangeRequest.ConsentChangeAction, str]]=..., project: _Optional[str]=..., service_term_id: _Optional[str]=..., service_term_version: _Optional[str]=...) -> None:
        ...