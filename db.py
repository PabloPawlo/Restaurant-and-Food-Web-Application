from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

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

def __init__(self, name):
    self.name = name

class ConnectionDB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    food = db.relationship("Food")
    user = db.relationship("User")
    isReady = db.Column(db.String(20))

@app.route('/order')
def show_order():
    userId = request.args.get('userId')
    print(userId)
    #db.session.query(ConnectionDB).filter(ConnectionDB.user_id == 9)

    #s = select([users, addresses]).where( == userId)
    #for row in conn.execute(s):
    #    print(row)
    #(1, u'jack', u'Jack Jone

    return render_template('show_order.html', connections=ConnectionDB.query.all(), foods=Food.query.all(), users=User.query.all())  #.query.filter(ConnectionDB.user_id == userId))

@app.route('/')
def show_all():
    return render_template('show_all.html', foods=Food.query.all(), users=User.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['uname']:
            flash('Please enter all the fields', 'error')
        else:

            flash('Record was successfully added')
            user = User(uname=request.form['uname'])
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            connection = ConnectionDB(user_id=user.id, food_id=food.id, isReady='Nie')
            db.session.add(connection)
            db.session.commit()
            return redirect(url_for('show_order', userId=user.id))
    return render_template('new.html', connections=ConnectionDB.query.all(), foods=Food.query.all(), users=User.query.all())


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