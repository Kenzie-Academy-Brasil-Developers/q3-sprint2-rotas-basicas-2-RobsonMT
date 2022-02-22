from flask import Flask, jsonify
from http import HTTPStatus
from tokenize import Number
# from os import getenv

app = Flask(__name__)


@app.get('/')
def home():
   
    mensage = {"data": "Hello Flask!"}

    return mensage ,HTTPStatus.OK


@app.get('/current_datetime')
def current_datetime():

    current_datetime = {
        "current_datetime": "19/02/2022 05:28:19 PM",
        "message": "Boa tarde!"
    }

    return jsonify(current_datetime), HTTPStatus.OK