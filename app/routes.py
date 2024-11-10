from app import app
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

if __name__=='main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)
    
@app.route('/')
@app.route('/index', defaults={"nome":"usuário"})
@app.route('/index/<nome>/<profissao>/<idade>')
def index(nome, profissao, idade):
    dados = {"profissao": profissao, "Idade": idade}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    if usuario == 'admin' and senha ==  'senha123':
        return "usuario: {} e senha: {}".format(usuario,senha)
    else:
        flash("Dados inválidos") 
        flash("Login ou senha inválidos") 
        return redirect('/login')