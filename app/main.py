from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.config import get_config
from app.exception import AppException

from app.routers import common, user_account


config = get_config()

app = FastAPI(prefix=config.url_prefix, title=config.app_name)

@app.exception_handler(AppException)
async def unicorn_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.error_code,
        content={"error": exc.message},
    )


app.include_router(common.router)
app.include_router(user_account.router)
