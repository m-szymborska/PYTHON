import requests



api_key = "6b4db4ac268f992766f9819115da36d6"

# api url = https://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=6b4db4ac268f992766f9819115da36d6
ENDPO = "https://api.openweathermap.org/data/3.0/onecall"
we_params = {
    "lat": 52.2,
    "lon": 21.0,
    "appid": api_key,
}

response = requests.get(ENDPO, params=we_params)
print(response.status_code)

