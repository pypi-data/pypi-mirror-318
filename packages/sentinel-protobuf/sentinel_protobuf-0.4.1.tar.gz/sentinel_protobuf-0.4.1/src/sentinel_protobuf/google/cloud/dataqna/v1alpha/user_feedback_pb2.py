"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataqna/v1alpha/user_feedback.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dataqna/v1alpha/user_feedback.proto\x12\x1cgoogle.cloud.dataqna.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd9\x02\n\x0cUserFeedback\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\x12free_form_feedback\x18\x02 \x01(\t\x12M\n\x06rating\x18\x03 \x01(\x0e2=.google.cloud.dataqna.v1alpha.UserFeedback.UserFeedbackRating"V\n\x12UserFeedbackRating\x12$\n USER_FEEDBACK_RATING_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSITIVE\x10\x01\x12\x0c\n\x08NEGATIVE\x10\x02:s\xeaAp\n#dataqna.googleapis.com/UserFeedback\x12Iprojects/{project}/locations/{location}/questions/{question}/userFeedbackB\xd3\x01\n com.google.cloud.dataqna.v1alphaB\x11UserFeedbackProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataqna.v1alpha.user_feedback_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.dataqna.v1alphaB\x11UserFeedbackProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alpha'
    _globals['_USERFEEDBACK'].fields_by_name['name']._loaded_options = None
    _globals['_USERFEEDBACK'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_USERFEEDBACK']._loaded_options = None
    _globals['_USERFEEDBACK']._serialized_options = b'\xeaAp\n#dataqna.googleapis.com/UserFeedback\x12Iprojects/{project}/locations/{location}/questions/{question}/userFeedback'
    _globals['_USERFEEDBACK']._serialized_start = 143
    _globals['_USERFEEDBACK']._serialized_end = 488
    _globals['_USERFEEDBACK_USERFEEDBACKRATING']._serialized_start = 285
    _globals['_USERFEEDBACK_USERFEEDBACKRATING']._serialized_end = 371