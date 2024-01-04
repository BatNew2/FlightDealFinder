import requests
HEADER = {
    "apikey": "RtZv8SYl0Xezf2egd8gYBkgwT7o6tSg_"
}
query = {
    "fly_from": "CGK",
    "fly_to": "NYC",
    "date_from": f"11/6/2024",
    "date_to": f"11/3/2024",
    "max_stopovers": 0,
    "limit": 2
}
response = requests.get("https://api.tequila.kiwi.com/v2/search/", headers=HEADER, params=query)
response.raise_for_status()
data = response.json()
print(f"{data['data'][0]['price']}, {data['data'][0]['deep_link']}")