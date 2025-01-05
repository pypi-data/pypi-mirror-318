"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/admin/v1beta1/datastore_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/datastore/admin/v1beta1/datastore_admin.proto\x12\x1egoogle.datastore.admin.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x04\n\x0eCommonMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\x0eoperation_type\x18\x03 \x01(\x0e2-.google.datastore.admin.v1beta1.OperationType\x12J\n\x06labels\x18\x04 \x03(\x0b2:.google.datastore.admin.v1beta1.CommonMetadata.LabelsEntry\x12C\n\x05state\x18\x05 \x01(\x0e24.google.datastore.admin.v1beta1.CommonMetadata.State\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8b\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\x0e\n\nFINALIZING\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tCANCELLED\x10\x07":\n\x08Progress\x12\x16\n\x0ework_completed\x18\x01 \x01(\x03\x12\x16\n\x0ework_estimated\x18\x02 \x01(\x03"\x8d\x02\n\x15ExportEntitiesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12Q\n\x06labels\x18\x02 \x03(\x0b2A.google.datastore.admin.v1beta1.ExportEntitiesRequest.LabelsEntry\x12C\n\rentity_filter\x18\x03 \x01(\x0b2,.google.datastore.admin.v1beta1.EntityFilter\x12\x19\n\x11output_url_prefix\x18\x04 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x85\x02\n\x15ImportEntitiesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12Q\n\x06labels\x18\x02 \x03(\x0b2A.google.datastore.admin.v1beta1.ImportEntitiesRequest.LabelsEntry\x12\x11\n\tinput_url\x18\x03 \x01(\t\x12C\n\rentity_filter\x18\x04 \x01(\x0b2,.google.datastore.admin.v1beta1.EntityFilter\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01",\n\x16ExportEntitiesResponse\x12\x12\n\noutput_url\x18\x01 \x01(\t"\xbf\x02\n\x16ExportEntitiesMetadata\x12>\n\x06common\x18\x01 \x01(\x0b2..google.datastore.admin.v1beta1.CommonMetadata\x12C\n\x11progress_entities\x18\x02 \x01(\x0b2(.google.datastore.admin.v1beta1.Progress\x12@\n\x0eprogress_bytes\x18\x03 \x01(\x0b2(.google.datastore.admin.v1beta1.Progress\x12C\n\rentity_filter\x18\x04 \x01(\x0b2,.google.datastore.admin.v1beta1.EntityFilter\x12\x19\n\x11output_url_prefix\x18\x05 \x01(\t"\xb7\x02\n\x16ImportEntitiesMetadata\x12>\n\x06common\x18\x01 \x01(\x0b2..google.datastore.admin.v1beta1.CommonMetadata\x12C\n\x11progress_entities\x18\x02 \x01(\x0b2(.google.datastore.admin.v1beta1.Progress\x12@\n\x0eprogress_bytes\x18\x03 \x01(\x0b2(.google.datastore.admin.v1beta1.Progress\x12C\n\rentity_filter\x18\x04 \x01(\x0b2,.google.datastore.admin.v1beta1.EntityFilter\x12\x11\n\tinput_url\x18\x05 \x01(\t"4\n\x0cEntityFilter\x12\r\n\x05kinds\x18\x01 \x03(\t\x12\x15\n\rnamespace_ids\x18\x02 \x03(\t*Y\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fEXPORT_ENTITIES\x10\x01\x12\x13\n\x0fIMPORT_ENTITIES\x10\x022\xc6\x02\n\x0eDatastoreAdmin\x12\x98\x01\n\x0eExportEntities\x125.google.datastore.admin.v1beta1.ExportEntitiesRequest\x1a\x1d.google.longrunning.Operation"0\x82\xd3\xe4\x93\x02*"%/v1beta1/projects/{project_id}:export:\x01*\x12\x98\x01\n\x0eImportEntities\x125.google.datastore.admin.v1beta1.ImportEntitiesRequest\x1a\x1d.google.longrunning.Operation"0\x82\xd3\xe4\x93\x02*"%/v1beta1/projects/{project_id}:import:\x01*B\xcd\x01\n"com.google.datastore.admin.v1beta1B\x13DatastoreAdminProtoP\x01Z>cloud.google.com/go/datastore/admin/apiv1beta1/adminpb;adminpb\xaa\x02$Google.Cloud.Datastore.Admin.V1Beta1\xea\x02(Google::Cloud::Datastore::Admin::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.admin.v1beta1.datastore_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.datastore.admin.v1beta1B\x13DatastoreAdminProtoP\x01Z>cloud.google.com/go/datastore/admin/apiv1beta1/adminpb;adminpb\xaa\x02$Google.Cloud.Datastore.Admin.V1Beta1\xea\x02(Google::Cloud::Datastore::Admin::V1beta1'
    _globals['_COMMONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASTOREADMIN'].methods_by_name['ExportEntities']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['ExportEntities']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v1beta1/projects/{project_id}:export:\x01*'
    _globals['_DATASTOREADMIN'].methods_by_name['ImportEntities']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['ImportEntities']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v1beta1/projects/{project_id}:import:\x01*'
    _globals['_OPERATIONTYPE']._serialized_start = 2038
    _globals['_OPERATIONTYPE']._serialized_end = 2127
    _globals['_COMMONMETADATA']._serialized_start = 189
    _globals['_COMMONMETADATA']._serialized_end = 704
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_start = 517
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_end = 562
    _globals['_COMMONMETADATA_STATE']._serialized_start = 565
    _globals['_COMMONMETADATA_STATE']._serialized_end = 704
    _globals['_PROGRESS']._serialized_start = 706
    _globals['_PROGRESS']._serialized_end = 764
    _globals['_EXPORTENTITIESREQUEST']._serialized_start = 767
    _globals['_EXPORTENTITIESREQUEST']._serialized_end = 1036
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_start = 517
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_end = 562
    _globals['_IMPORTENTITIESREQUEST']._serialized_start = 1039
    _globals['_IMPORTENTITIESREQUEST']._serialized_end = 1300
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_start = 517
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_end = 562
    _globals['_EXPORTENTITIESRESPONSE']._serialized_start = 1302
    _globals['_EXPORTENTITIESRESPONSE']._serialized_end = 1346
    _globals['_EXPORTENTITIESMETADATA']._serialized_start = 1349
    _globals['_EXPORTENTITIESMETADATA']._serialized_end = 1668
    _globals['_IMPORTENTITIESMETADATA']._serialized_start = 1671
    _globals['_IMPORTENTITIESMETADATA']._serialized_end = 1982
    _globals['_ENTITYFILTER']._serialized_start = 1984
    _globals['_ENTITYFILTER']._serialized_end = 2036
    _globals['_DATASTOREADMIN']._serialized_start = 2130
    _globals['_DATASTOREADMIN']._serialized_end = 2456