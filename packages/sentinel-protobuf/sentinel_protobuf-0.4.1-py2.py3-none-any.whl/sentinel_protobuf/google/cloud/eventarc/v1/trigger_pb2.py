"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/v1/trigger.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.eventarc.v1 import network_config_pb2 as google_dot_cloud_dot_eventarc_dot_v1_dot_network__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/eventarc/v1/trigger.proto\x12\x18google.cloud.eventarc.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/eventarc/v1/network_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\x9e\x07\n\x07Trigger\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\revent_filters\x18\x08 \x03(\x0b2%.google.cloud.eventarc.v1.EventFilterB\x06\xe0A\x06\xe0A\x02\x12B\n\x0fservice_account\x18\t \x01(\tB)\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount\x12?\n\x0bdestination\x18\n \x01(\x0b2%.google.cloud.eventarc.v1.DestinationB\x03\xe0A\x02\x12;\n\ttransport\x18\x0b \x01(\x0b2#.google.cloud.eventarc.v1.TransportB\x03\xe0A\x01\x12B\n\x06labels\x18\x0c \x03(\x0b2-.google.cloud.eventarc.v1.Trigger.LabelsEntryB\x03\xe0A\x01\x12\x14\n\x07channel\x18\r \x01(\tB\x03\xe0A\x01\x12J\n\nconditions\x18\x0f \x03(\x0b21.google.cloud.eventarc.v1.Trigger.ConditionsEntryB\x03\xe0A\x03\x12$\n\x17event_data_content_type\x18\x10 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x13 \x01(\x08B\x03\xe0A\x03\x12\x11\n\x04etag\x18c \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a[\n\x0fConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x127\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.eventarc.v1.StateCondition:\x028\x01:s\xeaAp\n\x1feventarc.googleapis.com/Trigger\x12:projects/{project}/locations/{location}/triggers/{trigger}*\x08triggers2\x07trigger"P\n\x0bEventFilter\x12\x16\n\tattribute\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08operator\x18\x03 \x01(\tB\x03\xe0A\x01"A\n\x0eStateCondition\x12\x1e\n\x04code\x18\x01 \x01(\x0e2\x10.google.rpc.Code\x12\x0f\n\x07message\x18\x02 \x01(\t"\x91\x03\n\x0bDestination\x127\n\tcloud_run\x18\x01 \x01(\x0b2".google.cloud.eventarc.v1.CloudRunH\x00\x12J\n\x0ecloud_function\x18\x02 \x01(\tB0\xfaA-\n+cloudfunctions.googleapis.com/CloudFunctionH\x00\x12,\n\x03gke\x18\x03 \x01(\x0b2\x1d.google.cloud.eventarc.v1.GKEH\x00\x12:\n\x08workflow\x18\x04 \x01(\tB&\xfaA#\n!workflows.googleapis.com/WorkflowH\x00\x12?\n\rhttp_endpoint\x18\x05 \x01(\x0b2&.google.cloud.eventarc.v1.HttpEndpointH\x00\x12D\n\x0enetwork_config\x18\x06 \x01(\x0b2\'.google.cloud.eventarc.v1.NetworkConfigB\x03\xe0A\x01B\x0c\n\ndescriptor"O\n\tTransport\x122\n\x06pubsub\x18\x01 \x01(\x0b2 .google.cloud.eventarc.v1.PubsubH\x00B\x0e\n\x0cintermediary"g\n\x08CloudRun\x123\n\x07service\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1arun.googleapis.com/Service\x12\x11\n\x04path\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06region\x18\x03 \x01(\tB\x03\xe0A\x02"s\n\x03GKE\x12\x14\n\x07cluster\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08location\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tnamespace\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07service\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04path\x18\x05 \x01(\tB\x03\xe0A\x01"7\n\x06Pubsub\x12\x12\n\x05topic\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0csubscription\x18\x02 \x01(\tB\x03\xe0A\x03" \n\x0cHttpEndpoint\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02B\xb1\x04\n\x1ccom.google.cloud.eventarc.v1B\x0cTriggerProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaA\x1f\n\x1arun.googleapis.com/Service\x12\x01*\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.v1.trigger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.eventarc.v1B\x0cTriggerProtoP\x01Z8cloud.google.com/go/eventarc/apiv1/eventarcpb;eventarcpb\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaA\x1f\n\x1arun.googleapis.com/Service\x12\x01*\xeaAa\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}'
    _globals['_TRIGGER_LABELSENTRY']._loaded_options = None
    _globals['_TRIGGER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TRIGGER_CONDITIONSENTRY']._loaded_options = None
    _globals['_TRIGGER_CONDITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_TRIGGER'].fields_by_name['name']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TRIGGER'].fields_by_name['uid']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER'].fields_by_name['create_time']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER'].fields_by_name['event_filters']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['event_filters']._serialized_options = b'\xe0A\x06\xe0A\x02'
    _globals['_TRIGGER'].fields_by_name['service_account']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_TRIGGER'].fields_by_name['destination']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['destination']._serialized_options = b'\xe0A\x02'
    _globals['_TRIGGER'].fields_by_name['transport']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['transport']._serialized_options = b'\xe0A\x01'
    _globals['_TRIGGER'].fields_by_name['labels']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_TRIGGER'].fields_by_name['channel']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['channel']._serialized_options = b'\xe0A\x01'
    _globals['_TRIGGER'].fields_by_name['conditions']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['conditions']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER'].fields_by_name['event_data_content_type']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['event_data_content_type']._serialized_options = b'\xe0A\x01'
    _globals['_TRIGGER'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER'].fields_by_name['etag']._loaded_options = None
    _globals['_TRIGGER'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_TRIGGER']._loaded_options = None
    _globals['_TRIGGER']._serialized_options = b'\xeaAp\n\x1feventarc.googleapis.com/Trigger\x12:projects/{project}/locations/{location}/triggers/{trigger}*\x08triggers2\x07trigger'
    _globals['_EVENTFILTER'].fields_by_name['attribute']._loaded_options = None
    _globals['_EVENTFILTER'].fields_by_name['attribute']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_EVENTFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTFILTER'].fields_by_name['operator']._loaded_options = None
    _globals['_EVENTFILTER'].fields_by_name['operator']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATION'].fields_by_name['cloud_function']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['cloud_function']._serialized_options = b'\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction'
    _globals['_DESTINATION'].fields_by_name['workflow']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['workflow']._serialized_options = b'\xfaA#\n!workflows.googleapis.com/Workflow'
    _globals['_DESTINATION'].fields_by_name['network_config']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['network_config']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDRUN'].fields_by_name['service']._loaded_options = None
    _globals['_CLOUDRUN'].fields_by_name['service']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1arun.googleapis.com/Service'
    _globals['_CLOUDRUN'].fields_by_name['path']._loaded_options = None
    _globals['_CLOUDRUN'].fields_by_name['path']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDRUN'].fields_by_name['region']._loaded_options = None
    _globals['_CLOUDRUN'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_GKE'].fields_by_name['cluster']._loaded_options = None
    _globals['_GKE'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02'
    _globals['_GKE'].fields_by_name['location']._loaded_options = None
    _globals['_GKE'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_GKE'].fields_by_name['namespace']._loaded_options = None
    _globals['_GKE'].fields_by_name['namespace']._serialized_options = b'\xe0A\x02'
    _globals['_GKE'].fields_by_name['service']._loaded_options = None
    _globals['_GKE'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_GKE'].fields_by_name['path']._loaded_options = None
    _globals['_GKE'].fields_by_name['path']._serialized_options = b'\xe0A\x01'
    _globals['_PUBSUB'].fields_by_name['topic']._loaded_options = None
    _globals['_PUBSUB'].fields_by_name['topic']._serialized_options = b'\xe0A\x01'
    _globals['_PUBSUB'].fields_by_name['subscription']._loaded_options = None
    _globals['_PUBSUB'].fields_by_name['subscription']._serialized_options = b'\xe0A\x03'
    _globals['_HTTPENDPOINT'].fields_by_name['uri']._loaded_options = None
    _globals['_HTTPENDPOINT'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_TRIGGER']._serialized_start = 232
    _globals['_TRIGGER']._serialized_end = 1158
    _globals['_TRIGGER_LABELSENTRY']._serialized_start = 903
    _globals['_TRIGGER_LABELSENTRY']._serialized_end = 948
    _globals['_TRIGGER_CONDITIONSENTRY']._serialized_start = 950
    _globals['_TRIGGER_CONDITIONSENTRY']._serialized_end = 1041
    _globals['_EVENTFILTER']._serialized_start = 1160
    _globals['_EVENTFILTER']._serialized_end = 1240
    _globals['_STATECONDITION']._serialized_start = 1242
    _globals['_STATECONDITION']._serialized_end = 1307
    _globals['_DESTINATION']._serialized_start = 1310
    _globals['_DESTINATION']._serialized_end = 1711
    _globals['_TRANSPORT']._serialized_start = 1713
    _globals['_TRANSPORT']._serialized_end = 1792
    _globals['_CLOUDRUN']._serialized_start = 1794
    _globals['_CLOUDRUN']._serialized_end = 1897
    _globals['_GKE']._serialized_start = 1899
    _globals['_GKE']._serialized_end = 2014
    _globals['_PUBSUB']._serialized_start = 2016
    _globals['_PUBSUB']._serialized_end = 2071
    _globals['_HTTPENDPOINT']._serialized_start = 2073
    _globals['_HTTPENDPOINT']._serialized_end = 2105