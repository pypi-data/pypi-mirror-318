from google.ads.googleads.v17.enums import consent_status_pb2 as _consent_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Consent(_message.Message):
    __slots__ = ('ad_user_data', 'ad_personalization')
    AD_USER_DATA_FIELD_NUMBER: _ClassVar[int]
    AD_PERSONALIZATION_FIELD_NUMBER: _ClassVar[int]
    ad_user_data: _consent_status_pb2.ConsentStatusEnum.ConsentStatus
    ad_personalization: _consent_status_pb2.ConsentStatusEnum.ConsentStatus

    def __init__(self, ad_user_data: _Optional[_Union[_consent_status_pb2.ConsentStatusEnum.ConsentStatus, str]]=..., ad_personalization: _Optional[_Union[_consent_status_pb2.ConsentStatusEnum.ConsentStatus, str]]=...) -> None:
        ...