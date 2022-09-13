from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional, Union
from db.models import User
from fastapi import HTTPException


def create_user(
    db: Session,
    name: str,
    surname: str,
    age: int
) -> User:
    user = User(
        name=name,
        surname=surname,
        age=age
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_list(
    db: Session,
    min: int,
    max: int,
) -> list[User] | User:
    if  min and max != None:
        return db.query(User).filter((User.age >= min), (User.age <= max)).all()
    elif min != None:
        return db.query(User).filter((User.age >= min)).all()
    elif max != None:
        return db.query(User).filter((User.age <= max)).all()
    else:
        return db.query(User).all()