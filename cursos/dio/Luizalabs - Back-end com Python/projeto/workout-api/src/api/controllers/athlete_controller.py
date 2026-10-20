import uuid
from datetime import datetime

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from api.configs.dependencies import DatabaseDependency
from api.models.athlete_model import AthleteModel
from api.models.category_model import CategoryModel
from api.models.training_center_model import TrainingCenterModel
from api.schemas.athlete_schema import (
    AthleteRequestSchema,
    AthleteResponseSchema,
    AthleteUpdateRequestSchema,
)

router = APIRouter()


@router.get(
    "/",
    summary="Consulta de todos os atletas cadastrados",
    status_code=status.HTTP_200_OK,
    response_model=list[AthleteResponseSchema],
)
async def index(db_session: DatabaseDependency) -> list[AthleteResponseSchema]:
    athletes: list[AthleteResponseSchema] = (
        (await db_session.execute(select(AthleteModel))).scalars().all()
    )

    return [AthleteResponseSchema.model_validate(athlete) for athlete in athletes]


@router.get(
    "/{id}",
    summary="Visualização do cadastro do atleta",
    status_code=status.HTTP_200_OK,
    response_model=AthleteResponseSchema,
)
async def show(id: UUID4, db_session: DatabaseDependency) -> AthleteResponseSchema:
    athlete: AthleteResponseSchema = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalar_one_or_none()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id do Atleta não encontrado!"
        )

    return athlete


@router.post(
    "/",
    summary="Criar um novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AthleteResponseSchema,
)
async def post(
    db_session: DatabaseDependency, athlete_request: AthleteRequestSchema = Body(...)
):
    category: CategoryModel = (
        await db_session.execute(
            select(CategoryModel).filter_by(name=athlete_request.category.name)
        )
    ).scalar_one_or_none()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Categoria {athlete_request.category.name} não foi encontrada!",
        )

    training_center: TrainingCenterModel = (
        await db_session.execute(
            select(TrainingCenterModel).filter_by(
                name=athlete_request.training_center.name
            )
        )
    ).scalar_one_or_none()

    if not training_center:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O centro de treinamento {athlete_request.training_center.name} não foi encontrado!",
        )

    try:
        athlete_response: AthleteResponseSchema = AthleteResponseSchema(
            id=uuid.uuid4(),
            created_at=datetime.utcnow(),
            **athlete_request.model_dump(),
        )

        athlete_model: AthleteModel = AthleteModel(
            **athlete_response.model_dump(exclude=("category", "training_center"))
        )

        athlete_model.category_id = category.pk_id
        athlete_model.training_center_id = training_center.pk_id

        db_session.add(athlete_model)
        await db_session.commit()
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro ao inserir os dados no banco\n{exc.args}",
        )

    return athlete_response


@router.patch(
    "/{id}",
    summary="Editar um atleta com base no id",
    status_code=status.HTTP_200_OK,
    response_model=AthleteResponseSchema,
)
async def update(
    id: UUID4,
    db_session: DatabaseDependency,
    athlete_request: AthleteUpdateRequestSchema,
) -> AthleteResponseSchema:
    athlete: AthleteResponseSchema = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalar_one_or_none()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id do Atleta não encontrado"
        )

    athlete_update = athlete_request.model_dump(exclude_unset=True)

    for key, value in athlete_update.items():
        setattr(athlete, key, value)

    await db_session.commit()
    await db_session.refresh(athlete)

    return athlete


@router.delete(
    "/{id}",
    summary="Deletar um atleta pelo seu ID",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete = (
        await db_session.execute(select(AthleteModel).filter_by(id=id))
    ).scalar_one_or_none()

    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id do atleta não encontrado"
        )

    await db_session.delete(athlete)
    await db_session.commit()

    return None
