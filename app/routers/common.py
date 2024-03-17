from fastapi import APIRouter

from app.config import get_config


config = get_config()

router = APIRouter(tags=["Common"])


@router.get("/version")
def get_version():
    return {"version": config.version}

@router.get("/")
def healthcheck():
    return {"message": "Happy"}
