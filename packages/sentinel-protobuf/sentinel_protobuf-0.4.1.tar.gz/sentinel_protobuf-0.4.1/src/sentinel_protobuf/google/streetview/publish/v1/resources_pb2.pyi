from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESSING_STATE_UNSPECIFIED: _ClassVar[ProcessingState]
    PENDING: _ClassVar[ProcessingState]
    PROCESSING: _ClassVar[ProcessingState]
    PROCESSED: _ClassVar[ProcessingState]
    FAILED: _ClassVar[ProcessingState]

class ProcessingFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESSING_FAILURE_REASON_UNSPECIFIED: _ClassVar[ProcessingFailureReason]
    LOW_RESOLUTION: _ClassVar[ProcessingFailureReason]
    DUPLICATE: _ClassVar[ProcessingFailureReason]
    INSUFFICIENT_GPS: _ClassVar[ProcessingFailureReason]
    NO_OVERLAP_GPS: _ClassVar[ProcessingFailureReason]
    INVALID_GPS: _ClassVar[ProcessingFailureReason]
    FAILED_TO_REFINE_POSITIONS: _ClassVar[ProcessingFailureReason]
    TAKEDOWN: _ClassVar[ProcessingFailureReason]
    CORRUPT_VIDEO: _ClassVar[ProcessingFailureReason]
    INTERNAL: _ClassVar[ProcessingFailureReason]
    INVALID_VIDEO_FORMAT: _ClassVar[ProcessingFailureReason]
    INVALID_VIDEO_DIMENSIONS: _ClassVar[ProcessingFailureReason]
    INVALID_CAPTURE_TIME: _ClassVar[ProcessingFailureReason]
    GPS_DATA_GAP: _ClassVar[ProcessingFailureReason]
    JUMPY_GPS: _ClassVar[ProcessingFailureReason]
    INVALID_IMU: _ClassVar[ProcessingFailureReason]
    INSUFFICIENT_IMU: _ClassVar[ProcessingFailureReason]
    INSUFFICIENT_OVERLAP_TIME_SERIES: _ClassVar[ProcessingFailureReason]
    IMU_DATA_GAP: _ClassVar[ProcessingFailureReason]
    UNSUPPORTED_CAMERA: _ClassVar[ProcessingFailureReason]
    NOT_OUTDOORS: _ClassVar[ProcessingFailureReason]
    INSUFFICIENT_VIDEO_FRAMES: _ClassVar[ProcessingFailureReason]
    INSUFFICIENT_MOVEMENT: _ClassVar[ProcessingFailureReason]
    MAST_DOWN: _ClassVar[ProcessingFailureReason]
    CAMERA_COVERED: _ClassVar[ProcessingFailureReason]
PROCESSING_STATE_UNSPECIFIED: ProcessingState
PENDING: ProcessingState
PROCESSING: ProcessingState
PROCESSED: ProcessingState
FAILED: ProcessingState
PROCESSING_FAILURE_REASON_UNSPECIFIED: ProcessingFailureReason
LOW_RESOLUTION: ProcessingFailureReason
DUPLICATE: ProcessingFailureReason
INSUFFICIENT_GPS: ProcessingFailureReason
NO_OVERLAP_GPS: ProcessingFailureReason
INVALID_GPS: ProcessingFailureReason
FAILED_TO_REFINE_POSITIONS: ProcessingFailureReason
TAKEDOWN: ProcessingFailureReason
CORRUPT_VIDEO: ProcessingFailureReason
INTERNAL: ProcessingFailureReason
INVALID_VIDEO_FORMAT: ProcessingFailureReason
INVALID_VIDEO_DIMENSIONS: ProcessingFailureReason
INVALID_CAPTURE_TIME: ProcessingFailureReason
GPS_DATA_GAP: ProcessingFailureReason
JUMPY_GPS: ProcessingFailureReason
INVALID_IMU: ProcessingFailureReason
INSUFFICIENT_IMU: ProcessingFailureReason
INSUFFICIENT_OVERLAP_TIME_SERIES: ProcessingFailureReason
IMU_DATA_GAP: ProcessingFailureReason
UNSUPPORTED_CAMERA: ProcessingFailureReason
NOT_OUTDOORS: ProcessingFailureReason
INSUFFICIENT_VIDEO_FRAMES: ProcessingFailureReason
INSUFFICIENT_MOVEMENT: ProcessingFailureReason
MAST_DOWN: ProcessingFailureReason
CAMERA_COVERED: ProcessingFailureReason

