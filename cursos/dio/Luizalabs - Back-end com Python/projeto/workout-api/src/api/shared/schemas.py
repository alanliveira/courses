from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )


class ResponseSchema(BaseModel):
    id: UUID
    created_at: datetime
