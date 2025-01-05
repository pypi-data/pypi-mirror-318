from google.ads.searchads360.v0.enums import conversion_custom_variable_cardinality_pb2 as _conversion_custom_variable_cardinality_pb2
from google.ads.searchads360.v0.enums import conversion_custom_variable_family_pb2 as _conversion_custom_variable_family_pb2
from google.ads.searchads360.v0.enums import conversion_custom_variable_status_pb2 as _conversion_custom_variable_status_pb2
from google.ads.searchads360.v0.enums import floodlight_variable_data_type_pb2 as _floodlight_variable_data_type_pb2
from google.ads.searchads360.v0.enums import floodlight_variable_type_pb2 as _floodlight_variable_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariable(_message.Message):
    __slots__ = ("resource_name", "id", "name", "tag", "status", "owner_customer", "family", "cardinality", "floodlight_conversion_custom_variable_info", "custom_column_ids")
    class FloodlightConversionCustomVariableInfo(_message.Message):
        __slots__ = ("floodlight_variable_type", "floodlight_variable_data_type")
        FLOODLIGHT_VARIABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FLOODLIGHT_VARIABLE_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        floodlight_variable_type: _floodlight_variable_type_pb2.FloodlightVariableTypeEnum.FloodlightVariableType
        floodlight_variable_data_type: _floodlight_variable_data_type_pb2.FloodlightVariableDataTypeEnum.FloodlightVariableDataType
        def __init__(self, floodlight_variable_type: _Optional[_Union[_floodlight_variable_type_pb2.FloodlightVariableTypeEnum.FloodlightVariableType, str]] = ..., floodlight_variable_data_type: _Optional[_Union[_floodlight_variable_data_type_pb2.FloodlightVariableDataTypeEnum.FloodlightVariableDataType, str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    FLOODLIGHT_CONVERSION_CUSTOM_VARIABLE_INFO_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLUMN_IDS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    tag: str
    status: _conversion_custom_variable_status_pb2.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str
    family: _conversion_custom_variable_family_pb2.ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily
    cardinality: _conversion_custom_variable_cardinality_pb2.ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    floodlight_conversion_custom_variable_info: ConversionCustomVariable.FloodlightConversionCustomVariableInfo
    custom_column_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., tag: _Optional[str] = ..., status: _Optional[_Union[_conversion_custom_variable_status_pb2.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus, str]] = ..., owner_customer: _Optional[str] = ..., family: _Optional[_Union[_conversion_custom_variable_family_pb2.ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamily, str]] = ..., cardinality: _Optional[_Union[_conversion_custom_variable_cardinality_pb2.ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality, str]] = ..., floodlight_conversion_custom_variable_info: _Optional[_Union[ConversionCustomVariable.FloodlightConversionCustomVariableInfo, _Mapping]] = ..., custom_column_ids: _Optional[_Iterable[int]] = ...) -> None: ...
