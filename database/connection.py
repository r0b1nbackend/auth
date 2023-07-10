from sqlmodel import SQLModel,create_engine,Session
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
engine_url = create_engine(database_connection_string,echo=True,connect_args={"check_same_thread":False})


def conn():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session