from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello world"

@app.route('/user/<name>')
def greet(name):
  return f"Hej {name} - velkommen!"



if __name__ == '__main__':
  app.run("0.0.0.0", port=8000)