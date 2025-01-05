"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/tpu/v1/cloud_tpu.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/tpu/v1/cloud_tpu.proto\x12\x13google.cloud.tpu.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"9\n\x10SchedulingConfig\x12\x13\n\x0bpreemptible\x18\x01 \x01(\x08\x12\x10\n\x08reserved\x18\x02 \x01(\x08"3\n\x0fNetworkEndpoint\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05"\xb4\n\n\x04Node\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1d\n\x10accelerator_type\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x16\n\nip_address\x18\x08 \x01(\tB\x02\x18\x01\x12\x10\n\x04port\x18\x0e \x01(\tB\x02\x18\x01\x123\n\x05state\x18\t \x01(\x0e2\x1f.google.cloud.tpu.v1.Node.StateB\x03\xe0A\x03\x12\x1f\n\x12health_description\x18\n \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12tensorflow_version\x18\x0b \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07network\x18\x0c \x01(\t\x12\x12\n\ncidr_block\x18\r \x01(\t\x12\x1c\n\x0fservice_account\x18\x0f \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x11scheduling_config\x18\x11 \x01(\x0b2%.google.cloud.tpu.v1.SchedulingConfig\x12D\n\x11network_endpoints\x18\x15 \x03(\x0b2$.google.cloud.tpu.v1.NetworkEndpointB\x03\xe0A\x03\x120\n\x06health\x18\x16 \x01(\x0e2 .google.cloud.tpu.v1.Node.Health\x125\n\x06labels\x18\x18 \x03(\x0b2%.google.cloud.tpu.v1.Node.LabelsEntry\x12\x1e\n\x16use_service_networking\x18\x1b \x01(\x08\x12>\n\x0bapi_version\x18& \x01(\x0e2$.google.cloud.tpu.v1.Node.ApiVersionB\x03\xe0A\x03\x123\n\x08symptoms\x18\' \x03(\x0b2\x1c.google.cloud.tpu.v1.SymptomB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe1\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0e\n\nRESTARTING\x10\x03\x12\r\n\tREIMAGING\x10\x04\x12\x0c\n\x08DELETING\x10\x05\x12\r\n\tREPAIRING\x10\x06\x12\x0b\n\x07STOPPED\x10\x08\x12\x0c\n\x08STOPPING\x10\t\x12\x0c\n\x08STARTING\x10\n\x12\r\n\tPREEMPTED\x10\x0b\x12\x0e\n\nTERMINATED\x10\x0c\x12\n\n\x06HIDING\x10\r\x12\n\n\x06HIDDEN\x10\x0e\x12\x0c\n\x08UNHIDING\x10\x0f"\x89\x01\n\x06Health\x12\x16\n\x12HEALTH_UNSPECIFIED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\x18\n\x14DEPRECATED_UNHEALTHY\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x18\n\x14UNHEALTHY_TENSORFLOW\x10\x04\x12\x19\n\x15UNHEALTHY_MAINTENANCE\x10\x05"O\n\nApiVersion\x12\x1b\n\x17API_VERSION_UNSPECIFIED\x10\x00\x12\r\n\tV1_ALPHA1\x10\x01\x12\x06\n\x02V1\x10\x02\x12\r\n\tV2_ALPHA1\x10\x03:R\xeaAO\n\x17tpu.googleapis.com/Node\x124projects/{project}/locations/{location}/nodes/{node}"j\n\x10ListNodesRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17tpu.googleapis.com/Node\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"k\n\x11ListNodesResponse\x12(\n\x05nodes\x18\x01 \x03(\x0b2\x19.google.cloud.tpu.v1.Node\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"?\n\x0eGetNodeRequest\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\n\x17tpu.googleapis.com/Node"\x83\x01\n\x11CreateNodeRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17tpu.googleapis.com/Node\x12\x0f\n\x07node_id\x18\x02 \x01(\t\x12,\n\x04node\x18\x03 \x01(\x0b2\x19.google.cloud.tpu.v1.NodeB\x03\xe0A\x02"B\n\x11DeleteNodeRequest\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\n\x17tpu.googleapis.com/Node">\n\x12ReimageNodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12tensorflow_version\x18\x02 \x01(\t"\x1f\n\x0fStopNodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t" \n\x10StartNodeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xaf\x01\n\x11TensorFlowVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t:{\xeaAx\n$tpu.googleapis.com/TensorFlowVersion\x12Pprojects/{project}/locations/{location}/tensorFlowVersions/{tensor_flow_version}"Y\n\x1bGetTensorFlowVersionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$tpu.googleapis.com/TensorFlowVersion"\xa6\x01\n\x1dListTensorFlowVersionsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$tpu.googleapis.com/TensorFlowVersion\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12\x10\n\x08order_by\x18\x06 \x01(\t"\x93\x01\n\x1eListTensorFlowVersionsResponse\x12C\n\x13tensorflow_versions\x18\x01 \x03(\x0b2&.google.cloud.tpu.v1.TensorFlowVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xa3\x01\n\x0fAcceleratorType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t:t\xeaAq\n"tpu.googleapis.com/AcceleratorType\x12Kprojects/{project}/locations/{location}/acceleratorTypes/{accelerator_type}"U\n\x19GetAcceleratorTypeRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"tpu.googleapis.com/AcceleratorType"\xa2\x01\n\x1bListAcceleratorTypesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"tpu.googleapis.com/AcceleratorType\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t\x12\x10\n\x08order_by\x18\x06 \x01(\t"\x8d\x01\n\x1cListAcceleratorTypesResponse\x12?\n\x11accelerator_types\x18\x01 \x03(\x0b2$.google.cloud.tpu.v1.AcceleratorType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xd6\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x15\n\rstatus_detail\x18\x05 \x01(\t\x12\x18\n\x10cancel_requested\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t"\xc5\x02\n\x07Symptom\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12>\n\x0csymptom_type\x18\x02 \x01(\x0e2(.google.cloud.tpu.v1.Symptom.SymptomType\x12\x0f\n\x07details\x18\x03 \x01(\t\x12\x11\n\tworker_id\x18\x04 \x01(\t"\xa4\x01\n\x0bSymptomType\x12\x1c\n\x18SYMPTOM_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nLOW_MEMORY\x10\x01\x12\x11\n\rOUT_OF_MEMORY\x10\x02\x12\x15\n\x11EXECUTE_TIMED_OUT\x10\x03\x12\x13\n\x0fMESH_BUILD_FAIL\x10\x04\x12\x15\n\x11HBM_OUT_OF_MEMORY\x10\x05\x12\x11\n\rPROJECT_ABUSE\x10\x062\xde\x0f\n\x03Tpu\x12\x96\x01\n\tListNodes\x12%.google.cloud.tpu.v1.ListNodesRequest\x1a&.google.cloud.tpu.v1.ListNodesResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=projects/*/locations/*}/nodes\x12\x83\x01\n\x07GetNode\x12#.google.cloud.tpu.v1.GetNodeRequest\x1a\x19.google.cloud.tpu.v1.Node"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=projects/*/locations/*/nodes/*}\x12\xbe\x01\n\nCreateNode\x12&.google.cloud.tpu.v1.CreateNodeRequest\x1a\x1d.google.longrunning.Operation"i\xcaA\x19\n\x04Node\x12\x11OperationMetadata\xdaA\x13parent,node,node_id\x82\xd3\xe4\x93\x021")/v1/{parent=projects/*/locations/*}/nodes:\x04node\x12\xa9\x01\n\nDeleteNode\x12&.google.cloud.tpu.v1.DeleteNodeRequest\x1a\x1d.google.longrunning.Operation"T\xcaA\x19\n\x04Node\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02+*)/v1/{name=projects/*/locations/*/nodes/*}\x12\xaf\x01\n\x0bReimageNode\x12\'.google.cloud.tpu.v1.ReimageNodeRequest\x1a\x1d.google.longrunning.Operation"X\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/nodes/*}:reimage:\x01*\x12\xa6\x01\n\x08StopNode\x12$.google.cloud.tpu.v1.StopNodeRequest\x1a\x1d.google.longrunning.Operation"U\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/locations/*/nodes/*}:stop:\x01*\x12\xa9\x01\n\tStartNode\x12%.google.cloud.tpu.v1.StartNodeRequest\x1a\x1d.google.longrunning.Operation"V\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/nodes/*}:start:\x01*\x12\xca\x01\n\x16ListTensorFlowVersions\x122.google.cloud.tpu.v1.ListTensorFlowVersionsRequest\x1a3.google.cloud.tpu.v1.ListTensorFlowVersionsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*}/tensorflowVersions\x12\xb7\x01\n\x14GetTensorFlowVersion\x120.google.cloud.tpu.v1.GetTensorFlowVersionRequest\x1a&.google.cloud.tpu.v1.TensorFlowVersion"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/tensorflowVersions/*}\x12\xc2\x01\n\x14ListAcceleratorTypes\x120.google.cloud.tpu.v1.ListAcceleratorTypesRequest\x1a1.google.cloud.tpu.v1.ListAcceleratorTypesResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/acceleratorTypes\x12\xaf\x01\n\x12GetAcceleratorType\x12..google.cloud.tpu.v1.GetAcceleratorTypeRequest\x1a$.google.cloud.tpu.v1.AcceleratorType"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/acceleratorTypes/*}\x1aF\xcaA\x12tpu.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBU\n\x17com.google.cloud.tpu.v1B\rCloudTpuProtoP\x01Z)cloud.google.com/go/tpu/apiv1/tpupb;tpupbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tpu.v1.cloud_tpu_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.tpu.v1B\rCloudTpuProtoP\x01Z)cloud.google.com/go/tpu/apiv1/tpupb;tpupb'
    _globals['_NODE_LABELSENTRY']._loaded_options = None
    _globals['_NODE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NODE'].fields_by_name['name']._loaded_options = None
    _globals['_NODE'].fields_by_name['name']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_NODE'].fields_by_name['accelerator_type']._loaded_options = None
    _globals['_NODE'].fields_by_name['accelerator_type']._serialized_options = b'\xe0A\x02'
    _globals['_NODE'].fields_by_name['ip_address']._loaded_options = None
    _globals['_NODE'].fields_by_name['ip_address']._serialized_options = b'\x18\x01'
    _globals['_NODE'].fields_by_name['port']._loaded_options = None
    _globals['_NODE'].fields_by_name['port']._serialized_options = b'\x18\x01'
    _globals['_NODE'].fields_by_name['state']._loaded_options = None
    _globals['_NODE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['health_description']._loaded_options = None
    _globals['_NODE'].fields_by_name['health_description']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['tensorflow_version']._loaded_options = None
    _globals['_NODE'].fields_by_name['tensorflow_version']._serialized_options = b'\xe0A\x02'
    _globals['_NODE'].fields_by_name['service_account']._loaded_options = None
    _globals['_NODE'].fields_by_name['service_account']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['create_time']._loaded_options = None
    _globals['_NODE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['network_endpoints']._loaded_options = None
    _globals['_NODE'].fields_by_name['network_endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['api_version']._loaded_options = None
    _globals['_NODE'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_NODE'].fields_by_name['symptoms']._loaded_options = None
    _globals['_NODE'].fields_by_name['symptoms']._serialized_options = b'\xe0A\x03'
    _globals['_NODE']._loaded_options = None
    _globals['_NODE']._serialized_options = b'\xeaAO\n\x17tpu.googleapis.com/Node\x124projects/{project}/locations/{location}/nodes/{node}'
    _globals['_LISTNODESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNODESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17tpu.googleapis.com/Node'
    _globals['_GETNODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x19\n\x17tpu.googleapis.com/Node'
    _globals['_CREATENODEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENODEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17tpu.googleapis.com/Node'
    _globals['_CREATENODEREQUEST'].fields_by_name['node']._loaded_options = None
    _globals['_CREATENODEREQUEST'].fields_by_name['node']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x19\n\x17tpu.googleapis.com/Node'
    _globals['_TENSORFLOWVERSION']._loaded_options = None
    _globals['_TENSORFLOWVERSION']._serialized_options = b'\xeaAx\n$tpu.googleapis.com/TensorFlowVersion\x12Pprojects/{project}/locations/{location}/tensorFlowVersions/{tensor_flow_version}'
    _globals['_GETTENSORFLOWVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTENSORFLOWVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$tpu.googleapis.com/TensorFlowVersion'
    _globals['_LISTTENSORFLOWVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTENSORFLOWVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$tpu.googleapis.com/TensorFlowVersion'
    _globals['_ACCELERATORTYPE']._loaded_options = None
    _globals['_ACCELERATORTYPE']._serialized_options = b'\xeaAq\n"tpu.googleapis.com/AcceleratorType\x12Kprojects/{project}/locations/{location}/acceleratorTypes/{accelerator_type}'
    _globals['_GETACCELERATORTYPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCELERATORTYPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"tpu.googleapis.com/AcceleratorType'
    _globals['_LISTACCELERATORTYPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCELERATORTYPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"tpu.googleapis.com/AcceleratorType'
    _globals['_TPU']._loaded_options = None
    _globals['_TPU']._serialized_options = b'\xcaA\x12tpu.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TPU'].methods_by_name['ListNodes']._loaded_options = None
    _globals['_TPU'].methods_by_name['ListNodes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=projects/*/locations/*}/nodes'
    _globals['_TPU'].methods_by_name['GetNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['GetNode']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1/{name=projects/*/locations/*/nodes/*}'
    _globals['_TPU'].methods_by_name['CreateNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['CreateNode']._serialized_options = b'\xcaA\x19\n\x04Node\x12\x11OperationMetadata\xdaA\x13parent,node,node_id\x82\xd3\xe4\x93\x021")/v1/{parent=projects/*/locations/*}/nodes:\x04node'
    _globals['_TPU'].methods_by_name['DeleteNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['DeleteNode']._serialized_options = b'\xcaA\x19\n\x04Node\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02+*)/v1/{name=projects/*/locations/*/nodes/*}'
    _globals['_TPU'].methods_by_name['ReimageNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['ReimageNode']._serialized_options = b'\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/nodes/*}:reimage:\x01*'
    _globals['_TPU'].methods_by_name['StopNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['StopNode']._serialized_options = b'\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/locations/*/nodes/*}:stop:\x01*'
    _globals['_TPU'].methods_by_name['StartNode']._loaded_options = None
    _globals['_TPU'].methods_by_name['StartNode']._serialized_options = b'\xcaA\x19\n\x04Node\x12\x11OperationMetadata\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/nodes/*}:start:\x01*'
    _globals['_TPU'].methods_by_name['ListTensorFlowVersions']._loaded_options = None
    _globals['_TPU'].methods_by_name['ListTensorFlowVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*}/tensorflowVersions'
    _globals['_TPU'].methods_by_name['GetTensorFlowVersion']._loaded_options = None
    _globals['_TPU'].methods_by_name['GetTensorFlowVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/tensorflowVersions/*}'
    _globals['_TPU'].methods_by_name['ListAcceleratorTypes']._loaded_options = None
    _globals['_TPU'].methods_by_name['ListAcceleratorTypes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/acceleratorTypes'
    _globals['_TPU'].methods_by_name['GetAcceleratorType']._loaded_options = None
    _globals['_TPU'].methods_by_name['GetAcceleratorType']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/acceleratorTypes/*}'
    _globals['_SCHEDULINGCONFIG']._serialized_start = 245
    _globals['_SCHEDULINGCONFIG']._serialized_end = 302
    _globals['_NETWORKENDPOINT']._serialized_start = 304
    _globals['_NETWORKENDPOINT']._serialized_end = 355
    _globals['_NODE']._serialized_start = 358
    _globals['_NODE']._serialized_end = 1690
    _globals['_NODE_LABELSENTRY']._serialized_start = 1112
    _globals['_NODE_LABELSENTRY']._serialized_end = 1157
    _globals['_NODE_STATE']._serialized_start = 1160
    _globals['_NODE_STATE']._serialized_end = 1385
    _globals['_NODE_HEALTH']._serialized_start = 1388
    _globals['_NODE_HEALTH']._serialized_end = 1525
    _globals['_NODE_APIVERSION']._serialized_start = 1527
    _globals['_NODE_APIVERSION']._serialized_end = 1606
    _globals['_LISTNODESREQUEST']._serialized_start = 1692
    _globals['_LISTNODESREQUEST']._serialized_end = 1798
    _globals['_LISTNODESRESPONSE']._serialized_start = 1800
    _globals['_LISTNODESRESPONSE']._serialized_end = 1907
    _globals['_GETNODEREQUEST']._serialized_start = 1909
    _globals['_GETNODEREQUEST']._serialized_end = 1972
    _globals['_CREATENODEREQUEST']._serialized_start = 1975
    _globals['_CREATENODEREQUEST']._serialized_end = 2106
    _globals['_DELETENODEREQUEST']._serialized_start = 2108
    _globals['_DELETENODEREQUEST']._serialized_end = 2174
    _globals['_REIMAGENODEREQUEST']._serialized_start = 2176
    _globals['_REIMAGENODEREQUEST']._serialized_end = 2238
    _globals['_STOPNODEREQUEST']._serialized_start = 2240
    _globals['_STOPNODEREQUEST']._serialized_end = 2271
    _globals['_STARTNODEREQUEST']._serialized_start = 2273
    _globals['_STARTNODEREQUEST']._serialized_end = 2305
    _globals['_TENSORFLOWVERSION']._serialized_start = 2308
    _globals['_TENSORFLOWVERSION']._serialized_end = 2483
    _globals['_GETTENSORFLOWVERSIONREQUEST']._serialized_start = 2485
    _globals['_GETTENSORFLOWVERSIONREQUEST']._serialized_end = 2574
    _globals['_LISTTENSORFLOWVERSIONSREQUEST']._serialized_start = 2577
    _globals['_LISTTENSORFLOWVERSIONSREQUEST']._serialized_end = 2743
    _globals['_LISTTENSORFLOWVERSIONSRESPONSE']._serialized_start = 2746
    _globals['_LISTTENSORFLOWVERSIONSRESPONSE']._serialized_end = 2893
    _globals['_ACCELERATORTYPE']._serialized_start = 2896
    _globals['_ACCELERATORTYPE']._serialized_end = 3059
    _globals['_GETACCELERATORTYPEREQUEST']._serialized_start = 3061
    _globals['_GETACCELERATORTYPEREQUEST']._serialized_end = 3146
    _globals['_LISTACCELERATORTYPESREQUEST']._serialized_start = 3149
    _globals['_LISTACCELERATORTYPESREQUEST']._serialized_end = 3311
    _globals['_LISTACCELERATORTYPESRESPONSE']._serialized_start = 3314
    _globals['_LISTACCELERATORTYPESRESPONSE']._serialized_end = 3455
    _globals['_OPERATIONMETADATA']._serialized_start = 3458
    _globals['_OPERATIONMETADATA']._serialized_end = 3672
    _globals['_SYMPTOM']._serialized_start = 3675
    _globals['_SYMPTOM']._serialized_end = 4000
    _globals['_SYMPTOM_SYMPTOMTYPE']._serialized_start = 3836
    _globals['_SYMPTOM_SYMPTOMTYPE']._serialized_end = 4000
    _globals['_TPU']._serialized_start = 4003
    _globals['_TPU']._serialized_end = 6017