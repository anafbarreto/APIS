from flask import Flask
from flask import render_template # Para o HTML 

# Manipular as requisições para um endpoint
import urllib.request

# Para exibir o resultado
import json 

## Instancia do Flask
app = Flask(__name__)

""" Rota
@app.route("/")
def hello_world():
    return "Olá, WoMakers!"""

# Incluindo no HTML
@app.route("/")
def get_list_elements_page():
    
     url = "https://rickandmortyapi.com/api/character" 
     response = urllib.request.urlopen(url) 
     data = response.read()
     dict = json.loads(data)
     
     return render_template("characters.html", characters = dict["results"])
    
# Listando elementos de uma busca
@app.route("/lista")
def get_list_elements(): 
    
    url = "https://rickandmortyapi.com/api/character" 
    response = urllib.request.urlopen(url) # Acessando a URL que definimos antes
    character_x = response.read() # Lendo o resultado
    dict_character = json.loads(character_x) # Convertendo o resultado para Json

    characters = [] #Dicionário
    
    for character in dict_character ["results"]:
        character_info = {
       "name": character ["name"],
       "status": character ["status"]
    }
        
    characters.append(character_info) # Adicionando na lista, os resultados das busca

    return {"characters": characters}