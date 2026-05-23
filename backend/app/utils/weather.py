import requests

API_KEY = "0ba4104d02124697a3d94610262305"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)
    data = response.json()

    return {
        "temperature": data["current"]["temp_c"],
        "rainfall": data["current"]["precip_mm"]
    }