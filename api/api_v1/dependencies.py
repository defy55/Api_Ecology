from typing import Annotated, Any, Dict, Optional, TypeVar, Union

from fastapi import Path, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select, delete, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class Dependencies:

    @staticmethod
    async def get_items(session: AsyncSession, model: Base):

        stmt = select(model).order_by(model.id)
        result: Result = await session.execute(stmt)
        products = result.scalars().all()
        return products

    # Read one
    @staticmethod
    async def get_item_to_param(
        session: AsyncSession, model: Base, name_param: Any, value: Any
    ):
        stmt = select(model).where(name_param == value)
        result: Result = await session.execute(stmt)
        item = result.scalar()
        if item is not None:
            return item

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Value {value} not found!",
        )

    @staticmethod
    async def find_one_or_none(
        session: AsyncSession, model: Any, **filter_by
    ) -> Optional[ModelType]:
        stmt = select(model).filter_by(**filter_by)
        result = await session.execute(stmt)
        return result.scalars().one_or_none()

    # Create
    @staticmethod
    async def create_item(
        session: AsyncSession,
        model: Base,
        value: Any,
    ):
        if isinstance(value, dict):
            create_data = value
            session.add(**create_data)
        else:
            create_data = model(**value.model_dump())
            session.add(create_data)
        await session.commit()
        # await session.refresh(product)
        return create_data

    # Update
    @staticmethod
    async def update_item(
        model: Base,
        update: Any,
        item_id: Any,
        session: AsyncSession,
        name_param: Any,
        partial: bool = False,
        partial_none: bool = True,
    ):
        item_data = await Dependencies.get_item_to_param(
            session=session, model=model, name_param=name_param, value=item_id
        )
        for name, value in update.model_dump(
            exclude_unset=partial, exclude_none=partial_none
        ).items():
            setattr(item_data, name, value)
        await session.commit()
        return item_data

    @staticmethod
    async def update(
        session: AsyncSession,
        model: Any,
        *where,
        data_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> Optional[ModelType]:
        if isinstance(data_in, dict):
            update_data = data_in
        else:
            update_data = data_in.model_dump(exclude_unset=True)

        stmt = update(model).where(*where).values(**update_data).returning(model)
        result = await session.execute(stmt)
        products = result.scalars().all()
        return products

    # Delete
    @staticmethod
    async def item_delete(
        model: Base,
        item_id: Any,
        name_param: Any,
        session: AsyncSession,
    ) -> None:
        stmt = (
            delete(model)
            .where(name_param == item_id)
            .returning(
                name_param,
            )
        )
        result: Result = await session.execute(stmt)

        item = result.all()
        if item:
            return await session.commit()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Value {item_id} not found!",
        )

    @staticmethod
    async def delete(session: AsyncSession, model, *filter, **filter_by) -> None:
        stmt = delete(model).filter(*filter).filter_by(**filter_by)
        await session.execute(stmt)
