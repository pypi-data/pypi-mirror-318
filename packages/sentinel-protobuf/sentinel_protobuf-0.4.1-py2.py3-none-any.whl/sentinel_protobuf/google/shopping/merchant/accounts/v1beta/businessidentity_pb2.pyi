from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BusinessIdentity(_message.Message):
    __slots__ = ('name', 'promotions_consent', 'black_owned', 'women_owned', 'veteran_owned', 'latino_owned', 'small_business')

    class PromotionsConsent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROMOTIONS_CONSENT_UNSPECIFIED: _ClassVar[BusinessIdentity.PromotionsConsent]
        PROMOTIONS_CONSENT_GIVEN: _ClassVar[BusinessIdentity.PromotionsConsent]
        PROMOTIONS_CONSENT_DENIED: _ClassVar[BusinessIdentity.PromotionsConsent]
    PROMOTIONS_CONSENT_UNSPECIFIED: BusinessIdentity.PromotionsConsent
    PROMOTIONS_CONSENT_GIVEN: BusinessIdentity.PromotionsConsent
    PROMOTIONS_CONSENT_DENIED: BusinessIdentity.PromotionsConsent

    class IdentityAttribute(_message.Message):
        __slots__ = ('identity_declaration',)

        class IdentityDeclaration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IDENTITY_DECLARATION_UNSPECIFIED: _ClassVar[BusinessIdentity.IdentityAttribute.IdentityDeclaration]
            SELF_IDENTIFIES_AS: _ClassVar[BusinessIdentity.IdentityAttribute.IdentityDeclaration]
            DOES_NOT_SELF_IDENTIFY_AS: _ClassVar[BusinessIdentity.IdentityAttribute.IdentityDeclaration]
        IDENTITY_DECLARATION_UNSPECIFIED: BusinessIdentity.IdentityAttribute.IdentityDeclaration
        SELF_IDENTIFIES_AS: BusinessIdentity.IdentityAttribute.IdentityDeclaration
        DOES_NOT_SELF_IDENTIFY_AS: BusinessIdentity.IdentityAttribute.IdentityDeclaration
        IDENTITY_DECLARATION_FIELD_NUMBER: _ClassVar[int]
        identity_declaration: BusinessIdentity.IdentityAttribute.IdentityDeclaration

        def __init__(self, identity_declaration: _Optional[_Union[BusinessIdentity.IdentityAttribute.IdentityDeclaration, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONS_CONSENT_FIELD_NUMBER: _ClassVar[int]
    BLACK_OWNED_FIELD_NUMBER: _ClassVar[int]
    WOMEN_OWNED_FIELD_NUMBER: _ClassVar[int]
    VETERAN_OWNED_FIELD_NUMBER: _ClassVar[int]
    LATINO_OWNED_FIELD_NUMBER: _ClassVar[int]
    SMALL_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    promotions_consent: BusinessIdentity.PromotionsConsent
    black_owned: BusinessIdentity.IdentityAttribute
    women_owned: BusinessIdentity.IdentityAttribute
    veteran_owned: BusinessIdentity.IdentityAttribute
    latino_owned: BusinessIdentity.IdentityAttribute
    small_business: BusinessIdentity.IdentityAttribute

    def __init__(self, name: _Optional[str]=..., promotions_consent: _Optional[_Union[BusinessIdentity.PromotionsConsent, str]]=..., black_owned: _Optional[_Union[BusinessIdentity.IdentityAttribute, _Mapping]]=..., women_owned: _Optional[_Union[BusinessIdentity.IdentityAttribute, _Mapping]]=..., veteran_owned: _Optional[_Union[BusinessIdentity.IdentityAttribute, _Mapping]]=..., latino_owned: _Optional[_Union[BusinessIdentity.IdentityAttribute, _Mapping]]=..., small_business: _Optional[_Union[BusinessIdentity.IdentityAttribute, _Mapping]]=...) -> None:
        ...

class GetBusinessIdentityRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBusinessIdentityRequest(_message.Message):
    __slots__ = ('business_identity', 'update_mask')
    BUSINESS_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    business_identity: BusinessIdentity
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, business_identity: _Optional[_Union[BusinessIdentity, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...