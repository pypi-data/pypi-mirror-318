"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/genomics/v1alpha2/pipelines.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/genomics/v1alpha2/pipelines.proto\x12\x18google.genomics.v1alpha2\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"^\n\rComputeEngine\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x0c\n\x04zone\x18\x02 \x01(\t\x12\x14\n\x0cmachine_type\x18\x03 \x01(\t\x12\x12\n\ndisk_names\x18\x04 \x03(\t"R\n\x0fRuntimeMetadata\x12?\n\x0ecompute_engine\x18\x01 \x01(\x0b2\'.google.genomics.v1alpha2.ComputeEngine"\xed\x02\n\x08Pipeline\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12E\n\x10input_parameters\x18\x08 \x03(\x0b2+.google.genomics.v1alpha2.PipelineParameter\x12F\n\x11output_parameters\x18\t \x03(\x0b2+.google.genomics.v1alpha2.PipelineParameter\x12:\n\x06docker\x18\x05 \x01(\x0b2(.google.genomics.v1alpha2.DockerExecutorH\x00\x12>\n\tresources\x18\x06 \x01(\x0b2+.google.genomics.v1alpha2.PipelineResources\x12\x13\n\x0bpipeline_id\x18\x07 \x01(\tB\n\n\x08executor"M\n\x15CreatePipelineRequest\x124\n\x08pipeline\x18\x01 \x01(\x0b2".google.genomics.v1alpha2.Pipeline"\xa1\x05\n\x0fRunPipelineArgs\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12E\n\x06inputs\x18\x02 \x03(\x0b25.google.genomics.v1alpha2.RunPipelineArgs.InputsEntry\x12G\n\x07outputs\x18\x03 \x03(\x0b26.google.genomics.v1alpha2.RunPipelineArgs.OutputsEntry\x12A\n\x0fservice_account\x18\x04 \x01(\x0b2(.google.genomics.v1alpha2.ServiceAccount\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12>\n\tresources\x18\x06 \x01(\x0b2+.google.genomics.v1alpha2.PipelineResources\x129\n\x07logging\x18\x07 \x01(\x0b2(.google.genomics.v1alpha2.LoggingOptions\x12D\n!keep_vm_alive_on_failure_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12E\n\x06labels\x18\t \x03(\x0b25.google.genomics.v1alpha2.RunPipelineArgs.LabelsEntry\x1a-\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a.\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xbb\x01\n\x12RunPipelineRequest\x12\x15\n\x0bpipeline_id\x18\x01 \x01(\tH\x00\x12@\n\x12ephemeral_pipeline\x18\x02 \x01(\x0b2".google.genomics.v1alpha2.PipelineH\x00\x12@\n\rpipeline_args\x18\x03 \x01(\x0b2).google.genomics.v1alpha2.RunPipelineArgsB\n\n\x08pipeline")\n\x12GetPipelineRequest\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\t"f\n\x14ListPipelinesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bname_prefix\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"g\n\x15ListPipelinesResponse\x125\n\tpipelines\x18\x01 \x03(\x0b2".google.genomics.v1alpha2.Pipeline\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t",\n\x15DeletePipelineRequest\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\t"L\n\x1aGetControllerConfigRequest\x12\x14\n\x0coperation_id\x18\x01 \x01(\t\x12\x18\n\x10validation_token\x18\x02 \x01(\x04"\xd9\x05\n\x10ControllerConfig\x12\r\n\x05image\x18\x01 \x01(\t\x12\x0b\n\x03cmd\x18\x02 \x01(\t\x12\x14\n\x0cgcs_log_path\x18\x03 \x01(\t\x12\x14\n\x0cmachine_type\x18\x04 \x01(\t\x12B\n\x04vars\x18\x05 \x03(\x0b24.google.genomics.v1alpha2.ControllerConfig.VarsEntry\x12D\n\x05disks\x18\x06 \x03(\x0b25.google.genomics.v1alpha2.ControllerConfig.DisksEntry\x12O\n\x0bgcs_sources\x18\x07 \x03(\x0b2:.google.genomics.v1alpha2.ControllerConfig.GcsSourcesEntry\x12K\n\tgcs_sinks\x18\x08 \x03(\x0b28.google.genomics.v1alpha2.ControllerConfig.GcsSinksEntry\x1a \n\x0eRepeatedString\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a,\n\nDisksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1al\n\x0fGcsSourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12H\n\x05value\x18\x02 \x01(\x0b29.google.genomics.v1alpha2.ControllerConfig.RepeatedString:\x028\x01\x1aj\n\rGcsSinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12H\n\x05value\x18\x02 \x01(\x0b29.google.genomics.v1alpha2.ControllerConfig.RepeatedString:\x028\x01"T\n\x0eTimestampEvent\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xcc\x01\n\x19SetOperationStatusRequest\x12\x14\n\x0coperation_id\x18\x01 \x01(\t\x12B\n\x10timestamp_events\x18\x02 \x03(\x0b2(.google.genomics.v1alpha2.TimestampEvent\x12$\n\nerror_code\x18\x03 \x01(\x0e2\x10.google.rpc.Code\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12\x18\n\x10validation_token\x18\x05 \x01(\x04"/\n\x0eServiceAccount\x12\r\n\x05email\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t""\n\x0eLoggingOptions\x12\x10\n\x08gcs_path\x18\x01 \x01(\t"\xd6\x03\n\x11PipelineResources\x12\x19\n\x11minimum_cpu_cores\x18\x01 \x01(\x05\x12\x13\n\x0bpreemptible\x18\x02 \x01(\x08\x12\x16\n\x0eminimum_ram_gb\x18\x03 \x01(\x01\x12?\n\x05disks\x18\x04 \x03(\x0b20.google.genomics.v1alpha2.PipelineResources.Disk\x12\r\n\x05zones\x18\x05 \x03(\t\x12\x19\n\x11boot_disk_size_gb\x18\x06 \x01(\x05\x12\x12\n\nno_address\x18\x07 \x01(\x08\x1a\xf9\x01\n\x04Disk\x12\x0c\n\x04name\x18\x01 \x01(\t\x12C\n\x04type\x18\x02 \x01(\x0e25.google.genomics.v1alpha2.PipelineResources.Disk.Type\x12\x0f\n\x07size_gb\x18\x03 \x01(\x05\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x13\n\x0bauto_delete\x18\x06 \x01(\x08\x12\x13\n\x0bmount_point\x18\x08 \x01(\t"S\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0ePERSISTENT_HDD\x10\x01\x12\x12\n\x0ePERSISTENT_SSD\x10\x02\x12\r\n\tLOCAL_SSD\x10\x03"\xc1\x01\n\x11PipelineParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rdefault_value\x18\x05 \x01(\t\x12I\n\nlocal_copy\x18\x06 \x01(\x0b25.google.genomics.v1alpha2.PipelineParameter.LocalCopy\x1a\'\n\tLocalCopy\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04disk\x18\x02 \x01(\t"1\n\x0eDockerExecutor\x12\x12\n\nimage_name\x18\x01 \x01(\t\x12\x0b\n\x03cmd\x18\x02 \x01(\t2\x88\x08\n\x11PipelinesV1Alpha2\x12\x8c\x01\n\x0eCreatePipeline\x12/.google.genomics.v1alpha2.CreatePipelineRequest\x1a".google.genomics.v1alpha2.Pipeline"%\x82\xd3\xe4\x93\x02\x1f"\x13/v1alpha2/pipelines:\x08pipeline\x12~\n\x0bRunPipeline\x12,.google.genomics.v1alpha2.RunPipelineRequest\x1a\x1d.google.longrunning.Operation""\x82\xd3\xe4\x93\x02\x1c"\x17/v1alpha2/pipelines:run:\x01*\x12\x8a\x01\n\x0bGetPipeline\x12,.google.genomics.v1alpha2.GetPipelineRequest\x1a".google.genomics.v1alpha2.Pipeline")\x82\xd3\xe4\x93\x02#\x12!/v1alpha2/pipelines/{pipeline_id}\x12\x8d\x01\n\rListPipelines\x12..google.genomics.v1alpha2.ListPipelinesRequest\x1a/.google.genomics.v1alpha2.ListPipelinesResponse"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1alpha2/pipelines\x12\x84\x01\n\x0eDeletePipeline\x12/.google.genomics.v1alpha2.DeletePipelineRequest\x1a\x16.google.protobuf.Empty")\x82\xd3\xe4\x93\x02#*!/v1alpha2/pipelines/{pipeline_id}\x12\xa8\x01\n\x13GetControllerConfig\x124.google.genomics.v1alpha2.GetControllerConfigRequest\x1a*.google.genomics.v1alpha2.ControllerConfig"/\x82\xd3\xe4\x93\x02)\x12\'/v1alpha2/pipelines:getControllerConfig\x12\x94\x01\n\x12SetOperationStatus\x123.google.genomics.v1alpha2.SetOperationStatusRequest\x1a\x16.google.protobuf.Empty"1\x82\xd3\xe4\x93\x02+\x1a&/v1alpha2/pipelines:setOperationStatus:\x01*Bp\n\x17com.google.genomics.v1aB\x0ePipelinesProtoP\x01Z@google.golang.org/genproto/googleapis/genomics/v1alpha2;genomics\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.genomics.v1alpha2.pipelines_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.genomics.v1aB\x0ePipelinesProtoP\x01Z@google.golang.org/genproto/googleapis/genomics/v1alpha2;genomics\xf8\x01\x01'
    _globals['_RUNPIPELINEARGS_INPUTSENTRY']._loaded_options = None
    _globals['_RUNPIPELINEARGS_INPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNPIPELINEARGS_OUTPUTSENTRY']._loaded_options = None
    _globals['_RUNPIPELINEARGS_OUTPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNPIPELINEARGS_LABELSENTRY']._loaded_options = None
    _globals['_RUNPIPELINEARGS_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTROLLERCONFIG_VARSENTRY']._loaded_options = None
    _globals['_CONTROLLERCONFIG_VARSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTROLLERCONFIG_DISKSENTRY']._loaded_options = None
    _globals['_CONTROLLERCONFIG_DISKSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTROLLERCONFIG_GCSSOURCESENTRY']._loaded_options = None
    _globals['_CONTROLLERCONFIG_GCSSOURCESENTRY']._serialized_options = b'8\x01'
    _globals['_CONTROLLERCONFIG_GCSSINKSENTRY']._loaded_options = None
    _globals['_CONTROLLERCONFIG_GCSSINKSENTRY']._serialized_options = b'8\x01'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['CreatePipeline']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['CreatePipeline']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x13/v1alpha2/pipelines:\x08pipeline'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['RunPipeline']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['RunPipeline']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/v1alpha2/pipelines:run:\x01*'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['GetPipeline']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['GetPipeline']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/v1alpha2/pipelines/{pipeline_id}'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['ListPipelines']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['ListPipelines']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15\x12\x13/v1alpha2/pipelines'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['DeletePipeline']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['DeletePipeline']._serialized_options = b'\x82\xd3\xe4\x93\x02#*!/v1alpha2/pipelines/{pipeline_id}'
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['GetControllerConfig']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['GetControllerConfig']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/v1alpha2/pipelines:getControllerConfig"
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['SetOperationStatus']._loaded_options = None
    _globals['_PIPELINESV1ALPHA2'].methods_by_name['SetOperationStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x1a&/v1alpha2/pipelines:setOperationStatus:\x01*'
    _globals['_COMPUTEENGINE']._serialized_start = 254
    _globals['_COMPUTEENGINE']._serialized_end = 348
    _globals['_RUNTIMEMETADATA']._serialized_start = 350
    _globals['_RUNTIMEMETADATA']._serialized_end = 432
    _globals['_PIPELINE']._serialized_start = 435
    _globals['_PIPELINE']._serialized_end = 800
    _globals['_CREATEPIPELINEREQUEST']._serialized_start = 802
    _globals['_CREATEPIPELINEREQUEST']._serialized_end = 879
    _globals['_RUNPIPELINEARGS']._serialized_start = 882
    _globals['_RUNPIPELINEARGS']._serialized_end = 1555
    _globals['_RUNPIPELINEARGS_INPUTSENTRY']._serialized_start = 1415
    _globals['_RUNPIPELINEARGS_INPUTSENTRY']._serialized_end = 1460
    _globals['_RUNPIPELINEARGS_OUTPUTSENTRY']._serialized_start = 1462
    _globals['_RUNPIPELINEARGS_OUTPUTSENTRY']._serialized_end = 1508
    _globals['_RUNPIPELINEARGS_LABELSENTRY']._serialized_start = 1510
    _globals['_RUNPIPELINEARGS_LABELSENTRY']._serialized_end = 1555
    _globals['_RUNPIPELINEREQUEST']._serialized_start = 1558
    _globals['_RUNPIPELINEREQUEST']._serialized_end = 1745
    _globals['_GETPIPELINEREQUEST']._serialized_start = 1747
    _globals['_GETPIPELINEREQUEST']._serialized_end = 1788
    _globals['_LISTPIPELINESREQUEST']._serialized_start = 1790
    _globals['_LISTPIPELINESREQUEST']._serialized_end = 1892
    _globals['_LISTPIPELINESRESPONSE']._serialized_start = 1894
    _globals['_LISTPIPELINESRESPONSE']._serialized_end = 1997
    _globals['_DELETEPIPELINEREQUEST']._serialized_start = 1999
    _globals['_DELETEPIPELINEREQUEST']._serialized_end = 2043
    _globals['_GETCONTROLLERCONFIGREQUEST']._serialized_start = 2045
    _globals['_GETCONTROLLERCONFIGREQUEST']._serialized_end = 2121
    _globals['_CONTROLLERCONFIG']._serialized_start = 2124
    _globals['_CONTROLLERCONFIG']._serialized_end = 2853
    _globals['_CONTROLLERCONFIG_REPEATEDSTRING']._serialized_start = 2512
    _globals['_CONTROLLERCONFIG_REPEATEDSTRING']._serialized_end = 2544
    _globals['_CONTROLLERCONFIG_VARSENTRY']._serialized_start = 2546
    _globals['_CONTROLLERCONFIG_VARSENTRY']._serialized_end = 2589
    _globals['_CONTROLLERCONFIG_DISKSENTRY']._serialized_start = 2591
    _globals['_CONTROLLERCONFIG_DISKSENTRY']._serialized_end = 2635
    _globals['_CONTROLLERCONFIG_GCSSOURCESENTRY']._serialized_start = 2637
    _globals['_CONTROLLERCONFIG_GCSSOURCESENTRY']._serialized_end = 2745
    _globals['_CONTROLLERCONFIG_GCSSINKSENTRY']._serialized_start = 2747
    _globals['_CONTROLLERCONFIG_GCSSINKSENTRY']._serialized_end = 2853
    _globals['_TIMESTAMPEVENT']._serialized_start = 2855
    _globals['_TIMESTAMPEVENT']._serialized_end = 2939
    _globals['_SETOPERATIONSTATUSREQUEST']._serialized_start = 2942
    _globals['_SETOPERATIONSTATUSREQUEST']._serialized_end = 3146
    _globals['_SERVICEACCOUNT']._serialized_start = 3148
    _globals['_SERVICEACCOUNT']._serialized_end = 3195
    _globals['_LOGGINGOPTIONS']._serialized_start = 3197
    _globals['_LOGGINGOPTIONS']._serialized_end = 3231
    _globals['_PIPELINERESOURCES']._serialized_start = 3234
    _globals['_PIPELINERESOURCES']._serialized_end = 3704
    _globals['_PIPELINERESOURCES_DISK']._serialized_start = 3455
    _globals['_PIPELINERESOURCES_DISK']._serialized_end = 3704
    _globals['_PIPELINERESOURCES_DISK_TYPE']._serialized_start = 3621
    _globals['_PIPELINERESOURCES_DISK_TYPE']._serialized_end = 3704
    _globals['_PIPELINEPARAMETER']._serialized_start = 3707
    _globals['_PIPELINEPARAMETER']._serialized_end = 3900
    _globals['_PIPELINEPARAMETER_LOCALCOPY']._serialized_start = 3861
    _globals['_PIPELINEPARAMETER_LOCALCOPY']._serialized_end = 3900
    _globals['_DOCKEREXECUTOR']._serialized_start = 3902
    _globals['_DOCKEREXECUTOR']._serialized_end = 3951
    _globals['_PIPELINESV1ALPHA2']._serialized_start = 3954
    _globals['_PIPELINESV1ALPHA2']._serialized_end = 4986