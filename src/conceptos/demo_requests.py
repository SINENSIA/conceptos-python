import requests
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Acceder a las variables
api_key = os.getenv('API_KEY')
api_url = os.getenv('API_URL')

url = f"{api_url}/models"

payload = {}
headers = {
  'Authorization': f'Bearer {api_key}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)