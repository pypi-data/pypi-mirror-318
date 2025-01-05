from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.devtools.containeranalysis.v1beta1.attestation import attestation_pb2 as _attestation_pb2
from google.devtools.containeranalysis.v1beta1.build import build_pb2 as _build_pb2
from google.devtools.containeranalysis.v1beta1.common import common_pb2 as _common_pb2
from google.devtools.containeranalysis.v1beta1.deployment import deployment_pb2 as _deployment_pb2
from google.devtools.containeranalysis.v1beta1.discovery import discovery_pb2 as _discovery_pb2
from google.devtools.containeranalysis.v1beta1.image import image_pb2 as _image_pb2
from google.devtools.containeranalysis.v1beta1.package import package_pb2 as _package_pb2
from google.devtools.containeranalysis.v1beta1.provenance import provenance_pb2 as _provenance_pb2
from google.devtools.containeranalysis.v1beta1.vulnerability import vulnerability_pb2 as _vulnerability_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Occurrence(_message.Message):
    __slots__ = ('name', 'resource', 'note_name', 'kind', 'remediation', 'create_time', 'update_time', 'vulnerability', 'build', 'derived_image', 'installation', 'deployment', 'discovered', 'attestation')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    NOTE_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    DERIVED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource: Resource
    note_name: str
    kind: _common_pb2.NoteKind
    remediation: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    vulnerability: _vulnerability_pb2.Details
    build: _build_pb2.Details
    derived_image: _image_pb2.Details
    installation: _package_pb2.Details
    deployment: _deployment_pb2.Details
    discovered: _discovery_pb2.Details
    attestation: _attestation_pb2.Details

    def __init__(self, name: _Optional[str]=..., resource: _Optional[_Union[Resource, _Mapping]]=..., note_name: _Optional[str]=..., kind: _Optional[_Union[_common_pb2.NoteKind, str]]=..., remediation: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., vulnerability: _Optional[_Union[_vulnerability_pb2.Details, _Mapping]]=..., build: _Optional[_Union[_build_pb2.Details, _Mapping]]=..., derived_image: _Optional[_Union[_image_pb2.Details, _Mapping]]=..., installation: _Optional[_Union[_package_pb2.Details, _Mapping]]=..., deployment: _Optional[_Union[_deployment_pb2.Details, _Mapping]]=..., discovered: _Optional[_Union[_discovery_pb2.Details, _Mapping]]=..., attestation: _Optional[_Union[_attestation_pb2.Details, _Mapping]]=...) -> None:
        ...

class Resource(_message.Message):
    __slots__ = ('name', 'uri', 'content_hash')
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HASH_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    content_hash: _provenance_pb2.Hash

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., content_hash: _Optional[_Union[_provenance_pb2.Hash, _Mapping]]=...) -> None:
        ...

class Note(_message.Message):
    __slots__ = ('name', 'short_description', 'long_description', 'kind', 'related_url', 'expiration_time', 'create_time', 'update_time', 'related_note_names', 'vulnerability', 'build', 'base_image', 'package', 'deployable', 'discovery', 'attestation_authority')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LONG_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    RELATED_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RELATED_NOTE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    BASE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYABLE_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    ATTESTATION_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    short_description: str
    long_description: str
    kind: _common_pb2.NoteKind
    related_url: _containers.RepeatedCompositeFieldContainer[_common_pb2.RelatedUrl]
    expiration_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    related_note_names: _containers.RepeatedScalarFieldContainer[str]
    vulnerability: _vulnerability_pb2.Vulnerability
    build: _build_pb2.Build
    base_image: _image_pb2.Basis
    package: _package_pb2.Package
    deployable: _deployment_pb2.Deployable
    discovery: _discovery_pb2.Discovery
    attestation_authority: _attestation_pb2.Authority

    def __init__(self, name: _Optional[str]=..., short_description: _Optional[str]=..., long_description: _Optional[str]=..., kind: _Optional[_Union[_common_pb2.NoteKind, str]]=..., related_url: _Optional[_Iterable[_Union[_common_pb2.RelatedUrl, _Mapping]]]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., related_note_names: _Optional[_Iterable[str]]=..., vulnerability: _Optional[_Union[_vulnerability_pb2.Vulnerability, _Mapping]]=..., build: _Optional[_Union[_build_pb2.Build, _Mapping]]=..., base_image: _Optional[_Union[_image_pb2.Basis, _Mapping]]=..., package: _Optional[_Union[_package_pb2.Package, _Mapping]]=..., deployable: _Optional[_Union[_deployment_pb2.Deployable, _Mapping]]=..., discovery: _Optional[_Union[_discovery_pb2.Discovery, _Mapping]]=..., attestation_authority: _Optional[_Union[_attestation_pb2.Authority, _Mapping]]=...) -> None:
        ...

class GetOccurrenceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOccurrencesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOccurrencesResponse(_message.Message):
    __slots__ = ('occurrences', 'next_page_token')
    OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    occurrences: _containers.RepeatedCompositeFieldContainer[Occurrence]
    next_page_token: str

    def __init__(self, occurrences: _Optional[_Iterable[_Union[Occurrence, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteOccurrenceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOccurrenceRequest(_message.Message):
    __slots__ = ('parent', 'occurrence')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    occurrence: Occurrence

    def __init__(self, parent: _Optional[str]=..., occurrence: _Optional[_Union[Occurrence, _Mapping]]=...) -> None:
        ...

class UpdateOccurrenceRequest(_message.Message):
    __slots__ = ('name', 'occurrence', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    occurrence: Occurrence
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., occurrence: _Optional[_Union[Occurrence, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetNoteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetOccurrenceNoteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNotesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNotesResponse(_message.Message):
    __slots__ = ('notes', 'next_page_token')
    NOTES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[Note]
    next_page_token: str

    def __init__(self, notes: _Optional[_Iterable[_Union[Note, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteNoteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateNoteRequest(_message.Message):
    __slots__ = ('parent', 'note_id', 'note')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    note_id: str
    note: Note

    def __init__(self, parent: _Optional[str]=..., note_id: _Optional[str]=..., note: _Optional[_Union[Note, _Mapping]]=...) -> None:
        ...

class UpdateNoteRequest(_message.Message):
    __slots__ = ('name', 'note', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    note: Note
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., note: _Optional[_Union[Note, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListNoteOccurrencesRequest(_message.Message):
    __slots__ = ('name', 'filter', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListNoteOccurrencesResponse(_message.Message):
    __slots__ = ('occurrences', 'next_page_token')
    OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    occurrences: _containers.RepeatedCompositeFieldContainer[Occurrence]
    next_page_token: str

    def __init__(self, occurrences: _Optional[_Iterable[_Union[Occurrence, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchCreateNotesRequest(_message.Message):
    __slots__ = ('parent', 'notes')

    class NotesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Note

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Note, _Mapping]]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notes: _containers.MessageMap[str, Note]

    def __init__(self, parent: _Optional[str]=..., notes: _Optional[_Mapping[str, Note]]=...) -> None:
        ...

class BatchCreateNotesResponse(_message.Message):
    __slots__ = ('notes',)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[Note]

    def __init__(self, notes: _Optional[_Iterable[_Union[Note, _Mapping]]]=...) -> None:
        ...

class BatchCreateOccurrencesRequest(_message.Message):
    __slots__ = ('parent', 'occurrences')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    occurrences: _containers.RepeatedCompositeFieldContainer[Occurrence]

    def __init__(self, parent: _Optional[str]=..., occurrences: _Optional[_Iterable[_Union[Occurrence, _Mapping]]]=...) -> None:
        ...

class BatchCreateOccurrencesResponse(_message.Message):
    __slots__ = ('occurrences',)
    OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    occurrences: _containers.RepeatedCompositeFieldContainer[Occurrence]

    def __init__(self, occurrences: _Optional[_Iterable[_Union[Occurrence, _Mapping]]]=...) -> None:
        ...

class GetVulnerabilityOccurrencesSummaryRequest(_message.Message):
    __slots__ = ('parent', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class VulnerabilityOccurrencesSummary(_message.Message):
    __slots__ = ('counts',)

    class FixableTotalByDigest(_message.Message):
        __slots__ = ('resource', 'severity', 'fixable_count', 'total_count')
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        FIXABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
        resource: Resource
        severity: _vulnerability_pb2.Severity
        fixable_count: int
        total_count: int

        def __init__(self, resource: _Optional[_Union[Resource, _Mapping]]=..., severity: _Optional[_Union[_vulnerability_pb2.Severity, str]]=..., fixable_count: _Optional[int]=..., total_count: _Optional[int]=...) -> None:
            ...
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    counts: _containers.RepeatedCompositeFieldContainer[VulnerabilityOccurrencesSummary.FixableTotalByDigest]

    def __init__(self, counts: _Optional[_Iterable[_Union[VulnerabilityOccurrencesSummary.FixableTotalByDigest, _Mapping]]]=...) -> None:
        ...