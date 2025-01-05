from google.api import annotations_pb2 as _annotations_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InfoMergeOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFO_MERGE_OPERATION_UNSPECIFIED: _ClassVar[InfoMergeOperation]
    IGNORE_NEW: _ClassVar[InfoMergeOperation]
    MOVE_TO_CALLS: _ClassVar[InfoMergeOperation]
INFO_MERGE_OPERATION_UNSPECIFIED: InfoMergeOperation
IGNORE_NEW: InfoMergeOperation
MOVE_TO_CALLS: InfoMergeOperation

class VariantSetMetadata(_message.Message):
    __slots__ = ('key', 'value', 'id', 'type', 'number', 'description', 'info')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[VariantSetMetadata.Type]
        INTEGER: _ClassVar[VariantSetMetadata.Type]
        FLOAT: _ClassVar[VariantSetMetadata.Type]
        FLAG: _ClassVar[VariantSetMetadata.Type]
        CHARACTER: _ClassVar[VariantSetMetadata.Type]
        STRING: _ClassVar[VariantSetMetadata.Type]
    TYPE_UNSPECIFIED: VariantSetMetadata.Type
    INTEGER: VariantSetMetadata.Type
    FLOAT: VariantSetMetadata.Type
    FLAG: VariantSetMetadata.Type
    CHARACTER: VariantSetMetadata.Type
    STRING: VariantSetMetadata.Type

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    id: str
    type: VariantSetMetadata.Type
    number: str
    description: str
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=..., id: _Optional[str]=..., type: _Optional[_Union[VariantSetMetadata.Type, str]]=..., number: _Optional[str]=..., description: _Optional[str]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...

class VariantSet(_message.Message):
    __slots__ = ('dataset_id', 'id', 'reference_set_id', 'reference_bounds', 'metadata', 'name', 'description')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    id: str
    reference_set_id: str
    reference_bounds: _containers.RepeatedCompositeFieldContainer[ReferenceBound]
    metadata: _containers.RepeatedCompositeFieldContainer[VariantSetMetadata]
    name: str
    description: str

    def __init__(self, dataset_id: _Optional[str]=..., id: _Optional[str]=..., reference_set_id: _Optional[str]=..., reference_bounds: _Optional[_Iterable[_Union[ReferenceBound, _Mapping]]]=..., metadata: _Optional[_Iterable[_Union[VariantSetMetadata, _Mapping]]]=..., name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class Variant(_message.Message):
    __slots__ = ('variant_set_id', 'id', 'names', 'created', 'reference_name', 'start', 'end', 'reference_bases', 'alternate_bases', 'quality', 'filter', 'info', 'calls')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_BASES_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_BASES_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str
    id: str
    names: _containers.RepeatedScalarFieldContainer[str]
    created: int
    reference_name: str
    start: int
    end: int
    reference_bases: str
    alternate_bases: _containers.RepeatedScalarFieldContainer[str]
    quality: float
    filter: _containers.RepeatedScalarFieldContainer[str]
    info: _containers.MessageMap[str, _struct_pb2.ListValue]
    calls: _containers.RepeatedCompositeFieldContainer[VariantCall]

    def __init__(self, variant_set_id: _Optional[str]=..., id: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., created: _Optional[int]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., reference_bases: _Optional[str]=..., alternate_bases: _Optional[_Iterable[str]]=..., quality: _Optional[float]=..., filter: _Optional[_Iterable[str]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=..., calls: _Optional[_Iterable[_Union[VariantCall, _Mapping]]]=...) -> None:
        ...

class VariantCall(_message.Message):
    __slots__ = ('call_set_id', 'call_set_name', 'genotype', 'phaseset', 'genotype_likelihood', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    CALL_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    GENOTYPE_FIELD_NUMBER: _ClassVar[int]
    PHASESET_FIELD_NUMBER: _ClassVar[int]
    GENOTYPE_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    call_set_id: str
    call_set_name: str
    genotype: _containers.RepeatedScalarFieldContainer[int]
    phaseset: str
    genotype_likelihood: _containers.RepeatedScalarFieldContainer[float]
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, call_set_id: _Optional[str]=..., call_set_name: _Optional[str]=..., genotype: _Optional[_Iterable[int]]=..., phaseset: _Optional[str]=..., genotype_likelihood: _Optional[_Iterable[float]]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...

class CallSet(_message.Message):
    __slots__ = ('id', 'name', 'sample_id', 'variant_set_ids', 'created', 'info')

    class InfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    sample_id: str
    variant_set_ids: _containers.RepeatedScalarFieldContainer[str]
    created: int
    info: _containers.MessageMap[str, _struct_pb2.ListValue]

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., sample_id: _Optional[str]=..., variant_set_ids: _Optional[_Iterable[str]]=..., created: _Optional[int]=..., info: _Optional[_Mapping[str, _struct_pb2.ListValue]]=...) -> None:
        ...

class ReferenceBound(_message.Message):
    __slots__ = ('reference_name', 'upper_bound')
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    reference_name: str
    upper_bound: int

    def __init__(self, reference_name: _Optional[str]=..., upper_bound: _Optional[int]=...) -> None:
        ...

class ImportVariantsRequest(_message.Message):
    __slots__ = ('variant_set_id', 'source_uris', 'format', 'normalize_reference_names', 'info_merge_config')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[ImportVariantsRequest.Format]
        FORMAT_VCF: _ClassVar[ImportVariantsRequest.Format]
        FORMAT_COMPLETE_GENOMICS: _ClassVar[ImportVariantsRequest.Format]
    FORMAT_UNSPECIFIED: ImportVariantsRequest.Format
    FORMAT_VCF: ImportVariantsRequest.Format
    FORMAT_COMPLETE_GENOMICS: ImportVariantsRequest.Format

    class InfoMergeConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InfoMergeOperation

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[InfoMergeOperation, str]]=...) -> None:
            ...
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_REFERENCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    INFO_MERGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str
    source_uris: _containers.RepeatedScalarFieldContainer[str]
    format: ImportVariantsRequest.Format
    normalize_reference_names: bool
    info_merge_config: _containers.ScalarMap[str, InfoMergeOperation]

    def __init__(self, variant_set_id: _Optional[str]=..., source_uris: _Optional[_Iterable[str]]=..., format: _Optional[_Union[ImportVariantsRequest.Format, str]]=..., normalize_reference_names: bool=..., info_merge_config: _Optional[_Mapping[str, InfoMergeOperation]]=...) -> None:
        ...

