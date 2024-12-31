from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class CustomerApprovalGrantedCustomerApprovalGrantedDetailCustomer(BaseModel):
    """
    The customer granted approval for this subscription
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_granted"]
    description: str


CustomerApprovalGrantedCustomerApprovalGrantedDetail = (
    CustomerApprovalGrantedCustomerApprovalGrantedDetailCustomer
)


class FinishedSubscriptionFinishedDetailGocardless(BaseModel):
    """
    The subscription has finished.
    """

    origin: Literal["gocardless"]
    cause: Literal["subscription_finished"]
    description: str


FinishedSubscriptionFinishedDetail = FinishedSubscriptionFinishedDetailGocardless


class ResumedSubscriptionResumedDetailApi(BaseModel):
    """
    The subscription was resumed.
    """

    origin: Literal["api"]
    cause: Literal["subscription_resumed"]
    description: str


class ResumedSubscriptionResumedDetailGocardless(BaseModel):
    """
    The subscription was resumed.
    """

    origin: Literal["gocardless"]
    cause: Literal["subscription_resumed"]
    description: str


ResumedSubscriptionResumedDetail = Annotated[
    ResumedSubscriptionResumedDetailApi | ResumedSubscriptionResumedDetailGocardless,
    Field(..., discriminator="origin"),
]


class AmendedSubscriptionAmendedDetailApi(BaseModel):
    """
    Subscription amount has been amended.
    """

    origin: Literal["api"]
    cause: Literal["subscription_amended"]
    description: str


AmendedSubscriptionAmendedDetail = AmendedSubscriptionAmendedDetailApi


class CustomerApprovalDeniedCustomerApprovalDeniedDetailCustomer(BaseModel):
    """
    The customer denied approval for this subscription
    """

    origin: Literal["customer"]
    cause: Literal["customer_approval_denied"]
    description: str


CustomerApprovalDeniedCustomerApprovalDeniedDetail = (
    CustomerApprovalDeniedCustomerApprovalDeniedDetailCustomer
)


class PausedSubscriptionPausedDetailApi(BaseModel):
    """
    The subscription has been paused.
    """

    origin: Literal["api"]
    cause: Literal["subscription_paused"]
    description: str


class PausedSubscriptionPausedDetailGocardless(BaseModel):
    """
    The subscription has been paused.
    """

    origin: Literal["gocardless"]
    cause: Literal["subscription_paused"]
    description: str


PausedSubscriptionPausedDetail = Annotated[
    PausedSubscriptionPausedDetailApi | PausedSubscriptionPausedDetailGocardless,
    Field(..., discriminator="origin"),
]


class ScheduledPauseCancelledScheduledPauseCancelledDetailApi(BaseModel):
    """
    An upcoming pause for this subscription has been cancelled.
    """

    origin: Literal["api"]
    cause: Literal["scheduled_pause_cancelled"]
    description: str


ScheduledPauseCancelledScheduledPauseCancelledDetail = (
    ScheduledPauseCancelledScheduledPauseCancelledDetailApi
)


class ScheduledPauseScheduledPauseDetailApi(BaseModel):
    """
    The subscription has been scheduled to be paused at a future date.
    """

    origin: Literal["api"]
    cause: Literal["scheduled_pause"]
    description: str


ScheduledPauseScheduledPauseDetail = ScheduledPauseScheduledPauseDetailApi


class CreatedSubscriptionCreatedDetailApi(BaseModel):
    """
    Subscription created via the API.
    """

    origin: Literal["api"]
    cause: Literal["subscription_created"]
    description: str


CreatedSubscriptionCreatedDetail = CreatedSubscriptionCreatedDetailApi


class PaymentCreatedPaymentCreatedDetailGocardless(BaseModel):
    """
    Payment created by a subscription.
    """

    origin: Literal["gocardless"]
    cause: Literal["payment_created"]
    description: str


PaymentCreatedPaymentCreatedDetail = PaymentCreatedPaymentCreatedDetailGocardless


class ScheduledResumeScheduledResumeDetailApi(BaseModel):
    """
    This paused subscription has been scheduled to be resumed at a future date.
    """

    origin: Literal["api"]
    cause: Literal["scheduled_resume"]
    description: str


ScheduledResumeScheduledResumeDetail = ScheduledResumeScheduledResumeDetailApi


class CancelledBankAccountClosedDetailBank(BaseModel):
    """
    This subscription was cancelled because the customer is deceased.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_closed"]
    scheme: str
    reason_code: str
    description: str


class CancelledBankAccountClosedDetailApi(BaseModel):
    """
    The mandate for this subscription was cancelled at your request.
    """

    origin: Literal["api"]
    cause: Literal["bank_account_closed"]
    description: str


