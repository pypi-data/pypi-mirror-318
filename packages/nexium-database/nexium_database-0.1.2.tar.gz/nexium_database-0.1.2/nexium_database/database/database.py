from typing import Type

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel


class Database:
    def __init__(self, url: str, models: list[Type[SQLModel]]) -> None:
        self.engine = create_async_engine(
            url=url,
            pool_pre_ping=True,
        )
        self.models = models
        self.session = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def get_session(self):
        async with self.session() as session:
            yield session

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
