"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/mapsplatformdatasets/v1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.maps.mapsplatformdatasets.v1 import data_source_pb2 as google_dot_maps_dot_mapsplatformdatasets_dot_v1_dot_data__source__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/maps/mapsplatformdatasets/v1/dataset.proto\x12#google.maps.mapsplatformdatasets.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/maps/mapsplatformdatasets/v1/data_source.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x05\n\x07Dataset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x12\n\nversion_id\x18\x04 \x01(\t\x129\n\x05usage\x18\x05 \x03(\x0e2*.google.maps.mapsplatformdatasets.v1.Usage\x12Q\n\x11local_file_source\x18\x06 \x01(\x0b24.google.maps.mapsplatformdatasets.v1.LocalFileSourceH\x00\x12D\n\ngcs_source\x18\x07 \x01(\x0b2..google.maps.mapsplatformdatasets.v1.GcsSourceH\x00\x12@\n\x06status\x18\x0c \x01(\x0b2+.google.maps.mapsplatformdatasets.v1.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x13version_create_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12 \n\x13version_description\x18\x0b \x01(\tB\x03\xe0A\x03:W\xeaAT\n+mapsplatformdatasets.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}B\r\n\x0bdata_source"\x8e\x03\n\x06Status\x12@\n\x05state\x18\x01 \x01(\x0e21.google.maps.mapsplatformdatasets.v1.Status.State\x12\x15\n\rerror_message\x18\x02 \x01(\t"\xaa\x02\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSTATE_IMPORTING\x10\x01\x12\x1a\n\x16STATE_IMPORT_SUCCEEDED\x10\x02\x12\x17\n\x13STATE_IMPORT_FAILED\x10\x03\x12\x12\n\x0eSTATE_DELETING\x10\x04\x12\x19\n\x15STATE_DELETION_FAILED\x10\x05\x12\x14\n\x10STATE_PROCESSING\x10\x06\x12\x1b\n\x17STATE_PROCESSING_FAILED\x10\x07\x12\x16\n\x12STATE_NEEDS_REVIEW\x10\x08\x12\x14\n\x10STATE_PUBLISHING\x10\t\x12\x1b\n\x17STATE_PUBLISHING_FAILED\x10\n\x12\x13\n\x0fSTATE_COMPLETED\x10\x0b*=\n\x05Usage\x12\x15\n\x11USAGE_UNSPECIFIED\x10\x00\x12\x1d\n\x19USAGE_DATA_DRIVEN_STYLING\x10\x01B\xef\x01\n\'com.google.maps.mapsplatformdatasets.v1B\x0cDatasetProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.mapsplatformdatasets.v1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.mapsplatformdatasets.v1B\x0cDatasetProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1"
    _globals['_DATASET'].fields_by_name['status']._loaded_options = None
    _globals['_DATASET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['version_create_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['version_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['version_description']._loaded_options = None
    _globals['_DATASET'].fields_by_name['version_description']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaAT\n+mapsplatformdatasets.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}'
    _globals['_USAGE']._serialized_start = 1314
    _globals['_USAGE']._serialized_end = 1375
    _globals['_DATASET']._serialized_start = 239
    _globals['_DATASET']._serialized_end = 911
    _globals['_STATUS']._serialized_start = 914
    _globals['_STATUS']._serialized_end = 1312
    _globals['_STATUS_STATE']._serialized_start = 1014
    _globals['_STATUS_STATE']._serialized_end = 1312