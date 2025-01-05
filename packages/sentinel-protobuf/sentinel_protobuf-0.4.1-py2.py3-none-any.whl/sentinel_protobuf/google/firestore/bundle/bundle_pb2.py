"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/bundle/bundle.proto')
_sym_db = _symbol_database.Default()
from ....google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from ....google.firestore.v1 import query_pb2 as google_dot_firestore_dot_v1_dot_query__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/firestore/bundle/bundle.proto\x12\x17google.firestore.bundle\x1a"google/firestore/v1/document.proto\x1a\x1fgoogle/firestore/v1/query.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd5\x01\n\x0cBundledQuery\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x10structured_query\x18\x02 \x01(\x0b2$.google.firestore.v1.StructuredQueryH\x00\x12C\n\nlimit_type\x18\x03 \x01(\x0e2/.google.firestore.bundle.BundledQuery.LimitType" \n\tLimitType\x12\t\n\x05FIRST\x10\x00\x12\x08\n\x04LAST\x10\x01B\x0c\n\nquery_type"\x87\x01\n\nNamedQuery\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\rbundled_query\x18\x02 \x01(\x0b2%.google.firestore.bundle.BundledQuery\x12-\n\tread_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"w\n\x17BundledDocumentMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\tread_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06exists\x18\x03 \x01(\x08\x12\x0f\n\x07queries\x18\x04 \x03(\t"\x8c\x01\n\x0eBundleMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x03 \x01(\r\x12\x17\n\x0ftotal_documents\x18\x04 \x01(\r\x12\x13\n\x0btotal_bytes\x18\x05 \x01(\x04"\x9a\x02\n\rBundleElement\x12;\n\x08metadata\x18\x01 \x01(\x0b2\'.google.firestore.bundle.BundleMetadataH\x00\x12:\n\x0bnamed_query\x18\x02 \x01(\x0b2#.google.firestore.bundle.NamedQueryH\x00\x12M\n\x11document_metadata\x18\x03 \x01(\x0b20.google.firestore.bundle.BundledDocumentMetadataH\x00\x121\n\x08document\x18\x04 \x01(\x0b2\x1d.google.firestore.v1.DocumentH\x00B\x0e\n\x0celement_typeB\x92\x01\n\x1bcom.google.firestore.bundleB\x0bBundleProtoP\x01Z6cloud.google.com/go/firestore/bundle/bundlepb;bundlepb\xa2\x02\x05FSTPB\xaa\x02\x10Firestore.Bundle\xca\x02\x10Firestore\\Bundleb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.bundle.bundle_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.firestore.bundleB\x0bBundleProtoP\x01Z6cloud.google.com/go/firestore/bundle/bundlepb;bundlepb\xa2\x02\x05FSTPB\xaa\x02\x10Firestore.Bundle\xca\x02\x10Firestore\\Bundle'
    _globals['_BUNDLEDQUERY']._serialized_start = 168
    _globals['_BUNDLEDQUERY']._serialized_end = 381
    _globals['_BUNDLEDQUERY_LIMITTYPE']._serialized_start = 335
    _globals['_BUNDLEDQUERY_LIMITTYPE']._serialized_end = 367
    _globals['_NAMEDQUERY']._serialized_start = 384
    _globals['_NAMEDQUERY']._serialized_end = 519
    _globals['_BUNDLEDDOCUMENTMETADATA']._serialized_start = 521
    _globals['_BUNDLEDDOCUMENTMETADATA']._serialized_end = 640
    _globals['_BUNDLEMETADATA']._serialized_start = 643
    _globals['_BUNDLEMETADATA']._serialized_end = 783
    _globals['_BUNDLEELEMENT']._serialized_start = 786
    _globals['_BUNDLEELEMENT']._serialized_end = 1068