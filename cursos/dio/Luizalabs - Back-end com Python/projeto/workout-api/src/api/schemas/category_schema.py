from datetime import datetime
from typing import Annotated

from pydantic import UUID4, Field

from api.shared.schemas import BaseSchema, ResponseSchema


class CategorySchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            title="Nome da categoria",
            examples=["Baseball"],
            max_length=10,
        ),
    ]


class CategoryAthleteSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            title="Nome da categoria",
            examples=["Baseball"],
            max_length=10,
        ),
    ]


class CategoryRequestSchema(CategorySchema):
    pass


class CategoryResponseSchema(CategorySchema, ResponseSchema):
    id: Annotated[UUID4, Field(title="Identificador da categoria")]
    created_at: Annotated[datetime, Field(title="Data de criação")]
