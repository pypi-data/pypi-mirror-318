"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta2/operation.proto')
_sym_db = _symbol_database.Default()
from .....google.firestore.admin.v1beta2 import index_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/firestore/admin/v1beta2/operation.proto\x12\x1egoogle.firestore.admin.v1beta2\x1a*google/firestore/admin/v1beta2/index.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\xcc\x02\n\x16IndexOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05index\x18\x03 \x01(\t\x12=\n\x05state\x18\x04 \x01(\x0e2..google.firestore.admin.v1beta2.OperationState\x12D\n\x12progress_documents\x18\x05 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12@\n\x0eprogress_bytes\x18\x06 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress"\xa5\x05\n\x16FieldOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05field\x18\x03 \x01(\t\x12d\n\x13index_config_deltas\x18\x04 \x03(\x0b2G.google.firestore.admin.v1beta2.FieldOperationMetadata.IndexConfigDelta\x12=\n\x05state\x18\x05 \x01(\x0e2..google.firestore.admin.v1beta2.OperationState\x12C\n\x11document_progress\x18\x06 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12@\n\x0ebytes_progress\x18\x07 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x1a\xf1\x01\n\x10IndexConfigDelta\x12g\n\x0bchange_type\x18\x01 \x01(\x0e2R.google.firestore.admin.v1beta2.FieldOperationMetadata.IndexConfigDelta.ChangeType\x124\n\x05index\x18\x02 \x01(\x0b2%.google.firestore.admin.v1beta2.Index">\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02"\xfb\x02\n\x17ExportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0foperation_state\x18\x03 \x01(\x0e2..google.firestore.admin.v1beta2.OperationState\x12D\n\x12progress_documents\x18\x04 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12@\n\x0eprogress_bytes\x18\x05 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x07 \x01(\t"\xfa\x02\n\x17ImportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0foperation_state\x18\x03 \x01(\x0e2..google.firestore.admin.v1beta2.OperationState\x12D\n\x12progress_documents\x18\x04 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12@\n\x0eprogress_bytes\x18\x05 \x01(\x0b2(.google.firestore.admin.v1beta2.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x07 \x01(\t"4\n\x17ExportDocumentsResponse\x12\x19\n\x11output_uri_prefix\x18\x01 \x01(\t":\n\x08Progress\x12\x16\n\x0eestimated_work\x18\x01 \x01(\x03\x12\x16\n\x0ecompleted_work\x18\x02 \x01(\x03*\x9e\x01\n\x0eOperationState\x12\x1f\n\x1bOPERATION_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\x0e\n\nFINALIZING\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tCANCELLED\x10\x07B\xa4\x01\n"com.google.firestore.admin.v1beta2B\x0eOperationProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta2.operation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta2B\x0eOperationProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2'
    _globals['_OPERATIONSTATE']._serialized_start = 2082
    _globals['_OPERATIONSTATE']._serialized_end = 2240
    _globals['_INDEXOPERATIONMETADATA']._serialized_start = 190
    _globals['_INDEXOPERATIONMETADATA']._serialized_end = 522
    _globals['_FIELDOPERATIONMETADATA']._serialized_start = 525
    _globals['_FIELDOPERATIONMETADATA']._serialized_end = 1202
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA']._serialized_start = 961
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA']._serialized_end = 1202
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA_CHANGETYPE']._serialized_start = 1140
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA_CHANGETYPE']._serialized_end = 1202
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_start = 1205
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_end = 1584
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 1587
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 1965
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_start = 1967
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_end = 2019
    _globals['_PROGRESS']._serialized_start = 2021
    _globals['_PROGRESS']._serialized_end = 2079