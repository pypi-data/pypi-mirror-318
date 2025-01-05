"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/runtimeconfig/v1beta1/runtimeconfig.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.cloud.runtimeconfig.v1beta1 import resources_pb2 as google_dot_cloud_dot_runtimeconfig_dot_v1beta1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/runtimeconfig/v1beta1/runtimeconfig.proto\x12"google.cloud.runtimeconfig.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a2google/cloud/runtimeconfig/v1beta1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"K\n\x12ListConfigsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x13ListConfigsResponse\x12B\n\x07configs\x18\x01 \x03(\x0b21.google.cloud.runtimeconfig.v1beta1.RuntimeConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t" \n\x10GetConfigRequest\x12\x0c\n\x04name\x18\x02 \x01(\t"|\n\x13CreateConfigRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12A\n\x06config\x18\x02 \x01(\x0b21.google.cloud.runtimeconfig.v1beta1.RuntimeConfig\x12\x12\n\nrequest_id\x18\x03 \x01(\t"f\n\x13UpdateConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12A\n\x06config\x18\x02 \x01(\x0b21.google.cloud.runtimeconfig.v1beta1.RuntimeConfig"#\n\x13DeleteConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"t\n\x14ListVariablesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x15\n\rreturn_values\x18\x05 \x01(\x08"q\n\x15ListVariablesResponse\x12?\n\tvariables\x18\x01 \x03(\x0b2,.google.cloud.runtimeconfig.v1beta1.Variable\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x14WatchVariableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nnewer_than\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp""\n\x12GetVariableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"{\n\x15CreateVariableRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12>\n\x08variable\x18\x02 \x01(\x0b2,.google.cloud.runtimeconfig.v1beta1.Variable\x12\x12\n\nrequest_id\x18\x03 \x01(\t"e\n\x15UpdateVariableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x08variable\x18\x02 \x01(\x0b2,.google.cloud.runtimeconfig.v1beta1.Variable"8\n\x15DeleteVariableRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\trecursive\x18\x02 \x01(\x08"K\n\x12ListWaitersRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x13ListWaitersResponse\x12;\n\x07waiters\x18\x01 \x03(\x0b2*.google.cloud.runtimeconfig.v1beta1.Waiter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t" \n\x10GetWaiterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"u\n\x13CreateWaiterRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12:\n\x06waiter\x18\x02 \x01(\x0b2*.google.cloud.runtimeconfig.v1beta1.Waiter\x12\x12\n\nrequest_id\x18\x03 \x01(\t"#\n\x13DeleteWaiterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xd6\x14\n\x14RuntimeConfigManager\x12\xac\x01\n\x0bListConfigs\x126.google.cloud.runtimeconfig.v1beta1.ListConfigsRequest\x1a7.google.cloud.runtimeconfig.v1beta1.ListConfigsResponse",\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{parent=projects/*}/configs\x12\xa2\x01\n\tGetConfig\x124.google.cloud.runtimeconfig.v1beta1.GetConfigRequest\x1a1.google.cloud.runtimeconfig.v1beta1.RuntimeConfig",\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{name=projects/*/configs/*}\x12\xb0\x01\n\x0cCreateConfig\x127.google.cloud.runtimeconfig.v1beta1.CreateConfigRequest\x1a1.google.cloud.runtimeconfig.v1beta1.RuntimeConfig"4\x82\xd3\xe4\x93\x02."$/v1beta1/{parent=projects/*}/configs:\x06config\x12\xb0\x01\n\x0cUpdateConfig\x127.google.cloud.runtimeconfig.v1beta1.UpdateConfigRequest\x1a1.google.cloud.runtimeconfig.v1beta1.RuntimeConfig"4\x82\xd3\xe4\x93\x02.\x1a$/v1beta1/{name=projects/*/configs/*}:\x06config\x12\x8d\x01\n\x0cDeleteConfig\x127.google.cloud.runtimeconfig.v1beta1.DeleteConfigRequest\x1a\x16.google.protobuf.Empty",\x82\xd3\xe4\x93\x02&*$/v1beta1/{name=projects/*/configs/*}\x12\xbe\x01\n\rListVariables\x128.google.cloud.runtimeconfig.v1beta1.ListVariablesRequest\x1a9.google.cloud.runtimeconfig.v1beta1.ListVariablesResponse"8\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/configs/*}/variables\x12\xae\x01\n\x0bGetVariable\x126.google.cloud.runtimeconfig.v1beta1.GetVariableRequest\x1a,.google.cloud.runtimeconfig.v1beta1.Variable"9\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/configs/*/variables/**}\x12\xbb\x01\n\rWatchVariable\x128.google.cloud.runtimeconfig.v1beta1.WatchVariableRequest\x1a,.google.cloud.runtimeconfig.v1beta1.Variable"B\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/configs/*/variables/**}:watch:\x01*\x12\xbd\x01\n\x0eCreateVariable\x129.google.cloud.runtimeconfig.v1beta1.CreateVariableRequest\x1a,.google.cloud.runtimeconfig.v1beta1.Variable"B\x82\xd3\xe4\x93\x02<"0/v1beta1/{parent=projects/*/configs/*}/variables:\x08variable\x12\xbe\x01\n\x0eUpdateVariable\x129.google.cloud.runtimeconfig.v1beta1.UpdateVariableRequest\x1a,.google.cloud.runtimeconfig.v1beta1.Variable"C\x82\xd3\xe4\x93\x02=\x1a1/v1beta1/{name=projects/*/configs/*/variables/**}:\x08variable\x12\x9e\x01\n\x0eDeleteVariable\x129.google.cloud.runtimeconfig.v1beta1.DeleteVariableRequest\x1a\x16.google.protobuf.Empty"9\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/configs/*/variables/**}\x12\xb6\x01\n\x0bListWaiters\x126.google.cloud.runtimeconfig.v1beta1.ListWaitersRequest\x1a7.google.cloud.runtimeconfig.v1beta1.ListWaitersResponse"6\x82\xd3\xe4\x93\x020\x12./v1beta1/{parent=projects/*/configs/*}/waiters\x12\xa5\x01\n\tGetWaiter\x124.google.cloud.runtimeconfig.v1beta1.GetWaiterRequest\x1a*.google.cloud.runtimeconfig.v1beta1.Waiter"6\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/configs/*/waiters/*}\x12\xa6\x01\n\x0cCreateWaiter\x127.google.cloud.runtimeconfig.v1beta1.CreateWaiterRequest\x1a\x1d.google.longrunning.Operation">\x82\xd3\xe4\x93\x028"./v1beta1/{parent=projects/*/configs/*}/waiters:\x06waiter\x12\x97\x01\n\x0cDeleteWaiter\x127.google.cloud.runtimeconfig.v1beta1.DeleteWaiterRequest\x1a\x16.google.protobuf.Empty"6\x82\xd3\xe4\x93\x020*./v1beta1/{name=projects/*/configs/*/waiters/*}B\xc2\x01\n&com.google.cloud.runtimeconfig.v1beta1P\x01ZLcloud.google.com/go/runtimeconfig/apiv1beta1/runtimeconfigpb;runtimeconfigpb\xaa\x02"Google.Cloud.RuntimeConfig.V1Beta1\xca\x02"Google\\Cloud\\RuntimeConfig\\V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.runtimeconfig.v1beta1.runtimeconfig_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.runtimeconfig.v1beta1P\x01ZLcloud.google.com/go/runtimeconfig/apiv1beta1/runtimeconfigpb;runtimeconfigpb\xaa\x02"Google.Cloud.RuntimeConfig.V1Beta1\xca\x02"Google\\Cloud\\RuntimeConfig\\V1beta1'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListConfigs']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListConfigs']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{parent=projects/*}/configs'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetConfig']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{name=projects/*/configs/*}'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateConfig']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02."$/v1beta1/{parent=projects/*}/configs:\x06config'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['UpdateConfig']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['UpdateConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x1a$/v1beta1/{name=projects/*/configs/*}:\x06config'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteConfig']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02&*$/v1beta1/{name=projects/*/configs/*}'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListVariables']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListVariables']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/configs/*}/variables'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetVariable']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetVariable']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/configs/*/variables/**}'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['WatchVariable']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['WatchVariable']._serialized_options = b'\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/configs/*/variables/**}:watch:\x01*'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateVariable']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateVariable']._serialized_options = b'\x82\xd3\xe4\x93\x02<"0/v1beta1/{parent=projects/*/configs/*}/variables:\x08variable'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['UpdateVariable']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['UpdateVariable']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x1a1/v1beta1/{name=projects/*/configs/*/variables/**}:\x08variable'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteVariable']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteVariable']._serialized_options = b'\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/configs/*/variables/**}'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListWaiters']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['ListWaiters']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta1/{parent=projects/*/configs/*}/waiters'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetWaiter']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['GetWaiter']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/configs/*/waiters/*}'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateWaiter']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['CreateWaiter']._serialized_options = b'\x82\xd3\xe4\x93\x028"./v1beta1/{parent=projects/*/configs/*}/waiters:\x06waiter'
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteWaiter']._loaded_options = None
    _globals['_RUNTIMECONFIGMANAGER'].methods_by_name['DeleteWaiter']._serialized_options = b'\x82\xd3\xe4\x93\x020*./v1beta1/{name=projects/*/configs/*/waiters/*}'
    _globals['_LISTCONFIGSREQUEST']._serialized_start = 275
    _globals['_LISTCONFIGSREQUEST']._serialized_end = 350
    _globals['_LISTCONFIGSRESPONSE']._serialized_start = 352
    _globals['_LISTCONFIGSRESPONSE']._serialized_end = 466
    _globals['_GETCONFIGREQUEST']._serialized_start = 468
    _globals['_GETCONFIGREQUEST']._serialized_end = 500
    _globals['_CREATECONFIGREQUEST']._serialized_start = 502
    _globals['_CREATECONFIGREQUEST']._serialized_end = 626
    _globals['_UPDATECONFIGREQUEST']._serialized_start = 628
    _globals['_UPDATECONFIGREQUEST']._serialized_end = 730
    _globals['_DELETECONFIGREQUEST']._serialized_start = 732
    _globals['_DELETECONFIGREQUEST']._serialized_end = 767
    _globals['_LISTVARIABLESREQUEST']._serialized_start = 769
    _globals['_LISTVARIABLESREQUEST']._serialized_end = 885
    _globals['_LISTVARIABLESRESPONSE']._serialized_start = 887
    _globals['_LISTVARIABLESRESPONSE']._serialized_end = 1000
    _globals['_WATCHVARIABLEREQUEST']._serialized_start = 1002
    _globals['_WATCHVARIABLEREQUEST']._serialized_end = 1086
    _globals['_GETVARIABLEREQUEST']._serialized_start = 1088
    _globals['_GETVARIABLEREQUEST']._serialized_end = 1122
    _globals['_CREATEVARIABLEREQUEST']._serialized_start = 1124
    _globals['_CREATEVARIABLEREQUEST']._serialized_end = 1247
    _globals['_UPDATEVARIABLEREQUEST']._serialized_start = 1249
    _globals['_UPDATEVARIABLEREQUEST']._serialized_end = 1350
    _globals['_DELETEVARIABLEREQUEST']._serialized_start = 1352
    _globals['_DELETEVARIABLEREQUEST']._serialized_end = 1408
    _globals['_LISTWAITERSREQUEST']._serialized_start = 1410
    _globals['_LISTWAITERSREQUEST']._serialized_end = 1485
    _globals['_LISTWAITERSRESPONSE']._serialized_start = 1487
    _globals['_LISTWAITERSRESPONSE']._serialized_end = 1594
    _globals['_GETWAITERREQUEST']._serialized_start = 1596
    _globals['_GETWAITERREQUEST']._serialized_end = 1628
    _globals['_CREATEWAITERREQUEST']._serialized_start = 1630
    _globals['_CREATEWAITERREQUEST']._serialized_end = 1747
    _globals['_DELETEWAITERREQUEST']._serialized_start = 1749
    _globals['_DELETEWAITERREQUEST']._serialized_end = 1784
    _globals['_RUNTIMECONFIGMANAGER']._serialized_start = 1787
    _globals['_RUNTIMECONFIGMANAGER']._serialized_end = 4433