CancelledBankAccountClosedDetail = Annotated[
    CancelledBankAccountClosedDetailBank | CancelledBankAccountClosedDetailApi,
    Field(..., discriminator="origin"),
]


class CancelledReturnOnOdfiRequestDetailBank(BaseModel):
    """
    This subscription has been cancelled because its mandate was cancelled.
    """

    origin: Literal["bank"]
    cause: Literal["return_on_odfi_request"]
    scheme: str
    reason_code: str
    description: str


CancelledReturnOnOdfiRequestDetail = CancelledReturnOnOdfiRequestDetailBank


class CancelledReferToPayerDetailBank(BaseModel):
    """
    This subscription has been cancelled because the bank details for its mandate are incorrect.
    """

    origin: Literal["bank"]
    cause: Literal["refer_to_payer"]
    scheme: str
    reason_code: str
    description: str


CancelledReferToPayerDetail = CancelledReferToPayerDetailBank


class CancelledMandateCancelledDetailBank(BaseModel):
    """
    This subscription was canceled because the customer cancelled the mandate at their bank.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


class CancelledMandateCancelledDetailApi(BaseModel):
    """
    The subscription was cancelled because its mandate was cancelled at your request.
    """

    origin: Literal["api"]
    cause: Literal["mandate_cancelled"]
    description: str


class CancelledMandateCancelledDetailGocardless(BaseModel):
    """
    The mandate for this subscription was cancelled at your request.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_cancelled"]
    scheme: str
    reason_code: str
    description: str


CancelledMandateCancelledDetail = Annotated[
    CancelledMandateCancelledDetailBank
    | CancelledMandateCancelledDetailApi
    | CancelledMandateCancelledDetailGocardless,
    Field(..., discriminator="origin"),
]


class CancelledInvalidBankDetailsDetailBank(BaseModel):
    """
    This subscription has been cancelled because the bank details for its mandate are incorrect.
    """

    origin: Literal["bank"]
    cause: Literal["invalid_bank_details"]
    scheme: str
    reason_code: str
    description: str


CancelledInvalidBankDetailsDetail = CancelledInvalidBankDetailsDetailBank


class CancelledDirectDebitNotEnabledDetailBank(BaseModel):
    """
    This subscription has been cancelled because the bank account it was going to be taken from does not support direct debit.
    """

    origin: Literal["bank"]
    cause: Literal["direct_debit_not_enabled"]
    scheme: str
    reason_code: str
    description: str


CancelledDirectDebitNotEnabledDetail = CancelledDirectDebitNotEnabledDetailBank


class CancelledAuthorisationDisputedDetailBank(BaseModel):
    """
    This subscription has been cancelled because the customer disputes authorising its mandate.
    """

    origin: Literal["bank"]
    cause: Literal["authorisation_disputed"]
    scheme: str
    reason_code: str
    description: str


CancelledAuthorisationDisputedDetail = CancelledAuthorisationDisputedDetailBank


class CancelledSubscriptionCancelledDetailApi(BaseModel):
    """
    The subscription has been cancelled at your request.
    """

    origin: Literal["api"]
    cause: Literal["subscription_cancelled"]
    description: str


CancelledSubscriptionCancelledDetail = CancelledSubscriptionCancelledDetailApi


