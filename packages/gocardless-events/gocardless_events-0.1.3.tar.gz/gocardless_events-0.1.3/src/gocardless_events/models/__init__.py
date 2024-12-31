from typing import Annotated

from pydantic import Field, RootModel

from .billing_request import BillingRequest
from .creditor import Creditor
from .export import Export
from .instalment_schedule import InstalmentSchedule
from .mandate import Mandate
from .payer_authorization import PayerAuthorization
from .payment import Payment
from .payout import Payout
from .refund import Refund
from .scheme_identifier import SchemeIdentifier
from .subscription import Subscription

EventType = Annotated[
    SchemeIdentifier
    | PayerAuthorization
    | Payment
    | Creditor
    | Mandate
    | Subscription
    | BillingRequest
    | Export
    | InstalmentSchedule
    | Refund
    | Payout,
    Field(..., discriminator="resource_type"),
]

Event = RootModel[EventType]

__all__ = [
    "BillingRequest",
    "Creditor",
    "Event",
    "Export",
    "InstalmentSchedule",
    "Mandate",
    "PayerAuthorization",
    "Payment",
    "Payout",
    "Refund",
    "SchemeIdentifier",
    "Subscription",
]
