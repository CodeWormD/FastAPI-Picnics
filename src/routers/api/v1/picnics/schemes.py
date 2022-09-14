from datetime import datetime

from pydantic import BaseModel

from ..users.schemes import UserModel


class PicnicModel(BaseModel):
    id: int
    city_id: int
    time: datetime

    class Config:
        orm_mode = True


class PicnicListModel(BaseModel):
    id: int
    city_id: int
    time: datetime
    users: list[UserModel] | None = None

    class Config:
        orm_mode = True


class PicnicRegModel(BaseModel):
    user_id: int
    picnic_id: int

    class Config:
        orm_mode = True
