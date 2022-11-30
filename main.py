from flask import Flask, request, json
import json 


app = Flask(__name__)


banco_dados = {"1":{"id": 1, "nome": "Ronaldo", "endereco": "HEXA"}, "2":{"id": 2, "nome": "Kaka", "endereco": "Penta"}, "3":{"id": 3, "nome": "Roger", "endereco": "Tubarao"}}
dados = {"id": 0, "nome": None, "endereco": None}

@app.route('/', methods=['GET'])
def get_home():
    return "Seja bem-vindo"


@app.route('/site', methods=['GET'])
def get_nome():
    return banco_dados

@app.route('/site', methods=['POST'])
def add():
    dados = json.loads(request.data)
    banco_dados[str(dados['id'])] = dados
    return banco_dados


@app.route('/site/<id>', methods=['PUT'])
def update(id):
    dados = json.loads(request.data)
    if str(id) in banco_dados.keys():
        banco_dados[str(id)] = dados
    return banco_dados

@app.route('/site/<id>', methods=['DELETE'])
def delete(id):
    dados = json.loads(request.data)
    if str(id) in banco_dados.keys():
        del banco_dados[str(id)]
    return banco_dados

if __name__ == '__main__':
    app.run()