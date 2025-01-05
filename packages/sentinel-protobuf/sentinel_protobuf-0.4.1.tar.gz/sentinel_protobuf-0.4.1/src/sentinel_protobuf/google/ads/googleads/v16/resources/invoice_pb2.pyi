from google.ads.googleads.v16.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v16.enums import invoice_type_pb2 as _invoice_type_pb2
from google.ads.googleads.v16.enums import month_of_year_pb2 as _month_of_year_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ("resource_name", "id", "type", "billing_setup", "payments_account_id", "payments_profile_id", "issue_date", "due_date", "service_date_range", "currency_code", "adjustments_subtotal_amount_micros", "adjustments_tax_amount_micros", "adjustments_total_amount_micros", "regulatory_costs_subtotal_amount_micros", "regulatory_costs_tax_amount_micros", "regulatory_costs_total_amount_micros", "export_charge_subtotal_amount_micros", "export_charge_tax_amount_micros", "export_charge_total_amount_micros", "subtotal_amount_micros", "tax_amount_micros", "total_amount_micros", "corrected_invoice", "replaced_invoices", "pdf_url", "account_budget_summaries", "account_summaries")
    class AccountSummary(_message.Message):
        __slots__ = ("customer", "billing_correction_subtotal_amount_micros", "billing_correction_tax_amount_micros", "billing_correction_total_amount_micros", "coupon_adjustment_subtotal_amount_micros", "coupon_adjustment_tax_amount_micros", "coupon_adjustment_total_amount_micros", "excess_credit_adjustment_subtotal_amount_micros", "excess_credit_adjustment_tax_amount_micros", "excess_credit_adjustment_total_amount_micros", "regulatory_costs_subtotal_amount_micros", "regulatory_costs_tax_amount_micros", "regulatory_costs_total_amount_micros", "export_charge_subtotal_amount_micros", "export_charge_tax_amount_micros", "export_charge_total_amount_micros", "subtotal_amount_micros", "tax_amount_micros", "total_amount_micros")
        CUSTOMER_FIELD_NUMBER: _ClassVar[int]
        BILLING_CORRECTION_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        BILLING_CORRECTION_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        BILLING_CORRECTION_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        COUPON_ADJUSTMENT_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        COUPON_ADJUSTMENT_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        COUPON_ADJUSTMENT_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXCESS_CREDIT_ADJUSTMENT_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXCESS_CREDIT_ADJUSTMENT_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXCESS_CREDIT_ADJUSTMENT_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        REGULATORY_COSTS_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        REGULATORY_COSTS_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        REGULATORY_COSTS_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXPORT_CHARGE_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXPORT_CHARGE_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        EXPORT_CHARGE_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        customer: str
        billing_correction_subtotal_amount_micros: int
        billing_correction_tax_amount_micros: int
        billing_correction_total_amount_micros: int
        coupon_adjustment_subtotal_amount_micros: int
        coupon_adjustment_tax_amount_micros: int
        coupon_adjustment_total_amount_micros: int
        excess_credit_adjustment_subtotal_amount_micros: int
        excess_credit_adjustment_tax_amount_micros: int
        excess_credit_adjustment_total_amount_micros: int
        regulatory_costs_subtotal_amount_micros: int
        regulatory_costs_tax_amount_micros: int
        regulatory_costs_total_amount_micros: int
        export_charge_subtotal_amount_micros: int
        export_charge_tax_amount_micros: int
        export_charge_total_amount_micros: int
        subtotal_amount_micros: int
        tax_amount_micros: int
        total_amount_micros: int
        def __init__(self, customer: _Optional[str] = ..., billing_correction_subtotal_amount_micros: _Optional[int] = ..., billing_correction_tax_amount_micros: _Optional[int] = ..., billing_correction_total_amount_micros: _Optional[int] = ..., coupon_adjustment_subtotal_amount_micros: _Optional[int] = ..., coupon_adjustment_tax_amount_micros: _Optional[int] = ..., coupon_adjustment_total_amount_micros: _Optional[int] = ..., excess_credit_adjustment_subtotal_amount_micros: _Optional[int] = ..., excess_credit_adjustment_tax_amount_micros: _Optional[int] = ..., excess_credit_adjustment_total_amount_micros: _Optional[int] = ..., regulatory_costs_subtotal_amount_micros: _Optional[int] = ..., regulatory_costs_tax_amount_micros: _Optional[int] = ..., regulatory_costs_total_amount_micros: _Optional[int] = ..., export_charge_subtotal_amount_micros: _Optional[int] = ..., export_charge_tax_amount_micros: _Optional[int] = ..., export_charge_total_amount_micros: _Optional[int] = ..., subtotal_amount_micros: _Optional[int] = ..., tax_amount_micros: _Optional[int] = ..., total_amount_micros: _Optional[int] = ...) -> None: ...
    class AccountBudgetSummary(_message.Message):
        __slots__ = ("customer", "customer_descriptive_name", "account_budget", "account_budget_name", "purchase_order_number", "subtotal_amount_micros", "tax_amount_micros", "total_amount_micros", "billable_activity_date_range", "served_amount_micros", "billed_amount_micros", "overdelivery_amount_micros", "invalid_activity_amount_micros", "invalid_activity_summaries")
        CUSTOMER_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_BUDGET_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_BUDGET_NAME_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        BILLABLE_ACTIVITY_DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
        SERVED_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        BILLED_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        OVERDELIVERY_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        INVALID_ACTIVITY_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        INVALID_ACTIVITY_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
        customer: str
        customer_descriptive_name: str
        account_budget: str
        account_budget_name: str
        purchase_order_number: str
        subtotal_amount_micros: int
        tax_amount_micros: int
        total_amount_micros: int
        billable_activity_date_range: _dates_pb2.DateRange
        served_amount_micros: int
        billed_amount_micros: int
        overdelivery_amount_micros: int
        invalid_activity_amount_micros: int
        invalid_activity_summaries: _containers.RepeatedCompositeFieldContainer[Invoice.InvalidActivitySummary]
        def __init__(self, customer: _Optional[str] = ..., customer_descriptive_name: _Optional[str] = ..., account_budget: _Optional[str] = ..., account_budget_name: _Optional[str] = ..., purchase_order_number: _Optional[str] = ..., subtotal_amount_micros: _Optional[int] = ..., tax_amount_micros: _Optional[int] = ..., total_amount_micros: _Optional[int] = ..., billable_activity_date_range: _Optional[_Union[_dates_pb2.DateRange, _Mapping]] = ..., served_amount_micros: _Optional[int] = ..., billed_amount_micros: _Optional[int] = ..., overdelivery_amount_micros: _Optional[int] = ..., invalid_activity_amount_micros: _Optional[int] = ..., invalid_activity_summaries: _Optional[_Iterable[_Union[Invoice.InvalidActivitySummary, _Mapping]]] = ...) -> None: ...
    class InvalidActivitySummary(_message.Message):
        __slots__ = ("original_month_of_service", "original_year_of_service", "original_invoice_id", "original_account_budget_name", "original_purchase_order_number", "amount_micros")
        ORIGINAL_MONTH_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_YEAR_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_ACCOUNT_BUDGET_NAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PURCHASE_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        original_month_of_service: _month_of_year_pb2.MonthOfYearEnum.MonthOfYear
        original_year_of_service: str
        original_invoice_id: str
        original_account_budget_name: str
        original_purchase_order_number: str
        amount_micros: int
        def __init__(self, original_month_of_service: _Optional[_Union[_month_of_year_pb2.MonthOfYearEnum.MonthOfYear, str]] = ..., original_year_of_service: _Optional[str] = ..., original_invoice_id: _Optional[str] = ..., original_account_budget_name: _Optional[str] = ..., original_purchase_order_number: _Optional[str] = ..., amount_micros: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BILLING_SETUP_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_DATE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENTS_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    REGULATORY_COSTS_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    REGULATORY_COSTS_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    REGULATORY_COSTS_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CHARGE_SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CHARGE_TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CHARGE_TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_INVOICE_FIELD_NUMBER: _ClassVar[int]
    REPLACED_INVOICES_FIELD_NUMBER: _ClassVar[int]
    PDF_URL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_BUDGET_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: str
    type: _invoice_type_pb2.InvoiceTypeEnum.InvoiceType
    billing_setup: str
    payments_account_id: str
    payments_profile_id: str
    issue_date: str
    due_date: str
    service_date_range: _dates_pb2.DateRange
    currency_code: str
    adjustments_subtotal_amount_micros: int
    adjustments_tax_amount_micros: int
    adjustments_total_amount_micros: int
    regulatory_costs_subtotal_amount_micros: int
    regulatory_costs_tax_amount_micros: int
    regulatory_costs_total_amount_micros: int
    export_charge_subtotal_amount_micros: int
    export_charge_tax_amount_micros: int
    export_charge_total_amount_micros: int
    subtotal_amount_micros: int
    tax_amount_micros: int
    total_amount_micros: int
    corrected_invoice: str
    replaced_invoices: _containers.RepeatedScalarFieldContainer[str]
    pdf_url: str
    account_budget_summaries: _containers.RepeatedCompositeFieldContainer[Invoice.AccountBudgetSummary]
    account_summaries: _containers.RepeatedCompositeFieldContainer[Invoice.AccountSummary]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[str] = ..., type: _Optional[_Union[_invoice_type_pb2.InvoiceTypeEnum.InvoiceType, str]] = ..., billing_setup: _Optional[str] = ..., payments_account_id: _Optional[str] = ..., payments_profile_id: _Optional[str] = ..., issue_date: _Optional[str] = ..., due_date: _Optional[str] = ..., service_date_range: _Optional[_Union[_dates_pb2.DateRange, _Mapping]] = ..., currency_code: _Optional[str] = ..., adjustments_subtotal_amount_micros: _Optional[int] = ..., adjustments_tax_amount_micros: _Optional[int] = ..., adjustments_total_amount_micros: _Optional[int] = ..., regulatory_costs_subtotal_amount_micros: _Optional[int] = ..., regulatory_costs_tax_amount_micros: _Optional[int] = ..., regulatory_costs_total_amount_micros: _Optional[int] = ..., export_charge_subtotal_amount_micros: _Optional[int] = ..., export_charge_tax_amount_micros: _Optional[int] = ..., export_charge_total_amount_micros: _Optional[int] = ..., subtotal_amount_micros: _Optional[int] = ..., tax_amount_micros: _Optional[int] = ..., total_amount_micros: _Optional[int] = ..., corrected_invoice: _Optional[str] = ..., replaced_invoices: _Optional[_Iterable[str]] = ..., pdf_url: _Optional[str] = ..., account_budget_summaries: _Optional[_Iterable[_Union[Invoice.AccountBudgetSummary, _Mapping]]] = ..., account_summaries: _Optional[_Iterable[_Union[Invoice.AccountSummary, _Mapping]]] = ...) -> None: ...
