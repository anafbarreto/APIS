from flask import Flask
from flask import render_template # Para o HTML 
import urllib.request # Manipular as requisições para um endpoint
import json # Para exibir o resultado


app = Flask(__name__) # Instancia do Flask

@app.route('/') # Rota URL raiz
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) # Envia a requisição e recebe a resposta
    data = response.read() # Leitura dos dados
    dict = json.loads(data) # Transforma os dados Json em Py
    
    return render_template("characters.html", characters=dict['results'])

@app.route('/profile/<id>') # Obter um personagem
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+ id #
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    """Para cada url transforma em array e pega o ultimo elemento depois da barra "episode":["https://rickandmortyapi.com/api/episode/1"...]
assim, pega id do episodio e adiciona na lista episodios"""
    list_episodes_ids = [] 
    for episode in dict['episode']:
        episode_id = episode.split("/")[-1]
        list_episodes_ids.append(episode_id)
        
    # pega o id da localização do personagem 
    location_id= dict["location"]["url"].split("/")[-1]
    
    #Converte os elementos da lista para inteiro 
    list_episodes_ids = [int(id) for id in list_episodes_ids]
   
    #Consulta para montar os dados do episodio    
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url) 
    data = response.read()
    episodes_dict = json.loads(data) 
    
    episodes_found = []
    
    for episode in episodes_dict["results"]:
        if episode["id"] in list_episodes_ids:
            episodes_found.append ({
                "id":episode["id"],
            "name":episode["name"],
            "episode":episode["episode"]
        })
            
    # Verifica se não foram encontrados episódios para este personagem
    if not episodes_found:
        error_message = "Não foram encontrados episódios para este personagem."
        return render_template("profile.html", profile=dict, error_message=error_message, location_id=location_id)

    return render_template("profile.html", profile=dict, episodes_found=episodes_found, location_id=location_id)

# Listando elementos de uma busca
@app.route('/lista')
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name":character["name"],
            "status":character["status"]
        }
        
        characters.append(character)
    return {"characters":characters}

@app.route("/locations") # rota de locations
def get_list_locations_page():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)
    
    return render_template("locations.html", locations = dict["results"])

@app.route("/listalocations") # rota da lista de localizações
def get_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url) 
    data = response.read()
    dict = json.loads(data)
    
    locations = []
    
    for location in dict["results"]:
        location = {
            "id":location["id"],
            "name":location["name"],
            "type":location["type"],
            "dimension":location["dimension"],
        }
        locations.append(location);
    
    return {"locations":locations}

@app.route("/location/<id>") # obter uma location
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    location_dict = json.loads(data)
    list_ids = []
    character_names = []
    
    for resident in location_dict["residents"]:
        resident_id = resident.split("/")[-1]
        list_ids.append(resident_id)
        
        # Consulta o nome do personagem pelo id e armazena na lista
        character_url = f"https://rickandmortyapi.com/api/character/{resident_id}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        character_names.append(character_dict["name"])
        
    residents_info = list(zip(list_ids, character_names))
    return render_template("location.html", location=location_dict, residents_info = residents_info)

# Listar Episodios
@app.route("/episodes")
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url) 
    data = response.read()
    episodes_dict = json.loads(data); 
    
    episodes = []
    
    for episode in episodes_dict["results"]:
        episode = {
            "id":episode["id"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "episode":episode["episode"]
        }
        episodes.append(episode)
        
    return render_template("episodes.html", episodes=episodes)

# obter uma location de um episodio
@app.route("/episode/<id>") 
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read()
    episode_dict = json.loads(data)
    list_ids_characters = []
    character_names = []
    
    for character in episode_dict["characters"]:
        character_id = character.split("/")[-1]
        list_ids_characters.append(character_id)
        
        # Consulta o nome do personagem pelo id e armazena na lista
        character_url = f"https://rickandmortyapi.com/api/character/{character_id}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        character_names.append(character_dict["name"])
        
    return render_template("episode.html", episode=episode_dict, list_ids_characters = list_ids_characters, characters_names = character_names)
