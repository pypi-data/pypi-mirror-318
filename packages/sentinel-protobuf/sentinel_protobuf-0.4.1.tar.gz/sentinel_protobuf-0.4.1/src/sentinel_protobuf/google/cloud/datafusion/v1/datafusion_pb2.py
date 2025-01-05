"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datafusion/v1/datafusion.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/datafusion/v1/datafusion.proto\x12\x1agoogle.cloud.datafusion.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"7\n\rNetworkConfig\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x15\n\rip_allocation\x18\x02 \x01(\t"\xdd\x01\n\x07Version\x12\x16\n\x0eversion_number\x18\x01 \x01(\t\x12\x17\n\x0fdefault_version\x18\x02 \x01(\x08\x12\x1a\n\x12available_features\x18\x03 \x03(\t\x126\n\x04type\x18\x04 \x01(\x0e2(.google.cloud.datafusion.v1.Version.Type"M\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cTYPE_PREVIEW\x10\x01\x12\x1d\n\x19TYPE_GENERAL_AVAILABILITY\x10\x02"\xc7\x02\n\x0bAccelerator\x12Q\n\x10accelerator_type\x18\x01 \x01(\x0e27.google.cloud.datafusion.v1.Accelerator.AcceleratorType\x12<\n\x05state\x18\x02 \x01(\x0e2-.google.cloud.datafusion.v1.Accelerator.State"_\n\x0fAcceleratorType\x12 \n\x1cACCELERATOR_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03CDC\x10\x01\x12\x0e\n\nHEALTHCARE\x10\x02\x12\x11\n\rCCAI_INSIGHTS\x10\x03"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03"P\n\x0fCryptoKeyConfig\x12=\n\rkey_reference\x18\x01 \x01(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey"\xd2\r\n\x08Instance\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x03\xfaA$\n"datafusion.googleapis.com/Instance\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12<\n\x04type\x18\x03 \x01(\x0e2).google.cloud.datafusion.v1.Instance.TypeB\x03\xe0A\x02\x12"\n\x1aenable_stackdriver_logging\x18\x04 \x01(\x08\x12%\n\x1denable_stackdriver_monitoring\x18\x05 \x01(\x08\x12\x18\n\x10private_instance\x18\x06 \x01(\x08\x12A\n\x0enetwork_config\x18\x07 \x01(\x0b2).google.cloud.datafusion.v1.NetworkConfig\x12@\n\x06labels\x18\x08 \x03(\x0b20.google.cloud.datafusion.v1.Instance.LabelsEntry\x12B\n\x07options\x18\t \x03(\x0b21.google.cloud.datafusion.v1.Instance.OptionsEntry\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x05state\x18\x0c \x01(\x0e2*.google.cloud.datafusion.v1.Instance.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\r \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10service_endpoint\x18\x0e \x01(\tB\x03\xe0A\x03\x12\x0c\n\x04zone\x18\x0f \x01(\t\x12\x0f\n\x07version\x18\x10 \x01(\t\x12\x1e\n\x0fservice_account\x18\x11 \x01(\tB\x05\x18\x01\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x12 \x01(\t\x12>\n\x11available_version\x18\x13 \x03(\x0b2#.google.cloud.datafusion.v1.Version\x12\x19\n\x0capi_endpoint\x18\x14 \x01(\tB\x03\xe0A\x03\x12\x17\n\ngcs_bucket\x18\x15 \x01(\tB\x03\xe0A\x03\x12=\n\x0caccelerators\x18\x16 \x03(\x0b2\'.google.cloud.datafusion.v1.Accelerator\x12\x1f\n\x12p4_service_account\x18\x17 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11tenant_project_id\x18\x18 \x01(\tB\x03\xe0A\x03\x12 \n\x18dataproc_service_account\x18\x19 \x01(\t\x12\x13\n\x0benable_rbac\x18\x1b \x01(\x08\x12F\n\x11crypto_key_config\x18\x1c \x01(\x0b2+.google.cloud.datafusion.v1.CryptoKeyConfig\x12Q\n\x0fdisabled_reason\x18\x1d \x03(\x0e23.google.cloud.datafusion.v1.Instance.DisabledReasonB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"F\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x0e\n\nENTERPRISE\x10\x02\x12\r\n\tDEVELOPER\x10\x03"\xb4\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\r\n\tUPGRADING\x10\x05\x12\x0e\n\nRESTARTING\x10\x06\x12\x0c\n\x08UPDATING\x10\x07\x12\x11\n\rAUTO_UPDATING\x10\x08\x12\x12\n\x0eAUTO_UPGRADING\x10\t\x12\x0c\n\x08DISABLED\x10\n"D\n\x0eDisabledReason\x12\x1f\n\x1bDISABLED_REASON_UNSPECIFIED\x10\x00\x12\x11\n\rKMS_KEY_ISSUE\x10\x01:e\xeaAb\n"datafusion.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}"\x9a\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"~\n\x15ListInstancesResponse\x127\n\tinstances\x18\x01 \x03(\x0b2$.google.cloud.datafusion.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x9b\x01\n\x1cListAvailableVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x19\n\x11latest_patch_only\x18\x04 \x01(\x08"y\n\x1dListAvailableVersionsResponse\x12?\n\x12available_versions\x18\x01 \x03(\x0b2#.google.cloud.datafusion.v1.Version\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x12GetInstanceRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance"\xa4\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x08instance\x18\x03 \x01(\x0b2$.google.cloud.datafusion.v1.Instance"Q\n\x15DeleteInstanceRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance"\x85\x01\n\x15UpdateInstanceRequest\x12;\n\x08instance\x18\x01 \x01(\x0b2$.google.cloud.datafusion.v1.InstanceB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"R\n\x16RestartInstanceRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance"\xf5\x02\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x15\n\rstatus_detail\x18\x05 \x01(\t\x12\x1e\n\x16requested_cancellation\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t\x12^\n\x11additional_status\x18\x08 \x03(\x0b2C.google.cloud.datafusion.v1.OperationMetadata.AdditionalStatusEntry\x1a7\n\x15AdditionalStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\xd7\x0b\n\nDataFusion\x12\xcb\x01\n\x15ListAvailableVersions\x128.google.cloud.datafusion.v1.ListAvailableVersionsRequest\x1a9.google.cloud.datafusion.v1.ListAvailableVersionsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/versions\x12\xab\x01\n\rListInstances\x120.google.cloud.datafusion.v1.ListInstancesRequest\x1a1.google.cloud.datafusion.v1.ListInstancesResponse"5\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\x9a\x01\n\x0bGetInstance\x12..google.cloud.datafusion.v1.GetInstanceRequest\x1a$.google.cloud.datafusion.v1.Instance"5\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\xe1\x01\n\x0eCreateInstance\x121.google.cloud.datafusion.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xcd\x01\n\x0eDeleteInstance\x121.google.cloud.datafusion.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x12\xe3\x01\n\x0eUpdateInstance\x121.google.cloud.datafusion.v1.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\xc6\x01\n\x0fRestartInstance\x122.google.cloud.datafusion.v1.RestartInstanceRequest\x1a\x1d.google.longrunning.Operation"`\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/instances/*}:restart:\x01*\x1aM\xcaA\x19datafusion.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb7\x02\n\x1ecom.google.cloud.datafusion.v1P\x01Z>cloud.google.com/go/datafusion/apiv1/datafusionpb;datafusionpb\xaa\x02\x1aGoogle.Cloud.DataFusion.V1\xca\x02\x1aGoogle\\Cloud\\DataFusion\\V1\xea\x02\x1dGoogle::Cloud::DataFusion::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datafusion.v1.datafusion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.datafusion.v1P\x01Z>cloud.google.com/go/datafusion/apiv1/datafusionpb;datafusionpb\xaa\x02\x1aGoogle.Cloud.DataFusion.V1\xca\x02\x1aGoogle\\Cloud\\DataFusion\\V1\xea\x02\x1dGoogle::Cloud::DataFusion::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}'
    _globals['_CRYPTOKEYCONFIG'].fields_by_name['key_reference']._loaded_options = None
    _globals['_CRYPTOKEYCONFIG'].fields_by_name['key_reference']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE_OPTIONSENTRY']._loaded_options = None
    _globals['_INSTANCE_OPTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA$\n"datafusion.googleapis.com/Instance'
    _globals['_INSTANCE'].fields_by_name['type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state_message']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['service_endpoint']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['service_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['service_account']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['service_account']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['api_endpoint']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['gcs_bucket']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['gcs_bucket']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['p4_service_account']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['p4_service_account']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['tenant_project_id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['tenant_project_id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['disabled_reason']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['disabled_reason']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAb\n"datafusion.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTAVAILABLEVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAVAILABLEVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_RESTARTINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTARTINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"datafusion.googleapis.com/Instance'
    _globals['_OPERATIONMETADATA_ADDITIONALSTATUSENTRY']._loaded_options = None
    _globals['_OPERATIONMETADATA_ADDITIONALSTATUSENTRY']._serialized_options = b'8\x01'
    _globals['_DATAFUSION']._loaded_options = None
    _globals['_DATAFUSION']._serialized_options = b'\xcaA\x19datafusion.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAFUSION'].methods_by_name['ListAvailableVersions']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['ListAvailableVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/versions'
    _globals['_DATAFUSION'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['ListInstances']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances'
    _globals['_DATAFUSION'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['GetInstance']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_DATAFUSION'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_DATAFUSION'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_DATAFUSION'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance'
    _globals['_DATAFUSION'].methods_by_name['RestartInstance']._loaded_options = None
    _globals['_DATAFUSION'].methods_by_name['RestartInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/instances/*}:restart:\x01*'
    _globals['_NETWORKCONFIG']._serialized_start = 294
    _globals['_NETWORKCONFIG']._serialized_end = 349
    _globals['_VERSION']._serialized_start = 352
    _globals['_VERSION']._serialized_end = 573
    _globals['_VERSION_TYPE']._serialized_start = 496
    _globals['_VERSION_TYPE']._serialized_end = 573
    _globals['_ACCELERATOR']._serialized_start = 576
    _globals['_ACCELERATOR']._serialized_end = 903
    _globals['_ACCELERATOR_ACCELERATORTYPE']._serialized_start = 736
    _globals['_ACCELERATOR_ACCELERATORTYPE']._serialized_end = 831
    _globals['_ACCELERATOR_STATE']._serialized_start = 833
    _globals['_ACCELERATOR_STATE']._serialized_end = 903
    _globals['_CRYPTOKEYCONFIG']._serialized_start = 905
    _globals['_CRYPTOKEYCONFIG']._serialized_end = 985
    _globals['_INSTANCE']._serialized_start = 988
    _globals['_INSTANCE']._serialized_end = 2734
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 2213
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 2258
    _globals['_INSTANCE_OPTIONSENTRY']._serialized_start = 2260
    _globals['_INSTANCE_OPTIONSENTRY']._serialized_end = 2306
    _globals['_INSTANCE_TYPE']._serialized_start = 2308
    _globals['_INSTANCE_TYPE']._serialized_end = 2378
    _globals['_INSTANCE_STATE']._serialized_start = 2381
    _globals['_INSTANCE_STATE']._serialized_end = 2561
    _globals['_INSTANCE_DISABLEDREASON']._serialized_start = 2563
    _globals['_INSTANCE_DISABLEDREASON']._serialized_end = 2631
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 2737
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 2891
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 2893
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 3019
    _globals['_LISTAVAILABLEVERSIONSREQUEST']._serialized_start = 3022
    _globals['_LISTAVAILABLEVERSIONSREQUEST']._serialized_end = 3177
    _globals['_LISTAVAILABLEVERSIONSRESPONSE']._serialized_start = 3179
    _globals['_LISTAVAILABLEVERSIONSRESPONSE']._serialized_end = 3300
    _globals['_GETINSTANCEREQUEST']._serialized_start = 3302
    _globals['_GETINSTANCEREQUEST']._serialized_end = 3380
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 3383
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 3547
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 3549
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 3630
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 3633
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 3766
    _globals['_RESTARTINSTANCEREQUEST']._serialized_start = 3768
    _globals['_RESTARTINSTANCEREQUEST']._serialized_end = 3850
    _globals['_OPERATIONMETADATA']._serialized_start = 3853
    _globals['_OPERATIONMETADATA']._serialized_end = 4226
    _globals['_OPERATIONMETADATA_ADDITIONALSTATUSENTRY']._serialized_start = 4171
    _globals['_OPERATIONMETADATA_ADDITIONALSTATUSENTRY']._serialized_end = 4226
    _globals['_DATAFUSION']._serialized_start = 4229
    _globals['_DATAFUSION']._serialized_end = 5724