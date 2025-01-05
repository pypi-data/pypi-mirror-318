"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/resultstore_upload.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import action_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_action__pb2
from .....google.devtools.resultstore.v2 import configuration_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configuration__pb2
from .....google.devtools.resultstore.v2 import configured_target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_configured__target__pb2
from .....google.devtools.resultstore.v2 import file_set_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__set__pb2
from .....google.devtools.resultstore.v2 import invocation_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_invocation__pb2
from .....google.devtools.resultstore.v2 import target_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_target__pb2
from .....google.devtools.resultstore.v2 import upload_metadata_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_upload__metadata__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/devtools/resultstore/v2/resultstore_upload.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/action.proto\x1a2google/devtools/resultstore/v2/configuration.proto\x1a6google/devtools/resultstore/v2/configured_target.proto\x1a-google/devtools/resultstore/v2/file_set.proto\x1a/google/devtools/resultstore/v2/invocation.proto\x1a+google/devtools/resultstore/v2/target.proto\x1a4google/devtools/resultstore/v2/upload_metadata.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x02\n\x17CreateInvocationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x15\n\rinvocation_id\x18\x02 \x01(\t\x12C\n\ninvocation\x18\x03 \x01(\x0b2*.google.devtools.resultstore.v2.InvocationB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x04 \x01(\t\x126\n\x12auto_finalize_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1c\n\x14initial_resume_token\x18\x07 \x01(\t\x12\x16\n\x0euploader_state\x18\x08 \x01(\x0c"\xa7\x01\n\x17UpdateInvocationRequest\x12>\n\ninvocation\x18\x03 \x01(\x0b2*.google.devtools.resultstore.v2.Invocation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xba\x01\n\x16MergeInvocationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12>\n\ninvocation\x18\x03 \x01(\x0b2*.google.devtools.resultstore.v2.Invocation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"r\n\x16TouchInvocationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x1b\n\x13authorization_token\x18\x02 \x01(\t"b\n\x17TouchInvocationResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x02id\x18\x02 \x01(\x0b2-.google.devtools.resultstore.v2.Invocation.Id"V\n\x17DeleteInvocationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation"u\n\x19FinalizeInvocationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x1b\n\x13authorization_token\x18\x03 \x01(\t"e\n\x1aFinalizeInvocationResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x02id\x18\x02 \x01(\x0b2-.google.devtools.resultstore.v2.Invocation.Id"\xd5\x01\n\x13CreateTargetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12=\n\x06parent\x18\x02 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\ttarget_id\x18\x03 \x01(\t\x12;\n\x06target\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.TargetB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xb8\x01\n\x13UpdateTargetRequest\x126\n\x06target\x18\x03 \x01(\x0b2&.google.devtools.resultstore.v2.Target\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\xcb\x01\n\x12MergeTargetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x126\n\x06target\x18\x03 \x01(\x0b2&.google.devtools.resultstore.v2.Target\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"m\n\x15FinalizeTargetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target\x12\x1b\n\x13authorization_token\x18\x03 \x01(\t"]\n\x16FinalizeTargetResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x125\n\x02id\x18\x02 \x01(\x0b2).google.devtools.resultstore.v2.Target.Id"\xf0\x01\n\x1dCreateConfiguredTargetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x129\n\x06parent\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target\x12\x11\n\tconfig_id\x18\x03 \x01(\t\x12P\n\x11configured_target\x18\x04 \x01(\x0b20.google.devtools.resultstore.v2.ConfiguredTargetB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xd7\x01\n\x1dUpdateConfiguredTargetRequest\x12K\n\x11configured_target\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.ConfiguredTarget\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\xea\x01\n\x1cMergeConfiguredTargetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12K\n\x11configured_target\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.ConfiguredTarget\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\x81\x01\n\x1fFinalizeConfiguredTargetRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget\x12\x1b\n\x13authorization_token\x18\x03 \x01(\t"q\n FinalizeConfiguredTargetResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x02id\x18\x02 \x01(\x0b23.google.devtools.resultstore.v2.ConfiguredTarget.Id"\xdb\x01\n\x13CreateActionRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12C\n\x06parent\x18\x02 \x01(\tB3\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget\x12\x11\n\taction_id\x18\x03 \x01(\t\x12;\n\x06action\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.ActionB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xb8\x01\n\x13UpdateActionRequest\x126\n\x06action\x18\x03 \x01(\x0b2&.google.devtools.resultstore.v2.Action\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\xcb\x01\n\x12MergeActionRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x126\n\x06action\x18\x03 \x01(\x0b2&.google.devtools.resultstore.v2.Action\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\xea\x01\n\x1aCreateConfigurationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12=\n\x06parent\x18\x02 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x11\n\tconfig_id\x18\x03 \x01(\t\x12I\n\rconfiguration\x18\x04 \x01(\x0b2-.google.devtools.resultstore.v2.ConfigurationB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xcd\x01\n\x1aUpdateConfigurationRequest\x12D\n\rconfiguration\x18\x03 \x01(\x0b2-.google.devtools.resultstore.v2.Configuration\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x06 \x01(\x08"\xdb\x01\n\x14CreateFileSetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12=\n\x06parent\x18\x02 \x01(\tB-\xe0A\x02\xfaA\'\n%resultstore.googleapis.com/Invocation\x12\x13\n\x0bfile_set_id\x18\x03 \x01(\t\x12>\n\x08file_set\x18\x04 \x01(\x0b2\'.google.devtools.resultstore.v2.FileSetB\x03\xe0A\x02\x12\x1b\n\x13authorization_token\x18\x05 \x01(\t"\xbc\x01\n\x14UpdateFileSetRequest\x129\n\x08file_set\x18\x01 \x01(\x0b2\'.google.devtools.resultstore.v2.FileSet\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x03 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x04 \x01(\x08"\xcf\x01\n\x13MergeFileSetRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x129\n\x08file_set\x18\x02 \x01(\x0b2\'.google.devtools.resultstore.v2.FileSet\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13authorization_token\x18\x04 \x01(\t\x12\x1b\n\x13create_if_not_found\x18\x05 \x01(\x08"\xe6\x01\n\x12UploadBatchRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13authorization_token\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11next_resume_token\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cresume_token\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0euploader_state\x18\x06 \x01(\x0c\x12F\n\x0fupload_requests\x18\x05 \x03(\x0b2-.google.devtools.resultstore.v2.UploadRequest"\x15\n\x13UploadBatchResponse"\xcb\x06\n\rUploadRequest\x12<\n\x02id\x18\x01 \x01(\x0b20.google.devtools.resultstore.v2.UploadRequest.Id\x12W\n\x10upload_operation\x18\x02 \x01(\x0e2=.google.devtools.resultstore.v2.UploadRequest.UploadOperation\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1b\n\x13create_if_not_found\x18\n \x01(\x08\x12@\n\ninvocation\x18\x04 \x01(\x0b2*.google.devtools.resultstore.v2.InvocationH\x00\x128\n\x06target\x18\x05 \x01(\x0b2&.google.devtools.resultstore.v2.TargetH\x00\x12F\n\rconfiguration\x18\x06 \x01(\x0b2-.google.devtools.resultstore.v2.ConfigurationH\x00\x12M\n\x11configured_target\x18\x07 \x01(\x0b20.google.devtools.resultstore.v2.ConfiguredTargetH\x00\x128\n\x06action\x18\x08 \x01(\x0b2&.google.devtools.resultstore.v2.ActionH\x00\x12;\n\x08file_set\x18\t \x01(\x0b2\'.google.devtools.resultstore.v2.FileSetH\x00\x1aY\n\x02Id\x12\x11\n\ttarget_id\x18\x01 \x01(\t\x12\x18\n\x10configuration_id\x18\x02 \x01(\t\x12\x11\n\taction_id\x18\x03 \x01(\t\x12\x13\n\x0bfile_set_id\x18\x04 \x01(\t"d\n\x0fUploadOperation\x12 \n\x1cUPLOAD_OPERATION_UNSPECIFIED\x10\x00\x12\n\n\x06CREATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\t\n\x05MERGE\x10\x03\x12\x0c\n\x08FINALIZE\x10\x04B\n\n\x08resource"\x87\x01\n"GetInvocationUploadMetadataRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)resultstore.googleapis.com/UploadMetadata\x12 \n\x13authorization_token\x18\x02 \x01(\tB\x03\xe0A\x022\x8f)\n\x11ResultStoreUpload\x12\xd6\x01\n\x10CreateInvocation\x127.google.devtools.resultstore.v2.CreateInvocationRequest\x1a*.google.devtools.resultstore.v2.Invocation"]\xdaA7request_id,invocation,invocation_id,authorization_token\x82\xd3\xe4\x93\x02\x1d"\x0f/v2/invocations:\ninvocation\x12\xdd\x01\n\x10UpdateInvocation\x127.google.devtools.resultstore.v2.UpdateInvocationRequest\x1a*.google.devtools.resultstore.v2.Invocation"d\xdaA*invocation,update_mask,authorization_token\x82\xd3\xe4\x93\x0212#/v2/{invocation.name=invocations/*}:\ninvocation\x12\xab\x01\n\x0fMergeInvocation\x126.google.devtools.resultstore.v2.MergeInvocationRequest\x1a*.google.devtools.resultstore.v2.Invocation"4\x82\xd3\xe4\x93\x02.")/v2/{invocation.name=invocations/*}:merge:\x01*\x12\xad\x01\n\x0fTouchInvocation\x126.google.devtools.resultstore.v2.TouchInvocationRequest\x1a7.google.devtools.resultstore.v2.TouchInvocationResponse")\x82\xd3\xe4\x93\x02#"\x1e/v2/{name=invocations/*}:touch:\x01*\x12\xb9\x01\n\x12FinalizeInvocation\x129.google.devtools.resultstore.v2.FinalizeInvocationRequest\x1a:.google.devtools.resultstore.v2.FinalizeInvocationResponse",\x82\xd3\xe4\x93\x02&"!/v2/{name=invocations/*}:finalize:\x01*\x12\x85\x01\n\x10DeleteInvocation\x127.google.devtools.resultstore.v2.DeleteInvocationRequest\x1a\x16.google.protobuf.Empty" \x82\xd3\xe4\x93\x02\x1a*\x18/v2/{name=invocations/*}\x12\xd8\x01\n\x0cCreateTarget\x123.google.devtools.resultstore.v2.CreateTargetRequest\x1a&.google.devtools.resultstore.v2.Target"k\xdaA6request_id,parent,target,target_id,authorization_token\x82\xd3\xe4\x93\x02,""/v2/{parent=invocations/*}/targets:\x06target\x12\xcf\x01\n\x0cUpdateTarget\x123.google.devtools.resultstore.v2.UpdateTargetRequest\x1a&.google.devtools.resultstore.v2.Target"b\xdaA&target,update_mask,authorization_token\x82\xd3\xe4\x93\x0232)/v2/{target.name=invocations/*/targets/*}:\x06target\x12\xa5\x01\n\x0bMergeTarget\x122.google.devtools.resultstore.v2.MergeTargetRequest\x1a&.google.devtools.resultstore.v2.Target":\x82\xd3\xe4\x93\x024"//v2/{target.name=invocations/*/targets/*}:merge:\x01*\x12\xb7\x01\n\x0eFinalizeTarget\x125.google.devtools.resultstore.v2.FinalizeTargetRequest\x1a6.google.devtools.resultstore.v2.FinalizeTargetResponse"6\x82\xd3\xe4\x93\x020"+/v2/{name=invocations/*/targets/*}:finalize:\x01*\x12\xa1\x02\n\x16CreateConfiguredTarget\x12=.google.devtools.resultstore.v2.CreateConfiguredTargetRequest\x1a0.google.devtools.resultstore.v2.ConfiguredTarget"\x95\x01\xdaAArequest_id,parent,configured_target,config_id,authorization_token\x82\xd3\xe4\x93\x02K"6/v2/{parent=invocations/*/targets/*}/configuredTargets:\x11configured_target\x12\xa3\x02\n\x16UpdateConfiguredTarget\x12=.google.devtools.resultstore.v2.UpdateConfiguredTargetRequest\x1a0.google.devtools.resultstore.v2.ConfiguredTarget"\x97\x01\xdaA1configured_target,update_mask,authorization_token\x82\xd3\xe4\x93\x02]2H/v2/{configured_target.name=invocations/*/targets/*/configuredTargets/*}:\x11configured_target\x12\xe2\x01\n\x15MergeConfiguredTarget\x12<.google.devtools.resultstore.v2.MergeConfiguredTargetRequest\x1a0.google.devtools.resultstore.v2.ConfiguredTarget"Y\x82\xd3\xe4\x93\x02S"N/v2/{configured_target.name=invocations/*/targets/*/configuredTargets/*}:merge:\x01*\x12\xe9\x01\n\x18FinalizeConfiguredTarget\x12?.google.devtools.resultstore.v2.FinalizeConfiguredTargetRequest\x1a@.google.devtools.resultstore.v2.FinalizeConfiguredTargetResponse"J\x82\xd3\xe4\x93\x02D"?/v2/{name=invocations/*/targets/*/configuredTargets/*}:finalize:\x01*\x12\xf7\x01\n\x0cCreateAction\x123.google.devtools.resultstore.v2.CreateActionRequest\x1a&.google.devtools.resultstore.v2.Action"\x89\x01\xdaA6request_id,parent,action,action_id,authorization_token\x82\xd3\xe4\x93\x02J"@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions:\x06action\x12\xee\x01\n\x0cUpdateAction\x123.google.devtools.resultstore.v2.UpdateActionRequest\x1a&.google.devtools.resultstore.v2.Action"\x80\x01\xdaA&action,update_mask,authorization_token\x82\xd3\xe4\x93\x02Q2G/v2/{action.name=invocations/*/targets/*/configuredTargets/*/actions/*}:\x06action\x12\xc3\x01\n\x0bMergeAction\x122.google.devtools.resultstore.v2.MergeActionRequest\x1a&.google.devtools.resultstore.v2.Action"X\x82\xd3\xe4\x93\x02R"M/v2/{action.name=invocations/*/targets/*/configuredTargets/*/actions/*}:merge:\x01*\x12\xfb\x01\n\x13CreateConfiguration\x12:.google.devtools.resultstore.v2.CreateConfigurationRequest\x1a-.google.devtools.resultstore.v2.Configuration"y\xdaA=request_id,parent,configuration,config_id,authorization_token\x82\xd3\xe4\x93\x023""/v2/{parent=invocations/*}/configs:\rconfiguration\x12\xf9\x01\n\x13UpdateConfiguration\x12:.google.devtools.resultstore.v2.UpdateConfigurationRequest\x1a-.google.devtools.resultstore.v2.Configuration"w\xdaA-configuration,update_mask,authorization_token\x82\xd3\xe4\x93\x02A20/v2/{configuration.name=invocations/*/configs/*}:\rconfiguration\x12\xe2\x01\n\rCreateFileSet\x124.google.devtools.resultstore.v2.CreateFileSetRequest\x1a\'.google.devtools.resultstore.v2.FileSet"r\xdaA:request_id,parent,file_set,file_set_id,authorization_token\x82\xd3\xe4\x93\x02/"#/v2/{parent=invocations/*}/fileSets:\x08file_set\x12\xd9\x01\n\rUpdateFileSet\x124.google.devtools.resultstore.v2.UpdateFileSetRequest\x1a\'.google.devtools.resultstore.v2.FileSet"i\xdaA(file_set,update_mask,authorization_token\x82\xd3\xe4\x93\x0282,/v2/{file_set.name=invocations/*/fileSets/*}:\x08file_set\x12\xab\x01\n\x0cMergeFileSet\x123.google.devtools.resultstore.v2.MergeFileSetRequest\x1a\'.google.devtools.resultstore.v2.FileSet"=\x82\xd3\xe4\x93\x027"2/v2/{file_set.name=invocations/*/fileSets/*}:merge:\x01*\x12\xaa\x01\n\x0bUploadBatch\x122.google.devtools.resultstore.v2.UploadBatchRequest\x1a3.google.devtools.resultstore.v2.UploadBatchResponse"2\x82\xd3\xe4\x93\x02,"\'/v2/{parent=invocations/*}/batch:upload:\x01*\x12\xdd\x01\n\x1bGetInvocationUploadMetadata\x12B.google.devtools.resultstore.v2.GetInvocationUploadMetadataRequest\x1a..google.devtools.resultstore.v2.UploadMetadata"J\xdaA\x18name,authorization_token\x82\xd3\xe4\x93\x02)\x12\'/v2/{name=invocations/*/uploadMetadata}\x1aN\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x89\x01\n"com.google.devtools.resultstore.v2B\x16ResultStoreUploadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.resultstore_upload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x16ResultStoreUploadProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_CREATEINVOCATIONREQUEST'].fields_by_name['invocation']._loaded_options = None
    _globals['_CREATEINVOCATIONREQUEST'].fields_by_name['invocation']._serialized_options = b'\xe0A\x02'
    _globals['_TOUCHINVOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TOUCHINVOCATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_DELETEINVOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINVOCATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_FINALIZEINVOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FINALIZEINVOCATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_CREATETARGETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETARGETREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_CREATETARGETREQUEST'].fields_by_name['target']._loaded_options = None
    _globals['_CREATETARGETREQUEST'].fields_by_name['target']._serialized_options = b'\xe0A\x02'
    _globals['_FINALIZETARGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FINALIZETARGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target'
    _globals['_CREATECONFIGUREDTARGETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONFIGUREDTARGETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!resultstore.googleapis.com/Target'
    _globals['_CREATECONFIGUREDTARGETREQUEST'].fields_by_name['configured_target']._loaded_options = None
    _globals['_CREATECONFIGUREDTARGETREQUEST'].fields_by_name['configured_target']._serialized_options = b'\xe0A\x02'
    _globals['_FINALIZECONFIGUREDTARGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FINALIZECONFIGUREDTARGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget'
    _globals['_CREATEACTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEACTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+resultstore.googleapis.com/ConfiguredTarget'
    _globals['_CREATEACTIONREQUEST'].fields_by_name['action']._loaded_options = None
    _globals['_CREATEACTIONREQUEST'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFILESETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFILESETREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%resultstore.googleapis.com/Invocation"
    _globals['_CREATEFILESETREQUEST'].fields_by_name['file_set']._loaded_options = None
    _globals['_CREATEFILESETREQUEST'].fields_by_name['file_set']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['authorization_token']._loaded_options = None
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['authorization_token']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['next_resume_token']._loaded_options = None
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['next_resume_token']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['resume_token']._loaded_options = None
    _globals['_UPLOADBATCHREQUEST'].fields_by_name['resume_token']._serialized_options = b'\xe0A\x02'
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)resultstore.googleapis.com/UploadMetadata'
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST'].fields_by_name['authorization_token']._loaded_options = None
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST'].fields_by_name['authorization_token']._serialized_options = b'\xe0A\x02'
    _globals['_RESULTSTOREUPLOAD']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD']._serialized_options = b'\xcaA\x1aresultstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateInvocation']._serialized_options = b'\xdaA7request_id,invocation,invocation_id,authorization_token\x82\xd3\xe4\x93\x02\x1d"\x0f/v2/invocations:\ninvocation'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateInvocation']._serialized_options = b'\xdaA*invocation,update_mask,authorization_token\x82\xd3\xe4\x93\x0212#/v2/{invocation.name=invocations/*}:\ninvocation'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeInvocation']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v2/{invocation.name=invocations/*}:merge:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['TouchInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['TouchInvocation']._serialized_options = b'\x82\xd3\xe4\x93\x02#"\x1e/v2/{name=invocations/*}:touch:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeInvocation']._serialized_options = b'\x82\xd3\xe4\x93\x02&"!/v2/{name=invocations/*}:finalize:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['DeleteInvocation']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['DeleteInvocation']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a*\x18/v2/{name=invocations/*}'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateTarget']._serialized_options = b'\xdaA6request_id,parent,target,target_id,authorization_token\x82\xd3\xe4\x93\x02,""/v2/{parent=invocations/*}/targets:\x06target'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateTarget']._serialized_options = b'\xdaA&target,update_mask,authorization_token\x82\xd3\xe4\x93\x0232)/v2/{target.name=invocations/*/targets/*}:\x06target'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeTarget']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v2/{target.name=invocations/*/targets/*}:merge:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeTarget']._serialized_options = b'\x82\xd3\xe4\x93\x020"+/v2/{name=invocations/*/targets/*}:finalize:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateConfiguredTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateConfiguredTarget']._serialized_options = b'\xdaAArequest_id,parent,configured_target,config_id,authorization_token\x82\xd3\xe4\x93\x02K"6/v2/{parent=invocations/*/targets/*}/configuredTargets:\x11configured_target'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateConfiguredTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateConfiguredTarget']._serialized_options = b'\xdaA1configured_target,update_mask,authorization_token\x82\xd3\xe4\x93\x02]2H/v2/{configured_target.name=invocations/*/targets/*/configuredTargets/*}:\x11configured_target'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeConfiguredTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeConfiguredTarget']._serialized_options = b'\x82\xd3\xe4\x93\x02S"N/v2/{configured_target.name=invocations/*/targets/*/configuredTargets/*}:merge:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeConfiguredTarget']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['FinalizeConfiguredTarget']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v2/{name=invocations/*/targets/*/configuredTargets/*}:finalize:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateAction']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateAction']._serialized_options = b'\xdaA6request_id,parent,action,action_id,authorization_token\x82\xd3\xe4\x93\x02J"@/v2/{parent=invocations/*/targets/*/configuredTargets/*}/actions:\x06action'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateAction']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateAction']._serialized_options = b'\xdaA&action,update_mask,authorization_token\x82\xd3\xe4\x93\x02Q2G/v2/{action.name=invocations/*/targets/*/configuredTargets/*/actions/*}:\x06action'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeAction']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeAction']._serialized_options = b'\x82\xd3\xe4\x93\x02R"M/v2/{action.name=invocations/*/targets/*/configuredTargets/*/actions/*}:merge:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateConfiguration']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateConfiguration']._serialized_options = b'\xdaA=request_id,parent,configuration,config_id,authorization_token\x82\xd3\xe4\x93\x023""/v2/{parent=invocations/*}/configs:\rconfiguration'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateConfiguration']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateConfiguration']._serialized_options = b'\xdaA-configuration,update_mask,authorization_token\x82\xd3\xe4\x93\x02A20/v2/{configuration.name=invocations/*/configs/*}:\rconfiguration'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateFileSet']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['CreateFileSet']._serialized_options = b'\xdaA:request_id,parent,file_set,file_set_id,authorization_token\x82\xd3\xe4\x93\x02/"#/v2/{parent=invocations/*}/fileSets:\x08file_set'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateFileSet']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UpdateFileSet']._serialized_options = b'\xdaA(file_set,update_mask,authorization_token\x82\xd3\xe4\x93\x0282,/v2/{file_set.name=invocations/*/fileSets/*}:\x08file_set'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeFileSet']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['MergeFileSet']._serialized_options = b'\x82\xd3\xe4\x93\x027"2/v2/{file_set.name=invocations/*/fileSets/*}:merge:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UploadBatch']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['UploadBatch']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v2/{parent=invocations/*}/batch:upload:\x01*'
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['GetInvocationUploadMetadata']._loaded_options = None
    _globals['_RESULTSTOREUPLOAD'].methods_by_name['GetInvocationUploadMetadata']._serialized_options = b"\xdaA\x18name,authorization_token\x82\xd3\xe4\x93\x02)\x12'/v2/{name=invocations/*/uploadMetadata}"
    _globals['_CREATEINVOCATIONREQUEST']._serialized_start = 651
    _globals['_CREATEINVOCATIONREQUEST']._serialized_end = 927
    _globals['_UPDATEINVOCATIONREQUEST']._serialized_start = 930
    _globals['_UPDATEINVOCATIONREQUEST']._serialized_end = 1097
    _globals['_MERGEINVOCATIONREQUEST']._serialized_start = 1100
    _globals['_MERGEINVOCATIONREQUEST']._serialized_end = 1286
    _globals['_TOUCHINVOCATIONREQUEST']._serialized_start = 1288
    _globals['_TOUCHINVOCATIONREQUEST']._serialized_end = 1402
    _globals['_TOUCHINVOCATIONRESPONSE']._serialized_start = 1404
    _globals['_TOUCHINVOCATIONRESPONSE']._serialized_end = 1502
    _globals['_DELETEINVOCATIONREQUEST']._serialized_start = 1504
    _globals['_DELETEINVOCATIONREQUEST']._serialized_end = 1590
    _globals['_FINALIZEINVOCATIONREQUEST']._serialized_start = 1592
    _globals['_FINALIZEINVOCATIONREQUEST']._serialized_end = 1709
    _globals['_FINALIZEINVOCATIONRESPONSE']._serialized_start = 1711
    _globals['_FINALIZEINVOCATIONRESPONSE']._serialized_end = 1812
    _globals['_CREATETARGETREQUEST']._serialized_start = 1815
    _globals['_CREATETARGETREQUEST']._serialized_end = 2028
    _globals['_UPDATETARGETREQUEST']._serialized_start = 2031
    _globals['_UPDATETARGETREQUEST']._serialized_end = 2215
    _globals['_MERGETARGETREQUEST']._serialized_start = 2218
    _globals['_MERGETARGETREQUEST']._serialized_end = 2421
    _globals['_FINALIZETARGETREQUEST']._serialized_start = 2423
    _globals['_FINALIZETARGETREQUEST']._serialized_end = 2532
    _globals['_FINALIZETARGETRESPONSE']._serialized_start = 2534
    _globals['_FINALIZETARGETRESPONSE']._serialized_end = 2627
    _globals['_CREATECONFIGUREDTARGETREQUEST']._serialized_start = 2630
    _globals['_CREATECONFIGUREDTARGETREQUEST']._serialized_end = 2870
    _globals['_UPDATECONFIGUREDTARGETREQUEST']._serialized_start = 2873
    _globals['_UPDATECONFIGUREDTARGETREQUEST']._serialized_end = 3088
    _globals['_MERGECONFIGUREDTARGETREQUEST']._serialized_start = 3091
    _globals['_MERGECONFIGUREDTARGETREQUEST']._serialized_end = 3325
    _globals['_FINALIZECONFIGUREDTARGETREQUEST']._serialized_start = 3328
    _globals['_FINALIZECONFIGUREDTARGETREQUEST']._serialized_end = 3457
    _globals['_FINALIZECONFIGUREDTARGETRESPONSE']._serialized_start = 3459
    _globals['_FINALIZECONFIGUREDTARGETRESPONSE']._serialized_end = 3572
    _globals['_CREATEACTIONREQUEST']._serialized_start = 3575
    _globals['_CREATEACTIONREQUEST']._serialized_end = 3794
    _globals['_UPDATEACTIONREQUEST']._serialized_start = 3797
    _globals['_UPDATEACTIONREQUEST']._serialized_end = 3981
    _globals['_MERGEACTIONREQUEST']._serialized_start = 3984
    _globals['_MERGEACTIONREQUEST']._serialized_end = 4187
    _globals['_CREATECONFIGURATIONREQUEST']._serialized_start = 4190
    _globals['_CREATECONFIGURATIONREQUEST']._serialized_end = 4424
    _globals['_UPDATECONFIGURATIONREQUEST']._serialized_start = 4427
    _globals['_UPDATECONFIGURATIONREQUEST']._serialized_end = 4632
    _globals['_CREATEFILESETREQUEST']._serialized_start = 4635
    _globals['_CREATEFILESETREQUEST']._serialized_end = 4854
    _globals['_UPDATEFILESETREQUEST']._serialized_start = 4857
    _globals['_UPDATEFILESETREQUEST']._serialized_end = 5045
    _globals['_MERGEFILESETREQUEST']._serialized_start = 5048
    _globals['_MERGEFILESETREQUEST']._serialized_end = 5255
    _globals['_UPLOADBATCHREQUEST']._serialized_start = 5258
    _globals['_UPLOADBATCHREQUEST']._serialized_end = 5488
    _globals['_UPLOADBATCHRESPONSE']._serialized_start = 5490
    _globals['_UPLOADBATCHRESPONSE']._serialized_end = 5511
    _globals['_UPLOADREQUEST']._serialized_start = 5514
    _globals['_UPLOADREQUEST']._serialized_end = 6357
    _globals['_UPLOADREQUEST_ID']._serialized_start = 6154
    _globals['_UPLOADREQUEST_ID']._serialized_end = 6243
    _globals['_UPLOADREQUEST_UPLOADOPERATION']._serialized_start = 6245
    _globals['_UPLOADREQUEST_UPLOADOPERATION']._serialized_end = 6345
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST']._serialized_start = 6360
    _globals['_GETINVOCATIONUPLOADMETADATAREQUEST']._serialized_end = 6495
    _globals['_RESULTSTOREUPLOAD']._serialized_start = 6498
    _globals['_RESULTSTOREUPLOAD']._serialized_end = 11761