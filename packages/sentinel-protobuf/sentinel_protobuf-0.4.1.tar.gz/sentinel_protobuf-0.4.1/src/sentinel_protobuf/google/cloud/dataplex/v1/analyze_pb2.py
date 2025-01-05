"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataplex/v1/analyze.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import resources_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/dataplex/v1/analyze.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/dataplex/v1/resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\r\n\x0bEnvironment\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x03\xfaA%\n#dataplex.googleapis.com/Environment\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03uid\x18\x03 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x06 \x03(\x0b21.google.cloud.dataplex.v1.Environment.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x07 \x01(\tB\x03\xe0A\x01\x123\n\x05state\x18\x08 \x01(\x0e2\x1f.google.cloud.dataplex.v1.StateB\x03\xe0A\x03\x12Z\n\x13infrastructure_spec\x18d \x01(\x0b28.google.cloud.dataplex.v1.Environment.InfrastructureSpecB\x03\xe0A\x02\x12L\n\x0csession_spec\x18e \x01(\x0b21.google.cloud.dataplex.v1.Environment.SessionSpecB\x03\xe0A\x01\x12P\n\x0esession_status\x18f \x01(\x0b23.google.cloud.dataplex.v1.Environment.SessionStatusB\x03\xe0A\x03\x12H\n\tendpoints\x18\xc8\x01 \x01(\x0b2/.google.cloud.dataplex.v1.Environment.EndpointsB\x03\xe0A\x03\x1a\xe5\x04\n\x12InfrastructureSpec\x12a\n\x07compute\x182 \x01(\x0b2I.google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResourcesB\x03\xe0A\x01H\x00\x12`\n\x08os_image\x18d \x01(\x0b2G.google.cloud.dataplex.v1.Environment.InfrastructureSpec.OsImageRuntimeB\x03\xe0A\x02H\x01\x1ac\n\x10ComputeResources\x12\x19\n\x0cdisk_size_gb\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\nnode_count\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1b\n\x0emax_node_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x1a\x8c\x02\n\x0eOsImageRuntime\x12\x1a\n\rimage_version\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ejava_libraries\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1c\n\x0fpython_packages\x18\x03 \x03(\tB\x03\xe0A\x01\x12p\n\nproperties\x18\x04 \x03(\x0b2W.google.cloud.dataplex.v1.Environment.InfrastructureSpec.OsImageRuntime.PropertiesEntryB\x03\xe0A\x01\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0b\n\tresourcesB\t\n\x07runtime\x1aj\n\x0bSessionSpec\x129\n\x11max_idle_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12 \n\x13enable_fast_startup\x18\x02 \x01(\x08B\x03\xe0A\x01\x1a$\n\rSessionStatus\x12\x13\n\x06active\x18\x01 \x01(\x08B\x03\xe0A\x03\x1a5\n\tEndpoints\x12\x16\n\tnotebooks\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03sql\x18\x02 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:y\xeaAv\n#dataplex.googleapis.com/Environment\x12Oprojects/{project}/locations/{location}/lakes/{lake}/environments/{environment}"\xa6\x07\n\x07Content\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fdataplex.googleapis.com/Content\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04path\x18\x03 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x06labels\x18\x06 \x03(\x0b2-.google.cloud.dataplex.v1.Content.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x18\n\tdata_text\x18\t \x01(\tB\x03\xe0A\x02H\x00\x12A\n\nsql_script\x18d \x01(\x0b2+.google.cloud.dataplex.v1.Content.SqlScriptH\x01\x12>\n\x08notebook\x18e \x01(\x0b2*.google.cloud.dataplex.v1.Content.NotebookH\x01\x1a\x91\x01\n\tSqlScript\x12L\n\x06engine\x18\x01 \x01(\x0e27.google.cloud.dataplex.v1.Content.SqlScript.QueryEngineB\x03\xe0A\x02"6\n\x0bQueryEngine\x12\x1c\n\x18QUERY_ENGINE_UNSPECIFIED\x10\x00\x12\t\n\x05SPARK\x10\x02\x1a\x93\x01\n\x08Notebook\x12O\n\x0bkernel_type\x18\x01 \x01(\x0e25.google.cloud.dataplex.v1.Content.Notebook.KernelTypeB\x03\xe0A\x02"6\n\nKernelType\x12\x1b\n\x17KERNEL_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PYTHON3\x10\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:l\xeaAi\n\x1fdataplex.googleapis.com/Content\x12Fprojects/{project}/locations/{location}/lakes/{lake}/content/{content}B\x06\n\x04dataB\t\n\x07content"\xcd\x02\n\x07Session\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fdataplex.googleapis.com/Session\x12\x14\n\x07user_id\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\x05state\x18\x04 \x01(\x0e2\x1f.google.cloud.dataplex.v1.StateB\x03\xe0A\x03:\x89\x01\xeaA\x85\x01\n\x1fdataplex.googleapis.com/Session\x12bprojects/{project}/locations/{location}/lakes/{lake}/environments/{environment}/sessions/{session}Bh\n\x1ccom.google.cloud.dataplex.v1B\x0cAnalyzeProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.analyze_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x0cAnalyzeProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['disk_size_gb']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['disk_size_gb']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['node_count']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['node_count']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['max_node_count']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES'].fields_by_name['max_node_count']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME_PROPERTIESENTRY']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['image_version']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['image_version']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['java_libraries']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['java_libraries']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['python_packages']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['python_packages']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['properties']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC'].fields_by_name['compute']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC'].fields_by_name['compute']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC'].fields_by_name['os_image']._loaded_options = None
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC'].fields_by_name['os_image']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT_SESSIONSPEC'].fields_by_name['max_idle_duration']._loaded_options = None
    _globals['_ENVIRONMENT_SESSIONSPEC'].fields_by_name['max_idle_duration']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_SESSIONSPEC'].fields_by_name['enable_fast_startup']._loaded_options = None
    _globals['_ENVIRONMENT_SESSIONSPEC'].fields_by_name['enable_fast_startup']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT_SESSIONSTATUS'].fields_by_name['active']._loaded_options = None
    _globals['_ENVIRONMENT_SESSIONSTATUS'].fields_by_name['active']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT_ENDPOINTS'].fields_by_name['notebooks']._loaded_options = None
    _globals['_ENVIRONMENT_ENDPOINTS'].fields_by_name['notebooks']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT_ENDPOINTS'].fields_by_name['sql']._loaded_options = None
    _globals['_ENVIRONMENT_ENDPOINTS'].fields_by_name['sql']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT_LABELSENTRY']._loaded_options = None
    _globals['_ENVIRONMENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENVIRONMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA%\n#dataplex.googleapis.com/Environment'
    _globals['_ENVIRONMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['uid']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['labels']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['description']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['state']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['infrastructure_spec']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['infrastructure_spec']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT'].fields_by_name['session_spec']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['session_spec']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['session_status']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['session_status']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['endpoints']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT']._loaded_options = None
    _globals['_ENVIRONMENT']._serialized_options = b'\xeaAv\n#dataplex.googleapis.com/Environment\x12Oprojects/{project}/locations/{location}/lakes/{lake}/environments/{environment}'
    _globals['_CONTENT_SQLSCRIPT'].fields_by_name['engine']._loaded_options = None
    _globals['_CONTENT_SQLSCRIPT'].fields_by_name['engine']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENT_NOTEBOOK'].fields_by_name['kernel_type']._loaded_options = None
    _globals['_CONTENT_NOTEBOOK'].fields_by_name['kernel_type']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENT_LABELSENTRY']._loaded_options = None
    _globals['_CONTENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTENT'].fields_by_name['name']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fdataplex.googleapis.com/Content'
    _globals['_CONTENT'].fields_by_name['uid']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_CONTENT'].fields_by_name['path']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['path']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONTENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONTENT'].fields_by_name['labels']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CONTENT'].fields_by_name['description']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CONTENT'].fields_by_name['data_text']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['data_text']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENT']._loaded_options = None
    _globals['_CONTENT']._serialized_options = b'\xeaAi\n\x1fdataplex.googleapis.com/Content\x12Fprojects/{project}/locations/{location}/lakes/{lake}/content/{content}'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fdataplex.googleapis.com/Session'
    _globals['_SESSION'].fields_by_name['user_id']._loaded_options = None
    _globals['_SESSION'].fields_by_name['user_id']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['state']._loaded_options = None
    _globals['_SESSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\x85\x01\n\x1fdataplex.googleapis.com/Session\x12bprojects/{project}/locations/{location}/lakes/{lake}/environments/{environment}/sessions/{session}'
    _globals['_ENVIRONMENT']._serialized_start = 236
    _globals['_ENVIRONMENT']._serialized_end = 1925
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC']._serialized_start = 941
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC']._serialized_end = 1554
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES']._serialized_start = 1160
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_COMPUTERESOURCES']._serialized_end = 1259
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME']._serialized_start = 1262
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME']._serialized_end = 1530
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME_PROPERTIESENTRY']._serialized_start = 1481
    _globals['_ENVIRONMENT_INFRASTRUCTURESPEC_OSIMAGERUNTIME_PROPERTIESENTRY']._serialized_end = 1530
    _globals['_ENVIRONMENT_SESSIONSPEC']._serialized_start = 1556
    _globals['_ENVIRONMENT_SESSIONSPEC']._serialized_end = 1662
    _globals['_ENVIRONMENT_SESSIONSTATUS']._serialized_start = 1664
    _globals['_ENVIRONMENT_SESSIONSTATUS']._serialized_end = 1700
    _globals['_ENVIRONMENT_ENDPOINTS']._serialized_start = 1702
    _globals['_ENVIRONMENT_ENDPOINTS']._serialized_end = 1755
    _globals['_ENVIRONMENT_LABELSENTRY']._serialized_start = 1757
    _globals['_ENVIRONMENT_LABELSENTRY']._serialized_end = 1802
    _globals['_CONTENT']._serialized_start = 1928
    _globals['_CONTENT']._serialized_end = 2862
    _globals['_CONTENT_SQLSCRIPT']._serialized_start = 2391
    _globals['_CONTENT_SQLSCRIPT']._serialized_end = 2536
    _globals['_CONTENT_SQLSCRIPT_QUERYENGINE']._serialized_start = 2482
    _globals['_CONTENT_SQLSCRIPT_QUERYENGINE']._serialized_end = 2536
    _globals['_CONTENT_NOTEBOOK']._serialized_start = 2539
    _globals['_CONTENT_NOTEBOOK']._serialized_end = 2686
    _globals['_CONTENT_NOTEBOOK_KERNELTYPE']._serialized_start = 2632
    _globals['_CONTENT_NOTEBOOK_KERNELTYPE']._serialized_end = 2686
    _globals['_CONTENT_LABELSENTRY']._serialized_start = 1757
    _globals['_CONTENT_LABELSENTRY']._serialized_end = 1802
    _globals['_SESSION']._serialized_start = 2865
    _globals['_SESSION']._serialized_end = 3198