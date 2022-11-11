import json

from flask import Flask, jsonify, request

from db import engine, Session

from models import Usuario

app = Flask(__name__)

session = Session()


@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return jsonify({"detail": "endpoint desde hola"})


@app.route('/crear-usuario', methods=["POST"])
def crear_usuario():
    data = json.loads(request.data)
    if 'email' not in data:
        return jsonify({"respuesta": "No estas enviando el username"})
    if 'password' not in data:
        return jsonify({"respuesta": "No estas enviando el password"})

    if len(data["email"]) == 0:
        return jsonify({"respuesta": "Username no puede estar vacio"})

    if len(data["password"]) == 0:
        return jsonify({"respuesta": "Password no puede estar vacio"})

    with engine.connect() as con:

        nuevo_usuario = Usuario(email=data["email"], password=data["password"])
        session.add(nuevo_usuario)
        try:
            session.commit()
        except:
            return jsonify({"detail": "El usuario ya fue creado"})

    return jsonify({"detail": "Usuario creado correctamente"})


if __name__ == '__main__':
    app.run(debug=True)
