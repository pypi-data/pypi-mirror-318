from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureFlags(_message.Message):
    __slots__ = ('reverse_scans', 'mutate_rows_rate_limit', 'mutate_rows_rate_limit2', 'last_scanned_row_responses', 'routing_cookie', 'retry_info', 'client_side_metrics_enabled', 'traffic_director_enabled', 'direct_access_requested')
    REVERSE_SCANS_FIELD_NUMBER: _ClassVar[int]
    MUTATE_ROWS_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MUTATE_ROWS_RATE_LIMIT2_FIELD_NUMBER: _ClassVar[int]
    LAST_SCANNED_ROW_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    RETRY_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SIDE_METRICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_DIRECTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ACCESS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    reverse_scans: bool
    mutate_rows_rate_limit: bool
    mutate_rows_rate_limit2: bool
    last_scanned_row_responses: bool
    routing_cookie: bool
    retry_info: bool
    client_side_metrics_enabled: bool
    traffic_director_enabled: bool
    direct_access_requested: bool

    def __init__(self, reverse_scans: bool=..., mutate_rows_rate_limit: bool=..., mutate_rows_rate_limit2: bool=..., last_scanned_row_responses: bool=..., routing_cookie: bool=..., retry_info: bool=..., client_side_metrics_enabled: bool=..., traffic_director_enabled: bool=..., direct_access_requested: bool=...) -> None:
        ...