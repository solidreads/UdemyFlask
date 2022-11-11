from flask import Flask, jsonify

from db import engine, Session

from models import Usuario

app = Flask(__name__)

session = Session()


@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return jsonify({"detail": "endpoint desde hola"})


@app.route('/crear-usuario', methods=["POST"])
def crear_usuario():
    with engine.connect() as con:
        nuevo_usuario = Usuario(email="hola1@gmail.com", password="123")
        session.add(nuevo_usuario)
        session.commit()

    return jsonify({"detail": "Usuario creado correctamente"})


if __name__ == '__main__':
    app.run(debug=True)
