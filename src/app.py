from flask import Flask

from flask_keystone import FlaskKeystone

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__": 
    # pragma: nocover
    app1 = FlaskKeystone(app)
    #app = app1.init_app(app)
    #app = app.init_app()
    app.run(host="0.0.0.0", port=8080)
