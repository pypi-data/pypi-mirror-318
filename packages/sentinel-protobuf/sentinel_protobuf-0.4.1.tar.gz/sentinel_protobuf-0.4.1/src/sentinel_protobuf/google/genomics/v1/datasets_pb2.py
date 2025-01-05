"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1/datasets.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/genomics/v1/datasets.proto\x12\x12google.genomics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"h\n\x07Dataset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"P\n\x13ListDatasetsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"^\n\x14ListDatasetsResponse\x12-\n\x08datasets\x18\x01 \x03(\x0b2\x1b.google.genomics.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"D\n\x14CreateDatasetRequest\x12,\n\x07dataset\x18\x01 \x01(\x0b2\x1b.google.genomics.v1.Dataset"\x89\x01\n\x14UpdateDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12,\n\x07dataset\x18\x02 \x01(\x0b2\x1b.google.genomics.v1.Dataset\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"*\n\x14DeleteDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t",\n\x16UndeleteDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t"\'\n\x11GetDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t2\x9f\t\n\x10DatasetServiceV1\x12w\n\x0cListDatasets\x12\'.google.genomics.v1.ListDatasetsRequest\x1a(.google.genomics.v1.ListDatasetsResponse"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/datasets\x12u\n\rCreateDataset\x12(.google.genomics.v1.CreateDatasetRequest\x1a\x1b.google.genomics.v1.Dataset"\x1d\x82\xd3\xe4\x93\x02\x17"\x0c/v1/datasets:\x07dataset\x12s\n\nGetDataset\x12%.google.genomics.v1.GetDatasetRequest\x1a\x1b.google.genomics.v1.Dataset"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/datasets/{dataset_id}\x12\x82\x01\n\rUpdateDataset\x12(.google.genomics.v1.UpdateDatasetRequest\x1a\x1b.google.genomics.v1.Dataset"*\x82\xd3\xe4\x93\x02$2\x19/v1/datasets/{dataset_id}:\x07dataset\x12t\n\rDeleteDataset\x12(.google.genomics.v1.DeleteDatasetRequest\x1a\x16.google.protobuf.Empty"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/datasets/{dataset_id}\x12\x89\x01\n\x0fUndeleteDataset\x12*.google.genomics.v1.UndeleteDatasetRequest\x1a\x1b.google.genomics.v1.Dataset"-\x82\xd3\xe4\x93\x02\'""/v1/datasets/{dataset_id}:undelete:\x01*\x12|\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"1\x82\xd3\xe4\x93\x02+"&/v1/{resource=datasets/*}:setIamPolicy:\x01*\x12|\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"1\x82\xd3\xe4\x93\x02+"&/v1/{resource=datasets/*}:getIamPolicy:\x01*\x12\xa2\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"7\x82\xd3\xe4\x93\x021",/v1/{resource=datasets/*}:testIamPermissions:\x01*Bh\n\x16com.google.genomics.v1B\rDatasetsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1.datasets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.genomics.v1B\rDatasetsProtoP\x01Z:google.golang.org/genproto/googleapis/genomics/v1;genomics\xf8\x01\x01'
    _globals['_DATASETSERVICEV1'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['ListDatasets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/datasets'
    _globals['_DATASETSERVICEV1'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['CreateDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x0c/v1/datasets:\x07dataset'
    _globals['_DATASETSERVICEV1'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['GetDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/datasets/{dataset_id}'
    _globals['_DATASETSERVICEV1'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['UpdateDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02$2\x19/v1/datasets/{dataset_id}:\x07dataset'
    _globals['_DATASETSERVICEV1'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['DeleteDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b*\x19/v1/datasets/{dataset_id}'
    _globals['_DATASETSERVICEV1'].methods_by_name['UndeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['UndeleteDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/v1/datasets/{dataset_id}:undelete:\x01*'
    _globals['_DATASETSERVICEV1'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02+"&/v1/{resource=datasets/*}:setIamPolicy:\x01*'
    _globals['_DATASETSERVICEV1'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02+"&/v1/{resource=datasets/*}:getIamPolicy:\x01*'
    _globals['_DATASETSERVICEV1'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATASETSERVICEV1'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1/{resource=datasets/*}:testIamPermissions:\x01*'
    _globals['_DATASET']._serialized_start = 243
    _globals['_DATASET']._serialized_end = 347
    _globals['_LISTDATASETSREQUEST']._serialized_start = 349
    _globals['_LISTDATASETSREQUEST']._serialized_end = 429
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 431
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 525
    _globals['_CREATEDATASETREQUEST']._serialized_start = 527
    _globals['_CREATEDATASETREQUEST']._serialized_end = 595
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 598
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 735
    _globals['_DELETEDATASETREQUEST']._serialized_start = 737
    _globals['_DELETEDATASETREQUEST']._serialized_end = 779
    _globals['_UNDELETEDATASETREQUEST']._serialized_start = 781
    _globals['_UNDELETEDATASETREQUEST']._serialized_end = 825
    _globals['_GETDATASETREQUEST']._serialized_start = 827
    _globals['_GETDATASETREQUEST']._serialized_end = 866
    _globals['_DATASETSERVICEV1']._serialized_start = 869
    _globals['_DATASETSERVICEV1']._serialized_end = 2052