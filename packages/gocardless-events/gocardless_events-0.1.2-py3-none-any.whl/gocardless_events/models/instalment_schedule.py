from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class ResumedInstalmentScheduleResumedDetailGocardless(BaseModel):
    """
    Instalment schedule has resumed
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_resumed"]
    description: str


ResumedInstalmentScheduleResumedDetail = (
    ResumedInstalmentScheduleResumedDetailGocardless
)


class CreationFailedInstalmentScheduleCreationFailedDetailApi(BaseModel):
    """
    Instalment schedule failed to be created
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_creation_failed"]
    description: str


CreationFailedInstalmentScheduleCreationFailedDetail = (
    CreationFailedInstalmentScheduleCreationFailedDetailApi
)


class ErroredInstalmentScheduleErroredDetailGocardless(BaseModel):
    """
    Instalment schedule has errored
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored"]
    description: str


ErroredInstalmentScheduleErroredDetail = (
    ErroredInstalmentScheduleErroredDetailGocardless
)


class ErroredInstalmentScheduleErroredLateDetailGocardless(BaseModel):
    """
    One or more payments in the instalment schedule has had a late failure
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_errored_late"]
    description: str


ErroredInstalmentScheduleErroredLateDetail = (
    ErroredInstalmentScheduleErroredLateDetailGocardless
)


class CompletedInstalmentScheduleCompletedDetailGocardless(BaseModel):
    """
    Instalment schedule has completed
    """

    origin: Literal["gocardless"]
    cause: Literal["instalment_schedule_completed"]
    description: str


CompletedInstalmentScheduleCompletedDetail = (
    CompletedInstalmentScheduleCompletedDetailGocardless
)


class CreatedInstalmentScheduleCreatedDetailApi(BaseModel):
    """
    Instalment schedule has been created via the API
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_created"]
    description: str


CreatedInstalmentScheduleCreatedDetail = CreatedInstalmentScheduleCreatedDetailApi


class CancelledInstalmentScheduleCancelledDetailApi(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["api"]
    cause: Literal["instalment_schedule_cancelled"]
    description: str


CancelledInstalmentScheduleCancelledDetail = (
    CancelledInstalmentScheduleCancelledDetailApi
)


class CancelledMandateCancelledDetailGocardless(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_cancelled"]
    description: str


CancelledMandateCancelledDetail = CancelledMandateCancelledDetailGocardless


class CancelledMandateFailedDetailGocardless(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_failed"]
    description: str


CancelledMandateFailedDetail = CancelledMandateFailedDetailGocardless


class CancelledMandateSuspendedByPayerDetailGocardless(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_suspended_by_payer"]
    description: str


CancelledMandateSuspendedByPayerDetail = (
    CancelledMandateSuspendedByPayerDetailGocardless
)


class CancelledMandateExpiredDetailGocardless(BaseModel):
    """
    Instalment schedule has been cancelled
    """

    origin: Literal["gocardless"]
    cause: Literal["mandate_expired"]
    description: str


CancelledMandateExpiredDetail = CancelledMandateExpiredDetailGocardless


class InstalmentScheduleResumed(BaseModel):
    """
    The instalment schedule has been rectified by remedying any failed payments.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["resumed"]
    details: ResumedInstalmentScheduleResumedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class InstalmentScheduleCreationFailed(BaseModel):
    """
    The instalment schedule failed to create due to validation errors when creating the payments. The errors will be included in the event payload.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["creation_failed"]
    details: CreationFailedInstalmentScheduleCreationFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class InstalmentScheduleErrored(BaseModel):
    """
    One or more instalments in this instalment schedule failed to collect successfully.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["errored"]
    details: Annotated[
        ErroredInstalmentScheduleErroredDetail
        | ErroredInstalmentScheduleErroredLateDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class InstalmentScheduleCompleted(BaseModel):
    """
    This instalment schedule has concluded. No further instalments will be collected.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["completed"]
    details: CompletedInstalmentScheduleCompletedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class InstalmentScheduleCreated(BaseModel):
    """
    The instalment schedule has been created.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["created"]
    details: CreatedInstalmentScheduleCreatedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class InstalmentScheduleCancelled(BaseModel):
    """
    The instalment schedule has been cancelled. Any pending payments have also been cancelled.
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["instalment_schedules"]
    action: Literal["cancelled"]
    details: Annotated[
        CancelledInstalmentScheduleCancelledDetail
        | CancelledMandateCancelledDetail
        | CancelledMandateFailedDetail
        | CancelledMandateSuspendedByPayerDetail
        | CancelledMandateExpiredDetail,
        Field(..., discriminator="cause"),
    ]
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


InstalmentScheduleType = Annotated[
    InstalmentScheduleResumed
    | InstalmentScheduleCreationFailed
    | InstalmentScheduleErrored
    | InstalmentScheduleCompleted
    | InstalmentScheduleCreated
    | InstalmentScheduleCancelled,
    Field(..., discriminator="action"),
]
InstalmentSchedule = RootModel[InstalmentScheduleType]
