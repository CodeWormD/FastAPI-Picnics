from fastapi import APIRouter

from .city.router import router as city_router


router = APIRouter(
    prefix='/api'
)

router.include_router(city_router)
