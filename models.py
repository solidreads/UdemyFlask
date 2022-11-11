from sqlalchemy import Column, String, Integer
from db import Base, engine


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(70), unique=True)
    password = Column(String(70))


Base.metadata.create_all(engine)
