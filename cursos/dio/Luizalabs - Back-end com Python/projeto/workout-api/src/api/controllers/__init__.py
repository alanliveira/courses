from .athlete_controller import router as athlete_router
from .category_controller import router as category_router
from .training_center_controller import router as training_center_router

__all__ = ["athlete_router", "category_router", "training_center_router"]
