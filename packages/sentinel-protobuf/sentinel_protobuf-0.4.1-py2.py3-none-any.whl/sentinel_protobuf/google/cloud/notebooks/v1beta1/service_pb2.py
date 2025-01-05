"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1beta1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.notebooks.v1beta1 import environment_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2
from .....google.cloud.notebooks.v1beta1 import instance_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_instance__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/notebooks/v1beta1/service.proto\x12\x1egoogle.cloud.notebooks.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a0google/cloud/notebooks/v1beta1/environment.proto\x1a-google/cloud/notebooks/v1beta1/instance.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xef\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x16\n\x0estatus_message\x18\x05 \x01(\t\x12\x1e\n\x16requested_cancellation\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t\x12\x10\n\x08endpoint\x18\x08 \x01(\t"R\n\x14ListInstancesRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x15ListInstancesResponse\x12;\n\tinstances\x18\x01 \x03(\x0b2(.google.cloud.notebooks.v1beta1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\'\n\x12GetInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\x87\x01\n\x15CreateInstanceRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x08instance\x18\x03 \x01(\x0b2(.google.cloud.notebooks.v1beta1.InstanceB\x03\xe0A\x02"H\n\x17RegisterInstanceRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x98\x01\n\x1dSetInstanceAcceleratorRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x04type\x18\x02 \x01(\x0e28.google.cloud.notebooks.v1beta1.Instance.AcceleratorTypeB\x03\xe0A\x02\x12\x17\n\ncore_count\x18\x03 \x01(\x03B\x03\xe0A\x02"M\n\x1dSetInstanceMachineTypeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cmachine_type\x18\x02 \x01(\tB\x03\xe0A\x02"\xb2\x01\n\x18SetInstanceLabelsRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\x06labels\x18\x02 \x03(\x0b2D.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"*\n\x15DeleteInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02")\n\x14StartInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"(\n\x13StopInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02")\n\x14ResetInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xce\x01\n\x19ReportInstanceInfoRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05vm_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12Y\n\x08metadata\x18\x03 \x03(\x0b2G.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01">\n\x1cIsInstanceUpgradeableRequest\x12\x1e\n\x11notebook_instance\x18\x01 \x01(\tB\x03\xe0A\x02"z\n\x1dIsInstanceUpgradeableResponse\x12\x13\n\x0bupgradeable\x18\x01 \x01(\x08\x12\x17\n\x0fupgrade_version\x18\x02 \x01(\t\x12\x14\n\x0cupgrade_info\x18\x03 \x01(\t\x12\x15\n\rupgrade_image\x18\x04 \x01(\t"+\n\x16UpgradeInstanceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"G\n\x1eUpgradeInstanceInternalRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05vm_id\x18\x02 \x01(\tB\x03\xe0A\x02"U\n\x17ListEnvironmentsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8b\x01\n\x18ListEnvironmentsResponse\x12A\n\x0cenvironments\x18\x01 \x03(\x0b2+.google.cloud.notebooks.v1beta1.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"*\n\x15GetEnvironmentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\x93\x01\n\x18CreateEnvironmentRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0eenvironment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12E\n\x0benvironment\x18\x03 \x01(\x0b2+.google.cloud.notebooks.v1beta1.EnvironmentB\x03\xe0A\x02"-\n\x18DeleteEnvironmentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x022\x81 \n\x0fNotebookService\x12\xb8\x01\n\rListInstances\x124.google.cloud.notebooks.v1beta1.ListInstancesRequest\x1a5.google.cloud.notebooks.v1beta1.ListInstancesResponse":\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/instances\x12\xa7\x01\n\x0bGetInstance\x122.google.cloud.notebooks.v1beta1.GetInstanceRequest\x1a(.google.cloud.notebooks.v1beta1.Instance":\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/instances/*}\x12\xcc\x01\n\x0eCreateInstance\x125.google.cloud.notebooks.v1beta1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"d\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xd2\x01\n\x10RegisterInstance\x127.google.cloud.notebooks.v1beta1.RegisterInstanceRequest\x1a\x1d.google.longrunning.Operation"f\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02@";/v1beta1/{parent=projects/*/locations/*}/instances:register:\x01*\x12\xe4\x01\n\x16SetInstanceAccelerator\x12=.google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest\x1a\x1d.google.longrunning.Operation"l\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setAccelerator:\x01*\x12\xe4\x01\n\x16SetInstanceMachineType\x12=.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest\x1a\x1d.google.longrunning.Operation"l\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setMachineType:\x01*\x12\xd5\x01\n\x11SetInstanceLabels\x128.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest\x1a\x1d.google.longrunning.Operation"g\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A2</v1beta1/{name=projects/*/locations/*/instances/*}:setLabels:\x01*\x12\xcf\x01\n\x0eDeleteInstance\x125.google.cloud.notebooks.v1beta1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"g\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/instances/*}\x12\xc9\x01\n\rStartInstance\x124.google.cloud.notebooks.v1beta1.StartInstanceRequest\x1a\x1d.google.longrunning.Operation"c\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/instances/*}:start:\x01*\x12\xc6\x01\n\x0cStopInstance\x123.google.cloud.notebooks.v1beta1.StopInstanceRequest\x1a\x1d.google.longrunning.Operation"b\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/locations/*/instances/*}:stop:\x01*\x12\xc9\x01\n\rResetInstance\x124.google.cloud.notebooks.v1beta1.ResetInstanceRequest\x1a\x1d.google.longrunning.Operation"c\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/instances/*}:reset:\x01*\x12\xd4\x01\n\x12ReportInstanceInfo\x129.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest\x1a\x1d.google.longrunning.Operation"d\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/instances/*}:report:\x01*\x12\xee\x01\n\x15IsInstanceUpgradeable\x12<.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableRequest\x1a=.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableResponse"X\x88\x02\x01\x82\xd3\xe4\x93\x02O\x12M/v1beta1/{notebook_instance=projects/*/locations/*/instances/*}:isUpgradeable\x12\xd2\x01\n\x0fUpgradeInstance\x126.google.cloud.notebooks.v1beta1.UpgradeInstanceRequest\x1a\x1d.google.longrunning.Operation"h\x88\x02\x01\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02?":/v1beta1/{name=projects/*/locations/*/instances/*}:upgrade:\x01*\x12\xea\x01\n\x17UpgradeInstanceInternal\x12>.google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest\x1a\x1d.google.longrunning.Operation"p\x88\x02\x01\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=projects/*/locations/*/instances/*}:upgradeInternal:\x01*\x12\xc4\x01\n\x10ListEnvironments\x127.google.cloud.notebooks.v1beta1.ListEnvironmentsRequest\x1a8.google.cloud.notebooks.v1beta1.ListEnvironmentsResponse"=\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/environments\x12\xb3\x01\n\x0eGetEnvironment\x125.google.cloud.notebooks.v1beta1.GetEnvironmentRequest\x1a+.google.cloud.notebooks.v1beta1.Environment"=\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/environments/*}\x12\xdb\x01\n\x11CreateEnvironment\x128.google.cloud.notebooks.v1beta1.CreateEnvironmentRequest\x1a\x1d.google.longrunning.Operation"m\xcaA \n\x0bEnvironment\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02D"5/v1beta1/{parent=projects/*/locations/*}/environments:\x0benvironment\x12\xd8\x01\n\x11DeleteEnvironment\x128.google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest\x1a\x1d.google.longrunning.Operation"j\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/environments/*}\x1aL\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xde\x01\n"com.google.cloud.notebooks.v1beta1B\x0eNotebooksProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.notebooks.v1beta1B\x0eNotebooksProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REGISTERINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_REGISTERINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['type']._loaded_options = None
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['core_count']._loaded_options = None
    _globals['_SETINSTANCEACCELERATORREQUEST'].fields_by_name['core_count']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCEMACHINETYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETINSTANCEMACHINETYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCEMACHINETYPEREQUEST'].fields_by_name['machine_type']._loaded_options = None
    _globals['_SETINSTANCEMACHINETYPEREQUEST'].fields_by_name['machine_type']._serialized_options = b'\xe0A\x02'
    _globals['_SETINSTANCELABELSREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_SETINSTANCELABELSREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SETINSTANCELABELSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETINSTANCELABELSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTINSTANCEINFOREQUEST_METADATAENTRY']._loaded_options = None
    _globals['_REPORTINSTANCEINFOREQUEST_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_REPORTINSTANCEINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REPORTINSTANCEINFOREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTINSTANCEINFOREQUEST'].fields_by_name['vm_id']._loaded_options = None
    _globals['_REPORTINSTANCEINFOREQUEST'].fields_by_name['vm_id']._serialized_options = b'\xe0A\x02'
    _globals['_ISINSTANCEUPGRADEABLEREQUEST'].fields_by_name['notebook_instance']._loaded_options = None
    _globals['_ISINSTANCEUPGRADEABLEREQUEST'].fields_by_name['notebook_instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPGRADEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADEINSTANCEINTERNALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPGRADEINSTANCEINTERNALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADEINSTANCEINTERNALREQUEST'].fields_by_name['vm_id']._loaded_options = None
    _globals['_UPGRADEINSTANCEINTERNALREQUEST'].fields_by_name['vm_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment_id']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_NOTEBOOKSERVICE']._loaded_options = None
    _globals['_NOTEBOOKSERVICE']._serialized_options = b'\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListInstances']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/instances'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetInstance']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/instances/*}'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['RegisterInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['RegisterInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02@";/v1beta1/{parent=projects/*/locations/*}/instances:register:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceAccelerator']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceAccelerator']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setAccelerator:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceMachineType']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceMachineType']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02F2A/v1beta1/{name=projects/*/locations/*/instances/*}:setMachineType:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceLabels']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['SetInstanceLabels']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A2</v1beta1/{name=projects/*/locations/*/instances/*}:setLabels:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/instances/*}'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StartInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StartInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/instances/*}:start:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StopInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['StopInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/locations/*/instances/*}:stop:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ResetInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ResetInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/instances/*}:reset:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ReportInstanceInfo']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ReportInstanceInfo']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/instances/*}:report:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['IsInstanceUpgradeable']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['IsInstanceUpgradeable']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02O\x12M/v1beta1/{notebook_instance=projects/*/locations/*/instances/*}:isUpgradeable'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstance']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstance']._serialized_options = b'\x88\x02\x01\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02?":/v1beta1/{name=projects/*/locations/*/instances/*}:upgrade:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstanceInternal']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['UpgradeInstanceInternal']._serialized_options = b'\x88\x02\x01\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=projects/*/locations/*/instances/*}:upgradeInternal:\x01*'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListEnvironments']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['ListEnvironments']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/environments'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['GetEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/environments/*}'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateEnvironment']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['CreateEnvironment']._serialized_options = b'\xcaA \n\x0bEnvironment\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02D"5/v1beta1/{parent=projects/*/locations/*}/environments:\x0benvironment'
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteEnvironment']._loaded_options = None
    _globals['_NOTEBOOKSERVICE'].methods_by_name['DeleteEnvironment']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/environments/*}'
    _globals['_OPERATIONMETADATA']._serialized_start = 336
    _globals['_OPERATIONMETADATA']._serialized_end = 575
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 577
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 659
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 662
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 792
    _globals['_GETINSTANCEREQUEST']._serialized_start = 794
    _globals['_GETINSTANCEREQUEST']._serialized_end = 833
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 836
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 971
    _globals['_REGISTERINSTANCEREQUEST']._serialized_start = 973
    _globals['_REGISTERINSTANCEREQUEST']._serialized_end = 1045
    _globals['_SETINSTANCEACCELERATORREQUEST']._serialized_start = 1048
    _globals['_SETINSTANCEACCELERATORREQUEST']._serialized_end = 1200
    _globals['_SETINSTANCEMACHINETYPEREQUEST']._serialized_start = 1202
    _globals['_SETINSTANCEMACHINETYPEREQUEST']._serialized_end = 1279
    _globals['_SETINSTANCELABELSREQUEST']._serialized_start = 1282
    _globals['_SETINSTANCELABELSREQUEST']._serialized_end = 1460
    _globals['_SETINSTANCELABELSREQUEST_LABELSENTRY']._serialized_start = 1415
    _globals['_SETINSTANCELABELSREQUEST_LABELSENTRY']._serialized_end = 1460
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 1462
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 1504
    _globals['_STARTINSTANCEREQUEST']._serialized_start = 1506
    _globals['_STARTINSTANCEREQUEST']._serialized_end = 1547
    _globals['_STOPINSTANCEREQUEST']._serialized_start = 1549
    _globals['_STOPINSTANCEREQUEST']._serialized_end = 1589
    _globals['_RESETINSTANCEREQUEST']._serialized_start = 1591
    _globals['_RESETINSTANCEREQUEST']._serialized_end = 1632
    _globals['_REPORTINSTANCEINFOREQUEST']._serialized_start = 1635
    _globals['_REPORTINSTANCEINFOREQUEST']._serialized_end = 1841
    _globals['_REPORTINSTANCEINFOREQUEST_METADATAENTRY']._serialized_start = 1794
    _globals['_REPORTINSTANCEINFOREQUEST_METADATAENTRY']._serialized_end = 1841
    _globals['_ISINSTANCEUPGRADEABLEREQUEST']._serialized_start = 1843
    _globals['_ISINSTANCEUPGRADEABLEREQUEST']._serialized_end = 1905
    _globals['_ISINSTANCEUPGRADEABLERESPONSE']._serialized_start = 1907
    _globals['_ISINSTANCEUPGRADEABLERESPONSE']._serialized_end = 2029
    _globals['_UPGRADEINSTANCEREQUEST']._serialized_start = 2031
    _globals['_UPGRADEINSTANCEREQUEST']._serialized_end = 2074
    _globals['_UPGRADEINSTANCEINTERNALREQUEST']._serialized_start = 2076
    _globals['_UPGRADEINSTANCEINTERNALREQUEST']._serialized_end = 2147
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_start = 2149
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_end = 2234
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_start = 2237
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_end = 2376
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 2378
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 2420
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_start = 2423
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_end = 2570
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_start = 2572
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_end = 2617
    _globals['_NOTEBOOKSERVICE']._serialized_start = 2620
    _globals['_NOTEBOOKSERVICE']._serialized_end = 6717