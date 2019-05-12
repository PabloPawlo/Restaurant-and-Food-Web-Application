from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class foods(db.Model):
    id = db.Column('food_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    time = db.Column(db.String(50))
    isReady = db.Column(db.String(200))



def __init__(self, name, time, isReady):
    self.name = name
    self.time = time
    self.isReady = isReady


@app.route('/')
def show_all():
    return render_template('show_all.html', foods=foods.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['time'] or not request.form['isReady']:
            flash('Please enter all the fields', 'error')
        else:
            food = foods(name = request.form['name'],time = request.form['time'],isReady = request.form['isReady'])

            db.session.add(food)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)