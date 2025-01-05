"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcemanager/v3/tag_values.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/resourcemanager/v3/tag_values.proto\x12\x1fgoogle.cloud.resourcemanager.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd2\x02\n\x08TagValue\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x13\n\x06parent\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x1a\n\nshort_name\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1c\n\x0fnamespaced_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x01:K\xeaAH\n,cloudresourcemanager.googleapis.com/TagValue\x12\x15tagValues/{tag_value}R\x01\x01"b\n\x14ListTagValuesRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\x12\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"o\n\x15ListTagValuesResponse\x12=\n\ntag_values\x18\x01 \x03(\x0b2).google.cloud.resourcemanager.v3.TagValue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x12GetTagValueRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue"b\n\x1cGetNamespacedTagValueRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue"v\n\x15CreateTagValueRequest\x12A\n\ttag_value\x18\x01 \x01(\x0b2).google.cloud.resourcemanager.v3.TagValueB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01"\x18\n\x16CreateTagValueMetadata"\xac\x01\n\x15UpdateTagValueRequest\x12A\n\ttag_value\x18\x01 \x01(\x0b2).google.cloud.resourcemanager.v3.TagValueB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\x18\n\x16UpdateTagValueMetadata"\x8a\x01\n\x15DeleteTagValueRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x01"\x18\n\x16DeleteTagValueMetadata2\xac\r\n\tTagValues\x12\x9e\x01\n\rListTagValues\x125.google.cloud.resourcemanager.v3.ListTagValuesRequest\x1a6.google.cloud.resourcemanager.v3.ListTagValuesResponse"\x1e\xdaA\x06parent\x82\xd3\xe4\x93\x02\x0f\x12\r/v3/tagValues\x12\x94\x01\n\x0bGetTagValue\x123.google.cloud.resourcemanager.v3.GetTagValueRequest\x1a).google.cloud.resourcemanager.v3.TagValue"%\xdaA\x04name\x82\xd3\xe4\x93\x02\x18\x12\x16/v3/{name=tagValues/*}\x12\xaa\x01\n\x15GetNamespacedTagValue\x12=.google.cloud.resourcemanager.v3.GetNamespacedTagValueRequest\x1a).google.cloud.resourcemanager.v3.TagValue"\'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v3/tagValues/namespaced\x12\xba\x01\n\x0eCreateTagValue\x126.google.cloud.resourcemanager.v3.CreateTagValueRequest\x1a\x1d.google.longrunning.Operation"Q\xcaA"\n\x08TagValue\x12\x16CreateTagValueMetadata\xdaA\ttag_value\x82\xd3\xe4\x93\x02\x1a"\r/v3/tagValues:\ttag_value\x12\xd9\x01\n\x0eUpdateTagValue\x126.google.cloud.resourcemanager.v3.UpdateTagValueRequest\x1a\x1d.google.longrunning.Operation"p\xcaA"\n\x08TagValue\x12\x16UpdateTagValueMetadata\xdaA\x15tag_value,update_mask\x82\xd3\xe4\x93\x02-2 /v3/{tag_value.name=tagValues/*}:\ttag_value\x12\xb3\x01\n\x0eDeleteTagValue\x126.google.cloud.resourcemanager.v3.DeleteTagValueRequest\x1a\x1d.google.longrunning.Operation"J\xcaA"\n\x08TagValue\x12\x16DeleteTagValueMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x18*\x16/v3/{name=tagValues/*}\x12\x88\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"=\xdaA\x08resource\x82\xd3\xe4\x93\x02,"\'/v3/{resource=tagValues/*}:getIamPolicy:\x01*\x12\x8f\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"D\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02,"\'/v3/{resource=tagValues/*}:setIamPolicy:\x01*\x12\xba\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"O\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x022"-/v3/{resource=tagValues/*}:testIamPermissions:\x01*\x1a\x90\x01\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xef\x01\n#com.google.cloud.resourcemanager.v3B\x0eTagValuesProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcemanager.v3.tag_values_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.resourcemanager.v3B\x0eTagValuesProtoP\x01ZMcloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb;resourcemanagerpb\xaa\x02\x1fGoogle.Cloud.ResourceManager.V3\xca\x02\x1fGoogle\\Cloud\\ResourceManager\\V3\xea\x02"Google::Cloud::ResourceManager::V3'
    _globals['_TAGVALUE'].fields_by_name['name']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_TAGVALUE'].fields_by_name['parent']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['parent']._serialized_options = b'\xe0A\x05'
    _globals['_TAGVALUE'].fields_by_name['short_name']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['short_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TAGVALUE'].fields_by_name['namespaced_name']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['namespaced_name']._serialized_options = b'\xe0A\x03'
    _globals['_TAGVALUE'].fields_by_name['description']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TAGVALUE'].fields_by_name['create_time']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TAGVALUE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TAGVALUE'].fields_by_name['etag']._loaded_options = None
    _globals['_TAGVALUE'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_TAGVALUE']._loaded_options = None
    _globals['_TAGVALUE']._serialized_options = b'\xeaAH\n,cloudresourcemanager.googleapis.com/TagValue\x12\x15tagValues/{tag_value}R\x01\x01'
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\x12\x01*'
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTAGVALUESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETTAGVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTAGVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue'
    _globals['_GETNAMESPACEDTAGVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNAMESPACEDTAGVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue'
    _globals['_CREATETAGVALUEREQUEST'].fields_by_name['tag_value']._loaded_options = None
    _globals['_CREATETAGVALUEREQUEST'].fields_by_name['tag_value']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGVALUEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATETAGVALUEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['tag_value']._loaded_options = None
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['tag_value']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATETAGVALUEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,cloudresourcemanager.googleapis.com/TagValue'
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETETAGVALUEREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_TAGVALUES']._loaded_options = None
    _globals['_TAGVALUES']._serialized_options = b'\xcaA#cloudresourcemanager.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TAGVALUES'].methods_by_name['ListTagValues']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['ListTagValues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x0f\x12\r/v3/tagValues'
    _globals['_TAGVALUES'].methods_by_name['GetTagValue']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['GetTagValue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x18\x12\x16/v3/{name=tagValues/*}'
    _globals['_TAGVALUES'].methods_by_name['GetNamespacedTagValue']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['GetNamespacedTagValue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v3/tagValues/namespaced'
    _globals['_TAGVALUES'].methods_by_name['CreateTagValue']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['CreateTagValue']._serialized_options = b'\xcaA"\n\x08TagValue\x12\x16CreateTagValueMetadata\xdaA\ttag_value\x82\xd3\xe4\x93\x02\x1a"\r/v3/tagValues:\ttag_value'
    _globals['_TAGVALUES'].methods_by_name['UpdateTagValue']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['UpdateTagValue']._serialized_options = b'\xcaA"\n\x08TagValue\x12\x16UpdateTagValueMetadata\xdaA\x15tag_value,update_mask\x82\xd3\xe4\x93\x02-2 /v3/{tag_value.name=tagValues/*}:\ttag_value'
    _globals['_TAGVALUES'].methods_by_name['DeleteTagValue']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['DeleteTagValue']._serialized_options = b'\xcaA"\n\x08TagValue\x12\x16DeleteTagValueMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x18*\x16/v3/{name=tagValues/*}'
    _globals['_TAGVALUES'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02,"\'/v3/{resource=tagValues/*}:getIamPolicy:\x01*'
    _globals['_TAGVALUES'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02,"\'/v3/{resource=tagValues/*}:setIamPolicy:\x01*'
    _globals['_TAGVALUES'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_TAGVALUES'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x022"-/v3/{resource=tagValues/*}:testIamPermissions:\x01*'
    _globals['_TAGVALUE']._serialized_start = 365
    _globals['_TAGVALUE']._serialized_end = 703
    _globals['_LISTTAGVALUESREQUEST']._serialized_start = 705
    _globals['_LISTTAGVALUESREQUEST']._serialized_end = 803
    _globals['_LISTTAGVALUESRESPONSE']._serialized_start = 805
    _globals['_LISTTAGVALUESRESPONSE']._serialized_end = 916
    _globals['_GETTAGVALUEREQUEST']._serialized_start = 918
    _globals['_GETTAGVALUEREQUEST']._serialized_end = 1006
    _globals['_GETNAMESPACEDTAGVALUEREQUEST']._serialized_start = 1008
    _globals['_GETNAMESPACEDTAGVALUEREQUEST']._serialized_end = 1106
    _globals['_CREATETAGVALUEREQUEST']._serialized_start = 1108
    _globals['_CREATETAGVALUEREQUEST']._serialized_end = 1226
    _globals['_CREATETAGVALUEMETADATA']._serialized_start = 1228
    _globals['_CREATETAGVALUEMETADATA']._serialized_end = 1252
    _globals['_UPDATETAGVALUEREQUEST']._serialized_start = 1255
    _globals['_UPDATETAGVALUEREQUEST']._serialized_end = 1427
    _globals['_UPDATETAGVALUEMETADATA']._serialized_start = 1429
    _globals['_UPDATETAGVALUEMETADATA']._serialized_end = 1453
    _globals['_DELETETAGVALUEREQUEST']._serialized_start = 1456
    _globals['_DELETETAGVALUEREQUEST']._serialized_end = 1594
    _globals['_DELETETAGVALUEMETADATA']._serialized_start = 1596
    _globals['_DELETETAGVALUEMETADATA']._serialized_end = 1620
    _globals['_TAGVALUES']._serialized_start = 1623
    _globals['_TAGVALUES']._serialized_end = 3331