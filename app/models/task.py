import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    category_id = Column(Integer, ForeignKey('category.id'))
    category_title = relationship('category', primaryjoin='task.category_id==category.id', remote_side='category.id', uselist=False)

    def __init__(self, title=None):
        self.title = title