from sqlalchemy import Column, String, Date
from src.models import Base


class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = {
        'schema': 'mydb'
    }
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    deadline = Column(Date)
    category = Column(String)
