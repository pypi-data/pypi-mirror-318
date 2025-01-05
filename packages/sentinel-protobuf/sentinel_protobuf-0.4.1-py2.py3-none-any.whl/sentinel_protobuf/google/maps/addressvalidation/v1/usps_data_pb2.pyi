from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UspsAddress(_message.Message):
    __slots__ = ('first_address_line', 'firm', 'second_address_line', 'urbanization', 'city_state_zip_address_line', 'city', 'state', 'zip_code', 'zip_code_extension')
    FIRST_ADDRESS_LINE_FIELD_NUMBER: _ClassVar[int]
    FIRM_FIELD_NUMBER: _ClassVar[int]
    SECOND_ADDRESS_LINE_FIELD_NUMBER: _ClassVar[int]
    URBANIZATION_FIELD_NUMBER: _ClassVar[int]
    CITY_STATE_ZIP_ADDRESS_LINE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    first_address_line: str
    firm: str
    second_address_line: str
    urbanization: str
    city_state_zip_address_line: str
    city: str
    state: str
    zip_code: str
    zip_code_extension: str

    def __init__(self, first_address_line: _Optional[str]=..., firm: _Optional[str]=..., second_address_line: _Optional[str]=..., urbanization: _Optional[str]=..., city_state_zip_address_line: _Optional[str]=..., city: _Optional[str]=..., state: _Optional[str]=..., zip_code: _Optional[str]=..., zip_code_extension: _Optional[str]=...) -> None:
        ...

class UspsData(_message.Message):
    __slots__ = ('standardized_address', 'delivery_point_code', 'delivery_point_check_digit', 'dpv_confirmation', 'dpv_footnote', 'dpv_cmra', 'dpv_vacant', 'dpv_no_stat', 'dpv_no_stat_reason_code', 'dpv_drop', 'dpv_throwback', 'dpv_non_delivery_days', 'dpv_non_delivery_days_values', 'dpv_no_secure_location', 'dpv_pbsa', 'dpv_door_not_accessible', 'dpv_enhanced_delivery_code', 'carrier_route', 'carrier_route_indicator', 'ews_no_match', 'post_office_city', 'post_office_state', 'abbreviated_city', 'fips_county_code', 'county', 'elot_number', 'elot_flag', 'lacs_link_return_code', 'lacs_link_indicator', 'po_box_only_postal_code', 'suitelink_footnote', 'pmb_designator', 'pmb_number', 'address_record_type', 'default_address', 'error_message', 'cass_processed')
    STANDARDIZED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_POINT_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_POINT_CHECK_DIGIT_FIELD_NUMBER: _ClassVar[int]
    DPV_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    DPV_FOOTNOTE_FIELD_NUMBER: _ClassVar[int]
    DPV_CMRA_FIELD_NUMBER: _ClassVar[int]
    DPV_VACANT_FIELD_NUMBER: _ClassVar[int]
    DPV_NO_STAT_FIELD_NUMBER: _ClassVar[int]
    DPV_NO_STAT_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    DPV_DROP_FIELD_NUMBER: _ClassVar[int]
    DPV_THROWBACK_FIELD_NUMBER: _ClassVar[int]
    DPV_NON_DELIVERY_DAYS_FIELD_NUMBER: _ClassVar[int]
    DPV_NON_DELIVERY_DAYS_VALUES_FIELD_NUMBER: _ClassVar[int]
    DPV_NO_SECURE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DPV_PBSA_FIELD_NUMBER: _ClassVar[int]
    DPV_DOOR_NOT_ACCESSIBLE_FIELD_NUMBER: _ClassVar[int]
    DPV_ENHANCED_DELIVERY_CODE_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ROUTE_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ROUTE_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    EWS_NO_MATCH_FIELD_NUMBER: _ClassVar[int]
    POST_OFFICE_CITY_FIELD_NUMBER: _ClassVar[int]
    POST_OFFICE_STATE_FIELD_NUMBER: _ClassVar[int]
    ABBREVIATED_CITY_FIELD_NUMBER: _ClassVar[int]
    FIPS_COUNTY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTY_FIELD_NUMBER: _ClassVar[int]
    ELOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ELOT_FLAG_FIELD_NUMBER: _ClassVar[int]
    LACS_LINK_RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    LACS_LINK_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    PO_BOX_ONLY_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    SUITELINK_FOOTNOTE_FIELD_NUMBER: _ClassVar[int]
    PMB_DESIGNATOR_FIELD_NUMBER: _ClassVar[int]
    PMB_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_RECORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CASS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    standardized_address: UspsAddress
    delivery_point_code: str
    delivery_point_check_digit: str
    dpv_confirmation: str
    dpv_footnote: str
    dpv_cmra: str
    dpv_vacant: str
    dpv_no_stat: str
    dpv_no_stat_reason_code: int
    dpv_drop: str
    dpv_throwback: str
    dpv_non_delivery_days: str
    dpv_non_delivery_days_values: int
    dpv_no_secure_location: str
    dpv_pbsa: str
    dpv_door_not_accessible: str
    dpv_enhanced_delivery_code: str
    carrier_route: str
    carrier_route_indicator: str
    ews_no_match: bool
    post_office_city: str
    post_office_state: str
    abbreviated_city: str
    fips_county_code: str
    county: str
    elot_number: str
    elot_flag: str
    lacs_link_return_code: str
    lacs_link_indicator: str
    po_box_only_postal_code: bool
    suitelink_footnote: str
    pmb_designator: str
    pmb_number: str
    address_record_type: str
    default_address: bool
    error_message: str
    cass_processed: bool

    def __init__(self, standardized_address: _Optional[_Union[UspsAddress, _Mapping]]=..., delivery_point_code: _Optional[str]=..., delivery_point_check_digit: _Optional[str]=..., dpv_confirmation: _Optional[str]=..., dpv_footnote: _Optional[str]=..., dpv_cmra: _Optional[str]=..., dpv_vacant: _Optional[str]=..., dpv_no_stat: _Optional[str]=..., dpv_no_stat_reason_code: _Optional[int]=..., dpv_drop: _Optional[str]=..., dpv_throwback: _Optional[str]=..., dpv_non_delivery_days: _Optional[str]=..., dpv_non_delivery_days_values: _Optional[int]=..., dpv_no_secure_location: _Optional[str]=..., dpv_pbsa: _Optional[str]=..., dpv_door_not_accessible: _Optional[str]=..., dpv_enhanced_delivery_code: _Optional[str]=..., carrier_route: _Optional[str]=..., carrier_route_indicator: _Optional[str]=..., ews_no_match: bool=..., post_office_city: _Optional[str]=..., post_office_state: _Optional[str]=..., abbreviated_city: _Optional[str]=..., fips_county_code: _Optional[str]=..., county: _Optional[str]=..., elot_number: _Optional[str]=..., elot_flag: _Optional[str]=..., lacs_link_return_code: _Optional[str]=..., lacs_link_indicator: _Optional[str]=..., po_box_only_postal_code: bool=..., suitelink_footnote: _Optional[str]=..., pmb_designator: _Optional[str]=..., pmb_number: _Optional[str]=..., address_record_type: _Optional[str]=..., default_address: bool=..., error_message: _Optional[str]=..., cass_processed: bool=...) -> None:
        ...