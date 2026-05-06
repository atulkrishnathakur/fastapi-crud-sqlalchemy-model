from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer
from app.db.base import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    name: Mapped[str] = mapped_column('name', String(255)) # type argument is required like String
    email: Mapped[str] = mapped_column('email', String(255))
    password: Mapped[str] = mapped_column('password', String(255))
    mobile: Mapped[str] = mapped_column('mobile', String(255))
