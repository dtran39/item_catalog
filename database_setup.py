# Part 1: Configuration: import modules
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# create instance of declarative base,
#   in order for our class to use sqlalchemy features
Base = declarative_base()
# End beginning configuration
# Part 2: Classes: represent data in python
class Restaurant(Base):
    # Official name of the table in sql
    __tablename__ = 'restaurant'
    # Mapper codes: creates variables used to create columns within our db
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    # nullable = False mean null value is not tolerated
    name =Column(String(80), nullable = False)
    # primary_key = true -> each entry's id is unique
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
# Part 1 in the end:
#   Connects to an existing db (or create a new one)
# A new .db file will be created
engine = create_engine('sqlite:///restaurantmenu.db')
# Go to the db, and add those new tables to it
Base.metadata.create_all(engine)
