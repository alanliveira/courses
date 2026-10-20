from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.shared.models import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "categories"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)

    athletes: Mapped[list["AthleteModel"]] = relationship(back_populates="category")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
