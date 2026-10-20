from fastapi import APIRouter

from api.controllers import athlete_router, category_router, training_center_router

api_router = APIRouter()

api_router.include_router(
    athlete_router,
    prefix="/athletes",
    tags=["athletes"],
)
api_router.include_router(
    category_router,
    prefix="/categories",
    tags=["category"],
)
api_router.include_router(
    training_center_router,
    prefix="/training_center",
    tags=["training center"],
)
