
from flask import Flask, request, render_template, redirect, url_for, flash, abort
app = Flask(__name__)
from db import db

# Mostrar tabela completa 
@app.route('/selectAll/', methods=['GET'])
def selectAll():
    select = db.selectByAll().to_json(orient='index')
    return select

# Inserir um contato no DB
@app.route('/insert/', methods=['POST'])
def insert():
    requestData = request.get_json()
    nome = requestData['nome']
    empresa = requestData['empresa']
    numero = requestData['numero']
    email = requestData['email']

    contato = db.Agenda(nome=nome, empresa=empresa, numero=numero, email=email)
    db.insert(contato)

    return '''
           O contato foi salvo.'''


# Deletar por ID
@app.route('/deleteByID/', methods=['DELETE'])
def deleteByID():
    id=request.args.get('id')
    contato = db.deleteById(id)
    return '''excluído com sucesso!'''

# Selecionar por ID
@app.route('/selectByID/', methods=['GET'])
def selectByID():
    id=request.args.get('id')
    contato = db.selectById(id).to_json(orient='index')
    return contato

# Editar por ID
@app.route('/editarByID/', methods=['PUT'])
def editarByID():
    id=request.args.get('id')

    requestData = request.get_json()
    nome = requestData['nome']
    empresa = requestData['empresa']
    numero = requestData['numero']
    email = requestData['email']
    
    contato=db.Agenda(id=id, nome=nome, empresa=empresa, numero=numero, email=email)
    selecao = db.updateById(contato).to_json(orient='index')
    
    return selecao

#Sistema de busca por nome, empresa ou email
@app.route('/agenda/', methods=['GET'])
def busca():
    busca = request.args.get('busca').lower()
    select = db.busca(busca).to_json(orient='index')           
    return select


if __name__ == '__main__':
    app.run(debug=True, port=5000)

