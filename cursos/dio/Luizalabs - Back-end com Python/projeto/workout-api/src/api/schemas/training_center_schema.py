from datetime import datetime
from typing import Annotated

from pydantic import UUID4, Field

from api.shared.schemas import BaseSchema, ResponseSchema


class TrainingCenterSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            title="Nome do centro de treinamento",
            examples=["Super Ball's 2"],
            max_length=50,
        ),
    ]
    address: Annotated[
        str,
        Field(
            title="Endereço do centro de treinamento",
            examples=["Rua do grau, 22, vila velha nova, São Paulo/SP"],
            max_length=60,
        ),
    ]
    owner: Annotated[
        str,
        Field(
            title="Nome do proprietário",
            examples=["José"],
            max_length=30,
        ),
    ]


class TrainingCenterAthleteSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            title="Nome do centro de treinamento",
            examples=["Super Ball's 2"],
            max_length=50,
        ),
    ]


class TrainingCenterRequestSchema(TrainingCenterSchema):
    pass


class TrainingCenterResponseSchema(TrainingCenterSchema, ResponseSchema):
    id: Annotated[UUID4, Field(title="Identificador do centro de treinamento")]
    created_at: Annotated[datetime, Field(title="Data de criação")]
