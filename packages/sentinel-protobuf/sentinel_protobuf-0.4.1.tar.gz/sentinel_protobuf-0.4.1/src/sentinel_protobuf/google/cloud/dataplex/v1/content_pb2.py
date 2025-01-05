"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/content.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import analyze_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_analyze__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/dataplex/v1/content.proto\x12\x18google.cloud.dataplex.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/dataplex/v1/analyze.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa1\x01\n\x14CreateContentRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cdataplex.googleapis.com/Lake\x127\n\x07content\x18\x02 \x01(\x0b2!.google.cloud.dataplex.v1.ContentB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\xa1\x01\n\x14UpdateContentRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x127\n\x07content\x18\x02 \x01(\x0b2!.google.cloud.dataplex.v1.ContentB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"M\n\x14DeleteContentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataplex.googleapis.com/Content"\x90\x01\n\x12ListContentRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cdataplex.googleapis.com/Lake\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"b\n\x13ListContentResponse\x122\n\x07content\x18\x01 \x03(\x0b2!.google.cloud.dataplex.v1.Content\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd8\x01\n\x11GetContentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataplex.googleapis.com/Content\x12J\n\x04view\x18\x02 \x01(\x0e27.google.cloud.dataplex.v1.GetContentRequest.ContentViewB\x03\xe0A\x01"@\n\x0bContentView\x12\x1c\n\x18CONTENT_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x022\xad\x10\n\x0eContentService\x12\x80\x02\n\rCreateContent\x12..google.cloud.dataplex.v1.CreateContentRequest\x1a!.google.cloud.dataplex.v1.Content"\x9b\x01\xdaA\x0eparent,content\x82\xd3\xe4\x93\x02\x83\x01"8/v1/{parent=projects/*/locations/*/lakes/*}/contentitems:\x07contentZ>"3/v1/{parent=projects/*/locations/*/lakes/*}/content:\x07content\x12\x97\x02\n\rUpdateContent\x12..google.cloud.dataplex.v1.UpdateContentRequest\x1a!.google.cloud.dataplex.v1.Content"\xb2\x01\xdaA\x13content,update_mask\x82\xd3\xe4\x93\x02\x95\x012A/v1/{content.name=projects/*/locations/*/lakes/*/contentitems/**}:\x07contentZG2</v1/{content.name=projects/*/locations/*/lakes/*/content/**}:\x07content\x12\xda\x01\n\rDeleteContent\x12..google.cloud.dataplex.v1.DeleteContentRequest\x1a\x16.google.protobuf.Empty"\x80\x01\xdaA\x04name\x82\xd3\xe4\x93\x02s*9/v1/{name=projects/*/locations/*/lakes/*/contentitems/**}Z6*4/v1/{name=projects/*/locations/*/lakes/*/content/**}\x12\xdf\x01\n\nGetContent\x12+.google.cloud.dataplex.v1.GetContentRequest\x1a!.google.cloud.dataplex.v1.Content"\x80\x01\xdaA\x04name\x82\xd3\xe4\x93\x02s\x129/v1/{name=projects/*/locations/*/lakes/*/contentitems/**}Z6\x124/v1/{name=projects/*/locations/*/lakes/*/content/**}\x12\xf3\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa7\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\x95\x01\x12J/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:getIamPolicyZG\x12E/v1/{resource=projects/*/locations/*/lakes/*/content/**}:getIamPolicy\x12\xee\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa2\x01\x82\xd3\xe4\x93\x02\x9b\x01"J/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:setIamPolicy:\x01*ZJ"E/v1/{resource=projects/*/locations/*/lakes/*/content/**}:setIamPolicy:\x01*\x12\x9a\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xae\x01\x82\xd3\xe4\x93\x02\xa7\x01"P/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:testIamPermissions:\x01*ZP"K/v1/{resource=projects/*/locations/*/lakes/*/content/**}:testIamPermissions:\x01*\x12\xed\x01\n\x0bListContent\x12,.google.cloud.dataplex.v1.ListContentRequest\x1a-.google.cloud.dataplex.v1.ListContentResponse"\x80\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02q\x128/v1/{parent=projects/*/locations/*/lakes/*}/contentitemsZ5\x123/v1/{parent=projects/*/locations/*/lakes/*}/content\x1aK\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBh\n\x1ccom.google.cloud.dataplex.v1B\x0cContentProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x0cContentProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_CREATECONTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONTENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cdataplex.googleapis.com/Lake'
    _globals['_CREATECONTENTREQUEST'].fields_by_name['content']._loaded_options = None
    _globals['_CREATECONTENTREQUEST'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONTENTREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATECONTENTREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['content']._loaded_options = None
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATECONTENTREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataplex.googleapis.com/Content'
    _globals['_LISTCONTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cdataplex.googleapis.com/Lake'
    _globals['_LISTCONTENTREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONTENTREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTENTREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONTENTREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTENTREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONTENTREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETCONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataplex.googleapis.com/Content'
    _globals['_GETCONTENTREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETCONTENTREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_CONTENTSERVICE']._loaded_options = None
    _globals['_CONTENTSERVICE']._serialized_options = b'\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONTENTSERVICE'].methods_by_name['CreateContent']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['CreateContent']._serialized_options = b'\xdaA\x0eparent,content\x82\xd3\xe4\x93\x02\x83\x01"8/v1/{parent=projects/*/locations/*/lakes/*}/contentitems:\x07contentZ>"3/v1/{parent=projects/*/locations/*/lakes/*}/content:\x07content'
    _globals['_CONTENTSERVICE'].methods_by_name['UpdateContent']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['UpdateContent']._serialized_options = b'\xdaA\x13content,update_mask\x82\xd3\xe4\x93\x02\x95\x012A/v1/{content.name=projects/*/locations/*/lakes/*/contentitems/**}:\x07contentZG2</v1/{content.name=projects/*/locations/*/lakes/*/content/**}:\x07content'
    _globals['_CONTENTSERVICE'].methods_by_name['DeleteContent']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['DeleteContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02s*9/v1/{name=projects/*/locations/*/lakes/*/contentitems/**}Z6*4/v1/{name=projects/*/locations/*/lakes/*/content/**}'
    _globals['_CONTENTSERVICE'].methods_by_name['GetContent']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['GetContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02s\x129/v1/{name=projects/*/locations/*/lakes/*/contentitems/**}Z6\x124/v1/{name=projects/*/locations/*/lakes/*/content/**}'
    _globals['_CONTENTSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02\x95\x01\x12J/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:getIamPolicyZG\x12E/v1/{resource=projects/*/locations/*/lakes/*/content/**}:getIamPolicy'
    _globals['_CONTENTSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x9b\x01"J/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:setIamPolicy:\x01*ZJ"E/v1/{resource=projects/*/locations/*/lakes/*/content/**}:setIamPolicy:\x01*'
    _globals['_CONTENTSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa7\x01"P/v1/{resource=projects/*/locations/*/lakes/*/contentitems/**}:testIamPermissions:\x01*ZP"K/v1/{resource=projects/*/locations/*/lakes/*/content/**}:testIamPermissions:\x01*'
    _globals['_CONTENTSERVICE'].methods_by_name['ListContent']._loaded_options = None
    _globals['_CONTENTSERVICE'].methods_by_name['ListContent']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02q\x128/v1/{parent=projects/*/locations/*/lakes/*}/contentitemsZ5\x123/v1/{parent=projects/*/locations/*/lakes/*}/content'
    _globals['_CREATECONTENTREQUEST']._serialized_start = 347
    _globals['_CREATECONTENTREQUEST']._serialized_end = 508
    _globals['_UPDATECONTENTREQUEST']._serialized_start = 511
    _globals['_UPDATECONTENTREQUEST']._serialized_end = 672
    _globals['_DELETECONTENTREQUEST']._serialized_start = 674
    _globals['_DELETECONTENTREQUEST']._serialized_end = 751
    _globals['_LISTCONTENTREQUEST']._serialized_start = 754
    _globals['_LISTCONTENTREQUEST']._serialized_end = 898
    _globals['_LISTCONTENTRESPONSE']._serialized_start = 900
    _globals['_LISTCONTENTRESPONSE']._serialized_end = 998
    _globals['_GETCONTENTREQUEST']._serialized_start = 1001
    _globals['_GETCONTENTREQUEST']._serialized_end = 1217
    _globals['_GETCONTENTREQUEST_CONTENTVIEW']._serialized_start = 1153
    _globals['_GETCONTENTREQUEST_CONTENTVIEW']._serialized_end = 1217
    _globals['_CONTENTSERVICE']._serialized_start = 1220
    _globals['_CONTENTSERVICE']._serialized_end = 3313