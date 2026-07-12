from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Business(Base):

    __tablename__ = "businesses"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )


    osm_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )


    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )


    industry: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )


    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )


    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )


    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    phone: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    whatsapp: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    has_whatsapp: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
    )


    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )


    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )


    source: Mapped[str] = mapped_column(
        String(100),
        default="OpenStreetMap",
        nullable=False,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


    def __repr__(self) -> str:

        return (
            f"<Business("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"city='{self.city}', "
            f"industry='{self.industry}'"
            f")>"
        )