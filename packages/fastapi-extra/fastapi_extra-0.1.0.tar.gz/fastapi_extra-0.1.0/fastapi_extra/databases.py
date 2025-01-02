__author__ = "ziyan.yin"
__date__ = "2024-12-26"


from typing import Annotated, Any, Literal

from fastapi.params import Depends
from pydantic import AnyUrl, BaseModel
from sqlalchemy import Engine, NullPool
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession
from sqlalchemy.orm import Session as _Session
from sqlalchemy.util import _concurrency_py3k
from sqlmodel import create_engine

from fastapi_extra.settings import Settings


class DatabaseConfig(BaseModel):
    url: AnyUrl
    echo: bool = False
    echo_pool: bool = False
    isolation_level: Literal[
        "SERIALIZABLE",
        "REPEATABLE READ",
        "READ COMMITTED",
        "READ UNCOMMITTED",
        "AUTOCOMMIT",
    ] | None = None
    max_overflow: int = 10
    pool_pre_ping: bool = False
    pool_size: int = 5
    pool_recycle: int = -1
    pool_timeout: int = 30
    pool_use_lifo: bool = False
    query_cache_size: int = 500


class DatabaseSettings(Settings):
    datasources: dict[str, DatabaseConfig]
    

_settings = DatabaseSettings()  # type: ignore
_engines: dict[str, Engine] = {}


def load_engine(name: str = "default", **kw: Any) -> Engine:
    if name in _engines:
        return _engines[name]
    if name in _settings.datasources:
        config = _settings.datasources[name]
        _engines[name] = create_engine(
            url=str(config.url),
            **config.model_dump(exclude_defaults=True, exclude={"url"}), 
            **kw
        )
            
        return _engines[name]
        
    raise KeyError(f"cannot find datasources.{name}")


async def shutdown() -> None:
    for engine in _engines.values():
        await _concurrency_py3k.greenlet_spawn(engine.dispose)


class SessionFactory(Depends):
    __slots__ = ("engine", )
    datasource: str = "default"
    
    def __init__(self):
        super().__init__()
        if _settings.mode == "test":
            self.engine = load_engine(self.datasource, poolclass=NullPool)
        else:
            self.engine = load_engine(self.datasource)
        self.dependency = self

    def __call__(self):
        with _Session(self.engine) as session:
            yield session


class AsyncSessionFactory(SessionFactory):
    
    def __init__(self):
        super().__init__()
        self.engine = AsyncEngine(self.engine)
    
    async def __call__(self):
        async with _AsyncSession(self.engine) as session:
            yield session


AsyncSession = Annotated[_AsyncSession, AsyncSessionFactory()]
