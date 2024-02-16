from flask import Flask 

## Instancia do Flask
app = Flask(__name__)

## Rota
@app.route('/')
def hello_world():
    return "Olá, WoMakers!"