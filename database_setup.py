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
class Category(Base):
    # Official name of the table in sql
    __tablename__ = 'category'
    # Mapper codes: creates variables used to create columns within our db
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Item(Base):
    __tablename__ = 'item'
    # primary_key = true -> each entry's id is unique
    id = Column(Integer, primary_key = True)
    # nullable = False mean null value is not tolerated
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
# Part 1 in the end:
#   Connects to an existing db (or create a new one)
# A new .db file will be created
engine = create_engine('sqlite:///item_catalog.db')
# Go to the db, and add those new tables to it
Base.metadata.create_all(engine)
