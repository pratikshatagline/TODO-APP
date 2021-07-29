from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__= 'todo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
