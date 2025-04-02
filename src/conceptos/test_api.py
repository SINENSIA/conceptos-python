import requests
import json

url = "https://www.omdbapi.com/?apikey=b50f00d8&s=Avatar"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Guardar el contenido de la respuesta en un archivo JSON
with open("resultado.json", "w") as json_file:
    json.dump(response.json(), json_file, indent=4)

print("El resultado ha sido guardado en 'avatar.json'.")
