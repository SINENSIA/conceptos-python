import requests

url = "https://www.omdbapi.com/?apikey=3c969dd7&s=Avatar"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
