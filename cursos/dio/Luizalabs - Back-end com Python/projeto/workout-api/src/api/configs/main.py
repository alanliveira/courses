from fastapi import FastAPI

from api.configs.routes import api_router

app = FastAPI(title="Workout API")

app.include_router(api_router)
