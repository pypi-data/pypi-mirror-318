"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/notebook_runtime.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1 import network_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_network__spec__pb2
from .....google.cloud.aiplatform.v1 import notebook_euc_config_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_notebook__euc__config__pb2
from .....google.cloud.aiplatform.v1 import notebook_idle_shutdown_config_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_notebook__idle__shutdown__config__pb2
from .....google.cloud.aiplatform.v1 import notebook_runtime_template_ref_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_notebook__runtime__template__ref__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/notebook_runtime.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a2google/cloud/aiplatform/v1/machine_resources.proto\x1a-google/cloud/aiplatform/v1/network_spec.proto\x1a4google/cloud/aiplatform/v1/notebook_euc_config.proto\x1a>google/cloud/aiplatform/v1/notebook_idle_shutdown_config.proto\x1a>google/cloud/aiplatform/v1/notebook_runtime_template_ref.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\t\n\x17NotebookRuntimeTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x17\n\nis_default\x18\x04 \x01(\x08B\x03\xe0A\x03\x12E\n\x0cmachine_spec\x18\x05 \x01(\x0b2\'.google.cloud.aiplatform.v1.MachineSpecB\x06\xe0A\x01\xe0A\x05\x12V\n\x19data_persistent_disk_spec\x18\x08 \x01(\x0b2..google.cloud.aiplatform.v1.PersistentDiskSpecB\x03\xe0A\x01\x12B\n\x0cnetwork_spec\x18\x0c \x01(\x0b2\'.google.cloud.aiplatform.v1.NetworkSpecB\x03\xe0A\x01\x12\x17\n\x0fservice_account\x18\r \x01(\t\x12\x0c\n\x04etag\x18\x0e \x01(\t\x12O\n\x06labels\x18\x0f \x03(\x0b2?.google.cloud.aiplatform.v1.NotebookRuntimeTemplate.LabelsEntry\x12T\n\x14idle_shutdown_config\x18\x11 \x01(\x0b26.google.cloud.aiplatform.v1.NotebookIdleShutdownConfig\x12A\n\neuc_config\x18\x12 \x01(\x0b2-.google.cloud.aiplatform.v1.NotebookEucConfig\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x15notebook_runtime_type\x18\x13 \x01(\x0e2/.google.cloud.aiplatform.v1.NotebookRuntimeTypeB\x06\xe0A\x01\xe0A\x05\x12P\n\x12shielded_vm_config\x18\x14 \x01(\x0b2,.google.cloud.aiplatform.v1.ShieldedVmConfigB\x06\xe0A\x01\xe0A\x05\x12\x19\n\x0cnetwork_tags\x18\x15 \x03(\tB\x03\xe0A\x01\x12C\n\x0fencryption_spec\x18\x17 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x95\x01\xeaA\x91\x01\n1aiplatform.googleapis.com/NotebookRuntimeTemplate\x12\\projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}"\xb2\x0b\n\x0fNotebookRuntime\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cruntime_user\x18\x02 \x01(\tB\x03\xe0A\x02\x12b\n\x1dnotebook_runtime_template_ref\x18\x03 \x01(\x0b26.google.cloud.aiplatform.v1.NotebookRuntimeTemplateRefB\x03\xe0A\x03\x12\x16\n\tproxy_uri\x18\x05 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12R\n\x0chealth_state\x18\x08 \x01(\x0e27.google.cloud.aiplatform.v1.NotebookRuntime.HealthStateB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x0b \x01(\t\x12\x1c\n\x0fservice_account\x18\r \x01(\tB\x03\xe0A\x03\x12T\n\rruntime_state\x18\x0e \x01(\x0e28.google.cloud.aiplatform.v1.NotebookRuntime.RuntimeStateB\x03\xe0A\x03\x12\x1a\n\ris_upgradable\x18\x0f \x01(\x08B\x03\xe0A\x03\x12G\n\x06labels\x18\x10 \x03(\x0b27.google.cloud.aiplatform.v1.NotebookRuntime.LabelsEntry\x128\n\x0fexpiration_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x07version\x18\x12 \x01(\tB\x03\xe0A\x03\x12S\n\x15notebook_runtime_type\x18\x13 \x01(\x0e2/.google.cloud.aiplatform.v1.NotebookRuntimeTypeB\x03\xe0A\x03\x12Y\n\x14idle_shutdown_config\x18\x17 \x01(\x0b26.google.cloud.aiplatform.v1.NotebookIdleShutdownConfigB\x03\xe0A\x03\x12\x19\n\x0cnetwork_tags\x18\x19 \x03(\tB\x03\xe0A\x01\x12H\n\x0fencryption_spec\x18\x1c \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpecB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x1d \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x1e \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"G\n\x0bHealthState\x12\x1c\n\x18HEALTH_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07HEALTHY\x10\x01\x12\r\n\tUNHEALTHY\x10\x02"\x99\x01\n\x0cRuntimeState\x12\x1d\n\x19RUNTIME_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x11\n\rBEING_STARTED\x10\x02\x12\x11\n\rBEING_STOPPED\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x12\n\x0eBEING_UPGRADED\x10\x05\x12\t\n\x05ERROR\x10d\x12\x0b\n\x07INVALID\x10e:{\xeaAx\n)aiplatform.googleapis.com/NotebookRuntime\x12Kprojects/{project}/locations/{location}/notebookRuntimes/{notebook_runtime}*]\n\x13NotebookRuntimeType\x12%\n!NOTEBOOK_RUNTIME_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cUSER_DEFINED\x10\x01\x12\r\n\tONE_CLICK\x10\x02B\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14NotebookRuntimeProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.notebook_runtime_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14NotebookRuntimeProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_NOTEBOOKRUNTIMETEMPLATE_LABELSENTRY']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['display_name']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['is_default']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['is_default']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['data_persistent_disk_spec']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['data_persistent_disk_spec']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['network_spec']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['network_spec']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['create_time']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['update_time']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['notebook_runtime_type']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['notebook_runtime_type']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['shielded_vm_config']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['shielded_vm_config']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['network_tags']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE'].fields_by_name['network_tags']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKRUNTIMETEMPLATE']._loaded_options = None
    _globals['_NOTEBOOKRUNTIMETEMPLATE']._serialized_options = b'\xeaA\x91\x01\n1aiplatform.googleapis.com/NotebookRuntimeTemplate\x12\\projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}'
    _globals['_NOTEBOOKRUNTIME_LABELSENTRY']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['name']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['runtime_user']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['runtime_user']._serialized_options = b'\xe0A\x02'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['notebook_runtime_template_ref']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['notebook_runtime_template_ref']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['proxy_uri']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['proxy_uri']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['create_time']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['update_time']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['health_state']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['health_state']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['display_name']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['service_account']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['service_account']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['runtime_state']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['runtime_state']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['is_upgradable']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['is_upgradable']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['expiration_time']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['expiration_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['version']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['notebook_runtime_type']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['notebook_runtime_type']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['idle_shutdown_config']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['idle_shutdown_config']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['network_tags']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['network_tags']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKRUNTIME']._loaded_options = None
    _globals['_NOTEBOOKRUNTIME']._serialized_options = b'\xeaAx\n)aiplatform.googleapis.com/NotebookRuntime\x12Kprojects/{project}/locations/{location}/notebookRuntimes/{notebook_runtime}'
    _globals['_NOTEBOOKRUNTIMETYPE']._serialized_start = 3154
    _globals['_NOTEBOOKRUNTIMETYPE']._serialized_end = 3247
    _globals['_NOTEBOOKRUNTIMETEMPLATE']._serialized_start = 506
    _globals['_NOTEBOOKRUNTIMETEMPLATE']._serialized_end = 1691
    _globals['_NOTEBOOKRUNTIMETEMPLATE_LABELSENTRY']._serialized_start = 1494
    _globals['_NOTEBOOKRUNTIMETEMPLATE_LABELSENTRY']._serialized_end = 1539
    _globals['_NOTEBOOKRUNTIME']._serialized_start = 1694
    _globals['_NOTEBOOKRUNTIME']._serialized_end = 3152
    _globals['_NOTEBOOKRUNTIME_LABELSENTRY']._serialized_start = 1494
    _globals['_NOTEBOOKRUNTIME_LABELSENTRY']._serialized_end = 1539
    _globals['_NOTEBOOKRUNTIME_HEALTHSTATE']._serialized_start = 2800
    _globals['_NOTEBOOKRUNTIME_HEALTHSTATE']._serialized_end = 2871
    _globals['_NOTEBOOKRUNTIME_RUNTIMESTATE']._serialized_start = 2874
    _globals['_NOTEBOOKRUNTIME_RUNTIMESTATE']._serialized_end = 3027