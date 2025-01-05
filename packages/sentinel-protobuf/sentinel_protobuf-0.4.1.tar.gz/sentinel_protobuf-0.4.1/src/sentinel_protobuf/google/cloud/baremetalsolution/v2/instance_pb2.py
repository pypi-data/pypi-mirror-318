"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.baremetalsolution.v2 import common_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_common__pb2
from .....google.cloud.baremetalsolution.v2 import lun_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_lun__pb2
from .....google.cloud.baremetalsolution.v2 import network_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_network__pb2
from .....google.cloud.baremetalsolution.v2 import volume_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_volume__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/baremetalsolution/v2/instance.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/baremetalsolution/v2/common.proto\x1a+google/cloud/baremetalsolution/v2/lun.proto\x1a/google/cloud/baremetalsolution/v2/network.proto\x1a.google/cloud/baremetalsolution/v2/volume.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc9\t\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x0f\n\x02id\x18\x0b \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x19\n\x0cmachine_type\x18\x04 \x01(\tB\x03\xe0A\x05\x12E\n\x05state\x18\x05 \x01(\x0e21.google.cloud.baremetalsolution.v2.Instance.StateB\x03\xe0A\x03\x12\x1e\n\x16hyperthreading_enabled\x18\x06 \x01(\x08\x12G\n\x06labels\x18\x07 \x03(\x0b27.google.cloud.baremetalsolution.v2.Instance.LabelsEntry\x129\n\x04luns\x18\x08 \x03(\x0b2&.google.cloud.baremetalsolution.v2.LunB\x03\xe0A\x05\x12?\n\x07volumes\x18\x10 \x03(\x0b2).google.cloud.baremetalsolution.v2.VolumeB\x03\xe0A\x04\x12A\n\x08networks\x18\t \x03(\x0b2*.google.cloud.baremetalsolution.v2.NetworkB\x03\xe0A\x03\x12/\n"interactive_serial_console_enabled\x18\n \x01(\x08B\x03\xe0A\x03\x12\x10\n\x08os_image\x18\x0c \x01(\t\x12\x10\n\x03pod\x18\r \x01(\tB\x03\xe0A\x05\x12U\n\x10network_template\x18\x0e \x01(\tB;\xfaA8\n6baremetalsolution.googleapis.com/ServerNetworkTemplate\x12O\n\x12logical_interfaces\x18\x0f \x03(\x0b23.google.cloud.baremetalsolution.v2.LogicalInterface\x12\x17\n\nlogin_info\x18\x11 \x01(\tB\x03\xe0A\x03\x12L\n\x10workload_profile\x18\x12 \x01(\x0e22.google.cloud.baremetalsolution.v2.WorkloadProfile\x12\x1d\n\x10firmware_version\x18\x13 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x82\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0b\n\x07DELETED\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STARTING\x10\x05\x12\x0c\n\x08STOPPING\x10\x06\x12\x0c\n\x08SHUTDOWN\x10\x07:l\xeaAi\n)baremetalsolution.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}"U\n\x12GetInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance"\x88\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x85\x01\n\x15ListInstancesResponse\x12>\n\tinstances\x18\x01 \x03(\x0b2+.google.cloud.baremetalsolution.v2.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x8c\x01\n\x15UpdateInstanceRequest\x12B\n\x08instance\x18\x01 \x01(\x0b2+.google.cloud.baremetalsolution.v2.InstanceB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"v\n\x15RenameInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance\x12\x1c\n\x0fnew_instance_id\x18\x02 \x01(\tB\x03\xe0A\x02"W\n\x14ResetInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance"W\n\x14StartInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance"\x17\n\x15StartInstanceResponse"V\n\x13StopInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance"\x16\n\x14StopInstanceResponse"h\n%EnableInteractiveSerialConsoleRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance"(\n&EnableInteractiveSerialConsoleResponse"i\n&DisableInteractiveSerialConsoleRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance")\n\'DisableInteractiveSerialConsoleResponse"\xa7\x01\n\x10DetachLunRequest\x12C\n\x08instance\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance\x129\n\x03lun\x18\x02 \x01(\tB,\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/Lun\x12\x13\n\x0bskip_reboot\x18\x03 \x01(\x08"\xac\x04\n\x15ServerNetworkTemplate\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12!\n\x19applicable_instance_types\x18\x02 \x03(\t\x12e\n\x12logical_interfaces\x18\x03 \x03(\x0b2I.google.cloud.baremetalsolution.v2.ServerNetworkTemplate.LogicalInterface\x1a\xdd\x01\n\x10LogicalInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\x12e\n\x04type\x18\x02 \x01(\x0e2W.google.cloud.baremetalsolution.v2.ServerNetworkTemplate.LogicalInterface.InterfaceType\x12\x10\n\x08required\x18\x03 \x01(\x08"B\n\rInterfaceType\x12\x1e\n\x1aINTERFACE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOND\x10\x01\x12\x07\n\x03NIC\x10\x02:\x95\x01\xeaA\x91\x01\n6baremetalsolution.googleapis.com/ServerNetworkTemplate\x12Wprojects/{project}/locations/{location}/serverNetworkTemplate/{server_network_template}B\xfc\x01\n%com.google.cloud.baremetalsolution.v2B\rInstanceProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\rInstanceProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_INSTANCE'].fields_by_name['id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['machine_type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['machine_type']._serialized_options = b'\xe0A\x05'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['luns']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['luns']._serialized_options = b'\xe0A\x05'
    _globals['_INSTANCE'].fields_by_name['volumes']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['volumes']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['networks']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['networks']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['interactive_serial_console_enabled']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['interactive_serial_console_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['pod']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['pod']._serialized_options = b'\xe0A\x05'
    _globals['_INSTANCE'].fields_by_name['network_template']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['network_template']._serialized_options = b'\xfaA8\n6baremetalsolution.googleapis.com/ServerNetworkTemplate'
    _globals['_INSTANCE'].fields_by_name['login_info']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['login_info']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['firmware_version']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['firmware_version']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAi\n)baremetalsolution.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_RENAMEINSTANCEREQUEST'].fields_by_name['new_instance_id']._loaded_options = None
    _globals['_RENAMEINSTANCEREQUEST'].fields_by_name['new_instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_ENABLEINTERACTIVESERIALCONSOLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENABLEINTERACTIVESERIALCONSOLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_DISABLEINTERACTIVESERIALCONSOLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DISABLEINTERACTIVESERIALCONSOLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_DETACHLUNREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_DETACHLUNREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/Instance'
    _globals['_DETACHLUNREQUEST'].fields_by_name['lun']._loaded_options = None
    _globals['_DETACHLUNREQUEST'].fields_by_name['lun']._serialized_options = b'\xe0A\x02\xfaA&\n$baremetalsolution.googleapis.com/Lun'
    _globals['_SERVERNETWORKTEMPLATE'].fields_by_name['name']._loaded_options = None
    _globals['_SERVERNETWORKTEMPLATE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SERVERNETWORKTEMPLATE']._loaded_options = None
    _globals['_SERVERNETWORKTEMPLATE']._serialized_options = b'\xeaA\x91\x01\n6baremetalsolution.googleapis.com/ServerNetworkTemplate\x12Wprojects/{project}/locations/{location}/serverNetworkTemplate/{server_network_template}'
    _globals['_INSTANCE']._serialized_start = 405
    _globals['_INSTANCE']._serialized_end = 1630
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 1342
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 1387
    _globals['_INSTANCE_STATE']._serialized_start = 1390
    _globals['_INSTANCE_STATE']._serialized_end = 1520
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1632
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1717
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1720
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1856
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1859
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1992
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 1995
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 2135
    _globals['_RENAMEINSTANCEREQUEST']._serialized_start = 2137
    _globals['_RENAMEINSTANCEREQUEST']._serialized_end = 2255
    _globals['_RESETINSTANCEREQUEST']._serialized_start = 2257
    _globals['_RESETINSTANCEREQUEST']._serialized_end = 2344
    _globals['_STARTINSTANCEREQUEST']._serialized_start = 2346
    _globals['_STARTINSTANCEREQUEST']._serialized_end = 2433
    _globals['_STARTINSTANCERESPONSE']._serialized_start = 2435
    _globals['_STARTINSTANCERESPONSE']._serialized_end = 2458
    _globals['_STOPINSTANCEREQUEST']._serialized_start = 2460
    _globals['_STOPINSTANCEREQUEST']._serialized_end = 2546
    _globals['_STOPINSTANCERESPONSE']._serialized_start = 2548
    _globals['_STOPINSTANCERESPONSE']._serialized_end = 2570
    _globals['_ENABLEINTERACTIVESERIALCONSOLEREQUEST']._serialized_start = 2572
    _globals['_ENABLEINTERACTIVESERIALCONSOLEREQUEST']._serialized_end = 2676
    _globals['_ENABLEINTERACTIVESERIALCONSOLERESPONSE']._serialized_start = 2678
    _globals['_ENABLEINTERACTIVESERIALCONSOLERESPONSE']._serialized_end = 2718
    _globals['_DISABLEINTERACTIVESERIALCONSOLEREQUEST']._serialized_start = 2720
    _globals['_DISABLEINTERACTIVESERIALCONSOLEREQUEST']._serialized_end = 2825
    _globals['_DISABLEINTERACTIVESERIALCONSOLERESPONSE']._serialized_start = 2827
    _globals['_DISABLEINTERACTIVESERIALCONSOLERESPONSE']._serialized_end = 2868
    _globals['_DETACHLUNREQUEST']._serialized_start = 2871
    _globals['_DETACHLUNREQUEST']._serialized_end = 3038
    _globals['_SERVERNETWORKTEMPLATE']._serialized_start = 3041
    _globals['_SERVERNETWORKTEMPLATE']._serialized_end = 3597
    _globals['_SERVERNETWORKTEMPLATE_LOGICALINTERFACE']._serialized_start = 3224
    _globals['_SERVERNETWORKTEMPLATE_LOGICALINTERFACE']._serialized_end = 3445
    _globals['_SERVERNETWORKTEMPLATE_LOGICALINTERFACE_INTERFACETYPE']._serialized_start = 3379
    _globals['_SERVERNETWORKTEMPLATE_LOGICALINTERFACE_INTERFACETYPE']._serialized_end = 3445