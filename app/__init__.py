
from .get_current_date_time import get_current_date_time
from flask import Flask,request
from http import HTTPStatus


app = Flask(__name__)

@app.get('/')
def home():
   
    mensage = {"data": "Hello Flask!"}

    return mensage ,HTTPStatus.OK


@app.get('/current_datetime')
def current_datetime():

    current_datetime = get_current_date_time()

    return current_datetime ,HTTPStatus.OK