class ImportVariantsResponse(_message.Message):
    __slots__ = ('call_set_ids',)
    CALL_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    call_set_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, call_set_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateVariantSetRequest(_message.Message):
    __slots__ = ('variant_set',)
    VARIANT_SET_FIELD_NUMBER: _ClassVar[int]
    variant_set: VariantSet

    def __init__(self, variant_set: _Optional[_Union[VariantSet, _Mapping]]=...) -> None:
        ...

class ExportVariantSetRequest(_message.Message):
    __slots__ = ('variant_set_id', 'call_set_ids', 'project_id', 'format', 'bigquery_dataset', 'bigquery_table')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[ExportVariantSetRequest.Format]
        FORMAT_BIGQUERY: _ClassVar[ExportVariantSetRequest.Format]
    FORMAT_UNSPECIFIED: ExportVariantSetRequest.Format
    FORMAT_BIGQUERY: ExportVariantSetRequest.Format
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DATASET_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TABLE_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str
    call_set_ids: _containers.RepeatedScalarFieldContainer[str]
    project_id: str
    format: ExportVariantSetRequest.Format
    bigquery_dataset: str
    bigquery_table: str

    def __init__(self, variant_set_id: _Optional[str]=..., call_set_ids: _Optional[_Iterable[str]]=..., project_id: _Optional[str]=..., format: _Optional[_Union[ExportVariantSetRequest.Format, str]]=..., bigquery_dataset: _Optional[str]=..., bigquery_table: _Optional[str]=...) -> None:
        ...

class GetVariantSetRequest(_message.Message):
    __slots__ = ('variant_set_id',)
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str

    def __init__(self, variant_set_id: _Optional[str]=...) -> None:
        ...

