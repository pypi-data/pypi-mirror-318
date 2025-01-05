"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/mapsplatformdatasets/v1/maps_platform_datasets_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.maps.mapsplatformdatasets.v1 import dataset_pb2 as google_dot_maps_dot_mapsplatformdatasets_dot_v1_dot_dataset__pb2
from .....google.maps.mapsplatformdatasets.v1 import maps_platform_datasets_pb2 as google_dot_maps_dot_mapsplatformdatasets_dot_v1_dot_maps__platform__datasets__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/maps/mapsplatformdatasets/v1/maps_platform_datasets_service.proto\x12#google.maps.mapsplatformdatasets.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a1google/maps/mapsplatformdatasets/v1/dataset.proto\x1a@google/maps/mapsplatformdatasets/v1/maps_platform_datasets.proto\x1a\x1bgoogle/protobuf/empty.proto2\xe1\t\n\x14MapsPlatformDatasets\x12\xbc\x01\n\rCreateDataset\x129.google.maps.mapsplatformdatasets.v1.CreateDatasetRequest\x1a,.google.maps.mapsplatformdatasets.v1.Dataset"B\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02+" /v1/{parent=projects/*}/datasets:\x07dataset\x12\xd9\x01\n\x15UpdateDatasetMetadata\x12A.google.maps.mapsplatformdatasets.v1.UpdateDatasetMetadataRequest\x1a,.google.maps.mapsplatformdatasets.v1.Dataset"O\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x0232(/v1/{dataset.name=projects/*/datasets/*}:\x07dataset\x12\xa3\x01\n\nGetDataset\x126.google.maps.mapsplatformdatasets.v1.GetDatasetRequest\x1a,.google.maps.mapsplatformdatasets.v1.Dataset"/\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1/{name=projects/*/datasets/*}\x12\xdf\x01\n\x12FetchDatasetErrors\x12>.google.maps.mapsplatformdatasets.v1.FetchDatasetErrorsRequest\x1a?.google.maps.mapsplatformdatasets.v1.FetchDatasetErrorsResponse"H\xdaA\x07dataset\x82\xd3\xe4\x93\x028\x126/v1/{dataset=projects/*/datasets/*}:fetchDatasetErrors\x12\xb6\x01\n\x0cListDatasets\x128.google.maps.mapsplatformdatasets.v1.ListDatasetsRequest\x1a9.google.maps.mapsplatformdatasets.v1.ListDatasetsResponse"1\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v1/{parent=projects/*}/datasets\x12\x93\x01\n\rDeleteDataset\x129.google.maps.mapsplatformdatasets.v1.DeleteDatasetRequest\x1a\x16.google.protobuf.Empty"/\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1/{name=projects/*/datasets/*}\x1aW\xcaA#mapsplatformdatasets.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n\'com.google.maps.mapsplatformdatasets.v1B MapsPlatformDatasetsServiceProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xf8\x01\x01\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.mapsplatformdatasets.v1.maps_platform_datasets_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.mapsplatformdatasets.v1B MapsPlatformDatasetsServiceProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xf8\x01\x01\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1"
    _globals['_MAPSPLATFORMDATASETS']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS']._serialized_options = b'\xcaA#mapsplatformdatasets.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['CreateDataset']._serialized_options = b'\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02+" /v1/{parent=projects/*}/datasets:\x07dataset'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['UpdateDatasetMetadata']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['UpdateDatasetMetadata']._serialized_options = b'\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x0232(/v1/{dataset.name=projects/*/datasets/*}:\x07dataset'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['GetDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1/{name=projects/*/datasets/*}'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['FetchDatasetErrors']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['FetchDatasetErrors']._serialized_options = b'\xdaA\x07dataset\x82\xd3\xe4\x93\x028\x126/v1/{dataset=projects/*/datasets/*}:fetchDatasetErrors'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['ListDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02"\x12 /v1/{parent=projects/*}/datasets'
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_MAPSPLATFORMDATASETS'].methods_by_name['DeleteDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1/{name=projects/*/datasets/*}'
    _globals['_MAPSPLATFORMDATASETS']._serialized_start = 315
    _globals['_MAPSPLATFORMDATASETS']._serialized_end = 1564