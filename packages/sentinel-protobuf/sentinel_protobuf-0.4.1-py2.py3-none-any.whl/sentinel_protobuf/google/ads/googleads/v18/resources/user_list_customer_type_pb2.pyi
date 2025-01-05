from google.ads.googleads.v18.enums import user_list_customer_type_category_pb2 as _user_list_customer_type_category_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserListCustomerType(_message.Message):
    __slots__ = ('resource_name', 'user_list', 'customer_type_category')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TYPE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    user_list: str
    customer_type_category: _user_list_customer_type_category_pb2.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory

    def __init__(self, resource_name: _Optional[str]=..., user_list: _Optional[str]=..., customer_type_category: _Optional[_Union[_user_list_customer_type_category_pb2.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory, str]]=...) -> None:
        ...