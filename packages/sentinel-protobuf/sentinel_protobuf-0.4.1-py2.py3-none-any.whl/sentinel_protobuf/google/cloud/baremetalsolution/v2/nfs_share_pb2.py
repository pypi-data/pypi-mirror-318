"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/nfs_share.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/baremetalsolution/v2/nfs_share.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x9d\t\n\x08NfsShare\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cnfs_share_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x08 \x01(\tB\x03\xe0A\x03\x12E\n\x05state\x18\x03 \x01(\x0e21.google.cloud.baremetalsolution.v2.NfsShare.StateB\x03\xe0A\x03\x12?\n\x06volume\x18\x04 \x01(\tB/\xe0A\x03\xfaA)\n\'baremetalsolution.googleapis.com/Volume\x12R\n\x0fallowed_clients\x18\x05 \x03(\x0b29.google.cloud.baremetalsolution.v2.NfsShare.AllowedClient\x12G\n\x06labels\x18\x06 \x03(\x0b27.google.cloud.baremetalsolution.v2.NfsShare.LabelsEntry\x12\x1a\n\x12requested_size_gib\x18\x07 \x01(\x03\x12R\n\x0cstorage_type\x18\t \x01(\x0e27.google.cloud.baremetalsolution.v2.NfsShare.StorageTypeB\x03\xe0A\x05\x1a\xb3\x02\n\rAllowedClient\x12>\n\x07network\x18\x01 \x01(\tB-\xfaA*\n(baremetalsolution.googleapis.com/Network\x12\x15\n\x08share_ip\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x14allowed_clients_cidr\x18\x03 \x01(\t\x12W\n\x11mount_permissions\x18\x04 \x01(\x0e2<.google.cloud.baremetalsolution.v2.NfsShare.MountPermissions\x12\x11\n\tallow_dev\x18\x05 \x01(\x08\x12\x12\n\nallow_suid\x18\x06 \x01(\x08\x12\x16\n\x0eno_root_squash\x18\x07 \x01(\x08\x12\x15\n\x08nfs_path\x18\x08 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"Y\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPROVISIONED\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04"O\n\x10MountPermissions\x12!\n\x1dMOUNT_PERMISSIONS_UNSPECIFIED\x10\x00\x12\x08\n\x04READ\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02"=\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\x12\x07\n\x03HDD\x10\x02:m\xeaAj\n)baremetalsolution.googleapis.com/NFSShare\x12=projects/{project}/locations/{location}/nfsShares/{nfs_share}"U\n\x12GetNfsShareRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShare"\x88\x01\n\x14ListNfsSharesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x86\x01\n\x15ListNfsSharesResponse\x12?\n\nnfs_shares\x18\x01 \x03(\x0b2+.google.cloud.baremetalsolution.v2.NfsShare\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x8d\x01\n\x15UpdateNfsShareRequest\x12C\n\tnfs_share\x18\x01 \x01(\x0b2+.google.cloud.baremetalsolution.v2.NfsShareB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"v\n\x15RenameNfsShareRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShare\x12\x1c\n\x0fnew_nfsshare_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x97\x01\n\x15CreateNfsShareRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\tnfs_share\x18\x02 \x01(\x0b2+.google.cloud.baremetalsolution.v2.NfsShareB\x03\xe0A\x02"X\n\x15DeleteNfsShareRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShareB\xfc\x01\n%com.google.cloud.baremetalsolution.v2B\rNfsShareProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.nfs_share_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\rNfsShareProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['network']._loaded_options = None
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['network']._serialized_options = b'\xfaA*\n(baremetalsolution.googleapis.com/Network'
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['share_ip']._loaded_options = None
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['share_ip']._serialized_options = b'\xe0A\x03'
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['nfs_path']._loaded_options = None
    _globals['_NFSSHARE_ALLOWEDCLIENT'].fields_by_name['nfs_path']._serialized_options = b'\xe0A\x03'
    _globals['_NFSSHARE_LABELSENTRY']._loaded_options = None
    _globals['_NFSSHARE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NFSSHARE'].fields_by_name['name']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_NFSSHARE'].fields_by_name['nfs_share_id']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['nfs_share_id']._serialized_options = b'\xe0A\x03'
    _globals['_NFSSHARE'].fields_by_name['id']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_NFSSHARE'].fields_by_name['state']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_NFSSHARE'].fields_by_name['volume']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['volume']._serialized_options = b"\xe0A\x03\xfaA)\n'baremetalsolution.googleapis.com/Volume"
    _globals['_NFSSHARE'].fields_by_name['storage_type']._loaded_options = None
    _globals['_NFSSHARE'].fields_by_name['storage_type']._serialized_options = b'\xe0A\x05'
    _globals['_NFSSHARE']._loaded_options = None
    _globals['_NFSSHARE']._serialized_options = b'\xeaAj\n)baremetalsolution.googleapis.com/NFSShare\x12=projects/{project}/locations/{location}/nfsShares/{nfs_share}'
    _globals['_GETNFSSHAREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNFSSHAREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShare'
    _globals['_LISTNFSSHARESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNFSSHARESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATENFSSHAREREQUEST'].fields_by_name['nfs_share']._loaded_options = None
    _globals['_UPDATENFSSHAREREQUEST'].fields_by_name['nfs_share']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMENFSSHAREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMENFSSHAREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShare'
    _globals['_RENAMENFSSHAREREQUEST'].fields_by_name['new_nfsshare_id']._loaded_options = None
    _globals['_RENAMENFSSHAREREQUEST'].fields_by_name['new_nfsshare_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENFSSHAREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENFSSHAREREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATENFSSHAREREQUEST'].fields_by_name['nfs_share']._loaded_options = None
    _globals['_CREATENFSSHAREREQUEST'].fields_by_name['nfs_share']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENFSSHAREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENFSSHAREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)baremetalsolution.googleapis.com/NFSShare'
    _globals['_NFSSHARE']._serialized_start = 183
    _globals['_NFSSHARE']._serialized_end = 1364
    _globals['_NFSSHARE_ALLOWEDCLIENT']._serialized_start = 664
    _globals['_NFSSHARE_ALLOWEDCLIENT']._serialized_end = 971
    _globals['_NFSSHARE_LABELSENTRY']._serialized_start = 973
    _globals['_NFSSHARE_LABELSENTRY']._serialized_end = 1018
    _globals['_NFSSHARE_STATE']._serialized_start = 1020
    _globals['_NFSSHARE_STATE']._serialized_end = 1109
    _globals['_NFSSHARE_MOUNTPERMISSIONS']._serialized_start = 1111
    _globals['_NFSSHARE_MOUNTPERMISSIONS']._serialized_end = 1190
    _globals['_NFSSHARE_STORAGETYPE']._serialized_start = 1192
    _globals['_NFSSHARE_STORAGETYPE']._serialized_end = 1253
    _globals['_GETNFSSHAREREQUEST']._serialized_start = 1366
    _globals['_GETNFSSHAREREQUEST']._serialized_end = 1451
    _globals['_LISTNFSSHARESREQUEST']._serialized_start = 1454
    _globals['_LISTNFSSHARESREQUEST']._serialized_end = 1590
    _globals['_LISTNFSSHARESRESPONSE']._serialized_start = 1593
    _globals['_LISTNFSSHARESRESPONSE']._serialized_end = 1727
    _globals['_UPDATENFSSHAREREQUEST']._serialized_start = 1730
    _globals['_UPDATENFSSHAREREQUEST']._serialized_end = 1871
    _globals['_RENAMENFSSHAREREQUEST']._serialized_start = 1873
    _globals['_RENAMENFSSHAREREQUEST']._serialized_end = 1991
    _globals['_CREATENFSSHAREREQUEST']._serialized_start = 1994
    _globals['_CREATENFSSHAREREQUEST']._serialized_end = 2145
    _globals['_DELETENFSSHAREREQUEST']._serialized_start = 2147
    _globals['_DELETENFSSHAREREQUEST']._serialized_end = 2235