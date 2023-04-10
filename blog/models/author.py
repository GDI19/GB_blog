from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String, Boolean
from sqlalchemy.orm import relationship
from .database import db


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')