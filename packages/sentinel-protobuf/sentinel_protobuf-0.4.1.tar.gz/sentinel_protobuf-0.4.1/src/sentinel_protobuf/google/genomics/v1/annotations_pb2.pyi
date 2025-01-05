from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANNOTATION_TYPE_UNSPECIFIED: _ClassVar[AnnotationType]
    GENERIC: _ClassVar[AnnotationType]
    VARIANT: _ClassVar[AnnotationType]
    GENE: _ClassVar[AnnotationType]
    TRANSCRIPT: _ClassVar[AnnotationType]
ANNOTATION_TYPE_UNSPECIFIED: AnnotationType
GENERIC: AnnotationType
VARIANT: AnnotationType
GENE: AnnotationType
TRANSCRIPT: AnnotationType

class AnnotationSet(_message.Message):
    __slots__ = ('id', 'dataset_id', 'reference_set_id', 'name', 'source_uri', 'type', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataset_id: str
    reference_set_id: str
    name: str
    source_uri: str
    type: AnnotationType
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., dataset_id: _Optional[str]=..., reference_set_id: _Optional[str]=..., name: _Optional[str]=..., source_uri: _Optional[str]=..., type: _Optional[_Union[AnnotationType, str]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...

class Annotation(_message.Message):
    __slots__ = ('id', 'annotation_set_id', 'name', 'reference_id', 'reference_name', 'start', 'end', 'reverse_strand', 'type', 'variant', 'transcript', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    REVERSE_STRAND_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    annotation_set_id: str
    name: str
    reference_id: str
    reference_name: str
    start: int
    end: int
    reverse_strand: bool
    type: AnnotationType
    variant: VariantAnnotation
    transcript: Transcript
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., annotation_set_id: _Optional[str]=..., name: _Optional[str]=..., reference_id: _Optional[str]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., reverse_strand: bool=..., type: _Optional[_Union[AnnotationType, str]]=..., variant: _Optional[_Union[VariantAnnotation, _Mapping]]=..., transcript: _Optional[_Union[Transcript, _Mapping]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...

class VariantAnnotation(_message.Message):
    __slots__ = ('type', 'effect', 'alternate_bases', 'gene_id', 'transcript_ids', 'conditions', 'clinical_significance')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[VariantAnnotation.Type]
        TYPE_OTHER: _ClassVar[VariantAnnotation.Type]
        INSERTION: _ClassVar[VariantAnnotation.Type]
        DELETION: _ClassVar[VariantAnnotation.Type]
        SUBSTITUTION: _ClassVar[VariantAnnotation.Type]
        SNP: _ClassVar[VariantAnnotation.Type]
        STRUCTURAL: _ClassVar[VariantAnnotation.Type]
        CNV: _ClassVar[VariantAnnotation.Type]
    TYPE_UNSPECIFIED: VariantAnnotation.Type
    TYPE_OTHER: VariantAnnotation.Type
    INSERTION: VariantAnnotation.Type
    DELETION: VariantAnnotation.Type
    SUBSTITUTION: VariantAnnotation.Type
    SNP: VariantAnnotation.Type
    STRUCTURAL: VariantAnnotation.Type
    CNV: VariantAnnotation.Type

    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECT_UNSPECIFIED: _ClassVar[VariantAnnotation.Effect]
        EFFECT_OTHER: _ClassVar[VariantAnnotation.Effect]
        FRAMESHIFT: _ClassVar[VariantAnnotation.Effect]
        FRAME_PRESERVING_INDEL: _ClassVar[VariantAnnotation.Effect]
        SYNONYMOUS_SNP: _ClassVar[VariantAnnotation.Effect]
        NONSYNONYMOUS_SNP: _ClassVar[VariantAnnotation.Effect]
        STOP_GAIN: _ClassVar[VariantAnnotation.Effect]
        STOP_LOSS: _ClassVar[VariantAnnotation.Effect]
        SPLICE_SITE_DISRUPTION: _ClassVar[VariantAnnotation.Effect]
    EFFECT_UNSPECIFIED: VariantAnnotation.Effect
    EFFECT_OTHER: VariantAnnotation.Effect
    FRAMESHIFT: VariantAnnotation.Effect
    FRAME_PRESERVING_INDEL: VariantAnnotation.Effect
    SYNONYMOUS_SNP: VariantAnnotation.Effect
    NONSYNONYMOUS_SNP: VariantAnnotation.Effect
    STOP_GAIN: VariantAnnotation.Effect
    STOP_LOSS: VariantAnnotation.Effect
    SPLICE_SITE_DISRUPTION: VariantAnnotation.Effect

    class ClinicalSignificance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLINICAL_SIGNIFICANCE_UNSPECIFIED: _ClassVar[VariantAnnotation.ClinicalSignificance]
        CLINICAL_SIGNIFICANCE_OTHER: _ClassVar[VariantAnnotation.ClinicalSignificance]
        UNCERTAIN: _ClassVar[VariantAnnotation.ClinicalSignificance]
        BENIGN: _ClassVar[VariantAnnotation.ClinicalSignificance]
        LIKELY_BENIGN: _ClassVar[VariantAnnotation.ClinicalSignificance]
        LIKELY_PATHOGENIC: _ClassVar[VariantAnnotation.ClinicalSignificance]
        PATHOGENIC: _ClassVar[VariantAnnotation.ClinicalSignificance]
        DRUG_RESPONSE: _ClassVar[VariantAnnotation.ClinicalSignificance]
        HISTOCOMPATIBILITY: _ClassVar[VariantAnnotation.ClinicalSignificance]
        CONFERS_SENSITIVITY: _ClassVar[VariantAnnotation.ClinicalSignificance]
        RISK_FACTOR: _ClassVar[VariantAnnotation.ClinicalSignificance]
        ASSOCIATION: _ClassVar[VariantAnnotation.ClinicalSignificance]
        PROTECTIVE: _ClassVar[VariantAnnotation.ClinicalSignificance]
        MULTIPLE_REPORTED: _ClassVar[VariantAnnotation.ClinicalSignificance]
    CLINICAL_SIGNIFICANCE_UNSPECIFIED: VariantAnnotation.ClinicalSignificance
    CLINICAL_SIGNIFICANCE_OTHER: VariantAnnotation.ClinicalSignificance
    UNCERTAIN: VariantAnnotation.ClinicalSignificance
    BENIGN: VariantAnnotation.ClinicalSignificance
    LIKELY_BENIGN: VariantAnnotation.ClinicalSignificance
    LIKELY_PATHOGENIC: VariantAnnotation.ClinicalSignificance
    PATHOGENIC: VariantAnnotation.ClinicalSignificance
    DRUG_RESPONSE: VariantAnnotation.ClinicalSignificance
    HISTOCOMPATIBILITY: VariantAnnotation.ClinicalSignificance
    CONFERS_SENSITIVITY: VariantAnnotation.ClinicalSignificance
    RISK_FACTOR: VariantAnnotation.ClinicalSignificance
    ASSOCIATION: VariantAnnotation.ClinicalSignificance
    PROTECTIVE: VariantAnnotation.ClinicalSignificance
    MULTIPLE_REPORTED: VariantAnnotation.ClinicalSignificance

    class ClinicalCondition(_message.Message):
        __slots__ = ('names', 'external_ids', 'concept_id', 'omim_id')
        NAMES_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_IDS_FIELD_NUMBER: _ClassVar[int]
        CONCEPT_ID_FIELD_NUMBER: _ClassVar[int]
        OMIM_ID_FIELD_NUMBER: _ClassVar[int]
        names: _containers.RepeatedScalarFieldContainer[str]
        external_ids: _containers.RepeatedCompositeFieldContainer[ExternalId]
        concept_id: str
        omim_id: str

        def __init__(self, names: _Optional[_Iterable[str]]=..., external_ids: _Optional[_Iterable[_Union[ExternalId, _Mapping]]]=..., concept_id: _Optional[str]=..., omim_id: _Optional[str]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_BASES_FIELD_NUMBER: _ClassVar[int]
    GENE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_IDS_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CLINICAL_SIGNIFICANCE_FIELD_NUMBER: _ClassVar[int]
    type: VariantAnnotation.Type
    effect: VariantAnnotation.Effect
    alternate_bases: str
    gene_id: str
    transcript_ids: _containers.RepeatedScalarFieldContainer[str]
    conditions: _containers.RepeatedCompositeFieldContainer[VariantAnnotation.ClinicalCondition]
    clinical_significance: VariantAnnotation.ClinicalSignificance

    def __init__(self, type: _Optional[_Union[VariantAnnotation.Type, str]]=..., effect: _Optional[_Union[VariantAnnotation.Effect, str]]=..., alternate_bases: _Optional[str]=..., gene_id: _Optional[str]=..., transcript_ids: _Optional[_Iterable[str]]=..., conditions: _Optional[_Iterable[_Union[VariantAnnotation.ClinicalCondition, _Mapping]]]=..., clinical_significance: _Optional[_Union[VariantAnnotation.ClinicalSignificance, str]]=...) -> None:
        ...

class Transcript(_message.Message):
    __slots__ = ('gene_id', 'exons', 'coding_sequence')

    class Exon(_message.Message):
        __slots__ = ('start', 'end', 'frame')
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        FRAME_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        frame: _wrappers_pb2.Int32Value

        def __init__(self, start: _Optional[int]=..., end: _Optional[int]=..., frame: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
            ...

    class CodingSequence(_message.Message):
        __slots__ = ('start', 'end')
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int

        def __init__(self, start: _Optional[int]=..., end: _Optional[int]=...) -> None:
            ...
    GENE_ID_FIELD_NUMBER: _ClassVar[int]
    EXONS_FIELD_NUMBER: _ClassVar[int]
    CODING_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    gene_id: str
    exons: _containers.RepeatedCompositeFieldContainer[Transcript.Exon]
    coding_sequence: Transcript.CodingSequence

    def __init__(self, gene_id: _Optional[str]=..., exons: _Optional[_Iterable[_Union[Transcript.Exon, _Mapping]]]=..., coding_sequence: _Optional[_Union[Transcript.CodingSequence, _Mapping]]=...) -> None:
        ...

class ExternalId(_message.Message):
    __slots__ = ('source_name', 'id')
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    source_name: str
    id: str

    def __init__(self, source_name: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...

class CreateAnnotationSetRequest(_message.Message):
    __slots__ = ('annotation_set',)
    ANNOTATION_SET_FIELD_NUMBER: _ClassVar[int]
    annotation_set: AnnotationSet

    def __init__(self, annotation_set: _Optional[_Union[AnnotationSet, _Mapping]]=...) -> None:
        ...

class GetAnnotationSetRequest(_message.Message):
    __slots__ = ('annotation_set_id',)
    ANNOTATION_SET_ID_FIELD_NUMBER: _ClassVar[int]
    annotation_set_id: str

    def __init__(self, annotation_set_id: _Optional[str]=...) -> None:
        ...

class UpdateAnnotationSetRequest(_message.Message):
    __slots__ = ('annotation_set_id', 'annotation_set', 'update_mask')
    ANNOTATION_SET_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    annotation_set_id: str
    annotation_set: AnnotationSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, annotation_set_id: _Optional[str]=..., annotation_set: _Optional[_Union[AnnotationSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAnnotationSetRequest(_message.Message):
    __slots__ = ('annotation_set_id',)
    ANNOTATION_SET_ID_FIELD_NUMBER: _ClassVar[int]
    annotation_set_id: str

    def __init__(self, annotation_set_id: _Optional[str]=...) -> None:
        ...

class SearchAnnotationSetsRequest(_message.Message):
    __slots__ = ('dataset_ids', 'reference_set_id', 'name', 'types', 'page_token', 'page_size')
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_set_id: str
    name: str
    types: _containers.RepeatedScalarFieldContainer[AnnotationType]
    page_token: str
    page_size: int

    def __init__(self, dataset_ids: _Optional[_Iterable[str]]=..., reference_set_id: _Optional[str]=..., name: _Optional[str]=..., types: _Optional[_Iterable[_Union[AnnotationType, str]]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchAnnotationSetsResponse(_message.Message):
    __slots__ = ('annotation_sets', 'next_page_token')
    ANNOTATION_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotation_sets: _containers.RepeatedCompositeFieldContainer[AnnotationSet]
    next_page_token: str

    def __init__(self, annotation_sets: _Optional[_Iterable[_Union[AnnotationSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateAnnotationRequest(_message.Message):
    __slots__ = ('annotation',)
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    annotation: Annotation

    def __init__(self, annotation: _Optional[_Union[Annotation, _Mapping]]=...) -> None:
        ...

class BatchCreateAnnotationsRequest(_message.Message):
    __slots__ = ('annotations', 'request_id')
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    request_id: str

    def __init__(self, annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]]=..., request_id: _Optional[str]=...) -> None:
        ...

class BatchCreateAnnotationsResponse(_message.Message):
    __slots__ = ('entries',)

    class Entry(_message.Message):
        __slots__ = ('status', 'annotation')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status
        annotation: Annotation

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., annotation: _Optional[_Union[Annotation, _Mapping]]=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[BatchCreateAnnotationsResponse.Entry]

    def __init__(self, entries: _Optional[_Iterable[_Union[BatchCreateAnnotationsResponse.Entry, _Mapping]]]=...) -> None:
        ...

class GetAnnotationRequest(_message.Message):
    __slots__ = ('annotation_id',)
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    annotation_id: str

    def __init__(self, annotation_id: _Optional[str]=...) -> None:
        ...

class UpdateAnnotationRequest(_message.Message):
    __slots__ = ('annotation_id', 'annotation', 'update_mask')
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    annotation_id: str
    annotation: Annotation
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, annotation_id: _Optional[str]=..., annotation: _Optional[_Union[Annotation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAnnotationRequest(_message.Message):
    __slots__ = ('annotation_id',)
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    annotation_id: str

    def __init__(self, annotation_id: _Optional[str]=...) -> None:
        ...

class SearchAnnotationsRequest(_message.Message):
    __slots__ = ('annotation_set_ids', 'reference_id', 'reference_name', 'start', 'end', 'page_token', 'page_size')
    ANNOTATION_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    annotation_set_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_id: str
    reference_name: str
    start: int
    end: int
    page_token: str
    page_size: int

    def __init__(self, annotation_set_ids: _Optional[_Iterable[str]]=..., reference_id: _Optional[str]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchAnnotationsResponse(_message.Message):
    __slots__ = ('annotations', 'next_page_token')
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    next_page_token: str

    def __init__(self, annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...