class UploadRef(_message.Message):
    __slots__ = ("upload_url",)
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    def __init__(self, upload_url: _Optional[str] = ...) -> None: ...

class PhotoId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Level(_message.Message):
    __slots__ = ("number", "name")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    number: float
    name: str
    def __init__(self, number: _Optional[float] = ..., name: _Optional[str] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ("lat_lng_pair", "altitude", "heading", "pitch", "roll", "gps_record_timestamp_unix_epoch", "level", "accuracy_meters")
    LAT_LNG_PAIR_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    GPS_RECORD_TIMESTAMP_UNIX_EPOCH_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_METERS_FIELD_NUMBER: _ClassVar[int]
    lat_lng_pair: _latlng_pb2.LatLng
    altitude: float
    heading: float
    pitch: float
    roll: float
    gps_record_timestamp_unix_epoch: _timestamp_pb2.Timestamp
    level: Level
    accuracy_meters: float
    def __init__(self, lat_lng_pair: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., altitude: _Optional[float] = ..., heading: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ..., gps_record_timestamp_unix_epoch: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., level: _Optional[_Union[Level, _Mapping]] = ..., accuracy_meters: _Optional[float] = ...) -> None: ...

class Imu(_message.Message):
    __slots__ = ("accel_mpsps", "gyro_rps", "mag_ut")
    class Measurement3d(_message.Message):
        __slots__ = ("capture_time", "x", "y", "z")
        CAPTURE_TIME_FIELD_NUMBER: _ClassVar[int]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        Z_FIELD_NUMBER: _ClassVar[int]
        capture_time: _timestamp_pb2.Timestamp
        x: float
        y: float
        z: float
        def __init__(self, capture_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...
    ACCEL_MPSPS_FIELD_NUMBER: _ClassVar[int]
    GYRO_RPS_FIELD_NUMBER: _ClassVar[int]
    MAG_UT_FIELD_NUMBER: _ClassVar[int]
    accel_mpsps: _containers.RepeatedCompositeFieldContainer[Imu.Measurement3d]
    gyro_rps: _containers.RepeatedCompositeFieldContainer[Imu.Measurement3d]
    mag_ut: _containers.RepeatedCompositeFieldContainer[Imu.Measurement3d]
    def __init__(self, accel_mpsps: _Optional[_Iterable[_Union[Imu.Measurement3d, _Mapping]]] = ..., gyro_rps: _Optional[_Iterable[_Union[Imu.Measurement3d, _Mapping]]] = ..., mag_ut: _Optional[_Iterable[_Union[Imu.Measurement3d, _Mapping]]] = ...) -> None: ...

class Place(_message.Message):
    __slots__ = ("place_id", "name", "language_code")
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    name: str
    language_code: str
    def __init__(self, place_id: _Optional[str] = ..., name: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("target",)
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: PhotoId
    def __init__(self, target: _Optional[_Union[PhotoId, _Mapping]] = ...) -> None: ...

class Photo(_message.Message):
    __slots__ = ("photo_id", "upload_reference", "download_url", "thumbnail_url", "share_link", "pose", "connections", "capture_time", "upload_time", "places", "view_count", "transfer_status", "maps_publish_status")
    class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSFER_STATUS_UNKNOWN: _ClassVar[Photo.TransferStatus]
        NEVER_TRANSFERRED: _ClassVar[Photo.TransferStatus]
        PENDING: _ClassVar[Photo.TransferStatus]
        COMPLETED: _ClassVar[Photo.TransferStatus]
        REJECTED: _ClassVar[Photo.TransferStatus]
        EXPIRED: _ClassVar[Photo.TransferStatus]
        CANCELLED: _ClassVar[Photo.TransferStatus]
        RECEIVED_VIA_TRANSFER: _ClassVar[Photo.TransferStatus]
    TRANSFER_STATUS_UNKNOWN: Photo.TransferStatus
    NEVER_TRANSFERRED: Photo.TransferStatus
    PENDING: Photo.TransferStatus
    COMPLETED: Photo.TransferStatus
    REJECTED: Photo.TransferStatus
    EXPIRED: Photo.TransferStatus
    CANCELLED: Photo.TransferStatus
    RECEIVED_VIA_TRANSFER: Photo.TransferStatus
    class MapsPublishStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_MAPS_PUBLISH_STATUS: _ClassVar[Photo.MapsPublishStatus]
        PUBLISHED: _ClassVar[Photo.MapsPublishStatus]
        REJECTED_UNKNOWN: _ClassVar[Photo.MapsPublishStatus]
    UNSPECIFIED_MAPS_PUBLISH_STATUS: Photo.MapsPublishStatus
    PUBLISHED: Photo.MapsPublishStatus
    REJECTED_UNKNOWN: Photo.MapsPublishStatus
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    SHARE_LINK_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    PLACES_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    MAPS_PUBLISH_STATUS_FIELD_NUMBER: _ClassVar[int]
    photo_id: PhotoId
    upload_reference: UploadRef
    download_url: str
    thumbnail_url: str
    share_link: str
    pose: Pose
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    capture_time: _timestamp_pb2.Timestamp
    upload_time: _timestamp_pb2.Timestamp
    places: _containers.RepeatedCompositeFieldContainer[Place]
    view_count: int
    transfer_status: Photo.TransferStatus
    maps_publish_status: Photo.MapsPublishStatus
    def __init__(self, photo_id: _Optional[_Union[PhotoId, _Mapping]] = ..., upload_reference: _Optional[_Union[UploadRef, _Mapping]] = ..., download_url: _Optional[str] = ..., thumbnail_url: _Optional[str] = ..., share_link: _Optional[str] = ..., pose: _Optional[_Union[Pose, _Mapping]] = ..., connections: _Optional[_Iterable[_Union[Connection, _Mapping]]] = ..., capture_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., places: _Optional[_Iterable[_Union[Place, _Mapping]]] = ..., view_count: _Optional[int] = ..., transfer_status: _Optional[_Union[Photo.TransferStatus, str]] = ..., maps_publish_status: _Optional[_Union[Photo.MapsPublishStatus, str]] = ...) -> None: ...

class PhotoSequence(_message.Message):
    __slots__ = ("id", "photos", "upload_reference", "capture_time_override", "upload_time", "raw_gps_timeline", "gps_source", "imu", "processing_state", "failure_reason", "failure_details", "distance_meters", "sequence_bounds", "view_count", "filename")
    class GpsSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHOTO_SEQUENCE: _ClassVar[PhotoSequence.GpsSource]
        CAMERA_MOTION_METADATA_TRACK: _ClassVar[PhotoSequence.GpsSource]
    PHOTO_SEQUENCE: PhotoSequence.GpsSource
    CAMERA_MOTION_METADATA_TRACK: PhotoSequence.GpsSource
    ID_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_TIME_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    RAW_GPS_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    GPS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IMU_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    FAILURE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    photos: _containers.RepeatedCompositeFieldContainer[Photo]
    upload_reference: UploadRef
    capture_time_override: _timestamp_pb2.Timestamp
    upload_time: _timestamp_pb2.Timestamp
    raw_gps_timeline: _containers.RepeatedCompositeFieldContainer[Pose]
    gps_source: PhotoSequence.GpsSource
    imu: Imu
    processing_state: ProcessingState
    failure_reason: ProcessingFailureReason
    failure_details: ProcessingFailureDetails
    distance_meters: float
    sequence_bounds: LatLngBounds
    view_count: int
    filename: str
    def __init__(self, id: _Optional[str] = ..., photos: _Optional[_Iterable[_Union[Photo, _Mapping]]] = ..., upload_reference: _Optional[_Union[UploadRef, _Mapping]] = ..., capture_time_override: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., raw_gps_timeline: _Optional[_Iterable[_Union[Pose, _Mapping]]] = ..., gps_source: _Optional[_Union[PhotoSequence.GpsSource, str]] = ..., imu: _Optional[_Union[Imu, _Mapping]] = ..., processing_state: _Optional[_Union[ProcessingState, str]] = ..., failure_reason: _Optional[_Union[ProcessingFailureReason, str]] = ..., failure_details: _Optional[_Union[ProcessingFailureDetails, _Mapping]] = ..., distance_meters: _Optional[float] = ..., sequence_bounds: _Optional[_Union[LatLngBounds, _Mapping]] = ..., view_count: _Optional[int] = ..., filename: _Optional[str] = ...) -> None: ...

class LatLngBounds(_message.Message):
    __slots__ = ("southwest", "northeast")
    SOUTHWEST_FIELD_NUMBER: _ClassVar[int]
    NORTHEAST_FIELD_NUMBER: _ClassVar[int]
    southwest: _latlng_pb2.LatLng
    northeast: _latlng_pb2.LatLng
    def __init__(self, southwest: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., northeast: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ...) -> None: ...

class ProcessingFailureDetails(_message.Message):
    __slots__ = ("insufficient_gps_details", "gps_data_gap_details", "imu_data_gap_details", "not_outdoors_details", "no_overlap_gps_details")
    INSUFFICIENT_GPS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    GPS_DATA_GAP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMU_DATA_GAP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NOT_OUTDOORS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NO_OVERLAP_GPS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    insufficient_gps_details: InsufficientGpsFailureDetails
    gps_data_gap_details: GpsDataGapFailureDetails
    imu_data_gap_details: ImuDataGapFailureDetails
    not_outdoors_details: NotOutdoorsFailureDetails
    no_overlap_gps_details: NoOverlapGpsFailureDetails
    def __init__(self, insufficient_gps_details: _Optional[_Union[InsufficientGpsFailureDetails, _Mapping]] = ..., gps_data_gap_details: _Optional[_Union[GpsDataGapFailureDetails, _Mapping]] = ..., imu_data_gap_details: _Optional[_Union[ImuDataGapFailureDetails, _Mapping]] = ..., not_outdoors_details: _Optional[_Union[NotOutdoorsFailureDetails, _Mapping]] = ..., no_overlap_gps_details: _Optional[_Union[NoOverlapGpsFailureDetails, _Mapping]] = ...) -> None: ...

class InsufficientGpsFailureDetails(_message.Message):
    __slots__ = ("gps_points_found",)
    GPS_POINTS_FOUND_FIELD_NUMBER: _ClassVar[int]
    gps_points_found: int
    def __init__(self, gps_points_found: _Optional[int] = ...) -> None: ...

class GpsDataGapFailureDetails(_message.Message):
    __slots__ = ("gap_duration", "gap_start_time")
    GAP_DURATION_FIELD_NUMBER: _ClassVar[int]
    GAP_START_TIME_FIELD_NUMBER: _ClassVar[int]
    gap_duration: _duration_pb2.Duration
    gap_start_time: _duration_pb2.Duration
    def __init__(self, gap_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gap_start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ImuDataGapFailureDetails(_message.Message):
    __slots__ = ("gap_duration", "gap_start_time")
    GAP_DURATION_FIELD_NUMBER: _ClassVar[int]
    GAP_START_TIME_FIELD_NUMBER: _ClassVar[int]
    gap_duration: _duration_pb2.Duration
    gap_start_time: _duration_pb2.Duration
    def __init__(self, gap_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gap_start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class NotOutdoorsFailureDetails(_message.Message):
    __slots__ = ("start_time",)
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _duration_pb2.Duration
    def __init__(self, start_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class NoOverlapGpsFailureDetails(_message.Message):
    __slots__ = ("gps_start_time", "gps_end_time", "video_start_time", "video_end_time")
    GPS_START_TIME_FIELD_NUMBER: _ClassVar[int]
    GPS_END_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_START_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_END_TIME_FIELD_NUMBER: _ClassVar[int]
    gps_start_time: _timestamp_pb2.Timestamp
    gps_end_time: _timestamp_pb2.Timestamp
    video_start_time: _timestamp_pb2.Timestamp
    video_end_time: _timestamp_pb2.Timestamp
    def __init__(self, gps_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gps_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., video_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., video_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
