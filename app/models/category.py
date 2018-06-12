import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app import db

class CategoryModel(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    task = relationship("task", back_populates="category")


    def __init__(self, title=None):
        self.title = title