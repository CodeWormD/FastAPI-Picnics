from sqlalchemy.orm import Session
from typing import List, Optional, Union
from db.models import City
from fastapi import HTTPException
from services.external_requests import CheckCityExisting


def get_city(
    db: Session,
    name: str | None = None,
) -> City:
    if name is None:
        raise HTTPException(
            status_code=400,
            detail='Параметр city должен быть указан')
    print(name)
    city = db.query(City).filter(City.name == name.capitalize()).first()

    if city is None:
       raise HTTPException(
            status_code=400,
            detail='Такого города нету в базе')
       

    return {'id': city.id, 'name': city.name, 'weather': city.weather}


def create_city(
    db: Session,
    city: str
) -> City:
    check = CheckCityExisting()
    if check.check_existing(city):
        city = City(name=city)
        db.add(city)
        db.commit()
        db.refresh(city)
        return city
    else:
        raise HTTPException(
            status_code=400,
            detail='Параметр city должен быть существующим городом')



def get_city_list(
    db: Session,
    q: str | None = None
) -> list[City] | City:
    if q:
        return get_city(db, q)
    cities = db.query(City).all()
    return [{'id': city.id, 'name': city.name, 'weather': city.weather} for city in cities]
    