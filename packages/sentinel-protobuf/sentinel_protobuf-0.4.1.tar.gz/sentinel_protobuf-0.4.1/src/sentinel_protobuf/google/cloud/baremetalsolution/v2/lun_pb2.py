"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/lun.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/baremetalsolution/v2/lun.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x06\n\x03Lun\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\n \x01(\t\x12;\n\x05state\x18\x02 \x01(\x0e2,.google.cloud.baremetalsolution.v2.Lun.State\x12\x0f\n\x07size_gb\x18\x03 \x01(\x03\x12T\n\x12multiprotocol_type\x18\x04 \x01(\x0e28.google.cloud.baremetalsolution.v2.Lun.MultiprotocolType\x12D\n\x0estorage_volume\x18\x05 \x01(\tB,\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12\x11\n\tshareable\x18\x06 \x01(\x08\x12\x10\n\x08boot_lun\x18\x07 \x01(\x08\x12H\n\x0cstorage_type\x18\x08 \x01(\x0e22.google.cloud.baremetalsolution.v2.Lun.StorageType\x12\x0c\n\x04wwid\x18\t \x01(\t\x124\n\x0bexpire_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\tinstances\x18\x0c \x03(\tB1\xe0A\x03\xfaA+\n)baremetalsolution.googleapis.com/Instance"a\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\t\n\x05READY\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x0c\n\x08COOL_OFF\x10\x05"B\n\x11MultiprotocolType\x12"\n\x1eMULTIPROTOCOL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05LINUX\x10\x01"=\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\x12\x07\n\x03HDD\x10\x02:n\xeaAk\n$baremetalsolution.googleapis.com/Lun\x12Cprojects/{project}/locations/{location}/volumes/{volume}/luns/{lun}"K\n\rGetLunRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/Lun"y\n\x0fListLunsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"v\n\x10ListLunsResponse\x124\n\x04luns\x18\x01 \x03(\x0b2&.google.cloud.baremetalsolution.v2.Lun\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"M\n\x0fEvictLunRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/LunB\xf7\x01\n%com.google.cloud.baremetalsolution.v2B\x08LunProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.lun_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x08LunProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_LUN'].fields_by_name['name']._loaded_options = None
    _globals['_LUN'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LUN'].fields_by_name['storage_volume']._loaded_options = None
    _globals['_LUN'].fields_by_name['storage_volume']._serialized_options = b"\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_LUN'].fields_by_name['expire_time']._loaded_options = None
    _globals['_LUN'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_LUN'].fields_by_name['instances']._loaded_options = None
    _globals['_LUN'].fields_by_name['instances']._serialized_options = b'\xe0A\x03\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_LUN']._loaded_options = None
    _globals['_LUN']._serialized_options = b'\xeaAk\n$baremetalsolution.googleapis.com/Lun\x12Cprojects/{project}/locations/{location}/volumes/{volume}/luns/{lun}'
    _globals['_GETLUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLUNREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/Lun'
    _globals['_LISTLUNSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLUNSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_EVICTLUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EVICTLUNREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/Lun'
    _globals['_LUN']._serialized_start = 176
    _globals['_LUN']._serialized_end = 1037
    _globals['_LUN_STATE']._serialized_start = 697
    _globals['_LUN_STATE']._serialized_end = 794
    _globals['_LUN_MULTIPROTOCOLTYPE']._serialized_start = 796
    _globals['_LUN_MULTIPROTOCOLTYPE']._serialized_end = 862
    _globals['_LUN_STORAGETYPE']._serialized_start = 864
    _globals['_LUN_STORAGETYPE']._serialized_end = 925
    _globals['_GETLUNREQUEST']._serialized_start = 1039
    _globals['_GETLUNREQUEST']._serialized_end = 1114
    _globals['_LISTLUNSREQUEST']._serialized_start = 1116
    _globals['_LISTLUNSREQUEST']._serialized_end = 1237
    _globals['_LISTLUNSRESPONSE']._serialized_start = 1239
    _globals['_LISTLUNSRESPONSE']._serialized_end = 1357
    _globals['_EVICTLUNREQUEST']._serialized_start = 1359
    _globals['_EVICTLUNREQUEST']._serialized_end = 1436