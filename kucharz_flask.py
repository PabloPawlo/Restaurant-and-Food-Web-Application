from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    time = db.Column(db.String(50))


def __init__(self, name, time):
    self.name = name
    self.time = time


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20))


def __init__(self, uname):
    self.uname = uname


class ConnectionDB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    food = db.relationship("Food")
    user = db.relationship("User")
    isReady = db.Column(db.String(20))


@app.route('/order')
def order():
    userId = request.args.get('userId')

    print(userId)
    #db.session.query(ConnectionDB).filter(ConnectionDB.user_id == 9)

    #s = select([users, addresses]).where( == userId)
    #for row in conn.execute(s):
    #    print(row)
    #(1, u'jack', u'Jack Jone
    q = db.session.query(ConnectionDB).join(User).filter(ConnectionDB.user_id==userId).all()
    q2 = db.session.query(User.uname).filter(User.id==userId).all()
    qpa = db.session.query(Food).join(User, ConnectionDB.user_id==userId).join(ConnectionDB, Food.id == ConnectionDB.food_id).filter().all()

    return render_template('show_order.html', connections = q,qonnections = qpa, users=q2 )


@app.route('/')
def show_all():
    #q = db.session.query(User.uname, Food.name).join(ConnectionDB.user_id == User.id and ConnectionDB.food_id==Food.id).all()
    q = db.session.query(ConnectionDB)\
        .join(Food, ConnectionDB.food_id == Food.id)\
        .join(User, ConnectionDB.user_id == User.id)\
        .all()

    return render_template('show_all.html', connections=q)











@app.route('/post_order', methods=['POST'])
def post_order():
    data = request.get_json()

    user = User(uname=data['name'])
    db.session.add(user)
    db.session.commit()

    for food_id in data['tab']:
        print(food_id)
        connection = ConnectionDB(user_id=user.id, food_id=food_id, isReady='Nie')
        db.session.add(connection)
    db.session.commit()
    return redirect(url_for('order', userId=user.id))


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:

            flash('Record was successfully added')
            user = User(name=request.form['name'])
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            connection = ConnectionDB(user_id=user.id, food_id=food.id, isReady='Nie')
            db.session.add(connection)
            db.session.commit()
            return redirect(url_for('tak', userId=user.id))
    return render_template('new.html', foods=Food.query.all())


if __name__ == '__main__':

    db.drop_all()
    db.create_all()
    food = Food(name='Chicken', time='15min')
    db.session.add(food)
    food2 = Food(name='Potato Chips', time='10min')
    db.session.add(food2)
    food3 = Food(name='Cola', time='1min')
    db.session.add(food3)
    food4 = Food(name='Soup', time='10min')
    db.session.add(food4)
    db.session.commit()
    app.run(debug=True)