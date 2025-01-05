"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/lifesciences/v2beta/workflows.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/lifesciences/v2beta/workflows.proto\x12 google.cloud.lifesciences.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\xff\x01\n\x12RunPipelineRequest\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12A\n\x08pipeline\x18\x01 \x01(\x0b2*.google.cloud.lifesciences.v2beta.PipelineB\x03\xe0A\x02\x12P\n\x06labels\x18\x02 \x03(\x0b2@.google.cloud.lifesciences.v2beta.RunPipelineRequest.LabelsEntry\x12\x15\n\rpub_sub_topic\x18\x03 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x15\n\x13RunPipelineResponse"\x80\x03\n\x08Pipeline\x129\n\x07actions\x18\x01 \x03(\x0b2(.google.cloud.lifesciences.v2beta.Action\x12>\n\tresources\x18\x02 \x01(\x0b2+.google.cloud.lifesciences.v2beta.Resources\x12P\n\x0benvironment\x18\x03 \x03(\x0b2;.google.cloud.lifesciences.v2beta.Pipeline.EnvironmentEntry\x12G\n\x15encrypted_environment\x18\x05 \x01(\x0b2(.google.cloud.lifesciences.v2beta.Secret\x12*\n\x07timeout\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x1a2\n\x10EnvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xca\x07\n\x06Action\x12\x16\n\x0econtainer_name\x18\x01 \x01(\t\x12\x16\n\timage_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08commands\x18\x03 \x03(\t\x12\x12\n\nentrypoint\x18\x04 \x01(\t\x12N\n\x0benvironment\x18\x05 \x03(\x0b29.google.cloud.lifesciences.v2beta.Action.EnvironmentEntry\x12G\n\x15encrypted_environment\x18\x15 \x01(\x0b2(.google.cloud.lifesciences.v2beta.Secret\x12\x15\n\rpid_namespace\x18\x06 \x01(\t\x12Q\n\rport_mappings\x18\x08 \x03(\x0b2:.google.cloud.lifesciences.v2beta.Action.PortMappingsEntry\x127\n\x06mounts\x18\t \x03(\x0b2\'.google.cloud.lifesciences.v2beta.Mount\x12D\n\x06labels\x18\n \x03(\x0b24.google.cloud.lifesciences.v2beta.Action.LabelsEntry\x12=\n\x0bcredentials\x18\x0b \x01(\x0b2(.google.cloud.lifesciences.v2beta.Secret\x12*\n\x07timeout\x18\x0c \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\x12ignore_exit_status\x18\r \x01(\x08\x12\x19\n\x11run_in_background\x18\x0e \x01(\x08\x12\x12\n\nalways_run\x18\x0f \x01(\x08\x12\x13\n\x0benable_fuse\x18\x10 \x01(\x08\x12\x1d\n\x15publish_exposed_ports\x18\x11 \x01(\x08\x12\x1e\n\x16disable_image_prefetch\x18\x12 \x01(\x08\x12&\n\x1edisable_standard_error_capture\x18\x13 \x01(\x08\x12\x1e\n\x16block_external_network\x18\x14 \x01(\x08\x1a2\n\x10EnvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a3\n\x11PortMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"/\n\x06Secret\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x13\n\x0bcipher_text\x18\x02 \x01(\t"6\n\x05Mount\x12\x0c\n\x04disk\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x11\n\tread_only\x18\x03 \x01(\x08"v\n\tResources\x12\x0f\n\x07regions\x18\x02 \x03(\t\x12\r\n\x05zones\x18\x03 \x03(\t\x12I\n\x0fvirtual_machine\x18\x04 \x01(\x0b20.google.cloud.lifesciences.v2beta.VirtualMachine"\xbc\x05\n\x0eVirtualMachine\x12\x19\n\x0cmachine_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bpreemptible\x18\x02 \x01(\x08\x12L\n\x06labels\x18\x03 \x03(\x0b2<.google.cloud.lifesciences.v2beta.VirtualMachine.LabelsEntry\x125\n\x05disks\x18\x04 \x03(\x0b2&.google.cloud.lifesciences.v2beta.Disk\x12:\n\x07network\x18\x05 \x01(\x0b2).google.cloud.lifesciences.v2beta.Network\x12C\n\x0caccelerators\x18\x06 \x03(\x0b2-.google.cloud.lifesciences.v2beta.Accelerator\x12I\n\x0fservice_account\x18\x07 \x01(\x0b20.google.cloud.lifesciences.v2beta.ServiceAccount\x12\x19\n\x11boot_disk_size_gb\x18\x08 \x01(\x05\x12\x14\n\x0ccpu_platform\x18\t \x01(\t\x12\x12\n\nboot_image\x18\n \x01(\t\x12!\n\x15nvidia_driver_version\x18\x0b \x01(\tB\x02\x18\x01\x12%\n\x1denable_stackdriver_monitoring\x18\x0c \x01(\x08\x12\x1b\n\x13docker_cache_images\x18\r \x03(\t\x129\n\x07volumes\x18\x0e \x03(\x0b2(.google.cloud.lifesciences.v2beta.Volume\x12\x13\n\x0breservation\x18\x0f \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"/\n\x0eServiceAccount\x12\r\n\x05email\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t"*\n\x0bAccelerator\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03"K\n\x07Network\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x1b\n\x13use_private_address\x18\x02 \x01(\x08\x12\x12\n\nsubnetwork\x18\x03 \x01(\t"I\n\x04Disk\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07size_gb\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x14\n\x0csource_image\x18\x04 \x01(\t"\xfa\x01\n\x06Volume\x12\x0e\n\x06volume\x18\x01 \x01(\t\x12K\n\x0fpersistent_disk\x18\x02 \x01(\x0b20.google.cloud.lifesciences.v2beta.PersistentDiskH\x00\x12G\n\rexisting_disk\x18\x03 \x01(\x0b2..google.cloud.lifesciences.v2beta.ExistingDiskH\x00\x12?\n\tnfs_mount\x18\x04 \x01(\x0b2*.google.cloud.lifesciences.v2beta.NFSMountH\x00B\t\n\x07storage"E\n\x0ePersistentDisk\x12\x0f\n\x07size_gb\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0csource_image\x18\x03 \x01(\t"\x1c\n\x0cExistingDisk\x12\x0c\n\x04disk\x18\x01 \x01(\t"\x1a\n\x08NFSMount\x12\x0e\n\x06target\x18\x01 \x01(\t"\x9e\x03\n\x08Metadata\x12<\n\x08pipeline\x18\x01 \x01(\x0b2*.google.cloud.lifesciences.v2beta.Pipeline\x12F\n\x06labels\x18\x02 \x03(\x0b26.google.cloud.lifesciences.v2beta.Metadata.LabelsEntry\x127\n\x06events\x18\x03 \x03(\x0b2\'.google.cloud.lifesciences.v2beta.Event\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rpub_sub_topic\x18\x07 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xf5\x06\n\x05Event\x12-\n\ttimestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12A\n\x07delayed\x18\x11 \x01(\x0b2..google.cloud.lifesciences.v2beta.DelayedEventH\x00\x12P\n\x0fworker_assigned\x18\x12 \x01(\x0b25.google.cloud.lifesciences.v2beta.WorkerAssignedEventH\x00\x12P\n\x0fworker_released\x18\x13 \x01(\x0b25.google.cloud.lifesciences.v2beta.WorkerReleasedEventH\x00\x12J\n\x0cpull_started\x18\x14 \x01(\x0b22.google.cloud.lifesciences.v2beta.PullStartedEventH\x00\x12J\n\x0cpull_stopped\x18\x15 \x01(\x0b22.google.cloud.lifesciences.v2beta.PullStoppedEventH\x00\x12T\n\x11container_started\x18\x16 \x01(\x0b27.google.cloud.lifesciences.v2beta.ContainerStartedEventH\x00\x12T\n\x11container_stopped\x18\x17 \x01(\x0b27.google.cloud.lifesciences.v2beta.ContainerStoppedEventH\x00\x12R\n\x10container_killed\x18\x18 \x01(\x0b26.google.cloud.lifesciences.v2beta.ContainerKilledEventH\x00\x12]\n\x16unexpected_exit_status\x18\x19 \x01(\x0b2;.google.cloud.lifesciences.v2beta.UnexpectedExitStatusEventH\x00\x12?\n\x06failed\x18\x1a \x01(\x0b2-.google.cloud.lifesciences.v2beta.FailedEventH\x00B\t\n\x07details".\n\x0cDelayedEvent\x12\r\n\x05cause\x18\x01 \x01(\t\x12\x0f\n\x07metrics\x18\x02 \x03(\t"K\n\x13WorkerAssignedEvent\x12\x0c\n\x04zone\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x14\n\x0cmachine_type\x18\x03 \x01(\t"5\n\x13WorkerReleasedEvent\x12\x0c\n\x04zone\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t"%\n\x10PullStartedEvent\x12\x11\n\timage_uri\x18\x01 \x01(\t"%\n\x10PullStoppedEvent\x12\x11\n\timage_uri\x18\x01 \x01(\t"\xd5\x01\n\x15ContainerStartedEvent\x12\x11\n\taction_id\x18\x01 \x01(\x05\x12`\n\rport_mappings\x18\x02 \x03(\x0b2I.google.cloud.lifesciences.v2beta.ContainerStartedEvent.PortMappingsEntry\x12\x12\n\nip_address\x18\x03 \x01(\t\x1a3\n\x11PortMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01"O\n\x15ContainerStoppedEvent\x12\x11\n\taction_id\x18\x01 \x01(\x05\x12\x13\n\x0bexit_status\x18\x02 \x01(\x05\x12\x0e\n\x06stderr\x18\x03 \x01(\t"C\n\x19UnexpectedExitStatusEvent\x12\x11\n\taction_id\x18\x01 \x01(\x05\x12\x13\n\x0bexit_status\x18\x02 \x01(\x05")\n\x14ContainerKilledEvent\x12\x11\n\taction_id\x18\x01 \x01(\x05"<\n\x0bFailedEvent\x12\x1e\n\x04code\x18\x01 \x01(\x0e2\x10.google.rpc.Code\x12\r\n\x05cause\x18\x02 \x01(\t2\xb2\x02\n\x16WorkflowsServiceV2Beta\x12\xc6\x01\n\x0bRunPipeline\x124.google.cloud.lifesciences.v2beta.RunPipelineRequest\x1a\x1d.google.longrunning.Operation"b\xcaA\x1f\n\x13RunPipelineResponse\x12\x08Metadata\x82\xd3\xe4\x93\x02:"5/v2beta/{parent=projects/*/locations/*}/pipelines:run:\x01*\x1aO\xcaA\x1blifesciences.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n$com.google.cloud.lifesciences.v2betaB\x0eWorkflowsProtoP\x01ZHcloud.google.com/go/lifesciences/apiv2beta/lifesciencespb;lifesciencespb\xa2\x02\x04CLSW\xaa\x02 Google.Cloud.LifeSciences.V2Beta\xca\x02 Google\\Cloud\\LifeSciences\\V2beta\xea\x02#Google::Cloud::LifeSciences::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.lifesciences.v2beta.workflows_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.lifesciences.v2betaB\x0eWorkflowsProtoP\x01ZHcloud.google.com/go/lifesciences/apiv2beta/lifesciencespb;lifesciencespb\xa2\x02\x04CLSW\xaa\x02 Google.Cloud.LifeSciences.V2Beta\xca\x02 Google\\Cloud\\LifeSciences\\V2beta\xea\x02#Google::Cloud::LifeSciences::V2beta'
    _globals['_RUNPIPELINEREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_RUNPIPELINEREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNPIPELINEREQUEST'].fields_by_name['pipeline']._loaded_options = None
    _globals['_RUNPIPELINEREQUEST'].fields_by_name['pipeline']._serialized_options = b'\xe0A\x02'
    _globals['_PIPELINE_ENVIRONMENTENTRY']._loaded_options = None
    _globals['_PIPELINE_ENVIRONMENTENTRY']._serialized_options = b'8\x01'
    _globals['_ACTION_ENVIRONMENTENTRY']._loaded_options = None
    _globals['_ACTION_ENVIRONMENTENTRY']._serialized_options = b'8\x01'
    _globals['_ACTION_PORTMAPPINGSENTRY']._loaded_options = None
    _globals['_ACTION_PORTMAPPINGSENTRY']._serialized_options = b'8\x01'
    _globals['_ACTION_LABELSENTRY']._loaded_options = None
    _globals['_ACTION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ACTION'].fields_by_name['image_uri']._loaded_options = None
    _globals['_ACTION'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x02'
    _globals['_VIRTUALMACHINE_LABELSENTRY']._loaded_options = None
    _globals['_VIRTUALMACHINE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_VIRTUALMACHINE'].fields_by_name['machine_type']._loaded_options = None
    _globals['_VIRTUALMACHINE'].fields_by_name['machine_type']._serialized_options = b'\xe0A\x02'
    _globals['_VIRTUALMACHINE'].fields_by_name['nvidia_driver_version']._loaded_options = None
    _globals['_VIRTUALMACHINE'].fields_by_name['nvidia_driver_version']._serialized_options = b'\x18\x01'
    _globals['_METADATA_LABELSENTRY']._loaded_options = None
    _globals['_METADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTAINERSTARTEDEVENT_PORTMAPPINGSENTRY']._loaded_options = None
    _globals['_CONTAINERSTARTEDEVENT_PORTMAPPINGSENTRY']._serialized_options = b'8\x01'
    _globals['_WORKFLOWSSERVICEV2BETA']._loaded_options = None
    _globals['_WORKFLOWSSERVICEV2BETA']._serialized_options = b'\xcaA\x1blifesciences.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WORKFLOWSSERVICEV2BETA'].methods_by_name['RunPipeline']._loaded_options = None
    _globals['_WORKFLOWSSERVICEV2BETA'].methods_by_name['RunPipeline']._serialized_options = b'\xcaA\x1f\n\x13RunPipelineResponse\x12\x08Metadata\x82\xd3\xe4\x93\x02:"5/v2beta/{parent=projects/*/locations/*}/pipelines:run:\x01*'
    _globals['_RUNPIPELINEREQUEST']._serialized_start = 300
    _globals['_RUNPIPELINEREQUEST']._serialized_end = 555
    _globals['_RUNPIPELINEREQUEST_LABELSENTRY']._serialized_start = 510
    _globals['_RUNPIPELINEREQUEST_LABELSENTRY']._serialized_end = 555
    _globals['_RUNPIPELINERESPONSE']._serialized_start = 557
    _globals['_RUNPIPELINERESPONSE']._serialized_end = 578
    _globals['_PIPELINE']._serialized_start = 581
    _globals['_PIPELINE']._serialized_end = 965
    _globals['_PIPELINE_ENVIRONMENTENTRY']._serialized_start = 915
    _globals['_PIPELINE_ENVIRONMENTENTRY']._serialized_end = 965
    _globals['_ACTION']._serialized_start = 968
    _globals['_ACTION']._serialized_end = 1938
    _globals['_ACTION_ENVIRONMENTENTRY']._serialized_start = 915
    _globals['_ACTION_ENVIRONMENTENTRY']._serialized_end = 965
    _globals['_ACTION_PORTMAPPINGSENTRY']._serialized_start = 1840
    _globals['_ACTION_PORTMAPPINGSENTRY']._serialized_end = 1891
    _globals['_ACTION_LABELSENTRY']._serialized_start = 510
    _globals['_ACTION_LABELSENTRY']._serialized_end = 555
    _globals['_SECRET']._serialized_start = 1940
    _globals['_SECRET']._serialized_end = 1987
    _globals['_MOUNT']._serialized_start = 1989
    _globals['_MOUNT']._serialized_end = 2043
    _globals['_RESOURCES']._serialized_start = 2045
    _globals['_RESOURCES']._serialized_end = 2163
    _globals['_VIRTUALMACHINE']._serialized_start = 2166
    _globals['_VIRTUALMACHINE']._serialized_end = 2866
    _globals['_VIRTUALMACHINE_LABELSENTRY']._serialized_start = 510
    _globals['_VIRTUALMACHINE_LABELSENTRY']._serialized_end = 555
    _globals['_SERVICEACCOUNT']._serialized_start = 2868
    _globals['_SERVICEACCOUNT']._serialized_end = 2915
    _globals['_ACCELERATOR']._serialized_start = 2917
    _globals['_ACCELERATOR']._serialized_end = 2959
    _globals['_NETWORK']._serialized_start = 2961
    _globals['_NETWORK']._serialized_end = 3036
    _globals['_DISK']._serialized_start = 3038
    _globals['_DISK']._serialized_end = 3111
    _globals['_VOLUME']._serialized_start = 3114
    _globals['_VOLUME']._serialized_end = 3364
    _globals['_PERSISTENTDISK']._serialized_start = 3366
    _globals['_PERSISTENTDISK']._serialized_end = 3435
    _globals['_EXISTINGDISK']._serialized_start = 3437
    _globals['_EXISTINGDISK']._serialized_end = 3465
    _globals['_NFSMOUNT']._serialized_start = 3467
    _globals['_NFSMOUNT']._serialized_end = 3493
    _globals['_METADATA']._serialized_start = 3496
    _globals['_METADATA']._serialized_end = 3910
    _globals['_METADATA_LABELSENTRY']._serialized_start = 510
    _globals['_METADATA_LABELSENTRY']._serialized_end = 555
    _globals['_EVENT']._serialized_start = 3913
    _globals['_EVENT']._serialized_end = 4798
    _globals['_DELAYEDEVENT']._serialized_start = 4800
    _globals['_DELAYEDEVENT']._serialized_end = 4846
    _globals['_WORKERASSIGNEDEVENT']._serialized_start = 4848
    _globals['_WORKERASSIGNEDEVENT']._serialized_end = 4923
    _globals['_WORKERRELEASEDEVENT']._serialized_start = 4925
    _globals['_WORKERRELEASEDEVENT']._serialized_end = 4978
    _globals['_PULLSTARTEDEVENT']._serialized_start = 4980
    _globals['_PULLSTARTEDEVENT']._serialized_end = 5017
    _globals['_PULLSTOPPEDEVENT']._serialized_start = 5019
    _globals['_PULLSTOPPEDEVENT']._serialized_end = 5056
    _globals['_CONTAINERSTARTEDEVENT']._serialized_start = 5059
    _globals['_CONTAINERSTARTEDEVENT']._serialized_end = 5272
    _globals['_CONTAINERSTARTEDEVENT_PORTMAPPINGSENTRY']._serialized_start = 1840
    _globals['_CONTAINERSTARTEDEVENT_PORTMAPPINGSENTRY']._serialized_end = 1891
    _globals['_CONTAINERSTOPPEDEVENT']._serialized_start = 5274
    _globals['_CONTAINERSTOPPEDEVENT']._serialized_end = 5353
    _globals['_UNEXPECTEDEXITSTATUSEVENT']._serialized_start = 5355
    _globals['_UNEXPECTEDEXITSTATUSEVENT']._serialized_end = 5422
    _globals['_CONTAINERKILLEDEVENT']._serialized_start = 5424
    _globals['_CONTAINERKILLEDEVENT']._serialized_end = 5465
    _globals['_FAILEDEVENT']._serialized_start = 5467
    _globals['_FAILEDEVENT']._serialized_end = 5527
    _globals['_WORKFLOWSSERVICEV2BETA']._serialized_start = 5530
    _globals['_WORKFLOWSSERVICEV2BETA']._serialized_end = 5836