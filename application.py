from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
app = Flask(__name__)


engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all categories
@app.route('/')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', items=categories)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
