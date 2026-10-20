from datetime import datetime
from typing import Annotated, Optional

from pydantic import UUID4, Field, PositiveFloat

from api.schemas.category_schema import CategoryAthleteSchema
from api.schemas.training_center_schema import TrainingCenterAthleteSchema
from api.shared.schemas import BaseSchema, ResponseSchema


class AthleteSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            title="Nome do atleta",
            examples=["João"],
            max_length=50,
        ),
    ]
    cpf: Annotated[
        str,
        Field(
            title="CPF do atleta",
            examples=["12345678901"],
            max_length=11,
        ),
    ]
    age: Annotated[
        int,
        Field(
            title="Idade do atleta",
            examples=[42],
        ),
    ]
    weight: Annotated[
        PositiveFloat,
        Field(
            title="Peso do atleta",
            examples=[67.42],
        ),
    ]
    height: Annotated[
        PositiveFloat,
        Field(
            title="Altura do atleta",
            examples=[1.8],
        ),
    ]
    gender: Annotated[
        str,
        Field(
            title="Sexo do atleta",
            examples=["M"],
            max_length=1,
        ),
    ]
    category: Annotated[
        CategoryAthleteSchema,
        Field(description="Categoria do atheta"),
    ]
    training_center: Annotated[
        TrainingCenterAthleteSchema,
        Field(description="Centro de treinamento do Atleta"),
    ]


class AthleteUpdateRequestSchema(BaseSchema):
    name: Annotated[
        Optional[str],
        Field(
            None,
            title="Nome do atleta",
            examples=["João"],
            max_length=50,
        ),
    ]
    age: Annotated[
        Optional[int],
        Field(
            None,
            title="Idade do atleta",
            examples=[42],
        ),
    ]


class AthleteRequestSchema(AthleteSchema):
    pass


class AthleteResponseSchema(AthleteSchema, ResponseSchema):
    id: Annotated[UUID4, Field(title="Identificador do atleta")]
    created_at: Annotated[datetime, Field(title="Data de criação")]
