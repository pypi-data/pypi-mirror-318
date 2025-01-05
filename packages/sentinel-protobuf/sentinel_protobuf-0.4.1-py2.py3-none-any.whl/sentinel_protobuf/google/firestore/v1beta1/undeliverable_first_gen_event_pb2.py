"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1beta1/undeliverable_first_gen_event.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/firestore/v1beta1/undeliverable_first_gen_event.proto\x12\x18google.firestore.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\xdf\x03\n\x1aUndeliverableFirstGenEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12K\n\x06reason\x18\x02 \x01(\x0e2;.google.firestore.v1beta1.UndeliverableFirstGenEvent.Reason\x12\x15\n\rdocument_name\x18\x03 \x01(\t\x12e\n\x14document_change_type\x18\x04 \x01(\x0e2G.google.firestore.v1beta1.UndeliverableFirstGenEvent.DocumentChangeType\x12\x15\n\rfunction_name\x18\x05 \x03(\t\x122\n\x0etriggered_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp":\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x18\n\x14EXCEEDING_SIZE_LIMIT\x10\x01"^\n\x12DocumentChangeType\x12$\n DOCUMENT_CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06DELETE\x10\x02\x12\n\n\x06UPDATE\x10\x03B\xe9\x01\n\x1ccom.google.firestore.v1beta1B\x1fUndeliverableFirstGenEventProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1beta1.undeliverable_first_gen_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.firestore.v1beta1B\x1fUndeliverableFirstGenEventProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1'
    _globals['_UNDELIVERABLEFIRSTGENEVENT']._serialized_start = 124
    _globals['_UNDELIVERABLEFIRSTGENEVENT']._serialized_end = 603
    _globals['_UNDELIVERABLEFIRSTGENEVENT_REASON']._serialized_start = 449
    _globals['_UNDELIVERABLEFIRSTGENEVENT_REASON']._serialized_end = 507
    _globals['_UNDELIVERABLEFIRSTGENEVENT_DOCUMENTCHANGETYPE']._serialized_start = 509
    _globals['_UNDELIVERABLEFIRSTGENEVENT_DOCUMENTCHANGETYPE']._serialized_end = 603