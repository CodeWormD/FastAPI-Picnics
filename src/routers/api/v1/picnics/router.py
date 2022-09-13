from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import picnic
from db.database import get_db
from typing import Union, Optional, List

from .schemes import (
    PicnicModel,
    PicnicListModel,
    PicnicRegModel)

router = APIRouter(
    prefix='/picnics',
    tags=['picnics']
)


@router.post('/picnic-add/', summary='Создать пикник', response_model=PicnicModel)
def picnic_create(
    db: Session = Depends(get_db),
    *,
    data: PicnicRegModel
):
    return picnic.create_picnic(db, city_id=data.city_id, time=data.time)


@router.get('/all-picnics/', summary='Все пикники', response_model=list[PicnicListModel])
def picnic_get_all(
    db: Session = Depends(get_db),
):
    return picnic.get_picnic_list(db)


@router.post('/picnic-register/', summary='Регистрация на пикник', response_model=PicnicRegModel)
def picnic_rege(
    db: Session = Depends(get_db),
    *,
    data: PicnicRegModel
):
    return picnic.picnic_reg(db, **data.dict())