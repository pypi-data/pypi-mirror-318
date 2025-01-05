from google.ads.googleads.v16.enums import call_tracking_display_location_pb2 as _call_tracking_display_location_pb2
from google.ads.googleads.v16.enums import call_type_pb2 as _call_type_pb2
from google.ads.googleads.v16.enums import google_voice_call_status_pb2 as _google_voice_call_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CallView(_message.Message):
    __slots__ = ('resource_name', 'caller_country_code', 'caller_area_code', 'call_duration_seconds', 'start_call_date_time', 'end_call_date_time', 'call_tracking_display_location', 'type', 'call_status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CALLER_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CALLER_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    CALL_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    START_CALL_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_CALL_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CALL_TRACKING_DISPLAY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    caller_country_code: str
    caller_area_code: str
    call_duration_seconds: int
    start_call_date_time: str
    end_call_date_time: str
    call_tracking_display_location: _call_tracking_display_location_pb2.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    type: _call_type_pb2.CallTypeEnum.CallType
    call_status: _google_voice_call_status_pb2.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus

    def __init__(self, resource_name: _Optional[str]=..., caller_country_code: _Optional[str]=..., caller_area_code: _Optional[str]=..., call_duration_seconds: _Optional[int]=..., start_call_date_time: _Optional[str]=..., end_call_date_time: _Optional[str]=..., call_tracking_display_location: _Optional[_Union[_call_tracking_display_location_pb2.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation, str]]=..., type: _Optional[_Union[_call_type_pb2.CallTypeEnum.CallType, str]]=..., call_status: _Optional[_Union[_google_voice_call_status_pb2.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus, str]]=...) -> None:
        ...