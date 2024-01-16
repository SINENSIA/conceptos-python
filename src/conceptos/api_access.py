import requests

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

headers = {
	"X-RapidAPI-Key": "012607e2aamsh5f135f5cf38586ap1f1dbejsna2d4b1f5493e",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}

headers = {
	"X-RapidAPI-Key": "012607e2aamsh5f135f5cf38586ap1f1dbejsna2d4b1f5493e",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/price"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}

headers = {
	"X-RapidAPI-Key": "012607e2aamsh5f135f5cf38586ap1f1dbejsna2d4b1f5493e",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())