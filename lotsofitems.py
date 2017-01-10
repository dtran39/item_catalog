from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///item_catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# clear category tables
session.query(Category).delete()
session.query(Item).delete()
# Adding categories
category_names = ['Soccer', 'Basketball', 'Snowboarding']
categories = {}
for a_category_name in category_names:
    new_category = Category(name=a_category_name)
    categories[a_category_name] = new_category
    session.add(new_category)
    session.commit()
# Adding items
#   Soccer items
soccer_items = [
    {'name': 'Cleats', 'description': 'a new pair of cleats'},
    {'name': 'Shinguard', 'description': 'Shin guard protects your shin'},
    {'name': 'Jersey', 'description': 'The jersey of your favourite club'}
]
#   Basketball items
basketball_items = [
    {'name': 'Basketball', 'description': 'Ball for the game'}
]
# Snowboarding items
snowboarding_items = [
    {'name': 'Snowboard', 'description': 'a snowboard'},
    {'name': 'Googles', 'description': 'Protect your eyes'}
]
#
items = {
    'Soccer': soccer_items,
    'Basketball': basketball_items,
    'Snowboarding': snowboarding_items
}
for a_category_name in items:
    category_object = categories[a_category_name]
    category_items = items[a_category_name]
    for an_item in category_items:
        new_item = Item(name=an_item['name'], description=an_item['description'],
                        category=category_object)
        session.add(new_item)
        session.commit()
print "Finish adding categories and items"
