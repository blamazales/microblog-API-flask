from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha-palavra-chave"

from . import routes