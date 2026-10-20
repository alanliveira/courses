from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from api.configs.dependencies import DatabaseDependency
from api.models.training_center_model import TrainingCenterModel
from api.schemas.training_center_schema import (
    TrainingCenterRequestSchema,
    TrainingCenterResponseSchema,
)

router = APIRouter()


@router.get(
    "/",
    summary="",
    status_code=status.HTTP_200_OK,
    response_model=list[TrainingCenterResponseSchema],
)
async def index(db_session: DatabaseDependency) -> list[TrainingCenterResponseSchema]:
    training_centers: list[TrainingCenterResponseSchema] = (
        (await db_session.execute(select(TrainingCenterModel))).scalars().all()
    )

    return training_centers


@router.get(
    "/{id}",
    summary="Listar os centro de treinamentos",
    status_code=status.HTTP_200_OK,
    response_model=TrainingCenterResponseSchema,
)
async def show(
    id: UUID4, db_session: DatabaseDependency
) -> TrainingCenterResponseSchema:
    training_center: TrainingCenterResponseSchema = (
        await db_session.execute(select(TrainingCenterModel).filter_by(id=id))
    ).scalar_one()

    if not training_center:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID de centro de treinamento não encontrado",
        )

    return training_center


@router.post(
    "/",
    summary="Criar um novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=TrainingCenterResponseSchema,
)
async def create(
    db_session: DatabaseDependency, training_center_request: TrainingCenterRequestSchema
) -> TrainingCenterResponseSchema:
    training_center_response = TrainingCenterResponseSchema(
        id=uuid4(), created_at=datetime.now(), **training_center_request.model_dump()
    )
    training_center_model = TrainingCenterModel(**training_center_response.model_dump())
    db_session.add(training_center_model)
    await db_session.commit()

    return training_center_model
