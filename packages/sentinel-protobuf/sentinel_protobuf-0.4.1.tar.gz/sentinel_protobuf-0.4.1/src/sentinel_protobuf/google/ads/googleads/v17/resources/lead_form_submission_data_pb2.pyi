from google.ads.googleads.v17.enums import lead_form_field_user_input_type_pb2 as _lead_form_field_user_input_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LeadFormSubmissionData(_message.Message):
    __slots__ = ('resource_name', 'id', 'asset', 'campaign', 'lead_form_submission_fields', 'custom_lead_form_submission_fields', 'ad_group', 'ad_group_ad', 'gclid', 'submission_date_time')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    LEAD_FORM_SUBMISSION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LEAD_FORM_SUBMISSION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    GCLID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: str
    asset: str
    campaign: str
    lead_form_submission_fields: _containers.RepeatedCompositeFieldContainer[LeadFormSubmissionField]
    custom_lead_form_submission_fields: _containers.RepeatedCompositeFieldContainer[CustomLeadFormSubmissionField]
    ad_group: str
    ad_group_ad: str
    gclid: str
    submission_date_time: str

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[str]=..., asset: _Optional[str]=..., campaign: _Optional[str]=..., lead_form_submission_fields: _Optional[_Iterable[_Union[LeadFormSubmissionField, _Mapping]]]=..., custom_lead_form_submission_fields: _Optional[_Iterable[_Union[CustomLeadFormSubmissionField, _Mapping]]]=..., ad_group: _Optional[str]=..., ad_group_ad: _Optional[str]=..., gclid: _Optional[str]=..., submission_date_time: _Optional[str]=...) -> None:
        ...

class LeadFormSubmissionField(_message.Message):
    __slots__ = ('field_type', 'field_value')
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_type: _lead_form_field_user_input_type_pb2.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    field_value: str

    def __init__(self, field_type: _Optional[_Union[_lead_form_field_user_input_type_pb2.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType, str]]=..., field_value: _Optional[str]=...) -> None:
        ...

class CustomLeadFormSubmissionField(_message.Message):
    __slots__ = ('question_text', 'field_value')
    QUESTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    question_text: str
    field_value: str

    def __init__(self, question_text: _Optional[str]=..., field_value: _Optional[str]=...) -> None:
        ...