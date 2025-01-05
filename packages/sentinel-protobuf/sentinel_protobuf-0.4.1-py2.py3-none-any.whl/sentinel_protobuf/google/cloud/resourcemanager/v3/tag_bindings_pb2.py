"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/tag_bindings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/resourcemanager/v3/tag_bindings.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"\xb5\x01\n\nTagBinding\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x11\n\ttag_value\x18\x03 \x01(\t\x12!\n\x19tag_value_namespaced_name\x18\x04 \x01(\t:N\xeaAK\n.cloudresourcemanager.googleapis.com/TagBinding\x12\x19tagBindings/{tag_binding}"\x1a\n\x18CreateTagBindingMetadata"|\n\x17CreateTagBindingRequest\x12E\n\x0btag_binding\x18\x01 \x01(\x0b2+.google.cloud.resourcemanager.v3.TagBindingB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01"\x1a\n\x18DeleteTagBindingMetadata"_\n\x17DeleteTagBindingRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.cloudresourcemanager.googleapis.com/TagBinding"d\n\x16ListTagBindingsRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"u\n\x17ListTagBindingsResponse\x12A\n\x0ctag_bindings\x18\x01 \x03(\x0b2+.google.cloud.resourcemanager.v3.TagBinding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"`\n\x18ListEffectiveTagsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"{\n\x19ListEffectiveTagsResponse\x12E\n\x0eeffective_tags\x18\x01 \x03(\x0b2-.google.cloud.resourcemanager.v3.EffectiveTag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x80\x02\n\x0cEffectiveTag\x12D\n\ttag_value\x18\x01 \x01(\tB1\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue\x12\x1c\n\x14namespaced_tag_value\x18\x02 \x01(\t\x12@\n\x07tag_key\x18\x03 \x01(\tB/\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey\x12\x1a\n\x12namespaced_tag_key\x18\x04 \x01(\t\x12\x1b\n\x13tag_key_parent_name\x18\x06 \x01(\t\x12\x11\n\tinherited\x18\x05 \x01(\x082\x91\x07\n\x0bTagBindings\x12\xa6\x01\n\x0fListTagBindings\x127.google.cloud.resourcemanager.v3.ListTagBindingsRequest\x1a8.google.cloud.resourcemanager.v3.ListTagBindingsResponse" \xdaA\x06parent\x82\xd3\xe4\x93\x02\x11\x12\x0f/v3/tagBindings\x12\xc8\x01\n\x10CreateTagBinding\x128.google.cloud.resourcemanager.v3.CreateTagBindingRequest\x1a\x1d.google.longrunning.Operation"[\xcaA&\n\nTagBinding\x12\x18CreateTagBindingMetadata\xdaA\x0btag_binding\x82\xd3\xe4\x93\x02\x1e"\x0f/v3/tagBindings:\x0btag_binding\x12\xc9\x01\n\x10DeleteTagBinding\x128.google.cloud.resourcemanager.v3.DeleteTagBindingRequest\x1a\x1d.google.longrunning.Operation"\\\xcaA1\n\x15google.protobuf.Empty\x12\x18DeleteTagBindingMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v3/{name=tagBindings/**}\x12\xae\x01\n\x11ListEffectiveTags\x129.google.cloud.resourcemanager.v3.ListEffectiveTagsRequest\x1a:.google.cloud.resourcemanager.v3.ListEffectiveTagsResponse""\xdaA\x06parent\x82\xd3\xe4\x93\x02\x13\x12\x11/v3/effectiveTags\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xf1\x01\n#com.google.cloud.resourcemanager.v3B\x10TagBindingsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.tag_bindings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\x10TagBindingsProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_TAGBINDING'].fields_by_name['name']._loaded_options = None
    _globals['_TAGBINDING'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TAGBINDING']._loaded_options = None
    _globals['_TAGBINDING']._serialized_options = b'\xeaAK\n.cloudresourcemanager.googleapis.com/TagBinding\x12\x19tagBindings/{tag_binding}'
    _globals['_CREATETAGBINDINGREQUEST'].fields_by_name['tag_binding']._loaded_options = None
    _globals['_CREATETAGBINDINGREQUEST'].fields_by_name['tag_binding']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGBINDINGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATETAGBINDINGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETAGBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.cloudresourcemanager.googleapis.com/TagBinding'
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTAGBINDINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEFFECTIVETAGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_EFFECTIVETAG'].fields_by_name['tag_value']._loaded_options = None
    _globals['_EFFECTIVETAG'].fields_by_name['tag_value']._serialized_options = b'\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue'
    _globals['_EFFECTIVETAG'].fields_by_name['tag_key']._loaded_options = None
    _globals['_EFFECTIVETAG'].fields_by_name['tag_key']._serialized_options = b'\xfaA,\n*cloudresourcemanager.googleapis.com/TagKey'
    _globals['_TAGBINDINGS']._loaded_options = None
    _globals['_TAGBINDINGS']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TAGBINDINGS'].methods_by_name['ListTagBindings']._loaded_options = None
    _globals['_TAGBINDINGS'].methods_by_name['ListTagBindings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x11\x12\x0f/v3/tagBindings'
    _globals['_TAGBINDINGS'].methods_by_name['CreateTagBinding']._loaded_options = None
    _globals['_TAGBINDINGS'].methods_by_name['CreateTagBinding']._serialized_options = b'\xcaA&\n\nTagBinding\x12\x18CreateTagBindingMetadata\xdaA\x0btag_binding\x82\xd3\xe4\x93\x02\x1e"\x0f/v3/tagBindings:\x0btag_binding'
    _globals['_TAGBINDINGS'].methods_by_name['DeleteTagBinding']._loaded_options = None
    _globals['_TAGBINDINGS'].methods_by_name['DeleteTagBinding']._serialized_options = b'\xcaA1\n\x15google.protobuf.Empty\x12\x18DeleteTagBindingMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v3/{name=tagBindings/**}'
    _globals['_TAGBINDINGS'].methods_by_name['ListEffectiveTags']._loaded_options = None
    _globals['_TAGBINDINGS'].methods_by_name['ListEffectiveTags']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x13\x12\x11/v3/effectiveTags'
    _globals['_TAGBINDING']._serialized_start = 269
    _globals['_TAGBINDING']._serialized_end = 450
    _globals['_CREATETAGBINDINGMETADATA']._serialized_start = 452
    _globals['_CREATETAGBINDINGMETADATA']._serialized_end = 478
    _globals['_CREATETAGBINDINGREQUEST']._serialized_start = 480
    _globals['_CREATETAGBINDINGREQUEST']._serialized_end = 604
    _globals['_DELETETAGBINDINGMETADATA']._serialized_start = 606
    _globals['_DELETETAGBINDINGMETADATA']._serialized_end = 632
    _globals['_DELETETAGBINDINGREQUEST']._serialized_start = 634
    _globals['_DELETETAGBINDINGREQUEST']._serialized_end = 729
    _globals['_LISTTAGBINDINGSREQUEST']._serialized_start = 731
    _globals['_LISTTAGBINDINGSREQUEST']._serialized_end = 831
    _globals['_LISTTAGBINDINGSRESPONSE']._serialized_start = 833
    _globals['_LISTTAGBINDINGSRESPONSE']._serialized_end = 950
    _globals['_LISTEFFECTIVETAGSREQUEST']._serialized_start = 952
    _globals['_LISTEFFECTIVETAGSREQUEST']._serialized_end = 1048
    _globals['_LISTEFFECTIVETAGSRESPONSE']._serialized_start = 1050
    _globals['_LISTEFFECTIVETAGSRESPONSE']._serialized_end = 1173
    _globals['_EFFECTIVETAG']._serialized_start = 1176
    _globals['_EFFECTIVETAG']._serialized_end = 1432
    _globals['_TAGBINDINGS']._serialized_start = 1435
    _globals['_TAGBINDINGS']._serialized_end = 2348