class SearchVariantSetsRequest(_message.Message):
    __slots__ = ('dataset_ids', 'page_token', 'page_size')
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    page_token: str
    page_size: int

    def __init__(self, dataset_ids: _Optional[_Iterable[str]]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchVariantSetsResponse(_message.Message):
    __slots__ = ('variant_sets', 'next_page_token')
    VARIANT_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    variant_sets: _containers.RepeatedCompositeFieldContainer[VariantSet]
    next_page_token: str

    def __init__(self, variant_sets: _Optional[_Iterable[_Union[VariantSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteVariantSetRequest(_message.Message):
    __slots__ = ('variant_set_id',)
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str

    def __init__(self, variant_set_id: _Optional[str]=...) -> None:
        ...

class UpdateVariantSetRequest(_message.Message):
    __slots__ = ('variant_set_id', 'variant_set', 'update_mask')
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str
    variant_set: VariantSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, variant_set_id: _Optional[str]=..., variant_set: _Optional[_Union[VariantSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class SearchVariantsRequest(_message.Message):
    __slots__ = ('variant_set_ids', 'variant_name', 'call_set_ids', 'reference_name', 'start', 'end', 'page_token', 'page_size', 'max_calls')
    VARIANT_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    VARIANT_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_CALLS_FIELD_NUMBER: _ClassVar[int]
    variant_set_ids: _containers.RepeatedScalarFieldContainer[str]
    variant_name: str
    call_set_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_name: str
    start: int
    end: int
    page_token: str
    page_size: int
    max_calls: int

    def __init__(self, variant_set_ids: _Optional[_Iterable[str]]=..., variant_name: _Optional[str]=..., call_set_ids: _Optional[_Iterable[str]]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., max_calls: _Optional[int]=...) -> None:
        ...

class SearchVariantsResponse(_message.Message):
    __slots__ = ('variants', 'next_page_token')
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    variants: _containers.RepeatedCompositeFieldContainer[Variant]
    next_page_token: str

    def __init__(self, variants: _Optional[_Iterable[_Union[Variant, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateVariantRequest(_message.Message):
    __slots__ = ('variant',)
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: Variant

    def __init__(self, variant: _Optional[_Union[Variant, _Mapping]]=...) -> None:
        ...

class UpdateVariantRequest(_message.Message):
    __slots__ = ('variant_id', 'variant', 'update_mask')
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    variant_id: str
    variant: Variant
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, variant_id: _Optional[str]=..., variant: _Optional[_Union[Variant, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteVariantRequest(_message.Message):
    __slots__ = ('variant_id',)
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    variant_id: str

    def __init__(self, variant_id: _Optional[str]=...) -> None:
        ...

class GetVariantRequest(_message.Message):
    __slots__ = ('variant_id',)
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    variant_id: str

    def __init__(self, variant_id: _Optional[str]=...) -> None:
        ...

class MergeVariantsRequest(_message.Message):
    __slots__ = ('variant_set_id', 'variants', 'info_merge_config')

    class InfoMergeConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InfoMergeOperation

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[InfoMergeOperation, str]]=...) -> None:
            ...
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    INFO_MERGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    variant_set_id: str
    variants: _containers.RepeatedCompositeFieldContainer[Variant]
    info_merge_config: _containers.ScalarMap[str, InfoMergeOperation]

    def __init__(self, variant_set_id: _Optional[str]=..., variants: _Optional[_Iterable[_Union[Variant, _Mapping]]]=..., info_merge_config: _Optional[_Mapping[str, InfoMergeOperation]]=...) -> None:
        ...

class SearchCallSetsRequest(_message.Message):
    __slots__ = ('variant_set_ids', 'name', 'page_token', 'page_size')
    VARIANT_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    variant_set_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    page_token: str
    page_size: int

    def __init__(self, variant_set_ids: _Optional[_Iterable[str]]=..., name: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchCallSetsResponse(_message.Message):
    __slots__ = ('call_sets', 'next_page_token')
    CALL_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    call_sets: _containers.RepeatedCompositeFieldContainer[CallSet]
    next_page_token: str

    def __init__(self, call_sets: _Optional[_Iterable[_Union[CallSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateCallSetRequest(_message.Message):
    __slots__ = ('call_set',)
    CALL_SET_FIELD_NUMBER: _ClassVar[int]
    call_set: CallSet

    def __init__(self, call_set: _Optional[_Union[CallSet, _Mapping]]=...) -> None:
        ...

class UpdateCallSetRequest(_message.Message):
    __slots__ = ('call_set_id', 'call_set', 'update_mask')
    CALL_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    call_set_id: str
    call_set: CallSet
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, call_set_id: _Optional[str]=..., call_set: _Optional[_Union[CallSet, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCallSetRequest(_message.Message):
    __slots__ = ('call_set_id',)
    CALL_SET_ID_FIELD_NUMBER: _ClassVar[int]
    call_set_id: str

    def __init__(self, call_set_id: _Optional[str]=...) -> None:
        ...

class GetCallSetRequest(_message.Message):
    __slots__ = ('call_set_id',)
    CALL_SET_ID_FIELD_NUMBER: _ClassVar[int]
    call_set_id: str

    def __init__(self, call_set_id: _Optional[str]=...) -> None:
        ...

class StreamVariantsRequest(_message.Message):
    __slots__ = ('project_id', 'variant_set_id', 'call_set_ids', 'reference_name', 'start', 'end')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    variant_set_id: str
    call_set_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_name: str
    start: int
    end: int

    def __init__(self, project_id: _Optional[str]=..., variant_set_id: _Optional[str]=..., call_set_ids: _Optional[_Iterable[str]]=..., reference_name: _Optional[str]=..., start: _Optional[int]=..., end: _Optional[int]=...) -> None:
        ...

class StreamVariantsResponse(_message.Message):
    __slots__ = ('variants',)
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    variants: _containers.RepeatedCompositeFieldContainer[Variant]

    def __init__(self, variants: _Optional[_Iterable[_Union[Variant, _Mapping]]]=...) -> None:
        ...