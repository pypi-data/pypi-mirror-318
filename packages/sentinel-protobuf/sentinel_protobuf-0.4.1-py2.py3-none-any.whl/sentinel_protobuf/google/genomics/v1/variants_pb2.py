"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/variants.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/genomics/v1/variants.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\x80\x03\n\x12VariantSetMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x129\n\x04type\x18\x05 \x01(\x0e2+.google.genomics.v1.VariantSetMetadata.Type\x12\x0e\n\x06number\x18\x08 \x01(\t\x12\x13\n\x0bdescription\x18\x07 \x01(\t\x12>\n\x04info\x18\x03 \x03(\x0b20.google.genomics.v1.VariantSetMetadata.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"Y\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INTEGER\x10\x01\x12\t\n\x05FLOAT\x10\x02\x12\x08\n\x04FLAG\x10\x03\x12\r\n\tCHARACTER\x10\x04\x12\n\n\x06STRING\x10\x05"\xe1\x01\n\nVariantSet\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x06 \x01(\t\x12<\n\x10reference_bounds\x18\x05 \x03(\x0b2".google.genomics.v1.ReferenceBound\x128\n\x08metadata\x18\x04 \x03(\x0b2&.google.genomics.v1.VariantSetMetadata\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x13\n\x0bdescription\x18\x08 \x01(\t"\x82\x03\n\x07Variant\x12\x16\n\x0evariant_set_id\x18\x0f \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05names\x18\x03 \x03(\t\x12\x0f\n\x07created\x18\x0c \x01(\x03\x12\x16\n\x0ereference_name\x18\x0e \x01(\t\x12\r\n\x05start\x18\x10 \x01(\x03\x12\x0b\n\x03end\x18\r \x01(\x03\x12\x17\n\x0freference_bases\x18\x06 \x01(\t\x12\x17\n\x0falternate_bases\x18\x07 \x03(\t\x12\x0f\n\x07quality\x18\x08 \x01(\x01\x12\x0e\n\x06filter\x18\t \x03(\t\x123\n\x04info\x18\n \x03(\x0b2%.google.genomics.v1.Variant.InfoEntry\x12.\n\x05calls\x18\x0b \x03(\x0b2\x1f.google.genomics.v1.VariantCall\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"\xfc\x01\n\x0bVariantCall\x12\x13\n\x0bcall_set_id\x18\x08 \x01(\t\x12\x15\n\rcall_set_name\x18\t \x01(\t\x12\x10\n\x08genotype\x18\x07 \x03(\x05\x12\x10\n\x08phaseset\x18\x05 \x01(\t\x12\x1b\n\x13genotype_likelihood\x18\x06 \x03(\x01\x127\n\x04info\x18\x02 \x03(\x0b2).google.genomics.v1.VariantCall.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"\xde\x01\n\x07CallSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tsample_id\x18\x07 \x01(\t\x12\x17\n\x0fvariant_set_ids\x18\x06 \x03(\t\x12\x0f\n\x07created\x18\x05 \x01(\x03\x123\n\x04info\x18\x04 \x03(\x0b2%.google.genomics.v1.CallSet.InfoEntry\x1aG\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"=\n\x0eReferenceBound\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x03"\xb4\x03\n\x15ImportVariantsRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x13\n\x0bsource_uris\x18\x02 \x03(\t\x12@\n\x06format\x18\x03 \x01(\x0e20.google.genomics.v1.ImportVariantsRequest.Format\x12!\n\x19normalize_reference_names\x18\x05 \x01(\x08\x12Y\n\x11info_merge_config\x18\x06 \x03(\x0b2>.google.genomics.v1.ImportVariantsRequest.InfoMergeConfigEntry\x1a^\n\x14InfoMergeConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0e2&.google.genomics.v1.InfoMergeOperation:\x028\x01"N\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nFORMAT_VCF\x10\x01\x12\x1c\n\x18FORMAT_COMPLETE_GENOMICS\x10\x02".\n\x16ImportVariantsResponse\x12\x14\n\x0ccall_set_ids\x18\x01 \x03(\t"N\n\x17CreateVariantSetRequest\x123\n\x0bvariant_set\x18\x01 \x01(\x0b2\x1e.google.genomics.v1.VariantSet"\x88\x02\n\x17ExportVariantSetRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x14\n\x0ccall_set_ids\x18\x02 \x03(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12B\n\x06format\x18\x04 \x01(\x0e22.google.genomics.v1.ExportVariantSetRequest.Format\x12\x18\n\x10bigquery_dataset\x18\x05 \x01(\t\x12\x16\n\x0ebigquery_table\x18\x06 \x01(\t"5\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\x13\n\x0fFORMAT_BIGQUERY\x10\x01".\n\x14GetVariantSetRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t"V\n\x18SearchVariantSetsRequest\x12\x13\n\x0bdataset_ids\x18\x01 \x03(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"j\n\x19SearchVariantSetsResponse\x124\n\x0cvariant_sets\x18\x01 \x03(\x0b2\x1e.google.genomics.v1.VariantSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"1\n\x17DeleteVariantSetRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t"\x97\x01\n\x17UpdateVariantSetRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x123\n\x0bvariant_set\x18\x02 \x01(\x0b2\x1e.google.genomics.v1.VariantSet\x12/\n\x0bupdate_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xca\x01\n\x15SearchVariantsRequest\x12\x17\n\x0fvariant_set_ids\x18\x01 \x03(\t\x12\x14\n\x0cvariant_name\x18\x02 \x01(\t\x12\x14\n\x0ccall_set_ids\x18\x03 \x03(\t\x12\x16\n\x0ereference_name\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\x12\x0b\n\x03end\x18\x06 \x01(\x03\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x11\n\tpage_size\x18\x08 \x01(\x05\x12\x11\n\tmax_calls\x18\t \x01(\x05"`\n\x16SearchVariantsResponse\x12-\n\x08variants\x18\x01 \x03(\x0b2\x1b.google.genomics.v1.Variant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"D\n\x14CreateVariantRequest\x12,\n\x07variant\x18\x01 \x01(\x0b2\x1b.google.genomics.v1.Variant"\x89\x01\n\x14UpdateVariantRequest\x12\x12\n\nvariant_id\x18\x01 \x01(\t\x12,\n\x07variant\x18\x02 \x01(\x0b2\x1b.google.genomics.v1.Variant\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"*\n\x14DeleteVariantRequest\x12\x12\n\nvariant_id\x18\x01 \x01(\t"\'\n\x11GetVariantRequest\x12\x12\n\nvariant_id\x18\x01 \x01(\t"\x97\x02\n\x14MergeVariantsRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12-\n\x08variants\x18\x02 \x03(\x0b2\x1b.google.genomics.v1.Variant\x12X\n\x11info_merge_config\x18\x03 \x03(\x0b2=.google.genomics.v1.MergeVariantsRequest.InfoMergeConfigEntry\x1a^\n\x14InfoMergeConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0e2&.google.genomics.v1.InfoMergeOperation:\x028\x01"e\n\x15SearchCallSetsRequest\x12\x17\n\x0fvariant_set_ids\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"a\n\x16SearchCallSetsResponse\x12.\n\tcall_sets\x18\x01 \x03(\x0b2\x1b.google.genomics.v1.CallSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"E\n\x14CreateCallSetRequest\x12-\n\x08call_set\x18\x01 \x01(\x0b2\x1b.google.genomics.v1.CallSet"\x8b\x01\n\x14UpdateCallSetRequest\x12\x13\n\x0bcall_set_id\x18\x01 \x01(\t\x12-\n\x08call_set\x18\x02 \x01(\x0b2\x1b.google.genomics.v1.CallSet\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"+\n\x14DeleteCallSetRequest\x12\x13\n\x0bcall_set_id\x18\x01 \x01(\t"(\n\x11GetCallSetRequest\x12\x13\n\x0bcall_set_id\x18\x01 \x01(\t"\x8d\x01\n\x15StreamVariantsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x16\n\x0evariant_set_id\x18\x02 \x01(\t\x12\x14\n\x0ccall_set_ids\x18\x03 \x03(\t\x12\x16\n\x0ereference_name\x18\x04 \x01(\t\x12\r\n\x05start\x18\x05 \x01(\x03\x12\x0b\n\x03end\x18\x06 \x01(\x03"G\n\x16StreamVariantsResponse\x12-\n\x08variants\x18\x01 \x03(\x0b2\x1b.google.genomics.v1.Variant*]\n\x12InfoMergeOperation\x12$\n INFO_MERGE_OPERATION_UNSPECIFIED\x10\x00\x12\x0e\n\nIGNORE_NEW\x10\x01\x12\x11\n\rMOVE_TO_CALLS\x10\x022\xa5\x01\n\x17StreamingVariantService\x12\x89\x01\n\x0eStreamVariants\x12).google.genomics.v1.StreamVariantsRequest\x1a*.google.genomics.v1.StreamVariantsResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants:stream:\x01*0\x012\xbd\x12\n\x10VariantServiceV1\x12z\n\x0eImportVariants\x12).google.genomics.v1.ImportVariantsRequest\x1a\x1d.google.longrunning.Operation"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants:import:\x01*\x12\x85\x01\n\x10CreateVariantSet\x12+.google.genomics.v1.CreateVariantSetRequest\x1a\x1e.google.genomics.v1.VariantSet"$\x82\xd3\xe4\x93\x02\x1e"\x0f/v1/variantsets:\x0bvariant_set\x12\x92\x01\n\x10ExportVariantSet\x12+.google.genomics.v1.ExportVariantSetRequest\x1a\x1d.google.longrunning.Operation"2\x82\xd3\xe4\x93\x02,"\'/v1/variantsets/{variant_set_id}:export:\x01*\x12\x83\x01\n\rGetVariantSet\x12(.google.genomics.v1.GetVariantSetRequest\x1a\x1e.google.genomics.v1.VariantSet"(\x82\xd3\xe4\x93\x02"\x12 /v1/variantsets/{variant_set_id}\x12\x93\x01\n\x11SearchVariantSets\x12,.google.genomics.v1.SearchVariantSetsRequest\x1a-.google.genomics.v1.SearchVariantSetsResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/v1/variantsets/search:\x01*\x12\x81\x01\n\x10DeleteVariantSet\x12+.google.genomics.v1.DeleteVariantSetRequest\x1a\x16.google.protobuf.Empty"(\x82\xd3\xe4\x93\x02"* /v1/variantsets/{variant_set_id}\x12\x96\x01\n\x10UpdateVariantSet\x12+.google.genomics.v1.UpdateVariantSetRequest\x1a\x1e.google.genomics.v1.VariantSet"5\x82\xd3\xe4\x93\x02/2 /v1/variantsets/{variant_set_id}:\x0bvariant_set\x12\x87\x01\n\x0eSearchVariants\x12).google.genomics.v1.SearchVariantsRequest\x1a*.google.genomics.v1.SearchVariantsResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants/search:\x01*\x12u\n\rCreateVariant\x12(.google.genomics.v1.CreateVariantRequest\x1a\x1b.google.genomics.v1.Variant"\x1d\x82\xd3\xe4\x93\x02\x17"\x0c/v1/variants:\x07variant\x12\x82\x01\n\rUpdateVariant\x12(.google.genomics.v1.UpdateVariantRequest\x1a\x1b.google.genomics.v1.Variant"*\x82\xd3\xe4\x93\x02$2\x19/v1/variants/{variant_id}:\x07variant\x12t\n\rDeleteVariant\x12(.google.genomics.v1.DeleteVariantRequest\x1a\x16.google.protobuf.Empty"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/variants/{variant_id}\x12s\n\nGetVariant\x12%.google.genomics.v1.GetVariantRequest\x1a\x1b.google.genomics.v1.Variant"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/variants/{variant_id}\x12p\n\rMergeVariants\x12(.google.genomics.v1.MergeVariantsRequest\x1a\x16.google.protobuf.Empty"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/v1/variants:merge:\x01*\x12\x87\x01\n\x0eSearchCallSets\x12).google.genomics.v1.SearchCallSetsRequest\x1a*.google.genomics.v1.SearchCallSetsResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1/callsets/search:\x01*\x12v\n\rCreateCallSet\x12(.google.genomics.v1.CreateCallSetRequest\x1a\x1b.google.genomics.v1.CallSet"\x1e\x82\xd3\xe4\x93\x02\x18"\x0c/v1/callsets:\x08call_set\x12\x84\x01\n\rUpdateCallSet\x12(.google.genomics.v1.UpdateCallSetRequest\x1a\x1b.google.genomics.v1.CallSet",\x82\xd3\xe4\x93\x02&2\x1a/v1/callsets/{call_set_id}:\x08call_set\x12u\n\rDeleteCallSet\x12(.google.genomics.v1.DeleteCallSetRequest\x1a\x16.google.protobuf.Empty""\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/callsets/{call_set_id}\x12t\n\nGetCallSet\x12%.google.genomics.v1.GetCallSetRequest\x1a\x1b.google.genomics.v1.CallSet""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/callsets/{call_set_id}Bh\n\x16com.google.genomics.v1B\rVariantsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.variants_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\rVariantsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_VARIANTSETMETADATA_INFOENTRY']._loaded_options = None
    _globals['_VARIANTSETMETADATA_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_VARIANT_INFOENTRY']._loaded_options = None
    _globals['_VARIANT_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_VARIANTCALL_INFOENTRY']._loaded_options = None
    _globals['_VARIANTCALL_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_CALLSET_INFOENTRY']._loaded_options = None
    _globals['_CALLSET_INFOENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTVARIANTSREQUEST_INFOMERGECONFIGENTRY']._loaded_options = None
    _globals['_IMPORTVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_MERGEVARIANTSREQUEST_INFOMERGECONFIGENTRY']._loaded_options = None
    _globals['_MERGEVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_STREAMINGVARIANTSERVICE'].methods_by_name['StreamVariants']._loaded_options = None
    _globals['_STREAMINGVARIANTSERVICE'].methods_by_name['StreamVariants']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants:stream:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['ImportVariants']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['ImportVariants']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants:import:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateVariantSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateVariantSet']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e"\x0f/v1/variantsets:\x0bvariant_set'
    _globals['_VARIANTSERVICEV1'].methods_by_name['ExportVariantSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['ExportVariantSet']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v1/variantsets/{variant_set_id}:export:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetVariantSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetVariantSet']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /v1/variantsets/{variant_set_id}'
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchVariantSets']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchVariantSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/v1/variantsets/search:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteVariantSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteVariantSet']._serialized_options = b'\x82\xd3\xe4\x93\x02"* /v1/variantsets/{variant_set_id}'
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateVariantSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateVariantSet']._serialized_options = b'\x82\xd3\xe4\x93\x02/2 /v1/variantsets/{variant_set_id}:\x0bvariant_set'
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchVariants']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchVariants']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1/variants/search:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateVariant']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateVariant']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x0c/v1/variants:\x07variant'
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateVariant']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateVariant']._serialized_options = b'\x82\xd3\xe4\x93\x02$2\x19/v1/variants/{variant_id}:\x07variant'
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteVariant']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteVariant']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b*\x19/v1/variants/{variant_id}'
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetVariant']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetVariant']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/variants/{variant_id}'
    _globals['_VARIANTSERVICEV1'].methods_by_name['MergeVariants']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['MergeVariants']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/v1/variants:merge:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchCallSets']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['SearchCallSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1/callsets/search:\x01*'
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateCallSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['CreateCallSet']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x0c/v1/callsets:\x08call_set'
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateCallSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['UpdateCallSet']._serialized_options = b'\x82\xd3\xe4\x93\x02&2\x1a/v1/callsets/{call_set_id}:\x08call_set'
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteCallSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['DeleteCallSet']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/callsets/{call_set_id}'
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetCallSet']._loaded_options = None
    _globals['_VARIANTSERVICEV1'].methods_by_name['GetCallSet']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/callsets/{call_set_id}'
    _globals['_INFOMERGEOPERATION']._serialized_start = 4646
    _globals['_INFOMERGEOPERATION']._serialized_end = 4739
    _globals['_VARIANTSETMETADATA']._serialized_start = 218
    _globals['_VARIANTSETMETADATA']._serialized_end = 602
    _globals['_VARIANTSETMETADATA_INFOENTRY']._serialized_start = 440
    _globals['_VARIANTSETMETADATA_INFOENTRY']._serialized_end = 511
    _globals['_VARIANTSETMETADATA_TYPE']._serialized_start = 513
    _globals['_VARIANTSETMETADATA_TYPE']._serialized_end = 602
    _globals['_VARIANTSET']._serialized_start = 605
    _globals['_VARIANTSET']._serialized_end = 830
    _globals['_VARIANT']._serialized_start = 833
    _globals['_VARIANT']._serialized_end = 1219
    _globals['_VARIANT_INFOENTRY']._serialized_start = 440
    _globals['_VARIANT_INFOENTRY']._serialized_end = 511
    _globals['_VARIANTCALL']._serialized_start = 1222
    _globals['_VARIANTCALL']._serialized_end = 1474
    _globals['_VARIANTCALL_INFOENTRY']._serialized_start = 440
    _globals['_VARIANTCALL_INFOENTRY']._serialized_end = 511
    _globals['_CALLSET']._serialized_start = 1477
    _globals['_CALLSET']._serialized_end = 1699
    _globals['_CALLSET_INFOENTRY']._serialized_start = 440
    _globals['_CALLSET_INFOENTRY']._serialized_end = 511
    _globals['_REFERENCEBOUND']._serialized_start = 1701
    _globals['_REFERENCEBOUND']._serialized_end = 1762
    _globals['_IMPORTVARIANTSREQUEST']._serialized_start = 1765
    _globals['_IMPORTVARIANTSREQUEST']._serialized_end = 2201
    _globals['_IMPORTVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_start = 2027
    _globals['_IMPORTVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_end = 2121
    _globals['_IMPORTVARIANTSREQUEST_FORMAT']._serialized_start = 2123
    _globals['_IMPORTVARIANTSREQUEST_FORMAT']._serialized_end = 2201
    _globals['_IMPORTVARIANTSRESPONSE']._serialized_start = 2203
    _globals['_IMPORTVARIANTSRESPONSE']._serialized_end = 2249
    _globals['_CREATEVARIANTSETREQUEST']._serialized_start = 2251
    _globals['_CREATEVARIANTSETREQUEST']._serialized_end = 2329
    _globals['_EXPORTVARIANTSETREQUEST']._serialized_start = 2332
    _globals['_EXPORTVARIANTSETREQUEST']._serialized_end = 2596
    _globals['_EXPORTVARIANTSETREQUEST_FORMAT']._serialized_start = 2543
    _globals['_EXPORTVARIANTSETREQUEST_FORMAT']._serialized_end = 2596
    _globals['_GETVARIANTSETREQUEST']._serialized_start = 2598
    _globals['_GETVARIANTSETREQUEST']._serialized_end = 2644
    _globals['_SEARCHVARIANTSETSREQUEST']._serialized_start = 2646
    _globals['_SEARCHVARIANTSETSREQUEST']._serialized_end = 2732
    _globals['_SEARCHVARIANTSETSRESPONSE']._serialized_start = 2734
    _globals['_SEARCHVARIANTSETSRESPONSE']._serialized_end = 2840
    _globals['_DELETEVARIANTSETREQUEST']._serialized_start = 2842
    _globals['_DELETEVARIANTSETREQUEST']._serialized_end = 2891
    _globals['_UPDATEVARIANTSETREQUEST']._serialized_start = 2894
    _globals['_UPDATEVARIANTSETREQUEST']._serialized_end = 3045
    _globals['_SEARCHVARIANTSREQUEST']._serialized_start = 3048
    _globals['_SEARCHVARIANTSREQUEST']._serialized_end = 3250
    _globals['_SEARCHVARIANTSRESPONSE']._serialized_start = 3252
    _globals['_SEARCHVARIANTSRESPONSE']._serialized_end = 3348
    _globals['_CREATEVARIANTREQUEST']._serialized_start = 3350
    _globals['_CREATEVARIANTREQUEST']._serialized_end = 3418
    _globals['_UPDATEVARIANTREQUEST']._serialized_start = 3421
    _globals['_UPDATEVARIANTREQUEST']._serialized_end = 3558
    _globals['_DELETEVARIANTREQUEST']._serialized_start = 3560
    _globals['_DELETEVARIANTREQUEST']._serialized_end = 3602
    _globals['_GETVARIANTREQUEST']._serialized_start = 3604
    _globals['_GETVARIANTREQUEST']._serialized_end = 3643
    _globals['_MERGEVARIANTSREQUEST']._serialized_start = 3646
    _globals['_MERGEVARIANTSREQUEST']._serialized_end = 3925
    _globals['_MERGEVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_start = 2027
    _globals['_MERGEVARIANTSREQUEST_INFOMERGECONFIGENTRY']._serialized_end = 2121
    _globals['_SEARCHCALLSETSREQUEST']._serialized_start = 3927
    _globals['_SEARCHCALLSETSREQUEST']._serialized_end = 4028
    _globals['_SEARCHCALLSETSRESPONSE']._serialized_start = 4030
    _globals['_SEARCHCALLSETSRESPONSE']._serialized_end = 4127
    _globals['_CREATECALLSETREQUEST']._serialized_start = 4129
    _globals['_CREATECALLSETREQUEST']._serialized_end = 4198
    _globals['_UPDATECALLSETREQUEST']._serialized_start = 4201
    _globals['_UPDATECALLSETREQUEST']._serialized_end = 4340
    _globals['_DELETECALLSETREQUEST']._serialized_start = 4342
    _globals['_DELETECALLSETREQUEST']._serialized_end = 4385
    _globals['_GETCALLSETREQUEST']._serialized_start = 4387
    _globals['_GETCALLSETREQUEST']._serialized_end = 4427
    _globals['_STREAMVARIANTSREQUEST']._serialized_start = 4430
    _globals['_STREAMVARIANTSREQUEST']._serialized_end = 4571
    _globals['_STREAMVARIANTSRESPONSE']._serialized_start = 4573
    _globals['_STREAMVARIANTSRESPONSE']._serialized_end = 4644
    _globals['_STREAMINGVARIANTSERVICE']._serialized_start = 4742
    _globals['_STREAMINGVARIANTSERVICE']._serialized_end = 4907
    _globals['_VARIANTSERVICEV1']._serialized_start = 4910
    _globals['_VARIANTSERVICEV1']._serialized_end = 7275