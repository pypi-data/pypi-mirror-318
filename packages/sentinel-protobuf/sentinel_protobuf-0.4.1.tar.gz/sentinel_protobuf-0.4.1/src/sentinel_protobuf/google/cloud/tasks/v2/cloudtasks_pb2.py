"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/tasks/v2/cloudtasks.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2 import queue_pb2 as google_dot_cloud_dot_tasks_dot_v2_dot_queue__pb2
from .....google.cloud.tasks.v2 import task_pb2 as google_dot_cloud_dot_tasks_dot_v2_dot_task__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/tasks/v2/cloudtasks.proto\x12\x15google.cloud.tasks.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/cloud/tasks/v2/queue.proto\x1a google/cloud/tasks/v2/task.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x83\x01\n\x11ListQueuesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"[\n\x12ListQueuesResponse\x12,\n\x06queues\x18\x01 \x03(\x0b2\x1c.google.cloud.tasks.v2.Queue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\x0fGetQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"\x7f\n\x12CreateQueueRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue\x120\n\x05queue\x18\x02 \x01(\x0b2\x1c.google.cloud.tasks.v2.QueueB\x03\xe0A\x02"w\n\x12UpdateQueueRequest\x120\n\x05queue\x18\x01 \x01(\x0b2\x1c.google.cloud.tasks.v2.QueueB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x12DeleteQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"J\n\x11PurgeQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"J\n\x11PauseQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"K\n\x12ResumeQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"\xaa\x01\n\x10ListTasksRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task\x127\n\rresponse_view\x18\x02 \x01(\x0e2 .google.cloud.tasks.v2.Task.View\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"X\n\x11ListTasksResponse\x12*\n\x05tasks\x18\x01 \x03(\x0b2\x1b.google.cloud.tasks.v2.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x7f\n\x0eGetTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task\x127\n\rresponse_view\x18\x02 \x01(\x0e2 .google.cloud.tasks.v2.Task.View"\xb4\x01\n\x11CreateTaskRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task\x12.\n\x04task\x18\x02 \x01(\x0b2\x1b.google.cloud.tasks.v2.TaskB\x03\xe0A\x02\x127\n\rresponse_view\x18\x03 \x01(\x0e2 .google.cloud.tasks.v2.Task.View"I\n\x11DeleteTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task"\x7f\n\x0eRunTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task\x127\n\rresponse_view\x18\x02 \x01(\x0e2 .google.cloud.tasks.v2.Task.View2\xdd\x14\n\nCloudTasks\x12\x9e\x01\n\nListQueues\x12(.google.cloud.tasks.v2.ListQueuesRequest\x1a).google.cloud.tasks.v2.ListQueuesResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v2/{parent=projects/*/locations/*}/queues\x12\x8b\x01\n\x08GetQueue\x12&.google.cloud.tasks.v2.GetQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v2/{name=projects/*/locations/*/queues/*}\x12\xa0\x01\n\x0bCreateQueue\x12).google.cloud.tasks.v2.CreateQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"H\xdaA\x0cparent,queue\x82\xd3\xe4\x93\x023"*/v2/{parent=projects/*/locations/*}/queues:\x05queue\x12\xab\x01\n\x0bUpdateQueue\x12).google.cloud.tasks.v2.UpdateQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"S\xdaA\x11queue,update_mask\x82\xd3\xe4\x93\x02920/v2/{queue.name=projects/*/locations/*/queues/*}:\x05queue\x12\x8b\x01\n\x0bDeleteQueue\x12).google.cloud.tasks.v2.DeleteQueueRequest\x1a\x16.google.protobuf.Empty"9\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v2/{name=projects/*/locations/*/queues/*}\x12\x98\x01\n\nPurgeQueue\x12(.google.cloud.tasks.v2.PurgeQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"B\xdaA\x04name\x82\xd3\xe4\x93\x025"0/v2/{name=projects/*/locations/*/queues/*}:purge:\x01*\x12\x98\x01\n\nPauseQueue\x12(.google.cloud.tasks.v2.PauseQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"B\xdaA\x04name\x82\xd3\xe4\x93\x025"0/v2/{name=projects/*/locations/*/queues/*}:pause:\x01*\x12\x9b\x01\n\x0bResumeQueue\x12).google.cloud.tasks.v2.ResumeQueueRequest\x1a\x1c.google.cloud.tasks.v2.Queue"C\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v2/{name=projects/*/locations/*/queues/*}:resume:\x01*\x12\x9c\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Q\xdaA\x08resource\x82\xd3\xe4\x93\x02@";/v2/{resource=projects/*/locations/*/queues/*}:getIamPolicy:\x01*\x12\xa3\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"X\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02@";/v2/{resource=projects/*/locations/*/queues/*}:setIamPolicy:\x01*\x12\xce\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"c\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/queues/*}:testIamPermissions:\x01*\x12\xa3\x01\n\tListTasks\x12\'.google.cloud.tasks.v2.ListTasksRequest\x1a(.google.cloud.tasks.v2.ListTasksResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2/{parent=projects/*/locations/*/queues/*}/tasks\x12\x90\x01\n\x07GetTask\x12%.google.cloud.tasks.v2.GetTaskRequest\x1a\x1b.google.cloud.tasks.v2.Task"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2/{name=projects/*/locations/*/queues/*/tasks/*}\x12\xa0\x01\n\nCreateTask\x12(.google.cloud.tasks.v2.CreateTaskRequest\x1a\x1b.google.cloud.tasks.v2.Task"K\xdaA\x0bparent,task\x82\xd3\xe4\x93\x027"2/v2/{parent=projects/*/locations/*/queues/*}/tasks:\x01*\x12\x91\x01\n\nDeleteTask\x12(.google.cloud.tasks.v2.DeleteTaskRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2/{name=projects/*/locations/*/queues/*/tasks/*}\x12\x97\x01\n\x07RunTask\x12%.google.cloud.tasks.v2.RunTaskRequest\x1a\x1b.google.cloud.tasks.v2.Task"H\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/queues/*/tasks/*}:run:\x01*\x1aM\xcaA\x19cloudtasks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBv\n\x19com.google.cloud.tasks.v2B\x0fCloudTasksProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspb\xa2\x02\x05TASKSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2.cloudtasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.tasks.v2B\x0fCloudTasksProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspb\xa2\x02\x05TASKS'
    _globals['_LISTQUEUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUEUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue'
    _globals['_GETQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue'
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['queue']._loaded_options = None
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['queue']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUEUEREQUEST'].fields_by_name['queue']._loaded_options = None
    _globals['_UPDATEQUEUEREQUEST'].fields_by_name['queue']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_PURGEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PURGEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_PAUSEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_RESUMEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task'
    _globals['_GETTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task'
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_RUNTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_CLOUDTASKS']._loaded_options = None
    _globals['_CLOUDTASKS']._serialized_options = b'\xcaA\x19cloudtasks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDTASKS'].methods_by_name['ListQueues']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ListQueues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v2/{parent=projects/*/locations/*}/queues'
    _globals['_CLOUDTASKS'].methods_by_name['GetQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v2/{name=projects/*/locations/*/queues/*}'
    _globals['_CLOUDTASKS'].methods_by_name['CreateQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['CreateQueue']._serialized_options = b'\xdaA\x0cparent,queue\x82\xd3\xe4\x93\x023"*/v2/{parent=projects/*/locations/*}/queues:\x05queue'
    _globals['_CLOUDTASKS'].methods_by_name['UpdateQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['UpdateQueue']._serialized_options = b'\xdaA\x11queue,update_mask\x82\xd3\xe4\x93\x02920/v2/{queue.name=projects/*/locations/*/queues/*}:\x05queue'
    _globals['_CLOUDTASKS'].methods_by_name['DeleteQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['DeleteQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v2/{name=projects/*/locations/*/queues/*}'
    _globals['_CLOUDTASKS'].methods_by_name['PurgeQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['PurgeQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025"0/v2/{name=projects/*/locations/*/queues/*}:purge:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['PauseQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['PauseQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025"0/v2/{name=projects/*/locations/*/queues/*}:pause:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['ResumeQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ResumeQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v2/{name=projects/*/locations/*/queues/*}:resume:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02@";/v2/{resource=projects/*/locations/*/queues/*}:getIamPolicy:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02@";/v2/{resource=projects/*/locations/*/queues/*}:setIamPolicy:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/queues/*}:testIamPermissions:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['ListTasks']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ListTasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2/{parent=projects/*/locations/*/queues/*}/tasks'
    _globals['_CLOUDTASKS'].methods_by_name['GetTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2/{name=projects/*/locations/*/queues/*/tasks/*}'
    _globals['_CLOUDTASKS'].methods_by_name['CreateTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['CreateTask']._serialized_options = b'\xdaA\x0bparent,task\x82\xd3\xe4\x93\x027"2/v2/{parent=projects/*/locations/*/queues/*}/tasks:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['DeleteTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['DeleteTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2/{name=projects/*/locations/*/queues/*/tasks/*}'
    _globals['_CLOUDTASKS'].methods_by_name['RunTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['RunTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v2/{name=projects/*/locations/*/queues/*/tasks/*}:run:\x01*'
    _globals['_LISTQUEUESREQUEST']._serialized_start = 373
    _globals['_LISTQUEUESREQUEST']._serialized_end = 504
    _globals['_LISTQUEUESRESPONSE']._serialized_start = 506
    _globals['_LISTQUEUESRESPONSE']._serialized_end = 597
    _globals['_GETQUEUEREQUEST']._serialized_start = 599
    _globals['_GETQUEUEREQUEST']._serialized_end = 671
    _globals['_CREATEQUEUEREQUEST']._serialized_start = 673
    _globals['_CREATEQUEUEREQUEST']._serialized_end = 800
    _globals['_UPDATEQUEUEREQUEST']._serialized_start = 802
    _globals['_UPDATEQUEUEREQUEST']._serialized_end = 921
    _globals['_DELETEQUEUEREQUEST']._serialized_start = 923
    _globals['_DELETEQUEUEREQUEST']._serialized_end = 998
    _globals['_PURGEQUEUEREQUEST']._serialized_start = 1000
    _globals['_PURGEQUEUEREQUEST']._serialized_end = 1074
    _globals['_PAUSEQUEUEREQUEST']._serialized_start = 1076
    _globals['_PAUSEQUEUEREQUEST']._serialized_end = 1150
    _globals['_RESUMEQUEUEREQUEST']._serialized_start = 1152
    _globals['_RESUMEQUEUEREQUEST']._serialized_end = 1227
    _globals['_LISTTASKSREQUEST']._serialized_start = 1230
    _globals['_LISTTASKSREQUEST']._serialized_end = 1400
    _globals['_LISTTASKSRESPONSE']._serialized_start = 1402
    _globals['_LISTTASKSRESPONSE']._serialized_end = 1490
    _globals['_GETTASKREQUEST']._serialized_start = 1492
    _globals['_GETTASKREQUEST']._serialized_end = 1619
    _globals['_CREATETASKREQUEST']._serialized_start = 1622
    _globals['_CREATETASKREQUEST']._serialized_end = 1802
    _globals['_DELETETASKREQUEST']._serialized_start = 1804
    _globals['_DELETETASKREQUEST']._serialized_end = 1877
    _globals['_RUNTASKREQUEST']._serialized_start = 1879
    _globals['_RUNTASKREQUEST']._serialized_end = 2006
    _globals['_CLOUDTASKS']._serialized_start = 2009
    _globals['_CLOUDTASKS']._serialized_end = 4662