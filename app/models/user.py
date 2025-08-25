from datetime import datetime
from sqlalchemy import TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.datasources.database import Base
from typing import Annotated
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)


class AccessRole(enum.Enum):
    USER = "user"
    ADMIN = "admin"


class UserInfoModel(Base):
    __tablename__ = "user_info"

    id: Mapped[intpk]
    access_role: Mapped[AccessRole]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
