"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1beta1/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.notebooks.v1beta1 import environment_pb2 as google_dot_cloud_dot_notebooks_dot_v1beta1_dot_environment__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/notebooks/v1beta1/instance.proto\x12\x1egoogle.cloud.notebooks.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/notebooks/v1beta1/environment.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfe\x01\n\x13ReservationAffinity\x12_\n\x18consume_reservation_type\x18\x01 \x01(\x0e28.google.cloud.notebooks.v1beta1.ReservationAffinity.TypeB\x03\xe0A\x01\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06values\x18\x03 \x03(\tB\x03\xe0A\x01"_\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eNO_RESERVATION\x10\x01\x12\x13\n\x0fANY_RESERVATION\x10\x02\x12\x18\n\x14SPECIFIC_RESERVATION\x10\x03"\xd9\x12\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12;\n\x08vm_image\x18\x02 \x01(\x0b2\'.google.cloud.notebooks.v1beta1.VmImageH\x00\x12I\n\x0fcontainer_image\x18\x03 \x01(\x0b2..google.cloud.notebooks.v1beta1.ContainerImageH\x00\x12\x1b\n\x13post_startup_script\x18\x04 \x01(\t\x12\x16\n\tproxy_uri\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0finstance_owners\x18\x06 \x03(\tB\x03\xe0A\x04\x12\x17\n\x0fservice_account\x18\x07 \x01(\t\x12\x19\n\x0cmachine_type\x18\x08 \x01(\tB\x03\xe0A\x02\x12V\n\x12accelerator_config\x18\t \x01(\x0b2:.google.cloud.notebooks.v1beta1.Instance.AcceleratorConfig\x12B\n\x05state\x18\n \x01(\x0e2..google.cloud.notebooks.v1beta1.Instance.StateB\x03\xe0A\x03\x12\x1a\n\x12install_gpu_driver\x18\x0b \x01(\x08\x12\x1e\n\x16custom_gpu_driver_path\x18\x0c \x01(\t\x12N\n\x0eboot_disk_type\x18\r \x01(\x0e21.google.cloud.notebooks.v1beta1.Instance.DiskTypeB\x03\xe0A\x04\x12\x1e\n\x11boot_disk_size_gb\x18\x0e \x01(\x03B\x03\xe0A\x04\x12N\n\x0edata_disk_type\x18\x19 \x01(\x0e21.google.cloud.notebooks.v1beta1.Instance.DiskTypeB\x03\xe0A\x04\x12\x1e\n\x11data_disk_size_gb\x18\x1a \x01(\x03B\x03\xe0A\x04\x12 \n\x13no_remove_data_disk\x18\x1b \x01(\x08B\x03\xe0A\x04\x12U\n\x0fdisk_encryption\x18\x0f \x01(\x0e27.google.cloud.notebooks.v1beta1.Instance.DiskEncryptionB\x03\xe0A\x04\x12\x14\n\x07kms_key\x18\x10 \x01(\tB\x03\xe0A\x04\x12\x14\n\x0cno_public_ip\x18\x11 \x01(\x08\x12\x17\n\x0fno_proxy_access\x18\x12 \x01(\x08\x12\x0f\n\x07network\x18\x13 \x01(\t\x12\x0e\n\x06subnet\x18\x14 \x01(\t\x12D\n\x06labels\x18\x15 \x03(\x0b24.google.cloud.notebooks.v1beta1.Instance.LabelsEntry\x12H\n\x08metadata\x18\x16 \x03(\x0b26.google.cloud.notebooks.v1beta1.Instance.MetadataEntry\x12G\n\x08nic_type\x18\x1c \x01(\x0e20.google.cloud.notebooks.v1beta1.Instance.NicTypeB\x03\xe0A\x01\x12V\n\x14reservation_affinity\x18\x1d \x01(\x0b23.google.cloud.notebooks.v1beta1.ReservationAffinityB\x03\xe0A\x01\x12\x1b\n\x0ecan_ip_forward\x18\x1f \x01(\x08B\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x17 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x18 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1ao\n\x11AcceleratorConfig\x12F\n\x04type\x18\x01 \x01(\x0e28.google.cloud.notebooks.v1beta1.Instance.AcceleratorType\x12\x12\n\ncore_count\x18\x02 \x01(\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x86\x02\n\x0fAcceleratorType\x12 \n\x1cACCELERATOR_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10NVIDIA_TESLA_K80\x10\x01\x12\x15\n\x11NVIDIA_TESLA_P100\x10\x02\x12\x15\n\x11NVIDIA_TESLA_V100\x10\x03\x12\x13\n\x0fNVIDIA_TESLA_P4\x10\x04\x12\x13\n\x0fNVIDIA_TESLA_T4\x10\x05\x12\x17\n\x13NVIDIA_TESLA_T4_VWS\x10\x08\x12\x19\n\x15NVIDIA_TESLA_P100_VWS\x10\t\x12\x17\n\x13NVIDIA_TESLA_P4_VWS\x10\n\x12\n\n\x06TPU_V2\x10\x06\x12\n\n\x06TPU_V3\x10\x07"\xc3\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0b\n\x07DELETED\x10\x06\x12\r\n\tUPGRADING\x10\x07\x12\x10\n\x0cINITIALIZING\x10\x08\x12\x0f\n\x0bREGISTERING\x10\t\x12\x0e\n\nSUSPENDING\x10\n\x12\r\n\tSUSPENDED\x10\x0b"S\n\x08DiskType\x12\x19\n\x15DISK_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPD_STANDARD\x10\x01\x12\n\n\x06PD_SSD\x10\x02\x12\x0f\n\x0bPD_BALANCED\x10\x03"E\n\x0eDiskEncryption\x12\x1f\n\x1bDISK_ENCRYPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04GMEK\x10\x01\x12\x08\n\x04CMEK\x10\x02">\n\x07NicType\x12\x18\n\x14UNSPECIFIED_NIC_TYPE\x10\x00\x12\x0e\n\nVIRTIO_NET\x10\x01\x12\t\n\x05GVNIC\x10\x02:O\xeaAL\n!notebooks.googleapis.com/Instance\x12\'projects/{project}/instances/{instance}B\r\n\x0benvironmentB\xdd\x01\n"com.google.cloud.notebooks.v1beta1B\rInstanceProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1beta1.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.notebooks.v1beta1B\rInstanceProtoP\x01Z@cloud.google.com/go/notebooks/apiv1beta1/notebookspb;notebookspb\xaa\x02\x1eGoogle.Cloud.Notebooks.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Notebooks\\V1beta1\xea\x02!Google::Cloud::Notebooks::V1beta1'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['consume_reservation_type']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['consume_reservation_type']._serialized_options = b'\xe0A\x01'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['key']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['key']._serialized_options = b'\xe0A\x01'
    _globals['_RESERVATIONAFFINITY'].fields_by_name['values']._loaded_options = None
    _globals['_RESERVATIONAFFINITY'].fields_by_name['values']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE_METADATAENTRY']._loaded_options = None
    _globals['_INSTANCE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['proxy_uri']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['proxy_uri']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['instance_owners']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['instance_owners']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['machine_type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['machine_type']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['boot_disk_type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['boot_disk_type']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['boot_disk_size_gb']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['boot_disk_size_gb']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['data_disk_type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['data_disk_type']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['data_disk_size_gb']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['data_disk_size_gb']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['no_remove_data_disk']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['no_remove_data_disk']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['disk_encryption']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['disk_encryption']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['kms_key']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x04'
    _globals['_INSTANCE'].fields_by_name['nic_type']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['nic_type']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['reservation_affinity']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['reservation_affinity']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['can_ip_forward']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['can_ip_forward']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b"\xeaAL\n!notebooks.googleapis.com/Instance\x12'projects/{project}/instances/{instance}"
    _globals['_RESERVATIONAFFINITY']._serialized_start = 225
    _globals['_RESERVATIONAFFINITY']._serialized_end = 479
    _globals['_RESERVATIONAFFINITY_TYPE']._serialized_start = 384
    _globals['_RESERVATIONAFFINITY_TYPE']._serialized_end = 479
    _globals['_INSTANCE']._serialized_start = 482
    _globals['_INSTANCE']._serialized_end = 2875
    _globals['_INSTANCE_ACCELERATORCONFIG']._serialized_start = 1889
    _globals['_INSTANCE_ACCELERATORCONFIG']._serialized_end = 2000
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 2002
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 2047
    _globals['_INSTANCE_METADATAENTRY']._serialized_start = 2049
    _globals['_INSTANCE_METADATAENTRY']._serialized_end = 2096
    _globals['_INSTANCE_ACCELERATORTYPE']._serialized_start = 2099
    _globals['_INSTANCE_ACCELERATORTYPE']._serialized_end = 2361
    _globals['_INSTANCE_STATE']._serialized_start = 2364
    _globals['_INSTANCE_STATE']._serialized_end = 2559
    _globals['_INSTANCE_DISKTYPE']._serialized_start = 2561
    _globals['_INSTANCE_DISKTYPE']._serialized_end = 2644
    _globals['_INSTANCE_DISKENCRYPTION']._serialized_start = 2646
    _globals['_INSTANCE_DISKENCRYPTION']._serialized_end = 2715
    _globals['_INSTANCE_NICTYPE']._serialized_start = 2717
    _globals['_INSTANCE_NICTYPE']._serialized_end = 2779