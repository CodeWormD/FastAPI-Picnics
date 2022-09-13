from fastapi import APIRouter

from .city.router import router as city_router
from .users.router import router as user_router
from .picnics.router import router as picnic_router


router = APIRouter(
    prefix='/api/v1'
)

router.include_router(city_router)
router.include_router(user_router)
router.include_router(picnic_router)
