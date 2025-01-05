from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.streetview.publish.v1 import resources_pb2 as _resources_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASIC: _ClassVar[PhotoView]
    INCLUDE_DOWNLOAD_URL: _ClassVar[PhotoView]
BASIC: PhotoView
INCLUDE_DOWNLOAD_URL: PhotoView

class CreatePhotoRequest(_message.Message):
    __slots__ = ("photo",)
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    photo: _resources_pb2.Photo
    def __init__(self, photo: _Optional[_Union[_resources_pb2.Photo, _Mapping]] = ...) -> None: ...

class GetPhotoRequest(_message.Message):
    __slots__ = ("photo_id", "view", "language_code")
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    photo_id: str
    view: PhotoView
    language_code: str
    def __init__(self, photo_id: _Optional[str] = ..., view: _Optional[_Union[PhotoView, str]] = ..., language_code: _Optional[str] = ...) -> None: ...

class BatchGetPhotosRequest(_message.Message):
    __slots__ = ("photo_ids", "view", "language_code")
    PHOTO_IDS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    photo_ids: _containers.RepeatedScalarFieldContainer[str]
    view: PhotoView
    language_code: str
    def __init__(self, photo_ids: _Optional[_Iterable[str]] = ..., view: _Optional[_Union[PhotoView, str]] = ..., language_code: _Optional[str] = ...) -> None: ...

class BatchGetPhotosResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PhotoResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[PhotoResponse, _Mapping]]] = ...) -> None: ...

class PhotoResponse(_message.Message):
    __slots__ = ("status", "photo")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    photo: _resources_pb2.Photo
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., photo: _Optional[_Union[_resources_pb2.Photo, _Mapping]] = ...) -> None: ...

class ListPhotosRequest(_message.Message):
    __slots__ = ("view", "page_size", "page_token", "filter", "language_code")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    view: PhotoView
    page_size: int
    page_token: str
    filter: str
    language_code: str
    def __init__(self, view: _Optional[_Union[PhotoView, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class ListPhotosResponse(_message.Message):
    __slots__ = ("photos", "next_page_token")
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    photos: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Photo]
    next_page_token: str
    def __init__(self, photos: _Optional[_Iterable[_Union[_resources_pb2.Photo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePhotoRequest(_message.Message):
    __slots__ = ("photo", "update_mask")
    PHOTO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    photo: _resources_pb2.Photo
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, photo: _Optional[_Union[_resources_pb2.Photo, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class BatchUpdatePhotosRequest(_message.Message):
    __slots__ = ("update_photo_requests",)
    UPDATE_PHOTO_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    update_photo_requests: _containers.RepeatedCompositeFieldContainer[UpdatePhotoRequest]
    def __init__(self, update_photo_requests: _Optional[_Iterable[_Union[UpdatePhotoRequest, _Mapping]]] = ...) -> None: ...

class BatchUpdatePhotosResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PhotoResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[PhotoResponse, _Mapping]]] = ...) -> None: ...

class DeletePhotoRequest(_message.Message):
    __slots__ = ("photo_id",)
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    photo_id: str
    def __init__(self, photo_id: _Optional[str] = ...) -> None: ...

class BatchDeletePhotosRequest(_message.Message):
    __slots__ = ("photo_ids",)
    PHOTO_IDS_FIELD_NUMBER: _ClassVar[int]
    photo_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, photo_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePhotoSequenceRequest(_message.Message):
    __slots__ = ("photo_sequence", "input_type")
    class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INPUT_TYPE_UNSPECIFIED: _ClassVar[CreatePhotoSequenceRequest.InputType]
        VIDEO: _ClassVar[CreatePhotoSequenceRequest.InputType]
        XDM: _ClassVar[CreatePhotoSequenceRequest.InputType]
    INPUT_TYPE_UNSPECIFIED: CreatePhotoSequenceRequest.InputType
    VIDEO: CreatePhotoSequenceRequest.InputType
    XDM: CreatePhotoSequenceRequest.InputType
    PHOTO_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    photo_sequence: _resources_pb2.PhotoSequence
    input_type: CreatePhotoSequenceRequest.InputType
    def __init__(self, photo_sequence: _Optional[_Union[_resources_pb2.PhotoSequence, _Mapping]] = ..., input_type: _Optional[_Union[CreatePhotoSequenceRequest.InputType, str]] = ...) -> None: ...

class GetPhotoSequenceRequest(_message.Message):
    __slots__ = ("sequence_id", "view", "filter")
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    sequence_id: str
    view: PhotoView
    filter: str
    def __init__(self, sequence_id: _Optional[str] = ..., view: _Optional[_Union[PhotoView, str]] = ..., filter: _Optional[str] = ...) -> None: ...

class DeletePhotoSequenceRequest(_message.Message):
    __slots__ = ("sequence_id",)
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    sequence_id: str
    def __init__(self, sequence_id: _Optional[str] = ...) -> None: ...

class BatchDeletePhotosResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, status: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class ListPhotoSequencesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListPhotoSequencesResponse(_message.Message):
    __slots__ = ("photo_sequences", "next_page_token")
    PHOTO_SEQUENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    photo_sequences: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str
    def __init__(self, photo_sequences: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
