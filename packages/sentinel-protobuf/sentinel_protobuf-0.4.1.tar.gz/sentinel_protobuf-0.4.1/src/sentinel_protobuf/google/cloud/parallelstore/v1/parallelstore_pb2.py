"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/parallelstore/v1/parallelstore.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/parallelstore/v1/parallelstore.proto\x12\x1dgoogle.cloud.parallelstore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x92\x08\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12A\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.parallelstore.v1.Instance.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x06labels\x18\x06 \x03(\x0b23.google.cloud.parallelstore.v1.Instance.LabelsEntryB\x03\xe0A\x01\x12\x1c\n\x0ccapacity_gib\x18\x08 \x01(\x03B\x06\xe0A\x05\xe0A\x02\x12\x19\n\x0cdaos_version\x18\t \x01(\tB\x03\xe0A\x03\x12\x1a\n\raccess_points\x18\n \x03(\tB\x03\xe0A\x03\x12:\n\x07network\x18\x0b \x01(\tB)\xe0A\x05\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network\x12D\n\x11reserved_ip_range\x18\x0c \x01(\tB)\xe0A\x05\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Address\x12N\n\x1beffective_reserved_ip_range\x18\x0e \x01(\tB)\xe0A\x05\xe0A\x03\xfaA \n\x1ecompute.googleapis.com/Address\x12N\n\x11file_stripe_level\x18\x0f \x01(\x0e2..google.cloud.parallelstore.v1.FileStripeLevelB\x03\xe0A\x01\x12X\n\x16directory_stripe_level\x18\x10 \x01(\x0e23.google.cloud.parallelstore.v1.DirectoryStripeLevelB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"a\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tUPGRADING\x10\x05:}\xeaAz\n%parallelstore.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance"\xb2\x01\n\x14ListInstancesRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%parallelstore.googleapis.com/Instance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x15ListInstancesResponse\x12:\n\tinstances\x18\x01 \x03(\x0b2\'.google.cloud.parallelstore.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x12GetInstanceRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%parallelstore.googleapis.com/Instance"\xc9\x01\n\x15CreateInstanceRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%parallelstore.googleapis.com/Instance\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x08instance\x18\x03 \x01(\x0b2\'.google.cloud.parallelstore.v1.InstanceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa6\x01\n\x15UpdateInstanceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x08instance\x18\x02 \x01(\x0b2\'.google.cloud.parallelstore.v1.InstanceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x15DeleteInstanceRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%parallelstore.googleapis.com/Instance\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"#\n\x0fSourceGcsBucket\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02"(\n\x14DestinationGcsBucket\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02"(\n\x13SourceParallelstore\x12\x11\n\x04path\x18\x01 \x01(\tB\x03\xe0A\x01"-\n\x18DestinationParallelstore\x12\x11\n\x04path\x18\x01 \x01(\tB\x03\xe0A\x01"\xf9\x02\n\x11ImportDataRequest\x12K\n\x11source_gcs_bucket\x18\x02 \x01(\x0b2..google.cloud.parallelstore.v1.SourceGcsBucketH\x00\x12\\\n\x19destination_parallelstore\x18\x03 \x01(\x0b27.google.cloud.parallelstore.v1.DestinationParallelstoreH\x01\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%parallelstore.googleapis.com/Instance\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12B\n\x0fservice_account\x18\x05 \x01(\tB)\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccountB\x08\n\x06sourceB\r\n\x0bdestination"\xf9\x02\n\x11ExportDataRequest\x12R\n\x14source_parallelstore\x18\x02 \x01(\x0b22.google.cloud.parallelstore.v1.SourceParallelstoreH\x00\x12U\n\x16destination_gcs_bucket\x18\x03 \x01(\x0b23.google.cloud.parallelstore.v1.DestinationGcsBucketH\x01\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%parallelstore.googleapis.com/Instance\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12B\n\x0fservice_account\x18\x05 \x01(\tB)\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccountB\x08\n\x06sourceB\r\n\x0bdestination"\x14\n\x12ImportDataResponse"\xd7\x02\n\x12ImportDataMetadata\x12T\n\x12operation_metadata\x18\x01 \x01(\x0b28.google.cloud.parallelstore.v1.TransferOperationMetadata\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x06 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x08 \x01(\tB\x03\xe0A\x03"\x14\n\x12ExportDataResponse"\xd7\x02\n\x12ExportDataMetadata\x12T\n\x12operation_metadata\x18\x01 \x01(\x0b28.google.cloud.parallelstore.v1.TransferOperationMetadata\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x06 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x08 \x01(\tB\x03\xe0A\x03"\xaf\x04\n\x19TransferOperationMetadata\x12W\n\x14source_parallelstore\x18\x07 \x01(\x0b22.google.cloud.parallelstore.v1.SourceParallelstoreB\x03\xe0A\x03H\x00\x12P\n\x11source_gcs_bucket\x18\x08 \x01(\x0b2..google.cloud.parallelstore.v1.SourceGcsBucketB\x03\xe0A\x03H\x00\x12Z\n\x16destination_gcs_bucket\x18\t \x01(\x0b23.google.cloud.parallelstore.v1.DestinationGcsBucketB\x03\xe0A\x03H\x01\x12a\n\x19destination_parallelstore\x18\n \x01(\x0b27.google.cloud.parallelstore.v1.DestinationParallelstoreB\x03\xe0A\x03H\x01\x12F\n\x08counters\x18\x03 \x01(\x0b2/.google.cloud.parallelstore.v1.TransferCountersB\x03\xe0A\x03\x12G\n\rtransfer_type\x18\x06 \x01(\x0e2+.google.cloud.parallelstore.v1.TransferTypeB\x03\xe0A\x03B\x08\n\x06sourceB\r\n\x0bdestination"\x9c\x01\n\x10TransferCounters\x12\x15\n\robjects_found\x18\x01 \x01(\x03\x12\x13\n\x0bbytes_found\x18\x02 \x01(\x03\x12\x17\n\x0fobjects_skipped\x18\x03 \x01(\x03\x12\x15\n\rbytes_skipped\x18\x04 \x01(\x03\x12\x16\n\x0eobjects_copied\x18\x05 \x01(\x03\x12\x14\n\x0cbytes_copied\x18\x06 \x01(\x03*E\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06IMPORT\x10\x01\x12\n\n\x06EXPORT\x10\x02*\x8a\x01\n\x0fFileStripeLevel\x12!\n\x1dFILE_STRIPE_LEVEL_UNSPECIFIED\x10\x00\x12\x19\n\x15FILE_STRIPE_LEVEL_MIN\x10\x01\x12\x1e\n\x1aFILE_STRIPE_LEVEL_BALANCED\x10\x02\x12\x19\n\x15FILE_STRIPE_LEVEL_MAX\x10\x03*\xa3\x01\n\x14DirectoryStripeLevel\x12&\n"DIRECTORY_STRIPE_LEVEL_UNSPECIFIED\x10\x00\x12\x1e\n\x1aDIRECTORY_STRIPE_LEVEL_MIN\x10\x01\x12#\n\x1fDIRECTORY_STRIPE_LEVEL_BALANCED\x10\x02\x12\x1e\n\x1aDIRECTORY_STRIPE_LEVEL_MAX\x10\x032\x8b\x0c\n\rParallelstore\x12\xba\x01\n\rListInstances\x123.google.cloud.parallelstore.v1.ListInstancesRequest\x1a4.google.cloud.parallelstore.v1.ListInstancesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\xa7\x01\n\x0bGetInstance\x121.google.cloud.parallelstore.v1.GetInstanceRequest\x1a\'.google.cloud.parallelstore.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\xe4\x01\n\x0eCreateInstance\x124.google.cloud.parallelstore.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xe6\x01\n\x0eUpdateInstance\x124.google.cloud.parallelstore.v1.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\xd0\x01\n\x0eDeleteInstance\x124.google.cloud.parallelstore.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x12\xcd\x01\n\nImportData\x120.google.cloud.parallelstore.v1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"n\xcaA(\n\x12ImportDataResponse\x12\x12ImportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:importData:\x01*\x12\xcd\x01\n\nExportData\x120.google.cloud.parallelstore.v1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"n\xcaA(\n\x12ExportDataResponse\x12\x12ExportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:exportData:\x01*\x1aP\xcaA\x1cparallelstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xee\x03\n!com.google.cloud.parallelstore.v1B\x12ParallelstoreProtoP\x01ZGcloud.google.com/go/parallelstore/apiv1/parallelstorepb;parallelstorepb\xaa\x02\x1dGoogle.Cloud.Parallelstore.V1\xca\x02\x1dGoogle\\Cloud\\Parallelstore\\V1\xea\x02 Google::Cloud::Parallelstore::V1\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n\x1ecompute.googleapis.com/Address\x127projects/{project}/regions/{region}/addresses/{address}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.parallelstore.v1.parallelstore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.parallelstore.v1B\x12ParallelstoreProtoP\x01ZGcloud.google.com/go/parallelstore/apiv1/parallelstorepb;parallelstorepb\xaa\x02\x1dGoogle.Cloud.Parallelstore.V1\xca\x02\x1dGoogle\\Cloud\\Parallelstore\\V1\xea\x02 Google::Cloud::Parallelstore::V1\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n\x1ecompute.googleapis.com/Address\x127projects/{project}/regions/{region}/addresses/{address}\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INSTANCE'].fields_by_name['description']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['capacity_gib']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['capacity_gib']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['daos_version']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['daos_version']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['access_points']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['access_points']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['network']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['network']._serialized_options = b'\xe0A\x05\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_INSTANCE'].fields_by_name['reserved_ip_range']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['reserved_ip_range']._serialized_options = b'\xe0A\x05\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Address'
    _globals['_INSTANCE'].fields_by_name['effective_reserved_ip_range']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['effective_reserved_ip_range']._serialized_options = b'\xe0A\x05\xe0A\x03\xfaA \n\x1ecompute.googleapis.com/Address'
    _globals['_INSTANCE'].fields_by_name['file_stripe_level']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['file_stripe_level']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['directory_stripe_level']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['directory_stripe_level']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAz\n%parallelstore.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%parallelstore.googleapis.com/Instance"
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%parallelstore.googleapis.com/Instance"
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%parallelstore.googleapis.com/Instance"
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%parallelstore.googleapis.com/Instance"
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_SOURCEGCSBUCKET'].fields_by_name['uri']._loaded_options = None
    _globals['_SOURCEGCSBUCKET'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_DESTINATIONGCSBUCKET'].fields_by_name['uri']._loaded_options = None
    _globals['_DESTINATIONGCSBUCKET'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_SOURCEPARALLELSTORE'].fields_by_name['path']._loaded_options = None
    _globals['_SOURCEPARALLELSTORE'].fields_by_name['path']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATIONPARALLELSTORE'].fields_by_name['path']._loaded_options = None
    _globals['_DESTINATIONPARALLELSTORE'].fields_by_name['path']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%parallelstore.googleapis.com/Instance"
    _globals['_IMPORTDATAREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%parallelstore.googleapis.com/Instance"
    _globals['_EXPORTDATAREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_parallelstore']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_parallelstore']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_gcs_bucket']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_gcs_bucket']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_gcs_bucket']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_gcs_bucket']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_parallelstore']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_parallelstore']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['counters']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['counters']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['transfer_type']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['transfer_type']._serialized_options = b'\xe0A\x03'
    _globals['_PARALLELSTORE']._loaded_options = None
    _globals['_PARALLELSTORE']._serialized_options = b'\xcaA\x1cparallelstore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PARALLELSTORE'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances'
    _globals['_PARALLELSTORE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_PARALLELSTORE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_PARALLELSTORE'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance'
    _globals['_PARALLELSTORE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_PARALLELSTORE'].methods_by_name['ImportData']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['ImportData']._serialized_options = b'\xcaA(\n\x12ImportDataResponse\x12\x12ImportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:importData:\x01*'
    _globals['_PARALLELSTORE'].methods_by_name['ExportData']._loaded_options = None
    _globals['_PARALLELSTORE'].methods_by_name['ExportData']._serialized_options = b'\xcaA(\n\x12ExportDataResponse\x12\x12ExportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:exportData:\x01*'
    _globals['_TRANSFERTYPE']._serialized_start = 4930
    _globals['_TRANSFERTYPE']._serialized_end = 4999
    _globals['_FILESTRIPELEVEL']._serialized_start = 5002
    _globals['_FILESTRIPELEVEL']._serialized_end = 5140
    _globals['_DIRECTORYSTRIPELEVEL']._serialized_start = 5143
    _globals['_DIRECTORYSTRIPELEVEL']._serialized_end = 5306
    _globals['_INSTANCE']._serialized_start = 362
    _globals['_INSTANCE']._serialized_end = 1404
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 1133
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 1178
    _globals['_INSTANCE_STATE']._serialized_start = 1180
    _globals['_INSTANCE_STATE']._serialized_end = 1277
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1407
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1585
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1588
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1717
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1719
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1800
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 1803
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 2004
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 2007
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 2173
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 2175
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 2284
    _globals['_OPERATIONMETADATA']._serialized_start = 2287
    _globals['_OPERATIONMETADATA']._serialized_end = 2543
    _globals['_SOURCEGCSBUCKET']._serialized_start = 2545
    _globals['_SOURCEGCSBUCKET']._serialized_end = 2580
    _globals['_DESTINATIONGCSBUCKET']._serialized_start = 2582
    _globals['_DESTINATIONGCSBUCKET']._serialized_end = 2622
    _globals['_SOURCEPARALLELSTORE']._serialized_start = 2624
    _globals['_SOURCEPARALLELSTORE']._serialized_end = 2664
    _globals['_DESTINATIONPARALLELSTORE']._serialized_start = 2666
    _globals['_DESTINATIONPARALLELSTORE']._serialized_end = 2711
    _globals['_IMPORTDATAREQUEST']._serialized_start = 2714
    _globals['_IMPORTDATAREQUEST']._serialized_end = 3091
    _globals['_EXPORTDATAREQUEST']._serialized_start = 3094
    _globals['_EXPORTDATAREQUEST']._serialized_end = 3471
    _globals['_IMPORTDATARESPONSE']._serialized_start = 3473
    _globals['_IMPORTDATARESPONSE']._serialized_end = 3493
    _globals['_IMPORTDATAMETADATA']._serialized_start = 3496
    _globals['_IMPORTDATAMETADATA']._serialized_end = 3839
    _globals['_EXPORTDATARESPONSE']._serialized_start = 3841
    _globals['_EXPORTDATARESPONSE']._serialized_end = 3861
    _globals['_EXPORTDATAMETADATA']._serialized_start = 3864
    _globals['_EXPORTDATAMETADATA']._serialized_end = 4207
    _globals['_TRANSFEROPERATIONMETADATA']._serialized_start = 4210
    _globals['_TRANSFEROPERATIONMETADATA']._serialized_end = 4769
    _globals['_TRANSFERCOUNTERS']._serialized_start = 4772
    _globals['_TRANSFERCOUNTERS']._serialized_end = 4928
    _globals['_PARALLELSTORE']._serialized_start = 5309
    _globals['_PARALLELSTORE']._serialized_end = 6856