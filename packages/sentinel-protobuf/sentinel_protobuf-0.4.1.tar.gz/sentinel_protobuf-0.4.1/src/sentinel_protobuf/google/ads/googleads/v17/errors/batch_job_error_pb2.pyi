from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BatchJobErrorEnum(_message.Message):
    __slots__ = ()

    class BatchJobError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BatchJobErrorEnum.BatchJobError]
        UNKNOWN: _ClassVar[BatchJobErrorEnum.BatchJobError]
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING: _ClassVar[BatchJobErrorEnum.BatchJobError]
        EMPTY_OPERATIONS: _ClassVar[BatchJobErrorEnum.BatchJobError]
        INVALID_SEQUENCE_TOKEN: _ClassVar[BatchJobErrorEnum.BatchJobError]
        RESULTS_NOT_READY: _ClassVar[BatchJobErrorEnum.BatchJobError]
        INVALID_PAGE_SIZE: _ClassVar[BatchJobErrorEnum.BatchJobError]
        CAN_ONLY_REMOVE_PENDING_JOB: _ClassVar[BatchJobErrorEnum.BatchJobError]
        CANNOT_LIST_RESULTS: _ClassVar[BatchJobErrorEnum.BatchJobError]
        ASSET_GROUP_AND_ASSET_GROUP_ASSET_TRANSACTION_FAILURE: _ClassVar[BatchJobErrorEnum.BatchJobError]
        ASSET_GROUP_LISTING_GROUP_FILTER_TRANSACTION_FAILURE: _ClassVar[BatchJobErrorEnum.BatchJobError]
        REQUEST_TOO_LARGE: _ClassVar[BatchJobErrorEnum.BatchJobError]
    UNSPECIFIED: BatchJobErrorEnum.BatchJobError
    UNKNOWN: BatchJobErrorEnum.BatchJobError
    CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING: BatchJobErrorEnum.BatchJobError
    EMPTY_OPERATIONS: BatchJobErrorEnum.BatchJobError
    INVALID_SEQUENCE_TOKEN: BatchJobErrorEnum.BatchJobError
    RESULTS_NOT_READY: BatchJobErrorEnum.BatchJobError
    INVALID_PAGE_SIZE: BatchJobErrorEnum.BatchJobError
    CAN_ONLY_REMOVE_PENDING_JOB: BatchJobErrorEnum.BatchJobError
    CANNOT_LIST_RESULTS: BatchJobErrorEnum.BatchJobError
    ASSET_GROUP_AND_ASSET_GROUP_ASSET_TRANSACTION_FAILURE: BatchJobErrorEnum.BatchJobError
    ASSET_GROUP_LISTING_GROUP_FILTER_TRANSACTION_FAILURE: BatchJobErrorEnum.BatchJobError
    REQUEST_TOO_LARGE: BatchJobErrorEnum.BatchJobError

    def __init__(self) -> None:
        ...