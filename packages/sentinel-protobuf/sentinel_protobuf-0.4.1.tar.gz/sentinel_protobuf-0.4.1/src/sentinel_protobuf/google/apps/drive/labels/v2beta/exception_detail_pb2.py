"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/drive/labels/v2beta/exception_detail.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/apps/drive/labels/v2beta/exception_detail.proto\x12\x1fgoogle.apps.drive.labels.v2beta"U\n\x0fExceptionDetail\x12B\n\nerror_type\x18\x01 \x01(\x0e2..google.apps.drive.labels.v2beta.ExceptionType*\xe1\x06\n\rExceptionType\x12\x1e\n\x1aEXCEPTION_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eFIELD_REQUIRED\x10\x01\x12\x1c\n\x18METAMODEL_ALREADY_EXISTS\x10\x02\x12\x17\n\x13METAMODEL_NOT_FOUND\x10\x03\x12&\n"ILLEGAL_METAMODEL_STATE_TRANSITION\x10\x04\x12(\n$INVALID_METAMODEL_DEPRECATION_POLICY\x10\x05\x12#\n\x1fMETAMODEL_DELETION_DENIED_UNTIL\x10\x06\x12\x11\n\rINVALID_FIELD\x10\x07\x12!\n\x1dMETAMODEL_PRECONDITION_FAILED\x10\x08\x12\x17\n\x13DUPLICATE_FIELD_KEY\x10\t\x12\x19\n\x15ILLEGAL_FIELD_REMOVAL\x10\n\x12#\n\x1fILLEGAL_FIELD_OPTIONS_FOR_FIELD\x10\x0b\x12-\n)UNSUPPORTED_CHANGE_TO_PUBLISHED_METAMODEL\x10\x0c\x120\n,ILLEGAL_METAMODEL_STATE_TRANSITION_IN_UPDATE\x10\r\x12\x16\n\x12PAGE_TOKEN_EXPIRED\x10\x0e\x12\x12\n\x0eNOT_AUTHORIZED\x10\x0f\x12"\n\x1eILLEGAL_FIELD_STATE_TRANSITION\x10\x10\x12.\n*ILLEGAL_CHOICE_SET_OPTION_STATE_TRANSITION\x10\x11\x12\x1e\n\x1aINVALID_CHOICE_SET_OPTIONS\x10\x12\x12\x15\n\x11INVALID_FIELD_KEY\x10\x13\x12 \n\x1cINVALID_FIELD_PROPERTY_RANGE\x10\x14\x12\x1c\n\x18INVALID_LOCALIZED_STRING\x10\x15\x12%\n!ILLEGAL_CHANGE_TO_PUBLISHED_FIELD\x10\x16\x12&\n"INVALID_FIELD_UPDATE_NOT_INCLUSIVE\x10\x17\x12\x1c\n\x18INVALID_CHOICE_SET_STATE\x10\x18\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\xf4\x03B\x84\x01\n#com.google.apps.drive.labels.v2betaB\x14ExceptionDetailProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labelsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.exception_detail_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\x14ExceptionDetailProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels'
    _globals['_EXCEPTIONTYPE']._serialized_start = 179
    _globals['_EXCEPTIONTYPE']._serialized_end = 1044
    _globals['_EXCEPTIONDETAIL']._serialized_start = 91
    _globals['_EXCEPTIONDETAIL']._serialized_end = 176