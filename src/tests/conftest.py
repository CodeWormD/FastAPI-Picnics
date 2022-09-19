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
engine = create_engine(DB_FOR_TEST)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope='package')
def create_app():
    test_app = app
    return test_app


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session_ = SessionTesting(bind=connection)
    yield session_
    session_.close()
    transaction.rollback()
    connection.close()



@pytest.fixture(scope='function')
def client(create_app, db_session):
    def _get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_db
    with TestClient(create_app) as client:
        yield client