class CancelledMandateExpiredDetailGocardless(BaseModel):
    """
    The subscription was cancelled because its mandate has expired.
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    description: str


CancelledMandateExpiredDetail = CancelledMandateExpiredDetailGocardless


class CancelledBankAccountTransferredDetailBank(BaseModel):
    """
    The mandate for this subscription was cancelled as the customer asked their bank to transfer the mandate to a new account but the bank has failed to send GoCardless the new bank details.
    """

    origin: Literal["bank"]
    cause: Literal["bank_account_transferred"]
    scheme: str
    reason_code: str
    description: str


CancelledBankAccountTransferredDetail = CancelledBankAccountTransferredDetailBank


class CancelledAccountBlockedForAnyFinancialTransactionDetailBank(BaseModel):
    """
    This subscription has been cancelled because the bank account for its mandate was blocked.
    """

    origin: Literal["bank"]
    cause: Literal["account_blocked_for_any_financial_transaction"]
    scheme: str
    reason_code: str
    description: str


CancelledAccountBlockedForAnyFinancialTransactionDetail = (
    CancelledAccountBlockedForAnyFinancialTransactionDetailBank
)


class CancelledPlanCancelledDetailApi(BaseModel):
    """
    The subscription has been cancelled because the associated plan was cancelled.
    """

    origin: Literal["api"]
    cause: Literal["plan_cancelled"]
    description: str


CancelledPlanCancelledDetail = CancelledPlanCancelledDetailApi


class CancelledPaymentStoppedDetailBank(BaseModel):
    """
    The subscription was cancelled because the payment was stopped by the payer or their bank.
    """

    origin: Literal["bank"]
    cause: Literal["payment_stopped"]
    scheme: str
    reason_code: str
    description: str


CancelledPaymentStoppedDetail = CancelledPaymentStoppedDetailBank


class CancelledOtherDetailBank(BaseModel):
    """
    An error was received from the banks while setting up the mandate for this subscription.
    """

    origin: Literal["bank"]
    cause: Literal["other"]
    scheme: str
    reason_code: str
    description: str


CancelledOtherDetail = CancelledOtherDetailBank


class CancelledMandateSuspendedByPayerDetailBank(BaseModel):
    """
    The subscription has been cancelled because its mandate was suspended by payer.
    """

    origin: Literal["bank"]
    cause: Literal["mandate_suspended_by_payer"]
    scheme: str
    reason_code: str
    description: str


CancelledMandateSuspendedByPayerDetail = CancelledMandateSuspendedByPayerDetailBank


class CancelledInitialOneOffPaymentFailedDetailGocardless(BaseModel):
    """
    This subscription has been cancelled because its mandate was cancelled.
    """

    origin: Literal["gocardless"]
    cause: Literal["initial_one_off_payment_failed"]
    description: str


CancelledInitialOneOffPaymentFailedDetail = (
    CancelledInitialOneOffPaymentFailedDetailGocardless
)


class SubscriptionCustomerApprovalGranted(BaseModel):
    """
    The subscription required additional approval from the customer before it could become active and that approval has been granted.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["customer_approval_granted"]
    details: CustomerApprovalGrantedCustomerApprovalGrantedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionFinished(BaseModel):
    """
    This subscription has finished. No further payments will be created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["finished"]
    details: FinishedSubscriptionFinishedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionResumed(BaseModel):
    """
    This subscription was resumed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["resumed"]
    details: ResumedSubscriptionResumedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionAmended(BaseModel):
    """
    The subscription amount has been changed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["amended"]
    details: AmendedSubscriptionAmendedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionCustomerApprovalDenied(BaseModel):
    """
    The subscription required additional approval from the customer before it could become active and that approval has been denied.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["customer_approval_denied"]
    details: CustomerApprovalDeniedCustomerApprovalDeniedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionPaused(BaseModel):
    """
    This subscription has been paused.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["paused"]
    details: PausedSubscriptionPausedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionScheduledPauseCancelled(BaseModel):
    """
    An upcoming pause for this subscription has been cancelled.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["scheduled_pause_cancelled"]
    details: ScheduledPauseCancelledScheduledPauseCancelledDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionScheduledPause(BaseModel):
    """
    This subscription has been scheduled to be paused at a future date.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["scheduled_pause"]
    details: ScheduledPauseScheduledPauseDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionCreated(BaseModel):
    """
    The subscription has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["created"]
    details: CreatedSubscriptionCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionPaymentCreated(BaseModel):
    """
    A payment has been created by this subscription.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["payment_created"]
    details: PaymentCreatedPaymentCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionScheduledResume(BaseModel):
    """
    This paused subscription has been scheduled to be resumed at a future date.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["scheduled_resume"]
    details: ScheduledResumeScheduledResumeDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class SubscriptionCancelled(BaseModel):
    """
    This subscription has been cancelled. No further payments will be created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["subscriptions"]
    action: Literal["cancelled"]
    details: Annotated[
        CancelledBankAccountClosedDetail
        | CancelledReturnOnOdfiRequestDetail
        | CancelledReferToPayerDetail
        | CancelledMandateCancelledDetail
        | CancelledInvalidBankDetailsDetail
        | CancelledDirectDebitNotEnabledDetail
        | CancelledAuthorisationDisputedDetail
        | CancelledSubscriptionCancelledDetail
        | CancelledMandateExpiredDetail
        | CancelledBankAccountTransferredDetail
        | CancelledAccountBlockedForAnyFinancialTransactionDetail
        | CancelledPlanCancelledDetail
        | CancelledPaymentStoppedDetail
        | CancelledOtherDetail
        | CancelledMandateSuspendedByPayerDetail
        | CancelledInitialOneOffPaymentFailedDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


SubscriptionType = Annotated[
    SubscriptionCustomerApprovalGranted
    | SubscriptionFinished
    | SubscriptionResumed
    | SubscriptionAmended
    | SubscriptionCustomerApprovalDenied
    | SubscriptionPaused
    | SubscriptionScheduledPauseCancelled
    | SubscriptionScheduledPause
    | SubscriptionCreated
    | SubscriptionPaymentCreated
    | SubscriptionScheduledResume
    | SubscriptionCancelled,
    Field(..., discriminator="action"),
]
Subscription = RootModel[SubscriptionType]
