"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/tag_holds.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/resourcemanager/v3/tag_holds.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf1\x01\n\x07TagHold\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06holder\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06origin\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x16\n\thelp_link\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:[\xeaAX\n+cloudresourcemanager.googleapis.com/TagHold\x12)tagValues/{tag_value}/tagHolds/{tag_hold}"\xb8\x01\n\x14CreateTagHoldRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+cloudresourcemanager.googleapis.com/TagHold\x12?\n\x08tag_hold\x18\x02 \x01(\x0b2(.google.cloud.resourcemanager.v3.TagHoldB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\x17\n\x15CreateTagHoldMetadata"u\n\x14DeleteTagHoldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/TagHold\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01"\x17\n\x15DeleteTagHoldMetadata"\xa0\x01\n\x13ListTagHoldsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+cloudresourcemanager.googleapis.com/TagHold\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"l\n\x14ListTagHoldsResponse\x12;\n\ttag_holds\x18\x01 \x03(\x0b2(.google.cloud.resourcemanager.v3.TagHold\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xec\x05\n\x08TagHolds\x12\xcf\x01\n\rCreateTagHold\x125.google.cloud.resourcemanager.v3.CreateTagHoldRequest\x1a\x1d.google.longrunning.Operation"h\xcaA \n\x07TagHold\x12\x15CreateTagHoldMetadata\xdaA\x0fparent,tag_hold\x82\xd3\xe4\x93\x02-"!/v3/{parent=tagValues/*}/tagHolds:\x08tag_hold\x12\xc8\x01\n\rDeleteTagHold\x125.google.cloud.resourcemanager.v3.DeleteTagHoldRequest\x1a\x1d.google.longrunning.Operation"a\xcaA.\n\x15google.protobuf.Empty\x12\x15DeleteTagHoldMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v3/{name=tagValues/*/tagHolds/*}\x12\xaf\x01\n\x0cListTagHolds\x124.google.cloud.resourcemanager.v3.ListTagHoldsRequest\x1a5.google.cloud.resourcemanager.v3.ListTagHoldsResponse"2\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v3/{parent=tagValues/*}/tagHolds\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xee\x01\n#com.google.cloud.resourcemanager.v3B\rTagHoldsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.tag_holds_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\rTagHoldsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_TAGHOLD'].fields_by_name['name']._loaded_options = None
    _globals['_TAGHOLD'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TAGHOLD'].fields_by_name['holder']._loaded_options = None
    _globals['_TAGHOLD'].fields_by_name['holder']._serialized_options = b'\xe0A\x02'
    _globals['_TAGHOLD'].fields_by_name['origin']._loaded_options = None
    _globals['_TAGHOLD'].fields_by_name['origin']._serialized_options = b'\xe0A\x01'
    _globals['_TAGHOLD'].fields_by_name['help_link']._loaded_options = None
    _globals['_TAGHOLD'].fields_by_name['help_link']._serialized_options = b'\xe0A\x01'
    _globals['_TAGHOLD'].fields_by_name['create_time']._loaded_options = None
    _globals['_TAGHOLD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TAGHOLD']._loaded_options = None
    _globals['_TAGHOLD']._serialized_options = b'\xeaAX\n+cloudresourcemanager.googleapis.com/TagHold\x12)tagValues/{tag_value}/tagHolds/{tag_hold}'
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+cloudresourcemanager.googleapis.com/TagHold'
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['tag_hold']._loaded_options = None
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['tag_hold']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATETAGHOLDREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETAGHOLDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGHOLDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/TagHold'
    _globals['_DELETETAGHOLDREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETETAGHOLDREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+cloudresourcemanager.googleapis.com/TagHold'
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTAGHOLDSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_TAGHOLDS']._loaded_options = None
    _globals['_TAGHOLDS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TAGHOLDS'].methods_by_name['CreateTagHold']._loaded_options = None
    _globals['_TAGHOLDS'].methods_by_name['CreateTagHold']._serialized_options = b'\xcaA \n\x07TagHold\x12\x15CreateTagHoldMetadata\xdaA\x0fparent,tag_hold\x82\xd3\xe4\x93\x02-"!/v3/{parent=tagValues/*}/tagHolds:\x08tag_hold'
    _globals['_TAGHOLDS'].methods_by_name['DeleteTagHold']._loaded_options = None
    _globals['_TAGHOLDS'].methods_by_name['DeleteTagHold']._serialized_options = b'\xcaA.\n\x15google.protobuf.Empty\x12\x15DeleteTagHoldMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v3/{name=tagValues/*/tagHolds/*}'
    _globals['_TAGHOLDS'].methods_by_name['ListTagHolds']._loaded_options = None
    _globals['_TAGHOLDS'].methods_by_name['ListTagHolds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v3/{parent=tagValues/*}/tagHolds'
    _globals['_TAGHOLD']._serialized_start = 299
    _globals['_TAGHOLD']._serialized_end = 540
    _globals['_CREATETAGHOLDREQUEST']._serialized_start = 543
    _globals['_CREATETAGHOLDREQUEST']._serialized_end = 727
    _globals['_CREATETAGHOLDMETADATA']._serialized_start = 729
    _globals['_CREATETAGHOLDMETADATA']._serialized_end = 752
    _globals['_DELETETAGHOLDREQUEST']._serialized_start = 754
    _globals['_DELETETAGHOLDREQUEST']._serialized_end = 871
    _globals['_DELETETAGHOLDMETADATA']._serialized_start = 873
    _globals['_DELETETAGHOLDMETADATA']._serialized_end = 896
    _globals['_LISTTAGHOLDSREQUEST']._serialized_start = 899
    _globals['_LISTTAGHOLDSREQUEST']._serialized_end = 1059
    _globals['_LISTTAGHOLDSRESPONSE']._serialized_start = 1061
    _globals['_LISTTAGHOLDSRESPONSE']._serialized_end = 1169
    _globals['_TAGHOLDS']._serialized_start = 1172
    _globals['_TAGHOLDS']._serialized_end = 1920