from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from entity.Media import base

engine: Engine = create_engine(f"sqlite:///.media-manager.db")
session_maker: sessionmaker = sessionmaker()
session_maker.configure(bind=engine)
session: Session = session_maker()

base.metadata.create_all(engine)
