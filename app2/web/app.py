from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

@app.route('/')
def index():
  db.create_all()
  greeted = User.query.first()
  if greeted:
    return f"Hej - velkommen tilbage {greeted.name}"
  else:
    return f"Hej"

@app.route('/user/<name>')
def greet(name):
  new_user = User(name=name)
  db.session.add(new_user)
  db.session.commit()
  return f"Hej {name} - velkommen!"



if __name__ == '__main__':
  app.run("0.0.0.0", port=8000)