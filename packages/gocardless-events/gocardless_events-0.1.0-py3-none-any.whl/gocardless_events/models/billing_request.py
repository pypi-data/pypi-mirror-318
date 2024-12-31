from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class ChooseCurrencyBillingRequestChooseCurrencyDetailApi(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_choose_currency"]
    description: str


class ChooseCurrencyBillingRequestChooseCurrencyDetailPayer(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_choose_currency"]
    description: str


ChooseCurrencyBillingRequestChooseCurrencyDetail = Annotated[
    ChooseCurrencyBillingRequestChooseCurrencyDetailApi
    | ChooseCurrencyBillingRequestChooseCurrencyDetailPayer,
    Field(..., discriminator="origin"),
]


class FulfilledBillingRequestFulfilledDetailGocardless(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_fulfilled"]
    description: str


class FulfilledBillingRequestFulfilledDetailApi(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_fulfilled"]
    description: str


FulfilledBillingRequestFulfilledDetail = Annotated[
    FulfilledBillingRequestFulfilledDetailGocardless
    | FulfilledBillingRequestFulfilledDetailApi,
    Field(..., discriminator="origin"),
]


class BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetailPayer(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


class BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetailGocardless(
    BaseModel
):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_authorised"]
    description: str


BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail = Annotated[
    BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetailPayer
    | BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetailGocardless,
    Field(..., discriminator="origin"),
]


class FlowVisitedBillingRequestFlowVisitedDetailPayer(BaseModel):
    """
    The billing request flow has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_visited"]
    description: str


FlowVisitedBillingRequestFlowVisitedDetail = (
    FlowVisitedBillingRequestFlowVisitedDetailPayer
)


class FailedBillingRequestFailedDetailGocardless(BaseModel):
    """
    This billing request has failed.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_failed"]
    description: str


class FailedBillingRequestFailedDetailApi(BaseModel):
    """
    This billing request has failed.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_failed"]
    description: str


FailedBillingRequestFailedDetail = Annotated[
    FailedBillingRequestFailedDetailGocardless | FailedBillingRequestFailedDetailApi,
    Field(..., discriminator="origin"),
]


class CollectBankAccountBillingRequestCollectBankAccountDetailApi(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


class CollectBankAccountBillingRequestCollectBankAccountDetailPayer(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_bank_account"]
    description: str


CollectBankAccountBillingRequestCollectBankAccountDetail = Annotated[
    CollectBankAccountBillingRequestCollectBankAccountDetailApi
    | CollectBankAccountBillingRequestCollectBankAccountDetailPayer,
    Field(..., discriminator="origin"),
]


class PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetailApi(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


class PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetailPayer(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_payer_details_confirmed"]
    description: str


PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail = Annotated[
    PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetailApi
    | PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetailPayer,
    Field(..., discriminator="origin"),
]


class CollectAmountBillingRequestCollectAmountDetailPayer(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_amount"]
    description: str


CollectAmountBillingRequestCollectAmountDetail = (
    CollectAmountBillingRequestCollectAmountDetailPayer
)


class BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetailPayer(
    BaseModel
):
    """
    A bank authorisation for this billing request has expired.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_expired"]
    description: str


BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail = (
    BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetailPayer
)


class FlowExitedBillingRequestFlowExitedDetailPayer(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_exited"]
    description: str


FlowExitedBillingRequestFlowExitedDetail = FlowExitedBillingRequestFlowExitedDetailPayer


class CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetailApi(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


class CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetailPayer(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_collect_customer_details"]
    description: str


CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail = Annotated[
    CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetailApi
    | CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetailPayer,
    Field(..., discriminator="origin"),
]


class CreatedBillingRequestCreatedDetailGocardless(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_created"]
    description: str


class CreatedBillingRequestCreatedDetailApi(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_created"]
    description: str


class CreatedBillingRequestCreatedDetailPayer(BaseModel):
    """
    This billing request has been created.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_created"]
    description: str


CreatedBillingRequestCreatedDetail = Annotated[
    CreatedBillingRequestCreatedDetailGocardless
    | CreatedBillingRequestCreatedDetailApi
    | CreatedBillingRequestCreatedDetailPayer,
    Field(..., discriminator="origin"),
]


class BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetailPayer(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


class BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetailGocardless(
    BaseModel
):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_failed"]
    description: str


BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail = Annotated[
    BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetailPayer
    | BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetailGocardless,
    Field(..., discriminator="origin"),
]


class PayerGeoBlockedPayerGeoBlockedDetailPayer(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    origin: Literal["payer"]
    cause: Literal["payer_geo_blocked"]
    description: str


PayerGeoBlockedPayerGeoBlockedDetail = PayerGeoBlockedPayerGeoBlockedDetailPayer


class FlowCreatedBillingRequestFlowCreatedDetailGocardless(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_flow_created"]
    description: str


class FlowCreatedBillingRequestFlowCreatedDetailApi(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_flow_created"]
    description: str


class FlowCreatedBillingRequestFlowCreatedDetailPayer(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_flow_created"]
    description: str


FlowCreatedBillingRequestFlowCreatedDetail = Annotated[
    FlowCreatedBillingRequestFlowCreatedDetailGocardless
    | FlowCreatedBillingRequestFlowCreatedDetailApi
    | FlowCreatedBillingRequestFlowCreatedDetailPayer,
    Field(..., discriminator="origin"),
]


class BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetailPayer(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


class BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetailGocardless(
    BaseModel
):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_bank_authorisation_denied"]
    description: str


BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail = Annotated[
    BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetailPayer
    | BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetailGocardless,
    Field(..., discriminator="origin"),
]


class SelectInstitutionBillingRequestSelectInstitutionDetailPayer(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_select_institution"]
    description: str


SelectInstitutionBillingRequestSelectInstitutionDetail = (
    SelectInstitutionBillingRequestSelectInstitutionDetailPayer
)


class BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetailPayer(
    BaseModel
):
    """
    A bank authorisation link for this billing request has been visited.
    """

    origin: Literal["payer"]
    cause: Literal["billing_request_bank_authorisation_visited"]
    description: str


BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail = (
    BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetailPayer
)


class CancelledBillingRequestCancelledDetailGocardless(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    origin: Literal["gocardless"]
    cause: Literal["billing_request_cancelled"]
    description: str


class CancelledBillingRequestCancelledDetailApi(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    origin: Literal["api"]
    cause: Literal["billing_request_cancelled"]
    description: str


CancelledBillingRequestCancelledDetail = Annotated[
    CancelledBillingRequestCancelledDetailGocardless
    | CancelledBillingRequestCancelledDetailApi,
    Field(..., discriminator="origin"),
]


class BillingRequestChooseCurrency(BaseModel):
    """
    Currency details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["choose_currency"]
    details: ChooseCurrencyBillingRequestChooseCurrencyDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFulfilled(BaseModel):
    """
    This billing request has been fulfilled and the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["fulfilled"]
    details: FulfilledBillingRequestFulfilledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationAuthorised(BaseModel):
    """
    A bank authorisation for this billing request has been authorised by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_authorised"]
    details: BankAuthorisationAuthorisedBillingRequestBankAuthorisationAuthorisedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowVisited(BaseModel):
    """
    The billing request flow has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_visited"]
    details: FlowVisitedBillingRequestFlowVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFailed(BaseModel):
    """
    This billing request has failed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["failed"]
    details: FailedBillingRequestFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectBankAccount(BaseModel):
    """
    Bank account details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_bank_account"]
    details: CollectBankAccountBillingRequestCollectBankAccountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestPayerDetailsConfirmed(BaseModel):
    """
    Payer has confirmed all their details for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_details_confirmed"]
    details: PayerDetailsConfirmedBillingRequestPayerDetailsConfirmedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectAmount(BaseModel):
    """
    Amount has been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_amount"]
    details: CollectAmountBillingRequestCollectAmountDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationExpired(BaseModel):
    """
    A bank authorisation for this billing request has expired.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_expired"]
    details: BankAuthorisationExpiredBillingRequestBankAuthorisationExpiredDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowExited(BaseModel):
    """
    The billing request flow has been exited by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_exited"]
    details: FlowExitedBillingRequestFlowExitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCollectCustomerDetails(BaseModel):
    """
    Customer details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["collect_customer_details"]
    details: CollectCustomerDetailsBillingRequestCollectCustomerDetailsDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCreated(BaseModel):
    """
    This billing request has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["created"]
    details: CreatedBillingRequestCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationFailed(BaseModel):
    """
    A bank authorisation for this billing request has failed because of a bank account mismatch.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_failed"]
    details: BankAuthorisationFailedBillingRequestBankAuthorisationFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestPayerGeoBlocked(BaseModel):
    """
    Payer blocked for 24 hours for attempting to pay from an unsupported location.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["payer_geo_blocked"]
    details: PayerGeoBlockedPayerGeoBlockedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestFlowCreated(BaseModel):
    """
    A billing request flow has been created against this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["flow_created"]
    details: FlowCreatedBillingRequestFlowCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationDenied(BaseModel):
    """
    A bank authorisation for this billing request has been denied by the payer.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_denied"]
    details: BankAuthorisationDeniedBillingRequestBankAuthorisationDeniedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestSelectInstitution(BaseModel):
    """
    Institution details have been collected for this billing request.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["select_institution"]
    details: SelectInstitutionBillingRequestSelectInstitutionDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestBankAuthorisationVisited(BaseModel):
    """
    A bank authorisation link for this billing request has been visited.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["bank_authorisation_visited"]
    details: BankAuthorisationVisitedBillingRequestBankAuthorisationVisitedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class BillingRequestCancelled(BaseModel):
    """
    This billing request has been cancelled none of the resources have been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["billing_requests"]
    action: Literal["cancelled"]
    details: CancelledBillingRequestCancelledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


BillingRequestType = Annotated[
    BillingRequestChooseCurrency
    | BillingRequestFulfilled
    | BillingRequestBankAuthorisationAuthorised
    | BillingRequestFlowVisited
    | BillingRequestFailed
    | BillingRequestCollectBankAccount
    | BillingRequestPayerDetailsConfirmed
    | BillingRequestCollectAmount
    | BillingRequestBankAuthorisationExpired
    | BillingRequestFlowExited
    | BillingRequestCollectCustomerDetails
    | BillingRequestCreated
    | BillingRequestBankAuthorisationFailed
    | BillingRequestPayerGeoBlocked
    | BillingRequestFlowCreated
    | BillingRequestBankAuthorisationDenied
    | BillingRequestSelectInstitution
    | BillingRequestBankAuthorisationVisited
    | BillingRequestCancelled,
    Field(..., discriminator="action"),
]
BillingRequest = RootModel[BillingRequestType]
