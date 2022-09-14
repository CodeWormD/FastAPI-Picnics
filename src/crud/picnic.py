from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from db.models import Picnic, PicnicRegistration, User


def create_picnic(
    db: Session,
    city_id: int,
    time: datetime,
) -> Picnic:
    picnic = Picnic(city_id=city_id, time=time)
    db.add(picnic)
    db.commit()
    db.refresh(picnic)
    return picnic


# надо переписать и сформировать ответ вручную под шаблон схемы
def get_picnic_list(
    db: Session,
) -> list[Picnic]:
    ab = (db.query(Picnic).options(joinedload(Picnic.users).joinedload(PicnicRegistration.user))
            .filter((PicnicRegistration.user_id == User.id)
                    & (PicnicRegistration.picnic_id == Picnic.id))
            .all())
    return ab


def picnic_reg(
    db: Session,
    user_id: int,
    picnic_id: int,
) -> PicnicRegistration:
    pic_reg = PicnicRegistration(user_id=user_id, picnic_id=picnic_id)
    db.add(pic_reg)
    db.commit()
    db.refresh(pic_reg)
    return pic_reg
