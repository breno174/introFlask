# minha_aplicacao.py

from crypt import methods
from flask import Flask
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Bem vindo ao flask!'

@app.route('/primeira', methods=['GET'])
def primeira_rota():
    user = getenv('DB_USERNAME')
    return {'msg': 'primeira rota', 'user': user}