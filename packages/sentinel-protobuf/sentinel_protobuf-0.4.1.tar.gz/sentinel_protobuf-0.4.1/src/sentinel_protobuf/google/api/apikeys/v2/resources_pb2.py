"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/apikeys/v2/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/api/apikeys/v2/resources.proto\x12\x15google.api.apikeys.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x04\n\x03Key\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x17\n\nkey_string\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x0bannotations\x18\x08 \x03(\x0b2+.google.api.apikeys.v2.Key.AnnotationsEntry\x129\n\x0crestrictions\x18\t \x01(\x0b2#.google.api.apikeys.v2.Restrictions\x12\x11\n\x04etag\x18\x0b \x01(\tB\x03\xe0A\x03\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:a\xeaA^\n\x1aapikeys.googleapis.com/Key\x122projects/{project}/locations/{location}/keys/{key}*\x04keys2\x03keyR\x01\x01"\x9e\x03\n\x0cRestrictions\x12Q\n\x18browser_key_restrictions\x18\x01 \x01(\x0b2-.google.api.apikeys.v2.BrowserKeyRestrictionsH\x00\x12O\n\x17server_key_restrictions\x18\x02 \x01(\x0b2,.google.api.apikeys.v2.ServerKeyRestrictionsH\x00\x12Q\n\x18android_key_restrictions\x18\x03 \x01(\x0b2-.google.api.apikeys.v2.AndroidKeyRestrictionsH\x00\x12I\n\x14ios_key_restrictions\x18\x04 \x01(\x0b2).google.api.apikeys.v2.IosKeyRestrictionsH\x00\x125\n\x0bapi_targets\x18\x05 \x03(\x0b2 .google.api.apikeys.v2.ApiTargetB\x15\n\x13client_restrictions"3\n\x16BrowserKeyRestrictions\x12\x19\n\x11allowed_referrers\x18\x01 \x03(\t",\n\x15ServerKeyRestrictions\x12\x13\n\x0ballowed_ips\x18\x01 \x03(\t"a\n\x16AndroidKeyRestrictions\x12G\n\x14allowed_applications\x18\x01 \x03(\x0b2).google.api.apikeys.v2.AndroidApplication"D\n\x12AndroidApplication\x12\x18\n\x10sha1_fingerprint\x18\x01 \x01(\t\x12\x14\n\x0cpackage_name\x18\x02 \x01(\t"0\n\x12IosKeyRestrictions\x12\x1a\n\x12allowed_bundle_ids\x18\x01 \x03(\t"2\n\tApiTarget\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x14\n\x07methods\x18\x02 \x03(\tB\x03\xe0A\x01B\xb5\x01\n\x19com.google.api.apikeys.v2B\x0eResourcesProtoP\x01Z5cloud.google.com/go/apikeys/apiv2/apikeyspb;apikeyspb\xaa\x02\x17Google.Cloud.ApiKeys.V2\xca\x02\x17Google\\Cloud\\ApiKeys\\V2\xea\x02\x1aGoogle::Cloud::ApiKeys::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.apikeys.v2.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.api.apikeys.v2B\x0eResourcesProtoP\x01Z5cloud.google.com/go/apikeys/apiv2/apikeyspb;apikeyspb\xaa\x02\x17Google.Cloud.ApiKeys.V2\xca\x02\x17Google\\Cloud\\ApiKeys\\V2\xea\x02\x1aGoogle::Cloud::ApiKeys::V2'
    _globals['_KEY_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_KEY_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_KEY'].fields_by_name['name']._loaded_options = None
    _globals['_KEY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['uid']._loaded_options = None
    _globals['_KEY'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['key_string']._loaded_options = None
    _globals['_KEY'].fields_by_name['key_string']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['create_time']._loaded_options = None
    _globals['_KEY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['update_time']._loaded_options = None
    _globals['_KEY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['delete_time']._loaded_options = None
    _globals['_KEY'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_KEY'].fields_by_name['etag']._loaded_options = None
    _globals['_KEY'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_KEY']._loaded_options = None
    _globals['_KEY']._serialized_options = b'\xeaA^\n\x1aapikeys.googleapis.com/Key\x122projects/{project}/locations/{location}/keys/{key}*\x04keys2\x03keyR\x01\x01'
    _globals['_APITARGET'].fields_by_name['methods']._loaded_options = None
    _globals['_APITARGET'].fields_by_name['methods']._serialized_options = b'\xe0A\x01'
    _globals['_KEY']._serialized_start = 158
    _globals['_KEY']._serialized_end = 704
    _globals['_KEY_ANNOTATIONSENTRY']._serialized_start = 555
    _globals['_KEY_ANNOTATIONSENTRY']._serialized_end = 605
    _globals['_RESTRICTIONS']._serialized_start = 707
    _globals['_RESTRICTIONS']._serialized_end = 1121
    _globals['_BROWSERKEYRESTRICTIONS']._serialized_start = 1123
    _globals['_BROWSERKEYRESTRICTIONS']._serialized_end = 1174
    _globals['_SERVERKEYRESTRICTIONS']._serialized_start = 1176
    _globals['_SERVERKEYRESTRICTIONS']._serialized_end = 1220
    _globals['_ANDROIDKEYRESTRICTIONS']._serialized_start = 1222
    _globals['_ANDROIDKEYRESTRICTIONS']._serialized_end = 1319
    _globals['_ANDROIDAPPLICATION']._serialized_start = 1321
    _globals['_ANDROIDAPPLICATION']._serialized_end = 1389
    _globals['_IOSKEYRESTRICTIONS']._serialized_start = 1391
    _globals['_IOSKEYRESTRICTIONS']._serialized_end = 1439
    _globals['_APITARGET']._serialized_start = 1441
    _globals['_APITARGET']._serialized_end = 1491