from app import app
from flask import render_template
import os

if __name__=='main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)
    
@app.route('/')
@app.route('/index')
def index():
    nome = "Bárbara"
    dados = {"profissao": "Técnica", "Idade":29}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')