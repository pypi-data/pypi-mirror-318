"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/mapsplatformdatasets/v1/data_source.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/maps/mapsplatformdatasets/v1/data_source.proto\x12#google.maps.mapsplatformdatasets.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"i\n\x0fLocalFileSource\x12\x10\n\x08filename\x18\x01 \x01(\t\x12D\n\x0bfile_format\x18\x02 \x01(\x0e2/.google.maps.mapsplatformdatasets.v1.FileFormat"d\n\tGcsSource\x12\x11\n\tinput_uri\x18\x01 \x01(\t\x12D\n\x0bfile_format\x18\x02 \x01(\x0e2/.google.maps.mapsplatformdatasets.v1.FileFormat*l\n\nFileFormat\x12\x1b\n\x17FILE_FORMAT_UNSPECIFIED\x10\x00\x12\x17\n\x13FILE_FORMAT_GEOJSON\x10\x01\x12\x13\n\x0fFILE_FORMAT_KML\x10\x02\x12\x13\n\x0fFILE_FORMAT_CSV\x10\x03B\xf2\x01\n\'com.google.maps.mapsplatformdatasets.v1B\x0fDataSourceProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.mapsplatformdatasets.v1.data_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.maps.mapsplatformdatasets.v1B\x0fDataSourceProtoP\x01Zacloud.google.com/go/maps/mapsplatformdatasets/apiv1/mapsplatformdatasetspb;mapsplatformdatasetspb\xa2\x02\x04MDV1\xaa\x02#Google.Maps.MapsPlatformDatasets.V1\xca\x02#Google\\Maps\\MapsPlatformDatasets\\V1"
    _globals['_FILEFORMAT']._serialized_start = 363
    _globals['_FILEFORMAT']._serialized_end = 471
    _globals['_LOCALFILESOURCE']._serialized_start = 154
    _globals['_LOCALFILESOURCE']._serialized_end = 259
    _globals['_GCSSOURCE']._serialized_start = 261
    _globals['_GCSSOURCE']._serialized_end = 361