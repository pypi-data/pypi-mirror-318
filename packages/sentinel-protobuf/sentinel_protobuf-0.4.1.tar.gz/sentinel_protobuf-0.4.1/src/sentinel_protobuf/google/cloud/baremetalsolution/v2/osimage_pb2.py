"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/osimage.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/baremetalsolution/v2/osimage.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x02\n\x07OSImage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0c\n\x04code\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12!\n\x19applicable_instance_types\x18\x04 \x03(\t\x12#\n\x1bsupported_network_templates\x18\x05 \x03(\t:}\xeaAz\n(baremetalsolution.googleapis.com/OsImage\x12;projects/{project}/locations/{location}/osImages/{os_image}*\x08osImages2\x07osImage"w\n\x13ListOSImagesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"n\n\x14ListOSImagesResponse\x12=\n\tos_images\x18\x01 \x03(\x0b2*.google.cloud.baremetalsolution.v2.OSImage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB\xfb\x01\n%com.google.cloud.baremetalsolution.v2B\x0cOsImageProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.osimage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x0cOsImageProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_OSIMAGE'].fields_by_name['name']._loaded_options = None
    _globals['_OSIMAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_OSIMAGE']._loaded_options = None
    _globals['_OSIMAGE']._serialized_options = b'\xeaAz\n(baremetalsolution.googleapis.com/OsImage\x12;projects/{project}/locations/{location}/osImages/{os_image}*\x08osImages2\x07osImage'
    _globals['_LISTOSIMAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOSIMAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_OSIMAGE']._serialized_start = 147
    _globals['_OSIMAGE']._serialized_end = 409
    _globals['_LISTOSIMAGESREQUEST']._serialized_start = 411
    _globals['_LISTOSIMAGESREQUEST']._serialized_end = 530
    _globals['_LISTOSIMAGESRESPONSE']._serialized_start = 532
    _globals['_LISTOSIMAGESRESPONSE']._serialized_end = 642