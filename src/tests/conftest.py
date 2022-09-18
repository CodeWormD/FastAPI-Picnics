import os
import sys
import pytest
from fastapi import FastAPI
from typing import Any
from typing import Generator
from fastapi.testclient import TestClient
from main import app
from db.models import Base
from db.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy.orm import close_all_sessions


DB_FOR_TEST = "postgresql://postgres:1@localhost/fastapi-picnics_test"
engine = create_engine(
    DB_FOR_TEST, connect_args={"check_same_thread": False}
)
# Use connect_args parameter only with sqlite
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)



@pytest.fixture(scope="function")
def db():
    dburl = DB_FOR_TEST

    if database_exists(dburl):
        drop_database(dburl)
    
    create_engine(dburl)
    create_database(dburl)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "src\\alembic.ini"))
    command.upgrade(alembic_cfg, "head")
    yield
    close_all_sessions()
    drop_database(dburl)

app.dependency_overrides[get_db] = db

@pytest.fixture()
def client(db) -> Generator:
    app.dependency_overrides[get_db] = db
    with TestClient(app) as client:
        yield client