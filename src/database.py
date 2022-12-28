from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://james:foxtrot09er@localhost/fastapi-pizza', echo = True)

Base = declarative_base()

session = sessionmaker()

