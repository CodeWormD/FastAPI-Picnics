from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from crud import user
from db.database import get_db
from .schemes import RegisterUserRequest, UserModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/register-user/',
             summary='Создать пользователя',
             response_model=UserModel)
def register_user(
    db: Session = Depends(get_db),
    *,
    data: RegisterUserRequest
):
    return user.create_user(db, **data.dict())


@router.get('/users-list/',
            summary='Список пользователей',
            response_model=list[UserModel] | UserModel)
def list_users(
    db: Session = Depends(get_db),
    min_age: int = Query(None),
    max_age: int = Query(None),

):
    return user.get_user_list(db, min_age, max_age)
