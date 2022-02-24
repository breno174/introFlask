# minha_aplicacao.py

from crypt import methods
from flask import Flask, jsonify, request
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

    req = request.args
    nome = request.args.get('nome')
    #Para: /segunda/query_params?valor_1=russia&valor_2=ucrania
    #retorna -> "Bem vindo ImmutableMultiDict([('valor_1', 'russia'), ('valor_2', 'ucrania')])!"

    #se nos parametros estiver o argumentos 'nome', ele retorna com esse valor
    #Ex -> "Bem vindo Russia!"
    if nome:
        return {'msg': f'Bem vindo {nome}!'}
    elif req:
        return {'msg': f'Bem vindo {req}!'}
    
    return {'msg': 'Status OK!'}


#@app.get("/courses/<course_id>") -> dessa forma receve qualquer parametro
@app.get("/courses/<int:course_id>") #-> dessa forma só aceita receber inteiros
def get_course(course_id):
    """
        Lógica interna para busca do curso e suas funcionalidades,
        utilizando a variável course_id que vem da url
    """

    # Retorno dos dados do curso
    return {"id_curso": course_id}


@app.route("/users/<int:id>/edit", methods=["GET"])
def route_edit_user(id):
    msg = "You want to edit the user with ID: {} | Arg type: {}".format(id, type(id))
    print(msg)
    # -> "You want to edit the user with ID: 14 | Arg type: <class 'int'>"
    return jsonify(msg)