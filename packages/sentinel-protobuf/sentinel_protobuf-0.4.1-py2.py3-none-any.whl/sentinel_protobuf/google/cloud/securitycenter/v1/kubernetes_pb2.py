"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/kubernetes.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.securitycenter.v1 import container_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_container__pb2
from .....google.cloud.securitycenter.v1 import label_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_label__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/securitycenter/v1/kubernetes.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a.google/cloud/securitycenter/v1/container.proto\x1a*google/cloud/securitycenter/v1/label.proto"\x82\x0c\n\nKubernetes\x12<\n\x04pods\x18\x01 \x03(\x0b2..google.cloud.securitycenter.v1.Kubernetes.Pod\x12>\n\x05nodes\x18\x02 \x03(\x0b2/.google.cloud.securitycenter.v1.Kubernetes.Node\x12G\n\nnode_pools\x18\x03 \x03(\x0b23.google.cloud.securitycenter.v1.Kubernetes.NodePool\x12>\n\x05roles\x18\x04 \x03(\x0b2/.google.cloud.securitycenter.v1.Kubernetes.Role\x12D\n\x08bindings\x18\x05 \x03(\x0b22.google.cloud.securitycenter.v1.Kubernetes.Binding\x12O\n\x0eaccess_reviews\x18\x06 \x03(\x0b27.google.cloud.securitycenter.v1.Kubernetes.AccessReview\x12B\n\x07objects\x18\x07 \x03(\x0b21.google.cloud.securitycenter.v1.Kubernetes.Object\x1a\x95\x01\n\x03Pod\x12\n\n\x02ns\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x125\n\x06labels\x18\x03 \x03(\x0b2%.google.cloud.securitycenter.v1.Label\x12=\n\ncontainers\x18\x04 \x03(\x0b2).google.cloud.securitycenter.v1.Container\x1a\x14\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x1aX\n\x08NodePool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x05nodes\x18\x02 \x03(\x0b2/.google.cloud.securitycenter.v1.Kubernetes.Node\x1a\x9e\x01\n\x04Role\x12B\n\x04kind\x18\x01 \x01(\x0e24.google.cloud.securitycenter.v1.Kubernetes.Role.Kind\x12\n\n\x02ns\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t"8\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x08\n\x04ROLE\x10\x01\x12\x10\n\x0cCLUSTER_ROLE\x10\x02\x1a\xa8\x01\n\x07Binding\x12\n\n\x02ns\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12=\n\x04role\x18\x03 \x01(\x0b2/.google.cloud.securitycenter.v1.Kubernetes.Role\x12D\n\x08subjects\x18\x04 \x03(\x0b22.google.cloud.securitycenter.v1.Kubernetes.Subject\x1a\xbe\x01\n\x07Subject\x12I\n\x04kind\x18\x01 \x01(\x0e2;.google.cloud.securitycenter.v1.Kubernetes.Subject.AuthType\x12\n\n\x02ns\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t"N\n\x08AuthType\x12\x19\n\x15AUTH_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04USER\x10\x01\x12\x12\n\x0eSERVICEACCOUNT\x10\x02\x12\t\n\x05GROUP\x10\x03\x1a}\n\x0cAccessReview\x12\r\n\x05group\x18\x01 \x01(\t\x12\n\n\x02ns\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08resource\x18\x04 \x01(\t\x12\x13\n\x0bsubresource\x18\x05 \x01(\t\x12\x0c\n\x04verb\x18\x06 \x01(\t\x12\x0f\n\x07version\x18\x07 \x01(\t\x1a~\n\x06Object\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\n\n\x02ns\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12=\n\ncontainers\x18\x05 \x03(\x0b2).google.cloud.securitycenter.v1.ContainerB\xe9\x01\n"com.google.cloud.securitycenter.v1B\x0fKubernetesProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.kubernetes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0fKubernetesProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_KUBERNETES']._serialized_start = 176
    _globals['_KUBERNETES']._serialized_end = 1714
    _globals['_KUBERNETES_POD']._serialized_start = 673
    _globals['_KUBERNETES_POD']._serialized_end = 822
    _globals['_KUBERNETES_NODE']._serialized_start = 824
    _globals['_KUBERNETES_NODE']._serialized_end = 844
    _globals['_KUBERNETES_NODEPOOL']._serialized_start = 846
    _globals['_KUBERNETES_NODEPOOL']._serialized_end = 934
    _globals['_KUBERNETES_ROLE']._serialized_start = 937
    _globals['_KUBERNETES_ROLE']._serialized_end = 1095
    _globals['_KUBERNETES_ROLE_KIND']._serialized_start = 1039
    _globals['_KUBERNETES_ROLE_KIND']._serialized_end = 1095
    _globals['_KUBERNETES_BINDING']._serialized_start = 1098
    _globals['_KUBERNETES_BINDING']._serialized_end = 1266
    _globals['_KUBERNETES_SUBJECT']._serialized_start = 1269
    _globals['_KUBERNETES_SUBJECT']._serialized_end = 1459
    _globals['_KUBERNETES_SUBJECT_AUTHTYPE']._serialized_start = 1381
    _globals['_KUBERNETES_SUBJECT_AUTHTYPE']._serialized_end = 1459
    _globals['_KUBERNETES_ACCESSREVIEW']._serialized_start = 1461
    _globals['_KUBERNETES_ACCESSREVIEW']._serialized_end = 1586
    _globals['_KUBERNETES_OBJECT']._serialized_start = 1588
    _globals['_KUBERNETES_OBJECT']._serialized_end = 1714