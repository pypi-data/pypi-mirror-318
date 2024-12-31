from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class AccountAutoFrozenAccountAutoFrozenDetailGocardless(BaseModel):
    """
    This creditor account has been automatically frozen and had restrictions applied.
    """

    origin: Literal["gocardless"]
    cause: Literal["account_auto_frozen"]
    description: str


AccountAutoFrozenAccountAutoFrozenDetail = (
    AccountAutoFrozenAccountAutoFrozenDetailGocardless
)


class UpdatedCreditorUpdatedDetailGocardless(BaseModel):
    """
    This creditor has been updated.
    """

    origin: Literal["gocardless"]
    cause: Literal["creditor_updated"]
    description: str


UpdatedCreditorUpdatedDetail = UpdatedCreditorUpdatedDetailGocardless


class AccountAutoFrozenRevertedAccountAutoFrozenRevertedDetailGocardless(BaseModel):
    """
    The restrictions on this creditor account have been removed.
    """

    origin: Literal["gocardless"]
    cause: Literal["account_auto_frozen_reverted"]
    description: str


AccountAutoFrozenRevertedAccountAutoFrozenRevertedDetail = (
    AccountAutoFrozenRevertedAccountAutoFrozenRevertedDetailGocardless
)


class BouncedPayoutBouncedPayoutDetailGocardless(BaseModel):
    """
    A payout for this creditor has failed. Please retry the payout or contact your bank for more information.
    """

    origin: Literal["gocardless"]
    cause: Literal["bounced_payout"]
    description: str


BouncedPayoutBouncedPayoutDetail = BouncedPayoutBouncedPayoutDetailGocardless


class NewPayoutCurrencyAddedNewPayoutCurrencyAddedDetailGocardless(BaseModel):
    """
    This creditor has added a new payout currency.
    """

    origin: Literal["gocardless"]
    cause: Literal["new_payout_currency_added"]
    description: str


NewPayoutCurrencyAddedNewPayoutCurrencyAddedDetail = (
    NewPayoutCurrencyAddedNewPayoutCurrencyAddedDetailGocardless
)


class CreditorAccountAutoFrozen(BaseModel):
    """
    This creditor account has been automatically frozen and had restrictions applied.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["creditors"]
    action: Literal["account_auto_frozen"]
    details: AccountAutoFrozenAccountAutoFrozenDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class CreditorUpdated(BaseModel):
    """
    Something has changed about this creditor. The property that has changed will be included in the event details. Currently this webhook is sent forlogo_urlverification_statusmandate_imports_enabledcustom_payment_pages_enabledandmerchant_responsible_for_notifications.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["creditors"]
    action: Literal["updated"]
    details: UpdatedCreditorUpdatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class CreditorAccountAutoFrozenReverted(BaseModel):
    """
    This creditor accounts restrictions have been removed.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["creditors"]
    action: Literal["account_auto_frozen_reverted"]
    details: AccountAutoFrozenRevertedAccountAutoFrozenRevertedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class CreditorBouncedPayout(BaseModel):
    """
    A payout for this creditor has failed. Please contact your bank for more information or retry the payout.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["creditors"]
    action: Literal["bounced_payout"]
    details: BouncedPayoutBouncedPayoutDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class CreditorNewPayoutCurrencyAdded(BaseModel):
    """
    This creditor has added a new payout currency.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["creditors"]
    action: Literal["new_payout_currency_added"]
    details: NewPayoutCurrencyAddedNewPayoutCurrencyAddedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


CreditorType = Annotated[
    CreditorAccountAutoFrozen
    | CreditorUpdated
    | CreditorAccountAutoFrozenReverted
    | CreditorBouncedPayout
    | CreditorNewPayoutCurrencyAdded,
    Field(..., discriminator="action"),
]
Creditor = RootModel[CreditorType]
