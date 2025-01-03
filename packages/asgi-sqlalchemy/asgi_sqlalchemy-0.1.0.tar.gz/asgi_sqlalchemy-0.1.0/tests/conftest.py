"""Pytest common testing utilities."""

from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
import uvloop
from uvloop import EventLoopPolicy

from asgi_sqlalchemy.context import DatabaseContext


@pytest_asyncio.fixture
async def sqlite_database() -> AsyncGenerator[DatabaseContext]:
    """Provide a mock sqlite database."""
    async with DatabaseContext(
        "sqlite+aiosqlite:///:memory:",
        engine_kwargs={"pool_pre_ping": True},
        session_kwargs={"autoflush": False, "expire_on_commit": False},
    ) as db:
        yield db


@pytest.fixture(scope="session")
def event_loop_policy() -> EventLoopPolicy:
    """Set pytest event loop to uvloop."""
    return uvloop.EventLoopPolicy()
