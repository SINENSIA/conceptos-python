import requests
from dotenv import load_dotenv
import os

load_dotenv()

coinrankin_host = os.getenv('COINRANKING_HOST')
url = f"https://{ coinrankin_host }/coins"

querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h",
               "tiers[0]": "1", "orderBy": "marketCap", "orderDirection": "desc", "limit": "50", "offset": "0"}

headers = {
    "X-RapidAPI-Key": os.getenv('RAPIDAPI_TOKEN'),
    "X-RapidAPI-Host": os.getenv('COINRANKING_HOST')
}

response = requests.get(url, headers=headers, params=querystring)

response_data = response.json()

bitcoin_id = [x['uuid']
              for x in response_data['data']['coins'] if x['symbol'] == 'BTC'][0]

print("El id de Bitcoin es:", bitcoin_id)

"""
Con gran volumen de datos es preferible, ya que la compresión de lista 
siempre recorre toda la lista coins, incluso si BTC está al principio. Por 
el contrario el bucle se para cuando se encuentra BTC:

bitcoin_id = None
for coin in response_data['data']['coins']:
    if coin['symbol'] == 'BTC':
        bitcoin_id = coin['uuid']
        break
"""

url = f"https://{ coinrankin_host }/coin/{bitcoin_id}"

querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h"}

headers = {
    "X-RapidAPI-Key": "012607e2aamsh5f135f5cf38586ap1f1dbejsna2d4b1f5493e",
    "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

bitcoin = response.json()
print(type(bitcoin))
print(bitcoin['data']['coin']['sparkline'])

url = f"https://{ coinrankin_host }/coin/{bitcoin_id}/price"

querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl"}

headers = {
    "X-RapidAPI-Key": "012607e2aamsh5f135f5cf38586ap1f1dbejsna2d4b1f5493e",
    "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()['data']
print(data)
print("Precio actual de Bitcoin en $: ", round(float(data['price']), 0))
