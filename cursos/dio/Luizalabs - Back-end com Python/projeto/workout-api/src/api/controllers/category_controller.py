import uuid
from datetime import datetime

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from api.configs.dependencies import DatabaseDependency
from api.models.category_model import CategoryModel
from api.schemas.category_schema import CategoryRequestSchema, CategoryResponseSchema

router = APIRouter()


@router.get(
    "/",
    summary="Consulta de todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoryResponseSchema],
)
async def index(db_session: DatabaseDependency) -> list[CategoryResponseSchema]:
    categories: list[CategoryResponseSchema] = (
        (await db_session.execute(select(CategoryModel))).scalars().all()
    )

    return categories


@router.get(
    "/{id}",
    summary="Consulta de uma categoria",
    status_code=status.HTTP_200_OK,
    response_model=CategoryResponseSchema,
)
async def show(id: UUID4, db_session: DatabaseDependency) -> CategoryResponseSchema:
    category: CategoryResponseSchema = (
        await db_session.execute(select(CategoryModel).filter_by(id=id))
    ).scalar_one()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada pelo id {id}",
        )

    return category


@router.post(
    "/",
    summary="Criar uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryResponseSchema,
)
async def create(
    db_session: DatabaseDependency, category_request: CategoryRequestSchema
) -> CategoryResponseSchema:

    category_response = CategoryResponseSchema(
        id=uuid.uuid4(), created_at=datetime.now(), **category_request.model_dump()
    )
    category_model = CategoryModel(**category_response.model_dump())
    db_session.add(category_model)
    await db_session.commit()

    return category_response
