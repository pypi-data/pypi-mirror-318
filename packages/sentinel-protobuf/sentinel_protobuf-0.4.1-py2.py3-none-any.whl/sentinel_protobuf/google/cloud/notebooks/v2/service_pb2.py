"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v2/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.notebooks.v2 import diagnostic_config_pb2 as google_dot_cloud_dot_notebooks_dot_v2_dot_diagnostic__config__pb2
from .....google.cloud.notebooks.v2 import instance_pb2 as google_dot_cloud_dot_notebooks_dot_v2_dot_instance__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/notebooks/v2/service.proto\x12\x19google.cloud.notebooks.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/notebooks/v2/diagnostic_config.proto\x1a(google/cloud/notebooks/v2/instance.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xef\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x16\n\x0estatus_message\x18\x05 \x01(\t\x12\x1e\n\x16requested_cancellation\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t\x12\x10\n\x08endpoint\x18\x08 \x01(\t"\xae\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!notebooks.googleapis.com/Instance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"}\n\x15ListInstancesResponse\x126\n\tinstances\x18\x01 \x03(\x0b2#.google.cloud.notebooks.v2.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"M\n\x12GetInstanceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance"\xc1\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!notebooks.googleapis.com/Instance\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\x08instance\x18\x03 \x01(\x0b2#.google.cloud.notebooks.v2.InstanceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa2\x01\n\x15UpdateInstanceRequest\x12:\n\x08instance\x18\x01 \x01(\x0b2#.google.cloud.notebooks.v2.InstanceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"i\n\x15DeleteInstanceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01")\n\x14StartInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"(\n\x13StopInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02")\n\x14ResetInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"C\n!CheckInstanceUpgradabilityRequest\x12\x1e\n\x11notebook_instance\x18\x01 \x01(\tB\x03\xe0A\x02"\x7f\n"CheckInstanceUpgradabilityResponse\x12\x13\n\x0bupgradeable\x18\x01 \x01(\x08\x12\x17\n\x0fupgrade_version\x18\x02 \x01(\t\x12\x14\n\x0cupgrade_info\x18\x03 \x01(\t\x12\x15\n\rupgrade_image\x18\x04 \x01(\t"+\n\x16UpgradeInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\x8d\x01\n\x17RollbackInstanceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance\x12\x1c\n\x0ftarget_snapshot\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0brevision_id\x18\x03 \x01(\tB\x06\xe0A\x03\xe0A\x02"\xbd\x01\n\x17DiagnoseInstanceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance\x12K\n\x11diagnostic_config\x18\x02 \x01(\x0b2+.google.cloud.notebooks.v2.DiagnosticConfigB\x03\xe0A\x02\x12\x1c\n\x0ftimeout_minutes\x18\x03 \x01(\x05B\x03\xe0A\x012\xfa\x13\n\x0fNotebookService\x12\xb2\x01\n\rListInstances\x12/.google.cloud.notebooks.v2.ListInstancesRequest\x1a0.google.cloud.notebooks.v2.ListInstancesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v2/{parent=projects/*/locations/*}/instances\x12\x9f\x01\n\x0bGetInstance\x12-.google.cloud.notebooks.v2.GetInstanceRequest\x1a#.google.cloud.notebooks.v2.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v2/{name=projects/*/locations/*/instances/*}\x12\xe0\x01\n\x0eCreateInstance\x120.google.cloud.notebooks.v2.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v2/{parent=projects/*/locations/*}/instances:\x08instance\x12\xe2\x01\n\x0eUpdateInstance\x120.google.cloud.notebooks.v2.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v2/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\xcc\x01\n\x0eDeleteInstance\x120.google.cloud.notebooks.v2.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v2/{name=projects/*/locations/*/instances/*}\x12\xbf\x01\n\rStartInstance\x12/.google.cloud.notebooks.v2.StartInstanceRequest\x1a\x1d.google.longrunning.Operation"^\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x028"3/v2/{name=projects/*/locations/*/instances/*}:start:\x01*\x12\xbc\x01\n\x0cStopInstance\x12..google.cloud.notebooks.v2.StopInstanceRequest\x1a\x1d.google.longrunning.Operation"]\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x027"2/v2/{name=projects/*/locations/*/instances/*}:stop:\x01*\x12\xbf\x01\n\rResetInstance\x12/.google.cloud.notebooks.v2.ResetInstanceRequest\x1a\x1d.google.longrunning.Operation"^\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x028"3/v2/{name=projects/*/locations/*/instances/*}:reset:\x01*\x12\xf0\x01\n\x1aCheckInstanceUpgradability\x12<.google.cloud.notebooks.v2.CheckInstanceUpgradabilityRequest\x1a=.google.cloud.notebooks.v2.CheckInstanceUpgradabilityResponse"U\x82\xd3\xe4\x93\x02O\x12M/v2/{notebook_instance=projects/*/locations/*/instances/*}:checkUpgradability\x12\xc5\x01\n\x0fUpgradeInstance\x121.google.cloud.notebooks.v2.UpgradeInstanceRequest\x1a\x1d.google.longrunning.Operation"`\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02:"5/v2/{name=projects/*/locations/*/instances/*}:upgrade:\x01*\x12\xc8\x01\n\x10RollbackInstance\x122.google.cloud.notebooks.v2.RollbackInstanceRequest\x1a\x1d.google.longrunning.Operation"a\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/instances/*}:rollback:\x01*\x12\xe1\x01\n\x10DiagnoseInstance\x122.google.cloud.notebooks.v2.DiagnoseInstanceRequest\x1a\x1d.google.longrunning.Operation"z\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x16name,diagnostic_config\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/instances/*}:diagnose:\x01*\x1aL\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc3\x01\n\x1dcom.google.cloud.notebooks.v2B\x0cServiceProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v2B\x0cServiceProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!notebooks.googleapis.com/Instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!notebooks.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CHECKINSTANCEUPGRADABILITYREQUEST'].fields_by_name['notebook_instance']._loaded_options = None
    _globals['_CHECKINSTANCEUPGRADABILITYREQUEST'].fields_by_name['notebook_instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPGRADEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance'
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['target_snapshot']._loaded_options = None
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['target_snapshot']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['revision_id']._loaded_options = None
    _globals['_ROLLBACKINSTANCEREQUEST'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x03\xe0A\x02'
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!notebooks.googleapis.com/Instance'
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['diagnostic_config']._loaded_options = None
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['diagnostic_config']._serialized_options = b'\xe0A\x02'
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['timeout_minutes']._loaded_options = None
    _globals['_DIAGNOSEINSTANCEREQUEST'].fields_by_name['timeout_minutes']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKSERVICE']._loaded_options = None
    _globals['_NOTEBOOKSERVICE']._serialized_options = b'\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v2/{parent=projects/*/locations/*}/instances'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v2/{name=projects/*/locations/*/instances/*}'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v2/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v2/{instance.name=projects/*/locations/*/instances/*}:\x08instance'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v2/{name=projects/*/locations/*/instances/*}'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StartInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StartInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x028"3/v2/{name=projects/*/locations/*/instances/*}:start:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StopInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StopInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x027"2/v2/{name=projects/*/locations/*/instances/*}:stop:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ResetInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ResetInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x028"3/v2/{name=projects/*/locations/*/instances/*}:reset:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CheckInstanceUpgradability']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CheckInstanceUpgradability']._serialized_options = b'\x82\xd3\xe4\x93\x02O\x12M/v2/{notebook_instance=projects/*/locations/*/instances/*}:checkUpgradability'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02:"5/v2/{name=projects/*/locations/*/instances/*}:upgrade:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['RollbackInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['RollbackInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/instances/*}:rollback:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DiagnoseInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DiagnoseInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x16name,diagnostic_config\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/instances/*}:diagnose:\x01*'
    _globals['_OPERATIONMETADATA']._serialized_start = 412
    _globals['_OPERATIONMETADATA']._serialized_end = 651
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 654
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 828
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 830
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 955
    _globals['_GETINSTANCEREQUEST']._serialized_start = 957
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1034
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 1037
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 1230
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 1233
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 1395
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 1397
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 1502
    _globals['_STARTINSTANCEREQUEST']._serialized_start = 1504
    _globals['_STARTINSTANCEREQUEST']._serialized_end = 1545
    _globals['_STOPINSTANCEREQUEST']._serialized_start = 1547
    _globals['_STOPINSTANCEREQUEST']._serialized_end = 1587
    _globals['_RESETINSTANCEREQUEST']._serialized_start = 1589
    _globals['_RESETINSTANCEREQUEST']._serialized_end = 1630
    _globals['_CHECKINSTANCEUPGRADABILITYREQUEST']._serialized_start = 1632
    _globals['_CHECKINSTANCEUPGRADABILITYREQUEST']._serialized_end = 1699
    _globals['_CHECKINSTANCEUPGRADABILITYRESPONSE']._serialized_start = 1701
    _globals['_CHECKINSTANCEUPGRADABILITYRESPONSE']._serialized_end = 1828
    _globals['_UPGRADEINSTANCEREQUEST']._serialized_start = 1830
    _globals['_UPGRADEINSTANCEREQUEST']._serialized_end = 1873
    _globals['_ROLLBACKINSTANCEREQUEST']._serialized_start = 1876
    _globals['_ROLLBACKINSTANCEREQUEST']._serialized_end = 2017
    _globals['_DIAGNOSEINSTANCEREQUEST']._serialized_start = 2020
    _globals['_DIAGNOSEINSTANCEREQUEST']._serialized_end = 2209
    _globals['_NOTEBOOKSERVICE']._serialized_start = 2212
    _globals['_NOTEBOOKSERVICE']._serialized_end = 4766