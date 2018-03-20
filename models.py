from sqlalchemy import ForeignKey, Column, String, Integer, Boolean
from sqlalchemy import true as db_true
from sqlalchemy import false as db_false
from sqlalchemy.event import listens_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db import db

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(db.Integer(), primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    password = Column(String(80), nullable=False, default="")
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True, server_default=db_true())
    is_admin = Column(Boolean, nullable=False, default=True, server_default=db_false())

    def __str__(self):
        return self.userid


class Videos(Base):
    __tablename__ = "videos"
    id = Column(db.Integer(), primary_key=True)
    title = Column(String(255))
    description = Column(String(4032))
    userid = Column(String(255), ForeignKey('users.id'))
    user = relationship("Users", foreign_keys=[userid])
    path = Column(String(400), nullable=False)


class Comments(Base):
    __tablename__ = "comments"
    id = Column(db.Integer(), primary_key=True)
    userid = Column(String(255), ForeignKey('users.id'))
    videoid = Column(String(255), ForeignKey('videos.id'))
    user = relationship("Users", foreign_keys=[userid])
    video = relationship("Videos", foreign_keys=[videoid])
    text = Column(String(4096))