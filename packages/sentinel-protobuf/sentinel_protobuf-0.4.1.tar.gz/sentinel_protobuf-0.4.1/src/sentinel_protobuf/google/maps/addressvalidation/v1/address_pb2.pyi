from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ('formatted_address', 'postal_address', 'address_components', 'missing_component_types', 'unconfirmed_component_types', 'unresolved_tokens')
    FORMATTED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    MISSING_COMPONENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_COMPONENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    formatted_address: str
    postal_address: _postal_address_pb2.PostalAddress
    address_components: _containers.RepeatedCompositeFieldContainer[AddressComponent]
    missing_component_types: _containers.RepeatedScalarFieldContainer[str]
    unconfirmed_component_types: _containers.RepeatedScalarFieldContainer[str]
    unresolved_tokens: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, formatted_address: _Optional[str]=..., postal_address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., address_components: _Optional[_Iterable[_Union[AddressComponent, _Mapping]]]=..., missing_component_types: _Optional[_Iterable[str]]=..., unconfirmed_component_types: _Optional[_Iterable[str]]=..., unresolved_tokens: _Optional[_Iterable[str]]=...) -> None:
        ...

class AddressComponent(_message.Message):
    __slots__ = ('component_name', 'component_type', 'confirmation_level', 'inferred', 'spell_corrected', 'replaced', 'unexpected')

    class ConfirmationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONFIRMATION_LEVEL_UNSPECIFIED: _ClassVar[AddressComponent.ConfirmationLevel]
        CONFIRMED: _ClassVar[AddressComponent.ConfirmationLevel]
        UNCONFIRMED_BUT_PLAUSIBLE: _ClassVar[AddressComponent.ConfirmationLevel]
        UNCONFIRMED_AND_SUSPICIOUS: _ClassVar[AddressComponent.ConfirmationLevel]
    CONFIRMATION_LEVEL_UNSPECIFIED: AddressComponent.ConfirmationLevel
    CONFIRMED: AddressComponent.ConfirmationLevel
    UNCONFIRMED_BUT_PLAUSIBLE: AddressComponent.ConfirmationLevel
    UNCONFIRMED_AND_SUSPICIOUS: AddressComponent.ConfirmationLevel
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INFERRED_FIELD_NUMBER: _ClassVar[int]
    SPELL_CORRECTED_FIELD_NUMBER: _ClassVar[int]
    REPLACED_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_FIELD_NUMBER: _ClassVar[int]
    component_name: ComponentName
    component_type: str
    confirmation_level: AddressComponent.ConfirmationLevel
    inferred: bool
    spell_corrected: bool
    replaced: bool
    unexpected: bool

    def __init__(self, component_name: _Optional[_Union[ComponentName, _Mapping]]=..., component_type: _Optional[str]=..., confirmation_level: _Optional[_Union[AddressComponent.ConfirmationLevel, str]]=..., inferred: bool=..., spell_corrected: bool=..., replaced: bool=..., unexpected: bool=...) -> None:
        ...

class ComponentName(_message.Message):
    __slots__ = ('text', 'language_code')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    text: str
    language_code: str

    def __init__(self, text: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...