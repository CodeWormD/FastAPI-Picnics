from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание сессии
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost/fastapi-picnics"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    except:
        db.close()