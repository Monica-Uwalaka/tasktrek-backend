from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker,Session

from typing import Generator, Any
import os
from dotenv import load_dotenv


load_dotenv()

# use an instance of the URL object instead of a plain string to bypass the need from string parsing
url_object = URL.create(
    drivername=os.getenv("DATABASE_DRIVER"),
    username=os.getenv("DATABASE_USERNAME"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    database=os.getenv("DATABASE_NAME")

)


# create a sqlalchemy engine
engine = create_engine(url_object)

# session establishes all conversations with the database using the engine, ORM unique objects are maintained inside a session
session_maker = sessionmaker(bind=engine)


