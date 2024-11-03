from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Bárbara"
    dados = {"profissao": "Técnica", "Idade":29}
    return render_template('index.html', nome=nome, dados=dados)