import os

from dotenv import load_dotenv
from .log import add_log
from .database import create_database_if_not_exists
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(os.getenv("CLOCKIFY_ENV"))

VACATION_URL = os.getenv("DATABASE_URL_VACATION")
engine_2 = create_engine(VACATION_URL)
BaseVacation = declarative_base()
SessionLocal_2 = sessionmaker(autocommit=False, autoflush=False, bind=engine_2)


class Vacation(BaseVacation):
    __tablename__ = "vacation"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String)
    username = Column(String)
    clockify_id = Column(String)
    routine_shift = Column(String)
    vdate = Column(String)
    hours = Column(String)
    confirmed_by = Column(String)

    def __repr__(self):
        return f"User('{self.username}') - VacationDate('{self.vdate}' - RoutineVacation('{self.routine_vacation}'))"


def init_vacation_db(bot):
    create_database_if_not_exists(VACATION_URL, bot)
    try:
        BaseVacation.metadata.create_all(engine_2)
    except Exception as e:
        add_log(f"Error creating Vacation table: {e}")
