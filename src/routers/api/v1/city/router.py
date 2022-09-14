from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from crud import city
from db.database import get_db

from .schemes import CityResponseScheme, CreateCityScheme

router = APIRouter(
    prefix='/city',
    tags=['city']
)


@router.get('/', summary='Get City', response_model=CityResponseScheme)
def get_city(
    db: Session = Depends(get_db),
    *,
    name: str = Query(description="Название города")
):
    """
    Получение города
    """
    return city.get_city(
        db,
        name
    )


@router.post(
    '/create/',
    summary='Create City',
    description='Создание города по его названию',
    response_model=CityResponseScheme)
def create_city(
    db: Session = Depends(get_db),
    *,
    data: CreateCityScheme
):
    """
    Создание города
    """
    return city.create_city(
        db,
        city=data.name
    )


@router.get('/get-cities/',
            summary='Get single or list of Cities',
            response_model=list[CityResponseScheme] | CityResponseScheme)
def get_city_all(
    q: str | None = None,
    db: Session = Depends(get_db),
):
    """
    Получение списка городов
    """
    return city.get_city_list(db, q)
