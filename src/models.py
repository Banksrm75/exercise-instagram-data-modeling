import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), unique=False, nullable=False)
    last_name = Column(String(250), unique=False, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    phone_number = Column(String(250), unique=False, nullable=True)
    gender = Column(String(250), unique=False, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=False, nullable=False)
    

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=False, nullable=False)
    body = Column(String(250), unique=False, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
   
class Comments(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    body = Column(String(250), unique=False, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    post_id = Column(Integer, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

class Follows(Base):
    __tablename__ = 'follows'
    
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey('users.id'))
    followed_user_id = Column(Integer, ForeignKey('users.id'))
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
