import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

# from sqlalchemy.dialects.postgresql import UUID


class Base(DeclarativeBase):
    __abstract__ = True

    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return f"{cls.__name__.lower()}s"

    # id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4
    )
    # id: Mapped[uuid.UUID] = mapped_column(
    #     uuid.UUID, primary_key=True, index=True, default=uuid.uuid4)
