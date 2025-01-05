"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v2/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.notebooks.v2 import gce_setup_pb2 as google_dot_cloud_dot_notebooks_dot_v2_dot_gce__setup__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/notebooks/v2/instance.proto\x12\x19google.cloud.notebooks.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/notebooks/v2/gce_setup.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfd\x03\n\x13UpgradeHistoryEntry\x12\x15\n\x08snapshot\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08vm_image\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fcontainer_image\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x16\n\tframework\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07version\x18\x05 \x01(\tB\x03\xe0A\x01\x12H\n\x05state\x18\x06 \x01(\x0e24.google.cloud.notebooks.v2.UpgradeHistoryEntry.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x05\x12J\n\x06action\x18\x08 \x01(\x0e25.google.cloud.notebooks.v2.UpgradeHistoryEntry.ActionB\x03\xe0A\x01\x12\x1b\n\x0etarget_version\x18\t \x01(\tB\x03\xe0A\x01"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03";\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07UPGRADE\x10\x01\x12\x0c\n\x08ROLLBACK\x10\x02"\x96\x07\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12=\n\tgce_setup\x18\x02 \x01(\x0b2#.google.cloud.notebooks.v2.GceSetupB\x03\xe0A\x01H\x00\x12\x16\n\tproxy_uri\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x0finstance_owners\x18\x04 \x03(\tB\x06\xe0A\x04\xe0A\x01\x12\x14\n\x07creator\x18\x05 \x01(\tB\x03\xe0A\x03\x124\n\x05state\x18\x06 \x01(\x0e2 .google.cloud.notebooks.v2.StateB\x03\xe0A\x03\x12L\n\x0fupgrade_history\x18\x07 \x03(\x0b2..google.cloud.notebooks.v2.UpgradeHistoryEntryB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x08 \x01(\tB\x03\xe0A\x03\x12A\n\x0chealth_state\x18\t \x01(\x0e2&.google.cloud.notebooks.v2.HealthStateB\x03\xe0A\x03\x12M\n\x0bhealth_info\x18\n \x03(\x0b23.google.cloud.notebooks.v2.Instance.HealthInfoEntryB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12!\n\x14disable_proxy_access\x18\r \x01(\x08B\x03\xe0A\x01\x12D\n\x06labels\x18\x0e \x03(\x0b2/.google.cloud.notebooks.v2.Instance.LabelsEntryB\x03\xe0A\x01\x1a1\n\x0fHealthInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:y\xeaAv\n!notebooks.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instanceB\x10\n\x0einfrastructure*\xb2\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0b\n\x07DELETED\x10\x06\x12\r\n\tUPGRADING\x10\x07\x12\x10\n\x0cINITIALIZING\x10\x08\x12\x0e\n\nSUSPENDING\x10\t\x12\r\n\tSUSPENDED\x10\n*w\n\x0bHealthState\x12\x1c\n\x18HEALTH_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\r\n\tUNHEALTHY\x10\x02\x12\x17\n\x13AGENT_NOT_INSTALLED\x10\x03\x12\x15\n\x11AGENT_NOT_RUNNING\x10\x04B\xc4\x01\n\x1dcom.google.cloud.notebooks.v2B\rInstanceProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v2.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v2B\rInstanceProtoP\x01Z;cloud.google.com/go/notebooks/apiv2/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V2\xca\x02\x19Google\\Cloud\\Notebooks\\V2\xea\x02\x1cGoogle::Cloud::Notebooks::V2'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['snapshot']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['snapshot']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['vm_image']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['vm_image']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['container_image']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['container_image']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['framework']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['framework']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['version']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['version']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['state']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['create_time']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x05'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['action']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['action']._serialized_options = b'\xe0A\x01'
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['target_version']._loaded_options = None
    _globals['_UPGRADEHISTORYENTRY'].fields_by_name['target_version']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE_HEALTHINFOENTRY']._loaded_options = None
    _globals['_INSTANCE_HEALTHINFOENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['gce_setup']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['gce_setup']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['proxy_uri']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['proxy_uri']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['instance_owners']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['instance_owners']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['creator']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['upgrade_history']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['upgrade_history']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['health_state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['health_state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['health_info']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['health_info']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['disable_proxy_access']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['disable_proxy_access']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAv\n!notebooks.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance'
    _globals['_STATE']._serialized_start = 1641
    _globals['_STATE']._serialized_end = 1819
    _globals['_HEALTHSTATE']._serialized_start = 1821
    _globals['_HEALTHSTATE']._serialized_end = 1940
    _globals['_UPGRADEHISTORYENTRY']._serialized_start = 208
    _globals['_UPGRADEHISTORYENTRY']._serialized_end = 717
    _globals['_UPGRADEHISTORYENTRY_STATE']._serialized_start = 586
    _globals['_UPGRADEHISTORYENTRY_STATE']._serialized_end = 656
    _globals['_UPGRADEHISTORYENTRY_ACTION']._serialized_start = 658
    _globals['_UPGRADEHISTORYENTRY_ACTION']._serialized_end = 717
    _globals['_INSTANCE']._serialized_start = 720
    _globals['_INSTANCE']._serialized_end = 1638
    _globals['_INSTANCE_HEALTHINFOENTRY']._serialized_start = 1401
    _globals['_INSTANCE_HEALTHINFOENTRY']._serialized_end = 1450
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 1452
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 1497