"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/mapsplatformdatasets/v1/maps_platform_datasets.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.mapsplatformdatasets.v1 import dataset_pb2 as google_dot_maps_dot_mapsplatformdatasets_dot_v1_dot_dataset__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/maps/mapsplatformdatasets/v1/maps_platform_datasets.proto\x12#google.maps.mapsplatformdatasets.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/maps/mapsplatformdatasets/v1/dataset.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9f\x01\n\x14CreateDatasetRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12B\n\x07dataset\x18\x02 \x01(\x0b2,.google.maps.mapsplatformdatasets.v1.DatasetB\x03\xe0A\x02"\x93\x01\n\x1cUpdateDatasetMetadataRequest\x12B\n\x07dataset\x18\x01 \x01(\x0b2,.google.maps.mapsplatformdatasets.v1.DatasetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"V\n\x11GetDatasetRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/Dataset"\x8e\x01\n\x13ListDatasetsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x04 \x01(\t"o\n\x14ListDatasetsResponse\x12>\n\x08datasets\x18\x01 \x03(\x0b2,.google.maps.mapsplatformdatasets.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x01\n\x19FetchDatasetErrorsRequest\x12D\n\x07dataset\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/Dataset\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"Y\n\x1aFetchDatasetErrorsResponse\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12"\n\x06errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status"Y\n\x14DeleteDatasetRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/DatasetB\xfc\x01\n\'com.google.maps.mapsplatformdatasets.v1B\x19MapsPlatformDatasetsProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.mapsplatformdatasets.v1.maps_platform_datasets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.mapsplatformdatasets.v1B\x19MapsPlatformDatasetsProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1"
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETMETADATAREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETMETADATAREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/Dataset'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_FETCHDATASETERRORSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_FETCHDATASETERRORSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/Dataset'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+mapsplatformdatasets.googleapis.com/Dataset'
    _globals['_CREATEDATASETREQUEST']._serialized_start = 276
    _globals['_CREATEDATASETREQUEST']._serialized_end = 435
    _globals['_UPDATEDATASETMETADATAREQUEST']._serialized_start = 438
    _globals['_UPDATEDATASETMETADATAREQUEST']._serialized_end = 585
    _globals['_GETDATASETREQUEST']._serialized_start = 587
    _globals['_GETDATASETREQUEST']._serialized_end = 673
    _globals['_LISTDATASETSREQUEST']._serialized_start = 676
    _globals['_LISTDATASETSREQUEST']._serialized_end = 818
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 820
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 931
    _globals['_FETCHDATASETERRORSREQUEST']._serialized_start = 934
    _globals['_FETCHDATASETERRORSREQUEST']._serialized_end = 1070
    _globals['_FETCHDATASETERRORSRESPONSE']._serialized_start = 1072
    _globals['_FETCHDATASETERRORSRESPONSE']._serialized_end = 1161
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1163
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1252