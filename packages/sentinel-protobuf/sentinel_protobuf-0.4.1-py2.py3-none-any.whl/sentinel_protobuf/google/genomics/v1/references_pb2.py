"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/references.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/genomics/v1/references.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto"\x90\x01\n\tReference\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x03\x12\x13\n\x0bmd5checksum\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12\x19\n\x11source_accessions\x18\x06 \x03(\t\x12\x15\n\rncbi_taxon_id\x18\x07 \x01(\x05"\xb6\x01\n\x0cReferenceSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rreference_ids\x18\x02 \x03(\t\x12\x13\n\x0bmd5checksum\x18\x03 \x01(\t\x12\x15\n\rncbi_taxon_id\x18\x04 \x01(\x05\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x13\n\x0bassembly_id\x18\x06 \x01(\t\x12\x12\n\nsource_uri\x18\x07 \x01(\t\x12\x19\n\x11source_accessions\x18\x08 \x03(\t"\x82\x01\n\x1aSearchReferenceSetsRequest\x12\x14\n\x0cmd5checksums\x18\x01 \x03(\t\x12\x12\n\naccessions\x18\x02 \x03(\t\x12\x13\n\x0bassembly_id\x18\x03 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05"p\n\x1bSearchReferenceSetsResponse\x128\n\x0ereference_sets\x18\x01 \x03(\x0b2 .google.genomics.v1.ReferenceSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"2\n\x16GetReferenceSetRequest\x12\x18\n\x10reference_set_id\x18\x01 \x01(\t"\x84\x01\n\x17SearchReferencesRequest\x12\x14\n\x0cmd5checksums\x18\x01 \x03(\t\x12\x12\n\naccessions\x18\x02 \x03(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05"f\n\x18SearchReferencesResponse\x121\n\nreferences\x18\x01 \x03(\x0b2\x1d.google.genomics.v1.Reference\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"+\n\x13GetReferenceRequest\x12\x14\n\x0creference_id\x18\x01 \x01(\t"k\n\x10ListBasesRequest\x12\x14\n\x0creference_id\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03end\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05"N\n\x11ListBasesResponse\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x10\n\x08sequence\x18\x02 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t2\xdb\x05\n\x12ReferenceServiceV1\x12\x9b\x01\n\x13SearchReferenceSets\x12..google.genomics.v1.SearchReferenceSetsRequest\x1a/.google.genomics.v1.SearchReferenceSetsResponse"#\x82\xd3\xe4\x93\x02\x1d"\x18/v1/referencesets/search:\x01*\x12\x8d\x01\n\x0fGetReferenceSet\x12*.google.genomics.v1.GetReferenceSetRequest\x1a .google.genomics.v1.ReferenceSet",\x82\xd3\xe4\x93\x02&\x12$/v1/referencesets/{reference_set_id}\x12\x8f\x01\n\x10SearchReferences\x12+.google.genomics.v1.SearchReferencesRequest\x1a,.google.genomics.v1.SearchReferencesResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/v1/references/search:\x01*\x12}\n\x0cGetReference\x12\'.google.genomics.v1.GetReferenceRequest\x1a\x1d.google.genomics.v1.Reference"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/references/{reference_id}\x12\x85\x01\n\tListBases\x12$.google.genomics.v1.ListBasesRequest\x1a%.google.genomics.v1.ListBasesResponse"+\x82\xd3\xe4\x93\x02%\x12#/v1/references/{reference_id}/basesBj\n\x16com.google.genomics.v1B\x0fReferencesProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.references_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\x0fReferencesProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_REFERENCESERVICEV1'].methods_by_name['SearchReferenceSets']._loaded_options = None
    _globals['_REFERENCESERVICEV1'].methods_by_name['SearchReferenceSets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x18/v1/referencesets/search:\x01*'
    _globals['_REFERENCESERVICEV1'].methods_by_name['GetReferenceSet']._loaded_options = None
    _globals['_REFERENCESERVICEV1'].methods_by_name['GetReferenceSet']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/v1/referencesets/{reference_set_id}'
    _globals['_REFERENCESERVICEV1'].methods_by_name['SearchReferences']._loaded_options = None
    _globals['_REFERENCESERVICEV1'].methods_by_name['SearchReferences']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/v1/references/search:\x01*'
    _globals['_REFERENCESERVICEV1'].methods_by_name['GetReference']._loaded_options = None
    _globals['_REFERENCESERVICEV1'].methods_by_name['GetReference']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/references/{reference_id}'
    _globals['_REFERENCESERVICEV1'].methods_by_name['ListBases']._loaded_options = None
    _globals['_REFERENCESERVICEV1'].methods_by_name['ListBases']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/v1/references/{reference_id}/bases'
    _globals['_REFERENCE']._serialized_start = 90
    _globals['_REFERENCE']._serialized_end = 234
    _globals['_REFERENCESET']._serialized_start = 237
    _globals['_REFERENCESET']._serialized_end = 419
    _globals['_SEARCHREFERENCESETSREQUEST']._serialized_start = 422
    _globals['_SEARCHREFERENCESETSREQUEST']._serialized_end = 552
    _globals['_SEARCHREFERENCESETSRESPONSE']._serialized_start = 554
    _globals['_SEARCHREFERENCESETSRESPONSE']._serialized_end = 666
    _globals['_GETREFERENCESETREQUEST']._serialized_start = 668
    _globals['_GETREFERENCESETREQUEST']._serialized_end = 718
    _globals['_SEARCHREFERENCESREQUEST']._serialized_start = 721
    _globals['_SEARCHREFERENCESREQUEST']._serialized_end = 853
    _globals['_SEARCHREFERENCESRESPONSE']._serialized_start = 855
    _globals['_SEARCHREFERENCESRESPONSE']._serialized_end = 957
    _globals['_GETREFERENCEREQUEST']._serialized_start = 959
    _globals['_GETREFERENCEREQUEST']._serialized_end = 1002
    _globals['_LISTBASESREQUEST']._serialized_start = 1004
    _globals['_LISTBASESREQUEST']._serialized_end = 1111
    _globals['_LISTBASESRESPONSE']._serialized_start = 1113
    _globals['_LISTBASESRESPONSE']._serialized_end = 1191
    _globals['_REFERENCESERVICEV1']._serialized_start = 1194
    _globals['_REFERENCESERVICEV1']._serialized_end = 1925