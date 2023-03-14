import datetime
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # importuojame migracijas
from forms import ContactForm

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfgdsdcSAD234221'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)  # Susiejame app ir db.


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    l_name = db.Column(db.String(80),  nullable=False)
    message = db.Column(db.Text)
    data = db.Column(db.DateTime, default=datetime.datetime.now())

    # prie konstruktoriaus irgi nepamirštame pridėti:
    def __init__(self, name, l_name, message):

        self.name = name
        self.l_name = l_name
        self.message = message



    def __repr__(self):
        return f'{self.id}:   {self.name} - {self.l_name}, {self.data}'

@app.route('/')
def index():
    # db.create_all()


    return render_template('index.html')

@app.route('/about')
def pensininkai():

    return render_template('about.html')

@app.route('/peticija', methods=['GET', 'POST'])
def peticija():
    data = Message.query.all()
    form = ContactForm()
    if form.validate_on_submit():
        objektas = Message(form.vardas.data, form.pavarde.data, form.komentaras.data)
        db.session.add_all([objektas])
        db.session.commit()
        return render_template('peticija.html', data=data, form=form)


    return render_template('peticija.html', data=data, form=form)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)