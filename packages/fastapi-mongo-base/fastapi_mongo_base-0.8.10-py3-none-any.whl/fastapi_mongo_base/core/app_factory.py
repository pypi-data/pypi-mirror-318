import asyncio
import logging
from collections import deque
from contextlib import asynccontextmanager

import fastapi
from fastapi.middleware.cors import CORSMiddleware

from fastapi_mongo_base.core import db, exceptions

try:
    from server.config import Settings
except ImportError:
    from .config import Settings


async def health(request: fastapi.Request):
    return {
        "status": "up",
        "host": request.url.hostname,
        # "host2": request.base_url.hostname,
        # "original_host":request.headers.get("x-original-host", "!not found!"),
        # "forwarded_host": request.headers.get("X-Forwarded-Host", "forwarded_host"),
        # "forwarded_proto": request.headers.get("X-Forwarded-Proto", "forwarded_proto"),
        # "forwarded_for": request.headers.get("X-Forwarded-For", "forwarded_for"),
    }


async def logs():
    with open(Settings.base_dir / "logs" / "info.log", "rb") as f:
        last_100_lines = deque(f, maxlen=100)

    return [line.decode("utf-8") for line in last_100_lines]


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI, worker=None, init_functions=[]):  # type: ignore
    """Initialize application services."""
    Settings().config_logger()
    await db.init_mongo_db()

    if worker:
        app.state.worker = asyncio.create_task(worker())

    for function in init_functions:
        if asyncio.iscoroutinefunction(function):
            await function()
        else:
            function()

    logging.info("Startup complete")
    yield
    app.state.worker.cancel()
    logging.info("Shutdown complete")


def create_app(
    title=Settings.project_name.replace("-", " ").title(),
    description=None,
    version="0.1.0",
    origins: list = None,
    lifespan_func=None,
    worker=None,
    init_functions: list = [],
    contact={
        "name": "Mahdi Kiani",
        "url": "https://github.com/mahdikiani/FastAPILaunchpad",
        "email": "mahdikiany@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/mahdikiani/FastAPILaunchpad/blob/main/LICENSE",
    },
    usso_handler: bool = True,
    ufaas_handler: bool = True,
    original_host_middleware: bool = False,
    request_log_middleware: bool = False,
    docs_url=f"{Settings.base_path}/docs",
    openapi_url=f"{Settings.base_path}/openapi.json",
) -> fastapi.FastAPI:
    """Create a FastAPI app with shared configurations."""
    if origins is None:
        origins = ["http://localhost:8000"]

    if lifespan_func is None:
        lifespan_func = lambda app: lifespan(app, worker, init_functions)

    app = fastapi.FastAPI(
        title=title,
        version=version,
        description=description,
        lifespan=lifespan_func,
        contact=contact,
        license_info=license_info,
        docs_url=docs_url,
        openapi_url=openapi_url,
    )

    exception_handlers = exceptions.EXCEPTION_HANDLERS
    if usso_handler:
        from usso.fastapi.integration import (
            EXCEPTION_HANDLERS as USSO_EXCEPTION_HANDLERS,
        )

        exception_handlers.update(USSO_EXCEPTION_HANDLERS)
    if ufaas_handler:
        from ufaas.fastapi.integration import (
            EXCEPTION_HANDLERS as UFAAS_EXCEPTION_HANDLERS,
        )

        exception_handlers.update(UFAAS_EXCEPTION_HANDLERS)

    for exc_class, handler in exception_handlers.items():
        app.exception_handler(exc_class)(handler)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if original_host_middleware:
        from ufaas_fastapi_business.core.middlewares import OriginalHostMiddleware

        app.add_middleware(OriginalHostMiddleware)
    if request_log_middleware:
        from .middlewares import RequestLoggingMiddleware

        app.add_middleware(RequestLoggingMiddleware)

    app.add_route(f"{Settings.base_path}/health", health)
    app.add_route(f"{Settings.base_path}/logs", logs, include_in_schema=False)

    return app
