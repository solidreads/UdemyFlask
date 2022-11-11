pip install virtualenv
virtualenv env


pip install flask
pip install sqlalchemy

Estructura
from Flask import Flask

from flask import Flask

app = Flask(__name__)





if __name__ == "__main__":
    app.run(debug=True)