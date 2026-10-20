"""Configurações da aplicação (lidas de variáveis de ambiente/.env)."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Driver assíncrono (aiosqlite) para a aplicação.
    # O Alembic é síncrono e usa `sqlite+pysqlite` no alembic.ini —
    # mesmo arquivo de banco, drivers diferentes.
    database_url: str = Field(default="sqlite+aiosqlite:///./workout.db")


settings = Settings()
