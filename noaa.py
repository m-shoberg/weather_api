import requests

url = "https://api.weather.gov/gridpoints/SEW/117,51/forecast"

headers={
}

response = requests.request("GET", url,)

print(response.text)