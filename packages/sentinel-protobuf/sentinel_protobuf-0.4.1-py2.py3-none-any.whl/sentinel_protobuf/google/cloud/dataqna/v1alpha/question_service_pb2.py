"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataqna/v1alpha/question_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataqna.v1alpha import question_pb2 as google_dot_cloud_dot_dataqna_dot_v1alpha_dot_question__pb2
from .....google.cloud.dataqna.v1alpha import user_feedback_pb2 as google_dot_cloud_dot_dataqna_dot_v1alpha_dot_user__feedback__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dataqna/v1alpha/question_service.proto\x12\x1cgoogle.cloud.dataqna.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/dataqna/v1alpha/question.proto\x1a0google/cloud/dataqna/v1alpha/user_feedback.proto\x1a google/protobuf/field_mask.proto"z\n\x12GetQuestionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdataqna.googleapis.com/Question\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x91\x01\n\x15CreateQuestionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12=\n\x08question\x18\x02 \x01(\x0b2&.google.cloud.dataqna.v1alpha.QuestionB\x03\xe0A\x02"N\n\x16ExecuteQuestionRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14interpretation_index\x18\x02 \x01(\x05B\x03\xe0A\x02"S\n\x16GetUserFeedbackRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dataqna.googleapis.com/UserFeedback"\x94\x01\n\x19UpdateUserFeedbackRequest\x12F\n\ruser_feedback\x18\x01 \x01(\x0b2*.google.cloud.dataqna.v1alpha.UserFeedbackB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xec\x08\n\x0fQuestionService\x12\xaa\x01\n\x0bGetQuestion\x120.google.cloud.dataqna.v1alpha.GetQuestionRequest\x1a&.google.cloud.dataqna.v1alpha.Question"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha/{name=projects/*/locations/*/questions/*}\x12\xc5\x01\n\x0eCreateQuestion\x123.google.cloud.dataqna.v1alpha.CreateQuestionRequest\x1a&.google.cloud.dataqna.v1alpha.Question"V\xdaA\x0fparent,question\x82\xd3\xe4\x93\x02>"2/v1alpha/{parent=projects/*/locations/*}/questions:\x08question\x12\xd2\x01\n\x0fExecuteQuestion\x124.google.cloud.dataqna.v1alpha.ExecuteQuestionRequest\x1a&.google.cloud.dataqna.v1alpha.Question"a\xdaA\x19name,interpretation_index\x82\xd3\xe4\x93\x02?":/v1alpha/{name=projects/*/locations/*/questions/*}:execute:\x01*\x12\xc3\x01\n\x0fGetUserFeedback\x124.google.cloud.dataqna.v1alpha.GetUserFeedbackRequest\x1a*.google.cloud.dataqna.v1alpha.UserFeedback"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1alpha/{name=projects/*/locations/*/questions/*/userFeedback}\x12\xfc\x01\n\x12UpdateUserFeedback\x127.google.cloud.dataqna.v1alpha.UpdateUserFeedbackRequest\x1a*.google.cloud.dataqna.v1alpha.UserFeedback"\x80\x01\xdaA\x19user_feedback,update_mask\x82\xd3\xe4\x93\x02^2M/v1alpha/{user_feedback.name=projects/*/locations/*/questions/*/userFeedback}:\ruser_feedback\x1aJ\xcaA\x16dataqna.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd6\x01\n com.google.cloud.dataqna.v1alphaB\x14QuestionServiceProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataqna.v1alpha.question_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.dataqna.v1alphaB\x14QuestionServiceProtoP\x01Z:cloud.google.com/go/dataqna/apiv1alpha/dataqnapb;dataqnapb\xaa\x02\x1cGoogle.Cloud.DataQnA.V1Alpha\xca\x02\x1cGoogle\\Cloud\\DataQnA\\V1alpha\xea\x02\x1fGoogle::Cloud::DataQnA::V1alpha'
    _globals['_GETQUESTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUESTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdataqna.googleapis.com/Question'
    _globals['_CREATEQUESTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEQUESTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEQUESTIONREQUEST'].fields_by_name['question']._loaded_options = None
    _globals['_CREATEQUESTIONREQUEST'].fields_by_name['question']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEQUESTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXECUTEQUESTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEQUESTIONREQUEST'].fields_by_name['interpretation_index']._loaded_options = None
    _globals['_EXECUTEQUESTIONREQUEST'].fields_by_name['interpretation_index']._serialized_options = b'\xe0A\x02'
    _globals['_GETUSERFEEDBACKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETUSERFEEDBACKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#dataqna.googleapis.com/UserFeedback'
    _globals['_UPDATEUSERFEEDBACKREQUEST'].fields_by_name['user_feedback']._loaded_options = None
    _globals['_UPDATEUSERFEEDBACKREQUEST'].fields_by_name['user_feedback']._serialized_options = b'\xe0A\x02'
    _globals['_QUESTIONSERVICE']._loaded_options = None
    _globals['_QUESTIONSERVICE']._serialized_options = b'\xcaA\x16dataqna.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_QUESTIONSERVICE'].methods_by_name['GetQuestion']._loaded_options = None
    _globals['_QUESTIONSERVICE'].methods_by_name['GetQuestion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1alpha/{name=projects/*/locations/*/questions/*}'
    _globals['_QUESTIONSERVICE'].methods_by_name['CreateQuestion']._loaded_options = None
    _globals['_QUESTIONSERVICE'].methods_by_name['CreateQuestion']._serialized_options = b'\xdaA\x0fparent,question\x82\xd3\xe4\x93\x02>"2/v1alpha/{parent=projects/*/locations/*}/questions:\x08question'
    _globals['_QUESTIONSERVICE'].methods_by_name['ExecuteQuestion']._loaded_options = None
    _globals['_QUESTIONSERVICE'].methods_by_name['ExecuteQuestion']._serialized_options = b'\xdaA\x19name,interpretation_index\x82\xd3\xe4\x93\x02?":/v1alpha/{name=projects/*/locations/*/questions/*}:execute:\x01*'
    _globals['_QUESTIONSERVICE'].methods_by_name['GetUserFeedback']._loaded_options = None
    _globals['_QUESTIONSERVICE'].methods_by_name['GetUserFeedback']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1alpha/{name=projects/*/locations/*/questions/*/userFeedback}'
    _globals['_QUESTIONSERVICE'].methods_by_name['UpdateUserFeedback']._loaded_options = None
    _globals['_QUESTIONSERVICE'].methods_by_name['UpdateUserFeedback']._serialized_options = b'\xdaA\x19user_feedback,update_mask\x82\xd3\xe4\x93\x02^2M/v1alpha/{user_feedback.name=projects/*/locations/*/questions/*/userFeedback}:\ruser_feedback'
    _globals['_GETQUESTIONREQUEST']._serialized_start = 329
    _globals['_GETQUESTIONREQUEST']._serialized_end = 451
    _globals['_CREATEQUESTIONREQUEST']._serialized_start = 454
    _globals['_CREATEQUESTIONREQUEST']._serialized_end = 599
    _globals['_EXECUTEQUESTIONREQUEST']._serialized_start = 601
    _globals['_EXECUTEQUESTIONREQUEST']._serialized_end = 679
    _globals['_GETUSERFEEDBACKREQUEST']._serialized_start = 681
    _globals['_GETUSERFEEDBACKREQUEST']._serialized_end = 764
    _globals['_UPDATEUSERFEEDBACKREQUEST']._serialized_start = 767
    _globals['_UPDATEUSERFEEDBACKREQUEST']._serialized_end = 915
    _globals['_QUESTIONSERVICE']._serialized_start = 918
    _globals['_QUESTIONSERVICE']._serialized_end = 2050