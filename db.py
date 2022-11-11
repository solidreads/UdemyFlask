from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# All se realiza por sesiones y las secciones tienen transacciones a las bases de datos
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql://marco:Test123#@localhost:5432/ejemplo")

Session = sessionmaker(bind=engine)
