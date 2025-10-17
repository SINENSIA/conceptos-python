import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OMDB_URL = os.getenv("OMDB_URL", "https://www.omdbapi.com/")
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "")

url = f"{OMDB_URL}?apikey={OMDB_API_KEY}&s=Avatar"

response = requests.get(url)

# Guardar el contenido de la respuesta en un archivo JSON
with open("resultado.json", "w") as json_file:
    json.dump(response.json(), json_file, indent=4)

print("El resultado ha sido guardado en 'avatar.json'.")
