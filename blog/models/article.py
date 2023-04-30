from .database import db
from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime

from .article_tag import article_tag_association_table

class Article(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    title = Column(String(100), nullable=False) 
    text = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __str__(self) -> str:
        return self.title