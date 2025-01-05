"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.documentai.v1beta3 import document_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__pb2
from .....google.cloud.documentai.v1beta3 import document_io_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__io__pb2
from .....google.cloud.documentai.v1beta3 import document_schema_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__schema__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/documentai/v1beta3/dataset.proto\x12\x1fgoogle.cloud.documentai.v1beta3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/documentai/v1beta3/document.proto\x1a1google/cloud/documentai/v1beta3/document_io.proto\x1a5google/cloud/documentai/v1beta3/document_schema.proto"\x9c\x08\n\x07Dataset\x12\\\n\x12gcs_managed_config\x18\x03 \x01(\x0b29.google.cloud.documentai.v1beta3.Dataset.GCSManagedConfigB\x03\xe0A\x01H\x00\x12l\n\x19document_warehouse_config\x18\x05 \x01(\x0b2@.google.cloud.documentai.v1beta3.Dataset.DocumentWarehouseConfigB\x05\x18\x01\xe0A\x01H\x00\x12h\n\x18unmanaged_dataset_config\x18\x06 \x01(\x0b2?.google.cloud.documentai.v1beta3.Dataset.UnmanagedDatasetConfigB\x03\xe0A\x01H\x00\x12f\n\x17spanner_indexing_config\x18\x04 \x01(\x0b2>.google.cloud.documentai.v1beta3.Dataset.SpannerIndexingConfigB\x03\xe0A\x01H\x01\x12\x0c\n\x04name\x18\x01 \x01(\t\x12B\n\x05state\x18\x02 \x01(\x0e2..google.cloud.documentai.v1beta3.Dataset.StateB\x03\xe0A\x02\x12\x1a\n\rsatisfies_pzs\x18\x08 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\t \x01(\x08B\x03\xe0A\x03\x1aW\n\x10GCSManagedConfig\x12C\n\ngcs_prefix\x18\x01 \x01(\x0b2*.google.cloud.documentai.v1beta3.GcsPrefixB\x03\xe0A\x02\x1ar\n\x17DocumentWarehouseConfig\x12\x17\n\ncollection\x18\x01 \x01(\tB\x03\xe0A\x03\x12>\n\x06schema\x18\x02 \x01(\tB.\xe0A\x03\xfaA(\n&contentwarehouse.googleapis.com/Schema\x1a\x18\n\x16UnmanagedDatasetConfig\x1a\x17\n\x15SpannerIndexingConfig"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x11\n\rUNINITIALIZED\x10\x01\x12\x10\n\x0cINITIALIZING\x10\x02\x12\x0f\n\x0bINITIALIZED\x10\x03:n\xeaAk\n!documentai.googleapis.com/Dataset\x12Fprojects/{project}/locations/{location}/processors/{processor}/datasetB\x10\n\x0estorage_sourceB\x11\n\x0findexing_source"\x86\x03\n\nDocumentId\x12^\n\x12gcs_managed_doc_id\x18\x01 \x01(\x0b2@.google.cloud.documentai.v1beta3.DocumentId.GCSManagedDocumentIdH\x00\x12[\n\x10unmanaged_doc_id\x18\x04 \x01(\x0b2?.google.cloud.documentai.v1beta3.DocumentId.UnmanagedDocumentIdH\x00\x12B\n\x0crevision_ref\x18\x03 \x01(\x0b2,.google.cloud.documentai.v1beta3.RevisionRef\x1aC\n\x14GCSManagedDocumentId\x12\x14\n\x07gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\tcw_doc_id\x18\x02 \x01(\tB\x02\x18\x01\x1a*\n\x13UnmanagedDocumentId\x12\x13\n\x06doc_id\x18\x01 \x01(\tB\x03\xe0A\x02B\x06\n\x04type"\xa9\x02\n\rDatasetSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x0fdocument_schema\x18\x03 \x01(\x0b2/.google.cloud.documentai.v1beta3.DocumentSchemaB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x05 \x01(\x08B\x03\xe0A\x03:\x82\x01\xeaA\x7f\n\'documentai.googleapis.com/DatasetSchema\x12Tprojects/{project}/locations/{location}/processors/{processor}/dataset/datasetSchema"\x87\x02\n\x15BatchDatasetDocuments\x12o\n\x17individual_document_ids\x18\x01 \x01(\x0b2L.google.cloud.documentai.v1beta3.BatchDatasetDocuments.IndividualDocumentIdsH\x00\x12\x10\n\x06filter\x18\x02 \x01(\tH\x00\x1a_\n\x15IndividualDocumentIds\x12F\n\x0cdocument_ids\x18\x01 \x03(\x0b2+.google.cloud.documentai.v1beta3.DocumentIdB\x03\xe0A\x02B\n\n\x08criteriaB\xc8\x02\n#com.google.cloud.documentai.v1beta3B\x0cDatasetProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3\xeaAb\n&contentwarehouse.googleapis.com/Schema\x128projects/{project}/locations/{location}/schemas/{schema}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x0cDatasetProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3\xeaAb\n&contentwarehouse.googleapis.com/Schema\x128projects/{project}/locations/{location}/schemas/{schema}'
    _globals['_DATASET_GCSMANAGEDCONFIG'].fields_by_name['gcs_prefix']._loaded_options = None
    _globals['_DATASET_GCSMANAGEDCONFIG'].fields_by_name['gcs_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG'].fields_by_name['collection']._loaded_options = None
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG'].fields_by_name['collection']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG'].fields_by_name['schema']._loaded_options = None
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG'].fields_by_name['schema']._serialized_options = b'\xe0A\x03\xfaA(\n&contentwarehouse.googleapis.com/Schema'
    _globals['_DATASET'].fields_by_name['gcs_managed_config']._loaded_options = None
    _globals['_DATASET'].fields_by_name['gcs_managed_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['document_warehouse_config']._loaded_options = None
    _globals['_DATASET'].fields_by_name['document_warehouse_config']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_DATASET'].fields_by_name['unmanaged_dataset_config']._loaded_options = None
    _globals['_DATASET'].fields_by_name['unmanaged_dataset_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['spanner_indexing_config']._loaded_options = None
    _globals['_DATASET'].fields_by_name['spanner_indexing_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['state']._loaded_options = None
    _globals['_DATASET'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaAk\n!documentai.googleapis.com/Dataset\x12Fprojects/{project}/locations/{location}/processors/{processor}/dataset'
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID'].fields_by_name['cw_doc_id']._loaded_options = None
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID'].fields_by_name['cw_doc_id']._serialized_options = b'\x18\x01'
    _globals['_DOCUMENTID_UNMANAGEDDOCUMENTID'].fields_by_name['doc_id']._loaded_options = None
    _globals['_DOCUMENTID_UNMANAGEDDOCUMENTID'].fields_by_name['doc_id']._serialized_options = b'\xe0A\x02'
    _globals['_DATASETSCHEMA'].fields_by_name['document_schema']._loaded_options = None
    _globals['_DATASETSCHEMA'].fields_by_name['document_schema']._serialized_options = b'\xe0A\x01'
    _globals['_DATASETSCHEMA'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATASETSCHEMA'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETSCHEMA'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATASETSCHEMA'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETSCHEMA']._loaded_options = None
    _globals['_DATASETSCHEMA']._serialized_options = b"\xeaA\x7f\n'documentai.googleapis.com/DatasetSchema\x12Tprojects/{project}/locations/{location}/processors/{processor}/dataset/datasetSchema"
    _globals['_BATCHDATASETDOCUMENTS_INDIVIDUALDOCUMENTIDS'].fields_by_name['document_ids']._loaded_options = None
    _globals['_BATCHDATASETDOCUMENTS_INDIVIDUALDOCUMENTIDS'].fields_by_name['document_ids']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET']._serialized_start = 297
    _globals['_DATASET']._serialized_end = 1349
    _globals['_DATASET_GCSMANAGEDCONFIG']._serialized_start = 860
    _globals['_DATASET_GCSMANAGEDCONFIG']._serialized_end = 947
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG']._serialized_start = 949
    _globals['_DATASET_DOCUMENTWAREHOUSECONFIG']._serialized_end = 1063
    _globals['_DATASET_UNMANAGEDDATASETCONFIG']._serialized_start = 1065
    _globals['_DATASET_UNMANAGEDDATASETCONFIG']._serialized_end = 1089
    _globals['_DATASET_SPANNERINDEXINGCONFIG']._serialized_start = 1091
    _globals['_DATASET_SPANNERINDEXINGCONFIG']._serialized_end = 1114
    _globals['_DATASET_STATE']._serialized_start = 1116
    _globals['_DATASET_STATE']._serialized_end = 1200
    _globals['_DOCUMENTID']._serialized_start = 1352
    _globals['_DOCUMENTID']._serialized_end = 1742
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID']._serialized_start = 1623
    _globals['_DOCUMENTID_GCSMANAGEDDOCUMENTID']._serialized_end = 1690
    _globals['_DOCUMENTID_UNMANAGEDDOCUMENTID']._serialized_start = 1692
    _globals['_DOCUMENTID_UNMANAGEDDOCUMENTID']._serialized_end = 1734
    _globals['_DATASETSCHEMA']._serialized_start = 1745
    _globals['_DATASETSCHEMA']._serialized_end = 2042
    _globals['_BATCHDATASETDOCUMENTS']._serialized_start = 2045
    _globals['_BATCHDATASETDOCUMENTS']._serialized_end = 2308
    _globals['_BATCHDATASETDOCUMENTS_INDIVIDUALDOCUMENTIDS']._serialized_start = 2201
    _globals['_BATCHDATASETDOCUMENTS_INDIVIDUALDOCUMENTIDS']._serialized_end = 2296