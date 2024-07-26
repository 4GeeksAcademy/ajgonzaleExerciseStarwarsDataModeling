import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(300), nullable=False)

class Vehicule(Base):
    __tablename__ = 'vehicule'
    id = Column(Integer, primary_key=True)
    model = Column(String(100))
    weight = Column(DECIMAL)
    year = Column(Integer)
    make = Column(String(100))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    dob = Column(Date)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population_in_millions = Column(Integer)
    terrain = Column(String)

class Favorites(Base) :
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicule_id = Column(Integer, ForeignKey('vehicule.id'))
    planet = relationship(Planet)
    character = relationship(Character)
    vehicule = relationship(Vehicule)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
