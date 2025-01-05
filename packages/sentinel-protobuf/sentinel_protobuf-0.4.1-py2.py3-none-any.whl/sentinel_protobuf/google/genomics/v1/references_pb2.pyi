from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Reference(_message.Message):
    __slots__ = ('id', 'length', 'md5checksum', 'name', 'source_uri', 'source_accessions', 'ncbi_taxon_id')
    ID_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    MD5CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ACCESSIONS_FIELD_NUMBER: _ClassVar[int]
    NCBI_TAXON_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    length: int
    md5checksum: str
    name: str
    source_uri: str
    source_accessions: _containers.RepeatedScalarFieldContainer[str]
    ncbi_taxon_id: int

    def __init__(self, id: _Optional[str]=..., length: _Optional[int]=..., md5checksum: _Optional[str]=..., name: _Optional[str]=..., source_uri: _Optional[str]=..., source_accessions: _Optional[_Iterable[str]]=..., ncbi_taxon_id: _Optional[int]=...) -> None:
        ...

class ReferenceSet(_message.Message):
    __slots__ = ('id', 'reference_ids', 'md5checksum', 'ncbi_taxon_id', 'description', 'assembly_id', 'source_uri', 'source_accessions')
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IDS_FIELD_NUMBER: _ClassVar[int]
    MD5CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    NCBI_TAXON_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLY_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ACCESSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    reference_ids: _containers.RepeatedScalarFieldContainer[str]
    md5checksum: str
    ncbi_taxon_id: int
    description: str
    assembly_id: str
    source_uri: str
    source_accessions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., reference_ids: _Optional[_Iterable[str]]=..., md5checksum: _Optional[str]=..., ncbi_taxon_id: _Optional[int]=..., description: _Optional[str]=..., assembly_id: _Optional[str]=..., source_uri: _Optional[str]=..., source_accessions: _Optional[_Iterable[str]]=...) -> None:
        ...

class SearchReferenceSetsRequest(_message.Message):
    __slots__ = ('md5checksums', 'accessions', 'assembly_id', 'page_token', 'page_size')
    MD5CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    ACCESSIONS_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLY_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    md5checksums: _containers.RepeatedScalarFieldContainer[str]
    accessions: _containers.RepeatedScalarFieldContainer[str]
    assembly_id: str
    page_token: str
    page_size: int

    def __init__(self, md5checksums: _Optional[_Iterable[str]]=..., accessions: _Optional[_Iterable[str]]=..., assembly_id: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchReferenceSetsResponse(_message.Message):
    __slots__ = ('reference_sets', 'next_page_token')
    REFERENCE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reference_sets: _containers.RepeatedCompositeFieldContainer[ReferenceSet]
    next_page_token: str

    def __init__(self, reference_sets: _Optional[_Iterable[_Union[ReferenceSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetReferenceSetRequest(_message.Message):
    __slots__ = ('reference_set_id',)
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    reference_set_id: str

    def __init__(self, reference_set_id: _Optional[str]=...) -> None:
        ...

class SearchReferencesRequest(_message.Message):
    __slots__ = ('md5checksums', 'accessions', 'reference_set_id', 'page_token', 'page_size')
    MD5CHECKSUMS_FIELD_NUMBER: _ClassVar[int]
    ACCESSIONS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    md5checksums: _containers.RepeatedScalarFieldContainer[str]
    accessions: _containers.RepeatedScalarFieldContainer[str]
    reference_set_id: str
    page_token: str
    page_size: int

    def __init__(self, md5checksums: _Optional[_Iterable[str]]=..., accessions: _Optional[_Iterable[str]]=..., reference_set_id: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchReferencesResponse(_message.Message):
    __slots__ = ('references', 'next_page_token')
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    references: _containers.RepeatedCompositeFieldContainer[Reference]
    next_page_token: str

    def __init__(self, references: _Optional[_Iterable[_Union[Reference, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetReferenceRequest(_message.Message):
    __slots__ = ('reference_id',)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str

    def __init__(self, reference_id: _Optional[str]=...) -> None:
        ...

class ListBasesRequest(_message.Message):
    __slots__ = ('reference_id', 'start', 'end', 'page_token', 'page_size')
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    start: int
    end: int
    page_token: str
    page_size: int

    def __init__(self, reference_id: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListBasesResponse(_message.Message):
    __slots__ = ('offset', 'sequence', 'next_page_token')
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    offset: int
    sequence: str
    next_page_token: str

    def __init__(self, offset: _Optional[int]=..., sequence: _Optional[str]=..., next_page_token: _Optional[str]=...) -> None:
        ...