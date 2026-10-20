"""Conexão com o banco de dados: engine assíncrona, sessão e dependency."""

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from api.configs.settings import settings

# Garante que os models estejam registrados no metadata do BaseModel.
# Sem este import, create_all roda com metadata vazia e não cria nada
# (silenciosamente) caso nada tenha importado api.models antes.
from api import models as _models  # noqa: F401
from api.shared.models import BaseModel

engine = create_async_engine(
    settings.database_url,
    echo=False,
)

# expire_on_commit=False evita que os atributos sejam recarregados
# de forma lazy ao acessá-los depois do commit (fora da sessão).
session_factory = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


async def get_session() -> AsyncIterator[AsyncSession]:
    """Dependency: entrega uma AsyncSession e garante o fechamento ao final."""
    async with session_factory() as session:
        yield session


async def init_db() -> None:
    """Cria as tabelas a partir dos models (dev/bootstrap).

    Em produção use Alembic: `alembic upgrade head`.
    """
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
