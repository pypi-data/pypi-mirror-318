from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import AwareDatetime, BaseModel, Field, RootModel


class FailedExportFailedDetailGocardless(BaseModel):
    """
    Export failed
    """

    origin: Literal["gocardless"]
    cause: Literal["export_failed"]
    description: str


FailedExportFailedDetail = FailedExportFailedDetailGocardless


class CompletedExportCompletedDetailGocardless(BaseModel):
    """
    Export completed
    """

    origin: Literal["gocardless"]
    cause: Literal["export_completed"]
    description: str


CompletedExportCompletedDetail = CompletedExportCompletedDetailGocardless


class StartedExportStartedDetailGocardless(BaseModel):
    """
    Export started
    """

    origin: Literal["gocardless"]
    cause: Literal["export_started"]
    description: str


StartedExportStartedDetail = StartedExportStartedDetailGocardless


class ExportFailed(BaseModel):
    """
    Export failed
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["failed"]
    details: FailedExportFailedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class ExportCompleted(BaseModel):
    """
    Export completed
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["completed"]
    details: CompletedExportCompletedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


class ExportStarted(BaseModel):
    """
    Export started
    """

    id: str
    created_at: AwareDatetime
    resource_type: Literal["exports"]
    action: Literal["started"]
    details: StartedExportStartedDetail
    metadata: dict[str, Any]
    resource_metadata: dict[str, Any] | None = None
    links: dict[str, Any]


ExportType = Annotated[
    ExportFailed | ExportCompleted | ExportStarted, Field(..., discriminator="action")
]
Export = RootModel[ExportType]
