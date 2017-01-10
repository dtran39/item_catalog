from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
app = Flask(__name__)


engine = create_engine('sqlite:///item_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    category = session.query(Category).filter_by(name='Snowboarding').first()
    items = session.query(Item).filter_by(category_id=category.id).all()
    return render_template('main.html', items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
