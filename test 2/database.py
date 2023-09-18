from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

eng = create_engine("sqlite:///test.db", echo=True)
Base = declarative_base()

Session = sessionmaker(bind=eng, autoflush=True)
