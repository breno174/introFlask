# minha_aplicacao.py

from crypt import methods
from flask import Flask, request
from os import getenv


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Bem vindo ao flask!'

@app.route('/primeira', methods=['GET'])
def primeira_rota():
    user = getenv('DB_USERNAME')
    return {'msg': 'primeira rota', 'user': user}


@app.get('/segunda/query_params')
def segunda_rota():
    nome = request.args
    #Para: /segunda/query_params?valor_1=russia&valor_2=ucrania
    #retorna Bem vindo ImmutableMultiDict([('valor_1', 'russia'), ('valor_2', 'ucrania')])!
    if nome:
        return {'msg': f'Bem vindo {nome}!'}
    
    return {'msg': 'Status OK!'}